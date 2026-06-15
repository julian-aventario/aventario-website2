-- Aventario website — lead capture schema for Supabase.
-- Run once: Supabase Dashboard -> SQL Editor -> New query -> paste -> Run.
--
-- The website inserts leads from the browser using the PUBLISHABLE key (safe to expose).
-- RLS is ON with an INSERT-ONLY policy: the public can add a lead but can never read,
-- update, or delete the table. You view leads in Dashboard -> Table editor -> leads.

create extension if not exists "pgcrypto";

create table if not exists public.leads (
  id          uuid primary key default gen_random_uuid(),
  created_at  timestamptz not null default now(),
  type        text not null default 'contact',   -- contact | whitepaper | newsletter | webinar
  name        text,
  email       text not null,
  company     text,
  message     text,
  source      text,                               -- which page/form submitted it
  consent     boolean not null default false,
  user_agent  text
);

create index if not exists leads_created_at_idx on public.leads (created_at desc);
create index if not exists leads_type_idx       on public.leads (type);

alter table public.leads enable row level security;

-- Allow anonymous INSERT only (the browser submits with the publishable/anon key).
-- No SELECT/UPDATE/DELETE policy => the public can add a lead but never read the table.
drop policy if exists "Public can submit a lead" on public.leads;
create policy "Public can submit a lead"
  on public.leads
  for insert
  to anon
  with check (true);

-- Webinar registrations (webinar.html). Same insert-only RLS pattern.
create table if not exists public.webinar_registrations (
  id          uuid primary key default gen_random_uuid(),
  created_at  timestamptz not null default now(),
  name        text,
  email       text not null,
  company     text,
  consent     boolean not null default false,
  webinar     text,
  source      text
);
alter table public.webinar_registrations enable row level security;
grant insert on public.webinar_registrations to anon;
drop policy if exists "Public can register for a webinar" on public.webinar_registrations;
create policy "Public can register for a webinar"
  on public.webinar_registrations
  for insert
  to anon
  with check (true);

-- IMPORTANT: the browser sends the publishable key as the `apikey` header ONLY.
-- Do NOT also send `Authorization: Bearer <publishable key>`. The new sb_publishable_
-- keys are not JWTs; sending one as a Bearer token breaks role resolution and trips RLS.

-- ---------------------------------------------------------------------------
-- Email notification on every new submission (via pg_net -> Resend).
-- Sends to julian.robida@aventario.com. The Resend key is injected at deploy
-- time (kept out of git) — replace <RESEND_API_KEY> before running, or apply via
-- the management API. The body is wrapped in an exception guard so a failed
-- email can NEVER roll back / block the lead insert.
-- To email a shared inbox or the team (not just the account owner) and send from
-- leads@aventario.com, verify aventario.com at resend.com/domains (adds ~3 DNS records).
-- ---------------------------------------------------------------------------
create extension if not exists pg_net;

create or replace function public.notify_new_submission()
returns trigger language plpgsql security definer
set search_path = public, net, extensions
as $fn$
declare payload jsonb := to_jsonb(NEW);
begin
  begin
    perform net.http_post(
      url := 'https://api.resend.com/emails',
      headers := jsonb_build_object('Content-Type','application/json','Authorization','Bearer <RESEND_API_KEY>'),
      body := jsonb_build_object(
        'from','Aventario Leads <onboarding@resend.dev>',
        'to', jsonb_build_array('julian.robida@aventario.com'),
        'subject','New '||TG_TABLE_NAME||': '||coalesce(payload->>'name', payload->>'email', '(no name)'),
        'html',
          '<h2 style="font-family:sans-serif">New submission ('||TG_TABLE_NAME||')</h2>'||
          '<table style="font-family:sans-serif;font-size:14px;border-collapse:collapse">'||
          (select string_agg('<tr><td style="padding:3px 12px;vertical-align:top"><b>'||key||'</b></td><td style="padding:3px 12px">'||coalesce(value,'-')||'</td></tr>','' order by key)
             from jsonb_each_text(payload) where key <> 'id')||
          '</table>'
      )
    );
  exception when others then null;  -- a failed email must never roll back the insert
  end;
  return NEW;
end;
$fn$;

drop trigger if exists trg_notify_leads on public.leads;
create trigger trg_notify_leads after insert on public.leads
  for each row execute function public.notify_new_submission();

drop trigger if exists trg_notify_webinar on public.webinar_registrations;
create trigger trg_notify_webinar after insert on public.webinar_registrations
  for each row execute function public.notify_new_submission();
