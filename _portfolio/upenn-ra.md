---
title: "TileLink Memory Verification for a 28 nm RISC-V Tapeout"
collection: portfolio
permalink: /portfolio/upenn-ra/
display_year: "2026"
period: "Sep. 2026 – Present"
start_month: "2026-09"
end_month: present
sort_key: "2026-09"
date_precision: month
work_type: Research Assistant
work_category: experience
venue: "University of Pennsylvania · The Radway Group"
excerpt: "Reusable TileLink-UL verification with independent memory checking, assertions, fault injection, and automated regressions for a Chipyard-based RISC-V project targeting a TSMC 28 nm tapeout."
project_group: research
tags: [RTL Verification, SystemVerilog, TileLink-UL, Regression Automation]
work_source:
  organization: "UPenn"
  detail: "The Radway Group"
---

## Research context

I work as a Research Assistant in the Radway Group at the University of Pennsylvania in Philadelphia, advised by Prof. Joseph Devietti and Prof. Robert M. Radway. The Chipyard-based RISC-V project targets a TSMC 28 nm tapeout. My work focuses on memory-interface verification; the target process describes the project direction rather than a completed tapeout or full-chip signoff.

## Separating the interface from the checker

I developed a reusable six-component SystemVerilog environment for TileLink-UL memory interfaces. It separates stimulus generation, protocol monitoring, functional checking, and DUT integration so that verification logic can be reused with different memory implementations. A dedicated adapter connects the environment to Chipyard-generated memory RTL, with functional tests run in Cadence Xcelium.

The functional checker uses an independent byte-addressed reference memory and a transaction scoreboard. It checks masked writes, returned read data, source IDs, response opcodes, and transfer sizes without accessing DUT-internal state. X-safe comparisons and explicit detection of unexpected or duplicate responses help distinguish data errors from transaction-accounting errors.

## Assertions and interface contracts

I implemented SystemVerilog Assertions for transaction legality, address alignment, byte masks, unknown signals, and response metadata. Strict A-channel stability is a separately selectable interface contract. Keeping it optional avoids treating an interface-specific assumption as a universal TileLink-UL protocol requirement.

## Parameterized fixture tests

I validated the behavioral-memory fixture with four selected parameter configurations. Together, these span 8-, 32-, and 64-bit data buses, source-ID widths of 1–3 bits, and response latencies of 0, 1, 3, and 7 cycles. These are four configurations, not the full Cartesian product of the listed parameter values.

The fixture tests exercise subword accesses, sparse write masks, address boundaries, A- and D-channel backpressure, and reset during a stalled response. This parameterized behavioral-fixture regression is distinct from functional integration testing against the Chipyard-generated RTL through the adapter.

## Testing the verification environment

I used five fault-injection scenarios to test whether the assertions and scoreboard detect the intended errors. Two cover A-channel payload changes and valid retraction under the optional strict contract. The other three cover read-data corruption, response source-ID corruption, and D-channel payload corruption following a stall.

A Python regression runner automates execution and result classification through GitHub Actions on a self-hosted runner. A negative test counts as a pass only when the log contains evidence that the intended fault was injected and the expected checker failed. Unrelated failures, timeouts, and simulator crashes are rejected rather than accepted as successful error detection.

I verified the regression runner itself with 24 Python unit tests. Those tests exercise the automation and classification logic; they are separate from the hardware fixture configurations, RTL integration tests, and five fault-injection scenarios.
