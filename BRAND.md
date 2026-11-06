# Dan O’Donnell — brand and implementation handoff

The personal site combines Coffee Cup AI’s verified brand with Flame’s anchor navigation, generous hero and modular long-page structure. The result is an original personal site, not a reproduction of either reference.

## Source assets

- Orange: `#FC630F`, sampled from the computed primary button on https://coffeecupai.com on November 6, 2026. CSS includes its mathematically equivalent OKLCH value.
- Display and body font: Manrope, variable weight 200–800, self-hosted from https://coffeecupai.com/assets/manrope-latin.woff2. The local asset is approximately 25 KB. Its preload is in every page head.
- Coffee Cup AI official logo: https://coffeecupai.com/assets/coffee-cup-ai-logo-humans-own-ai.svg, intrinsic 217×44. Transparent background, light lettering: use on dark surfaces. The original SVG is included locally.
- Portrait: user-provided AI-Dan-ODonnell.jpg, 350×420, converted to WebP. Display is capped at 350 CSS pixels. No identity or facial edits.
- The D. monogram is a new identity for Dan’s personal site. The book title panel is website typography, not a claim to be an official book cover.

## Tokens and contrast

| Foreground | Background | Role | WCAG contrast |
|---|---|---|---|
| #F5F1E9 | #121110 | Main text on base | 16.74:1 |
| #BCB5AC | #121110 | Muted text on base | 9.29:1 |
| #BCB5AC | #26221E | Muted text on raised surface | 7.78:1 |
| #FC630F | #121110 | Accent text on base | 6.22:1 |
| #18120E | #FC630F | Button/contact-band text | 6.12:1 |
| #18120E | #F2EDE4 | Light section text | 15.91:1 |
| #645B52 | #F2EDE4 | Light section muted text | 5.70:1 |
| #A03900 | #F2EDE4 | Accent text on light | 5.85:1 |

CSS variables are the source of truth in styles.css. Hero H1: 42–68px, weight 500, 1.08 line-height. H2: 34–48px. Section spacing: 72–120px, 64px on phones. Buttons: 4px radius. Cards: square corners. Main container: max 1184px. Mobile gutters: 20px. No shadows or continuous animation.

## Invariants — don’t break these

- Brand-orange buttons use dark text. The full orange contact section also uses dark text.
- Cream sections use a darker accent and focus ring. Do not apply orange body text on cream.
- No text opacity tricks; use explicit muted colors.
- Body copy is always visible without JavaScript. CSS smooth scrolling respects reduced motion.
- Every image has dimensions. The portrait is preloaded, WebP and at most its natural width. The footer-strip logo is lazy loaded.
- Keep the official Coffee Cup AI logo on a dark background.
- The menu and workflow controls expose their state through ARIA. Retain Escape-to-close behavior.
- Recompute metadata from site.config.json when changing the canonical domain; run python build.py.
- The January 2027 book is forthcoming as of this build. Do not automatically claim publication when the date passes.
- Press releases are described as announcements. Do not convert them to implied endorsements.
- Keep privacy statements synchronized with actual analytics, forms, storage and hosting features.

## Reference comparison and intentional changes

Computed values sampled at a 1280px viewport. Reference: https://technext.github.io/flameonepage/.

| Area | Flame reference | This build | Decision |
|---|---|---|---|
| Hero | Full-width photo carousel, 720px tall | Static portrait composition, about 709px tall | Similar generous opening; personal portrait instead of template artwork |
| H1 | Ubuntu, 59px, 64.9px line-height | Manrope, 65.92px, 71.19px line-height | Brand typography; two intentional lines |
| Navigation | Seven in-page links, over hero | Five in-page links, sticky charcoal header | Simplified for this content |
| Services | Six icon/text modules; three columns | Six SVG/text modules; three columns | Preserved structure and media type |
| Service padding/radius | 50px / 0px | 32px / 0px | Tighter padding to accommodate substantive content |
| Tablet services | Three columns at 768px | Two columns at 768px | Improved reading width |
| Intro | Three image features plus split explanation/accordion | Cream split introduction and separate FAQ | Adapted to supplied biography and consulting content |
| Projects/pricing | Three photo cards and three price cards | Workflow examples and four-stage consulting process | No invented projects or prices |
| Portfolio | Image mosaic and logo carousel | Career chronology, speaking records, book title panel | Evidence available for a personal site |
| Contact | Three location columns plus map | One orange contact band with direct email | No invented offices or form backend |
| Footer | Three link groups and legal links | Three link groups, separate legal pages, dynamic year | Similar hierarchy; working destinations |

## QA and limitations

- Browser layout widths checked: 390, 768, 1280, 1920. No document horizontal overflow. At 1920px the portrait remains 350px wide, and paragraphs remain contained.
- H1 is two lines at desktop; three at 768px. Services collapse 3 → 2 → 1.
- Menu open, close after selection and anchor offset verified. Workflow switches and FAQ expansion verified. Copyright displays 2026 through JavaScript.
- Source check verifies one H1 per page, all local assets, internal destinations/fragments, unique IDs and JSON-LD parsing. JavaScript syntax check passes.
- No external font requests, render-blocking stylesheet links, tracking scripts or embedded third-party media.
- The specialist web-perf, responsive-qa and design-review skills referenced by design-from-reference are not installed. Equivalent checks were performed where available.
- No Lighthouse or public PageSpeed Insights score is claimed. Owner-private hosting cannot be used as a meaningful public SEO/performance target; public-domain testing remains a launch step.
- Manual design assessment: hierarchy 9/10, brand consistency 9/10, content clarity 9/10, responsive fit 9/10. These are subjective review scores, not automated accessibility certification.
