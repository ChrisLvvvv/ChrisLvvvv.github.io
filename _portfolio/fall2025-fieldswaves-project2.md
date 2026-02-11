---
title: "Electromechanics Modeling and Magnetic Force Analysis"
collection: portfolio
permalink: /portfolio/fall2025-fieldswaves-project2/
date: 2025-11-15
venue: "ECSE 2110 Fields and Waves I – Project 2"
excerpt: "Analytical and computational evaluation of magnetic circuits, flux distribution and electromagnetic force generation using energy and co-energy methods."
tags:
  - Electromagnetics
  - Magnetic Circuits
  - Electromechanics
  - Energy Methods
  - MATLAB
---

This project analyzes electromagnetic energy conversion and magnetic force generation in an electromechanical system. The study integrates magnetic circuit modeling, nonlinear material behavior, and energy based force prediction to understand how magnetic fields perform mechanical work.

## Objectives
- Model magnetic circuits using reluctance and flux relationships.
- Compute magnetic energy, co-energy and force using field-theory based derivations.
- Analyze geometry dependent electromagnetic force in an actuator-like system.
- Validate analytical results using MATLAB based numerical evaluation.

## Technical Work

### Magnetic Circuit Modeling
- Constructed a complete magnetic circuit including:
  - Core regions
  - Air gaps
  - Nonlinear magnetic materials
- Computed **reluctances \( \mathcal{R} \)**, magnetic flux \( \Phi \) and magnetomotive force (MMF).
- Evaluated the equivalent magnetic circuit under varying gap lengths to understand force sensitivity.

### Energy and Co-Energy Analysis
- Derived magnetic **stored energy** \( W_{field} \) and **co-energy** \( W' \):

  \[
  W' = \int_0^{i} \lambda \, di
  \]

  where \( \lambda = N\Phi \) is the flux linkage.
  
- Used the co-energy method to compute force:

  \[
  F = \frac{\partial W'}{\partial x}
  \]

  relating mechanical displacement \( x \) to energy variation.

- Analyzed how force scales with:
  - Coil current  
  - Number of turns  
  - Air-gap thickness  
  - Material permeability  

### Force Prediction vs. Geometry
- Computed electromagnetic force for multiple air-gap distances.
- Built a parametric sweep in MATLAB to evaluate:
  - Flux density distribution
  - Energy trends
  - Force vs. displacement curve
- Identified nonlinear behavior as gaps shrink due to increasing flux density and mmf concentration.

### Numerical Simulation
- Created MATLAB scripts for symbolic and numeric evaluation of:
  - Magnetic flux and mmf  
  - Inductance as a function of gap  
  - Energy and co-energy  
  - Force curves  

- Verified consistency between:
  - Magnetic circuit approximations
  - Energy method predictions
  - Trend expectations from electromechanics theory

## Outcome
This project provided a complete electromechanical characterization of a magnetic actuator system. By modeling the magnetic circuit, deriving energy based force equations, and validating results numerically, the project built strong intuition for how electromagnetic fields convert electrical input into mechanical output. It reinforced core concepts in magnetic circuits, field energy, and the foundations of electric machinery design.
