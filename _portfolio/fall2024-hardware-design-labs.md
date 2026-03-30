---
title: "Computer Hardware Design – Lab Skills Summary"
collection: portfolio
permalink: /portfolio/fall2024-hardware-design/
date: 2024-12-03
venue: "ECSE 4770 – Fall 2024"
excerpt: "Summary of hardware design and RISC-V CPU construction skills from ECSE 4770, including SystemVerilog, FSMs, datapath design and multi-cycle/pipelined processors."
project_group: coursework-archive
tags:
  - SystemVerilog
  - Computer Architecture
  - FSM
  - Datapath
  - RISC-V
  - Hardware Design
  - Simulation
---

This page summarizes the major hardware design skills developed through the laboratories in ECSE 4770 Computer Hardware Design. These labs walk through the full construction of a working RISC-V processor, from combinational logic and finite state machines to a complete multi-cycle and pipelined architecture. The course emphasizes SystemVerilog modeling, hierarchical design, testbench creation and architectural debugging.

## Core Skills and Tools

- Modeling combinational and sequential logic in **SystemVerilog**
- Designing and implementing **structural and behavioral FSMs**
- Building RISC-V datapath components including ALU, register file and control units
- Constructing a **single-cycle RISC-V CPU** with full instruction flow
- Extending the design into a **multi-cycle architecture** with microcoded control
- Completing a **multi-cycle control unit** using FSM sequencing
- Implementing **pipelining concepts** and understanding hazards, forwarding and stalls
- Writing and testing assembly routines for RISC-V programs
- Creating comprehensive testbenches and waveform-based debugging using ModelSim or equivalent simulators

## Topics Covered

- Combinational logic analysis and hierarchical SystemVerilog modules  
- Structural vs behavioral FSM modeling  
- ALU design and arithmetic/logic operations  
- Single-cycle processor design and control signal generation  
- Multi-cycle datapath and control sequencing  
- Pipelining concepts (IF, ID, EX, MEM, WB) and hazard behavior  
- Assembly implementation of functions, stack usage and calling conventions  

## Outcome

These labs provided hands-on experience implementing and validating real processor components and control structures. By progressing from simple combinational circuits to full RISC-V CPU implementations, the course built strong proficiency in SystemVerilog, computer architecture and simulation-driven hardware debugging. This foundation directly supports later advanced work in GPU kernel research, architecture-aware optimization and embedded hardware projects.
