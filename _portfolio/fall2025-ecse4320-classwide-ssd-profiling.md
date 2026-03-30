---
title: "Classwide Project 3: SSD Performance Profiling with fio"
collection: portfolio
permalink: /portfolio/fall2025-ecse4320-classwide-ssd/
date: 2025-11-20
venue: "ECSE4320 Advanced Computer Systems"
excerpt: "Block level SSD performance study using fio, exploring throughput and latency across queue depth, block size and read write mixes."
project_group: coursework-archive
tags:
  - Storage
  - SSD
  - fio
  - Performance
  - Latency
---

[← Back to ECSE4320 Advanced Computer Systems Overview](/portfolio/fall2025-ecse4320/)

This classwide project profiled SSD performance using fio to understand how queue depth, block size and workload mix affect throughput and latency. I set up and ran fio jobs, processed raw JSON outputs and generated plots to characterize the behavior of a dedicated SSD under different access patterns.



## Experiment Setup

- Environment: Ubuntu on WSL2, Python 3 for analysis and plotting.  
- Tool: fio with JSON output enabled.  
- Target: dedicated 64 GiB test file on the SSD using direct I O to bypass the page cache.  
- Workloads were time based with warm up periods to reach steady state.

## Experiments

- **Queue depth sweep for 4 KiB random reads**  
  - Varied `iodepth` from small to large values.  
  - Measured IOPS, bandwidth and latency distributions.  
  - Highlighted the throughput latency trade off as concurrency increases.

- **Block size sweeps for sequential and random workloads**  
  - Swept block sizes from small (4 KiB) to large values.  
  - Compared sequential versus random access patterns.  
  - Showed how larger blocks improve throughput but can interact with device internal scheduling and alignment.

- **Read write mix sweep**  
  - Fixed 4 KiB random access and queue depth, varied the read write ratio.  
  - Evaluated 100 percent read, 100 percent write and mixed ratios such as 70/30 and 50/50.  
  - Observed asymmetric performance between reads and writes and how mixes move the device along different operating points.

- **Tail latency analysis**  
  - Collected detailed latency distribution data.  
  - Plotted tail latency curves to observe rare but long latency events.  
  - Emphasized why mean latency is not sufficient to characterize storage quality of service.

## Tooling and Scripts

- Used fio job files to describe each experiment configuration.  
- Wrote Python scripts to parse JSON logs, aggregate statistics and generate figures for block size, mix and tail latency.  
- Ensured experiments were reproducible through documented parameters and reusable scripts.

## Outcome

The project provided hands on experience with storage benchmarking and performance analysis. It built intuition for how SSDs respond to different workloads and how to design experiments that reveal throughput and latency trade offs that matter for real systems.
