# SRAM MAC figure sources and result definitions

All assets are extracted from the user-supplied project reports. Page numbers below are one-based PDF pages, matching the printed page numbers. No figure was redrawn, generated, recolored, or converted to grayscale. PNGs are self-contained; the site does not need the source PDFs.

| Asset | Report | Page | Figure | Extraction |
| --- | --- | --- | --- | --- |
| `system-overview.png` | `ESE5700_Project1_P3.pdf` | 2 | 1 | Original vector diagram rendered at 300 dpi; PDF-point crop `[82, 96, 526, 376]` |
| `sram-array-layout.png` | `ESE5700_Project1_P2__5_.pdf` | 2 | 1 | Both original layout panels rendered at 300 dpi; crop `[55, 55, 557, 297]` |
| `read-snm.png` | `ESE5700_Project1_P1.pdf` | 10 | 8 | Original embedded PNG, xref 44, 1244 × 1493 px; no resampling |
| `sequencer-schedule.png` | `ESE5700_Project1_P3.pdf` | 44 | 31 | Original vector plot rendered at 300 dpi; crop `[82, 209, 525, 531]` |
| `full-mac-test-a.png` | `ESE5700_Project1_P3.pdf` | 54 | 36 | Original vector plot rendered at 300 dpi; crop `[82, 219, 526, 534]` |
| `compute-energy.png` | `ESE5700_Project1_P3.pdf` | 57 | 37 | Original vector plots rendered at 300 dpi; crop `[82, 498, 532, 674]` |

The crops remove surrounding prose, report captions, page margins, and page numbers. Original axes, legends, units, signal names, test conditions, and annotations are retained. Source raster resolution limits still apply to the original layout screenshots. Full-resolution links are provided for inspection. The overview is used as the Work cover and in the project gallery; within the detail page, each figure appears only once. The gallery contains the overview, layout, and full-system Test A. SNM, the schedule, and energy appear in their relevant sections.

## Interpretation and provenance

- **Scope and ownership:** Part 1 p. 1 and Part 3 p. 59 record team contributions. Taoyu Lyu performed bitcell sizing/stability analysis and designed/characterized the registers and accumulator, implemented the sequencer, integrated the MAC, and developed full-system verification/timing/energy analysis. Zhixin He developed the SRAM macro and arithmetic datapath. Part 2 lists equal contributions. The article distinguishes individual work from the team implementation.
- **Bitcell revision:** the SNM image is the original Part 1 revision at TT, VDD = WL = 0.8 V, cell ratio 1.5, with 144.9 mV minimum read SNM. Part 2 pp. 1–5 describes revised routing and recharacterization. Its revised extraction baseline is not mixed with Part 1 capacitances; no capacitance table is reproduced on the page.
- **Read path:** Part 2 pp. 9–14 documents the full-swing BLB read inverter and transmission-gate output latch, not a differential sense amplifier.
- **Arithmetic optimization:** Part 3 pp. 25–31 and 58 reports 930.69 → 851.81 ps standalone adder delay (8.48%), 22 selectively doubled carry NAND2 cells, and approximately 110 µm² added estimated area. It does not establish an 8.5% full-system speedup.
- **Clock fanout:** Part 3 p. 12 characterizes 21 shared MAC-register loads and nine input-register loads in each SRAM separately. The final setup/hold checks use those configurations.
- **Sequencing:** Part 3 pp. 42–45 and 52–54 define E0 as sampled START, E1–E16 as useful reads, E2–E17 as accumulator captures, and 17 START-to-DONE periods. The SRAM output latch is the memory-read boundary; there is no product register. Figure 31 uses a 4 ns standalone sequencer test with scheduled read/capture annotations. Figure 36 is actual full-MAC Test A at 3.2 ns.
- **Verification:** Part 3 p. 29 reports 384 integrated datapath vectors; pp. 43 and 52–53 document unit and full-system/reset/restart checks. Table 19 reports A: 845, B: 3600, C: 800, all in 17 cycles. These are reported transistor-level simulation results, not formal proofs or a new simulation run for this website task.
- **Accepted period:** Part 3 pp. 49–51 reports 3.2 ns as the shortest tested setting satisfying arithmetic and control timing. 3.1 ns fails write-off/precharge ordering despite correct arithmetic. The scan resolution is 100 ps; the result is not an exact continuous-time or PVT-qualified limit.
- **Area:** Part 3 pp. 55–56, Table 20, reports approximately 4.5 × 10³ µm². Actual array layout area is counted once per array; other circuits use the bitcell-density estimate. Part 3 instantiates 4608 periphery fins per SRAM, versus Part 2's standalone 5344, so doubling Part 2's standalone macro area would be incorrect.
- **Energy/latency:** Part 3 pp. 56–58 reports TT, 27 °C, 0.8 V, nominal 17 × 3.2 ns ≈ 54 ns, Test A ≈ 19 pJ/dot and ≈ 1.2 pJ/MAC including SRAM. The integration interval is START CLK50 to actual DONE50, excludes operand loading, and includes the terminal clock-to-Q interval. MW/MX contain complete SRAMs and account for approximately 62% of Test A energy. Figure 37 retains original unrounded values; page tables use report-rounded values.
- **Project date:** `2026-10-27` comes from the Part 3 PDF creation metadata (`D:20261027221732Z`), not an inferred deadline or a claimed fabrication date. The visible source term is Fall 2026.
- **Assignment boundary:** `ese5700-project1.pdf` is the task brief, used only to check goals. Final implementation and system metrics follow the reports, with Part 3 taking precedence.

## Source SHA-256

- Part 1: `84c2b142ba1d3315e852856b5b8a9fae0082a3634437dae80835e9cb94b2b8a3`
- Part 2: `fbe66e87ee2bb649b3d6c2a3050eb52f215a4253d8aa957e132fc601c356fa18`
- Part 3: `80cf483228b25db84da23b393b3565b51b69aa4f5f5b97830799d6ef47dabe6c`

The four source PDFs are temporary inputs and are removed from the project root and generated output after content, asset, build, and browser validation. The extracted assets and these notes remain.
