---
title: "SRAM-Based 4-bit MAC Accelerator (Transistor-Level)"
collection: portfolio
permalink: /portfolio/sram-4bit-mac-accelerator/
# Date of the Part 3 report's PDF creation metadata, not an inferred course deadline.
date: 2026-10-27
venue: "University of Pennsylvania · ESE 5700 · Fall 2026"
project_group: coursework-archive
work_category: coursework
work_type: Coursework
tags:
  - SRAM
  - VLSI
  - Transistor-Level Design
excerpt: "Transistor-level design of a 16-element, 4-bit dot-product engine with custom SRAM, sequenced accumulation, and full-system verification using post-layout extracted memory arrays."
cover_image: /images/projects/sram-4bit-mac/system-overview.png
cover_alt: "MAC block diagram connecting two 16 × 4 SRAMs, the sequencer, multiplier, adder, and accumulator."
cover_caption: "System architecture · Part 3, Figure 1"
images:
  # Part 3, p. 2, Figure 1. Cropped from the report's vector block diagram.
  - src: /images/projects/sram-4bit-mac/system-overview.png
    alt: "MAC architecture with two extracted 16 × 4 SRAM arrays, multiplier-adder, 12-bit accumulator, sequencer, and clock generators."
    caption: "System organization reconstructed from the exported transistor-level Top. Both SRAM arrays use extracted views. Part 3, Figure 1."
    full_size: true
  # Part 2, p. 2, Figure 1. Both the complete array and adjacent-cell detail are retained.
  - src: /images/projects/sram-4bit-mac/sram-array-layout.png
    alt: "Virtuoso layout of the 16-row, four-column SRAM array, alongside an enlarged view of neighboring mirrored bitcells with original layer colors."
    caption: "Custom 16 × 4 SRAM array and neighboring-cell detail; array-only area is approximately 190 µm². Part 2, Figure 1."
    full_size: true
  # Part 3, p. 54, Figure 36. Actual full-MAC transient data, not the 4-ns sequencer schedule.
  - src: /images/projects/sram-4bit-mac/full-mac-test-a.png
    alt: "Full-MAC Test A transient traces at a 3.2 ns period: CLK, START, ACC_EN, DONE, address, W/X SRAM outputs, and ACC reaching 845 after E17."
    caption: "Reported full-MAC Test A at TT, 27 °C, 0.8 V and T = 3.2 ns. Analog bus transitions retain invalid-band gaps; ACC finishes at 845. Part 3, Figure 36."
    full_size: true
term: "Fall 2026"
work_source:
  organization: "UPenn"
  course_code: "ESE 5700"
  course_name: "Digital Integrated Circuits"
---

## Overview

This accelerator computes a 16-element unsigned dot product:

$$\mathrm{ACC}=\sum_{i=0}^{15}W[i]\,X[i].$$

Two independent 16 × 4 SRAMs store weights and activations. Their outputs feed a 4 × 4 multiplier and a 12-bit accumulator. The maximum result, 16 × 15 × 15 = 3600, fits within 12 bits without overflow.

I designed and characterized the registers and accumulator, implemented the sequencer, integrated the MAC, and developed the full-system testbenches. Zhixin He developed the SRAM macro and arithmetic datapath; debugging and review were shared.

The implementation uses Cadence GPDK / CDS_FF_MPT 18 nm FinFET devices, Virtuoso, Spectre/ADE, Quantus, and Pegasus. The reported full-system simulations combine two post-layout extracted SRAM arrays with transistor-level schematic/netlist implementations of the periphery and MAC logic. The complete accelerator was not physically laid out.

## Bitcell and SRAM Macro

I compared cell ratios to balance read stability against transistor area and writability. The Part 1 cell uses two-fin pull-ups, three-fin pull-downs, and two-fin access devices. Stronger pull-downs suppress read disturbance, but increasing their size gives diminishing noise-margin improvements and costs area.

Post-layout characterization at 0.8 V gave approximately 0.28 V hold SNM, 0.14 V read SNM, 0.24 V bitline write margin, and 24 µA read current. Supply sweeps at 0.7 and 0.5 V exposed shrinking margins. Transient writes and reads checked that accesses changed the intended state without destructive reads.

