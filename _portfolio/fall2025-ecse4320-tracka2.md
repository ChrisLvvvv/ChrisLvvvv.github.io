---
title: "Project A2: Dense and Sparse Matrix Multiplication with Roofline Analysis"
collection: portfolio
permalink: /portfolio/fall2025-ecse4320-tracka2/
date: 2025-10-25
excerpt: "Dense and CSR sparse matrix kernels using OpenMP and compiler autovectorization, examined with Roofline analysis across matrix densities."
project_group: coursework-archive
display_year: "2025"
period: "Fall 2025"
sort_key: "2025-Fall"
date_precision: "term"
work_type: "Coursework"
work_category: "coursework"
venue: "Rensselaer Polytechnic Institute · ECSE 4320 Advanced Computer Systems"
tags: ["OpenMP","CSR Matrices","Autovectorization","Roofline"]
term: "Fall 2025"
work_source:
  organization: "RPI"
  course_code: "ECSE 4320"
  course_name: "Advanced Computer Systems"
---

[← Advanced Computer Systems overview](/portfolio/fall2025-ecse4320/)

## Dense and sparse implementations

I implemented dense and CSR-based sparse matrix-multiplication kernels. OpenMP supplied parallel execution, while compiler autovectorization exposed data parallelism where the access structure allowed it.

Dense and sparse representations organize computation differently. The sparse implementation uses CSR structure, making matrix density and access patterns important parts of the comparison.

## Roofline interpretation

I applied Roofline analysis to examine compute and memory constraints and compare behavior across matrix densities. This provided a way to relate arithmetic work to data movement, rather than treating elapsed time alone as an explanation of performance.
