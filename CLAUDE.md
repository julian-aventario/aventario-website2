# Aventario Website

Static marketing site for **Aventario** — outcome-based IT vendor management for DACH mid-market enterprises. Target audience: CFOs, CIOs, and heads of procurement at mid-market firms looking to cut IT vendor costs by 10–40%.

## Stack

- **Pure static HTML** — no build step, no bundler, no framework.
- **Tailwind CSS** via CDN (`cdn.tailwindcss.com`). Theme tokens are defined inline inside each `<head>` via `tailwind.config`.
- **GSAP + ScrollTrigger** via CDN for animations.
- **Phosphor Icons** via CDN (`@phosphor-icons/web`).
- **Font:** Lato (400/700/900) via Google Fonts.

## Files

- [index.html](index.html) — homepage
- [about.html](about.html) — company / team
- [contact.html](contact.html) — contact form
- [resources.html](resources.html) — content hub
- [success-stories.html](success-stories.html) — case study index
- [success-stories/](success-stories/) — individual case study pages (Sodexo, Frankfurt Airport, pharmaceutical, tech, digital transformation)
- [impressum.html](impressum.html) — German legal imprint (required for DACH sites)
- [datenschutz.html](datenschutz.html) — German privacy notice (GDPR)
- [logos/](logos/) — brand SVGs (full logo + signet)

## Design tokens

Defined in each page's inline `tailwind.config`:

| Token | Value | Use |
|---|---|---|
| `base` | `#FAFAF7` | Page background |
| `surface` | `#FFFFFF` | Cards, panels |
| `text` | `#334b60` | Primary body text (deep blue-grey) |
| `muted` | `#5f768b` | Secondary text |
| `accent` | `#88C9BE` | Brand teal |
| `accentdark` | `#5FA99D` | Hover / active teal |
| `bordercolor` | `rgba(51, 75, 96, 0.12)` | Dividers |

**Type:** Lato for everything — both `font-sans` and `font-serif` alias to Lato.

## Conventions

- Art direction is intentionally strict — keep the existing palette, typography, and spacing rhythm. Do not introduce new colors or fonts without asking.
- German-language pages (impressum, datenschutz) exist for legal compliance — changes there are legal, not cosmetic. Get confirmation before editing copy.
- Keep pages self-contained: styles and scripts live inline per page. There is no shared CSS/JS bundle.
- Since this is static, previewing = opening `index.html` in a browser or serving the directory (`python3 -m http.server 8888`).

## Not a git repo

The directory is not under version control. Be careful with destructive operations — there is no safety net.