<!-- ESE5700_Project1_P1.pdf, p. 10, Figure 8. Original Part 1 revision. -->
<figure class="project-figure project-figure--narrow">
  <a class="project-image-link" href="{{ '/images/projects/sram-4bit-mac/read-snm.png' | relative_url }}" target="_blank" rel="noopener" aria-label="Open full-size post-layout read SNM plot">
    <img src="{{ '/images/projects/sram-4bit-mac/read-snm.png' | relative_url }}" alt="Part 1 post-layout read-SNM butterfly plot at TT, VDD = WL = 0.8 V and cell ratio 1.5, showing lobe margins of 149.4 and 144.9 mV." loading="lazy" decoding="async" width="1244" height="1493">
  </a>
  <figcaption>Original Part 1 bitcell: read SNM is the smaller lobe margin, 144.9 mV. Part 1, Figure 8.</figcaption>
</figure>

The custom bitcell and mirrored 16 × 4 array passed Pegasus DRC/LVS and Quantus extraction. Part 2 revised the bitcell routing and repeated characterization. Array loading therefore uses that revision’s extracted baseline; it does not combine the original Part 1 parasitics with the revised array.

The synchronous macro combines registered inputs, row decoding, precharge/equalization, complementary write drivers, a full-swing BLB read inverter, and an output latch. This read path needs substantial bitline discharge rather than a small differential. The latch preserves DOUT during precharge and writes. Unit tests progressed from the cell to extracted-array column tests and then the controller-driven macro.

## Datapath and Sequential Circuits

The multiplier forms sixteen partial products and reduces them with half/full adders. Its eight-bit result connects directly to the optimized 12-bit ripple-carry adder. There is no product register.

Selective sizing doubled the multiplicity of 22 carry-path NAND2 cells while leaving XOR sum networks unchanged. Standalone adder delay fell from about 931 to 852 ps, approximately 8.5%, at an estimated area cost of 110 µm². This is a local arithmetic improvement, not an 8.5% accelerator speedup.

I implemented positive-edge master-slave transmission-gate registers with static feedback and nonoverlapping clock phases. Accumulator input selection provides synchronous clear, load, and hold, with clear taking priority; the clock itself remains ungated.

Timing characterization checked both data polarities using functional capture and a 5% clock-to-Q degradation criterion. The final shared clock generator drives 21 sequencer/accumulator DFFs; each SRAM retains its own nine-DFF generator. I used these actual fanouts when checking setup and hold rather than extrapolating the original register bench.

## Sequencing and System Integration

I combined a four-bit address counter with an IDLE / COMPUTE / DONE FSM. External loading selects the shared address and data buses with independent memory write enables; computation selects the counter and disables writes.

READ_VALID marks an issued read that can be consumed. LAST_PENDING records the terminal address so the final product is captured before DONE. The SRAM output latch is the memory-read pipeline boundary: a new SRAM read overlaps accumulation of the preceding operands.

Taking the START-sampling edge as E0, E1–E16 read addresses 0–15, while E2–E17 perform sixteen accumulator updates. Completion takes **17 periods**, not sixteen. DONE then remains asserted and ACC holds its result. Synchronous reset takes priority; START can restart an active operation or begin another dot product.

<!-- ESE5700_Project1_P3.pdf, p. 44, Figure 31. Control-only 4-ns test with scheduled annotations. -->
<figure class="project-figure">
  <a class="project-image-link" href="{{ '/images/projects/sram-4bit-mac/sequencer-schedule.png' | relative_url }}" target="_blank" rel="noopener" aria-label="Open full-size 17-cycle sequencer schedule">
    <img src="{{ '/images/projects/sram-4bit-mac/sequencer-schedule.png' | relative_url }}" alt="Seventeen-cycle sequencer schedule from E0 to E17 at a 4 ns period, with measured control signals and annotated SRAM read and accumulator capture indices." loading="lazy" decoding="async" width="1847" height="1343">
  </a>
  <figcaption>Sequencer test at TT, 27 °C, 0.8 V and T = 4 ns: controls are measured; reads and captures are scheduled annotations. Part 3, Figure 31.</figcaption>
