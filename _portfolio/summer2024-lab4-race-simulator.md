---
title: "Pipeline Race Simulator"
collection: portfolio
permalink: /portfolio/summer2024-lab4-race/
date: 2024-08-01
venue: "COMP Architecture & Networks – Summer 2024"
excerpt: "Implemented a cycle-accurate simulator analyzing pipeline behavior, hazards and performance under race conditions."
project_group: coursework-archive
tags:
  - Computer Architecture
  - Pipeline
  - Simulation
  - C Programming
---

This project implements a cycle-accurate pipeline race simulator to study instruction flow, hazards and execution timing in a simplified processor. The simulator models stalls, forwarding decisions and race outcomes based on the given instruction stream.

## My Contribution
- Implemented the full pipeline logic in C, including cycle stepping and state updates  
- Simulated race-related hazards and verified correctness across instruction sequences  
- Collected timing results and analyzed performance behavior under different workloads  
- Compared outcomes with reference traces to validate correctness  

## Technical Summary
- **Language:** C  
- **Concepts:** pipeline hazards, forwarding, race conditions, timing analysis  
- **Output:** execution cycles, per-stage status, hazard detection  

## Outcome
Completed a fully functional pipeline simulator illustrating the internal behavior of pipelined execution and race handling at the architectural level.
