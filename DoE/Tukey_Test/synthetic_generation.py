# ==============================================
# COMPLETE DoE ANALYSIS WITH FIGURE EXPORT
# ==============================================

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
import patsy
from IPython.display import display
import os

# Set random seed for reproducibility
np.random.seed(42)

# Create figures directory if it doesn't exist
figures_dir = './figures'
os.makedirs(figures_dir, exist_ok=True)

# ==============================================
# SECTION 1: SYNTHETIC DATASET GENERATION
# ==============================================

n_per_group = 10
groups = ['A', 'B', 'C', 'D']
true_means = {'A': 0.0, 'B': 1.8, 'C': 2.0, 'D': 4.2}

data = []
for group in groups:
    y = np.random.normal(loc=true_means[group], scale=1.0, size=n_per_group)
    for val in y:
        data.append({'Group': group, 'Value': val})

df = pd.DataFrame(data)
print("Dataset Preview:")
display(df.head(10))
print(f"\nTotal observations (N): {len(df)}")

# ==============================================
# SECTION 2: DESIGN MATRIX CONSTRUCTION
# ==============================================

# 1. Baseline (Treatment) Contrast
X_treatment = patsy.dmatrix("C(Group, Treatment)", df, return_type="dataframe")
print("--- Baseline (Treatment) Design Matrix ---")
display(X_treatment.head())

# 2. Sum-to-Zero Contrast
X_sum = patsy.dmatrix("C(Group, Sum)", df, return_type="dataframe")
print("\n--- Sum-to-Zero Design Matrix ---")
display(X_sum.head())

# ==============================================
# SECTION 3: FIT LINEAR MODELS
# ==============================================

model_treat = smf.ols('Value ~ C(Group, Treatment)', data=df).fit()
model_sum = smf.ols('Value ~ C(Group, Sum)', data=df).fit()

# 1. Global ANOVA F-Test
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

# ==============================================
# SECTION 4: POWER ANALYSIS
# ==============================================

grand_mean = df['Value'].mean()
variance_between = np.mean([(true_means[g] - grand_mean)**2 for g in groups])
variance_within = df.groupby('Group')['Value'].var().mean()
cohens_f = np.sqrt(variance_between / variance_within)

print(f"Estimated Cohen's f (Effect Size): {cohens_f:.3f}")

analysis = FTestAnovaPower()
n_required = analysis.solve_power(
    effect_size=cohens_f, 
    nobs=None,
    alpha=0.05, 
    power=0.80, 
    k_groups=4
)

print(f"Required sample size PER GROUP for 80% power: {np.ceil(n_required)}")

# FIGURE 1: Power Curve
ns = np.arange(5, 30, 1)
powers = [analysis.power(effect_size=cohens_f, nobs=n, alpha=0.05, k_groups=4) for n in ns]

plt.figure(figsize=(8, 5))
plt.plot(ns, powers, marker='o', linestyle='-', color='b', linewidth=2, markersize=8)
plt.axhline(0.8, color='r', linestyle='--', linewidth=2, label='Target Power (0.80)')
plt.axvline(np.ceil(n_required), color='g', linestyle='--', linewidth=2, label=f'Required N={np.ceil(n_required)}')
plt.title('Power Curve for One-Way ANOVA', fontsize=14, fontweight='bold')
plt.xlabel('Sample Size per Group (n)', fontsize=12)
plt.ylabel('Statistical Power', fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(figures_dir, 'power_curve.png'), dpi=300, bbox_inches='tight')
plt.show()
print(f"Power curve saved to: {os.path.join(figures_dir, 'power_curve.png')}")

# ==============================================
# SECTION 5: MULTIPLE COMPARISONS
# ==============================================

# 1. Unadjusted P-values
unadjusted_p = []
comparison_labels = []
for i in range(len(groups)):
    for j in range(i+1, len(groups)):
        t_stat, p_val = stats.ttest_ind(
            df[df['Group'] == groups[i]]['Value'], 
            df[df['Group'] == groups[j]]['Value']
        )
        unadjusted_p.append(p_val)
        comparison_labels.append(f"{groups[i]} vs {groups[j]}")

