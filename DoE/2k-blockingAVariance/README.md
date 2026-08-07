# DoE Lecture 11: 2^k Blocking and Variance

> **Design of Experiments — Lecture 11**  
> Topics: Blocking in 2^k factorial designs, confounding structures, partial confounding, generalized interactions, intra-block vs inter-block variance, variance components analysis.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Core Concepts](#2-core-concepts)
3. [Rules of Thumb](#3-rules-of-thumb)
4. [Case Studies](#4-case-studies)
5. [Workflow](#5-workflow)
6. [Common Pitfalls](#6-common-pitfalls)
7. [Comparisons](#7-comparisons)
8. [References](#8-references)

---

## 1. Overview

Blocking is a technique used in factorial experiments to account for known sources of nuisance variation. When experimental units are heterogeneous, grouping them into homogeneous blocks and assigning treatments within blocks improves precision by removing block-to-block variation from the experimental error.

In **2^k factorial designs**, blocking is achieved by confounding (aliasing) certain high-order interactions with block effects. This sacrifices information on those interactions but preserves the ability to estimate main effects and lower-order interactions with higher precision.

### Key Principle
> *"Block what you can, randomize what you cannot."* — R.A. Fisher

### Why Block?
- **Reduces error variance** by removing systematic block differences
- **Increases precision** of treatment effect estimates
- **Maintains validity** when nuisance factors exist
- **Enables experiments** that would otherwise be impossible due to resource constraints

---

## 2. Core Concepts

### 2.1 Block Defining Contrast

The block defining contrast determines how runs are assigned to blocks. For a 2^k design in 2^p blocks:

- Choose **p independent block generators** (interactions)
- The **generalized interaction** of all generators defines the confounding structure
- All effects that are products of the block defining contrast are confounded with blocks

**Example:** 2^3 in 2 blocks
- Block generator: `ABC`
- Block defining contrast: `ABC = I`
- Confounded effects: `ABC` (lost), and all aliases: `A ≡ BC`, `B ≡ AC`, `C ≡ AB`

### 2.2 Generalized Interaction

For multiple block generators, the generalized interaction is found by multiplying all generators together (mod 2 on each factor):

| Generators | Generalized Interaction | Confounded Effects |
|------------|------------------------|-------------------|
| ABC, CDE | ABDE | ABC, CDE, ABDE |
| AB, ACD | BCD | AB, ACD, BCD |
| ABC, ABD | CD | ABC, ABD, CD |

**Rule:** The generalized interaction of p generators produces 2^p - 1 confounded effects (including the generators themselves).

### 2.3 Complete vs Partial Confounding

| Aspect | Complete Confounding | Partial Confounding |
|--------|---------------------|---------------------|
| **Definition** | Same effect confounded in all replicates | Different effects confounded across replicates |
| **Information Loss** | Permanent for confounded effects | Recoverable via pooling across replicates |
| **Use Case** | Single replicate, high-order interactions negligible | Multiple replicates, need all interactions |
| **Example** | 2^3 in 2 blocks, ABC lost forever | 3 replicates: ABC, AB, AC each confounded once |

### 2.4 Intra-block vs Inter-block Variance

| Type | Definition | Source | Analysis |
|------|-----------|--------|----------|
| **Intra-block** | Variation within the same block | Treatment differences + random error | Used for treatment comparisons |
| **Inter-block** | Variation between blocks | Block differences + treatment differences | Removed from error via blocking |

**Key Insight:** Blocking converts inter-block variance into a systematic component, leaving only intra-block variance in the error term.

### 2.5 Variance Components

In a blocked design with random blocks, the total variance decomposes as:

$$\sigma^2_{total} = \sigma^2_{block} + \sigma^2_{treatment} + \sigma^2_{error}$$

Where:
- $\sigma^2_{block}$ = Variance due to block differences
- $\sigma^2_{treatment}$ = Variance due to treatment differences
- $\sigma^2_{error}$ = Random experimental error

### 2.6 ANOVA with Blocks

```
Source        | SS        | df        | MS        | F
--------------|-----------|-----------|-----------|----
Blocks        | SS_Block  | b-1       | MS_Block  | -
Treatments    | SS_Trt    | t-1       | MS_Trt    | MS_Trt / MS_Error
Error         | SS_Error  | (b-1)(t-1)| MS_Error  | -
Total         | SS_Total  | bt-1      | -         | -
```

---

## 3. Rules of Thumb

### 3.1 Choosing Block Generators
1. **Always confound the highest-order interaction** possible
2. **Never confound main effects** or two-factor interactions unless absolutely necessary
3. **Minimize the number of confounded low-order interactions**
4. For p block generators, check all 2^p - 1 generalized interactions

### 3.2 Block Size Considerations
- **Small blocks** (2-4 runs): Higher confounding, easier to manage
- **Large blocks** (8-16 runs): Less confounding, harder to keep homogeneous
- **Rule:** Block size should be the largest unit that remains homogeneous

### 3.3 Number of Blocks
- 2^3 design: Max 4 blocks (confound 3 effects)
- 2^4 design: Max 8 blocks (confound 7 effects)
- 2^5 design: Max 16 blocks (confound 15 effects)
- **General:** 2^k in 2^p blocks confounds 2^p - 1 effects

### 3.4 When to Use Partial Confounding
- When **all interactions** are potentially important
- When you have **multiple replicates**
- When you need **higher precision** on confounded effects
- When the **experiment is large enough** to afford replication

### 3.5 Efficiency Gains
- Blocking can reduce MSE by **5-20x** depending on block heterogeneity
- The efficiency gain = MSE_CRD / MSE_RCBD
- If block variance > error variance, blocking is always beneficial

---

## 4. Case Studies

### Case Study 1: Chemical Reactor Yield (2^3 in 2 Blocks)

**Context:** A chemical plant runs experiments in two shifts (day/night). Temperature (A), Pressure (B), and Catalyst (C) are studied.

**Design:** 2^3 factorial in 2 blocks, confounding ABC with shift difference.

**Results:**
- Block Defining Contrast: ABC = I
- Confounded: ABC (lost)
- Estimated Effects: A = 7.88, B = -6.27, C = 4.13
- Main effects clearly significant; ABC interaction negligible

**Lesson:** When high-order interactions are negligible, complete confounding is efficient.

---

### Case Study 2: Semiconductor Etching Rate (2^4 in 4 Blocks)

**Context:** Etching rate depends on Power (A), Gas Flow (B), Pressure (C), Temperature (D). Four different machines (blocks) are used.

**Design:** 2^4 in 4 blocks using generators ABC and ABD.

**Results:**
- Generalized Interaction: CD
- Confounded Effects: ABC, ABD, CD, and all aliases
- Block Layout: 4 runs per block

**Lesson:** Multiple block generators create complex confounding; generalized interaction table essential.

---

### Case Study 3: Pharmaceutical Tablet Dissolution (2^5 in 8 Blocks)

**Context:** Tablet dissolution studied across 5 factors with 8 batches of raw material.

**Design:** 2^5 in 8 blocks using ABC, ABD, CDE.

**Results:**
- Generalized Interactions: CD, ABDE, ABCE, E
- Total Confounded: 31 effects (including all aliases)
- Runs per Block: 4

**Lesson:** In large designs with many blocks, substantial information is sacrificed; partial confounding recommended.

---

### Case Study 4: Recovering Confounded Effects via Partial Confounding

**Context:** A 2^3 design replicated 3 times. Each replicate uses a different blocking scheme.

**Strategy:**
| Replicate | Block Generator | Confounded | ABC Available? |
|-----------|----------------|------------|----------------|
| 1 | ABC | ABC | No |
| 2 | AB | AB | Yes |
| 3 | AC | AC | Yes |

**Combined Analysis:**
- ABC: Estimated from Replicates 2 & 3 via pooling
- AB: Estimated from Replicates 1 & 3
- AC: Estimated from Replicates 1 & 2
- A, B, C, BC: Estimated from all replicates

**Lesson:** Partial confounding allows recovery of all effects at the cost of replication.

---

### Case Study 5: Variance Reduction through Blocking

**Comparison:** CRD vs RCBD with 4 treatments, 4 blocks.

| Metric | CRD | RCBD |
|--------|-----|------|
| Treatment SS | 60.72 | 203.65 |
| Error SS | 917.00 | 36.06 |
| MSE | 76.42 | 4.01 |
| **Efficiency** | 1.0x | **19.1x** |

**Lesson:** When block effects are large (σ_block = 4, σ_error = 2), blocking provides massive precision gains.

---

## 5. Workflow

### Step-by-Step Blocking Design Process

```
1. IDENTIFY NUISANCE FACTORS
   └─> What creates heterogeneity? (batches, shifts, operators, days)

2. DETERMINE BLOCK SIZE
   └─> How many runs fit in one homogeneous block?

3. CHOOSE BLOCK GENERATORS
   └─> Select p independent interactions
   └─> Check all generalized interactions (2^p - 1 total)
   └─> Ensure no main effects or 2FIs are confounded

4. ASSIGN RUNS TO BLOCKS
   └─> Use block defining contrast: B = sign(generator column)
   └─> Block 0: negative sign; Block 1: positive sign

5. RANDOMIZE WITHIN BLOCKS
   └─> Randomize run order within each block
   └─> Randomize block order if possible

6. CONDUCT EXPERIMENT
   └─> Execute runs block by block
   └─> Record all responses

7. ANALYZE DATA
   └─> Remove block effects from ANOVA
   └─> Estimate treatment effects from intra-block contrasts
   └─> For partial confounding: pool estimates across replicates

8. INTERPRET RESULTS
   └─> Identify significant effects
   └─> Note which effects are confounded
   └─> Assess information loss vs precision gain
```

---

## 6. Common Pitfalls

### Pitfall 1: Confounding Important Interactions
**Problem:** Choosing block generators that confound two-factor interactions.  
**Solution:** Always use highest-order interactions as generators.

### Pitfall 2: Ignoring Generalized Interactions
**Problem:** Using ABC and ABD without realizing CD is also confounded.  
**Solution:** Calculate ALL generalized interactions before finalizing design.

### Pitfall 3: Block Heterogeneity Within Blocks
**Problem:** Blocks are not actually homogeneous.  
**Solution:** Define blocks by the actual nuisance factor; verify homogeneity.

### Pitfall 4: Treating Blocks as Fixed When Random
**Problem:** Using fixed-effects ANOVA when blocks are a random sample.  
**Solution:** Use mixed-effects models or random block ANOVA.

### Pitfall 5: Over-blocking
**Problem:** Too many blocks confound too many effects.  
**Solution:** Balance block size vs information loss; use partial confounding.

### Pitfall 6: Forgetting Inter-block Information
**Problem:** In partial confounding, ignoring information from block contrasts.  
**Solution:** Use combined intra-block and inter-block estimators for maximum efficiency.

### Pitfall 7: Incorrect Randomization
**Problem:** Randomizing across blocks instead of within blocks.  
**Solution:** Randomize run order WITHIN each block separately.

---

## 7. Comparisons

### 7.1 CRD vs RCBD vs BIBD

| Feature | CRD | RCBD | BIBD |
|---------|-----|------|------|
| Block Size | Any | = # treatments | < # treatments |
| Treatments/Block | All | All | Subset |
| Balance | Yes | Yes | Yes (balanced) |
| Confounding | None | High-order only | By design |
| Use When | Homogeneous units | Heterogeneous, all trts fit | Heterogeneous, limited block size |

### 7.2 Complete vs Partial Confounding

| Feature | Complete | Partial |
|---------|----------|---------|
| Replicates | 1+ (same confounding) | 2+ (different confounding) |
| Information Recovery | None | Full (with enough reps) |
| Precision of Confounded Effects | None | Lower (from subset of reps) |
| Precision of Unconfounded Effects | High | High |
| Best For | Screening, high-order negligible | All interactions important |

### 7.3 Blocking vs Fractional Factorial

| Aspect | Blocking | Fractional Factorial |
|--------|----------|---------------------|
| **Purpose** | Remove nuisance variation | Reduce run count |
| **Mechanism** | Confound with blocks | Confound with each other |
| **Resolution** | Not applicable | Resolution III, IV, V |
| **Information Loss** | Block confounded effects | Aliased effects |
| **Can Combine?** | Yes (e.g., 2^(5-1) in blocks) | Yes |

---

## 8. References

### Textbooks
1. **Box, G.E.P., Hunter, J.S., & Hunter, W.G.** (2005). *Statistics for Experimenters: Design, Innovation, and Discovery* (2nd ed.). Wiley. — Chapters 10-11 on blocking and confounding.

2. **Montgomery, D.C.** (2017). *Design and Analysis of Experiments* (9th ed.). Wiley. — Chapter 7: Blocking and Confounding in the 2^k Factorial Design.

3. **Wu, C.F.J. & Hamada, M.S.** (2009). *Experiments: Planning, Analysis, and Optimization* (2nd ed.). Wiley. — Chapter 5 on blocking.

### Papers
4. **Fisher, R.A.** (1935). *The Design of Experiments*. Oliver & Boyd. — Original development of blocking principles.

5. **Bose, R.C.** (1947). "Mathematical theory of the symmetrical factorial design." *Sankhyā*, 8, 107-166. — Foundation of confounding theory.

### Software
6. **R:** `FrF2` package (Groemping, 2014) — optimal fractional factorials with blocking.
7. **Python:** `pyDOE2`, `statsmodels` — blocking design generation and analysis.
8. **Minitab:** Stat > DOE > Factorial > Create Factorial Design > Designs > Blocks.

---

## Appendix: Quick Reference Tables

### Table A: 2^3 Blocking Schemes

| Blocks | Generators | Confounded | Runs/Block |
|--------|-----------|------------|------------|
| 2 | ABC | ABC | 4 |
| 4 | AB, AC | AB, AC, BC | 2 |

### Table B: 2^4 Blocking Schemes

| Blocks | Generators | Confounded | Runs/Block |
|--------|-----------|------------|------------|
| 2 | ABCD | ABCD | 8 |
| 4 | ABC, ACD | ABC, ACD, BD | 4 |
| 8 | AB, BC, CD | AB, BC, CD, AC, BD, AD, ABCD | 2 |

### Table C: 2^5 Blocking Schemes

| Blocks | Generators | Confounded | Runs/Block |
|--------|-----------|------------|------------|
| 2 | ABCDE | ABCDE | 16 |
| 4 | ABC, CDE | ABC, CDE, ABDE | 8 |
| 8 | ABC, ABD, CDE | 7 effects | 4 |
| 16 | AB, AC, AD, AE | 15 effects | 2 |

---

*Generated: 2026-08-07*  
*Lecture 11: 2^k Blocking and Variance*
