---
layout: single
title: "CV"
permalink: /cv/
intro: "Electrical engineering student focused on computer systems, hardware efficiency, embedded systems, and implementation-heavy research."
redirect_from:
  - /resume
---

<div class="cv-page">
  <section class="cv-hero">
    <div class="cv-hero__main">
      <p class="cv-hero__name">Taoyu Lyu</p>
      <p class="cv-hero__summary">Computer systems, hardware design, GPU inference, embedded control, and performance-oriented engineering.</p>
    </div>
    <div class="cv-hero__contact">
      <p><a href="mailto:taoyu9536@gmail.com">taoyu9536@gmail.com</a></p>
      <p><a href="https://www.linkedin.com/in/taoyulyu/">linkedin.com/in/taoyulyu</a></p>
      <p><a href="https://github.com/ChrisLvvvv">github.com/ChrisLvvvv</a></p>
    </div>
  </section>

  <section class="cv-section">
    <div class="cv-section__heading">
      <h2>Education</h2>
    </div>
    <article class="cv-entry">
      <header class="cv-entry__header">
        <div>
          <h3>Rensselaer Polytechnic Institute (RPI)</h3>
          <p class="cv-entry__subhead">Bachelor of Science in Electrical Engineering, Minor in Economics</p>
        </div>
        <div class="cv-entry__meta">
          <p>Troy, NY</p>
          <p>Aug. 2022 - June 2026</p>
        </div>
      </header>
      <div class="cv-entry__body">
        <ul>
          <li>Cumulative GPA: <strong>3.36/4.0</strong></li>
          <li>Recent academic trend: <strong>3.58</strong> in Fall 2025, <strong>3.77</strong> in Fall 2024, and <strong>3.92</strong> in Summer 2024, with Dean's Honor List recognition.</li>
          <li>Relevant coursework includes Computer Hardware Design, Computer Architecture and Networks, Advanced Computer Hardware Design, Embedded Control, VLSI Design, Signals and Systems, and Fields and Waves.</li>
        </ul>
      </div>
    </article>
  </section>

  <section class="cv-section">
    <div class="cv-section__heading">
      <h2>Research Experience</h2>
    </div>

    <article class="cv-entry">
      <header class="cv-entry__header">
        <div>
          <h3>Rensselaer Polytechnic Institute</h3>
          <p class="cv-entry__subhead">Undergraduate Research Program, Advisor: Prof. Liu Liu</p>
        </div>
        <div class="cv-entry__meta">
          <p>Troy, NY</p>
          <p>Aug. 2025 - Present</p>
        </div>
      </header>
      <div class="cv-entry__body">
        <p class="cv-entry__project">Project: High-Performance GPU Kernel Design for LLM Inference (vLLM)</p>
        <ul>
          <li>Analyzed the vLLM architecture with emphasis on PagedAttention, non-contiguous memory management, the KV cache block manager, and centralized scheduling for logical-to-physical block mapping.</li>
          <li>Benchmarked system behavior on local GPU clusters to study how block size affects memory occupancy, swap overhead, and kernel latency.</li>
          <li>Investigating kernel-level bottlenecks in Mixture-of-Experts architectures and designing custom CUDA kernels to improve expert routing efficiency and reduce memory bandwidth pressure.</li>
        </ul>
      </div>
    </article>

    <article class="cv-entry">
      <header class="cv-entry__header">
        <div>
          <h3>Independent Research Project</h3>
          <p class="cv-entry__subhead">Undergraduate Researcher, Advisor: Hongchen Tan</p>
        </div>
        <div class="cv-entry__meta">
          <p>Remote</p>
          <p>Aug. 2025 - Present</p>
        </div>
      </header>
      <div class="cv-entry__body">
        <p class="cv-entry__project">Project: ConTextGAT — Geometric Spatiotemporal EEG-Text Alignment via Contrastive Learning</p>
        <ul>
          <li>Conducted independent research on multimodal representation learning for sentence-level EEG-to-text retrieval using the ZuCo 2.0 dataset.</li>
          <li>Designed a dual-tower EEG-text model with a geometric-aware EEG encoder using GeoGAT, temporal transformers, and learnable-query cross-attention for long EEG sequences.</li>
          <li>Developed multi-positive contrastive objectives with hard-negative mining to align EEG embeddings with BERT sentence representations under noisy neural signals.</li>
          <li>Engineered balanced batch sampling, staged freezing and unfreezing, and a UNIQUE_EVAL protocol to reduce bias and evaluate retrieval performance with R@K and MRR.</li>
        </ul>
      </div>
    </article>

    <article class="cv-entry">
      <header class="cv-entry__header">
        <div>
          <h3>Rensselaer Polytechnic Institute</h3>
          <p class="cv-entry__subhead">Undergraduate Research Program, Advisor: Prof. Tong Zhang</p>
        </div>
        <div class="cv-entry__meta">
          <p>Troy, NY</p>
          <p>Aug. 2024 - Dec. 2024</p>
        </div>
      </header>
      <div class="cv-entry__body">
        <p class="cv-entry__project">Project: Enhancing KV Cache Efficiency with Compression and Bit-Plane Eviction</p>
        <ul>
          <li>Started from a hardware-oriented bit-plane eviction direction inspired by SmartQuant, then identified a critical long-context quality bottleneck caused by semantic information loss.</li>
          <li>Developed a content-aware hybrid compression strategy combining semantic similarity and temporal recency to balance short-term relevance with long-term memory retention.</li>
          <li>Designed a tree-based indexing structure to reduce token-to-cluster lookup overhead during decoding.</li>
          <li>Integrated clustering with bit-plane compression on LLaMA models and validated improved memory-quality tradeoffs compared with random eviction.</li>
        </ul>
      </div>
    </article>
  </section>

  <section class="cv-section">
    <div class="cv-section__heading">
      <h2>Professional Experience</h2>
    </div>

    <article class="cv-entry">
      <header class="cv-entry__header">
        <div>
          <h3>Huichuang Medical Equipment</h3>
          <p class="cv-entry__subhead">R&amp;D Intern, Hardware Team</p>
        </div>
        <div class="cv-entry__meta">
          <p>Beijing, China</p>
          <p>Feb. 2025 - Aug. 2025</p>
        </div>
      </header>
      <div class="cv-entry__body">
        <ul>
          <li>Redesigned schematics and a 4-layer PCB layout for an STM32-based multi-board control system using Altium Designer and KiCad for a Transcranial Magnetic Stimulation device platform.</li>
          <li>Analyzed instability in legacy hardware and executed component replacement decisions that improved reliability and noise immunity.</li>
          <li>Wrote a 30,000-word technical manual covering circuit analysis, calibration procedures, and standardized QA workflows.</li>
        </ul>
      </div>
    </article>

    <article class="cv-entry">
      <header class="cv-entry__header">
        <div>
          <h3>Yuwell Global</h3>
          <p class="cv-entry__subhead">Hardware Engineer Intern</p>
        </div>
        <div class="cv-entry__meta">
          <p>Danyang, China</p>
          <p>May 2023 - Aug. 2023</p>
        </div>
      </header>
      <div class="cv-entry__body">
        <ul>
          <li>Managed SMT soldering and signal verification for early YHT series infrared thermometer prototypes using Heimann sensors.</li>
          <li>Led root-cause analysis on units returned from the Japanese market, using oscilloscopes to isolate power-management and display failures.</li>
          <li>Worked with firmware engineers to trace power-gating behavior, validate fixes, and improve standby power behavior.</li>
        </ul>
      </div>
    </article>

    <article class="cv-entry">
      <header class="cv-entry__header">
        <div>
          <h3>Yuwell Global</h3>
          <p class="cv-entry__subhead">Test Engineer Intern</p>
        </div>
        <div class="cv-entry__meta">
          <p>Danyang, China</p>
          <p>Apr. 2022 - Aug. 2022</p>
        </div>
      </header>
      <div class="cv-entry__body">
        <ul>
          <li>Executed EMI and EMS testing under CISPR 22 (GB/T 9254) and IEC 61000-4, including ESD and radiated immunity procedures.</li>
          <li>Supported hardware verification and documentation for CE and FCC certification workflows.</li>
        </ul>
      </div>
    </article>
  </section>

  <section class="cv-section">
    <div class="cv-section__heading">
      <h2>Selected Projects</h2>
      <p class="cv-section__note">A compact project snapshot. <a href="/projects/">View the full Projects page</a>.</p>
    </div>

    <article class="cv-entry cv-entry--compact">
      <header class="cv-entry__header">
        <div>
          <h3>Advanced Computer Systems: Full-Stack Profiling and Optimization</h3>
          <p class="cv-entry__subhead">C++, FIO, Python, Linux Perf, Bash, libnuma, OpenMP, AVX-512, Pthreads</p>
        </div>
        <div class="cv-entry__meta">
          <p>Fall 2025</p>
        </div>
      </header>
      <div class="cv-entry__body">
        <ul>
          <li>Built profiling workflows for memory hierarchy latency, memory-level parallelism saturation, and NVMe SSD throughput-latency behavior using pointer-chasing, fio, and Python analysis.</li>
          <li>Designed benchmarks for CPU affinity, NUMA, and SMT behavior and quantified thread-placement and cross-socket tradeoffs on Linux systems.</li>
          <li>Implemented dense and CSR-sparse GEMM kernels with OpenMP and auto-vectorization, then used Roofline analysis to compare compute and memory bounds.</li>
        </ul>
      </div>
    </article>

    <article class="cv-entry cv-entry--compact">
      <header class="cv-entry__header">
        <div>
          <h3>RISC-V Processor Microarchitecture Design</h3>
          <p class="cv-entry__subhead">SystemVerilog, ModelSim, Assembly</p>
        </div>
        <div class="cv-entry__meta">
          <p>Fall 2024</p>
        </div>
      </header>
      <div class="cv-entry__body">
        <ul>
          <li>Engineered a 5-stage pipelined RV32I processor with forwarding, stalling, and hazard detection for data and control hazards.</li>
          <li>Designed a multicycle processor with an FSM-based controller to share resources more efficiently.</li>
          <li>Verified instruction behavior for core operations including R-type execution, loads and stores, branches, and jumps using ModelSim testbenches.</li>
        </ul>
      </div>
    </article>

    <article class="cv-entry cv-entry--compact">
      <header class="cv-entry__header">
        <div>
          <h3>Autonomous Robotic Control System</h3>
          <p class="cv-entry__subhead">Embedded C, ARM Cortex-M, PID Control, I2C, UART</p>
        </div>
        <div class="cv-entry__meta">
          <p>Fall 2024</p>
        </div>
      </header>
      <div class="cv-entry__body">
        <ul>
          <li>Built a cascaded PI/PD control architecture for wheel-speed regulation and heading stabilization with differential steering.</li>
          <li>Developed bare-metal drivers for PWM, ADC, quadrature encoders, I2C IMU and compass integration, and ultrasonic sensing.</li>
        </ul>
      </div>
    </article>

    <article class="cv-entry cv-entry--compact">
      <header class="cv-entry__header">
        <div>
          <h3>Electromechanical System Design and Analysis</h3>
          <p class="cv-entry__subhead">LTSpice, Oscilloscope, Circuit Modeling</p>
        </div>
        <div class="cv-entry__meta">
          <p>Fall 2025</p>
        </div>
      </header>
      <div class="cv-entry__body">
        <ul>
          <li>Optimized a DC motor design through coil, timing, resistance, and friction changes that increased rotational speed from 10 Hz to 60 Hz.</li>
          <li>Built and validated an equivalent SPICE model for transient current behavior and correlated simulated behavior with oscilloscope measurements.</li>
        </ul>
      </div>
    </article>
  </section>

  <section class="cv-section cv-section--split">
    <div class="cv-section__column">
      <div class="cv-section__heading">
        <h2>Certifications</h2>
      </div>
      <article class="cv-entry cv-entry--compact">
        <header class="cv-entry__header">
          <div>
            <h3>Lean Six Sigma Green Belt Certification</h3>
            <p class="cv-entry__subhead">IEEE</p>
          </div>
          <div class="cv-entry__meta">
            <p>2023</p>
          </div>
        </header>
      </article>
    </div>

    <div class="cv-section__column">
      <div class="cv-section__heading">
        <h2>Technical Skills</h2>
      </div>
      <div class="cv-skill-groups">
        <div class="cv-skill-group">
          <h3>Languages</h3>
          <p>C, C++, SystemVerilog, Python, RISC-V/MIPS/x86 Assembly, Bash, LaTeX, Verilog</p>
        </div>
        <div class="cv-skill-group">
          <h3>Hardware &amp; Embedded</h3>
          <p>STM32 (ARM Cortex-M), FPGA workflows, PCB Design with Altium Designer and KiCad, I2C, SPI, UART, oscilloscopes, logic analyzers, soldering</p>
        </div>
        <div class="cv-skill-group">
          <h3>Systems &amp; Tools</h3>
          <p>Linux, Perf, Git, GDB, CMake, LTSpice, LogicWorks, FIO, OpenMP, AVX-512, Pthreads</p>
        </div>
        <div class="cv-skill-group">
          <h3>Web &amp; Others</h3>
          <p>HTML, CSS, Markdown, Docker</p>
        </div>
      </div>
    </div>
  </section>
</div>
