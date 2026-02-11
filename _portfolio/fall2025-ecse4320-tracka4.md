---
title: "Project A4: Concurrent Hash Table and Memory Coherence"
collection: portfolio
permalink: /portfolio/fall2025-ecse4320-tracka4/
date: 2025-11-05
venue: "ECSE4320 Advanced Computer Systems"
excerpt: "Comparison of coarse grained and striped locking for a concurrent hash table, focusing on scalability, contention and cache coherence."
tags:
  - Concurrency
  - Hash Table
  - Locking
  - Multithreading
  - Performance
---

This project examined how synchronization design impacts the scalability of concurrent data structures. I implemented a thread safe chained hash table using two locking strategies and benchmarked their behavior under different workloads and thread counts.

## Design

- **Core data structure**  
  - Chained hash table supporting `insert`, `lookup` and `erase`.  
  - Designed to be accessed concurrently by many threads.

- **Coarse grained locking**  
  - Single global mutex guarding all operations.  
  - Simple to implement and correct, but quickly becomes a bottleneck at higher thread counts.

- **Striped locking**  
  - Partitioned the table into multiple stripes, each protected by its own mutex.  
  - Reduced lock contention by allowing operations on different stripes to proceed in parallel.  
  - Preserved correctness while improving throughput on multicore hardware.

## Benchmarking

- Implemented a benchmark driver in C++ using pthreads.  
- Evaluated three workload types:  
  - Lookup only, read dominated scenario.  
  - Insert only, write heavy stress test.  
  - Mixed workload with a 70 percent lookup and 30 percent insert split.  
- Swept thread counts from 1 to 16 and varied key set sizes.  
- Collected metrics such as throughput, speedup relative to a single thread and fairness across threads.

## Analysis

- Compared scaling behavior of coarse grained and striped locking.  
- Discussed how Amdahl’s Law and cache coherence effects limit speedup even with more fine grained locking.  
- Observed that striped locking significantly improved performance for mixed and read heavy workloads, while write heavy workloads remained more constrained by inherent serialization.

## Outcome

This project provided practical experience designing and evaluating concurrent data structures. It highlighted the trade offs between implementation complexity and performance, and emphasized the need to consider both contention and memory system behavior when choosing synchronization strategies.
