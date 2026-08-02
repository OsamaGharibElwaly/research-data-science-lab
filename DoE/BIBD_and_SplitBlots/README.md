# DoE Lecture 6: BIBDs and Split Plots

> **Design of Experiments** — Two advanced experimental designs for handling real-world constraints in factorial experiments.

---

## Table of Contents

1. [Overview](#overview)
2. [Case Study 1: Balanced Incomplete Block Design (BIBD)](#case-study-1-balanced-incomplete-block-design-bibd)
3. [Case Study 2: Split Plot Design](#case-study-2-split-plot-design)
4. [Key Takeaways](#key-takeaways)
5. [Running the Code](#running-the-code)

---

## Overview

This lecture covers two advanced experimental designs used when standard **Complete Randomized Designs (CRD)** or **Randomized Complete Block Designs (RCBD)** are impractical:

| Design | Problem It Solves | When to Use |
|--------|-------------------|-------------|
| **BIBD** | Not all treatments fit in every block | Block size is smaller than number of treatments |
| **Split Plot** | Factors have different levels of "hardness" to change | One factor is costly/difficult to change; another is easy |

---

## Case Study 1: Balanced Incomplete Block Design (BIBD)

### The Problem

You want to compare **4 crop varieties (A, B, C, D)** across **4 fields (blocks)**. However, **each field can only hold 3 varieties** — not all 4. This makes a standard RCBD impossible.

### The Solution: BIBD

A BIBD ensures:
- Every **pair of treatments** appears together in the same number of blocks
- Each block contains the **same number of treatments** (but fewer than the total)
- Each treatment appears the **same number of times** across all blocks

### Design Layout

| Block | Treatments |
|-------|------------|
| Field 1 | A, B, C |
| Field 2 | A, B, D |
| Field 3 | A, C, D |
| Field 4 | B, C, D |

Notice: Every pair (A&B, A&C, A&D, B&C, B&D, C&D) appears together in **exactly 2 blocks**.

### Model

```
Yield ~ Treatment + Block + Error
```

Using `statsmodels`:
```python
model = ols("Yield ~ C(Treatment) + C(Block)", data=bibd).fit()
anova = anova_lm(model)
```

### Key Insight

BIBD allows you to **estimate treatment effects while controlling for block effects**, even though no single block contains all treatments. The "balance" ensures fair comparison.

---

## Case Study 2: Split Plot Design

### The Problem

You want to study how **Temperature** and **Fertilizer** affect crop yield. But:
- **Temperature** is *hard to change* (requires adjusting greenhouse/heating systems)
- **Fertilizer** is *easy to change* (just swap the type)

If you randomize both freely, you waste time and resources constantly resetting temperature.

### The Solution: Split Plot Design

| Level | Factor | Why |
|-------|--------|-----|
| **Whole Plot** | Temperature (Low / High) | Hard-to-change; randomized at the block level |
| **Sub Plot** | Fertilizer (A / B / C) | Easy-to-change; randomized within each whole plot |
| **Block** | Farm (1 / 2 / 3) | Accounts for farm-to-farm variability |

### Design Structure

```
Farm 1
├── Low Temp  → Fertilizer A, B, C (random order)
└── High Temp → Fertilizer A, B, C (random order)

Farm 2
├── Low Temp  → Fertilizer A, B, C (random order)
└── High Temp → Fertilizer A, B, C (random order)

Farm 3
├── Low Temp  → Fertilizer A, B, C (random order)
└── High Temp → Fertilizer A, B, C (random order)
```

### Model

```python
model = ols(
    "Yield ~ C(Block) + C(Temperature) * C(Fertilizer)",
    data=splitplot
).fit()
```

### Key Insight

Split Plot Design **acknowledges the hierarchy of randomization**:
- Temperature effects are tested against **whole-plot error** (between temp groups)
- Fertilizer and interaction effects are tested against **sub-plot error** (within temp groups)

This gives **more precise estimates** for the easy-to-change factor and its interactions.

---

## Key Takeaways

| Concept | BIBD | Split Plot |
|---------|------|------------|
| **Core Issue** | Block size < number of treatments | Factors differ in "hardness" to change |
| **Randomization** | Treatments randomized within blocks | Two-stage: whole plot → sub plot |
| **Error Structure** | Single error term | Two error terms (whole-plot + sub-plot) |
| **Precision** | Balanced pairwise comparisons | Sub-plot factor gets more precision |
| **Real-world Use** | Clinical trials, agricultural plots | Industrial processes, greenhouses, baking |

### When to Choose Which?

- **Use BIBD** when physical constraints prevent all treatments from fitting in every block.
- **Use Split Plot** when one factor is structurally harder or more expensive to change than another.

---

## Running the Code

### Requirements

```bash
pip install numpy pandas matplotlib seaborn statsmodels joblib
```

### Outputs

| File | Description |
|------|-------------|
| `figures/bibd_layout.png` | Heatmap of the BIBD assignment matrix |
| `figures/bibd_treatment_effects.png` | Boxplot of yield by treatment |
| `figures/splitplot_layout.png` | Barplot of Temperature × Fertilizer |
| `figures/splitplot_interaction.png` | Interaction plot (point plot) |
| `figures/splitplot_anova.png` | Bar chart of ANOVA F-statistics |
| `models/bibd_model.pkl` | Saved BIBD regression model |
| `models/splitplot_model.pkl` | Saved Split Plot regression model |

### Quick Run

```bash
python DoE_Lecture_6.py
```

---

*Author: DoE Learning Lab*