# 2. Bonferroni Correction
reject_bonf, pvals_bonf, _, _ = multipletests(unadjusted_p, alpha=0.05, method='bonferroni')

# 3. Tukey's HSD
tukey_results = pairwise_tukeyhsd(endog=df['Value'], groups=df['Group'], alpha=0.05)
print("="*50)
print("TUKEY'S HSD TEST RESULTS")
print("="*50)
print(tukey_results)

# 4. Pingouin Pairwise Tests
pg_results = pg.pairwise_ttests(data=df, dv='Value', between='Group', padjust='holm')
print("\nPingouin Pairwise T-tests (Holm corrected):")
display(pg_results)

# 5. scikit-posthocs heatmap visualization
print("\n" + "="*50)
print("SCIKIT-POSTHOCS TUKEY HSD HEATMAP")
print("="*50)

# Calculate Tukey HSD p-values matrix
tukey_matrix = sp.posthoc_tukey(df, val_col='Value', group_col='Group')
print("Tukey HSD P-value Matrix:")
display(tukey_matrix)

# FIGURE 2: Tukey HSD P-value Matrix Heatmap
plt.figure(figsize=(8, 6))
heatmap = sns.heatmap(tukey_matrix, 
                     annot=True,
                     fmt='.4f',
                     cmap='RdYlGn_r',
                     cbar_kws={'label': 'p-value'},
                     square=True,
                     linewidths=0.5,
                     vmin=0, 
                     vmax=0.1)
plt.title('Tukey HSD: Pairwise P-value Matrix\n(Red = Significant Difference)', 
          fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(figures_dir, 'tukey_pvalue_heatmap.png'), dpi=300, bbox_inches='tight')
plt.show()
print(f"Tukey p-value heatmap saved to: {os.path.join(figures_dir, 'tukey_pvalue_heatmap.png')}")

# FIGURE 3: Significance Matrix
sig_matrix = tukey_matrix < 0.05
plt.figure(figsize=(8, 6))
sig_heatmap = sns.heatmap(sig_matrix, 
                         annot=True,
                         fmt='d',
                         cmap=['lightgreen', 'red'],
                         cbar=False,
                         square=True,
                         linewidths=0.5)
plt.title('Tukey HSD: Significant Differences (p < 0.05)\nGreen = Not Significant, Red = Significant',
          fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(figures_dir, 'tukey_significance_matrix.png'), dpi=300, bbox_inches='tight')
plt.show()
print(f"Significance matrix saved to: {os.path.join(figures_dir, 'tukey_significance_matrix.png')}")

# ==============================================
# SECTION 6: COMPARISON OF METHODS
# ==============================================

# Create a comparison DataFrame
comparison_df = pd.DataFrame({
    'Comparison': comparison_labels,
    'Unadjusted': unadjusted_p,
    'Bonferroni': pvals_bonf,
    'Tukey': [tukey_results.pvalues[i] for i in range(len(comparison_labels))]
})

print("\n" + "="*50)
print("MULTIPLE COMPARISON METHODS COMPARISON")
print("="*50)
display(comparison_df)

# FIGURE 4: Comparison of Methods Bar Chart
fig, ax = plt.subplots(figsize=(12, 6))
x = np.arange(len(comparison_labels))
width = 0.25

bars1 = ax.bar(x - width, comparison_df['Unadjusted'], width, label='Unadjusted', alpha=0.7, color='blue')
bars2 = ax.bar(x, comparison_df['Bonferroni'], width, label='Bonferroni', alpha=0.7, color='orange')
bars3 = ax.bar(x + width, comparison_df['Tukey'], width, label='Tukey HSD', alpha=0.7, color='green')

