import os
import numpy as np
import matplotlib.pyplot as plt

# Create figures folder
os.makedirs("./figures", exist_ok=True)

# -----------------------------
# Example: RCBD Experiment
# -----------------------------

# Treatments
treatments = ["A", "B", "C", "D"]

# Randomized Complete Block Design layout
rcbd = {
    "Block 1": ["A", "C", "D", "B"],
    "Block 2": ["D", "A", "B", "C"],
    "Block 3": ["C", "D", "A", "B"],
    "Block 4": ["B", "C", "A", "D"]
}


# -----------------------------
# Figure 1: RCBD Layout
# -----------------------------

fig, ax = plt.subplots(figsize=(8, 5))

colors = {
    "A": "lightgreen",
    "B": "lightblue",
    "C": "orange",
    "D": "pink"
}

for row, (block, values) in enumerate(rcbd.items()):

    for col, treatment in enumerate(values):

        ax.add_patch(
            plt.Rectangle(
                (col, -row),
                1,
                1,
                facecolor=colors[treatment],
                edgecolor="black"
            )
        )

        ax.text(
            col + 0.5,
            -row + 0.5,
            treatment,
            ha="center",
            va="center",
            fontsize=14
        )

    ax.text(
        -0.8,
        -row + 0.5,
        block,
        fontsize=12,
        va="center"
    )


ax.set_xlim(-1.5, 4)
ax.set_ylim(-4.5, 1)

ax.set_title(
    "Randomized Complete Block Design (RCBD)\n"
    "Each Block Contains All Treatments"
)

ax.axis("off")

plt.savefig(
    "./figures/rcbd_layout.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# -----------------------------
# Example Data
# -----------------------------

data = {
    "A": [82, 85, 83, 84],
    "B": [75, 78, 77, 76],
    "C": [88, 90, 89, 91],
    "D": [80, 81, 82, 83]
}


# -----------------------------
# Figure 2: Treatment Means
# -----------------------------

means = [
    np.mean(data[t])
    for t in treatments
]


plt.figure(figsize=(7, 4))

plt.bar(
    treatments,
    means
)

plt.xlabel("Treatment")
plt.ylabel("Average Yield")

plt.title(
    "RCBD Treatment Comparison\n"
    "Mean Response After Blocking"
)

plt.savefig(
    "./figures/treatment_means.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# -----------------------------
# Figure 3: Block Effect
# -----------------------------

block_means = []

for block, values in rcbd.items():

    block_values = []

    for treatment in values:
        block_values.append(
            data[treatment][list(rcbd.keys()).index(block)]
        )

    block_means.append(
        np.mean(block_values)
    )


plt.figure(figsize=(7,4))

plt.plot(
    list(rcbd.keys()),
    block_means,
    marker="o"
)

plt.xlabel("Blocks")
plt.ylabel("Average Response")

plt.title(
    "Block Effect in RCBD"
)

plt.savefig(
    "./figures/block_effect.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


print("Figures saved successfully in ./figures/")