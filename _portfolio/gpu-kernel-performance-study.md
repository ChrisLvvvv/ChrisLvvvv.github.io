---
title: "GPU Kernel Performance Study for MoE Workloads"
collection: portfolio
permalink: /portfolio/gpu-kernel-performance-study/
date: 2025-11-15
venue: "Undergraduate Research Project – Fall 2025"
excerpt: "Profiled and analyzed GPU kernel behavior for Mixture-of-Experts LLM workloads, focusing on PagedAttention performance, memory fragmentation, and scheduling inefficiencies."
tags:
  - GPU Systems
  - LLM Inference
  - CUDA Profiling
  - vLLM
  - MoE
  - PagedAttention
---

This project investigates GPU kernel performance bottlenecks in Mixture-of-Experts (MoE) large language model inference. The study focuses on PagedAttention, memory fragmentation in dynamic KV-cache allocation, and kernel-level scheduling behavior on modern NVIDIA GPUs. Using vLLM and custom profiling utilities, I examined how expert routing patterns and varying sequence lengths impact throughput and GPU utilization.

## My Contribution

- Built profiling workflows to analyze PagedAttention kernels under diverse batch sizes and MoE routing distributions  
- Measured memory fragmentation and cache behavior using custom scripts and NVIDIA profiling tools  
- Identified inefficiencies in expert activation imbalance and kernel launch patterns  
- Generated reproducible benchmarks and visualizations for throughput, latency, and SM occupancy  
- Documented key insights to guide later optimization work in memory scheduling and cache-aware design  

## Technical Summary

- **Concepts:** MoE routing, GPU memory hierarchy, PagedAttention, kernel scheduling  
- **Methods:** CUDA profiling, KV-cache inspection, GPU timeline analysis  
- **Tools:** vLLM, NVIDIA Nsight Systems, Nsight Compute, custom Python profiling scripts  

## Outcome

Produced a detailed analysis of bottlenecks in MoE inference workloads, highlighting opportunities for improved cache locality, reduced fragmentation, and more efficient kernel launches. The results serve as foundational work for ongoing URP research on KV-cache compression and memory-aware scheduling.
