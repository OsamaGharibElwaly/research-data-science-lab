#===========================================================
# TWO-WAY ANOVA COMPLETE CASE STUDY
# Fertilizer Type x Water Level
#===========================================================

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
import pingouin as pg

#===========================================================
# 1. CREATE EXPERIMENTAL DATA
#===========================================================

np.random.seed(42)

fertilizers = ["Organic", "Chemical", "Mixed"]
water_levels = ["Low", "Medium", "High"]

# Define effects
fertilizer_effects = {"Organic": 5, "Chemical": 10, "Mixed": 15}
water_effects = {"Low": 0, "Medium": 8, "High": 15}

# Interaction effects (specific combinations)
interaction_effects = {
    ("Mixed", "High"): 8,
    ("Organic", "Low"): -3
}

data = []
for fertilizer in fertilizers:
    for water in water_levels:
        base = 50
        effect = (
            base
            + fertilizer_effects[fertilizer]
            + water_effects[water]
            + interaction_effects.get((fertilizer, water), 0)
        )
        # 5 replicates per group
        for _ in range(5):
            height = effect + np.random.normal(0, 3)
            data.append([fertilizer, water, height])

df = pd.DataFrame(data, columns=["Fertilizer", "Water", "Height"])

print(df.head())
print(f"\nDataset size: {df.shape}")

#===========================================================
# 2. EXPLORATORY DATA ANALYSIS
#===========================================================

print("\nGroup Means:")
print(df.groupby(["Fertilizer", "Water"])["Height"].mean().unstack())

#===========================================================
# 3. VISUALIZATION
#===========================================================

# Create the figures directory if it doesn't exist
os.makedirs('./figures', exist_ok=True)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Boxplot
sns.boxplot(data=df, x="Fertilizer", y="Height", hue="Water", ax=axes[0])
axes[0].set_title("Plant Growth by Fertilizer and Water Level")

# Interaction plot
sns.pointplot(data=df, x="Water", y="Height", hue="Fertilizer", 
              errorbar="sd", ax=axes[1])
axes[1].set_title("Interaction Plot: Fertilizer × Water")

plt.tight_layout()

# Save the figure to the ./figures directory
figure_path = './figures/fertilizer_water_analysis.png'
fig.savefig(figure_path, dpi=300, bbox_inches='tight')
print(f"\nFigure saved to: {figure_path}")

plt.show()

#===========================================================
# 4. CHECK ANOVA ASSUMPTIONS
#===========================================================

print("\n" + "="*50)
print("CHECKING ANOVA ASSUMPTIONS")
print("="*50)

# Fit model
model = ols("Height ~ C(Fertilizer) * C(Water)", data=df).fit()
residuals = model.resid

# Assumption 1: Independence (design-based)
print("\nIndependence: Assumed from experimental design")

# Assumption 2: Normality of residuals
shapiro_stat, shapiro_p = stats.shapiro(residuals)
print(f"\nShapiro-Wilk Test: statistic={shapiro_stat:.4f}, p-value={shapiro_p:.4f}")
print(f"Residuals are {'approximately normal' if shapiro_p > 0.05 else 'not normal'}")

# Assumption 3: Homogeneity of variance
groups = [group["Height"].values for _, group in df.groupby(["Fertilizer", "Water"])]
levene_stat, levene_p = stats.levene(*groups)
print(f"\nLevene Test: statistic={levene_stat:.4f}, p-value={levene_p:.4f}")
print(f"Variances are {'equal' if levene_p > 0.05 else 'different'}")

#===========================================================
# 5. TWO-WAY ANOVA
#===========================================================

print("\n" + "="*50)
print("TWO-WAY ANOVA RESULTS")
print("="*50)

anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

#===========================================================
# 6. RESULTS INTERPRETATION
#===========================================================

print("\n" + "="*50)
print("INTERPRETATION")
print("="*50)

alpha = 0.05
for effect in anova_table.index:
    p_val = anova_table.loc[effect, "PR(>F)"]
    significance = "Significant" if p_val < alpha else "Not significant"
    print(f"{effect}: {significance} (p={p_val:.4f})")

