# Workflow upgrades — activation steps

The frontend and function code are shipped. Three activation steps remain, split by who owns the credential.

## 1. Database (needs the Supabase login / OAuth)
Run `supabase/wf_setup.sql` once (Supabase SQL editor, or I can run it via the Supabase MCP once you finish the OAuth). It creates the `subscribers` table with an anon-insert policy. Until this runs, the newsletter forms post but the row is rejected.

## 2. Lead routing to Teams + Asana (company IP)
The `supabase/functions/lead-router` Edge Function posts each new lead/registration/subscriber to MS Teams and opens an Asana task. It reads company secrets, so nothing sensitive is in the repo.

```
supabase functions deploy lead-router --no-verify-jwt
supabase secrets set TEAMS_WEBHOOK_URL="https://<tenant>.webhook.office.com/webhookb2/..."
supabase secrets set ASANA_TOKEN="1/xxxxxxxx"          # Asana PAT or service account
supabase secrets set ASANA_PROJECT_GID="1200xxxxxxxx"  # target Asana project
supabase secrets set ASANA_SECTION_GID="1200xxxxxxxx"  # optional
```
Then add Database Webhooks (Supabase Dashboard > Database > Webhooks) on INSERT for `leads`, `webinar_registrations`, `subscribers`, all pointing at the `lead-router` function.

To get the two company credentials:
- **Teams webhook:** in the target Teams channel > Connectors > Incoming Webhook > create > copy the URL.
- **Asana token:** Asana > Settings > Apps > Developer > Personal Access Token (or a service account), plus the project GID from the project URL.

## 3. Teams alert on outage (company IP)
Set the same Teams webhook as a Vercel env var so the keepalive health check can alert if Supabase ever fails:
```
Vercel > project > Settings > Environment Variables > TEAMS_WEBHOOK_URL = <same URL>
```

All three are gated on credentials that must be company-owned, which is why they are wired to secrets rather than hardcoded.
