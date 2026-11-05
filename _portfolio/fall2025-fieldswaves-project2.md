---
title: "Electromechanical System Design and Analysis"
collection: portfolio
permalink: /portfolio/fall2025-fieldswaves-project2/
date: 2025-11-15
excerpt: "DC motor iteration, an RL-plus-back-EMF model in LTspice, oscilloscope comparison, and a mechanically driven generator demonstration."
project_group: coursework-archive
display_year: "2025"
period: "Fall 2025"
sort_key: "2025-Fall"
date_precision: "term"
work_type: "Coursework"
work_category: "coursework"
tags: ["Electromechanics","LTspice","Oscilloscope","Circuit Modeling"]
term: "Fall 2025"
work_source: {}
---

## DC motor iteration

I iterated on a DC motor prototype by reducing the coil winding from 20 to 10 turns, adjusting commutator timing, and reducing mechanical friction. Across these changes, rotational frequency increased from 10 to 60 Hz and circuit resistance was reduced to 0.25 Ω.

| Prototype measure | Initial | Revised |
| :--- | ---: | ---: |
| Coil winding | 20 turns | 10 turns |
| Rotational frequency | 10 Hz | 60 Hz |

The revised circuit resistance was 0.25 Ω.

## Electrical model and measurements

I developed an equivalent RL circuit model with back-EMF in LTspice. I compared simulated transient behavior with oscilloscope voltage measurements to investigate how the electrical model relates to motor operation.

The model and measured voltage transients provided complementary views of the prototype. The mechanical changes, commutator timing, resistance, and back-EMF all mattered to interpreting its behavior.

## Generator operation

I also mechanically drove the motor to demonstrate generator operation. It produced a measured 17.9 mV electrical output without an external electrical supply.
