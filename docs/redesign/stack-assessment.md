# Stack Assessment

## Recommendation

Keep Jekyll for the next phase, but treat the current Academic Pages structure as a starting point rather than a design system.

## Why Jekyll Can Still Work

- the site is already content-oriented and static
- collections are a good fit for projects and publications
- `_data` works well for certificates and could also support future landing-page sections
- phase 1 cleanup is still meaningful because content modeling is reusable even if a migration happens later

## What Fights the Intended Redesign

- the current theme assumes an academic profile/sidebar pattern
- shared layouts are tightly coupled to the sidebar and archive presentation
- the markup patterns lean toward blog/archive output instead of intentionally designed portfolio sections

## When Astro Would Become More Attractive

Consider migrating later if you want:

- component-level control over every page section
- cleaner separation of content, layout, and interaction
- a less theme-shaped HTML structure
- a more flexible long-term portfolio system with custom sections and stronger design control

## Current Judgment

- Phase 1 with Jekyll: worthwhile
- Phase 2 visual redesign with Jekyll: possible
- Full migration right now: not necessary yet

If the redesign later starts fighting the Jekyll theme shell more than the actual content work, that is the right moment to revisit Astro.
