---
title: "KV Cache Compression and Bit-Plane Eviction Scheduling"
collection: portfolio
permalink: /portfolio/fall2024-kv-cache-compression/
date: 2024-12-01
excerpt: "Designed KV-cache compression and eviction strategies using bit-plane slicing, semantic clustering, and recency-aware prioritization for large-context LLM inference."
featured_on_home: true
project_group: research
work_title: "KV-Cache Efficiency with Semantic-Temporal Retention"
work_excerpt: "A memory-budgeted semantic-temporal KV-retention policy, evaluated against recency-based retention and bit-plane precision-reduction baselines."
display_year: "2024"
period: "Aug. 2024 – Dec. 2024"
start_month: "2024-08"
end_month: "2024-12"
sort_key: "2024-08"
date_precision: "month"
work_type: "Undergraduate Research Program"
work_category: "experience"
venue: "Rensselaer Polytechnic Institute · Undergraduate Research Program"
tags: ["KV Cache","Semantic Clustering","Temporal Retention","Memory Efficiency"]
work_source:
  organization: "RPI"
  detail: "URP"
---

## Research setting

I worked on KV-cache efficiency through Rensselaer Polytechnic Institute's Undergraduate Research Program in Troy, New York, from August to December 2024. Prof. Tong Zhang advised the project, with Dr. Rui Xie as my mentor.

## Understanding the memory budget

I profiled KV-cache growth during LLaMA 3.1 8B inference. The FP16 cache footprint was approximately 128 KB per token, reaching about 1 GB for an 8K-token context. This motivated examining which context information to retain when cache capacity is constrained.

## Semantic-temporal retention

I designed a memory-budgeted retention policy that combines semantic clustering with temporal recency. Rather than prioritizing tokens only by age, the policy considers their semantic grouping alongside how recently they were used.

I prototyped token-to-cluster mapping and lookup mechanisms to support assignment and retrieval of retained entries during autoregressive decoding.

## Comparing retention and precision

I evaluated memory-quality trade-offs by comparing the semantic-temporal policy with recency-based retention and bit-plane precision-reduction baselines. The semantic-temporal policy and lookup prototype were my design work; recency retention and bit-plane reduction served as comparison methods.
