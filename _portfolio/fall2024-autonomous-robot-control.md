---
title: "Autonomous Robotic Control System"
collection: portfolio
permalink: /portfolio/fall2024-autonomous-robot-control/
date: 2024-12-07
venue: "ENGR 2350 Embedded Control – Fall 2024"
excerpt: "Autonomous ARM Cortex-M robotic control system featuring cascaded PI/PD control, sensor fusion and hierarchical FSM navigation."
tags:
  - Embedded Systems
  - Robotics
  - MSP432
  - Sensor Fusion
  - PWM
  - PID Control
  - I2C
  - C Programming
---

This project implements a full autonomous navigation system on the ARM Cortex-M-based MSP432, integrating wheel-speed control, heading stabilization, sensor fusion and behavior-level decision making. The robot operates independently inside a bounded arena and uses multiple sensing modalities to detect collisions, maintain orientation and steer toward targets.

## My Contribution

- Designed and implemented the cascading closed-loop controller architecture:
  - **PI control** regulating wheel speed using quadrature encoder feedback to compensate for load variation, friction and battery voltage sag.
  - **PD control** for heading stabilization using inertial/compass sensor data, enabling smooth differential steering and reduced steady-state tracking error.
- Developed bare-metal embedded drivers including:
  - **PWM generation** for motor actuation  
  - **ADC sampling** for analog measurements  
  - **Timer input-capture** for quadrature encoder decoding  
  - **I²C communication** with the CMPS12 IMU/compass  
  - **Ultrasonic sensor integration** for collision and obstacle response
- Constructed a hierarchical **Finite State Machine** (FSM) that orchestrates behaviors such as:
  - Search / forward exploration  
  - Collision detection and recovery  
  - Controlled U-turn and re-entry into the field  
- Implemented non-blocking timing and internal state scheduling using timer interrupts to maintain real-time responsiveness and prevent motion freeze during sensing events.
- Conducted real-time telemetry logging through UART for debugging controller stability, wheel speed profiles and heading corrections.

## Technical Summary

- **Microcontroller:** TI MSP432 (ARM Cortex-M4F)  
- **Sensors:** CMPS12 IMU/compass (I²C), ultrasonic distance sensor, wheel encoders  
- **Control Algorithms:** Cascaded PI/PD, differential drive, encoder-based tachometer  
- **Software:** Bare-metal C, modular drivers, FSM-based architecture  
- **Actuation:** Dual H-bridge motor control using PWM and direction lines  
- **Toolchain:** Code Composer Studio (CCS), logic analyzer, serial telemetry  

## Outcome

The system achieved reliable autonomous behavior within the competition environment using robust closed-loop speed control, sensor fusion and structured state-machine logic. This project demonstrates strong proficiency in embedded C, ARM-level driver development, real-time control and robotics-oriented system integration.
