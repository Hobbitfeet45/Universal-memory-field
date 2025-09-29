---
title: Universal Memory Field
---

# Universal Memory Field

**Arithmetic Memory Field Theory (AMFT)** proposes that a scalar displacement field with memory organizes
structure across scales via a small set of preferred carrier modes (the “alphabet”). Particles, shells, and
band enrichments arise where resonance and memory align.

This site is the *reproducibility companion* for our paper. Use the navigation below to explore core results,
methods, and code.

## Quick Links

- **Core Results:** [/figures/](./figures/)
- **Reproducibility Notebooks:** [/notebooks/](./notebooks/)
- **Scripts:** [/scripts/](./scripts/)
- **Theory Notes:** [/theory/](./theory/)
- **Data:** [/data/](./data/)

---

## Core Ideas

- **Memory Kernel → Carriers:** The Toeplitz memory kernel yields a small set of spectral carriers that act as
  the organizing frequencies of the field.
- **Carriers → Shells:** Shells (e.g., particle masses) form on harmonics of these carriers, following
  a calibrated scaling law \( m = C (n/f)^\alpha \).
- **Two-Mode Dynamics:** We observe two scaling regimes (\(\alpha_{\text{low}} \approx 1.25\) for accumulation;
  \(\alpha_{\text{high}} \lesssim 1.1\) for release), consistent with a universal “breathing” of the field.
- **Cross-Scale Coherence:** The same carriers and scaling principles appear from particle physics to astrophysical
  QPOs and galactic structures.

---

## Reproduce the Figures

1. Install requirements.
2. Download the CSVs listed in **Data**.
3. Run the scripts in **Scripts** or open **Notebooks**.

Each figure page in **Figures** includes the code snippet used to generate it.

---

### Damping behavior and regime split

![Damping ratio vs mass](figures/damping_vs_mass_split_fits.png)

*Caption*: (see paper; brief web caption here)

### Observed vs predicted masses (marker encodes damping)

![Observed vs predicted masses](figures/obs_vs_pred_damping_markers.png)

