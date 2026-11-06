# Dan O’Donnell personal website

Buildless static website for https://danodonnell.net. The deployable files are in dist/. Source copy, tokens and a small Python generator are included for easy maintenance.

## Edit and preview

1. Edit home.html for home-page copy and styles.css for presentation.
2. Edit build.py for shared navigation, footer, legal copy and structured data.
3. Edit site.config.json for the canonical domain, SEO title and description.
4. Run `python build.py` and `python check.py`.
5. Run `python -m http.server 4173 --bind 127.0.0.1 --directory dist` and open http://127.0.0.1:4173/.

No package installation or framework build is required. The generated HTML contains inline CSS and pre-rendered content. JavaScript only adds navigation, example switching, active section indication and the copyright year. Email buttons use mailto links and do not submit a website form.

## Deployment

Upload dist/ to a static web host that serves directory index files and 404.html. The optional _headers file is understood by compatible hosts. Retain HTTPS and serve /privacy-policy/ and /terms-of-use/ as directory routes.

The Sites preview is owner-private by default. It is not the public launch at danodonnell.net. Complete domain DNS configuration and public audience setup before expecting Google to crawl it. The canonical URL, Open Graph URL, JSON-LD and sitemap all use the user-confirmed https://danodonnell.net.

Before public launch, confirm the privacy policy matches the chosen hosting provider and email/data practices, and update it if analytics, forms or subscriptions are added. The text describes the current minimal site. No analytics or marketing pixels are installed.

## Editorial facts

Verified sources support the founding of 2TheTopMarketing and evolution to Crevand, the SEO Rockstars appearance, and the AI consulting announcement. The owner supplied the three 404con appearances, expanded Mitchell+Palmer role, and book title/date. The book is labeled forthcoming January 2027. No testimonials, client performance figures, prices, publisher, ISBN or preorder link were invented.

See BRAND.md for tokens, source assets, contrast, reference comparison and QA. The separate SEO-and-build-report.html deliverable explains the On-Page.ai findings and remaining launch steps.
