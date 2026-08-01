Welcome to the **Advanced Design of Experiments (DoE) & Linear Modeling Interactive Guide**. 

As a senior data scientist, I've designed this notebook to bridge the gap between statistical theory and practical Python implementation. We will move from the foundational linear algebra of ANOVA to advanced mixed-effects modeling, ensuring you understand not just *how* to run these tests, but *why* they work mathematically.

Let's begin by setting up our environment and generating our synthetic dataset.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.power import FTestAnovaPower
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multitest import multipletests
import pingouin as pg
import scikit_posthocs as sp

# Set random seed for reproducibility
np.random.seed(42)

# --- Synthetic Dataset Generation (Lecture Point 3) ---
# 4 groups (A, B, C, D), n=10 per group, N=40. 
# We add true mean differences so the ANOVA yields significant results.
n_per_group = 10
groups = ['A', 'B', 'C', 'D']
true_means = {'A': 0.0, 'B': 1.8, 'C': 2.0, 'D': 4.2} # Added signal to standard normal noise

data = []
for group in groups:
    # Standard normal noise (mean=0, std=1) added to the true group mean
    y = np.random.normal(loc=true_means[group], scale=1.0, size=n_per_group)
    for val in y:
        data.append({'Group': group, 'Value': val})

df = pd.DataFrame(data)
print("Dataset Preview:")
display(df.head(10))
print(f"\nTotal observations (N): {len(df)}")
```

---

## Section 1: ANOVA, Design Matrices & Linear Constraints

### The Theory: Rank Deficiency in ANOVA (Point 2)
In a standard one-way ANOVA, we model the response $Y_{ij}$ as:
$$Y_{ij} = \mu + \tau_i + \epsilon_{ij}$$
Where $\mu$ is the global mean, $\tau_i$ is the treatment effect for group $i$, and $\epsilon_{ij}$ is the error. 

If we have $k=4$ groups, we have 5 parameters to estimate ($\mu, \tau_A, \tau_B, \tau_C, \tau_D$). However, the design matrix $X$ for this model is **rank-deficient** (non-invertible). The columns for the group indicators sum exactly to the intercept column. Mathematically, $X^T X$ is singular, meaning we cannot compute $(X^T X)^{-1}$ to find the OLS estimates $\hat{\beta} = (X^T X)^{-1}X^T Y$.

**The Solution:** We must impose a **linear constraint** to make the matrix full rank. The two most common constraints are:
1. **Baseline (Treatment) Constraint:** $\tau_A = 0$
2. **Sum-to-Zero Constraint:** $\sum \tau_i = 0$

### Python Implementation: Building the Design Matrices
Let's see how `patsy` (the formula engine behind `statsmodels`) handles these constraints under the hood.

```python
import patsy

# 1. Baseline (Treatment) Contrast
# The first group alphabetically (A) becomes the baseline.
X_treatment = patsy.dmatrix("C(Group, Treatment)", df, return_type="dataframe")
print("--- Baseline (Treatment) Design Matrix ---")
display(X_treatment.head())

# 2. Sum-to-Zero Contrast
# The intercept represents the grand mean.
X_sum = patsy.dmatrix("C(Group, Sum)", df, return_type="dataframe")
print("\n--- Sum-to-Zero Design Matrix ---")
display(X_sum.head())
```
*Notice how in the Treatment matrix, Group A is all zeros (the baseline). In the Sum matrix, Group D is represented by -1s in the other columns, enforcing the rule that $\tau_D = -(\tau_A + \tau_B + \tau_C)$.*

---

## Section 2: Model Output Interpretation in Python

### The Theory: Global vs. Local Tests (Points 4, 5, 6, 7, 10)
- **ANOVA F-Test (Point 4):** Tests the *global* null hypothesis $H_0: \tau_A = \tau_B = \tau_C = \tau_D = 0$. A small p-value tells us *at least one* group differs, but not which one.
- **Linear Model Summary (Points 5, 6, 7):** Tests *local* hypotheses. The p-values depend entirely on your chosen contrast.
  - Under **Treatment coding**, it tests if Group $i$ differs from the Baseline (Group A).
  - Under **Sum coding**, it tests if Group $i$ differs from the *overall global mean* ($\bar{Y}$).

### Python Implementation: Fitting and Interpreting
```python
# Fit models using both contrast types
model_treat = smf.ols('Value ~ C(Group, Treatment)', data=df).fit()
model_sum = smf.ols('Value ~ C(Group, Sum)', data=df).fit()

