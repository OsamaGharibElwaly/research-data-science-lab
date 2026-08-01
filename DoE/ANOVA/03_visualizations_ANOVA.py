# Import visualization libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

method_A = np.random.normal(loc=75, scale=5, size=30)
method_B = np.random.normal(loc=80, scale=5, size=30)
method_C = np.random.normal(loc=85, scale=5, size=30)

# Create a DataFrame
df = pd.DataFrame({
    "Score": np.concatenate([method_A, method_B, method_C]),
    "Method": (["A"] * 30) + (["B"] * 30) + (["C"] * 30)
})

# Create a boxplot to compare score distributions
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Method", y="Score")
plt.title("Exam Scores by Teaching Method")
plt.xlabel("Teaching Method")
plt.ylabel("Exam Score")
plt.show()