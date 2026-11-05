---
title: "Two-Wide Out-of-Order Execution Core"
collection: portfolio
permalink: /portfolio/two-wide-out-of-order-execution-core/
display_year: "2026"
period: "Spring 2026"
sort_key: "2026-Spring"
date_precision: term
work_type: Coursework
work_category: coursework
venue: "Rensselaer Polytechnic Institute · ECSE 4780 Advanced Computer Hardware Design"
excerpt: "A 32-bit Tomasulo-style execution core with two-wide dispatch, register renaming, an eight-entry ROB, conservative memory ordering, and self-checking simulation."
project_group: systems-hardware
tags: [SystemVerilog, Out-of-Order Execution, ModelSim, Microarchitecture]
term: "Spring 2026"
work_source:
  organization: "RPI"
  course_code: "ECSE 4780"
  course_name: "Advanced Computer Hardware Design"
---

## Execution-core scope

I implemented a 32-bit Tomasulo-style execution core for ECSE 4780 in Spring 2026 using SystemVerilog, ModelSim, and Intel Quartus Prime Lite. The supported instruction subset is ADD, MUL, LW, SW, and NOP.

The core combines two-wide in-order dispatch with dynamic execution scheduling and an eight-entry circular reorder buffer (ROB). It supports up to two in-order commits per cycle; that is a retirement capacity, rather than a measured sustained IPC result.

## Renaming and dependency handling

I designed register-alias-table (RAT) renaming so that the second dispatch slot can observe dependencies created by the first slot in the same cycle. Retirement preserves a younger destination mapping when an older writer commits. Value/tag operand tracking handles RAW, WAR, and WAW cases without allowing an older result to overwrite the identity of a newer producer.

Execution selection and single-common-data-bus (CDB) arbitration use instruction age relative to the ROB head. Completed results remain pending until the bus grants access. The nonpipelined add, multiply, and load/store units have execution latencies of four, six, and two cycles respectively.

## Backpressure and memory ordering

Dispatch checks ROB, reservation-station, and load/store-queue capacity. The second slot cannot bypass a blocked first slot, and instruction-queue contents are preserved during stalls.

A four-entry FIFO load/store queue tracks dependencies for base addresses and store data. Only its head can issue a memory operation, and a store can issue only when it also reaches the ROB head. This conservative design does not use load bypass or store-to-load forwarding.

## Self-checking verification

I developed ModelSim testbenches for same-cycle rename dependencies, structural stalls, CDB contention, memory ordering, and ROB-head blocking. The checks compare final register and memory values and require every queue, execution unit, and pending result to drain before completion.

The project focuses on this execution-core subset and its scheduling and ordering behavior.
