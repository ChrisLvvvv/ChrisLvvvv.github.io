---
title: "Advanced Computer Systems Projects Overview"
collection: portfolio
permalink: /portfolio/fall2025-ecse4320/
date: 2025-12-01
venue: "ECSE4320 Advanced Computer Systems"
excerpt: "Project set covering CPU scheduling, SIMD and sparse linear algebra, concurrent data structures and SSD storage profiling."
project_group: coursework-archive
tags:
  - Computer Systems
  - Performance
  - Concurrency
  - SIMD
  - Profiling
---

This course focused on performance oriented systems design across the compute stack, spanning CPU scheduling behavior, SIMD and sparse linear algebra, concurrent data structures and storage performance. I completed three Track A projects and one classwide project, each targeting a different layer of the system.

## Track A Projects

- **Project A1 – CPU Scheduling and Hardware Features**  
  Explored CPU affinity, scheduler oversubscription, NUMA behavior and simultaneous multithreading by running controlled microbenchmarks and analyzing how operating system policies and hardware topology affect performance and stability.

- **Project A2 – Dense vs Sparse Matrix Multiplication and Roofline Analysis**  
  Implemented and optimized dense and sparse matrix multiplication kernels using SIMD and multithreading, then used a Roofline model to classify each kernel as compute or memory bound and relate observed throughput to machine balance.

- **Project A4 – Concurrent Hash Table and Memory Coherence**  
  Designed and evaluated thread safe hash table implementations using coarse grained and striped locking, measuring scalability, throughput and cache coherence effects under different read and write workloads.

## Classwide Project

- **Classwide Project 3 – SSD Performance Profiling with fio**  
  Collaborated in the classwide benchmarking effort by profiling block device performance using fio, sweeping queue depth, block size and read write mixes to understand the throughput and latency trade offs of SSD storage.

Together, these projects strengthened my ability to reason about hardware aware optimization, measurement methodology and performance debugging across CPU, memory, concurrency and storage subsystems.

---

## Related Project Pages

- [Project A1 - CPU Scheduling and Hardware Features](/portfolio/fall2025-ecse4320-tracka1/)
- [Project A2 - Dense and Sparse Matmul with Roofline Analysis](/portfolio/fall2025-ecse4320-tracka2/)
- [Project A4 - Concurrent Hash Table and Memory Coherence](/portfolio/fall2025-ecse4320-tracka4/)
- [Classwide Project 3 - SSD Performance Profiling with fio](/portfolio/fall2025-ecse4320-classwide-ssd/)