ax.axhline(y=0.05, color='red', linestyle='--', linewidth=2, label='α = 0.05')
ax.set_xlabel('Comparison', fontsize=12)
ax.set_ylabel('p-value', fontsize=12)
ax.set_title('Comparison of Multiple Testing Correction Methods', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(comparison_labels, rotation=45, ha='right')
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(figures_dir, 'multiple_comparison_methods.png'), dpi=300, bbox_inches='tight')
plt.show()
print(f"Methods comparison saved to: {os.path.join(figures_dir, 'multiple_comparison_methods.png')}")

# FIGURE 5: Tukey HSD Mean Differences with Confidence Intervals
tukey_df = pd.DataFrame({
    'Comparison': comparison_labels,
    'Mean_Diff': tukey_results.meandiffs,
    'Lower_CI': tukey_results.conf_int[:, 0],
    'Upper_CI': tukey_results.conf_int[:, 1],
    'Significant': tukey_results.reject
})

fig, ax = plt.subplots(figsize=(10, 6))
colors = ['red' if sig else 'blue' for sig in tukey_df['Significant']]
ax.errorbar(tukey_df['Comparison'], tukey_df['Mean_Diff'],
           yerr=[tukey_df['Mean_Diff'] - tukey_df['Lower_CI'], 
                 tukey_df['Upper_CI'] - tukey_df['Mean_Diff']],
           fmt='o', color=colors, capsize=5, elinewidth=2, markersize=10)
ax.axhline(y=0, color='black', linestyle='-', alpha=0.5)
ax.set_xlabel('Comparison', fontsize=12)
ax.set_ylabel('Mean Difference', fontsize=12)
ax.set_title('Tukey HSD: Mean Differences with 95% Confidence Intervals\n(Red = Significant, Blue = Not Significant)',
             fontsize=14, fontweight='bold')
ax.axhline(y=0, color='black', linestyle='--', alpha=0.3)
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(figures_dir, 'tukey_mean_differences_ci.png'), dpi=300, bbox_inches='tight')
plt.show()
print(f"Tukey mean differences saved to: {os.path.join(figures_dir, 'tukey_mean_differences_ci.png')}")

# ==============================================
# SECTION 7: GROUP MEANS VISUALIZATION
# ==============================================

# FIGURE 6: Boxplot of Group Means
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Group', y='Value', palette='husl')
sns.stripplot(data=df, x='Group', y='Value', color='black', alpha=0.5, size=4)
plt.title('Distribution of Values by Group', fontsize=14, fontweight='bold')
plt.xlabel('Group', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(figures_dir, 'group_boxplot.png'), dpi=300, bbox_inches='tight')
plt.show()
print(f"Group boxplot saved to: {os.path.join(figures_dir, 'group_boxplot.png')}")

# FIGURE 7: QQ Plot for Normality Check
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
for idx, group in enumerate(groups):
    row = idx // 2
    col = idx % 2
    group_data = df[df['Group'] == group]['Value']
    stats.probplot(group_data, dist="norm", plot=axes[row, col])
    axes[row, col].set_title(f'QQ Plot: Group {group}', fontsize=12, fontweight='bold')
    axes[row, col].grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(figures_dir, 'qq_plots_by_group.png'), dpi=300, bbox_inches='tight')
plt.show()
print(f"QQ plots saved to: {os.path.join(figures_dir, 'qq_plots_by_group.png')}")

# FIGURE 8: Density Plot
plt.figure(figsize=(10, 6))
for group in groups:
    group_data = df[df['Group'] == group]['Value']
    sns.kdeplot(group_data, label=f'Group {group}', linewidth=2)
plt.title('Density Plots by Group', fontsize=14, fontweight='bold')
plt.xlabel('Value', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(figures_dir, 'group_density_plots.png'), dpi=300, bbox_inches='tight')
plt.show()
print(f"Density plots saved to: {os.path.join(figures_dir, 'group_density_plots.png')}")

# FIGURE 9: Pairwise Differences Heatmap
pairwise_diff = pd.DataFrame(index=groups, columns=groups)
for g1 in groups:
    for g2 in groups:
        if g1 == g2:
            pairwise_diff.loc[g1, g2] = 0
        else:
            diff = df[df['Group'] == g1]['Value'].mean() - df[df['Group'] == g2]['Value'].mean()
            pairwise_diff.loc[g1, g2] = diff