# 1. Global ANOVA F-Test (Identical for both parameterizations)
print("="*50)
print("GLOBAL ANOVA F-TEST (Type II Sum of Squares)")
print("="*50)
anova_table = anova_lm(model_treat, typ=2)
display(anova_table)

# 2. Local Parameter Estimates (Treatment Coding)
print("\n" + "="*50)
print("LINEAR MODEL SUMMARY: BASELINE (TREATMENT) CODING")
print("="*50)
print(model_treat.summary().tables[1])

# 3. Local Parameter Estimates (Sum-to-Zero Coding)
print("\n" + "="*50)
print("LINEAR MODEL SUMMARY: SUM-TO-ZERO CODING")
print("="*50)
print(model_sum.summary().tables[1])
```
**Interpretation Check:** 
- In the *Treatment* summary, the p-value for `C(Group, Treatment)[D]` tests if D is different from A.
- In the *Sum* summary, the intercept is the grand mean (~2.0), and the p-value for `C(Group, Sum)[D]` tests if D's effect deviates from that grand mean.

---

## Section 3: Power Analysis & Sample Size Planning

### The Theory: Why Power Matters (Points 11, 12)
Before collecting data, we must ensure our sample size $N$ is large enough to detect a true effect. Statistical power ($1 - \beta$) is the probability of correctly rejecting a false null hypothesis. Underpowered studies waste resources and risk Type II errors (false negatives).

### Python Implementation: Calculating Required Sample Size
We use `statsmodels.stats.power.FTestAnovaPower`. We need to define:
- $\alpha$ (Significance level, usually 0.05)
- Power (usually 0.80)
- $k$ (Number of groups)
- Effect size (Cohen's $f$)

```python
# Calculate Cohen's f from our synthetic data's true means and pooled variance
grand_mean = df['Value'].mean()
variance_between = np.mean([(true_means[g] - grand_mean)**2 for g in groups])
variance_within = df.groupby('Group')['Value'].var().mean()
cohens_f = np.sqrt(variance_between / variance_within)

print(f"Estimated Cohen's f (Effect Size): {cohens_f:.3f}")

# Initialize Power Analysis
analysis = FTestAnovaPower()

# Calculate required sample size per group
n_required = analysis.solve_power(
    effect_size=cohens_f, 
    nobs=None,       # We want to find this
    alpha=0.05, 
    power=0.80, 
    k_groups=4
)

print(f"Required sample size PER GROUP for 80% power: {np.ceil(n_required)}")

# Plotting a Power Curve
ns = np.arange(5, 30, 1)
powers = [analysis.power(effect_size=cohens_f, nobs=n, alpha=0.05, k_groups=4) for n in ns]

plt.figure(figsize=(8, 5))
plt.plot(ns, powers, marker='o', linestyle='-', color='b')
plt.axhline(0.8, color='r', linestyle='--', label='Target Power (0.80)')
plt.axvline(np.ceil(n_required), color='g', linestyle='--', label=f'Required N={np.ceil(n_required)}')
plt.title('Power Curve for One-Way ANOVA')
plt.xlabel('Sample Size per Group (n)')
plt.ylabel('Statistical Power')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

---

## Section 4: Pairwise Multiple Comparisons

### The Theory: The Multiple Testing Problem (Points 1, 8, 13, 14, 15, 16, 17, 18)
If ANOVA is significant, we want to know *which* groups differ. For $k=4$ groups, we must run $k(k-1)/2 = 6$ pairwise t-tests (Point 13). 

**The Risk (Point 1 & 8):** If we run 6 tests at $\alpha=0.05$, the probability of at least one false positive (Family-Wise Error Rate, FWER) skyrockets. 
$$FWER = 1 - (1 - 0.05)^6 \approx 0.26$$

