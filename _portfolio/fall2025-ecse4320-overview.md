---
title: "Advanced Computer Systems: Profiling and Optimization"
collection: portfolio
permalink: /portfolio/fall2025-ecse4320/
date: 2025-12-01
excerpt: "Course projects spanning memory latency, CPU placement, dense and sparse computation, concurrent hash tables, and NVMe storage profiling."
project_group: coursework-archive
display_year: "2025"
period: "Fall 2025"
sort_key: "2025-Fall"
date_precision: "term"
work_type: "Coursework"
work_category: "coursework"
venue: "Rensselaer Polytechnic Institute · ECSE 4320 Advanced Computer Systems"
tags: ["Computer Systems","Performance Profiling","Memory Systems","Concurrency"]
term: "Fall 2025"
work_source:
  organization: "RPI"
  course_code: "ECSE 4320"
  course_name: "Advanced Computer Systems"
---

## Measurement across the system

In ECSE 4320 at Rensselaer Polytechnic Institute, I built microbenchmarks and implementations to examine performance across processors, memory, storage, and concurrent software. I used C/C++, Python, Linux perf, fio, OpenMP, Pthreads, and libnuma as appropriate to each experiment.

I built pointer-chasing microbenchmarks to characterize L1, L2, L3, and DRAM access latency. I used Little's Law to estimate memory-level parallelism and examine saturation behavior, connecting individual access latency to the concurrency needed to sustain throughput.

## CPU placement and computation

I investigated CPU affinity, NUMA placement, and simultaneous multithreading with Linux microbenchmarks. The comparisons included local and cross-socket memory access and the effects of thread placement.

For matrix computation, I implemented dense and CSR-based sparse multiplication kernels with OpenMP and compiler autovectorization. Roofline analysis helped examine compute and memory constraints across matrix densities.

## Concurrency and storage

I built concurrent hash tables with coarse-grained and striped locking and compared scaling under read-heavy and write-heavy workloads. The analysis considered lock contention, false sharing, and cache-coherence traffic.

I profiled NVMe storage with fio and direct I/O, varying queue depth to examine throughput, average latency, and p99 latency near saturation.

## Related project pages

- [CPU scheduling and hardware features](/portfolio/fall2025-ecse4320-tracka1/)
- [Dense and sparse matrix multiplication with Roofline analysis](/portfolio/fall2025-ecse4320-tracka2/)
- [Concurrent hash tables and memory coherence](/portfolio/fall2025-ecse4320-tracka4/)
- [SSD performance profiling with fio](/portfolio/fall2025-ecse4320-classwide-ssd/)
