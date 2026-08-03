# DoE Lecture 8: Multiple Testing with FWER

> A comprehensive guide to Family-Wise Error Rate (FWER) control in multiple hypothesis testing, covering methods, case studies, comparisons, and practical implementation.

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [The Multiple Testing Problem](#2-the-multiple-testing-problem)
3. [FWER: Definition & Mathematical Formulation](#3-fwer-definition--mathematical-formulation)
4. [FWER Control Methods](#4-fwer-control-methods)
   - 4.1 [Bonferroni Correction](#41-bonferroni-correction)
   - 4.2 [Šidák Correction](#42-šídák-correction)
   - 4.3 [Holm-Bonferroni (Step-Down)](#43-holm-bonferroni-step-down)
   - 4.4 [Hochberg Procedure (Step-Up)](#44-hochberg-procedure-step-up)
   - 4.5 [Hommel Procedure](#45-hommel-procedure)
   - 4.6 [Permutation-Based Methods](#46-permutation-based-methods)
5. [Case Studies](#5-case-studies)
   - 5.1 [Case Study 1: E-commerce A/B Testing](#51-case-study-1-e-commerce-ab-testing)
   - 5.2 [Case Study 2: Clinical Trial with Multiple Endpoints](#52-case-study-2-clinical-trial-with-multiple-endpoints)
   - 5.3 [Case Study 3: Genomics — Pharmacodynamic Study](#53-case-study-3-genomics--pharmacodynamic-study)
   - 5.4 [Case Study 4: Allergy & Hypersensitivity Disease Investigation](#54-case-study-4-allergy--hypersensitivity-disease-investigation)
6. [Method Comparison](#6-method-comparison)
   - 6.1 [Power Comparison Table](#61-power-comparison-table)
   - 6.2 [Decision Framework](#62-decision-framework)
   - 6.3 [When to Use What](#63-when-to-use-what)
7. [FWER vs. FDR: When to Choose Which](#7-fwer-vs-fdr-when-to-choose-which)
8. [Practical Implementation](#8-practical-implementation)
   - 8.1 [R Code](#81-r-code)
   - 8.2 [Python Code](#82-python-code)
9. [Common Pitfalls & Best Practices](#9-common-pitfalls--best-practices)
10. [References](#10-references)

---

## 1. Introduction

When conducting a single hypothesis test at significance level $lpha = 0.05$, the probability of a Type I error (false positive) is exactly 5%. However, in modern data analysis — from clinical trials with multiple endpoints to genomics studies testing thousands of genes — researchers routinely conduct **many hypothesis tests simultaneously**.

Without correction, the probability of making **at least one false rejection** across all tests inflates dramatically. For $m$ independent tests at level $lpha$:

$$
\text{FWER} = P(\text{at least one false rejection}) = 1 - (1 - \alpha)^m
$$

| Number of Tests ($m$) | FWER at $\alpha = 0.05$ |
|----------------------|------------------------|
| 1                    | 5.0%                   |
| 5                    | 22.6%                  |
| 10                   | 40.1%                  |
| 20                   | 64.2%                  |
| 50                   | 92.3%                  |
| 100                  | 99.4%                  |

This guide covers **Family-Wise Error Rate (FWER)** control methods — the gold standard for confirmatory research where even a single false positive carries serious consequences.

---

## 2. The Multiple Testing Problem

### 2.1 Why It Matters

The multiple comparisons problem is not a theoretical curiosity — it has real consequences:

- **Clinical trials**: Regulatory agencies (FDA, EMA) require multiplicity adjustment for confirmatory trials with co-primary endpoints.
- **Genomics**: Studies routinely test tens of thousands of genes; uncorrected analysis leads to unreliable results.
- **A/B testing**: Testing multiple website variants without correction yields a high chance of implementing "winners" that are actually false positives.

### 2.2 Hidden Multiplicity

Multiple testing can be hidden in various ways:
- Testing many subgroups without pre-specification
- Analyzing data at multiple time points
- Testing multiple outcomes without correction
- "Peeking" at data during sequential collection
- Testing different model specifications

All of these constitute multiple testing and require appropriate correction.

---

## 3. FWER: Definition & Mathematical Formulation

### 3.1 Definition

The **Family-Wise Error Rate (FWER)** is the probability of making **at least one Type I error** (false positive) across a family of $m$ hypothesis tests:

$$
\text{FWER} = P(\text{reject at least one true } H_0) = P(V \geq 1)
$$

where $V$ is the number of true null hypotheses that are falsely rejected.

### 3.2 Strong vs. Weak Control

- **Strong FWER control**: $\text{FWER} \leq \alpha$ regardless of which null hypotheses are true.
- **Weak FWER control**: $\text{FWER} \leq \alpha$ only when **all** null hypotheses are true.

All methods discussed in this guide provide **strong FWER control**.

### 3.3 The Error Rate Inflation

For $m$ independent tests, each at level $\alpha$:

$$
\text{FWER} = 1 - (1 - \alpha)^m \approx m\alpha \quad \text{(for small } \alpha)
$$

This is the basis for the Bonferroni correction.

---

## 4. FWER Control Methods

### 4.1 Bonferroni Correction

**Method**: Reject $H_{0,i}$ if $p_i \leq \alpha / m$

**Adjusted p-values**: $\tilde{p}_i = \min(m \cdot p_i, 1)$

**Assumptions**: None — valid under any dependence structure.

**Pros**:
- Simple to understand and implement
- Guaranteed FWER control regardless of test dependence
- No need to order p-values

**Cons**:
- Very conservative, especially for large $m$
- Low statistical power
- Can be overly conservative when tests are positively correlated

**Example**: For $m = 20$ tests at $\alpha = 0.05$:
- Threshold: $0.05 / 20 = 0.0025$

---

### 4.2 Šidák Correction

**Method**: Reject $H_{0,i}$ if $p_i \leq 1 - (1 - \alpha)^{1/m}$

**Adjusted p-values**: $\tilde{p}_i = 1 - (1 - p_i)^m$

**Assumptions**: Tests must be **independent** (or have specific dependence structures).

**Pros**:
- Slightly less conservative than Bonferroni
- Exact FWER control under independence

**Cons**:
- Requires independence assumption
- Power gain over Bonferroni is typically small

**Comparison** (for $m = 20$, $\alpha = 0.05$):
- Bonferroni threshold: $0.00250$
- Šidák threshold: $0.00256$

---

### 4.3 Holm-Bonferroni (Step-Down)

**Method** (Step-Down Procedure):

1. Order p-values: $p_{(1)} \leq p_{(2)} \leq \dots \leq p_{(m)}$
2. For $i = 1, 2, \dots, m$:
   - Compare $p_{(i)}$ to $\alpha / (m - i + 1)$
   - If $p_{(i)} \leq \alpha / (m - i + 1)$, **reject** $H_{0,(i)}$ and continue
   - If $p_{(i)} > \alpha / (m - i + 1)$, **retain** $H_{0,(i)}$ and **stop** (retain all remaining)

**Adjusted p-values**: 
$$\tilde{p}_{(i)} = \max_{j \leq i} \left\{ \min((m - j + 1) \cdot p_{(j)}, 1) \right\}$$

**Assumptions**: None — valid under any dependence structure.

**Key Insight**: Holm is **uniformly more powerful** than Bonferroni — it rejects everything Bonferroni rejects and potentially more, while maintaining the same FWER guarantee.

**Example** ($m = 5$, $\alpha = 0.05$):

| Rank ($i$) | $p_{(i)}$ | Threshold ($\alpha/(m-i+1)$) | Decision |
|-----------|-----------|------------------------------|----------|
| 1         | 0.003     | $0.05/5 = 0.010$             | Reject   |
| 2         | 0.018     | $0.05/4 = 0.0125$            | Retain   |
| 3         | 0.042     | $0.05/3 = 0.0167$            | Retain   |
| 4         | 0.089     | $0.05/2 = 0.025$             | Retain   |
| 5         | 0.234     | $0.05/1 = 0.05$              | Retain   |

**Result**: Only the smallest p-value (0.003) is rejected.

---

### 4.4 Hochberg Procedure (Step-Up)

**Method** (Step-Up Procedure):

1. Order p-values: $p_{(1)} \leq p_{(2)} \leq \dots \leq p_{(m)}$
2. Start from the **largest** p-value and work **downward**:
   - Find the largest $i$ such that $p_{(i)} \leq \alpha / (m - i + 1)$
   - **Reject** all hypotheses $H_{0,(1)}, \dots, H_{0,(i)}$

**Assumptions**: Requires **independence** or **positive dependence** among test statistics (Simes' condition).

**Pros**:
- More powerful than Holm when independence/positive dependence holds
- Still controls FWER strongly

**Cons**:
- Requires independence or positive dependence assumption
- Not universally valid like Holm

---

### 4.5 Hommel Procedure

**Method**: A more complex step-up procedure that is even more powerful than Hochberg.

**Assumptions**: Independence or positive dependence.

**Pros**:
- Most powerful among the classical FWER methods

**Cons**:
- Computationally intensive for large $m$
- Complex to implement and explain
- Rarely used in practice due to complexity

---

### 4.6 Permutation-Based Methods

**Method**: Resample the data to estimate the null distribution of the maximum test statistic, then use this empirical distribution to control FWER.

**Assumptions**: Exchangeability under the null hypothesis.

**Pros**:
- Accounts for the actual dependence structure in the data
- Can be more powerful than analytical methods when tests are correlated
- No parametric assumptions needed

**Cons**:
- Computationally intensive
- Requires careful implementation
- Results can vary across different random seeds

**Best for**: Time series, spatial data, or any setting with strong, structured dependencies.

---

## 5. Case Studies

### 5.1 Case Study 1: E-commerce A/B Testing

**Context**: An e-commerce company tests five new homepage designs against the current version, measuring conversion rate improvements. Each variant has 10,000 visitors. Tests are two-proportion z-tests at $\alpha = 0.05$.

**Raw p-values**:

| Design | Raw p-value |
|--------|-------------|
| A      | 0.003       |
| B      | 0.018       |
| C      | 0.042       |
| D      | 0.089       |
| E      | 0.234       |

#### Analysis Without Correction

Three designs (A, B, C) appear significant at $\alpha = 0.05$.

**Problem**: With 5 tests, $\text{FWER} = 1 - (1 - 0.05)^5 = 22.6\%$. There's a ~1 in 4 chance that at least one "winner" is a false positive.

#### Bonferroni Correction

Threshold: $0.05 / 5 = 0.01$

| Design | p-value | vs. 0.01 | Decision |
|--------|---------|----------|----------|
| A      | 0.003   | < 0.01   | ✅ Reject |
| B      | 0.018   | > 0.01   | ❌ Retain |
| C      | 0.042   | > 0.01   | ❌ Retain |
| D      | 0.089   | > 0.01   | ❌ Retain |
| E      | 0.234   | > 0.01   | ❌ Retain |

**Result**: Only Design A is significant. Bonferroni may be throwing away real improvements in Design B.

#### Holm-Bonferroni

| Rank | Design | p-value | Threshold | Decision |
|------|--------|---------|-----------|----------|
| 1    | A      | 0.003   | 0.05/5 = 0.010 | ✅ Reject |
| 2    | B      | 0.018   | 0.05/4 = 0.0125 | ❌ Retain (STOP) |

**Result**: Same as Bonferroni in this case — only Design A is significant. But Holm would have rejected more if p-values were more favorable.

#### Business Impact
- **Without correction**: Risk of implementing 2-3 false "winners", wasting development resources
- **With FWER control**: Confident that Design A is genuinely better; may miss some real improvements but avoids costly false implementations

---

### 5.2 Case Study 2: Clinical Trial with Multiple Endpoints

**Context**: A Phase III randomized, double-blind trial evaluating a new anti-inflammatory drug for rheumatoid arthritis. 400 patients (200 treatment, 200 placebo), 24-week follow-up.

**Pre-specified endpoints** (all tested at $\alpha = 0.05$ with Holm-Bonferroni):

| Endpoint | Raw p-value | Primary? |
|----------|-------------|----------|
| Pain reduction (VAS) | 0.001 | Yes |
| C-reactive protein | 0.008 | No |
| Morning stiffness | 0.015 | No |
| Joint swelling count | 0.031 | No |
| Patient global assessment | 0.067 | No |

#### Why FWER (Not FDR)?

In clinical trials, each significant endpoint may appear on the drug's approved label, directly influencing prescribing decisions for millions of patients. A false claim about joint swelling improvement could lead clinicians to choose this drug over a genuinely better alternative. **Regulatory agencies (FDA, EMA) require FWER control for confirmatory trials.**

#### Holm-Bonferroni Analysis

| Rank | Endpoint | p-value | Threshold | Decision |
|------|----------|---------|-----------|----------|
| 1    | Pain reduction | 0.001 | 0.05/5 = 0.010 | ✅ Reject |
| 2    | CRP | 0.008 | 0.05/4 = 0.0125 | ✅ Reject |
| 3    | Morning stiffness | 0.015 | 0.05/3 = 0.0167 | ✅ Reject |
| 4    | Joint swelling | 0.031 | 0.05/2 = 0.025 | ❌ Retain (STOP) |

**Result**: Pain reduction, CRP, and morning stiffness are significant. Joint swelling and patient global assessment are retained.

#### Comparison with Bonferroni

Bonferroni threshold for all: $0.05/5 = 0.01$
- Would reject: Pain reduction (0.001), CRP (0.008)
- Would retain: Morning stiffness (0.015 > 0.01)

**Holm gains one additional significant endpoint** (morning stiffness) over Bonferroni at no cost to FWER control.

#### Regulatory Implication

In a trial costing hundreds of millions of dollars, the additional power to detect real endpoints translates directly into:
- Broader labeling claims
- Larger addressable market
- Better patient outcomes

---

### 5.3 Case Study 3: Genomics — Pharmacodynamic Study

**Context**: A pharmacodynamic study examining 15 hypotheses about drug effects on various biomarkers. Initial weights of $1/15$ assigned to each hypothesis.

**Methods Applied**:
- Generalized graphical procedures for $k$-FWER control ($k = 1, 2, 3$)
- Augmented graphical procedures
- FDP (False Discovery Proportion) control at $\gamma = 0.1, 0.2, 0.3$

**Results**:

| Procedure | $k$ / $\gamma$ | Rejected Hypotheses |
|-----------|----------------|---------------------|
| $k$-FWER Generalized | $k = 1$ | 7 |
| $k$-FWER Generalized | $k = 2$ | 8 |
| $k$-FWER Generalized | $k = 3$ | More than 8 |
| FDP Generalized | $\gamma = 0.1$ | 7 |
| FDP Generalized | $\gamma = 0.2$ | 8 |
| FDP Generalized | $\gamma = 0.3$ | 8 (or more with augmentation) |

**Key Insight**: The $k$-FWER and FDP controlling procedures give the same rejections for corresponding parameter values ($k=1$ ↔ $\gamma=0.1$; $k=2$ ↔ $\gamma=0.2$). The augmented procedure can reject more hypotheses by propagating significance levels.

**Note**: In high-dimensional genomics (thousands of genes), FWER methods become extremely conservative. FDR control (Benjamini-Hochberg) is typically preferred for exploratory genomics, while FWER is reserved for confirmatory subsets.

---

### 5.4 Case Study 4: Allergy & Hypersensitivity Disease Investigation

**Context**: Investigating associations between environmental exposures and allergy/hypersensitivity diseases (AHD) using exposomic datasets. Multiple hypothesis testing is common because AHD are multifactorial, affecting different organs with varying severity.

**Study Design**: Simulated and real data with four methods compared:
- Bonferroni
- Šidák
- Holm-Bonferroni
- Benjamini-Hochberg (FDR)

**Performance Metrics**: False negatives, sensitivity, specificity, positive predictive value (PPV), negative predictive value (NPV).

**Results**:

| Method | Conservatism | Power | Best For |
|--------|-------------|-------|----------|
| Bonferroni | Most conservative | Lowest | Quick, strict correction |
| Šidák | Very conservative | Low | Independent tests only |
| **Holm-Bonferroni** | **Balanced** | **Moderate** | **Default FWER control** |
| Benjamini-Hochberg | Least conservative | Highest | Exploratory analysis |

**Conclusion**: The Holm-Bonferroni method offers a favorable balance between statistical power and stringent control of false positives, providing researchers confidence in any statistically significant findings. The choice depends on study objectives, number of tests, and assumptions about dependence.

---

## 6. Method Comparison

### 6.1 Power Comparison Table

| Method | Type | Controls | Power | Independence Required? | Best For |
|--------|------|----------|-------|----------------------|----------|
| **Bonferroni** | Single-step | FWER | ⭐ Lowest | ❌ No | Quick conservative correction; any dependence |
| **Šidák** | Single-step | FWER | ⭐⭐ Low | ✅ Yes | Independent tests; slightly better than Bonferroni |
| **Holm-Bonferroni** | Step-down | FWER | ⭐⭐⭐ Moderate | ❌ No | **Default FWER control**; universally valid |
| **Hochberg** | Step-up | FWER | ⭐⭐⭐⭐ High | ✅ Yes | Independent/positive dependence; max power under FWER |
| **Hommel** | Step-up | FWER | ⭐⭐⭐⭐⭐ Highest | ✅ Yes | Complex settings; computationally intensive |
| **Permutation** | Resampling | FWER | Variable | Exchangeability | Strongly correlated tests |

### 6.2 Decision Framework

```
                    START
                      │
                      ▼
        Are you doing CONFIRMATORY research?
        (regulatory, medical, definitive claims)
                      │
          ┌───────────┴───────────┐
          │ YES                   │ NO
          ▼                       ▼
    Use FWER control          Use FDR control
    (Bonferroni/Holm)         (Benjamini-Hochberg)
          │
          ▼
    Are tests INDEPENDENT or
    POSITIVELY dependent?
          │
    ┌─────┴─────┐
    │ YES       │ NO / UNKNOWN
    ▼           ▼
  Use Hochberg  Use Holm-Bonferroni
  (more power)  (universally valid)
```

### 6.3 When to Use What

| Scenario | Recommended Method | Rationale |
|----------|-------------------|-----------|
| Clinical trial, multiple endpoints | Holm or Hochberg | Regulatory requirement; FWER control mandatory |
| E-commerce A/B testing (few variants) | Holm-Bonferroni | Prevent false "winners"; easy to explain |
| Genomics (GWAS, 500K SNPs) | Benjamini-Hochberg (FDR) | FWER too conservative; screening phase |
| Genomics (confirmatory subset) | Holm-Bonferroni | Validate top hits from discovery |
| Quality control (multiple metrics) | Holm-Bonferroni | Can't afford false alarms |
| Financial time series | Permutation-based | Strong correlations invalidate analytical methods |
| ANOVA post-hoc (all pairs) | Tukey HSD | Designed for pairwise comparisons |
| ANOVA post-hoc (vs. control) | Dunnett | Designed for control comparisons |

---

## 7. FWER vs. FDR: When to Choose Which

### 7.1 Key Differences

| Aspect | FWER | FDR |
|--------|------|-----|
| **Definition** | $P(V \geq 1)$ — probability of ANY false positive | $E[V/R]$ — expected proportion of false positives among rejections |
| **Goal** | Zero false positives (with high probability) | Tolerate some false positives for more discoveries |
| **Power** | Lower | Higher |
| **Best for** | Confirmatory research | Exploratory research |
| **Examples** | Clinical trials, regulatory submissions | Genomics screening, feature selection |

### 7.2 The Trade-off

- **FWER methods** (Bonferroni, Holm, Hochberg): Control the probability of making ANY false rejection. More conservative, fewer discoveries, but higher confidence in each one.
- **FDR methods** (Benjamini-Hochberg): Control the EXPECTED proportion of false rejections among all rejections. Less conservative, more discoveries, but some may be false.

### 7.3 Rule of Thumb

| Context | Choose |
|---------|--------|
| Each false positive carries severe consequences | FWER |
| You are screening for candidates to validate later | FDR |
| $m < 100$ | FWER or FDR (either works) |
| $m > 1000$ | FDR (FWER too conservative) |
| Regulatory submission required | FWER |
| Discovery/screening phase | FDR |

---

## 8. Practical Implementation

### 8.1 R Code

```r
# ============================================
# FWER Control Methods in R
# ============================================

# Sample p-values from a study with 10 tests
p_values <- c(0.001, 0.008, 0.015, 0.031, 0.042, 
              0.067, 0.089, 0.123, 0.234, 0.456)

# --- Bonferroni Correction ---
bonf_adj <- p.adjust(p_values, method = "bonferroni")
cat("Bonferroni significant:", sum(bonf_adj < 0.05), "\n")

# --- Holm-Bonferroni ---
holm_adj <- p.adjust(p_values, method = "holm")
cat("Holm significant:", sum(holm_adj < 0.05), "\n")

# --- Hochberg (requires independence/positive dependence) ---
hoch_adj <- p.adjust(p_values, method = "hochberg")
cat("Hochberg significant:", sum(hoch_adj < 0.05), "\n")

# --- Benjamini-Hochberg (FDR) for comparison ---
bh_adj <- p.adjust(p_values, method = "BH")
cat("BH (FDR) significant:", sum(bh_adj < 0.05), "\n")

# --- Comprehensive Comparison Table ---
results <- data.frame(
  Test = 1:length(p_values),
  Raw = p_values,
  Bonferroni = bonf_adj,
  Holm = holm_adj,
  Hochberg = hoch_adj,
  BH_FDR = bh_adj
)
print(results)

# --- Simulation: Power Comparison ---
set.seed(42)
m <- 20
n_true <- 5
n_null <- m - n_true

# Generate p-values
p_true <- replicate(n_true, t.test(rnorm(30, mean = 0.8, sd = 1), mu = 0)$p.value)
p_null <- runif(n_null, 0, 1)
pvals <- c(p_true, p_null)
truth <- c(rep("True Effect", n_true), rep("Null", n_null))

# Apply corrections
bonf <- p.adjust(pvals, method = "bonferroni")
holm <- p.adjust(pvals, method = "holm")
bh   <- p.adjust(pvals, method = "BH")

alpha <- 0.05
cat("\n=== Number of Rejections (alpha = 0.05) ===\n")
cat(sprintf("Bonferroni : %d / %d\n", sum(bonf < alpha), m))
cat(sprintf("Holm       : %d / %d\n", sum(holm < alpha), m))
cat(sprintf("BH (FDR)   : %d / %d\n", sum(bh < alpha), m))

cat("\n=== False Positives ===\n")
cat(sprintf("Bonferroni : %d\n", sum(bonf[truth == "Null"] < alpha)))
cat(sprintf("Holm       : %d\n", sum(holm[truth == "Null"] < alpha)))
cat(sprintf("BH (FDR)   : %d\n", sum(bh[truth == "Null"] < alpha)))
```

### 8.2 Python Code

```python
# ============================================
# FWER Control Methods in Python
# ============================================

import numpy as np
from scipy import stats
from scipy.stats import false_discovery_control

# --- Bonferroni Correction ---
def bonferroni_correction(p_values, alpha=0.05):
    p = np.asarray(p_values)
    m = len(p)
    rejected = p < (alpha / m)
    adjusted_p = np.minimum(p * m, 1.0)
    return adjusted_p, rejected

# --- Holm-Bonferroni (Step-Down) ---
def holm_bonferroni(p_values, alpha=0.05):
    p = np.asarray(p_values)
    m = len(p)
    order = np.argsort(p)
    sorted_p = p[order]

    # Step-down procedure
    thresholds = alpha / np.arange(m, 0, -1)
    rejected_sorted = sorted_p <= thresholds

    # Find first non-rejection
    if not np.any(rejected_sorted):
        rejected = np.zeros(m, dtype=bool)
    else:
        # All hypotheses up to the last consecutive rejection
        first_non_reject = np.where(~rejected_sorted)[0]
        if len(first_non_reject) == 0:
            n_reject = m
        else:
            n_reject = first_non_reject[0]

        rejected_sorted.fill(False)
        rejected_sorted[:n_reject] = True

        # Map back to original order
        rejected = np.zeros(m, dtype=bool)
        rejected[order] = rejected_sorted

    # Adjusted p-values
    adjusted_p = np.zeros(m)
    adjusted_p[order] = np.minimum.accumulate(sorted_p * np.arange(m, 0, -1))
    adjusted_p = np.minimum(adjusted_p, 1.0)

    return adjusted_p, rejected

# --- Šidák Correction ---
def sidak_correction(p_values, alpha=0.05):
    p = np.asarray(p_values)
    m = len(p)
    alpha_adj = 1 - (1 - alpha) ** (1 / m)
    adjusted_p = 1 - (1 - p) ** m
    rejected = p < alpha_adj
    return adjusted_p, rejected

# --- Example Usage ---
p_values = np.array([0.001, 0.008, 0.015, 0.031, 0.042, 
                     0.067, 0.089, 0.123, 0.234, 0.456])

print("=" * 50)
print("FWER CONTROL METHODS COMPARISON")
print("=" * 50)

# Bonferroni
bonf_adj, bonf_rej = bonferroni_correction(p_values)
print(f"\nBonferroni — Significant: {sum(bonf_rej)}")

# Holm
holm_adj, holm_rej = holm_bonferroni(p_values)
print(f"Holm-Bonferroni — Significant: {sum(holm_rej)}")

# Šidák
sidak_adj, sidak_rej = sidak_correction(p_values)
print(f"Šidák — Significant: {sum(sidak_rej)}")

# BH (FDR) for comparison
bh_adj = false_discovery_control(p_values, method="bh")
bh_rej = bh_adj < 0.05
print(f"Benjamini-Hochberg (FDR) — Significant: {sum(bh_rej)}")

# Summary table
import pandas as pd
results = pd.DataFrame({
    'Test': range(1, len(p_values) + 1),
    'Raw_p': p_values,
    'Bonferroni_adj': bonf_adj,
    'Holm_adj': holm_adj,
    'Sidak_adj': sidak_adj,
    'BH_adj': bh_adj
})
print("\n" + "=" * 50)
print(results.to_string(index=False))

# --- Simulation ---
np.random.seed(42)
m = 20
n_true = 5
n_null = m - n_true

# Generate p-values
p_true = np.array([stats.ttest_1samp(np.random.normal(0.8, 1, 30), 0).pvalue 
                   for _ in range(n_true)])
p_null = np.random.uniform(0, 1, n_null)
pvals = np.concatenate([p_true, p_null])
is_null = np.array([False] * n_true + [True] * n_null)

# Shuffle
shuffle_idx = np.random.permutation(m)
pvals = pvals[shuffle_idx]
is_null = is_null[shuffle_idx]

bonf_adj, bonf_rej = bonferroni_correction(pvals)
holm_adj, holm_rej = holm_bonferroni(pvals)
bh_adj = false_discovery_control(pvals, method="bh")
bh_rej = bh_adj < 0.05

print("\n" + "=" * 50)
print("SIMULATION RESULTS (m=20, 5 true effects)")
print("=" * 50)
print(f"Bonferroni rejections: {bonf_rej.sum()} | False positives: {(bonf_rej & is_null).sum()}")
print(f"Holm rejections:       {holm_rej.sum()} | False positives: {(holm_rej & is_null).sum()}")
print(f"BH (FDR) rejections:   {bh_rej.sum()} | False positives: {(bh_rej & is_null).sum()}")
```

---

## 9. Common Pitfalls & Best Practices

### 9.1 Pitfall 1: Ignoring Multiple Comparisons

**The most serious pitfall** is ignoring the multiple comparisons problem entirely. This leads to inflated false positive rates and unreliable conclusions.

> **Example**: The "dead salmon" fMRI study showed that without correction, even a dead salmon's brain appeared to have "significant" neural activity when enough voxels were tested.

### 9.2 Pitfall 2: Overcorrecting

Applying overly conservative corrections (like Bonferroni when Holm or FDR would suffice) reduces power and may cause you to miss real effects.

### 9.3 Pitfall 3: Post-Hoc Family Definition

Defining the "family" of tests **after** seeing the results invalidates the correction. Always pre-specify which tests belong to the family.

### 9.4 Pitfall 4: Ignoring Dependence Structure

When tests are strongly positively correlated (e.g., testing the same hypothesis in overlapping subsamples), standard corrections become overly conservative. Consider permutation-based methods.

### 9.5 Best Practices

1. **Pre-specify your analysis plan**: Define which tests you'll conduct before seeing the data.
2. **Match correction to research phase**: Use FWER for confirmatory, FDR for exploratory.
3. **Report the correction method used**: Always state which correction you applied.
4. **Report both raw and adjusted p-values**: Allows readers to apply their own standards.
5. **Consider the dependence structure**: Use Holm for arbitrary dependence; Hochberg for independence/positive dependence.
6. **Focus on effect sizes**: A barely significant corrected p-value with a tiny effect size isn't very informative.
7. **Use Holm over Bonferroni**: Holm is uniformly more powerful with no additional assumptions.

---

## 10. References

1. **Holm, S.** (1979). A simple sequentially rejective multiple test procedure. *Scandinavian Journal of Statistics*, 6(2), 65–70.

2. **Hochberg, Y.** (1988). A sharper Bonferroni procedure for multiple tests of significance. *Biometrika*, 75(4), 800–802.

3. **Hommel, G.** (1988). A stagewise rejective multiple test procedure based on a modified Bonferroni test. *Biometrika*, 75(2), 383–386.

4. **Benjamini, Y. & Hochberg, Y.** (1995). Controlling the false discovery rate: a practical and powerful approach to multiple testing. *Journal of the Royal Statistical Society: Series B*, 57(1), 289–300.

5. **Bretz, F., et al.** (2009). Graphical approaches for multiple comparison procedures. *Statistics in Medicine*, 28(4), 586–604.

6. **Dmitrienko, A. & D'Agostino, R.** (2013). Traditional multiplicity adjustment methods in clinical trials. *Statistics in Medicine*, 32(29), 5172–5188.

7. **FDA Guidance for Industry** (2017). *Multiple Endpoints in Clinical Trials*.

8. **Maurer, W., et al.** (2020). Graphical approaches for the control of generalized error rates. *Statistics in Medicine*, 39(23), 3135–3155.

9. **Zlaoui, K.** (2021). Multiple Testing — How Can You Adjust? *Medium/Data Science*.

10. **Multiple hypothesis testing in allergy and hypersensitivity diseases investigation** (2025). *Pedagogical perspective on FWER/FDR methods*.

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────────┐
│                    FWER CONTROL QUICK REFERENCE                  │
├─────────────────────────────────────────────────────────────────┤
│ BONFERRONI:  Reject if p ≤ α/m                                 │
│              Pros: Simple, no assumptions                         │
│              Cons: Very conservative                              │
├─────────────────────────────────────────────────────────────────┤
│ HOLM:        Order p-values, step-down                          │
│              Reject p(i) if p(i) ≤ α/(m-i+1)                    │
│              Pros: Uniformly more powerful than Bonferroni        │
│              Cons: None (use this as default!)                    │
├─────────────────────────────────────────────────────────────────┤
│ HOCHBERG:    Order p-values, step-up                            │
│              Reject all p(i) ≤ α/(m-i+1) up to max i            │
│              Pros: More powerful than Holm                        │
│              Cons: Requires independence/positive dependence      │
├─────────────────────────────────────────────────────────────────┤
│ ŠIDÁK:       Reject if p ≤ 1-(1-α)^(1/m)                        │
│              Pros: Slightly less conservative than Bonferroni     │
│              Cons: Requires independence                          │
├─────────────────────────────────────────────────────────────────┤
│ PERMUTATION: Resample to estimate null distribution             │
│              Pros: Accounts for actual dependence                 │
│              Cons: Computationally intensive                      │
└─────────────────────────────────────────────────────────────────┘

RULE OF THUMB: Use Holm-Bonferroni as your default FWER method.
              Use Hochberg only when you can verify independence.
              Use FDR (BH) for exploratory/high-dimensional data.
```

---

*This guide was prepared for DoE Lecture 8: Multiple Testing with FWER. For questions or corrections, please refer to the cited literature.*
