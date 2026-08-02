Here is the `EXPLAIN_CODE.md` file. It provides a comprehensive, section-by-section breakdown of the script, with special emphasis on the newly added features for saving figures and text outputs.

# Two-Way ANOVA Complete Case Study: Code Explanation

This document explains the structure, purpose, and functionality of the Python script for conducting a **Two-Way ANOVA** (Analysis of Variance). The script simulates an agricultural experiment to test the effects of **Fertilizer Type** and **Water Level** on **Plant Height**, including their interaction.

---

## 📦 1. Imported Libraries
The script relies on standard data science and statistical libraries:
- **`os`**: Handles operating system interactions, specifically creating directories for saving files.
- **`numpy` (`np`)**: Generates random data and handles numerical operations.
- **`pandas` (`pd`)**: Creates and manipulates the tabular dataset (DataFrame).
- **`matplotlib.pyplot` (`plt`) & `seaborn` (`sns`)**: Used for creating high-quality statistical visualizations.
- **`scipy.stats`**: Provides classical statistical tests (Shapiro-Wilk, Levene's).
- **`statsmodels` (`sm`, `ols`)**: Fits the Ordinary Least Squares (OLS) regression model and generates the ANOVA table.
- **`pingouin` (`pg`)**: A user-friendly statistical package used here for effect sizes (Partial Eta Squared) and Post-Hoc Tukey HSD tests.

---

## 📝 Step-by-Step Code Breakdown

### Section 1: Create Experimental Data
- **Purpose**: Simulates a realistic dataset.
- **How it works**: 
  - Defines 3 fertilizers and 3 water levels.
  - Assigns baseline values, main effects, and specific interaction effects (e.g., "Mixed" fertilizer + "High" water gives an extra boost).
  - Uses a nested loop to generate 5 replicates per group (3 × 3 × 5 = 45 total observations), adding random normal noise (`np.random.normal(0, 3)`) to simulate real-world variance.

### Section 2: Exploratory Data Analysis (EDA)
- **Purpose**: Get a quick look at the data structure.
- **How it works**: Uses `df.groupby()` to calculate and display the mean plant height for every Fertilizer × Water combination in a clean, unstacked table.

### Section 3: Visualization *(Includes New Save Feature)*
- **Purpose**: Visually assess main effects and interactions.
- **How it works**: 
  - Creates a 1×2 grid of subplots: a **Boxplot** (to show distribution and spread) and an **Interaction Plot** (pointplot with standard deviation error bars to visualize crossing/non-crossing lines).
  - **🆕 New Addition**: 
    ```python
    os.makedirs('./figures', exist_ok=True)
    fig.savefig('./figures/fertilizer_water_analysis.png', dpi=300, bbox_inches='tight')
    ```
    This automatically creates a `figures` folder in the current directory (if it doesn't exist) and saves the plot as a high-resolution (300 DPI) PNG file before displaying it.

### Section 4: Check ANOVA Assumptions
- **Purpose**: Validate that the data meets the requirements for ANOVA.
- **How it works**:
  1. **Independence**: Assumed based on the experimental design (randomized replicates).
  2. **Normality**: Uses the **Shapiro-Wilk test** on the model residuals. A p-value > 0.05 indicates the residuals are approximately normally distributed.
  3. **Homogeneity of Variance**: Uses **Levene’s Test** across all groups. A p-value > 0.05 indicates equal variances (homoscedasticity).

### Section 5: Two-Way ANOVA
- **Purpose**: Test for statistically significant effects.
- **How it works**: Fits an OLS model (`Height ~ C(Fertilizer) * C(Water)`), where `C()` denotes categorical variables and `*` includes both main effects and their interaction. It then generates a Type 2 ANOVA table using `sm.stats.anova_lm`.

### Section 6: Results Interpretation
- **Purpose**: Make the ANOVA table easy to read.
- **How it works**: Iterates through the ANOVA table rows, checks if the p-value (`PR(>F)`) is less than `alpha = 0.05`, and prints a human-readable "Significant" or "Not significant" statement for each factor.

### Section 7: Effect Size
- **Purpose**: Determine the *magnitude* of the effects, not just statistical significance.
- **How it works**: Uses `pingouin.anova` to calculate **Partial Eta Squared (`np2`)**. Values closer to 1 indicate a larger proportion of variance in plant height is explained by that factor.

### Section 8: Post-Hoc Tests
- **Purpose**: Identify *which specific groups* differ from each other if a main effect is significant.
- **How it works**: Conditionally runs **Tukey’s HSD** (Honest Significant Difference) test via `pingouin.pairwise_tukey` *only* if the main effect p-value is < 0.05. This prevents unnecessary multiple-comparison penalties.

### Section 9: Model Summary
- **Purpose**: Provide detailed regression statistics.
- **How it works**: Prints the full `model.summary()`, which includes R-squared, coefficients for each dummy variable, standard errors, and individual t-tests for each level compared to the baseline.

### Section 10: Export Results *(Includes New Save Feature)*
- **Purpose**: Save a permanent, readable record of the analysis.
- **How it works**: 
  - **🆕 New Addition**: Opens a file named `model_anova_results.txt` in write mode (`'w'`).
  - Uses formatted string writing (`f.write()`) to neatly separate the Model Summary, ANOVA Table, Effect Sizes, and Assumption Checks with headers and divider lines.
  - Prints a success message to the console confirming the file was saved.

---

## 🚀 How to Run This Script

1. **Install Dependencies** (if not already installed):
   ```bash
   pip install numpy pandas matplotlib seaborn scipy statsmodels pingouin
   ```
2. **Run the Script**:
   ```bash
   python your_script_name.py
   ```
3. **Check Outputs**:
   - Look in your terminal for the printed results.
   - Check your working directory for a new file: `model_anova_results.txt`.
   - Check your working directory for a new folder: `./figures/`, containing `fertilizer_water_analysis.png`.

---

## 💡 Why These Additions Matter
- **Reproducibility**: Saving the figure and the text output ensures that your analysis can be reviewed, shared, or included in reports without needing to re-run the code.
- **Robustness**: `os.makedirs(..., exist_ok=True)` prevents `FileNotFoundError` crashes if the script is run multiple times or on a new machine.
- **Quality**: `dpi=300` and `bbox_inches='tight'` ensure the saved image is publication-ready and no labels are cut off.
```