# Content Map

## Current Stack

- Static site generator: Jekyll
- Current theme base: Academic Pages / Minimal Mistakes style structure
- Styling pipeline: Sass via `assets/css/main.scss` and `_sass/`
- Content model: mix of `_pages/`, collections, and `_data/`

## Primary Section Ownership

- Home: `_pages/home.md`
- Projects index: `_pages/portfolio.html`
- Project entries: `_portfolio/*.md`
- CV: `_pages/cv.md`
- Alternate structured CV path already present but unused in nav: `_pages/cv-json.md` with `_data/cv.json`
- Publications index: `_pages/publications.html`
- Publication entries: `_publications/*.md`
- Certificates: `_pages/certificates.md` with `_data/certificates.yml`
- About: `_pages/about.md`

## Other Content Locations

- Downloadable static files: `files/`
- Certificate assets: `files/certificates/`
- Site images: `images/`
- Global site metadata and navigation: `_config.yml`, `_data/navigation.yml`

## Current Theme-Coupled Files

These files strongly shape the current academic-template presentation:

- `_layouts/default.html`
- `_layouts/single.html`
- `_layouts/archive.html`
- `_includes/sidebar.html`
- `_includes/author-profile.html`
- `_includes/masthead.html`
- `_includes/archive-single.html`
- `_sass/layout/_page.scss`
- `_sass/layout/_archive.scss`
- `_sass/layout/_sidebar.scss`

## Content Quality Notes

- `Projects` contains meaningful portfolio content and is worth preserving as the main long-form body of work.
- `Certificates` is now in a good data-driven direction.
- `CV` currently contains template/demo placeholder content and should be rewritten or migrated to structured data before the visual redesign is treated as complete.
- `_data/cv.json` is also still template/demo content.
- `Publications` currently appears to be template/demo content rather than real publications, so it should be treated as a content-cleanup area in a later phase.

## Recommended Future Content Model

- Home: structured landing content, likely split into hero, focus areas, selected work, and short intro blocks.
- Projects: keep as a collection, but add cleaner metadata over time for featured state, category, year, and external links.
- CV: move toward structured data or section-based includes instead of one large markdown page.
- Publications: keep as a collection if publication detail pages are useful.
- Certificates: keep the `_data/certificates.yml` model.
- About: keep as a dedicated single page with more narrative content than Home.