#===========================================================
# 7. EFFECT SIZE
#===========================================================

print("\n" + "="*50)
print("EFFECT SIZE (Partial Eta Squared)")
print("="*50)

effect_size = pg.anova(data=df, dv="Height", between=["Fertilizer", "Water"], detailed=True)

# 🛠️ FIX: Changed "p-unc" to "p_unc" (underscore) and "df" to "DF" (uppercase)
print(effect_size[["Source", "SS", "DF", "F", "p_unc", "np2"]])

#===========================================================
# 8. POST-HOC TESTS
#===========================================================

print("\n" + "="*50)
print("POST-HOC ANALYSIS (Tukey HSD)")
print("="*50)

# Only run post-hoc if main effect is significant
if anova_table.loc["C(Fertilizer)", "PR(>F)"] < alpha:
    print("\nFertilizer Comparison:")
    tukey_fertilizer = pg.pairwise_tukey(data=df, dv="Height", between="Fertilizer")
    # 🛠️ FIX: Pingouin uses 'mean_A', 'mean_B', and 'p_tukey' (all with underscores)
    print(tukey_fertilizer[["A", "B", "mean_A", "mean_B", "diff", "p_tukey"]])

if anova_table.loc["C(Water)", "PR(>F)"] < alpha:
    print("\nWater Level Comparison:")
    tukey_water = pg.pairwise_tukey(data=df, dv="Height", between="Water")
    # 🛠️ FIX: Pingouin uses 'mean_A', 'mean_B', and 'p_tukey' (all with underscores)
    print(tukey_water[["A", "B", "mean_A", "mean_B", "diff", "p_tukey"]])

#===========================================================
# 9. MODEL SUMMARY
#===========================================================

print("\n" + "="*50)
print("REGRESSION MODEL SUMMARY")
print("="*50)
print(model.summary())

#===========================================================
# 10. EXPORT RESULTS
#===========================================================

output_filename = 'model_anova_results.txt'

with open(output_filename, 'w') as f:
    f.write("="*60 + "\n")
    f.write("TWO-WAY ANOVA COMPLETE CASE STUDY - MODEL & RESULTS\n")
    f.write("="*60 + "\n\n")
    
    f.write("1. REGRESSION MODEL SUMMARY\n")
    f.write("-" * 60 + "\n")
    f.write(str(model.summary()))
    f.write("\n\n")
    
    f.write("2. ANOVA TABLE\n")
    f.write("-" * 60 + "\n")
    f.write(str(anova_table))
    f.write("\n\n")
    
    f.write("3. EFFECT SIZE (Partial Eta Squared)\n")
    f.write("-" * 60 + "\n")
    # Note: pg.anova uses 'DF' (uppercase) and 'p_unc' (underscore)
    f.write(str(effect_size[["Source", "SS", "DF", "F", "p_unc", "np2"]]))
    f.write("\n\n")
    
    f.write("4. POST-HOC TESTS (Tukey HSD)\n")
    f.write("-" * 60 + "\n")
    
    if anova_table.loc["C(Fertilizer)", "PR(>F)"] < alpha:
        f.write("Fertilizer Comparison:\n")
        f.write(str(tukey_fertilizer[["A", "B", "mean_A", "mean_B", "diff", "p_tukey"]]))
        f.write("\n\n")
        
    if anova_table.loc["C(Water)", "PR(>F)"] < alpha:
        f.write("Water Level Comparison:\n")
        f.write(str(tukey_water[["A", "B", "mean_A", "mean_B", "diff", "p_tukey"]]))
        f.write("\n\n")
    
    f.write("5. ASSUMPTIONS CHECK\n")
    f.write("-" * 60 + "\n")
    f.write(f"Shapiro-Wilk Test (Normality): statistic={shapiro_stat:.4f}, p-value={shapiro_p:.4f}\n")
    f.write(f"Levene Test (Homogeneity of Variance): statistic={levene_stat:.4f}, p-value={levene_p:.4f}\n")

print(f"\n✅ Results and model summary successfully saved to '{output_filename}'")