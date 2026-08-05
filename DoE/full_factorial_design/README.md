# DoE Lecture 10: Full Factorial Design

> **Design of Experiments (DoE) — Lecture 10**  
> A comprehensive guide to Full Factorial Designs: concepts, case studies, rules of thumb, and practical implementation.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Key Concepts](#2-key-concepts)
3. [Types of Full Factorial Designs](#3-types-of-full-factorial-designs)
4. [Rules of Thumb](#4-rules-of-thumb)
5. [Case Studies](#5-case-studies)
6. [Step-by-Step Workflow](#6-step-by-step-workflow)
7. [Analysis & Interpretation](#7-analysis--interpretation)
8. [Common Pitfalls](#8-common-pitfalls)
9. [When to Use Full Factorial vs. Other Designs](#9-when-to-use-full-factorial-vs-other-designs)
10. [References & Further Reading](#10-references--further-reading)

---

## 1. Overview

### What is a Full Factorial Design?

A **Full Factorial Design** is an experimental design in which **every possible combination of factor levels is tested**. This allows you to estimate:

- **Main effects** (the individual effect of each factor)
- **All interaction effects** (how factors work together)

Unlike One-Factor-At-a-Time (OFAT) approaches, factorial designs vary all factors simultaneously, making them more efficient and capable of detecting interactions that OFAT would miss.

### Why Use Full Factorial Designs?

| Advantage | Description |
|-----------|-------------|
| **Complete information** | Every combination is tested — no hidden interactions |
| **Interaction detection** | Can identify 2-way, 3-way, and higher-order interactions |
| **Efficiency vs. OFAT** | Fewer total runs for the same precision; every run informs every factor |
| **Model completeness** | Supports fitting a complete model including all interactions |
| **Foundation for RSM** | Often used as a first step before Response Surface Methodology |

### When Are They Used?

- **Screening is complete** — you already know which factors matter (typically ≤ 6 factors)
- **Interactions are suspected** — you need to quantify how factors work together
- **Optimization phase** — you want to build a predictive model for a small set of factors
- **Resources permit** — the number of runs is manageable

---

## 2. Key Concepts

### 2.1 Factors, Levels, and Runs

| Term | Definition | Example |
|------|------------|---------|
| **Factor** | An independent variable you manipulate | Temperature, Pressure, Catalyst Type |
| **Level** | A specific setting/value of a factor | Low (-1), High (+1) for a 2-level factor |
| **Run** | One experimental trial at a specific combination of factor levels | Run 1: Temp=Low, Pressure=Low |
| **Response** | The output variable you measure | Yield, Strength, Purity |

### 2.2 Main Effects

A **main effect** is the change in the response caused by changing the level of a single factor, **averaged over all levels of the other factors**.

```
Main Effect of Factor A = (Average response at A=High) − (Average response at A=Low)
```

### 2.3 Interaction Effects

An **interaction effect** exists when the effect of one factor depends on the level of another factor.

- **2-way interaction (AB)**: How Factor A's effect changes at different levels of Factor B
- **3-way interaction (ABC)**: How the AB interaction changes at different levels of Factor C
- **Higher-order interactions**: Typically negligible (sparsity of effects principle)

**Visual check**: In an interaction plot, parallel lines = no interaction; crossing/non-parallel lines = interaction present.

### 2.4 Coded Variables

Factors are typically coded to simplify analysis:

| Level | Coded Value |
|-------|-------------|
| Low | -1 |
| Center | 0 |
| High | +1 |

This standardization makes effect estimates directly comparable across factors with different units.

---

## 3. Types of Full Factorial Designs

### 3.1 2^k Designs (Two-Level Factorial)

The most common full factorial design. Each of *k* factors has 2 levels (Low/High).

| Design | Factors (k) | Runs (2^k) | Max Interactions |
|--------|-------------|------------|------------------|
| 2² | 2 | 4 | AB |
| 2³ | 3 | 8 | ABC |
| 2⁴ | 4 | 16 | ABCD |
| 2⁵ | 5 | 32 | ABCDE |
| 2⁶ | 6 | 64 | ABCDEF |
| 2⁷ | 7 | 128 | ABCDEFG |

> **Practical limit**: Full factorial designs are typically limited to **≤ 6 factors** in practice due to the exponential growth in runs.

### 3.2 3^k Designs (Three-Level Factorial)

Each factor has 3 levels (Low, Center, High). Allows estimation of **quadratic (curvature) effects**.

| Design | Factors (k) | Runs (3^k) |
|--------|-------------|------------|
| 3² | 2 | 9 |
| 3³ | 3 | 27 |
| 3⁴ | 4 | 81 |

> **Note**: 3^k designs grow even faster than 2^k designs. A 3⁴ design requires 81 runs.

### 3.3 General Full Factorial Designs

Factors can have different numbers of levels (e.g., 2 × 3 × 2 design). Total runs = product of all level counts.

**Example**: A 2 × 3 design (2 factors: one with 2 levels, one with 3 levels) requires 2 × 3 = **6 runs**.

### 3.4 Center Points

Center points (all factors at their middle level) are often added to:
- Test for **curvature** in the response surface
- Provide an estimate of **pure error**
- Improve model fit without dramatically increasing runs

---

## 4. Rules of Thumb

### 4.1 When to Choose Full Factorial

| Situation | Recommendation |
|-----------|----------------|
| **≤ 4 factors** | Full factorial is almost always appropriate |
| **5–6 factors** | Full factorial is feasible but costly; consider if interactions are critical |
| **≥ 7 factors** | Use **fractional factorial** or **screening designs** instead |
| **Need all interactions** | Full factorial is required |
| **Only main effects matter** | Fractional factorial or Plackett-Burman may suffice |
| **Need curvature detection** | Use 3-level design or add center points to 2^k |

### 4.2 Sample Size & Replication

| Rule | Guideline |
|------|-----------|
| **Minimum per cell** | At least **2–3 replicates** per experimental condition for error estimation |
| **Power-based sizing** | Use power analysis: detect effect size δ with power 1−β at significance α |
| **Social science rule** | Minimum **20 subjects per cell** for medium effect sizes (Cohen's power calculations) |
| **Engineering rule** | Start with 1 replicate; add replicates only if error variance is high |
| **Center points** | Add **3–5 center points** to test curvature and estimate pure error |

### 4.3 Factor Level Selection

| Rule | Guideline |
|------|-----------|
| **Range width** | Set levels as far apart as **practically possible** to maximize signal-to-noise ratio |
| **Avoid extrapolation** | Ensure levels span the region of interest, not beyond |
| **Two-level default** | Use 2 levels unless curvature is expected or known |
| **Categorical factors** | Ensure all relevant categories are included |

### 4.4 Design Principles (The "Three R's")

1. **Randomization**: Randomize run order to average out nuisance variables (time trends, operator differences, equipment drift)
2. **Replication**: Repeat runs under identical conditions to estimate experimental error
3. **Blocking**: Group runs into homogeneous blocks when known nuisance variables exist (e.g., different days, different batches)

### 4.5 Effect Significance

| Rule | Guideline |
|------|-----------|
| **Sparsity of effects** | Higher-order interactions (3-way and above) are often negligible — use this to simplify models |
| **Effect hierarchy** | Main effects > 2-way interactions > 3-way interactions > ... |
| **Normal probability plot** | Effects that deviate from the straight line are likely significant |
| **Pareto chart** | Rank effects by magnitude; effects crossing the reference line are significant |
| **p-value threshold** | Typically α = 0.05; adjust for multiple comparisons if needed |

### 4.6 Model Building

| Rule | Guideline |
|------|-----------|
| **Start saturated** | Fit the full model first, then simplify |
| **Keep hierarchy** | If an interaction is significant, keep the corresponding main effects even if they appear insignificant |
| **Check residuals** | Always examine residual plots for normality, constant variance, and independence |
| **Transform if needed** | Use Box-Cox transformation if residuals show non-constant variance |

---

## 5. Case Studies

### Case Study 1: Ceramic Strength Optimization (NIST Engineering Statistics Handbook)

**Context**: Optimize the strength of a ceramic material used in industrial applications.

**Factors & Levels** (2⁵ design, 32 runs):

| Factor | Low (-1) | High (+1) |
|--------|----------|-----------|
| X1: Table Speed | 0.025 m/s | 0.125 m/s |
| X2: Feed Rate | 0.005 mm | 0.125 mm |
| X3: Wheel Grit | 140/170 | 170/200 |
| X4: Direction | Longitudinal | Transverse |
| X5: Batch | Batch 1 | Batch 2 |

**Key Findings**:
- **Direction** was by far the most important factor
- **Batch** was the second most critical factor
- Several **2-way interactions** were significant (e.g., Table Speed × Feed Rate)
- One **3-way interaction** was significant
- A **Box-Cox transformation** (λ ≈ 0.2) was needed to stabilize variance
- Final model achieved **R²_adj = 0.982**

**Lesson**: Even with a well-planned design, always check model assumptions. A transformation can reveal a cleaner model and eliminate spurious interactions.

---

### Case Study 2: Ginger Essential Oil Extraction (Shah et al., 2014)

**Context**: Optimize solvent-free microwave extraction of essential oil from ginger.

**Design**: 2³ full factorial with **2 replicates per run** (16 total runs)

| Factor | Low (-1) | High (+1) |
|--------|----------|-----------|
| X1: Extraction Time | 10 min | 30 min |
| X2: Microwave Power | 288 W | 640 W |
| X3: Sample Type | Crushed | Sliced |

**Response**: Oil yield (%)

**Key Findings**:
- All three main effects were significant
- Interactions between time, power, and sample type influenced yield
- Optimal conditions were identified for maximum oil extraction
- Design-Expert software was used for design and analysis

**Lesson**: Full factorial designs with replication provide robust estimates of both effects and experimental error, enabling confident optimization.

---

### Case Study 3: Fluoride Removal by Donnan Dialysis (Boubakri et al., 2014)

**Context**: Investigate physico-chemical factors affecting fluoride removal from drinking water.

**Design**: 2⁴ full factorial + **4 center points** (20 total runs)

| Factor | Low (-1) | Center (0) | High (+1) |
|--------|----------|------------|-----------|
| C: Concentration | 5 mg/L | 10 mg/L | 15 mg/L |
| Q: Flow Rate | 0.4 L/h | 0.7 L/h | 1.0 L/h |
| A: Agitation Speed | 167 rpm | 500 rpm | 833 rpm |
| T: Temperature | 25°C | 30°C | 35°C |

**Responses**: Fluoride removal efficiency (%) and Fluoride flux (mg/cm²·h)

**Key Findings**:
- Removal efficiency ranged from 34.14% to 75.52%
- All 14 estimated effects were evaluated using Pareto charts and p-values
- Center points enabled testing for curvature in the response surface
- Final prediction models were developed for both responses

**Lesson**: Adding center points to a 2^k design is a cost-effective way to test for curvature without committing to a full 3^k design.

---

### Case Study 4: NASA Wind Tunnel Testing — OH-58F Helicopter

**Context**: Characterize aerodynamic download and drag on a helicopter fuselage model.

**Design**: Combined **Spherical CCD + Face-Centered CCD** (modified for wind tunnel constraints)

| Factor | Low (-1) | High (+1) |
|--------|----------|-----------|
| Angle of Attack (α) | −3° | +3° |
| Sideslip Angle (β) | −5° | +5° |
| Advance Ratio (μ) | 0.15 | 0.30 |
| Thrust Coefficient (C_T) | 0.004 | 0.010 |

**Key Findings**:
- DOE approach revealed interactions that OFAT testing missed
- Surface response models were built for download and drag
- Replicates at center points estimated experimental error
- DOE achieved better coverage of the design space with fewer runs than OFAT

**Lesson**: In complex, expensive experiments (like wind tunnel testing), DOE maximizes information per run and detects interactions that sequential OFAT approaches cannot.

---

### Case Study 5: Membrane Cleaning Optimization (Chen et al., 2003)

**Context**: Optimize physical and chemical cleaning of ultrafiltration (UF) and reverse osmosis (RO) membranes.

**Design**: Sequential fractional factorial designs with foldover

**Physical Cleaning (UF)**:
- Initial: Resolution III 2^(6−3) design (8 runs)
- Follow-up: Complete foldover → Resolution IV 2^(6−3) design (16 runs)

**Key Findings**:
- Initial screening identified important factors
- Foldover resolved aliasing and improved resolution
- Final models predicted clean water flux recovery and wash water usage

**Lesson**: Full factorial designs can be preceded by fractional factorial screening. When resources are limited, a sequential strategy (screen → foldover → full factorial if needed) is efficient.

---

## 6. Step-by-Step Workflow

### Step 1: Define the Problem
- Identify the **response variable(s)**
- List candidate **factors** based on subject-matter expertise
- Determine the **objective**: screening, characterization, or optimization

### Step 2: Select Factor Levels
- Choose **2 levels** per factor (unless curvature is expected)
- Set levels as far apart as practical
- Ensure levels are **feasible and safe**

### Step 3: Choose the Design
- Count factors (*k*)
- Calculate runs: **n = 2^k** (for 2-level designs)
- Decide on **replicates** and **center points**
- Verify resources (time, budget, materials)

### Step 4: Randomize & Block
- **Randomize** run order
- Use **blocking** if known nuisance variables exist (e.g., day, batch, operator)

### Step 5: Execute the Experiment
- Follow the design matrix exactly
- Record all data carefully
- Note any **deviations** or **unexpected events**

### Step 6: Analyze the Data
1. Fit the full model (main effects + all interactions)
2. Use **ANOVA** to test significance
3. Create **normal probability plot** of effects
4. Create **Pareto chart** of effect magnitudes
5. Simplify the model by removing non-significant terms (respect hierarchy)
6. Check **residual plots** (normality, constant variance, independence)
7. Apply **Box-Cox transformation** if residuals violate assumptions

### Step 7: Interpret & Optimize
- Plot **main effects** and **significant interactions**
- Identify **optimal factor settings**
- Use **contour plots** or **surface plots** for visualization
- Validate predictions with **confirmation runs**

### Step 8: Document & Report
- Document the design, analysis, and conclusions
- Include effect estimates, ANOVA tables, and diagnostic plots
- Report optimal settings with confidence intervals

---

## 7. Analysis & Interpretation

### 7.1 ANOVA Table Structure

| Source | SS | df | MS | F | p-value |
|--------|----|----|----|---|---------|
| Main Effects | ... | k | ... | ... | ... |
| 2-Way Interactions | ... | C(k,2) | ... | ... | ... |
| 3-Way Interactions | ... | C(k,3) | ... | ... | ... |
| Error (Pure Error) | ... | ... | MSE | — | — |
| Total | ... | n−1 | — | — | — |

### 7.2 Effect Estimates

For a 2^k design, the effect of a factor or interaction is calculated as:

```
Effect = (Sum of responses at High) − (Sum of responses at Low) / (n/2)
```

Half of this value gives the **regression coefficient** for the coded model.

### 7.3 Model Equation (Coded Form)

```
ŷ = β₀ + β₁x₁ + β₂x₂ + β₃x₃ + β₁₂x₁x₂ + β₁₃x₁x₃ + β₂₃x₂x₃ + β₁₂₃x₁x₂x₃ + ε
```

Where:
- β₀ = overall mean (intercept)
- βᵢ = half the main effect of factor *i*
- βᵢⱼ = half the 2-way interaction effect
- βᵢⱼₖ = half the 3-way interaction effect

### 7.4 Diagnostic Checks

| Check | Tool | What to Look For |
|-------|------|------------------|
| Normality | Normal probability plot of residuals | Points follow straight line |
| Constant variance | Residuals vs. fitted values | Random scatter, no funnel shape |
| Independence | Residuals vs. run order | No patterns or trends |
| Outliers | Box plot of residuals | Points beyond ±3σ |

---

## 8. Common Pitfalls

| Pitfall | Why It Happens | How to Avoid |
|---------|----------------|--------------|
| **Too many factors** | Exponential run growth (2^k) | Limit to ≤ 6 factors; use screening first |
| **Ignoring interactions** | Assuming factors act independently | Always test for interactions; don't drop them prematurely |
| **Poor level selection** | Levels too close or too far apart | Use subject-matter expertise; pilot studies help |
| **No randomization** | Convenience ordering | Always randomize run order |
| **No replication** | Resource constraints | At least 2–3 replicates for error estimation |
| **Skipping residual checks** | Time pressure or inexperience | Residual analysis is mandatory, not optional |
| **Overfitting** | Keeping too many terms | Use p-values, AIC/BIC, and cross-validation |
| **Violating hierarchy** | Dropping main effects but keeping interactions | Always retain main effects if their interactions are significant |
| **Extrapolation** | Predicting outside the design space | Stay within the factor ranges tested |

---

## 9. When to Use Full Factorial vs. Other Designs

| Design | Best For | Number of Factors | Runs | Interactions |
|--------|----------|-------------------|------|--------------|
| **Full Factorial (2^k)** | Complete characterization, all interactions | 2–6 | 2^k | All |
| **Fractional Factorial (2^(k−p))** | Screening, many factors | 5–15 | 2^(k−p) | Some aliased |
| **Plackett-Burman** | Screening, very many factors | 7–47 | k+1 | Main effects only |
| **3^k or CCD** | Curvature/optimization | 2–4 | 9–20+ | All + quadratic |
| **Box-Behnken** | Optimization, avoid extremes | 3–7 | ~15–30 | All + quadratic |
| **D-Optimal** | Irregular constraints | Variable | Custom | Selected |

### Decision Flowchart

```
Start
  │
  ▼
How many factors?
  │
  ├── > 10 ──→ Plackett-Burman or D-Optimal (Screening)
  │
  ├── 5–10 ──→ Fractional Factorial (2^(k−p))
  │              │
  │              └── Significant interactions found?
  │                    ├── Yes ──→ Augment to Full Factorial
  │                    └── No  ──→ Continue with fractional
  │
  ├── 3–5  ──→ Full Factorial (2^k) or CCD
  │              │
  │              └── Curvature suspected?
  │                    ├── Yes ──→ CCD or 3^k + center points
  │                    └── No  ──→ 2^k Full Factorial
  │
  └── ≤ 2  ──→ Full Factorial (2² or 3²)
```

---

## 10. References & Further Reading

### Textbooks
1. **Montgomery, D. C.** (2017). *Design and Analysis of Experiments* (10th ed.). Wiley. — The definitive reference for DoE.
2. **Box, G. E. P., Hunter, J. S., & Hunter, W. G.** (2005). *Statistics for Experimenters* (2nd ed.). Wiley. — Classic text with excellent practical guidance.
3. **Myers, R. H., Montgomery, D. C., & Anderson-Cook, C. M.** (2016). *Response Surface Methodology* (4th ed.). Wiley. — For optimization after factorial screening.

### Online Resources
4. **NIST/SEMATECH Engineering Statistics Handbook** — [Section 5.4: Full Factorial Designs](https://www.itl.nist.gov/div898/handbook/pri/section4/pri4.htm) — Excellent worked examples.
5. **Statease: Applications of DOE in Engineering and Science** — Collection of 26 real-world case studies.

### Software
6. **Minitab** — Industry standard for DoE analysis
7. **Design-Expert** — Specialized DoE software with excellent visualization
8. **JMP** — SAS-based platform with powerful DoE capabilities
9. **R packages**: `FrF2`, `DoE.base`, `rsm`, `BDEsize`
10. **Python**: `pyDOE2`, `statsmodels`, `scikit-learn`

### Key Papers
11. **Shah, M., & Garg, S. K.** (2014). Application of 2^k full factorial design in optimization of solvent-free microwave extraction of ginger essential oil. *Journal of Engineering*.
12. **Boubakri, A., et al.** (2014). Fluoride removal from diluted solutions by Donnan analysis using full factorial design. *Korean Journal of Chemical Engineering*.
13. **Chen, J. P., Kim, S. L., & Ting, Y. P.** (2003). Optimization of membrane physical and chemical cleaning by a statistical designed approach. *Journal of Membrane Science*.
14. **Tanner, P., et al.** (2016). Case Studies for the Statistical Design of Experiments Applied to Powered Rotor Wind Tunnel Testing. *NASA Technical Report*.

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────────┐
│                    FULL FACTORIAL DESIGN                          │
├─────────────────────────────────────────────────────────────────┤
│  Runs for 2^k: n = 2^k                                           │
│  Runs for general: n = l₁ × l₂ × ... × l_k                      │
│                                                                   │
│  Effects estimable: All main effects + all interactions           │
│                                                                   │
│  Practical limit: k ≤ 6 factors (2^k ≤ 64 runs)                  │
│                                                                   │
│  Always: Randomize, replicate, check residuals                    │
│  Add: 3–5 center points for curvature testing                     │
│                                                                   │
│  Analysis: ANOVA → Normal plot → Pareto → Model simplification   │
│  Diagnostics: Residual plots → Box-Cox if needed                  │
└─────────────────────────────────────────────────────────────────┘
```

---

*Last updated: August 2026*  
*For questions or corrections, please open an issue.*
