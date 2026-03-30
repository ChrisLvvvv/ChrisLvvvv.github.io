---
title: "Project A1: CPU Scheduling and Hardware Features"
collection: portfolio
permalink: /portfolio/fall2025-ecse4320-tracka1/
date: 2025-10-10
venue: "ECSE4320 Advanced Computer Systems"
excerpt: "Experimental study of CPU affinity, scheduler oversubscription, NUMA locality and SMT interference using microbenchmarks and Linux tooling."
project_group: coursework-archive
tags:
  - ECSE4320
  - Computer Systems
  - CPU Architecture
  - Operating Systems
  - NUMA
  - SMT
  - Performance
---

[← Back to ECSE4320 Advanced Computer Systems Overview](/portfolio/fall2025-ecse4320/)

This project explored how operating system scheduling policies and hardware features influence application performance.


## Experiments

- **Feature 1 – CPU Affinity**  
  - Benchmarked a parallel workload with and without explicit thread pinning.  
  - Measured both mean runtime and variance across repeated runs.  
  - Found that affinity primarily improved stability by reducing jitter, while average throughput remained similar when the scheduler made good default placements.

- **Feature 2 – Scheduler Behavior Under Oversubscription**  
  - Varied the number of worker threads from below to well above the logical core count.  
  - Examined how the Linux Completely Fair Scheduler handled oversubscription.  
  - Observed the transition from near linear scaling to saturation and degradation as context switching overhead and run queue contention increased.

- **Feature 3 – NUMA Locality**  
  - Investigated Non Uniform Memory Access behavior using memory bound workloads and different NUMA settings.  
  - Used tools such as `numactl` and bandwidth measurements to compare local versus remote access policies.  
  - Highlighted the importance of understanding the underlying topology, especially in virtualized or single socket systems where apparent NUMA domains may be abstracted.

- **Feature 4 – SMT Interference**  
  - Measured performance of compute bound and memory bound kernels with and without a competing thread pinned to the sibling logical CPU on the same core.  
  - Quantified how shared core resources and cache hierarchy produce interference under SMT.  
  - Showed that compute heavy workloads suffer more under interference than memory bound workloads which are already limited by bandwidth.

## Methodology

- Implemented microbenchmarks in C and C++ with POSIX threads.  
- Used Linux tools such as `taskset`, `numactl` and `perf` to control and observe scheduling behavior.  
- Ran multiple trials per configuration to capture run to run variability and reported both median and spread.

## Outcome

This project provided hands on insight into the interaction between OS scheduling, CPU topology and workload characteristics. It built intuition for when manual control such as affinity and NUMA policies can help, and when they simply mirror the scheduler’s default decisions.
