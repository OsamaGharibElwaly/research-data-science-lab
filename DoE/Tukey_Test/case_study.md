# Tukey's HSD Test: Theory and Interpretation Guide

## Complete Small Code Implementation (< 50 lines)

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.anova import anova_lm

# Generate synthetic data (4 groups, 15 each)
np.random.seed(42)
groups = ['Control', 'Low', 'Medium', 'High']
means = {'Control': 50, 'Low': 55, 'Medium': 60, 'High': 68}
data = []
for g in groups:
    for _ in range(15):
        data.append({'Group': g, 'Score': np.random.normal(means[g], 5)})
df = pd.DataFrame(data)

# ANOVA
model = ols('Score ~ C(Group)', data=df).fit()
anova = anova_lm(model)
print("ANOVA Results:")
print(anova)

# Tukey's HSD
tukey = pairwise_tukeyhsd(df['Score'], df['Group'], alpha=0.05)
print("\nTukey's HSD Results:")
print(tukey)

# Extract significant comparisons
sig = pd.DataFrame({
    'Comparison': [f"{g1}-{g2}" for g1, g2 in zip(tukey._results_table.data[1:, 1], 
                                                    tukey._results_table.data[1:, 0])],
    'Diff': tukey.meandiffs,
    'p_adj': tukey.pvalues,
    'Sig': tukey.reject
})
print("\nSignificant Differences:")
print(sig[sig['Sig'] == True])

# Visualization
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.bar(df.groupby('Group')['Score'].mean().index, 
        df.groupby('Group')['Score'].mean().values,
        yerr=df.groupby('Group')['Score'].std()/np.sqrt(15))
plt.title('Group Means ± SE')

plt.subplot(1,2,2)
plt.errorbar(range(len(sig)), sig['Diff'], 
             yerr=[sig['Diff']-tukey.conf_int[:,0], tukey.conf_int[:,1]-sig['Diff']],
             fmt='o')
plt.axhline(0, color='black', linestyle='--')
plt.title('Tukey HSD: Mean Differences with 95% CI')
plt.xticks(range(len(sig)), sig['Comparison'], rotation=45)
plt.tight_layout()
plt.show()
```

---

## Theoretical Explanation

### 1. The Multiple Comparison Problem

**Why we need Tukey's HSD:**

When we perform multiple t-tests after ANOVA, the probability of making at least one Type I error (false positive) increases dramatically.

| Number of Groups (k) | Pairwise Tests | FWER without correction | FWER with Tukey |
|---------------------|---------------|------------------------|-----------------|
| 3 | 3 | 14.3% | 5% |
| 4 | 6 | 26.5% | 5% |
| 5 | 10 | 40.1% | 5% |
| 6 | 15 | 53.7% | 5% |

**Formula:**
- FWER (uncorrected) = 1 - (1 - α)^m
- Where m = k(k-1)/2 pairwise comparisons

### 2. Tukey's HSD Formula

**The Honest Significant Difference (HSD):**

$$HSD = q_{\alpha, k, df} \times \sqrt{\frac{MSE}{n}}$$

**Components:**
- **q** = Studentized Range Statistic (critical value)
- **k** = Number of groups
- **df** = Error degrees of freedom (N - k)
- **MSE** = Mean Square Error from ANOVA
- **n** = Sample size per group

**Decision Rule:**
- If |mean difference| > HSD → **Significant**
- If |mean difference| ≤ HSD → **Not Significant**

### 3. Understanding the Output

| Column | What it Tells You | How to Interpret |
|--------|------------------|------------------|
| **Comparison** | Which groups are being compared | Group1 vs Group2 |
| **Diff** | Mean difference | Positive = first group higher |
| **Lower/Upper CI** | 95% Confidence Interval | If interval contains 0 → not significant |
| **p_adj** | Corrected p-value | If < 0.05 → significant |
| **Reject** | Statistical decision | True = significant difference |

### 4. Step-by-Step Interpretation

**Example Output:**
```
Comparison     Diff     Lower     Upper    p_adj   Reject
Low-Control    5.2      1.3       9.1      0.008    True
High-Control   18.3     14.4      22.2     0.000    True
High-Low       13.1     9.2       17.0     0.000    True
```

**How to read each row:**

**Row 1: Low vs Control (p_adj = 0.008)**
- ✓ Significant (p < 0.05)
- Low group is 5.2 points higher than Control
- 95% CI [1.3, 9.1] does NOT contain 0
- **Conclusion:** "Low treatment significantly outperforms Control"

**Row 2: High vs Control (p_adj = 0.000)**
- ✓ Significant (p < 0.001)
- High group is 18.3 points higher than Control
- 95% CI [14.4, 22.2] far from 0
- **Conclusion:** "Strong significant effect of High treatment"

**Row 3: High vs Low (p_adj = 0.000)**
- ✓ Significant (p < 0.001)
- High group is 13.1 points higher than Low
- **Conclusion:** "High treatment significantly outperforms Low"

### 5. Reporting Results

**Statistical Statement:**
> "A one-way ANOVA revealed a significant effect of treatment, F(3, 56) = 18.45, p < .001. Tukey's HSD post-hoc comparisons showed that all pairwise differences were significant (all p < .01). The High treatment produced the highest scores (M = 68.2), significantly outperforming Control (M = 49.8, diff = 18.4, p < .001), Low (M = 55.1, diff = 13.1, p < .001), and Medium (M = 60.3, diff = 7.9, p = .003)."

**Visual Summary:**
- Use plots with confidence intervals
- Use compact letter display (CLD) to show grouping
- Example: Control^a Low^ab Medium^bc High^c

### 6. Key Takeaways

1. **When to use:** Only after significant ANOVA
2. **What it does:** Controls family-wise error rate exactly
3. **Assumptions:** Equal variances, normality, independent samples
4. **Interpretation focus:** 
   - Check p_adj < 0.05
   - Check confidence interval excludes 0
   - Consider practical significance (effect size)

### 7. Quick Reference Table

| Value | Interpretation |
|-------|----------------|
| **p_adj < 0.05** | Significant difference |
| **p_adj > 0.05** | No significant difference |
| **CI excludes 0** | Significant difference |
| **CI includes 0** | No significant difference |
| **Large diff** | Strong practical effect |
| **Small diff** | Weak practical effect |

---

## Ready-to-Use Code for Your Own Data

```python
# Replace with your own data
def run_tukey_analysis(data, group_column, value_column):
    """
    data: DataFrame with group and value columns
    group_column: name of column containing group labels
    value_column: name of column containing measured values
    """
    
    # ANOVA
    model = ols(f'{value_column} ~ C({group_column})', data=data).fit()
    print("ANOVA:")
    print(anova_lm(model))
    
    # Tukey's HSD
    tukey = pairwise_tukeyhsd(data[value_column], data[group_column], alpha=0.05)
    print("\nTukey's HSD:")
    print(tukey)
    
    # Significant differences only
    sig_df = pd.DataFrame({
        'Comparison': [f"{g1} vs {g2}" for g1, g2 in zip(tukey._results_table.data[1:, 1], 
                                                           tukey._results_table.data[1:, 0])],
        'Difference': tukey.meandiffs,
        'p_adj': tukey.pvalues,
        'Significant': tukey.reject
    })
    return sig_df[sig_df['Significant'] == True]

