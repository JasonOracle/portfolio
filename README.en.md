# Portfolio · JasonOracle

[简体中文](README.md) | **English**

Personal portfolio of a frontend engineer with 9 years of experience, now working as an AI-Native full-stack developer. Pure static implementation (HTML / CSS / vanilla JS) — no build step, no third-party dependencies, fully responsive.

**Live site**: [https://portfolio-bwz.pages.dev](https://portfolio-bwz.pages.dev) · Cloudflare Pages

## Repository Structure

| File | Description |
|------|-------------|
| `index.html` | Main page — light theme (titanium-cool white + large-type layout, accent `#0071e3`) |
| `copy.html` | Style experiment draft for the "Recent Projects" section (paired with `copy.md`; verified and merged into the main page, safe to delete) |
| `assets/img/` | All screenshots in WebP, ~3MB for the entire site |

## Sections

- **Hero + Stats Bar**: 9 years of experience / ¥1M+ revenue / 10+ launched apps / 2 independent full-stack deliveries
- **Featured Work**: 4 key case studies (TiKu — three-end AI assessment SaaS, AI writing assistant matrix, bakery-chain AI operations App, AI customer-service system), asymmetric text-and-image layout
- **Recent Projects**: AI engineering infrastructure ×4 (agent-design-figma / CrossBrain / figma-agent-bridge / agent-bridge)
- **More Projects**: 20+ project card wall (bento grid, incl. 3 products with ¥10M+ revenue or 1M+ users)
- **Skills**: five-card layout with honest tiering — "proficient / self-taught / no production experience yet"

## Technical Highlights

- **Zero dependency**: single-file vanilla HTML / CSS / JS, no framework, no build
- **Image lightbox**: click to enlarge, multi-image navigation (keyboard ←→ / touch swipe), direct links to live demos, multi-image count badge
- **Scroll reveal**: IntersectionObserver-driven entrance animations with a `prefers-reduced-motion` static fallback
- **Restrained motion**: hover effects animate only `transform` / `opacity` — GPU-friendly

## Deployment (Cloudflare Pages)

1. Cloudflare Dashboard → Workers & Pages → Create → Pages → Connect to Git
2. Select this repository with the following build settings:
   - Framework preset: **None**
   - Build command: leave empty
   - Build output directory: `/`
3. Once deployed, the site is available at `*.pages.dev`; every push triggers an automatic update

---

📬 liuyn2017@qq.com · [GitHub Profile](https://github.com/JasonOracle)
