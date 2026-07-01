// W3 — lead-router: on a new lead / registration / subscriber, notify MS Teams
// and open an Asana task. Triggered by a Supabase Database Webhook (INSERT on
// public.leads, public.webinar_registrations, public.subscribers).
//
// Company IP — set these as Supabase Function secrets (NOT in this file):
//   supabase secrets set TEAMS_WEBHOOK_URL="https://<tenant>.webhook.office.com/..."
//   supabase secrets set ASANA_TOKEN="1/xxxx…"          (Asana Personal Access Token or service account)
//   supabase secrets set ASANA_PROJECT_GID="1200…"      (target project)
//   supabase secrets set ASANA_SECTION_GID="1200…"      (optional: target section)
// Deploy:  supabase functions deploy lead-router --no-verify-jwt

interface WebhookPayload {
  type: string;            // "INSERT"
  table: string;           // leads | webinar_registrations | subscribers
  record: Record<string, unknown>;
}

const TEAMS = Deno.env.get("TEAMS_WEBHOOK_URL");
const ASANA_TOKEN = Deno.env.get("ASANA_TOKEN");
const ASANA_PROJECT = Deno.env.get("ASANA_PROJECT_GID");
const ASANA_SECTION = Deno.env.get("ASANA_SECTION_GID");

function label(table: string) {
  if (table === "webinar_registrations") return "Webinar registration";
  if (table === "subscribers") return "Newsletter subscriber";
  return "Website lead";
}

async function notifyTeams(title: string, rec: Record<string, unknown>) {
  if (!TEAMS) return;
  const facts = Object.entries(rec)
    .filter(([k]) => !["id", "created_at", "consent"].includes(k))
    .map(([k, v]) => ({ name: k, value: String(v ?? "") }));
  const card = {
    "@type": "MessageCard",
    "@context": "https://schema.org/extensions",
    summary: title,
    themeColor: "334b60",
    title,
    sections: [{ facts }],
  };
  await fetch(TEAMS, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(card),
  }).catch(() => {});
}

async function createAsanaTask(title: string, rec: Record<string, unknown>) {
  if (!ASANA_TOKEN || !ASANA_PROJECT) return;
  const notes = Object.entries(rec)
    .map(([k, v]) => `${k}: ${v ?? ""}`)
    .join("\n");
  const data: Record<string, unknown> = {
    name: title,
    notes,
    projects: [ASANA_PROJECT],
  };
  const res = await fetch("https://app.asana.com/api/1.0/tasks", {
    method: "POST",
    headers: { Authorization: `Bearer ${ASANA_TOKEN}`, "Content-Type": "application/json" },
    body: JSON.stringify({ data }),
  }).catch(() => null);
  // optional: move into a section
  if (res && res.ok && ASANA_SECTION) {
    const created = await res.json().catch(() => null);
    const gid = created?.data?.gid;
    if (gid) {
      await fetch(`https://app.asana.com/api/1.0/sections/${ASANA_SECTION}/addTask`, {
        method: "POST",
        headers: { Authorization: `Bearer ${ASANA_TOKEN}`, "Content-Type": "application/json" },
        body: JSON.stringify({ data: { task: gid } }),
      }).catch(() => {});
    }
  }
}

Deno.serve(async (req) => {
  try {
    const payload = (await req.json()) as WebhookPayload;
    const rec = payload.record || {};
    const who = (rec.name as string) || (rec.email as string) || "unknown";
    const title = `${label(payload.table)}: ${who}`;
    await Promise.all([notifyTeams(title, rec), createAsanaTask(title, rec)]);
    return new Response(JSON.stringify({ ok: true }), {
      headers: { "Content-Type": "application/json" },
    });
  } catch (e) {
    return new Response(JSON.stringify({ ok: false, error: String(e) }), {
      status: 400,
      headers: { "Content-Type": "application/json" },
    });
  }
});