# Example usage with your data:
# results = run_tukey_analysis(df, 'Group', 'Score')
# print(results)
```

This concise guide covers the essential theory and practical application of Tukey's HSD test in under 50 lines of code, with comprehensive explanations for interpretation and reporting.

---
### BEFORE THIS Prompt by one : 


# Comprehensive Guide to Tukey's HSD Test: Theory, Interpretation, and Case Study

## Table of Contents
1. Theoretical Foundations
2. Statistical Concepts and Formulas
3. Case Study: Fertilizer Effectiveness
4. Detailed Output Interpretation
5. Reporting Guidelines

---

## 1. Theoretical Foundations

### 1.1 Why Tukey's HSD?

When conducting multiple pairwise comparisons after ANOVA, the probability of committing at least one Type I error (false positive) increases with each additional comparison. This is known as the **family-wise error rate (FWER)** inflation problem.

**The Problem:**
- If we make `k` independent comparisons at α = 0.05, the FWER is:
  - FWER = 1 - (1 - α)^k
  - For 6 comparisons: FWER = 1 - (0.95)^6 = 0.265 (26.5% chance of at least one false positive!)

**Tukey's Solution:**
- Uses the **Studentized Range Distribution** (q-distribution)
- Controls FWER exactly at α when sample sizes are equal
- Provides simultaneous confidence intervals for all pairwise differences

### 1.2 The Studentized Range Distribution

The studentized range distribution is the distribution of the range (max - min) of standardized normal variables. It's defined as:

$$q = \frac{\bar{Y}_{max} - \bar{Y}_{min}}{\sqrt{MSE/n}}$$

Where:
- $\bar{Y}_{max}$ = Largest group mean
- $\bar{Y}_{min}$ = Smallest group mean
- MSE = Mean Square Error from ANOVA
- n = Sample size per group

### 1.3 Tukey's HSD Formula

The **Honest Significant Difference** (HSD) value is calculated as:

$$HSD = q_{\alpha, k, df} \times \sqrt{\frac{MSE}{n}}$$

Where:
- $q_{\alpha, k, df}$ = Critical value from studentized range distribution
- k = Number of groups
- df = Degrees of freedom (error)
- MSE = Mean Square Error
- n = Sample size per group

Any pair with mean difference > HSD is declared significant.

---

## 2. Statistical Concepts and Formulas

### 2.1 Complete ANOVA vs Tukey's HSD Comparison

| Aspect | ANOVA (F-test) | Tukey's HSD |
|--------|----------------|-------------|
| **Purpose** | Test if any means differ | Identify which means differ |
| **Hypothesis** | H₀: μ₁ = μ₂ = ... = μₖ | H₀: μᵢ = μⱼ for each pair |
| **Number of Tests** | 1 (global) | k(k-1)/2 (pairwise) |
| **Distribution** | F-distribution | Studentized Range (q) |
| **Critical Value** | F₍α, k-1, N-k₎ | q₍α, k, N-k₎ |
| **Multiple Comparison Control** | N/A | Exact FWER control |
| **Power** | High for global differences | Lower but specific |
| **When to Use** | First step in analysis | Follow-up to significant ANOVA |

### 2.2 Types of Multiple Comparison Corrections

| Method | Description | FWER Control | Power | When to Use |
|--------|-------------|--------------|-------|-------------|
| **Tukey's HSD** | Uses studentized range distribution | Exact (balanced) | High | Post-ANOVA pairwise comparisons |
| **Bonferroni** | α ÷ number of comparisons | Conservative | Low | Few comparisons |
| **Scheffé** | Uses F-distribution | Conservative | Low | All possible contrasts |
| **Holm** | Sequential Bonferroni | Less conservative | Moderate | General use |
| **Dunnett** | Compare all to control | Exact | High | Comparing treatments to control |

### 2.3 Assumptions

Tukey's HSD assumes:
1. **Independence**: Observations are independent
2. **Normality**: Data within each group is normally distributed
3. **Homogeneity of Variances**: Equal variances across groups
4. **Balanced Design**: Equal sample sizes (approximately)

---

## 3. Case Study: Fertilizer Effectiveness

### Complete Analysis Code

```python
# ==============================================
# COMPLETE CASE STUDY: Fertilizer Effectiveness
# ==============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.anova import anova_lm
import warnings
warnings.filterwarnings('ignore')

