# Import libraries
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import numpy as np

method_A = np.random.normal(loc=75, scale=5, size=30)
method_B = np.random.normal(loc=80, scale=5, size=30)
method_C = np.random.normal(loc=85, scale=5, size=30)

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