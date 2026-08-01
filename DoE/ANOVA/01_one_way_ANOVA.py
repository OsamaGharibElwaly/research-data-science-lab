# Import libraries
import numpy as np
import pandas as pd
from scipy import stats

# Set a random seed for reproducibility
np.random.seed(42)

# Simulated exam scores from three teaching methods
method_A = np.random.normal(loc=75, scale=5, size=30)
method_B = np.random.normal(loc=80, scale=5, size=30)
method_C = np.random.normal(loc=85, scale=5, size=30)

# Perform One-Way ANOVA
f_statistic, p_value = stats.f_oneway(method_A, method_B, method_C)

print(f"F-statistic: {f_statistic:.3f}")
print(f"P-value: {p_value:.6f}")

# Interpret the result
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: At least one group mean differs.")
else:
    print("Fail to reject the null hypothesis: No significant difference.")

# =============================

# Import libraries
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Create a DataFrame
df = pd.DataFrame({
    "Score": np.concatenate([method_A, method_B, method_C]),
    "Method": (["A"] * 30) + (["B"] * 30) + (["C"] * 30)
})

# Fit an ordinary least squares (OLS) model
model = ols("Score ~ C(Method)", data=df).fit()

# Generate the ANOVA table
anova_table = sm.stats.anova_lm(model, typ=2)

print(anova_table)