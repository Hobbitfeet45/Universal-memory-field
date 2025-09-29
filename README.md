# Universal Memory Field

A companion repository and GitHub Pages site for the Arithmetic Memory Field Theory (AMFT) project.

This repo contains:
- **docs/** — the website (GitHub Pages).
- **docs/figures/** — polished and exploratory plots from the paper.
- **docs/data/** — CSVs and small data artifacts required to reproduce core plots.
- **docs/scripts/** — small Python modules and scripts to regenerate figures.
- **docs/notebooks/** — Jupyter notebooks for end-to-end reproduction.
- **docs/theory/** — mathematical notes and LaTeX snippets.
- **docs/references/** — bibliographic references and links.

## Quickstart

```bash
# 1) Clone and enter
git clone https://github.com/YOUR_GITHUB/universal-memory-field.git
cd universal-memory-field

# 2) (optional) Create a virtualenv
python -m venv .venv && source .venv/bin/activate

# 3) Install requirements
pip install -r requirements.txt

# 4) Build / preview the site locally (optional)
# GitHub Pages will serve docs/ automatically; locally you can use any static server:
python -m http.server --directory docs 4000
```

## Reproducibility

See `docs/notebooks/00_reproduce_core_figures.ipynb` (or the corresponding scripts in `docs/scripts/`)
for a fully reproducible path from data → figures.

---

© 2025 Universal Memory Field authors. See LICENSE for details.
