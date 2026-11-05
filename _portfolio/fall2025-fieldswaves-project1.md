---
title: "Wave Propagation and Transmission Line Analysis"
collection: portfolio
permalink: /portfolio/fall2025-fieldswaves-project1/
date: 2025-10-20
venue: "Rensselaer Polytechnic Institute · ECSE 2100 Fields and Waves I"
excerpt: "Analytical and MATLAB based study of wave propagation, impedance transformation, reflection behavior and power flow along transmission lines at high frequencies."
project_group: coursework-archive
tags:
  - Electromagnetics
  - Transmission Lines
  - Smith Chart
  - MATLAB
  - RF Engineering
display_year: "2025"
period: "Fall 2025"
date_precision: "term"
work_type: "Coursework"
term: "Fall 2025"
work_source:
  organization: "RPI"
  course_code: "ECSE 2100"
  course_name: "Fields and Waves I"
---

This project analyzes electromagnetic wave propagation on transmission lines through a combination of analytical derivations and MATLAB-based computation. It focuses on characterizing reflection behavior, impedance transformation, and power delivery at gigahertz frequencies using the transmission line (TL) equations and Smith Chart techniques.

## Objectives
- Determine reflection coefficient, input impedance, and voltage standing wave ratio (VSWR) for a lossy transmission line.
- Analyze impedance transformation as a function of line length and load characteristics.
- Evaluate power flow, delivered power ratio, and reflected power under mismatched load conditions.
- Use MATLAB and manual derivations to compute TL parameters at high frequency (2.4 GHz).

## Technical Work

### Transmission Line Parameters
- Computed the **propagation constant** γ, attenuation constant α, and phase constant β.
- Evaluated **characteristic impedance** \( Z_0 \) for a lossy line based on per-unit-length R, L, G, C parameters.
- Analyzed line behavior in both long-line and electrically short-line regimes.

### Reflection and Impedance Analysis
- Derived the **load reflection coefficient**:

  <div class="project-formula" markdown="1" role="region" aria-label="Load reflection coefficient formula" tabindex="0">

  \[
  \Gamma_L = \frac{Z_L - Z_0}{Z_L + Z_0}
  \]

  </div>

- Evaluated **SWR**, **return loss**, and **mismatch loss**.
- Computed **input impedance \( Z_{in}(d) \)** at various distances using:

  <div class="project-formula" markdown="1" role="region" aria-label="Input impedance formula" tabindex="0">

  \[
  Z_{in}(d)=Z_0\frac{Z_L+Z_0\tanh(\gamma d)}{Z_0+Z_L\tanh(\gamma d)}
  \]

  </div>

- Compared hand-computed values with MATLAB simulations to validate correctness.

### Smith Chart Interpretation
- Used the Smith Chart to:
  - Visualize normalized impedances  
  - Trace impedance transformation along the TL  
  - Identify matching conditions and distances  
- Cross-checked graphical Smith Chart results with analytical/mathematical computation.

### Power Flow Computation
- Calculated:
  - Incident and reflected wave amplitudes  
  - Delivered power ratio \( P_{delivered}/P_{incident} \)  
  - Fraction of power lost due to mismatch  
- Analyzed power delivery at **2.4 GHz**, demonstrating frequency-dependent sensitivity to mismatch and line length.

## Tools and Methods
- MATLAB scripts for numeric TL calculation, wave visualization, and complex impedance analysis.
- Hand derivations for TL formulas, reflection relationships, and impedance transformation.
- Smith Chart analysis for graphical impedance matching and validation.

## Outcome
This project provided a full analytical and computational characterization of transmission line behavior under mismatched loading. It reinforced core concepts of wave propagation, impedance transformation and RF power delivery, while building practical proficiency with MATLAB, Smith Charts, and high-frequency electromagnetic modeling.
