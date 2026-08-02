"""
DoE Lecture 6
BIBD and Split Plot Design

Case Studies:
1. Balanced Incomplete Block Design
2. Split Plot Design

Author: DoE Learning Lab
"""

import os
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

import joblib

# ==========================================================
# Create folders
# ==========================================================

os.makedirs("./figures", exist_ok=True)
os.makedirs("./models", exist_ok=True)

# ==========================================================
# PART 1
# BIBD CASE STUDY
# ==========================================================

print("\n========== BIBD CASE STUDY ==========")

"""
Research Question:

Which crop variety gives the highest yield?

Treatments:
A,B,C,D

Blocks:
Fields

Constraint:
Each field cannot contain all varieties.

"""

# BIBD Design Matrix

bibd = pd.DataFrame({

    "Block":[
        "Field1",
        "Field1",
        "Field1",

        "Field2",
        "Field2",
        "Field2",

        "Field3",
        "Field3",
        "Field3",

        "Field4",
        "Field4",
        "Field4"
    ],

    "Treatment":[

        "A",
        "B",
        "C",

        "A",
        "B",
        "D",

        "A",
        "C",
        "D",

        "B",
        "C",
        "D"
    ]

})

print(bibd)

# ----------------------------------------------------------
# Visualize BIBD Layout
# ----------------------------------------------------------

plt.figure(figsize=(8,5))

pivot = bibd.assign(Value=1).pivot(
    index="Block",
    columns="Treatment",
    values="Value"
)

sns.heatmap(
    pivot,
    annot=True,
    cmap="Blues",
    cbar=False
)

plt.title(
    "BIBD Experimental Layout\n"
    "X = Treatment Assigned"
)

plt.tight_layout()

plt.savefig(
    "./figures/bibd_layout.png",
    dpi=300
)

plt.close()

# ----------------------------------------------------------
# Simulate Yield Data
# ----------------------------------------------------------

np.random.seed(42)

treatment_effects = {

    "A":10,
    "B":14,
    "C":18,
    "D":22

}

block_effects = {

    "Field1":5,
    "Field2":0,
    "Field3":-3,
    "Field4":7

}

responses=[]

for _,row in bibd.iterrows():

    y = (
        50
        +
        treatment_effects[row.Treatment]
        +
        block_effects[row.Block]
        +
        np.random.normal(0,2)
    )

    responses.append(y)

bibd["Yield"]=responses

print(bibd)

# ----------------------------------------------------------
# BIBD ANOVA
# ----------------------------------------------------------

bibd_model = ols(
    "Yield ~ C(Treatment)+C(Block)",
    data=bibd
).fit()

anova_bibd = anova_lm(
    bibd_model
)

print(anova_bibd)

# Save model

joblib.dump(
    bibd_model,
    "./models/bibd_model.pkl"
)

# ----------------------------------------------------------
# Treatment Effect Plot
# ----------------------------------------------------------

plt.figure(figsize=(7,5))

sns.boxplot(
    data=bibd,
    x="Treatment",
    y="Yield"
)

plt.title(
    "BIBD Treatment Performance"
)

plt.tight_layout()

plt.savefig(
    "./figures/bibd_treatment_effects.png",
    dpi=300
)

plt.close()

# ==========================================================
# PART 2
# SPLIT PLOT DESIGN
# ==========================================================

print("\n========== SPLIT PLOT CASE STUDY ==========")

"""
Research Question:

How do temperature and fertilizer affect crop yield?

Whole plot factor:
Temperature
(Hard to change)

Sub plot factor:
Fertilizer
(Easy to change)

"""

temperature=[
    "Low",
    "High"
]

fertilizers=[
    "A",
    "B",
    "C"
]

blocks=[
    "Farm1",
    "Farm2",
    "Farm3"
]

data=[]

np.random.seed(20)

for block in blocks:

    for temp in temperature:

        for fert in fertilizers:

            base=100

            temp_effect={

                "Low":0,
                "High":15

            }

            fert_effect={

                "A":5,
                "B":10,
                "C":20

            }

            interaction=0

            if temp=="High" and fert=="C":

                interaction=8

            yield_value = (

                base
                +
                temp_effect[temp]
                +
                fert_effect[fert]
                +
                interaction
                +
                np.random.normal(0,3)

            )

            data.append([

                block,
                temp,
                fert,
                yield_value

            ])

splitplot=pd.DataFrame(
    data,
    columns=[
        "Block",
        "Temperature",
        "Fertilizer",
        "Yield"
    ]
)

print(splitplot)

# ----------------------------------------------------------
# Split Plot Visualization
# ----------------------------------------------------------

plt.figure(figsize=(9,6))

sns.barplot(
    data=splitplot,
    x="Temperature",
    y="Yield",
    hue="Fertilizer"
)

plt.title(
    "Split Plot Design\nTemperature × Fertilizer"
)

plt.tight_layout()

plt.savefig(
    "./figures/splitplot_layout.png",
    dpi=300
)

plt.close()

# ----------------------------------------------------------
# Interaction Plot
# ----------------------------------------------------------

plt.figure(figsize=(8,5))

sns.pointplot(
    data=splitplot,
    x="Temperature",
    y="Yield",
    hue="Fertilizer"
)

plt.title(
    "Temperature-Fertilizer Interaction"
)

plt.tight_layout()

plt.savefig(
    "./figures/splitplot_interaction.png",
    dpi=300
)

plt.close()

# ----------------------------------------------------------
# Split Plot ANOVA
# ----------------------------------------------------------

split_model = ols(
    """
    Yield ~
    C(Block)
    +
    C(Temperature)
    *
    C(Fertilizer)
    """,
    data=splitplot
).fit()

anova_split = anova_lm(
    split_model
)

print(anova_split)

# Save model

joblib.dump(
    split_model,
    "./models/splitplot_model.pkl"
)

# ----------------------------------------------------------
# ANOVA Visualization
# ----------------------------------------------------------

plt.figure(figsize=(8,5))

anova_split["F"].dropna().plot(
    kind="bar"
)

plt.title(
    "Split Plot ANOVA F Statistics"
)

plt.ylabel(
    "F value"
)

plt.tight_layout()

plt.savefig(
    "./figures/splitplot_anova.png",
    dpi=300
)

plt.close()

print("\nFinished!")
print("Figures saved in ./figures")
print("Models saved in ./models")