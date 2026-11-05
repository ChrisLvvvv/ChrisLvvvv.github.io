---
title: "Classwide Project 3: SSD Performance Profiling with fio"
collection: portfolio
permalink: /portfolio/fall2025-ecse4320-classwide-ssd/
date: 2025-11-20
excerpt: "NVMe direct-I/O profiling with fio, examining queue depth, throughput, average latency, and p99 latency near saturation."
project_group: coursework-archive
display_year: "2025"
period: "Fall 2025"
sort_key: "2025-Fall"
date_precision: "term"
work_type: "Coursework"
work_category: "coursework"
venue: "Rensselaer Polytechnic Institute · ECSE 4320 Advanced Computer Systems"
tags: ["NVMe","fio","Direct I/O","Tail Latency"]
term: "Fall 2025"
work_source:
  organization: "RPI"
  course_code: "ECSE 4320"
  course_name: "Advanced Computer Systems"
---

[← Advanced Computer Systems overview](/portfolio/fall2025-ecse4320/)

## Direct-I/O storage profiling

I profiled NVMe SSDs using fio with direct I/O. Varying queue depth let me examine how the number of outstanding requests relates to throughput and latency.

## Saturation and tail latency

I considered average latency and p99 latency near device saturation. Looking at both metrics made it possible to distinguish typical response time from the slower tail of the measured request distribution.

The project focused on the throughput–latency trade-off under increasing storage concurrency.
