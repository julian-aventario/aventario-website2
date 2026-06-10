# Go live: HubSpot → Supabase + Cal.com

The website is fully switched off HubSpot and wired to **your** Supabase project
(`zpuywttjadohtxvaloyq`) with the publishable key. Two small things left.

## Ignore the Next.js quickstart Supabase showed you
That screen (npm install, `@supabase/ssr`, middleware, `client.ts`/`server.ts`) is for a
**Next.js** app. Our site is plain static HTML — none of it applies. The only things we
needed were the **project URL** and the **publishable key**, and both are already in the code.

## 1. Create the table — the one required step (~30 sec)
Supabase Dashboard → your project → **SQL Editor → New query** → paste the contents of
[`supabase/schema.sql`](supabase/schema.sql) → **Run**.

That's it. The contact form and the whitepaper gate start writing into the `leads` table
the moment this runs. See submissions in **Table editor → leads**.

## 2. Cal.com (booking) — replaces the HubSpot scheduler
Create a free account at https://cal.com (use **cal.eu** for EU-hosted data), make a 30-min
intro event, and send me the link (`https://cal.com/<username>/<event>`). I'll drop it into
the "Book a call" box on the contact page. Until then I won't deploy that box — an unset
link would show an empty embed.

## Rename the project (optional)
I can't log into your Supabase account from here, but renaming is two clicks:
Dashboard → your project → **Settings → General → Project name** → `Aventario Live` → Save.
You mentioned a second project — make sure `zpuywttjadohtxvaloyq` is the keeper.

## How it works / security
- Forms insert straight into Supabase from the browser using the **publishable** key. That
  key is meant to be public; RLS is **insert-only**, so nobody can read the lead list through
  it — leads are visible only to you in the dashboard.
- **Fail-safe:** if Supabase is ever unreachable, the contact form falls back to email and
  the whitepaper still downloads. No lead or visitor is lost.
- **Spam:** a public insert form can be hit by bots. If that happens I'll add a free
  Cloudflare Turnstile check.
- `datenschutz.html` now names Supabase (EU, Frankfurt) + Cal.com instead of HubSpot — that's
  legal copy, give it a glance before deploy.
