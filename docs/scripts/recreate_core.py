#!/usr/bin/env python3

"""
Recreate a subset of core figures from provided CSVs.

Usage:
  python docs/scripts/recreate_core.py

Expects files placed in docs/data/:
  - Top_spectral_peaks.csv
  - combined_bands_significance.csv
  - (optional) kernel_used.npy
Outputs to docs/figures/.
"""
import os, re, numpy as np, pandas as pd, matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.dirname(__file__))
DATA = os.path.join(BASE, "data")
FIGS = os.path.join(BASE, "figures")
os.makedirs(FIGS, exist_ok=True)

def load_top_peaks():
    p = os.path.join(DATA, "Top_spectral_peaks.csv")
    df = pd.read_csv(p)
    # guess freq column
    fcol = None
    for c in df.columns:
        lc = c.lower()
        if "freq" in lc or lc.startswith("f"):
            if pd.api.types.is_numeric_dtype(df[c]):
                fcol = c; break
    if fcol is None:
        raise ValueError("No frequency-like column found in Top_spectral_peaks.csv")
    f = df[fcol].dropna().to_numpy(float)
    # keep within Nyquist
    f = f[(f>0)&(f<=0.5)]
    return np.sort(f)

def load_band_enrichment():
    p = os.path.join(DATA, "combined_bands_significance.csv")
    df = pd.read_csv(p)
    # guess columns
    band_col = None; score_col = None
    for c in df.columns:
        if any(k in c.lower() for k in ["band","harm","freq","ratio","x"]):
            if pd.api.types.is_numeric_dtype(df[c]): band_col=c; break
    for c in df.columns:
        if any(k in c.lower() for k in ["z","score","enrich","stat","-log"]):
            if pd.api.types.is_numeric_dtype(df[c]): score_col=c; break
    if band_col is None or score_col is None:
        raise ValueError("Need a band/frequency column and an enrichment/score column")
    x = df[band_col].to_numpy(float)
    s = df[score_col].to_numpy(float)
    # if x looks like indices, map to [0,0.5]
    if np.nanmax(x)>0.6:
        x = (x - np.nanmin(x)) / (np.nanmax(x)-np.nanmin(x)) * 0.5
    return x, s

def figure_mode_band_overlay():
    freqs = load_top_peaks()
    x, s = load_band_enrichment()
    plt.figure(figsize=(9,4.2))
    plt.plot(x, s, lw=2)
    for f in np.sort(freqs)[:8]:
        plt.axvline(f, ls="--", lw=1)
        plt.text(f, max(s)*1.02, f"{f:.3f}", ha="center", va="bottom", rotation=90, fontsize=8)
    plt.xlabel("harmonic coordinate")
    plt.ylabel("enrichment (arb.)")
    plt.title("Mode–band overlay")
    out = os.path.join(FIGS, "mode_band_overlay.png")
    plt.tight_layout(); plt.savefig(out, dpi=160); plt.close()
    print("Wrote", out)

def figure_carrier_hierarchy():
    freqs = load_top_peaks()[:6]
    plt.figure(figsize=(8,4))
    for f in freqs:
        plt.vlines(f, 0, 0.9, lw=2)
        for k in [2,3,4]:
            if k*f <= 0.5:
                plt.vlines(k*f, 0, 0.5, lw=1, alpha=0.6)
        if (1-f) <= 0.5:
            plt.vlines(1-f, 0, 0.5, lw=1, alpha=0.6)
        plt.text(f, 0.92, f"{f:.3f}", ha="center", va="bottom", rotation=90)
    plt.ylim(0,1.05); plt.xlim(0,0.5)
    plt.xlabel("frequency (cycles per lag)"); plt.ylabel("relative strength")
    plt.title("Carrier hierarchy (schematic)")
    out = os.path.join(FIGS, "carrier_hierarchy.png")
    plt.tight_layout(); plt.savefig(out, dpi=160); plt.close()
    print("Wrote", out)

if __name__=="__main__":
    figure_mode_band_overlay()
    figure_carrier_hierarchy()
