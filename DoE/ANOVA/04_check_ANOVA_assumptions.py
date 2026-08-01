# Import visualization libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import levene, shapiro

method_A = np.random.normal(loc=75, scale=5, size=30)
method_B = np.random.normal(loc=80, scale=5, size=30)
method_C = np.random.normal(loc=85, scale=5, size=30)

# Create a DataFrame
df = pd.DataFrame({
    "Score": np.concatenate([method_A, method_B, method_C]),
    "Method": (["A"] * 30) + (["B"] * 30) + (["C"] * 30)
})


# Homogeneity of variances (Levene's Test)
levene_stat, levene_p = levene(method_A, method_B, method_C)
print(f"Levene's Test p-value: {levene_p:.4f}")

# Normality (Shapiro-Wilk Test) for one group
shapiro_stat, shapiro_p = shapiro(method_A)
print(f"Shapiro-Wilk Test p-value (Method A): {shapiro_p:.4f}")