# Set seed for reproducibility
np.random.seed(42)

# ==============================================
# DATA GENERATION
# ==============================================

# Define experimental parameters
fertilizers = ['Fertilizer_A', 'Fertilizer_B', 'Fertilizer_C', 'Fertilizer_D']
true_means = {
    'Fertilizer_A': 25.0,  # Control
    'Fertilizer_B': 28.5,  # Slight improvement
    'Fertilizer_C': 32.0,  # Moderate improvement
    'Fertilizer_D': 37.5   # Major improvement
}
n_per_group = 20
sigma = 3.0  # Standard deviation

# Generate data
data = []
for fertilizer, mean in true_means.items():
    heights = np.random.normal(mean, sigma, n_per_group)
    for height in heights:
        data.append({'Fertilizer': fertilizer, 'Height': height})

df = pd.DataFrame(data)

# Sort categories for consistent reference
df['Fertilizer'] = pd.Categorical(df['Fertilizer'], 
                                  categories=sorted(df['Fertilizer'].unique()), 
                                  ordered=True)

print("="*80)
print("CASE STUDY: EFFECTIVENESS OF FERTILIZERS ON PLANT GROWTH")
print("="*80)

# ==============================================
# SECTION 1: SUMMARY STATISTICS
# ==============================================

print("\n" + "="*80)
print("SECTION 1: SUMMARY STATISTICS")
print("="*80)

# Calculate summary statistics
summary_stats = df.groupby('Fertilizer')['Height'].agg([
    ('N', 'count'),
    ('Mean', 'mean'),
    ('SD', 'std'),
    ('SE', lambda x: x.std() / np.sqrt(len(x))),
    ('Min', 'min'),
    ('Max', 'max'),
    ('Median', 'median')
]).round(2)

print("\nDESCRIPTIVE STATISTICS BY FERTILIZER TYPE:")
print("-"*70)
print(summary_stats)

# Additional statistics
grand_mean = df['Height'].mean()
total_n = len(df)

print(f"\nGrand Mean: {grand_mean:.2f} cm")
print(f"Total N: {total_n}")
print(f"Groups: {len(fertilizers)}")

# ==============================================
# SECTION 2: ANOVA (Step 1)
# ==============================================

print("\n" + "="*80)
print("SECTION 2: STEP 1 - GLOBAL ANOVA F-TEST")
print("="*80)

# Fit ANOVA model
model = ols('Height ~ C(Fertilizer)', data=df).fit()
anova_result = anova_lm(model, typ=2)

print("\nANOVA RESULTS TABLE:")
print("-"*70)
print(anova_result.to_string())

# Extract key statistics
f_stat = anova_result['F'].iloc[0]
p_val = anova_result['PR(>F)'].iloc[0]
df_between = int(anova_result['df'].iloc[0])
df_within = int(anova_result['df'].iloc[1])
ss_between = anova_result['sum_sq'].iloc[0]
ss_within = anova_result['sum_sq'].iloc[1]
ms_between = anova_result['mean_sq'].iloc[0]
ms_within = anova_result['mean_sq'].iloc[1]

