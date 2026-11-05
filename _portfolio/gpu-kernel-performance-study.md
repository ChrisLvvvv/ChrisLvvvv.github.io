---
title: "GPU Kernel Performance Study for MoE Workloads"
collection: portfolio
permalink: /portfolio/gpu-kernel-performance-study/
date: 2025-11-15
excerpt: "Profiled and analyzed GPU kernel behavior for Mixture-of-Experts LLM workloads, focusing on PagedAttention performance, memory fragmentation, and scheduling inefficiencies."
featured_on_home: true
project_group: research
work_title: "GPU Memory Management for High-Throughput LLM Serving"
work_excerpt: "Profiling fragmentation, block-based KV-cache allocation, and request scheduling in vLLM-style autoregressive serving."
display_year: "2025"
period: "Aug. 2025 – Jan. 2026"
start_month: "2025-08"
end_month: "2026-01"
sort_key: "2025-08"
date_precision: "month"
work_type: "Undergraduate Research Program"
work_category: "experience"
venue: "Rensselaer Polytechnic Institute · Undergraduate Research Program"
tags: ["GPU Memory","LLM Serving","PagedAttention","PyTorch"]
work_source:
  organization: "RPI"
  detail: "URP"
---

## Research setting

I carried out this undergraduate research at Rensselaer Polytechnic Institute in Troy, New York, from August 2025 to January 2026, advised by Prof. Liu Liu. I investigated GPU memory management for high-throughput LLM serving, focusing on fragmentation, allocation, and scheduling under variable-length requests.

## From contiguous reservations to KV blocks

I studied how PagedAttention maps logical KV-cache blocks to noncontiguous physical GPU memory in vLLM-style serving. The central question was how allocation granularity changes usable memory during large-batch autoregressive inference, when prompts and generated outputs require different amounts of cache space.

I developed PyTorch-based profiling scripts to vary sequence length, request concurrency, and KV block size across synthetic serving workloads. The workload ranges targeted 128–2048-token contexts and 1–64 concurrent requests.

## Allocation and scheduling

I benchmarked contiguous over-provisioning against block-based KV-cache allocation. The comparisons examined internal fragmentation, reserved-token waste, and effective GPU memory utilization under variable-length prompts and outputs.

I also analyzed the request-scheduling path through waiting, running, and swapped queues. This connected allocation behavior to CPU/GPU block placement, preemption, and block reuse, and to their effects on throughput when GPU memory is under pressure.
