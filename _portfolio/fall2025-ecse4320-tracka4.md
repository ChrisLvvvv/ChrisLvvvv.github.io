---
title: "Project A4: Concurrent Hash Table and Memory Coherence"
collection: portfolio
permalink: /portfolio/fall2025-ecse4320-tracka4/
date: 2025-11-05
excerpt: "Coarse-grained and striped locking evaluated under read-heavy and write-heavy workloads, with attention to contention and memory-system effects."
project_group: coursework-archive
display_year: "2025"
period: "Fall 2025"
sort_key: "2025-Fall"
date_precision: "term"
work_type: "Coursework"
work_category: "coursework"
venue: "Rensselaer Polytechnic Institute · ECSE 4320 Advanced Computer Systems"
tags: ["Concurrent Hash Tables","Locking","Pthreads","Cache Coherence"]
term: "Fall 2025"
work_source:
  organization: "RPI"
  course_code: "ECSE 4320"
  course_name: "Advanced Computer Systems"
---

[← Advanced Computer Systems overview](/portfolio/fall2025-ecse4320/)

## Synchronization choices

I built concurrent hash tables using coarse-grained and striped locking. The two approaches expose different opportunities for parallel access and different sources of synchronization overhead.

## Scaling and memory behavior

I compared scaling under read-heavy and write-heavy workloads. The analysis examined contention, false sharing, and cache-coherence traffic alongside the locking structure.

This project connected synchronization choices to the memory system: adding threads changes both access concurrency and the traffic required to keep shared data coherent.
