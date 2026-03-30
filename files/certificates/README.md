# Certificate Assets

Place certificate PDFs and optional preview images in this folder.

## Naming Convention

Use:

`YYYY-MM-DD_provider_course_documenttype.ext`

Rules:

- lowercase only
- use hyphens inside words
- use underscores only as the major separators shown above
- no spaces
- no special characters
- ASCII only

Examples:

- `2026-03-29_anthropic_claude-101_certificate.pdf`
- `2026-03-29_anthropic_claude-101_badge.png`

## Suggested Upload Pattern

- PDF certificate: `*_certificate.pdf`
- Badge or thumbnail image: `*_badge.png` or `*_thumbnail.jpg`

After uploading a file here, reference it from `_data/certificates.yml` with a site-root path such as:

- `/files/certificates/2026-03-29_anthropic_claude-101_certificate.pdf`
