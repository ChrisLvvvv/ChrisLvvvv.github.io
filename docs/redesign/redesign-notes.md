# Redesign Notes

## Direction

Target feel for later phases:

- clean and spacious
- warm and restrained
- calm visual rhythm
- content-first
- subtle interaction
- less academic template, more designed portfolio

## What This Phase Does

- audits current content ownership
- separates Home and About into distinct pages
- aligns the main navigation with the intended top-level information architecture
- adds internal documentation for future redesign work
- preserves current content and collections instead of forcing an early migration

## What This Phase Does Not Do

- no full visual redesign
- no large CSS pass
- no stack migration
- no destructive content cleanup

## High-Priority Cleanup Areas Before Visual Phase

- rewrite `CV` content so it reflects real experience rather than template placeholders
- replace demo `Publications` entries with real content or intentionally empty-state handling
- decide whether Home should remain markdown-driven or move to a more structured section model
- decide whether Projects should gain metadata such as `featured`, `project_type`, `year`, `external_url`, and `thumbnail`

## Desired Future Navigation

- Home
- Projects
- CV
- Publications
- Certificates
- About

## Layout Constraint to Address in Phase 2

The current left profile column is not just styling. It is injected by the shared page layouts through `_includes/sidebar.html`, so removing it cleanly will require layout work in addition to CSS changes.