</figure>

## Verification

Verification was hierarchical. The SRAM tests exercised checkerboard words, complements, and immediate write/read sequences. Register, counter, FSM, pipeline-control, and accumulator tests checked their local behavior before integration. The schematic-derived integrated datapath passed 384 vectors, including operand combinations and directed/pseudorandom accumulator cases.

I then tested operand loading, feedback accumulation, DONE, result retention, and reset/restart on the complete MAC with both extracted arrays. Checks combined valid voltage bands, control-edge ordering, and register setup/hold windows. These are simulation-based checks of applied stimuli, not formal verification or complete state-space coverage.

<table class="project-results project-results--tests">
  <caption>Reported full-system results at TT, 27 °C, 0.8 V and T = 3.2 ns.</caption>
  <thead><tr><th>Test</th><th>Expected ACC</th><th>Simulated ACC</th><th>Cycles</th><th>Result</th></tr></thead>
  <tbody>
    <tr><th scope="row">A</th><td>845</td><td>845</td><td>17</td><td>PASS</td></tr>
    <tr><th scope="row">B</th><td>3600</td><td>3600</td><td>17</td><td>PASS</td></tr>
    <tr><th scope="row">C</th><td>800</td><td>800</td><td>17</td><td>PASS</td></tr>
  </tbody>
</table>

## Results and Design Trade-offs

All final metrics use Part 3’s integrated configuration at **TT, 27 °C, VDD = 0.8 V**.

<table class="project-results">
  <caption>Nominal integrated results, reported to approximately two significant figures.</caption>
  <thead><tr><th>Metric</th><th>Result</th></tr></thead>
  <tbody>
    <tr><th scope="row">Shortest tested accepted period</th><td>3.2 ns</td></tr>
    <tr><th scope="row">START-to-DONE</th><td>17 periods</td></tr>
    <tr><th scope="row">Nominal dot-product latency</th><td>≈ 54 ns</td></tr>
    <tr><th scope="row">Test A compute energy</th><td>≈ 19 pJ / dot product</td></tr>
    <tr><th scope="row">Test A energy per MAC, including SRAM</th><td>≈ 1.2 pJ</td></tr>
    <tr><th scope="row">Estimated total area</th><td>≈ 4.5 × 10³ µm²</td></tr>
  </tbody>
</table>

The accepted period requires correct arithmetic and control timing. At 3.1 ns, Test A still computes correctly, but write-control release overlaps precharge during loading. SRAM pulse ordering therefore sets the tested limit. The faster adder adds capture headroom without changing the final 3.2 ns period.

Compute energy integrates supply current from the START-sampling clock crossing to the actual DONE crossing, excluding operand loading. Nominal latency uses seventeen clock periods. Area combines actual array layout areas with estimates for the remaining circuits, counted from Part 3’s instantiated hierarchy rather than twice the standalone Part 2 macro estimate.

<!-- ESE5700_Project1_P3.pdf, p. 57, Figure 37. Original measured branch and A/B/C energy plots. -->
<figure class="project-figure">
  <a class="project-image-link" href="{{ '/images/projects/sram-4bit-mac/compute-energy.png' | relative_url }}" target="_blank" rel="noopener" aria-label="Open full-size compute energy comparison">
    <img src="{{ '/images/projects/sram-4bit-mac/compute-energy.png' | relative_url }}" alt="Reported energy at 3.2 ns: Test A supply branches MW 5.839, MX 5.827, DP 3.386, ACC 1.580 and CTRL 2.303 pJ; total energies A 18.9350, B 17.0468 and C 17.9320 pJ." loading="lazy" decoding="async" width="1876" height="734">
  </a>
  <figcaption>Reported compute energy at 3.2 ns, using actual START-to-DONE windows and excluding loading. Part 3, Figure 37.</figcaption>
</figure>

The two complete SRAM supply branches contribute about 62% of Test A compute energy. Test C switches operand bits heavily but keeps the settled product at 50; Test A’s varying products consume more datapath and accumulator energy. Input toggling alone does not rank total energy.

Future work could retime write-off/precharge or reduce arithmetic sizing while preserving capture margin. These are proposed improvements, separate from the implemented results.
