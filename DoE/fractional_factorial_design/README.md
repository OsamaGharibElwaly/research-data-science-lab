# DoE Lecture 12: Fractional Factorial Design

## Overview

Fractional Factorial Designs are a cornerstone of efficient experimental design, allowing researchers to study the effects of many factors with significantly fewer experimental runs than a full factorial design. This lecture covers the theory, construction, analysis, and practical application of 2^(k-p) fractional factorial designs.

---

## Table of Contents

1. [Core Concepts](#1-core-concepts)
2. [Design Construction](#2-design-construction)
3. [Resolution & Aliasing](#3-resolution--aliasing)
4. [Rules of Thumb](#4-rules-of-thumb)
5. [Case Studies](#5-case-studies)
6. [Workflow](#6-workflow)
7. [Common Pitfalls](#7-common-pitfalls)
8. [Comparisons](#8-comparisons)
9. [References](#9-references)

---

## 1. Core Concepts

### 1.1 What is a Fractional Factorial Design?

A **fractional factorial design** is a subset (fraction) of a full 2^k factorial design. It is denoted as **2^(k-p)**, where:
- **k** = number of factors
- **p** = number of generators
- **Fraction size** = 1/2^p of the full factorial
- **Number of runs** = 2^(k-p)

### 1.2 Why Use Fractional Factorial Designs?

| k (factors) | Full Factorial (2^k) | Half Fraction (2^(k-1)) | Quarter Fraction (2^(k-2)) |
|-------------|---------------------|------------------------|---------------------------|
| 3 | 8 | 4 | — |
| 4 | 16 | 8 | — |
| 5 | 32 | 16 | 8 |
| 6 | 64 | 32 | 16 |
| 7 | 128 | 64 | 32 |
| 8 | 256 | 128 | 64 |
| 10 | 1,024 | 512 | 256 |

**Key Insight:** Higher-order interactions (3-factor and above) are often negligible. By assuming they are zero, we can use fractional designs to estimate lower-order effects with far fewer runs.

### 1.3 Generators and Defining Relation

**Generators** specify how additional factor columns are constructed from base factor columns.

Example: For a 2^(4-1) design with generator D = ABC:
- Start with full 2^3 design for factors A, B, C
- Create D by multiplying A × B × C
- The defining relation is: **I = ABCD**

The defining relation determines the entire aliasing structure of the design.

### 1.4 Principal vs. Complementary Fractions

For any fractional design, there are 2^p possible fractions. The **principal fraction** has the generator product equal to +I. The **complementary fraction** uses -I.

---

## 2. Design Construction

### 2.1 Step-by-Step Construction

**Step 1:** Choose k (factors) and p (generators) based on budget and objectives.

**Step 2:** Select p independent generators. Each generator should be a high-order interaction of the base factors.

**Step 3:** Write the full factorial for the base k-p factors.

**Step 4:** Create additional columns by multiplying the appropriate base columns according to the generators.

**Step 5:** Compute the defining relation by multiplying all generators and their generalized interactions.

**Step 6:** Determine resolution from the shortest word in the defining relation.

### 2.2 Example: 2^(5-2) Design

**Parameters:** k=5, p=2, n=8 runs

**Generators:** D = AB, E = AC

**Construction:**
1. Write full 2^3 for A, B, C
2. D = A × B
3. E = A × C

**Defining Relation:**
```
I = ABD = ACE = BCDE
```

**Resolution:** III (shortest word has length 3)

### 2.3 Minimum Aberration Criterion

When multiple designs have the same resolution, choose the one with **minimum aberration**:

- Minimize A_3 (number of length-3 words) first
- Then minimize A_4 (number of length-4 words)
- And so on...

**Example:** Two 2^(6-2) designs:

| Design | Generators | Defining Relation | A_4 | Preferred? |
|--------|-----------|-------------------|-----|-----------|
| A | E=ABC, F=BCD | I=ABCE+ADEF+BCDF | 3 | ✓ Yes |
| B | E=ABC, F=DEF | I=ABCE+ADEF+BCDF | — | Different structure |

---

## 3. Resolution & Aliasing

### 3.1 Design Resolution

**Resolution** is the length of the shortest word in the defining relation. It is written as a Roman numeral.

| Resolution | Notation | Main Effects Aliased With | 2FIs Aliased With |
|-----------|----------|--------------------------|-------------------|
| III | 2^(k-p)_III | 2FIs | Main Effects |
| IV | 2^(k-p)_IV | 3FIs+ | Other 2FIs |
| V | 2^(k-p)_V | 4FIs+ | 3FIs+ |
| VI | 2^(k-p)_VI | 5FIs+ | 4FIs+ |

### 3.2 Aliasing (Confounding)

Two effects are **aliased** (confounded) if they cannot be estimated separately. The alias structure is obtained by multiplying each effect by the defining relation.

**Example:** 2^(4-1) with I = ABCD

```
A × I = A × ABCD = A²BCD = BCD     →  A is aliased with BCD
AB × I = AB × ABCD = A²B²CD = CD   →  AB is aliased with CD
```

**Full Alias Structure:**
```
A + BCD
B + ACD
C + ABD
D + ABC
AB + CD
AC + BD
AD + BC
```

### 3.3 Clear Effects

An effect is **clear** if it is not aliased with any effect of interest (typically main effects and 2FIs).

- **Resolution III:** No clear 2FIs
- **Resolution IV:** All main effects are clear; some 2FIs may be clear
- **Resolution V:** All main effects and 2FIs are clear

---

## 4. Rules of Thumb

### 4.1 When to Use Each Resolution

| Situation | Recommended Resolution | Rationale |
|-----------|----------------------|-----------|
| Pure screening, many factors | III | Minimal runs, identify active factors |
| Screening + some 2FI estimation | IV | Main effects clear, 2FIs in pairs |
| Need all main effects + 2FIs | V | Complete estimation of 1st/2nd order |
| Follow-up to Resolution III | IV (via foldover) | De-alias main effects from 2FIs |

### 4.2 Generator Selection Rules

1. **Maximize resolution** — choose generators with the most letters
2. **Minimize aberration** — among equal resolution, minimize A_3, then A_4
3. **Avoid confounding effects of interest** — don't alias important 2FIs with each other
4. **Use standard tables** — reference published minimum aberration designs

### 4.3 Run Size Guidelines

| Objective | Minimum Resolution | Typical Run Size |
|-----------|-------------------|-----------------|
| Screen k factors | III | 2^(k-p) where 2^(k-p) ≥ k+1 |
| Estimate main effects + dominant 2FIs | IV | 2^(k-p) where 2^(k-p) ≥ 2k |
| Estimate all main effects + 2FIs | V | 2^(k-p) where 2^(k-p) ≥ 1+k+k(k-1)/2 |

---

## 5. Case Studies

### 5.1 Case Study 1: Chemical Process Screening (2^(7-4) Resolution III)

**Context:** Screen 7 process variables with only 8 runs.

**Design:** 2^(7-4) with generators D=AB, E=AC, F=BC, G=ABC

**Key Finding:** A and B are significant, but confounded with 2FIs. Requires follow-up.

**Lesson:** Resolution III is powerful for screening but requires follow-up experiments.

### 5.2 Case Study 2: Injection Molding (2^(6-2) Resolution IV)

**Context:** Optimize 6 factors with 16 runs.

**Design:** 2^(6-2) with generators E=ABC, F=BCD

**Key Finding:** Main effects are clear. 2FIs are aliased in pairs (AB=CE=DF, etc.).

**Lesson:** Resolution IV is the workhorse for industrial experimentation.

### 5.3 Case Study 3: Robust Parameter Design (2^(5-1) Resolution V)

**Context:** Find robust settings for 5 control factors.

**Design:** 2^(5-1) with generator E=ABCD

**Key Finding:** All main effects and 2FIs are estimable (assuming 3FIs+ negligible).

**Lesson:** Resolution V is the gold standard when run budget permits.

### 5.4 Case Study 4: Plackett-Burman vs Regular Fractional

**Context:** Compare designs for 11 factors in 12 runs.

**Plackett-Burman:** Non-regular, complex partial aliasing, can sometimes estimate 2FIs via regression.

**Regular 2^(11-7):** Clear aliasing structure, easier interpretation.

**Lesson:** Choose based on analysis strategy and factor count.

### 5.5 Case Study 5: Sequential Experimentation

**Context:** Investigate 8 factors efficiently.

**Strategy:**
1. Phase 1: 2^(8-4) Resolution IV (16 runs) → screen factors
2. Phase 2: Foldover (16 runs) → de-alias main effects
3. Phase 3: Full factorial on subset (if needed)

**Result:** 32 total runs vs. 256 for full 2^8.

**Lesson:** Sequential experimentation maximizes information per run.

---

## 6. Workflow

```
┌─────────────────────────────────────────────────────────────┐
│  STEP 1: Define Objectives                                  │
│  • Identify factors (k)                                     │
│  • Determine which effects are of interest                  │
│  • Set run budget                                           │
└──────────────────────────┬──────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 2: Choose Design Type                                 │
│  • If only screening: Resolution III                        │
│  • If main effects + some 2FIs: Resolution IV             │
│  • If all main effects + 2FIs: Resolution V                 │
│  • Reference standard tables for generators                 │
└──────────────────────────┬──────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 3: Construct Design                                   │
│  • Write base full factorial                                │
│  • Add columns using generators                             │
│  • Verify defining relation and resolution                  │
│  • Randomize run order                                      │
└──────────────────────────┬──────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 4: Conduct Experiment                                 │
│  • Run experiments in randomized order                      │
│  • Record responses                                         │
│  • Check for outliers/mistakes                              │
└──────────────────────────┬──────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 5: Analyze Data                                       │
│  • Calculate effect estimates                               │
│  • Use normal probability plot or half-normal plot        │
│  • Identify significant effects                             │
│  • Interpret with alias structure in mind                   │
└──────────────────────────┬──────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 6: Follow-up (if needed)                              │
│  • If ambiguities exist: foldover or additional runs        │
│  • If subset identified: full factorial on subset           │
│  • If model adequate: optimize and confirm                  │
└─────────────────────────────────────────────────────────────┘
```

---

## 7. Common Pitfalls

### 7.1 Ignoring Aliasing Structure

**Pitfall:** Treating estimated effects as if they represent single effects.

**Solution:** Always report the alias string. In Resolution III, a significant "A" effect could be A, BC, DE, or any combination.

### 7.2 Choosing Low-Order Generators

**Pitfall:** Using generators with too few letters (e.g., D=AB instead of D=ABC for k=4).

**Solution:** Always maximize resolution. Higher-order generators = better resolution.

### 7.3 Assuming All Higher-Order Interactions Are Zero

**Pitfall:** Assuming 3FIs are always negligible without justification.

**Solution:** Use domain knowledge. In some systems (chemical reactions), 3FIs can be important.

### 7.4 Not Randomizing Run Order

**Pitfall:** Running experiments in standard order, confounding time trends with factor effects.

**Solution:** Always randomize run order. Use blocking if necessary.

### 7.5 Forgetting About Foldover Options

**Pitfall:** Running a full factorial when a foldover would suffice.

**Solution:** After a Resolution III design, a foldover doubles runs but de-aliases all main effects from 2FIs.

### 7.6 Overlooking Minimum Aberration

**Pitfall:** Choosing any design with the right resolution without checking aberration.

**Solution:** Among equal-resolution designs, always choose minimum aberration to minimize confounding.

---

## 8. Comparisons

### 8.1 Full Factorial vs. Fractional Factorial

| Aspect | Full Factorial | Fractional Factorial |
|--------|---------------|---------------------|
| Runs | 2^k | 2^(k-p) |
| All effects estimable | Yes | No (aliasing) |
| Best for | k ≤ 4-5 | k ≥ 5 |
| Analysis complexity | Low | Medium |
| Follow-up needed | Rare | Often |

### 8.2 Resolution III vs. IV vs. V

| Criterion | Resolution III | Resolution IV | Resolution V |
|-----------|---------------|--------------|-------------|
| Main effects clear of 2FIs | No | Yes | Yes |
| 2FIs clear of each other | No | No | Yes |
| Typical use | Screening | Screening + 2FIs | Optimization |
| Run efficiency | Very high | High | Moderate |

### 8.3 Regular vs. Non-Regular Designs

| Aspect | Regular (2^(k-p)) | Plackett-Burman |
|--------|------------------|-----------------|
| Aliasing type | Complete | Partial |
| Number of runs | Power of 2 | Multiple of 4 |
| Analysis | Straightforward | Requires regression |
| Best for | Clear interpretation | Many factors, few runs |

---

## 9. References

### Textbooks
1. **Box, G.E.P., Hunter, J.S., & Hunter, W.G.** (2005). *Statistics for Experimenters: Design, Innovation, and Discovery*. 2nd ed. Wiley.
2. **Montgomery, D.C.** (2019). *Design and Analysis of Experiments*. 10th ed. Wiley.
3. **Wu, C.F.J. & Hamada, M.** (2009). *Experiments: Planning, Analysis, and Parameter Design Optimization*. 2nd ed. Wiley.

### Key Papers
4. **Box, G.E.P. & Hunter, J.S.** (1961). The 2^(k-p) fractional factorial designs. *Technometrics*, 3(3), 311-351.
5. **Fries, A. & Hunter, W.G.** (1980). Minimum aberration 2^(k-p) designs. *Technometrics*, 22(4), 601-608.

### Online Resources
6. NIST/SEMATECH Engineering Statistics Handbook — Fractional Factorial Designs
7. Penn State STAT 503 — Fractional Factorial Designs
8. JMP Statistical Knowledge Portal — Fractional Factorial Designs

---

## Generated Outputs

| File | Description |
|------|-------------|
| `figures/fig01_design_matrix.png` | 2^(6-2) Resolution IV design matrix |
| `figures/fig02_alias_structure.png` | Alias structure visualization |
| `figures/fig03_resolution_comparison.png` | Resolution III/IV/V comparison |
| `figures/fig04_fraction_size.png` | Run size comparison chart |
| `figures/fig05_generator_guide.png` | Generator selection guide |
| `figures/fig06_foldover.png` | Foldover technique illustration |
| `figures/fig07_min_aberration.png` | Minimum aberration concept |

---

*Generated for DoE Lecture 12: Fractional Factorial Design*
