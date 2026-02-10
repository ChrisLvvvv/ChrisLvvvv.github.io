---
title: "KV Cache Compression and Bit-Plane Eviction Scheduling"
collection: portfolio
permalink: /portfolio/fall2024-kv-cache-compression/
date: 2024-12-01
venue: "Undergraduate Research – Fall 2024"
excerpt: "Designed KV-cache compression and eviction strategies using bit-plane slicing, semantic clustering, and recency-aware prioritization for large-context LLM inference."
tags:
  - LLM Inference
  - KV Cache
  - Compression
  - GPU Systems
  - Research
---

This undergraduate research project investigates memory-efficient KV cache management for large-context transformer inference. KV cache growth is a dominant bottleneck for GPU memory capacity and throughput. This work develops and evaluates structured compression and eviction strategies to extend usable context lengths under fixed memory budgets.

## My Contribution

- Designed a **recency + semantic aware prioritization scheme** for token-level KV retention, combining temporal decay with cluster-level semantic importance.  
- Built a **lightweight lookup index** enabling fast token-to-cluster mapping during inference without noticeable latency overhead.  
- Implemented **bit-plane slicing** for K/V tensors and evaluated reconstruction error under constrained bit budgets to quantify quality-compression tradeoffs.  
- Analyzed compressibility patterns across **layers, heads, and context positions** using Llama 3.1 8B Instruct, mapping compression ratios to KV footprint and perplexity drift.  
- Developed profiling tools and scripts in PyTorch to extract per-layer, per-head KV tensors during autoregressive decoding for targeted analysis.  

## Technical Summary

- **Model:** Llama 3.1 8B Instruct  
- **Languages:** Python, PyTorch  
- **Tools:** HuggingFace Transformers, custom KV-cache dump hooks, GPU profiling  
- **Concepts:** bit-plane compression, semantic clustering, recency heuristics, memory-bounded inference  

## Additional Details

- Implemented hooks to log K/V tensors during decoding, enabling fine-grained analysis of redundancy and sensitivity.  
- Created a hybrid eviction scoring function that balances temporal relevance with semantic token importance for improved retention quality.  
- Identified structural redundancy in **early-layer K-planes** and semantic stability in **deeper-layer V-planes**, suggesting opportunities for layer-aware compression schedules.  
- Built an evaluation pipeline to measure compression ratio, KV footprint reduction, and perplexity drift without needing full retraining.  

## Outcome

Developed functional prototypes demonstrating that structured bit-plane compression and informed eviction policies can significantly reduce KV memory usage while maintaining long-context model quality. This work laid the groundwork for later visualization and profiling tools, including the KV Cache Inspector.
