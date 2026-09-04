# EspunyDesign — Cloudflare Pages deployment

This is a static site: pure HTML/CSS/vanilla JS, no build step, no framework.

## Structure

```
/                    → Spanish (default/root)
/ca/                 → Catalan
/en/                 → English
/assets/css/style.css
/assets/js/main.js
/assets/img/…        → optimized JPG + WebP (browser picks the smaller one)
/_headers            → Cloudflare Pages cache & security headers
/_redirects          → legacy path redirects
/robots.txt, /sitemap.xml
/404.html
```

Each language is a fully separate, statically rendered page (not a JS
language‑switcher), so search engines index `/`, `/ca/`, and `/en/` as
distinct pages with proper `hreflang` alternates — better for SEO and for
first‑paint performance than the previous single‑page + `localStorage`
approach.

## Deploy to Cloudflare Pages

**Option A — Git (recommended):**
1. Push this folder to a GitHub/GitLab repo.
2. Cloudflare dashboard → Workers & Pages → Create → Pages → Connect to Git.
3. Build settings:
   - Framework preset: **None**
   - Build command: *(leave empty)*
   - Build output directory: `/`
4. Deploy.

**Option B — Direct upload:**
1. Workers & Pages → Create → Pages → Upload assets.
2. Drag this whole folder in (it must contain `index.html` at the top level).

## Connect the domain

1. In the Pages project → **Custom domains** → add `espunydesign.com` (and
   `www.espunydesign.com` if you want it, since `_redirects` includes a
   www → apex rule for that case).
2. If the domain is already on Cloudflare, DNS records are created for you
   automatically. Otherwise point your DNS to Cloudflare per the dashboard
   instructions.

## What's already optimized

- **Images**: every photo has a same‑quality WebP sibling and a compressed,
  progressive JPEG fallback (`<picture>` + `<source type="image/webp">`),
  plus `width`/`height` attributes to prevent layout shift.
- **Fonts**: Google Fonts loaded with `preconnect` + `display=swap`.
- **Caching**: `/_headers` sets `Cache-Control: immutable, max-age=1y` for
  everything under `/assets/*` and the icon files; HTML revalidates on every
  request so content updates go live immediately.
- **JS**: single small vanilla file, loaded with `defer`, no dependencies.
- **CSS**: single stylesheet, CSS custom properties, no framework bloat.
- **SEO**: per‑language `<title>`/meta description, canonical + hreflang
  (`es`, `ca`, `en`, `x-default`), Open Graph/Twitter cards, JSON‑LD
  `ProfessionalService` structured data, `sitemap.xml`, `robots.txt`.
- **Accessibility**: skip‑link, proper `aria-*` on the nav/toggle/modals,
  focus handling on modal open, keyboard support for cards and the
  gallery lightbox.
- **Security headers**: `X-Content-Type-Options`, `X-Frame-Options`,
  `Referrer-Policy`, `Permissions-Policy` via `_headers`.

## Content notes

- The two full project write‑ups (Bar‑Restaurant Salamandra and
  Castelldefels House) use only the real text/data supplied — nothing
  invented.
- The other real photos found in the source data (Casa DRE, Casa POR,
  Terrassa Ben, and a general/"other" shot) are shown in a lightweight
  "more work" strip with just their name and a click‑to‑enlarge lightbox,
  since no verified location/year/description existed for them. Add real
  details any time by editing the `LANGS` dict in `build_site.py` and
  re‑running it, or by editing the three `index.html` files directly.
- Contact form posts to FormSubmit (`https://formsubmit.co/info@espunydesign.com`,
  matching the "project form" address from your notes) — no backend needed.
  First submission from a new domain requires a one‑time confirmation click
  from that inbox (FormSubmit sends it automatically).

## Regenerating the pages

`build_site.py` (in this same folder) is the source of truth for the three
HTML files — it renders `index.html`, `ca/index.html`, and `en/index.html`
from one template + a per‑language dictionary, so copy/spacing/wording only
needs to change in one place. Edit the `LANGS` dict, then run:

```
python3 build_site.py
```

from inside this folder — it overwrites the three `index.html` files in
place. (It doesn't touch `assets/`, `_headers`, etc.)