**Solution 1: Bonferroni Correction (Points 14, 15)**
Divide $\alpha$ by the number of tests ($k^* = 6$). New $\alpha = 0.05 / 6 = 0.0083$. 
*Proof:* Based on Boole’s inequality (Union Bound), $P(\cup A_i) \le \sum P(A_i)$. If each test is at $\alpha/k^*$, the sum is $\le \alpha$. It is mathematically sound but overly conservative (low power).

**Solution 2: Tukey’s HSD (Points 16, 17, 18)**
Uses the **Studentized Range Distribution**. It accounts for the correlation between pairwise comparisons in ANOVA. For equal sample sizes ($n_i = n_j$), it provides the *exact* FWER of $\alpha$ without being overly conservative. It also provides simultaneous confidence intervals.

### Python Implementation: Post-Hoc Testing
```python
# 1. Unadjusted P-values (Dangerous!)
# We can extract these from pairwise t-tests
unadjusted_p = []
for i in range(len(groups)):
    for j in range(i+1, len(groups)):
        t_stat, p_val = stats.ttest_ind(
            df[df['Group'] == groups[i]]['Value'], 
            df[df['Group'] == groups[j]]['Value']
        )
        unadjusted_p.append(p_val)

# 2. Bonferroni Correction (using statsmodels)
reject_bonf, pvals_bonf, _, _ = multipletests(unadjusted_p, alpha=0.05, method='bonferroni')

# 3. Tukey's HSD (using statsmodels)
tukey_results = pairwise_tukeyhsd(endog=df['Value'], groups=df['Group'], alpha=0.05)
print("="*50)
print("TUKEY'S HSD TEST RESULTS")
print("="*50)
print(tukey_results)

# 4. Alternative: Using scikit-posthocs and pingouin for visualization/verification
# pingouin for a quick pairwise T-test with Holm-Bonferroni (often preferred over strict Bonferroni)
pg_results = pg.pairwise_ttests(data=df, dv='Value', between='Group', padjust='holm')
print("\nPingouin Pairwise T-tests (Holm corrected):")
display(pg_results)

# scikit-posthocs for a visual heatmap of p-values
plt.figure(figsize=(6, 5))
sp.posthoc_tukey(df, val_col='Value', group_col='Group', plot_type='boxplot')
plt.title("Tukey HSD Group Differences (scikit-posthocs)")
plt.tight_layout()
plt.show()
```

---

## Section 5: Fixed vs. Random Effects (Mixed Models)

### The Theory: Variance Components (Points 19, 20)
- **Fixed Effects (Points 19):** We care about the specific levels of the factor (e.g., comparing Drug A, B, C, and D specifically). We estimate their specific means.
- **Random Effects:** The levels are a random sample from a larger population (e.g., testing 4 random "Batches" of a chemical, or 4 random "Subjects" in a repeated measures design). We don't care about the specific batch means; we want to estimate the **variance component** ($\sigma^2_{batch}$) to understand how much variability batches introduce.

### Python Implementation: Fitting a Mixed Model
Let's simulate a scenario where our 40 observations were collected across 5 different experimental "Days" (a random effect).

```python
# Add a random effect: 'Day' (5 days, 8 observations per day)
days = np.repeat(np.arange(1, 6), 8)
np.random.shuffle(days)
df['Day'] = days

# Add a random intercept for each day to simulate batch variance
day_effects = {d: np.random.normal(0, 0.8) for d in np.unique(days)}
df['Value'] = df['Value'] + df['Day'].map(day_effects)

print("Dataset with Random Effect (Day):")
display(df.head())

# Fit the Mixed Linear Model
# Fixed effect: Group
# Random effect: Day (grouping variable)
mixed_model = smf.mixedlm("Value ~ C(Group)", df, groups=df["Day"]).fit()

print("="*50)
print("MIXED EFFECTS MODEL SUMMARY")
print("="*50)
print(mixed_model.summary())

# Extracting Variance Components
print("\n--- Variance Components ---")
print(f"Random Effect Variance (Day): {mixed_model.cov_re.values[0,0]:.4f}")
print(f"Residual Variance (Error):    {mixed_model.scale:.4f}")
```
*Notice how the model separates the variance into the random effect of the "Day" and the residual error, giving us a much more accurate estimate of the fixed Group effects.*