print(f"\nANOVA STATISTICS:")
print("-"*50)
print(f"F-statistic: {f_stat:.2f}")
print(f"P-value: {p_val:.6f}")
print(f"df Between: {df_between}")
print(f"df Within: {df_within}")
print(f"SS Between: {ss_between:.2f}")
print(f"SS Within: {ss_within:.2f}")
print(f"MS Between: {ms_between:.2f}")
print(f"MS Within: {ms_within:.2f}")

# Interpretation
if p_val < 0.05:
    print("\n✓ INTERPRETATION: ANOVA is SIGNIFICANT (p < 0.05)")
    print("  → At least one fertilizer type differs from the others")
    print("  → PROCEED with Tukey's HSD test")
    proceed_tukey = True
else:
    print("\n✗ INTERPRETATION: ANOVA is NOT significant (p ≥ 0.05)")
    print("  → No evidence of differences among fertilizer types")
    print("  → STOP here - Tukey's HSD is not needed")
    proceed_tukey = False

# ==============================================
# SECTION 3: TUKEY'S HSD (Step 2)
# ==============================================

if proceed_tukey:
    print("\n" + "="*80)
    print("SECTION 3: STEP 2 - TUKEY'S HONEST SIGNIFICANT DIFFERENCE TEST")
    print("="*80)
    
    # Perform Tukey's HSD
    tukey_result = pairwise_tukeyhsd(endog=df['Height'], 
                                      groups=df['Fertilizer'], 
                                      alpha=0.05)
    
    # Calculate HSD value
    from scipy.stats import studentized_range
    
    # Critical value from studentized range distribution
    q_critical = studentized_range.ppf(0.95, len(fertilizers), df_within)
    hsd_value = q_critical * np.sqrt(ms_within / n_per_group)
    
    print(f"\nCRITICAL VALUES:")
    print("-"*50)
    print(f"q-critical (α=0.05, k={len(fertilizers)}, df={df_within}): {q_critical:.4f}")
    print(f"HSD Threshold: {hsd_value:.2f} cm")
    print(f"Any pair with mean difference > {hsd_value:.2f} cm is significantly different")
    
    # Display results
    print("\nTUKEY'S HSD RESULTS TABLE:")
    print("-"*80)
    
    # Create formatted table
    tukey_df = pd.DataFrame({
        'Comparison': [f"{g1} vs {g2}" for g1, g2 in zip(tukey_result._results_table.data[1:, 1], 
                                                           tukey_result._results_table.data[1:, 0])],
        'Diff': tukey_result.meandiffs,
        'Lower_95_CI': tukey_result.conf_int[:, 0],
        'Upper_95_CI': tukey_result.conf_int[:, 1],
        'p_adj': tukey_result.pvalues,
        'Significant': ['*' if rej else '' for rej in tukey_result.reject]
    })
    tukey_df = tukey_df.round(4)
    
    print(tukey_df.to_string(index=False))
    
    # ==============================================
    # SECTION 4: DETAILED INTERPRETATION (Step 3)
    # ==============================================
    
    print("\n" + "="*80)
    print("SECTION 4: DETAILED INTERPRETATION OF EACH COMPARISON")
    print("="*80)
    
    significant_pairs = tukey_df[tukey_df['Significant'] == '*']
    nonsignificant_pairs = tukey_df[tukey_df['Significant'] == '']
    
    print(f"\nNUMBER OF COMPARISONS:")
    print(f"Total pairs: {len(tukey_df)}")
    print(f"Significant: {len(significant_pairs)}")
    print(f"Not significant: {len(nonsignificant_pairs)}")
    
    if len(significant_pairs) > 0:
        print("\n" + "="*70)
        print("SIGNIFICANT COMPARISONS (p_adj < 0.05):")
        print("="*70)
        
        for idx, row in significant_pairs.iterrows():
            print(f"\n▶ {row['Comparison']}:")
            print(f"   Mean Difference: {row['Diff']:.2f} cm")
            print(f"   95% Confidence Interval: [{row['Lower_95_CI']:.2f}, {row['Upper_95_CI']:.2f}]")
            print(f"   Adjusted P-value: {row['p_adj']:.6f}")
            
            # Interpret direction
            g1, g2 = row['Comparison'].split(' vs ')
            if row['Diff'] > 0:
                print(f"   → {g1} significantly outperforms {g2} by {row['Diff']:.2f} cm")
            else:
                print(f"   → {g2} significantly outperforms {g1} by {abs(row['Diff']):.2f} cm")
            
            # Confidence interval interpretation
            if row['Lower_95_CI'] > 0:
                print(f"   → CI entirely above zero: confidence that true difference is positive")
            elif row['Upper_95_CI'] < 0:
                print(f"   → CI entirely below zero: confidence that true difference is negative")
    
    if len(nonsignificant_pairs) > 0:
        print("\n" + "="*70)
        print("NON-SIGNIFICANT COMPARISONS (p_adj ≥ 0.05):")
        print("="*70)
        
        for idx, row in nonsignificant_pairs.iterrows():
            print(f"\n▸ {row['Comparison']}:")
            print(f"   Mean Difference: {row['Diff']:.2f} cm")
            print(f"   95% Confidence Interval: [{row['Lower_95_CI']:.2f}, {row['Upper_95_CI']:.2f}]")
            print(f"   Adjusted P-value: {row['p_adj']:.6f}")
            print(f"   → No significant difference between these groups")
            
            # Check if confidence interval contains zero
            if row['Lower_95_CI'] < 0 < row['Upper_95_CI']:
                print(f"   → CI contains zero, consistent with non-significant result")
    
    # ==============================================
    # SECTION 5: RANKING AND CONCLUSIONS (Step 4)
    # ==============================================
    
    print("\n" + "="*80)
    print("SECTION 5: RANKING AND CONCLUSIONS")
    print("="*80)
    
    # Rank groups by mean
    sorted_means = summary_stats.sort_values('Mean', ascending=False)
    print("\nFERTILIZERS RANKED BY EFFECTIVENESS:")
    print("-"*50)
    for rank, (name, row) in enumerate(sorted_means.iterrows(), 1):
        print(f"{rank}. {name}: {row['Mean']:.2f} cm ± {row['SD']:.2f}")
    
    # Identify best and worst
    best = sorted_means.index[0]
    worst = sorted_means.index[-1]
    best_mean = sorted_means.iloc[0]['Mean']
    worst_mean = sorted_means.iloc[-1]['Mean']
    
    print(f"\nBEST PERFORMER: {best} ({best_mean:.2f} cm)")
    print(f"WORST PERFORMER: {worst} ({worst_mean:.2f} cm)")
    print(f"DIFFERENCE: {best_mean - worst_mean:.2f} cm")
    
    # Homogeneous groups (groups not significantly different)
    print("\nHOMOGENEOUS GROUPS (Not significantly different):")
    print("-"*50)
    
    # Group significant pairs into clusters
    significant_pairs_list = [row['Comparison'].split(' vs ') for _, row in significant_pairs.iterrows()]
    
    # Create adjacency matrix for significant differences
    all_groups = sorted(df['Fertilizer'].unique())
    sig_matrix = pd.DataFrame(0, index=all_groups, columns=all_groups)
    for g1, g2 in significant_pairs_list:
        sig_matrix.loc[g1, g2] = 1
        sig_matrix.loc[g2, g1] = 1
    
    # Find groups connected by non-significance (complement of significant graph)
    import networkx as nx
    G = nx.Graph()
    G.add_nodes_from(all_groups)
    
    # Add edges for non-significant pairs
    non_sig_pairs = [row['Comparison'].split(' vs ') for _, row in nonsignificant_pairs.iterrows()]
    for g1, g2 in non_sig_pairs:
        G.add_edge(g1, g2)
    
    # Find connected components
    components = list(nx.connected_components(G))
    
    for i, component in enumerate(components, 1):
        print(f"Group {i}: {', '.join(sorted(component))}")
        means = [f"{name} ({summary_stats.loc[name, 'Mean']:.1f} cm)" for name in sorted(component)]
        print(f"  Means: {', '.join(means)}")
    
    # ==============================================
    # SECTION 6: FINAL REPORT
    # ==============================================
    
    print("\n" + "="*80)
    print("FINAL REPORT: FERTILIZER EFFECTIVENESS STUDY")
    print("="*80)
    
    print("\nRESEARCH QUESTION:")
    print("Does the type of fertilizer significantly affect plant growth?")
    
    print("\nEXPERIMENTAL DESIGN:")
    print(f"- 4 fertilizer treatments: {', '.join(fertilizers)}")
    print(f"- {n_per_group} plants per treatment (N = {n_per_group * len(fertilizers)})")
    print("- Response: Plant height (cm) after 8 weeks")
    print("- Analysis: One-way ANOVA + Tukey's HSD post-hoc test")
    
    print("\nSTATISTICAL FINDINGS:")
    print(f"1. Global ANOVA: F({df_between}, {df_within}) = {f_stat:.2f}, p = {p_val:.6f}")
    print(f"   → {('Significant' if p_val < 0.05 else 'Not significant')} overall differences detected")
    
    if len(significant_pairs) > 0:
        print(f"\n2. Tukey's HSD identified {len(significant_pairs)} significant pairwise differences:")
        for idx, row in significant_pairs.iterrows():
            print(f"   • {row['Comparison']}: diff = {row['Diff']:.2f} cm, p_adj = {row['p_adj']:.6f}")
    
    print(f"\n3. Best fertilizer: {best} ({best_mean:.2f} cm)")
    print(f"   Worst fertilizer: {worst} ({worst_mean:.2f} cm)")
    print(f"   Difference between best and worst: {best_mean - worst_mean:.2f} cm")
    
    print("\nPRACTICAL CONCLUSIONS:")
    print(f"1. {best} provides superior plant growth compared to all other fertilizers tested")
    print(f"2. For maximum plant growth, recommend using {best} in similar growing conditions")
    print(f"3. The effect size difference between best and worst is {best_mean - worst_mean:.2f} cm")
    
    print("\nLIMITATIONS AND FUTURE DIRECTIONS:")
    print("1. Results specific to these experimental conditions")
    print("2. Consider cost-effectiveness alongside growth benefits")
    print("3. Further research needed on long-term effects and soil health")
    
    # ==============================================
    # SECTION 7: VISUALIZATION
    # ==============================================
    
    print("\n" + "="*80)
    print("SECTION 7: VISUALIZATION")
    print("="*80)
    
    # Create comprehensive visualization
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    
    # 1. Boxplot
    sns.boxplot(data=df, x='Fertilizer', y='Height', ax=axes[0,0], palette='Set2')
    axes[0,0].axhline(y=grand_mean, color='red', linestyle='--', linewidth=2, label='Grand Mean')
    axes[0,0].set_title('Plant Height Distribution by Fertilizer', fontsize=12, fontweight='bold')
    axes[0,0].set_ylabel('Height (cm)', fontsize=11)
    axes[0,0].legend()
    axes[0,0].grid(True, alpha=0.3)
    plt.setp(axes[0,0].xaxis.get_majorticklabels(), rotation=15)
    
    # 2. Bar plot with error bars
    means = df.groupby('Fertilizer')['Height'].mean()
    stds = df.groupby('Fertilizer')['Height'].std()
    se = stds / np.sqrt(n_per_group)
    axes[0,1].bar(means.index, means.values, yerr=se, capsize=5, 
                   color=['#66b3b2', '#ffcc99', '#ff9999', '#99cc99'])
    axes[0,1].axhline(y=grand_mean, color='red', linestyle='--', linewidth=2, label='Grand Mean')
    axes[0,1].set_title('Mean Plant Height (± SE)', fontsize=12, fontweight='bold')
    axes[0,1].set_ylabel('Mean Height (cm)', fontsize=11)
    axes[0,1].legend()
    axes[0,1].grid(True, alpha=0.3)
    plt.setp(axes[0,1].xaxis.get_majorticklabels(), rotation=15)
    
    # 3. QQ Plot for normality check
    import scipy.stats as scs
    residuals = model.resid
    scs.probplot(residuals, dist="norm", plot=axes[0,2])
    axes[0,2].set_title('QQ Plot: ANOVA Residuals', fontsize=12, fontweight='bold')
    axes[0,2].grid(True, alpha=0.3)
    
    # 4. Tukey HSD Confidence Intervals
    comparisons = tukey_df['Comparison'].values
    diff = tukey_df['Diff'].values
    lower = tukey_df['Lower_95_CI'].values
    upper = tukey_df['Upper_95_CI'].values
    significant = tukey_df['Significant'].values
    
    colors = ['red' if sig == '*' else 'blue' for sig in significant]
    axes[1,0].errorbar(comparisons, diff, 
                       yerr=[diff - lower, upper - diff],
                       fmt='o', color=colors, capsize=5, elinewidth=2, markersize=10)
    axes[1,0].axhline(y=0, color='black', linestyle='-', alpha=0.5)
    axes[1,0].axhline(y=hsd_value, color='green', linestyle='--', linewidth=2, 
                       label=f'HSD = {hsd_value:.2f} cm')
    axes[1,0].axhline(y=-hsd_value, color='green', linestyle='--', linewidth=2)
    axes[1,0].set_xlabel('Comparison', fontsize=11)
    axes[1,0].set_ylabel('Mean Difference (cm)', fontsize=11)
    axes[1,0].set_title('Tukey HSD: 95% Confidence Intervals\n(Red = Significant, Blue = Not)', 
                         fontsize=12, fontweight='bold')
    axes[1,0].legend()
    plt.setp(axes[1,0].xaxis.get_majorticklabels(), rotation=45, ha='right')
    axes[1,0].grid(True, alpha=0.3)
    
    # 5. P-values bar chart
    x_pos = np.arange(len(comparisons))
    axes[1,1].bar(x_pos, tukey_df['p_adj'], 
                  color=['red' if p < 0.05 else 'blue' for p in tukey_df['p_adj']], 
                  alpha=0.7)
    axes[1,1].axhline(y=0.05, color='black', linestyle='--', linewidth=2, label='α = 0.05')
    axes[1,1].set_xlabel('Comparison', fontsize=11)
    axes[1,1].set_ylabel('Adjusted P-value', fontsize=11)
    axes[1,1].set_title('Tukey HSD: Adjusted P-values\n(Below line = Significant)', 
                         fontsize=12, fontweight='bold')
    axes[1,1].set_xticks(x_pos)
    axes[1,1].set_xticklabels(comparisons, rotation=45, ha='right')
    axes[1,1].legend()
    axes[1,1].grid(True, alpha=0.3)
    
    # 6. Homogeneous groups visualization
    if len(components) > 0:
        # Create heatmap of significant differences
        sig_matrix_vis = pd.DataFrame(0, index=all_groups, columns=all_groups)
        for g1, g2 in significant_pairs_list:
            sig_matrix_vis.loc[g1, g2] = 1
            sig_matrix_vis.loc[g2, g1] = 1
        
        sns.heatmap(sig_matrix_vis, annot=True, fmt='d', 
                    cmap=['lightgreen', 'red'], 
                    cbar=False, square=True, linewidths=0.5, ax=axes[1,2])
        axes[1,2].set_title('Tukey HSD: Significant Differences\n(Green = Not Sig, Red = Sig)', 
                             fontsize=12, fontweight='bold')
        axes[1,2].set_xlabel('Fertilizer Type', fontsize=11)
        axes[1,2].set_ylabel('Fertilizer Type', fontsize=11)
    
    plt.tight_layout()
    plt.savefig('fertilizer_complete_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("\nVisualization saved as: fertilizer_complete_analysis.png")
    
else:
    print("\nSince ANOVA was not significant, Tukey's HSD was not performed.")
    print("All fertilizer types appear to produce similar plant growth.")

print("\n" + "="*80)
print("END OF CASE STUDY ANALYSIS")
print("="*80)
```

---

## 4. Detailed Output Interpretation Guide

### 4.1 Understanding Each Column in Tukey's Output

| Column | Name | Description | Interpretation |
|--------|------|-------------|----------------|
| **Comparison** | Groups compared | Which two groups are being tested | Shows the pair being evaluated |
| **Diff** | Mean Difference | Difference between group means | Positive = first group higher, Negative = second group higher |
| **Lower_95_CI** | Lower bound of 95% CI | Lower limit of confidence interval | If > 0, first group significantly higher |
| **Upper_95_CI** | Upper bound of 95% CI | Upper limit of confidence interval | If < 0, second group significantly higher |
| **p_adj** | Adjusted p-value | p-value corrected for multiple tests | If < 0.05, difference is significant |
| **Significant** | Significance indicator | '*' indicates significance | Star marks significant differences |

### 4.2 Step-by-Step Reading Guide

**Step 1: Check the Overall Pattern**
```python
# Look at the table holistically
print(f"Total comparisons: {len(tukey_df)}")
print(f"Significant comparisons: {sum(tukey_df['Significant'] == '*')}")
print(f"Significant proportion: {sum(tukey_df['Significant'] == '*') / len(tukey_df):.1%}")
```

**Step 2: Identify Significant Pairs**
```python
# Filter significant results
significant = tukey_df[tukey_df['Significant'] == '*']
print("\nSignificant Comparisons:")
print(significant[['Comparison', 'Diff', 'p_adj']].to_string(index=False))
```

**Step 3: Interpret Direction of Difference**
```python
# For each significant pair, determine direction
for _, row in significant.iterrows():
    g1, g2 = row['Comparison'].split(' vs ')
    if row['Diff'] > 0:
        print(f"{g1} > {g2} by {row['Diff']:.2f} cm")
    else:
        print(f"{g2} > {g1} by {abs(row['Diff']):.2f} cm")
```

**Step 4: Examine Confidence Intervals**
```python
# Check if CI contains zero
for _, row in tukey_df.iterrows():
    if row['Lower_95_CI'] < 0 < row['Upper_95_CI']:
        print(f"{row['Comparison']}: CI contains zero → Not significant")
    else:
        print(f"{row['Comparison']}: CI away from zero → Significant")
```

**Step 5: Identify Groups Forming Homogeneous Subsets**
```python
# Groups that are not significantly different form homogeneous subsets
nonsig = tukey_df[tukey_df['Significant'] == '']
print("\nNon-significant pairs (form homogeneous groups):")
print(nonsig['Comparison'].values)
```

### 4.3 Common Patterns and Their Meanings

| Pattern | Meaning | Interpretation |
|---------|---------|----------------|
| All pairs significant | Every group differs from every other | Strong treatment effects |
| No pairs significant | No group differs from any other | No treatment effects |
| Some pairs significant | Some groups differ, some don't | Partial treatment effects |
| Step-like pattern | A < B < C < D with varying significance | Graded treatment effects |
| Cluster pattern | Groups form distinct clusters | Natural grouping of treatments |

---

## 5. Reporting Guidelines

### 5.1 APA Style Reporting Template

**When reporting Tukey's HSD results:**

> "A one-way ANOVA revealed a significant effect of fertilizer type on plant growth, F(3, 76) = 48.23, p < .001. Post-hoc comparisons using Tukey's HSD test indicated that Fertilizer_D (M = 37.45, SD = 2.98) produced significantly taller plants than Fertilizer_A (M = 24.98, SD = 2.87), p < .001, Fertilizer_B (M = 28.53, SD = 3.12), p < .001, and Fertilizer_C (M = 32.04, SD = 3.05), p = .004. Fertilizer_C also significantly outperformed Fertilizer_A, p < .001, and Fertilizer_B, p = .012. However, Fertilizer_B did not significantly differ from Fertilizer_A, p = .452. The largest effect was observed between Fertilizer_D and Fertilizer_A, with a mean difference of 12.47 cm (95% CI [9.35, 15.59])."

### 5.2 Common Reporting Formats

**Format 1: Compact Table Format**
```python
# Create compact reporting table
report_table = pd.DataFrame({
    'Comparison': tukey_df['Comparison'],
    'Mean_Diff': tukey_df['Diff'],
    '95%_CI': [f"[{row['Lower_95_CI']:.2f}, {row['Upper_95_CI']:.2f}]" for _, row in tukey_df.iterrows()],
    'p': tukey_df['p_adj'],
    'Sig': ['*' if sig else 'ns' for sig in tukey_df['Significant']]
})
print(report_table.to_string(index=False))
```

**Format 2: Narrative Style**
```python
def generate_narrative(tukey_df, significant_pairs):
    narrative = "Tukey's HSD post-hoc comparisons revealed "
    
    if len(significant_pairs) == 0:
        narrative += "no significant differences between any groups (all p_adj > 0.05)."
    elif len(significant_pairs) == len(tukey_df):
        narrative += "significant differences between all pairs of groups."
    else:
        sig_comparisons = []
        for _, row in significant_pairs.iterrows():
            g1, g2 = row['Comparison'].split(' vs ')
            sig_comparisons.append(f"{g1} vs {g2} (diff = {row['Diff']:.2f} cm, p_adj = {row['p_adj']:.4f})")
        narrative += f"significant differences for {len(significant_pairs)} out of {len(tukey_df)} comparisons: " + "; ".join(sig_comparisons)
    
    return narrative

print(generate_narrative(tukey_df, significant_pairs))
```

### 5.3 Effect Size Reporting

Tukey's HSD doesn't provide a single effect size, but you can report:

**1. Mean Differences and Confidence Intervals**
```python
# Report the largest and smallest differences
max_diff = tukey_df['Diff'].max()
min_diff = tukey_df['Diff'].min()
print(f"Range of mean differences: {min_diff:.2f} to {max_diff:.2f} cm")
```

**2. Cohen's d for Pairwise Comparisons**
```python
def cohens_d(group1, group2):
    pooled_sd = np.sqrt((np.var(group1) + np.var(group2)) / 2)
    return (np.mean(group1) - np.mean(group2)) / pooled_sd

# Calculate Cohen's d for each pair
for _, row in significant_pairs.iterrows():
    g1, g2 = row['Comparison'].split(' vs ')
    d = cohens_d(df[df['Fertilizer'] == g1]['Height'].values,
                  df[df['Fertilizer'] == g2]['Height'].values)
    print(f"{g1} vs {g2}: Cohen's d = {d:.2f}")
```

**3. Eta-Squared (η²) from ANOVA**
```python
eta_squared = ss_between / (ss_between + ss_within)
print(f"Eta-squared (η²) = {eta_squared:.3f}")
print(f"Interpretation: {eta_squared*100:.1f}% of variance explained by fertilizer type")
```

### 5.4 Visual Reporting

```python
def create_report_summary():
    """Create a comprehensive summary figure for reporting"""
    fig = plt.figure(figsize=(15, 10))
    
    # Main plot: Means with significance letters
    ax1 = fig.add_subplot(221)
    means = df.groupby('Fertilizer')['Height'].mean()
    errors = df.groupby('Fertilizer')['Height'].std() / np.sqrt(n_per_group)
    
    bars = ax1.bar(range(len(means)), means, yerr=errors, capsize=5,
                   color=['#66b3b2', '#ffcc99', '#ff9999', '#99cc99'])
    ax1.set_xticks(range(len(means)))
    ax1.set_xticklabels(means.index, rotation=15)
    ax1.set_ylabel('Mean Height (cm)')
    ax1.set_title('Plant Growth by Fertilizer Type')
    ax1.grid(True, alpha=0.3)
    
    # Add significance letters
    import string
    sig_letters = []
    # Group means into homogeneous subsets
    # (Simplified - in practice, use compact letter display)
    if len(significant_pairs) > 0:
        # Sort means and assign letters
        sorted_means = means.sort_values(ascending=False)
        letters = {name: string.ascii_uppercase[i] for i, name in enumerate(sorted_means.index)}
        for i, (name, bar) in enumerate(zip(means.index, bars)):
            ax1.text(bar.get_x() + bar.get_width()/2., 
                    bar.get_height() + 0.5,
                    letters[name], ha='center', va='bottom', fontweight='bold')
    
    # Tukey results summary
    ax2 = fig.add_subplot(222)
    ax2.axis('off')
    ax