---
title: "Project A1: CPU Scheduling and Hardware Features"
collection: portfolio
permalink: /portfolio/fall2025-ecse4320-tracka1/
date: 2025-10-10
excerpt: "Linux microbenchmarks investigating CPU affinity, NUMA locality, simultaneous multithreading, and thread placement."
project_group: coursework-archive
display_year: "2025"
period: "Fall 2025"
sort_key: "2025-Fall"
date_precision: "term"
work_type: "Coursework"
work_category: "coursework"
venue: "Rensselaer Polytechnic Institute · ECSE 4320 Advanced Computer Systems"
tags: ["CPU Affinity","NUMA","SMT","Linux Profiling"]
term: "Fall 2025"
work_source:
  organization: "RPI"
  course_code: "ECSE 4320"
  course_name: "Advanced Computer Systems"
---

[← Advanced Computer Systems overview](/portfolio/fall2025-ecse4320/)

## Placement and memory locality

I designed Linux microbenchmarks to investigate CPU affinity, NUMA placement, and simultaneous multithreading. I compared local and cross-socket memory access and evaluated how thread placement interacts with the memory hierarchy.

## Measurement focus

The experiments connected software placement decisions to hardware topology. I used C/C++ with Pthreads, Linux perf, and libnuma to examine scheduling and memory behavior.