---

## 🧠 Test Your Understanding (Self-Assessment)

Challenge yourself with these practical scenarios. Write your code or formulate your answers in the cells below!

### Challenge 1: Contrast Interpretation
You fit a model using Sum-to-Zero contrasts: `Value ~ C(Group, Sum)`. The output shows the intercept is `15.0` and the coefficient for `Group C` is `2.5` (p < 0.01). 
**Question:** What is the estimated mean of Group C? What does the p-value specifically tell you in this context?

### Challenge 2: Power Analysis Calculation
You are designing a new experiment with 3 groups. You expect a small effect size (Cohen's $f = 0.20$). You want 90% power at an $\alpha$ of 0.05. 
**Task:** Write the Python code using `FTestAnovaPower` to calculate the required sample size *per group*.

### Challenge 3: Multiple Comparisons Logic
You have an experiment with 6 groups. 
**Question A:** How many pairwise comparisons will you make? 
**Question B:** If you use a strict Bonferroni correction, what is your new adjusted alpha threshold? 
**Question C:** Why might you choose Tukey's HSD over Bonferroni in this specific scenario?

### Challenge 4: Mixed Models Conceptual
You are analyzing student test scores. You have data on the `Teaching_Method` (Method A, B, C) and the `School_ID` (50 different schools). 
**Question:** Which variable should be modeled as a Fixed Effect and which as a Random Effect? Write the `statsmodels.formula.api.mixedlm` formula string to fit this model.

---
*End of Guide. Happy Modeling!*

---

# Tukey's Honest Significant Difference (HSD) Test Explained

## Tukey's HSD Test: A Comprehensive Explanation

**Tukey's Honest Significant Difference (HSD) test** is a post-hoc multiple comparison procedure specifically designed for ANOVA that simultaneously compares all possible pairs of group means while rigorously controlling the family-wise error rate (FWER). Developed by John Tukey, this test leverages the **studentized range distribution** (q-distribution) to determine the minimum mean difference required between any two groups to be considered statistically significant at a given α level. Unlike simple pairwise t-tests that inflate Type I error probability with each additional comparison, Tukey's HSD maintains the FWER at exactly α when sample sizes are equal across groups (balanced design), and approximately α when sample sizes are unequal. The test computes a single "honest significant difference" value—the threshold that any pair of means must exceed to be declared significantly different—using the formula: HSD = qₐᵥₖ × √(MSE/n), where q is the studentized range statistic, MSE is the mean squared error from the ANOVA, and n is the sample size per group. This approach produces adjusted p-values and simultaneous confidence intervals for all pairwise differences, making it the gold standard for post-hoc analysis in experimental designs with multiple treatment groups.

## Key Differences Between ANOVA and Tukey's HSD Test

| Aspect | ANOVA (F-test) | Tukey's HSD Test |
|--------|----------------|------------------|
| **Primary Purpose** | Tests the **global null hypothesis** that ALL group means are equal (H₀: μ₁ = μ₂ = ... = μₖ) | Identifies **which specific pairs** of group means differ significantly from each other |
| **Type of Test** | **Omnibus test** - provides a single overall p-value for the entire model | **Post-hoc pairwise test** - provides separate results for each pair comparison |
| **Question Answered** | "Is there any evidence that at least one group differs from the others?" | "Which specific groups are different from each other?" |
| **Hypothesis Testing** | One global hypothesis test | Multiple (k(k-1)/2) pairwise hypothesis tests |
| **Multiple Comparison Control** | No multiple comparison issue (single test) | Explicitly controls family-wise error rate (FWER) at α level |
| **When to Use** | First step to determine if there are ANY differences among groups | Only if ANOVA is significant, to discover where the differences lie |
| **Output** | F-statistic, degrees of freedom, p-value | Mean differences, adjusted p-values, confidence intervals for each pair |
| **Interpretation** | Significant p-value indicates not all group means are equal | Identifies exactly which pairs have statistically different means |
| **Underlying Distribution** | F-distribution | Studentized range distribution (q-distribution) |
| **Statistical Power** | High power for detecting any difference | Lower power than ANOVA but provides specific pairwise information |
| **Assumptions** | Normality, homogeneity of variances, independence | Same as ANOVA (normality, homogeneity, independence) + balanced designs preferred |

## Practical Example in Context

```python
# Visual demonstration of ANOVA vs Tukey's HSD
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.anova import anova_lm

# Create example data with clear group differences
np.random.seed(42)
groups = ['Control', 'Treatment1', 'Treatment2', 'Treatment3']
means = [0, 2, 4, 6]  # Increasing treatment effects
n_per_group = 15

data = []
for group, mean in zip(groups, means):
    values = np.random.normal(mean, 1.5, n_per_group)
    for val in values:
        data.append({'Group': group, 'Value': val})

df_example = pd.DataFrame(data)

# Perform ANOVA
model = ols('Value ~ C(Group)', data=df_example).fit()
anova_result = anova_lm(model)

# Perform Tukey's HSD
tukey_result = pairwise_tukeyhsd(df_example['Value'], df_example['Group'], alpha=0.05)

# Visualization
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 1. Boxplot showing group distributions
sns.boxplot(data=df_example, x='Group', y='Value', ax=axes[0], palette='Set2')
axes[0].set_title('Group Distributions', fontsize=12, fontweight='bold')
axes[0].grid(True, alpha=0.3)

# 2. ANOVA result visualization
anova_text = f"ANOVA F-test:\nF-statistic = {anova_result['F'].iloc[0]:.2f}\np-value = {anova_result['PR(>F)'].iloc[0]:.4f}"
if anova_result['PR(>F)'].iloc[0] < 0.05:
    anova_text += "\n✓ Significant at α=0.05"
else:
    anova_text += "\n✗ Not significant at α=0.05"
axes[1].text(0.5, 0.5, anova_text, ha='center', va='center', fontsize=14, 
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
axes[1].set_title('ANOVA Results', fontsize=12, fontweight='bold')
axes[1].axis('off')

# 3. Tukey's HSD results visualization
tukey_df = pd.DataFrame({
    'Comparison': [f"{g1}-{g2}" for g1, g2 in zip(tukey_result._results_table.data[1:, 1], 
                                                   tukey_result._results_table.data[1:, 0])],
    'Mean_Diff': tukey_result.meandiffs,
    'Significant': tukey_result.reject
})

colors = ['red' if sig else 'blue' for sig in tukey_df['Significant']]
axes[2].barh(tukey_df['Comparison'], tukey_df['Mean_Diff'], color=colors, alpha=0.7)
axes[2].axvline(x=0, color='black', linestyle='-', alpha=0.5)
axes[2].set_xlabel('Mean Difference')
axes[2].set_title('Tukey HSD: Pairwise Differences\n(Red = Significant)', fontsize=12, fontweight='bold')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("ANOVA RESULTS")
print("="*60)
print(anova_result)

print("\n" + "="*60)
print("TUKEY'S HSD TEST RESULTS")
print("="*60)
print(tukey_result)
```

## When to Use Each Test

### Use ANOVA When:
1. You want to know if **any differences exist** among groups
2. You're conducting an **initial screening** of treatment effects
3. You have a **single categorical factor** with multiple levels
4. You need a **single p-value** to report the overall effect

### Use Tukey's HSD When:
1. ANOVA is **significant** and you need to know **which groups differ**
2. You want to **explore all possible pairwise comparisons** simultaneously
3. You need to control the **family-wise error rate** (FWER)
4. You want **confidence intervals** for all pairwise differences
5. You have **balanced designs** (equal sample sizes per group)

## Summary

The relationship between ANOVA and Tukey's HSD is complementary: **ANOVA tells you IF there's a difference somewhere, while Tukey's HSD tells you WHERE the differences are**. ANOVA serves as a gateway test that protects against conducting unnecessary multiple comparisons when no overall effect exists. When ANOVA is significant, Tukey's HSD provides the detailed pairwise analysis needed to fully understand the experimental results. Together, they form a powerful analytical framework that balances global hypothesis testing with detailed pairwise exploration, ensuring both statistical rigor and practical interpretability.