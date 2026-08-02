"""
Lecture 7
Nested Factors and ANCOVA

Case Study

A fertilizer company wants to compare three fertilizers.

Each fertilizer is tested in different farms.

Each farm belongs ONLY to one fertilizer.

Thus:

Farm is NESTED inside Fertilizer.

Afterward,

they realize plant height before treatment influences yield.

Therefore ANCOVA is used using initial height as covariate.

"""

import os
import joblib
import warnings

warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy import stats

import statsmodels.api as sm
import statsmodels.formula.api as smf

# --------------------------------------------------------
# Create folders
# --------------------------------------------------------

os.makedirs("./figures", exist_ok=True)
os.makedirs("./models", exist_ok=True)

np.random.seed(42)

###############################################################
# PART 1
# Generate Nested Design Dataset
###############################################################

fertilizers = ["A","B","C"]

farms = {
    "A":["A1","A2","A3"],
    "B":["B1","B2","B3"],
    "C":["C1","C2","C3"]
}

rows=[]

for fert in fertilizers:

    fert_effect={
        "A":5,
        "B":10,
        "C":15
    }[fert]

    for farm in farms[fert]:

        farm_effect=np.random.normal(0,2)

        for i in range(15):

            yield_value=(
                60
                + fert_effect
                + farm_effect
                + np.random.normal(0,4)
            )

            rows.append([
                fert,
                farm,
                yield_value
            ])

nested_df=pd.DataFrame(
    rows,
    columns=[
        "Fertilizer",
        "Farm",
        "Yield"
    ]
)

print(nested_df.head())

###############################################################
# Visualization 1
###############################################################

fig,ax=plt.subplots(figsize=(10,6))

nested_df.boxplot(
    column="Yield",
    by="Farm",
    ax=ax
)

plt.suptitle("")
plt.title("Yield by Farm (Nested in Fertilizer)")
plt.tight_layout()

plt.savefig("./figures/nested_boxplot.png",dpi=300)
plt.close()

###############################################################
# Means plot
###############################################################

means=nested_df.groupby("Farm")["Yield"].mean()

plt.figure(figsize=(9,5))

means.plot(marker="o")

plt.ylabel("Mean Yield")
plt.title("Mean Yield for Each Farm")

plt.grid(True)

plt.tight_layout()

plt.savefig("./figures/nested_means.png",dpi=300)
plt.close()

###############################################################
# Nested Model
###############################################################

print("\nNested ANOVA")

nested_model=smf.ols(
    "Yield ~ C(Fertilizer)+C(Fertilizer):C(Farm)",
    data=nested_df
).fit()

anova_nested=sm.stats.anova_lm(
    nested_model,
    typ=2
)

print(anova_nested)

joblib.dump(
    nested_model,
    "./models/nested_model.pkl"
)

###############################################################
# Effect Size
###############################################################

anova_nested["eta_sq"]=(
    anova_nested["sum_sq"]/
    anova_nested["sum_sq"].sum()
)

print("\nEffect Size")
print(anova_nested)

###############################################################
# PART 2
# ANCOVA Dataset
###############################################################

rows=[]

for treatment in ["Control","Drug"]:

    effect=0

    if treatment=="Drug":
        effect=8

    for i in range(80):

        initial=np.random.normal(50,8)

        final=(
            20
            +0.75*initial
            +effect
            +np.random.normal(0,5)
        )

        rows.append([
            treatment,
            initial,
            final
        ])

ancova_df=pd.DataFrame(
    rows,
    columns=[
        "Treatment",
        "InitialHeight",
        "FinalYield"
    ]
)

###############################################################
# Scatter Plot
###############################################################

colors={
    "Control":"blue",
    "Drug":"red"
}

plt.figure(figsize=(8,6))

for t in ancova_df.Treatment.unique():

    subset=ancova_df[
        ancova_df.Treatment==t
    ]

    plt.scatter(
        subset.InitialHeight,
        subset.FinalYield,
        label=t,
        alpha=.7
    )

plt.legend()

