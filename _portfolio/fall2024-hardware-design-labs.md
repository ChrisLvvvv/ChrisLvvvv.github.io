---
title: "RISC-V Processor Microarchitecture Design"
collection: portfolio
permalink: /portfolio/fall2024-hardware-design/
date: 2024-12-03
excerpt: "Five-stage and multicycle RISC-V implementations with hazard control, FSM sequencing, and self-checking ModelSim verification."
project_group: coursework-archive
display_year: "2024"
period: "Fall 2024"
sort_key: "2024-Fall"
date_precision: "term"
work_type: "Coursework"
work_category: "coursework"
venue: "Rensselaer Polytechnic Institute · ECSE 4770 Computer Hardware Design"
tags: ["SystemVerilog","RISC-V","Pipeline Control","ModelSim"]
term: "Fall 2024"
work_source:
  organization: "RPI"
  course_code: "ECSE 4770"
  course_name: "Computer Hardware Design"
---

## Five-stage processor

For ECSE 4770, I implemented a RISC-V processor with fetch, decode, execute, memory, and writeback stages. I designed hazard-control logic for operand forwarding, pipeline stalls, and control-flow flushing.

The work connected instruction dependencies to datapath selection and pipeline control. Forwarding supplied operands when possible, while stalls and flushes handled cases that required delaying or discarding work.

## Multicycle implementation

I also designed a multicycle processor with FSM-based control. It shares datapath resources across instruction-execution stages and coordinates register, ALU, memory, and PC updates through the control sequence.

## Instruction scope and verification

I implemented R-type arithmetic and load/store, branch, and jump instructions, including lw, sw, beq, and jal. I used self-checking ModelSim testbenches to verify datapath and control behavior.
