// Vercel Cron keepalive + health check (ESM — the project's package.json is type:module).
// The Supabase free tier auto-pauses a project after 7 days with no requests.
// This function makes a real database request so the project stays counted as
// active, and reports Supabase reachability on each run (visible in the Vercel
// function logs). Scheduled every 5 days in vercel.json.
export default async function handler(req, res) {
  const SB = 'https://zpuywttjadohtxvaloyq.supabase.co';
  // Publishable key — safe to ship (it is already public in the site's form JS).
  const KEY = process.env.SUPABASE_PUBLISHABLE_KEY || 'sb_publishable_0R1ZCaygbhIA4xY3MhpN6w_qOFeRhoa';
  const started = Date.now();
  // W5: alert MS Teams if the health check fails (env-gated — set TEAMS_WEBHOOK_URL to enable).
  const TEAMS = process.env.TEAMS_WEBHOOK_URL;
  async function alertTeams(text) {
    if (!TEAMS) return;
    try {
      await fetch(TEAMS, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ text }) });
    } catch (_) {}
  }
  try {
    // A real PostgREST query touches the database, which is what resets the
    // inactivity timer. RLS may return an empty set; the request still counts.
    const r = await fetch(SB + '/rest/v1/leads?select=id&limit=1', {
      headers: { apikey: KEY, Authorization: 'Bearer ' + KEY },
    });
    // 200/400/401/404 are normal API responses = the project is serving.
    // A paused or unreachable project returns 5xx or throws.
    const alive = [200, 400, 401, 404].includes(r.status);
    const body = {
      ok: alive,
      service: 'supabase-keepalive',
      supabaseStatus: r.status,
      ms: Date.now() - started,
      ts: new Date().toISOString(),
    };
    console.log('[keepalive]', JSON.stringify(body));
    if (!alive) await alertTeams('Aventario Supabase health check FAILED (status ' + r.status + '). Forms may be down.');
    res.status(alive ? 200 : 503).json(body);
  } catch (e) {
    const body = {
      ok: false,
      service: 'supabase-keepalive',
      error: String((e && e.message) || e),
      ms: Date.now() - started,
      ts: new Date().toISOString(),
    };
    console.error('[keepalive] FAILED', JSON.stringify(body));
    await alertTeams('Aventario Supabase keepalive threw: ' + body.error + '. Project may be paused.');
    res.status(503).json(body);
  }
}