plt.xlabel("Initial Height")
plt.ylabel("Final Yield")

plt.title("ANCOVA Scatter")

plt.tight_layout()

plt.savefig("./figures/ancova_scatter.png",dpi=300)
plt.close()

###############################################################
# ANCOVA MODEL
###############################################################

ancova_model=smf.ols(
    "FinalYield~InitialHeight+C(Treatment)",
    data=ancova_df
).fit()

print("\nANCOVA SUMMARY")

print(ancova_model.summary())

joblib.dump(
    ancova_model,
    "./models/ancova_model.pkl"
)

###############################################################
# Regression Lines
###############################################################

plt.figure(figsize=(8,6))

for t in ancova_df.Treatment.unique():

    subset=ancova_df[
        ancova_df.Treatment==t
    ]

    plt.scatter(
        subset.InitialHeight,
        subset.FinalYield,
        alpha=.6,
        label=t
    )

x=np.linspace(
    ancova_df.InitialHeight.min(),
    ancova_df.InitialHeight.max(),
    100
)

control=pd.DataFrame({
    "InitialHeight":x,
    "Treatment":"Control"
})

drug=pd.DataFrame({
    "InitialHeight":x,
    "Treatment":"Drug"
})

plt.plot(
    x,
    ancova_model.predict(control),
    linewidth=3
)

plt.plot(
    x,
    ancova_model.predict(drug),
    linewidth=3
)

plt.legend()

plt.xlabel("Initial Height")
plt.ylabel("Final Yield")

plt.title("ANCOVA Regression Lines")

plt.tight_layout()

plt.savefig(
    "./figures/ancova_regression_lines.png",
    dpi=300
)

plt.close()

###############################################################
# Residual Diagnostics
###############################################################

res=ancova_model.resid
fit=ancova_model.fittedvalues

plt.figure(figsize=(7,5))

plt.hist(
    res,
    bins=15
)

plt.title("Residual Histogram")

plt.tight_layout()

plt.savefig("./figures/residuals_hist.png",dpi=300)
plt.close()

###############################################################

plt.figure(figsize=(6,6))

stats.probplot(
    res,
    dist="norm",
    plot=plt
)

plt.title("QQ Plot")

plt.tight_layout()

plt.savefig("./figures/qqplot.png",dpi=300)
plt.close()

###############################################################

plt.figure(figsize=(7,5))

plt.scatter(
    fit,
    res
)

plt.axhline(
    0,
    color="red"
)

plt.xlabel("Fitted")

plt.ylabel("Residual")

plt.title("Residual vs Fitted")

plt.tight_layout()

plt.savefig(
    "./figures/residual_vs_fitted.png",
    dpi=300
)

plt.close()

###############################################################
# Assumption Tests
###############################################################

print("\nShapiro Test")

print(
    stats.shapiro(res)
)

print("\nBreusch-Pagan")

from statsmodels.stats.diagnostic import het_breuschpagan

bp=het_breuschpagan(
    res,
    ancova_model.model.exog
)

print(bp)

###############################################################
# Predictions
###############################################################

new=pd.DataFrame({

    "InitialHeight":[45,55,65],

    "Treatment":[
        "Control",
        "Drug",
        "Drug"
    ]
})

pred=ancova_model.predict(new)

print("\nPredictions")

print(
    pd.concat(
        [
            new,
            pred.rename("PredictedYield")
        ],
        axis=1
    )
)

###############################################################
# Interpretation
###############################################################

print("\n=============================")
print("INTERPRETATION")
print("=============================")

print("""
Nested Factors

1. Fertilizer effect compares fertilizer types.

2. Farm is nested because
   each farm belongs to only one fertilizer.

3. Significant Farm effect means variability
   among farms inside fertilizers.

----------------------------

ANCOVA

1. Initial Height is a covariate.

2. Treatment effect is adjusted
   after removing variability due
   to Initial Height.

3. If Treatment p-value < 0.05,
   treatment has significant effect
   after adjustment.

4. InitialHeight coefficient tells
   how much yield changes per unit
   increase in initial height.

""")