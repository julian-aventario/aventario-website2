-- Workflow upgrades — database setup. Run once (Supabase SQL editor or MCP).

-- W1: newsletter subscribers -----------------------------------------------
create table if not exists public.subscribers (
  id uuid primary key default gen_random_uuid(),
  email text not null unique,
  source text,
  consent boolean default true,
  utm_source text, utm_medium text, utm_campaign text, utm_term text, utm_content text,
  gclid text, referrer text, landing_page text,
  created_at timestamptz default now()
);
alter table public.subscribers enable row level security;

-- Anonymous (publishable key) may insert only, same pattern as leads.
drop policy if exists "anon insert subscribers" on public.subscribers;
create policy "anon insert subscribers" on public.subscribers
  for insert to anon with check (true);

-- W3: route every new lead / registration / subscriber to Teams + Asana.
-- A Database Webhook (Dashboard: Database > Webhooks) on INSERT for
-- public.leads, public.webinar_registrations and public.subscribers should
-- call the `lead-router` Edge Function. Equivalent SQL trigger if you prefer
-- pg_net over the dashboard webhook:
--
--   create trigger route_new_lead after insert on public.leads
--     for each row execute function supabase_functions.http_request(
--       'https://<project>.functions.supabase.co/lead-router',
--       'POST', '{"Content-Type":"application/json"}', '{}', '1000');
--
-- (repeat for webinar_registrations and subscribers)