pairwise_diff = pairwise_diff.astype(float)

plt.figure(figsize=(8, 6))
sns.heatmap(pairwise_diff, annot=True, fmt='.2f', cmap='RdBu_r', 
            center=0, square=True, linewidths=0.5,
            cbar_kws={'label': 'Mean Difference'})
plt.title('Pairwise Mean Differences Between Groups', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(figures_dir, 'pairwise_mean_differences.png'), dpi=300, bbox_inches='tight')
plt.show()
print(f"Pairwise differences heatmap saved to: {os.path.join(figures_dir, 'pairwise_mean_differences.png')}")

# ==============================================
# SECTION 8: SUMMARY STATISTICS
# ==============================================

print("\n" + "="*50)
print("SUMMARY OF FINDINGS")
print("="*50)
print(f"Global ANOVA F-test: p = {anova_table['PR(>F)'].iloc[0]:.6f}")
print(f"Number of significant pairs (Tukey HSD): {sum(tukey_results.reject)}")
print(f"Number of significant pairs (Bonferroni): {sum(reject_bonf)}")
print("\nTukey HSD is less conservative than Bonferroni, identifying more significant differences.")

# Summary statistics table
summary_stats = df.groupby('Group')['Value'].agg(['count', 'mean', 'std', 'min', 'max']).round(3)
print("\n" + "="*50)
print("SUMMARY STATISTICS BY GROUP")
print("="*50)
display(summary_stats)

# Save summary statistics
summary_stats.to_csv(os.path.join(figures_dir, 'summary_statistics.csv'))
print(f"\nSummary statistics saved to: {os.path.join(figures_dir, 'summary_statistics.csv')}")

# Save the complete dataset
df.to_csv(os.path.join(figures_dir, 'experimental_data.csv'), index=False)
print(f"Complete dataset saved to: {os.path.join(figures_dir, 'experimental_data.csv')}")

# FIGURE 10: All Figures Combined Overview
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# Boxplot
sns.boxplot(data=df, x='Group', y='Value', ax=axes[0, 0], palette='husl')
axes[0, 0].set_title('Boxplot by Group', fontsize=12, fontweight='bold')
axes[0, 0].grid(True, alpha=0.3)

# Density plots
for group in groups:
    group_data = df[df['Group'] == group]['Value']
    sns.kdeplot(group_data, label=f'Group {group}', ax=axes[0, 1], linewidth=2)
axes[0, 1].set_title('Density Plots', fontsize=12, fontweight='bold')
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)

# Tukey HSD heatmap
sns.heatmap(tukey_matrix, annot=True, fmt='.3f', cmap='RdYlGn_r',
            ax=axes[1, 0], square=True, linewidths=0.5, vmin=0, vmax=0.1)
axes[1, 0].set_title('Tukey HSD P-values', fontsize=12, fontweight='bold')

# Significance matrix
sns.heatmap(sig_matrix, annot=True, fmt='d', cmap=['lightgreen', 'red'],
            ax=axes[1, 1], square=True, linewidths=0.5, cbar=False)
axes[1, 1].set_title('Significant Differences (p < 0.05)', fontsize=12, fontweight='bold')

plt.suptitle('Design of Experiments: Complete Analysis Overview', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(figures_dir, 'analysis_overview.png'), dpi=300, bbox_inches='tight')
plt.show()
print(f"Analysis overview saved to: {os.path.join(figures_dir, 'analysis_overview.png')}")

print("\n" + "="*50)
print("ALL FIGURES HAVE BEEN SUCCESSFULLY EXPORTED")
print("="*50)
print(f"Figures saved in: {os.path.abspath(figures_dir)}")
print("\nList of saved files:")
for file in sorted(os.listdir(figures_dir)):
    if file.endswith(('.png', '.csv')):
        print(f"  - {file}")