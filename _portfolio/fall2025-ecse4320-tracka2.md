---
title: "Project A2: Dense and Sparse Matrix Multiplication with Roofline Analysis"
collection: portfolio
permalink: /portfolio/fall2025-ecse4320-tracka2/
date: 2025-10-25
venue: "ECSE4320 Advanced Computer Systems"
excerpt: "SIMD and multithreaded optimization of dense and sparse matrix multiplication kernels, evaluated with a Roofline performance model."
tags:
  - SIMD
  - Linear Algebra
  - Sparse Matrices
  - Multithreading
  - Roofline
---

[← Back to ECSE4320 Advanced Computer Systems Overview](/portfolio/fall2025-ecse4320/)

This project studied performance differences between dense and sparse linear algebra kernels and related measured throughput to theoretical machine limits using a Roofline model. I implemented and optimized dense GEMM and sparse matrix multiplication kernels, then analyzed how arithmetic intensity and memory behavior constrained attainable performance.

## Implementations

- **Dense GEMM**  
  - Implemented a baseline dense matrix multiply kernel `C = A × B`.  
  - Added cache aware blocking and loop reordering to improve locality.  
  - Introduced SIMD vectorization and multithreading to exploit available cores.  
  - Compared against a reference BLAS implementation for correctness and sanity checking of performance.

- **CSR Sparse Matrix Multiplication (SpMM)**  
  - Implemented a sparse matrix multiplication kernel using CSR format for `A` and dense `B` and `C`.  
  - Designed loops to respect the irregular sparsity pattern while still allowing limited SIMD usage.  
  - Quantified how structure dependent memory access patterns bound performance even with parallelism.

## Roofline Analysis

- Measured achieved FLOP/s and memory bandwidth for each kernel and configuration.  
- Computed arithmetic intensity and plotted each variant onto a Roofline model.  
- Classified kernels as compute bound or memory bound based on their position relative to the machine’s peak compute and bandwidth ceilings.  
- Showed that optimized dense GEMM could approach the compute roof, while SpMM often remained constrained by memory traffic and irregular access.

## Tools and Environment

- Language and tools: C, OpenMP or pthreads, SIMD intrinsics where appropriate.  
- Profiling and plotting: Python with pandas and matplotlib.  
- Experiments used controlled matrix sizes, fixed random seeds and repeated trials, reporting best of or median runtimes depending on analysis context.

## Outcome

The project demonstrated how algorithmic structure, data layout and low level optimizations interact to determine performance in practice. It reinforced Roofline modeling as a useful framework for reasoning about optimization priorities across dense and sparse workloads.
