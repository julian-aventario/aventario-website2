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
