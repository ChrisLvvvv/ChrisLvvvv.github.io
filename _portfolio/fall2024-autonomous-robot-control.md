---
title: "Autonomous Robotic Control System"
collection: portfolio
permalink: /portfolio/fall2024-autonomous-robot-control/
date: 2024-12-07
excerpt: "Autonomous ARM Cortex-M robotic control system featuring cascaded PI/PD control, sensor fusion and hierarchical FSM navigation."
featured_on_home: true
project_group: systems-hardware
work_excerpt: "Embedded control combining PI wheel-speed regulation, PD heading control, bare-metal sensor drivers, and a navigation FSM for the Hit-the-Targets challenge."
display_year: "2024"
period: "Fall 2024"
sort_key: "2024-Fall"
date_precision: "term"
work_type: "Coursework"
work_category: "coursework"
venue: "Rensselaer Polytechnic Institute · ENGR 2350 Embedded Control"
tags: ["Embedded C","PI/PD Control","ARM Cortex-M","I2C"]
term: "Fall 2024"
work_source:
  organization: "RPI"
  course_code: "ENGR 2350"
  course_name: "Embedded Control"
---

## Closed-loop motion control

For ENGR 2350 in Fall 2024, I implemented an autonomous robotic control system using Embedded C on an ARM Cortex-M platform. PI wheel-speed regulation and PD heading control combined encoder feedback with differential steering to adjust motion under friction and battery variation.

## Drivers and sensing

I developed bare-metal drivers for PWM motor control, ADC sampling, and quadrature-encoder input capture. I integrated a CMPS12 compass/IMU over I2C and ultrasonic sensors for gesture-based control and obstacle detection.

These interfaces connected the control loops to measured motion and the robot's surroundings. Encoder feedback supported wheel-speed regulation, while compass/IMU information supported heading control.

## Navigation and onboard checks

I designed the navigation finite-state machine for the “Hit-the-Targets” challenge. It coordinated search, collision-recovery, and U-turn behaviors using nonblocking timer interrupts.

I tested the behaviors onboard, checking the interaction between sensing, motor control, and navigation state transitions.
