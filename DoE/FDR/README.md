> **Course**: Design of Experiments (DoE)  
> **Lecture**: 9 — Multiple Testing with False Discovery Rate (FDR)  
> **Topics**: Multiple Comparisons Problem, FWER vs. FDR, Benjamini-Hochberg Procedure, Benjamini-Yekutieli Procedure, Storey q-values, Practical Applications, Case Studies

---

## Table of Contents

- [Table of Contents](#table-of-contents)
- [1. Overview](#1-overview)
- [2. The Multiple Testing Problem](#2-the-multiple-testing-problem)
- [3. Conceptual Explanation](#3-conceptual-explanation)
  - [3.1 Family-Wise Error Rate (FWER)](#31-family-wise-error-rate-fwer)
  - [3.2 False Discovery Rate (FDR)](#32-false-discovery-rate-fdr)
  - [3.3 FDR vs. FWER: When to Use Which?](#33-fdr-vs-fwer-when-to-use-which)
- [4. Mathematical Formulation](#4-mathematical-formulation)
  - [4.1 The 2x2 Contingency Table](#41-the-2x2-contingency-table)
  - [4.2 False Discovery Proportion (FDP)](#42-false-discovery-proportion-fdp)
  - [4.3 Definition of FDR](#43-definition-of-fdr)
- [5. FDR Control Procedures](#5-fdr-control-procedures)
  - [5.1 Benjamini-Hochberg (BH) Procedure](#51-benjamini-hochberg-bh-procedure)
    - [Algorithm](#algorithm)
    - [Theoretical Guarantee](#theoretical-guarantee)
    - [Adjusted p-values](#adjusted-p-values)
  - [5.2 Benjamini-Yekutieli (BY) Procedure](#52-benjamini-yekutieli-by-procedure)
    - [Algorithm](#algorithm-1)
  - [5.3 Storey's q-value Procedure](#53-storeys-q-value-procedure)
    - [Key Idea](#key-idea)
    - [q-value Definition](#q-value-definition)
- [6. Step-by-Step Application Guide](#6-step-by-step-application-guide)
  - [6.1 Worked Example: BH Procedure](#61-worked-example-bh-procedure)
    - [Step 1: Collect p-values](#step-1-collect-p-values)
    - [Step 2: Sort and rank p-values](#step-2-sort-and-rank-p-values)
    - [Step 3: Calculate BH critical values](#step-3-calculate-bh-critical-values)
    - [Step 4: Interpretation](#step-4-interpretation)
  - [6.2 Computing Adjusted p-values](#62-computing-adjusted-p-values)
- [7. Case Studies](#7-case-studies)
  - [7.1 Case Study 1: Gene Expression Microarray Analysis](#71-case-study-1-gene-expression-microarray-analysis)
  - [7.2 Case Study 2: A/B Testing in Online Experiments](#72-case-study-2-ab-testing-in-online-experiments)
  - [7.3 Case Study 3: Proteomics Differential Expression](#73-case-study-3-proteomics-differential-expression)
- [8. Practical Implementation](#8-practical-implementation)
  - [8.1 R Code Examples](#81-r-code-examples)
    - [Basic BH Procedure](#basic-bh-procedure)
    - [Storey's q-value](#storeys-q-value)
    - [Comparing Methods](#comparing-methods)
  - [8.2 Python Code Examples](#82-python-code-examples)
    - [Using SciPy and Statsmodels](#using-scipy-and-statsmodels)
    - [Manual BH Implementation](#manual-bh-implementation)
- [9. Best Practices and Common Pitfalls](#9-best-practices-and-common-pitfalls)
  - [Best Practices](#best-practices)
  - [Common Pitfalls](#common-pitfalls)
- [10. References and Further Reading](#10-references-and-further-reading)
  - [Foundational Papers](#foundational-papers)
  - [Tutorials and Reviews](#tutorials-and-reviews)
  - [Software and Tools](#software-and-tools)
- [Appendix: Quick Reference Card](#appendix-quick-reference-card)

---

## 1. Overview

Modern experimental design often involves testing hundreds or thousands of hypotheses simultaneously. Whether analyzing gene expression levels across the entire genome, evaluating multiple variants in an A/B test, or screening thousands of compounds in a drug discovery pipeline, the **multiple testing problem** is unavoidable.

This lecture covers the modern approach to multiple testing correction based on controlling the **False Discovery Rate (FDR)** — a paradigm shift from classical Family-Wise Error Rate (FWER) control that offers substantially greater statistical power while maintaining interpretable error control.

> **Key Insight**: FDR-controlling procedures provide less stringent control of Type I errors compared to FWER methods (e.g., Bonferroni), but offer greater power at the cost of allowing a controlled proportion of false positives. This makes FDR ideal for exploratory analyses and high-throughput experiments.

---

## 2. The Multiple Testing Problem

When conducting a single hypothesis test at significance level alpha = 0.05, the probability of a false positive (Type I error) is 5%. However, when conducting *m* independent tests simultaneously, the probability of making **at least one** false positive increases dramatically:

```
P(at least one false positive) = 1 - (1 - alpha)^m
```

| Number of Tests (m) | P(at least one FP) at alpha = 0.05 |
|---------------------|--------------------------------|
| 1                   | 5.0%                           |
| 10                  | 40.1%                          |
| 100                 | 99.4%                          |
| 1,000               | ~100%                          |
| 10,000              | ~100%                          |

**The classic illustration** (Tukey, 1991): If you examine 500 comparisons and suspect significance at 5% individually, detecting 24 significant hypotheses tells you essentially nothing — because 25 (5% of 500) were expected by pure chance alone.

This is the core of the multiple testing problem: without correction, the more tests you run, the more false discoveries you accumulate purely by chance.

---

## 3. Conceptual Explanation

### 3.1 Family-Wise Error Rate (FWER)

The **Family-Wise Error Rate** is the probability of making **one or more** false discoveries among all tests conducted:

```
FWER = P(V >= 1)
```

Where *V* is the number of false positives. Classical methods like the **Bonferroni correction** control FWER by adjusting the significance threshold:

```
alpha_adjusted = alpha / m
```

**Limitation**: FWER control is extremely conservative when *m* is large. In genomics experiments with m = 20,000 genes, the Bonferroni threshold becomes 0.0000025 — essentially eliminating all but the most extreme signals and severely reducing statistical power.

### 3.2 False Discovery Rate (FDR)

The **False Discovery Rate**, introduced by Benjamini and Hochberg (1995), takes a fundamentally different approach. Instead of controlling the probability of *any* false positive, FDR controls the **expected proportion of false discoveries among all rejected hypotheses**:

```
FDR = E[V / max(R, 1)]
```

Where:
- **V** = number of false positives (false discoveries)
- **R** = total number of rejected null hypotheses (total discoveries)
- **max(R, 1)** ensures the denominator is never zero

**Intuition**: If you control FDR at 5% and identify 100 significant results, you expect approximately 5 of them to be false positives. This is a much more practical guarantee than FWER when testing thousands of hypotheses.

### 3.3 FDR vs. FWER: When to Use Which?

| Criterion | FWER (e.g., Bonferroni) | FDR (e.g., BH) |
|-----------|------------------------|----------------|
| **Error controlled** | Probability of >=1 false positive | Expected proportion of false positives among rejections |
| **Stringency** | Very strict | Moderate |
| **Statistical Power** | Low (many false negatives) | High (more true discoveries) |
| **Best for** | Confirmatory studies, clinical trials, high-stakes decisions | Exploratory analyses, genomics, screening, hypothesis generation |
| **When to use** | Any false positive is catastrophic | Follow-up experiments are feasible; can tolerate some false positives |
| **Typical alpha** | 0.05 | 0.05-0.20 |

> **Rule of Thumb**: Use FWER when you need to be virtually certain that every declared significant result is real. Use FDR when you are in a discovery phase and can validate findings in follow-up experiments.

---

## 4. Mathematical Formulation

### 4.1 The 2x2 Contingency Table

In multiple hypothesis testing, the outcomes can be summarized as:

|                    | Declared Non-Significant | Declared Significant | Total |
|--------------------|--------------------------|----------------------|-------|
| **Null True**      | U (True Negatives)       | V (False Positives)  | m0    |
| **Alternative True**| T (False Negatives)      | S (True Positives)   | m1    |
| **Total**          | m - R                    | R                    | m     |

Where:
- **m** = total number of hypotheses tested
- **m0** = number of true null hypotheses (unknown)
- **m1** = number of true alternative hypotheses (unknown)
- **V** = false positives (Type I errors)
- **S** = true positives
- **R = V + S** = total number of rejections

### 4.2 False Discovery Proportion (FDP)

The **False Discovery Proportion** is the unobserved random variable representing the actual proportion of false discoveries:

```
FDP = V / max(R, 1)
```

- If R = 0 (no rejections), FDP = 0 by convention
- FDP is a random variable that depends on the data
- We cannot observe V directly (we don't know which nulls are truly true)

### 4.3 Definition of FDR

The **False Discovery Rate** is the expectation of the FDP:

```
FDR = E[FDP] = E[V / max(R, 1)]
```

An alternative definition, the **positive FDR (pFDR)**, conditions on having made at least one rejection:

```
pFDR = E[V / R | R > 0]
```

The pFDR was introduced by Storey (2003) and has a natural Bayesian interpretation. When the number of tests is large and the probability of at least one rejection is high, FDR ~ pFDR.

---

## 5. FDR Control Procedures

### 5.1 Benjamini-Hochberg (BH) Procedure

The **Benjamini-Hochberg (1995)** procedure is the most widely used FDR-controlling method. It is a step-up procedure that compares ordered p-values to a linear threshold.

#### Algorithm

Given *m* p-values p_1, p_2, ..., p_m and desired FDR level alpha (or Q):

1. **Sort** the p-values in ascending order: p_(1) <= p_(2) <= ... <= p_(m)
2. **Find** the largest index *k* such that:
   ```
   p_(k) <= (k / m) * alpha
   ```
3. **Reject** all null hypotheses H_(1), H_(2), ..., H_(k)

Equivalently, the BH threshold is:
```
T_BH = max{p_(i) : p_(i) <= (i / m) * alpha}
```

#### Theoretical Guarantee

Under the assumption that the test statistics are **independent** (or exhibit positive regression dependency), the BH procedure guarantees:

```
FDR <= (m0 / m) * alpha <= alpha
```

Where m0 is the number of true null hypotheses. Since m0 <= m, the FDR is conservatively controlled at level alpha.

#### Adjusted p-values

The BH-adjusted p-value for the *i*-th ordered test is:

```
p_adjusted(i) = min_{j >= i} { min(1, (m / j) * p_(j)) }
```

This ensures monotonicity: p_adjusted(1) <= p_adjusted(2) <= ... <= p_adjusted(m).

### 5.2 Benjamini-Yekutieli (BY) Procedure

The **Benjamini-Yekutieli (2001)** procedure extends FDR control to **arbitrary dependence structures**, including negative correlations.

#### Algorithm

The BY procedure modifies the BH threshold by a correction factor c(m):

```
p_(k) <= (k / (m * c(m))) * alpha
```

Where:
- If tests are independent or positively correlated: **c(m) = 1** (reduces to BH)
- Under arbitrary dependence: **c(m) = sum_{i=1}^m (1/i) ~ ln(m) + gamma + 1/(2m)**
  - gamma ~ 0.57721 (Euler-Mascheroni constant)

**Trade-off**: The BY procedure is more conservative than BH, especially when m is large, because c(m) grows logarithmically with m. However, it provides a formal FDR guarantee under any dependence structure.

### 5.3 Storey's q-value Procedure

Storey (2002, 2003) introduced an alternative approach that estimates the **proportion of true null hypotheses** (pi0 = m0/m) to improve power.

#### Key Idea

The BH procedure assumes pi0 ~ 1 (most hypotheses are null), which is conservative. Storey's method estimates pi0 from the p-value distribution:

```
pi0_hat(lambda) = #{p_i > lambda} / (m * (1 - lambda))
```

Where lambda is a tuning parameter (typically lambda = 0.5). The intuition is that under the null, p-values are uniformly distributed on [0,1], so the flat region of the p-value histogram estimates pi0.

#### q-value Definition

The **q-value** is the pFDR analog of the p-value:

```
q(p) = inf_{gamma >= p} { pFDR(gamma) } = inf_{gamma >= p} { (pi0 * gamma) / P_hat(P <= gamma) }
```

Where P_hat(P <= gamma) is the empirical cumulative distribution of p-values.

**Interpretation**: The q-value for a feature is the minimum FDR that can be attained when calling that feature significant. If you select all features with q <= 0.05, you expect 5% of them to be false positives.

**Advantage over BH**: By estimating pi0 < 1, Storey's procedure can be substantially more powerful than BH. Storey showed examples where power increased by over **8x** compared to BH.

---

## 6. Step-by-Step Application Guide

### 6.1 Worked Example: BH Procedure

**Scenario**: A researcher tests 20 different dietary variables for association with heart disease. The desired FDR is Q = 20%.

#### Step 1: Collect p-values

| Variable | Raw p-value |
|----------|-------------|
| Var 1    | 0.001       |
| Var 2    | 0.008       |
| Var 3    | 0.015       |
| Var 4    | 0.020       |
| Var 5    | 0.025       |
| Var 6    | 0.028       |
| Var 7    | 0.031       |
| Var 8    | 0.033       |
| Var 9    | 0.035       |
| Var 10   | 0.036       |
| Var 11   | 0.039       |
| Var 12   | 0.040       |
| Var 13   | 0.042       |
| Var 14   | 0.044       |
| Var 15   | 0.046       |
| Var 16   | 0.048       |
| Var 17   | 0.050       |
| Var 18   | 0.055       |
| Var 19   | 0.060       |
| Var 20   | 0.070       |

#### Step 2: Sort and rank p-values

Already sorted above. Rank *i* goes from 1 to 20.

#### Step 3: Calculate BH critical values

Formula: **Critical Value = (i / m) * Q = (i / 20) * 0.20**

| Rank (i) | p-value | BH Critical Value | Significant? |
|----------|---------|-------------------|--------------|
| 1        | 0.001   | 0.010             | Yes (0.001 < 0.010) |
| 2        | 0.008   | 0.020             | Yes (0.008 < 0.020) |
| 3        | 0.015   | 0.030             | Yes (0.015 < 0.030) |
| 4        | 0.020   | 0.040             | Yes (0.020 < 0.040) |
| 5        | 0.025   | 0.050             | Yes (0.025 < 0.050) |
| 6        | 0.028   | 0.060             | Yes (0.028 < 0.060) |
| 7        | 0.031   | 0.070             | Yes (0.031 < 0.070) |
| 8        | 0.033   | 0.080             | Yes (0.033 < 0.080) |
| 9        | 0.035   | 0.090             | Yes (0.035 < 0.090) |
| 10       | 0.036   | 0.100             | Yes (0.036 < 0.100) |
| 11       | 0.039   | 0.110             | Yes (0.039 < 0.110) |
| 12       | 0.040   | 0.120             | Yes (0.040 < 0.120) |
| 13       | 0.042   | 0.130             | Yes (0.042 < 0.130) |
| 14       | 0.044   | 0.140             | Yes (0.044 < 0.140) |
| 15       | 0.046   | 0.150             | Yes (0.046 < 0.150) |
| 16       | 0.048   | 0.160             | Yes (0.048 < 0.160) |
| 17       | 0.050   | 0.170             | Yes (0.050 < 0.170) |
| 18       | 0.055   | 0.180             | Yes (0.055 < 0.180) |
| 19       | 0.060   | 0.190             | Yes (0.060 < 0.190) |
| 20       | 0.070   | 0.200             | Yes (0.070 < 0.200) |

In this example, all p-values are below their critical values at Q = 20%. Let's consider a more realistic scenario where the threshold matters:

**Revised Example** (more realistic with some non-significant results):

| Rank (i) | p-value | BH Critical (Q=20%) | Significant? |
|----------|---------|---------------------|--------------|
| 1        | 0.001   | 0.010               | Yes |
| 2        | 0.008   | 0.020               | Yes |
| 3        | 0.015   | 0.030               | Yes |
| 4        | 0.039   | 0.040               | Yes |
| 5        | 0.041   | 0.050               | Yes |
| 6        | 0.042   | 0.060               | Yes |
| 7        | 0.044   | 0.070               | Yes |
| 8        | 0.046   | 0.080               | Yes |
| 9        | 0.048   | 0.090               | Yes |
| 10       | 0.050   | 0.100               | Yes |
| 11       | 0.055   | 0.110               | Yes |
| 12       | 0.150   | 0.120               | **No** (0.150 > 0.120) |
| 13       | 0.160   | 0.130               | No |
| 14       | 0.170   | 0.140               | No |
| 15       | 0.180   | 0.150               | No |
| 16       | 0.190   | 0.160               | No |
| 17       | 0.200   | 0.170               | No |
| 18       | 0.250   | 0.180               | No |
| 19       | 0.300   | 0.190               | No |
| 20       | 0.500   | 0.200               | No |

- **Largest k where p_(k) <= critical value**: k = 11 (p = 0.055 <= 0.110)
- **k = 12**: p = 0.150 > 0.120 -> STOP

**Result**: Reject null hypotheses for Variables 1 through 11. Even though some variables with smaller ranks might not individually pass their critical values, because they have smaller p-values than Variable 11, they are also declared significant.

#### Step 4: Interpretation

With Q = 20%, we declare 11 variables significant. We expect approximately 20% of these (about 2 variables) to be false discoveries. This is a much more powerful result than Bonferroni, which at alpha = 0.05 would use a threshold of 0.0025 and likely find only 1-2 significant variables.

### 6.2 Computing Adjusted p-values

The BH-adjusted p-value formula ensures monotonicity:

```
p_adjusted(i) = min_{j >= i} { min(1, (m / j) * p_(j)) }
```

**Example calculation** for m = 20:

For the 11th ordered p-value (p_(11) = 0.055):
```
p_adjusted(11) = min(1, (20/11)*0.055, (20/12)*0.150, ...)
               = min(1, 0.100, 0.250, ...)
               = 0.100
```

If p_adjusted <= Q, the test is significant.

---

## 7. Case Studies

### 7.1 Case Study 1: Gene Expression Microarray Analysis

**Context**: A microarray experiment compares gene expression levels between treatment and control groups across m = 6,356 genes (Apo AI experiment, Callow et al., 2000).

**Challenge**: Testing 6,356 genes simultaneously. At alpha = 0.05, we expect ~318 false positives by chance alone.

**Approach**:
1. Compute a t-test or Wilcoxon rank-sum test for each gene
2. Obtain 6,356 raw p-values
3. Apply BH procedure at FDR = 5%
4. Compare with Bonferroni correction

**Results**:
- **Bonferroni threshold**: 0.05 / 6,356 ~ 7.86 x 10^-6
  - Very few genes significant; extremely conservative
- **BH procedure (FDR = 5%)**: 
  - Identifies a larger set of differentially expressed genes
  - Expected ~5% of identified genes to be false positives
  - Allows researchers to prioritize candidates for validation

**Key Insight**: In genomics, the goal is often to generate a candidate list for follow-up experiments (qPCR, Western blot). FDR control is ideal because follow-up experiments will filter out false positives. FWER control would miss many true biological signals.

**Practical Consideration**: When sample sizes are small (e.g., n1 = n2 = 8), even BH may have low power. Filtering genes by variance or expression level before testing can improve power by reducing m.

### 7.2 Case Study 2: A/B Testing in Online Experiments

**Context**: A tech company runs 20 simultaneous A/B tests on website features (e.g., button colors, page layouts, recommendation algorithms). Each test measures click-through rate (CTR).

**Challenge**: Running 20 tests at alpha = 0.05 yields a 64% chance of at least one false positive. Implementing a feature based on a false positive wastes engineering resources.

**Approach**:
1. Compute p-value for each A/B test
2. Apply BH correction at Q = 10% or Q = 20%
3. Implement only features with q <= Q

**Decision Framework**:

| Scenario | Recommended Method | Rationale |
|----------|-------------------|-----------|
| Exploratory phase, many ideas | BH at Q = 20% | Maximize discovery; validate winners |
| High-stakes feature launch | BH at Q = 5% or BY | More stringent; costly to ship bad features |
| Single critical metric | Bonferroni | Only one decision; false positive is costly |

**Example**: Microsoft and other tech companies routinely apply BH correction when evaluating website changes. A 10% FDR means that if 10 features are shipped, 1 is expected to be a false positive — an acceptable trade-off when follow-up monitoring can detect underperforming features post-launch.

### 7.3 Case Study 3: Proteomics Differential Expression

**Context**: A proteomics study quantifies thousands of proteins across disease and healthy samples to identify biomarkers.

**Challenge**: High-throughput mass spectrometry generates protein-level p-values for thousands of proteins. Multiple testing correction is essential but must balance sensitivity (finding true biomarkers) and specificity (avoiding false leads).

**Method Comparison**:

| Method | Controls | Best Use | Limitation |
|--------|----------|----------|------------|
| Bonferroni | FWER | Small confirmatory panels | Severe power loss at scale |
| Holm | FWER | Strict FWER with more power | Still conservative |
| Benjamini-Hochberg | FDR | **Default for discovery proteomics** | Assumes independence/positive dependence |
| Benjamini-Yekutieli | FDR | Arbitrary dependence | More conservative than BH |

**Best Practices**:
1. Apply BH across the **complete set** of tested proteins
2. Do **not** filter by raw p-values before correction (cherry-picking invalidates FDR control)
3. Report **adjusted p-values together with effect sizes** (fold change)
4. Consider biological interpretability alongside statistical significance

**Important Distinction**: In proteomics, there are two levels of FDR:
- **Identification-level FDR**: Controls errors in peptide/protein identification from spectra
- **Differential expression FDR**: Controls false positives in testing protein abundance changes

These address different error sources and should both be applied but not confused.

---

## 8. Practical Implementation

### 8.1 R Code Examples

#### Basic BH Procedure

```r
# Raw p-values from 20 tests
p_values <- c(0.001, 0.008, 0.015, 0.020, 0.025, 0.028, 0.031, 
              0.033, 0.035, 0.036, 0.039, 0.040, 0.042, 0.044,
              0.046, 0.048, 0.050, 0.055, 0.060, 0.070)

# Benjamini-Hochberg adjusted p-values
p_adjusted_bh <- p.adjust(p_values, method = "fdr")

# Results
data.frame(
  raw_p = p_values,
  adj_p = p_adjusted_bh,
  significant = p_adjusted_bh < 0.20
)
```

#### Storey's q-value

```r
# Install qvalue package if needed
# BiocManager::install("qvalue")
library(qvalue)

# Compute q-values
qobj <- qvalue(p = p_values, fdr.level = 0.05)

# Results
summary(qobj)
plot(qobj)

# Extract significant results
significant_genes <- which(qobj$qvalues < 0.05)
```

#### Comparing Methods

```r
# Multiple correction methods
methods <- c("bonferroni", "holm", "hochberg", "fdr", "BY")

results <- sapply(methods, function(m) p.adjust(p_values, method = m))
colnames(results) <- methods

print(round(results, 4))
```

### 8.2 Python Code Examples

#### Using SciPy and Statsmodels

```python
import numpy as np
from scipy import stats
import statsmodels.stats.multitest as smm

# Raw p-values
p_values = np.array([0.001, 0.008, 0.015, 0.020, 0.025, 0.028, 0.031,
                     0.033, 0.035, 0.036, 0.039, 0.040, 0.042, 0.044,
                     0.046, 0.048, 0.050, 0.055, 0.060, 0.070])

# Benjamini-Hochberg
reject_bh, p_adjusted_bh, _, _ = smm.multipletests(
    p_values, alpha=0.20, method='fdr_bh'
)

# Bonferroni (for comparison)
reject_bonf, p_adjusted_bonf, _, _ = smm.multipletests(
    p_values, alpha=0.05, method='bonferroni'
)

# Benjamini-Yekutieli
reject_by, p_adjusted_by, _, _ = smm.multipletests(
    p_values, alpha=0.20, method='fdr_by'
)

# Results summary
import pandas as pd
results = pd.DataFrame({
    'raw_p': p_values,
    'BH_adjusted': p_adjusted_bh,
    'BH_reject': reject_bh,
    'Bonferroni_adjusted': p_adjusted_bonf,
    'Bonferroni_reject': reject_bonf,
    'BY_adjusted': p_adjusted_by,
    'BY_reject': reject_by
})

print(results)
```

#### Manual BH Implementation

```python
def benjamini_hochberg(p_values, alpha=0.05):
    """
    Manual implementation of the Benjamini-Hochberg procedure.
    """
    p_values = np.asarray(p_values)
    m = len(p_values)
    
    # Sort p-values and keep track of original indices
    order = np.argsort(p_values)
    p_sorted = p_values[order]
    
    # Find largest k where p(k) <= (k/m) * alpha
    thresholds = np.arange(1, m + 1) / m * alpha
    below_threshold = p_sorted <= thresholds
    
    if np.any(below_threshold):
        k_max = np.max(np.where(below_threshold)[0]) + 1
        reject_sorted = np.arange(m) < k_max
    else:
        reject_sorted = np.zeros(m, dtype=bool)
    
    # Map back to original order
    reject = np.empty(m, dtype=bool)
    reject[order] = reject_sorted
    
    # Compute adjusted p-values
    p_adjusted_sorted = np.minimum.accumulate(
        np.minimum(1, p_sorted * m / np.arange(1, m + 1))[::-1]
    )[::-1]
    
    p_adjusted = np.empty(m)
    p_adjusted[order] = p_adjusted_sorted
    
    return reject, p_adjusted

# Test
reject, p_adj = benjamini_hochberg(p_values, alpha=0.20)
print(f"Rejected: {np.sum(reject)} out of {len(p_values)}")
print(f"Adjusted p-values: {np.round(p_adj, 4)}")
```

---

## 9. Best Practices and Common Pitfalls

### Best Practices

1. **Define your testing universe before analysis**
   - Apply correction across the full set of hypotheses you intended to test
   - Do not add tests post-hoc and recorrect selectively

2. **Choose FDR level based on context**
   - Q = 5%: Standard for publication-quality results
   - Q = 10-20%: Acceptable for exploratory analyses with inexpensive follow-up
   - Q > 20%: Only when false positives are very cheap and true positives very valuable

3. **Report effect sizes alongside adjusted p-values**
   - Statistical significance != practical significance
   - A gene with q = 0.01 but fold change of 1.05 may not be biologically relevant

4. **Consider dependence structure**
   - If tests are strongly correlated (e.g., genes in the same pathway), BH is still generally valid under positive dependence
   - For arbitrary dependence, use BY or resampling-based methods

5. **Visualize your p-value distribution**
   - A histogram of p-values should show a flat region near 1.0 (null distribution)
   - A peak near 0 indicates true signals
   - Deviations from uniformity may indicate model misspecification

### Common Pitfalls

1. **Cherry-picking before correction**
   - Do not filter by raw p-values and then apply FDR correction to the subset
   - This invalidates the FDR guarantee

2. **Confusing FDR with per-test error probability**
   - A q-value of 0.05 does NOT mean a specific feature has a 5% chance of being false
   - It means 5% of the *rejected set* is expected to be false

3. **Using overly conservative methods by default**
   - Bonferroni is not appropriate for large-scale exploratory studies
   - It leads to massive power loss and missed discoveries

4. **Ignoring dependence**
   - While BH is robust to positive dependence, strong negative correlations can inflate FDR
   - Use BY or permutation-based methods when dependence is a concern

5. **Setting pi0 = 1 blindly in Storey's method**
   - If many hypotheses are truly alternative, forcing pi0 = 1 loses power
   - Let the data estimate pi0, but check that the p-value histogram looks reasonable

6. **Confusing identification FDR with differential expression FDR**
   - In proteomics/genomics, peptide identification and differential expression are separate steps
   - Each requires its own error control

---

## 10. References and Further Reading

### Foundational Papers

1. **Benjamini, Y., & Hochberg, Y. (1995)**. Controlling the false discovery rate: a practical and powerful approach to multiple testing. *Journal of the Royal Statistical Society: Series B*, 57(1), 289-300.
   - The original BH procedure paper.

2. **Benjamini, Y., & Yekutieli, D. (2001)**. The control of the false discovery rate in multiple testing under dependency. *Annals of Statistics*, 29(4), 1165-1188.
   - Extends FDR control to arbitrary dependence structures.

3. **Storey, J. D. (2002)**. A direct approach to false discovery rates. *Journal of the Royal Statistical Society: Series B*, 64(3), 479-498.
   - Introduces the pFDR and fixed rejection region approach.

4. **Storey, J. D. (2003)**. The positive false discovery rate: A Bayesian interpretation and the q-value. *Annals of Statistics*, 31(6), 2013-2035.
   - Formalizes the q-value and its Bayesian interpretation.

5. **Storey, J. D., & Tibshirani, R. (2003)**. Statistical significance for genomewide studies. *PNAS*, 100(16), 9440-9445.
   - Practical application of q-values to genomics.

### Tutorials and Reviews

6. **Noble, W. S. (2009)**. How does multiple testing correction work? *Nature Biotechnology*, 27(12), 1135-1137.
   - Excellent intuitive explanation with visual examples.

7. **Verhoeven, K. J. F., Simonsen, K. L., & McIntyre, L. M. (2005)**. Implementing false discovery rate control: increasing your power. *Oikos*, 108(3), 643-647.
   - Practical guide with simulation examples.

8. **Genovese, C. R. (2004)**. A Tutorial on False Discovery Control. Carnegie Mellon University.
   - Comprehensive mathematical tutorial.

### Software and Tools

- **R**: `p.adjust()` (base), `qvalue` package (Bioconductor)
- **Python**: `statsmodels.stats.multitest`, `scipy.stats`
- **Online Calculator**: MultipleTesting.com

---

## Appendix: Quick Reference Card

| Concept | Formula / Definition |
|---------|---------------------|
| **FWER** | P(V >= 1) |
| **FDR** | E[V / max(R, 1)] |
| **pFDR** | E[V/R | R > 0] |
| **BH Threshold** | max{p_(i) : p_(i) <= (i/m) * alpha} |
| **BH Adjusted p-value** | min_{j>=i} {min(1, (m/j) * p_(j))} |
| **BY Threshold** | max{p_(i) : p_(i) <= (i/(m*c(m))) * alpha} |
| **q-value** | inf_{gamma>=p} {pFDR(gamma)} |
| **pi0 estimate** | #{p_i > lambda} / (m(1-lambda)) |

---

*End of Lecture 9: Multiple Testing with FDR*