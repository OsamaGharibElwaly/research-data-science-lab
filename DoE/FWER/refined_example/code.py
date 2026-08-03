#!/usr/bin/env python3
"""
DoE Lecture 8: Multiple Testing with Family-Wise Error Rate (FWER)
===================================================================
A comprehensive, production-ready implementation for teaching multiple 
hypothesis testing corrections in experimental design.

Features:
    - Object-oriented architecture with clean separation of concerns
    - Configurable experimental parameters via dataclasses
    - Comprehensive logging instead of print statements
    - Type hints throughout for better IDE support
    - Modular visualization system
    - Monte Carlo simulation engine
    - Support for Bonferroni, Holm, Šidák, and Tukey HSD corrections

Usage:
    python lecture8_fwer.py --help
    python lecture8_fwer.py --n-groups 5 --n-per-group 30 --alpha 0.05

Author: Generated
"""

from __future__ import annotations

import argparse
import logging
import os
import sys
import warnings
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.patches import Rectangle
from scipy import stats
from scipy.stats import t, f as f_dist
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multitest import multipletests

# Suppress warnings for cleaner output
warnings.filterwarnings("ignore")

# =============================================================================
# CONFIGURATION & LOGGING
# =============================================================================

@dataclass(frozen=True)
class ExperimentConfig:
    """Configuration for the fertilizer experiment.

    Attributes:
        group_names: Names of experimental groups.
        true_means: True population means for each group.
        n_per_group: Sample size per group.
        std_dev: Common standard deviation across groups.
        alpha: Significance level for hypothesis tests.
        seed: Random seed for reproducibility.
    """
    group_names: Tuple[str, ...] = ("Control", "Organic", "Nitrogen", "Potassium", "Mixed")
    true_means: Tuple[float, ...] = (50.0, 53.0, 55.0, 58.0, 60.0)
    n_per_group: int = 30
    std_dev: float = 4.0
    alpha: float = 0.05
    seed: int = 42

    def __post_init__(self) -> None:
        if len(self.group_names) != len(self.true_means):
            raise ValueError("group_names and true_means must have the same length")
        if self.n_per_group < 2:
            raise ValueError("n_per_group must be at least 2")
        if self.std_dev <= 0:
            raise ValueError("std_dev must be positive")
        if not 0 < self.alpha < 1:
            raise ValueError("alpha must be between 0 and 1")


@dataclass(frozen=True)
class OutputConfig:
    """Configuration for output directories and file formats.

    Attributes:
        figures_dir: Directory for saving figures.
        models_dir: Directory for saving fitted models.
        data_dir: Directory for saving generated data.
        dpi: Resolution for saved figures.
        fig_format: File format for figures (e.g., 'png', 'pdf', 'svg').
    """
    figures_dir: Path = field(default_factory=lambda: Path("figures"))
    models_dir: Path = field(default_factory=lambda: Path("models"))
    data_dir: Path = field(default_factory=lambda: Path("data"))
    dpi: int = 300
    fig_format: str = "png"

    def ensure_dirs(self) -> None:
        """Create output directories if they don't exist."""
        for d in (self.figures_dir, self.models_dir, self.data_dir):
            d.mkdir(parents=True, exist_ok=True)

    def figure_path(self, name: str) -> Path:
        """Return full path for a figure file."""
        return self.figures_dir / f"{name}.{self.fig_format}"

    def model_path(self, name: str) -> Path:
        """Return full path for a model file."""
        return self.models_dir / f"{name}.pkl"

    def data_path(self, name: str) -> Path:
        """Return full path for a data file."""
        return self.data_dir / f"{name}.csv"


def setup_logging(level: int = logging.INFO) -> logging.Logger:
    """Configure and return a logger with colored console output."""
    logger = logging.getLogger("fwer_lecture")
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level)
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(message)s",
            datefmt="%H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


# =============================================================================
# DATA GENERATION
# =============================================================================

class DataGenerator:
    """Generates experimental data for multiple groups."""

    def __init__(self, config: ExperimentConfig, logger: Optional[logging.Logger] = None):
        self.config = config
        self.logger = logger or logging.getLogger("fwer_lecture")
        self._rng = np.random.default_rng(config.seed)

    def generate(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """Generate wide and long-format DataFrames.

        Returns:
            A tuple of (wide_df, long_df) where wide_df has one column per
            group and long_df has 'Fertilizer' and 'Growth' columns.
        """
        self.logger.info("Generating experimental data...")

        data_dict = {
            name: self._rng.normal(mean, self.config.std_dev, self.config.n_per_group)
            for name, mean in zip(self.config.group_names, self.config.true_means)
        }

        wide_df = pd.DataFrame(data_dict)
        long_df = wide_df.melt(var_name="Fertilizer", value_name="Growth")

        self.logger.info(
            f"Generated {self.config.n_per_group} observations per group "
            f"across {len(self.config.group_names)} groups"
        )

        return wide_df, long_df

    def summary_stats(self, long_df: pd.DataFrame) -> pd.DataFrame:
        """Compute summary statistics by group."""
        return long_df.groupby("Fertilizer")["Growth"].agg(
            ["count", "mean", "std", "min", "max"]
        ).round(3)


# =============================================================================
# STATISTICAL ANALYSIS
# =============================================================================

@dataclass
class PairwiseResult:
    """Result container for a single pairwise comparison."""
    group1: str
    group2: str
    mean_diff: float
    t_statistic: float
    p_value: float
    se: float
    df: int


class StatisticalAnalyzer:
    """Performs ANOVA and pairwise comparisons."""

    def __init__(self, alpha: float = 0.05, logger: Optional[logging.Logger] = None):
        self.alpha = alpha
        self.logger = logger or logging.getLogger("fwer_lecture")

    def anova(self, long_df: pd.DataFrame) -> Tuple[Any, pd.DataFrame]:
        """Fit one-way ANOVA model and return fitted model + ANOVA table.

        Args:
            long_df: Long-format DataFrame with 'Fertilizer' and 'Growth'.

        Returns:
            Tuple of (fitted OLS model, ANOVA table as DataFrame).
        """
        self.logger.info("Fitting one-way ANOVA model...")

        model = ols("Growth ~ C(Fertilizer)", data=long_df).fit()
        anova_table = anova_lm(model, typ=2)

        f_stat = anova_table.loc["C(Fertilizer)", "F"]
        p_val = anova_table.loc["C(Fertilizer)", "PR(>F)"]

        self.logger.info(f"ANOVA F={f_stat:.3f}, p={p_val:.4f}")
        self.logger.info(
            f"Significant at α={self.alpha}: {'Yes' if p_val < self.alpha else 'No'}"
        )

        return model, anova_table

    def pairwise_ttests(self, wide_df: pd.DataFrame, groups: Tuple[str, ...]) -> pd.DataFrame:
        """Compute all pairwise independent t-tests.

        Args:
            wide_df: Wide-format DataFrame with one column per group.
            groups: Tuple of group names.

        Returns:
            DataFrame with columns: Comparison, Group1, Group2, mean_diff,
            t_statistic, p_value, se, df.
        """
        self.logger.info("Computing pairwise t-tests...")

        results: List[Dict[str, Any]] = []
        n = len(wide_df)

        for i in range(len(groups)):
            for j in range(i + 1, len(groups)):
                g1, g2 = groups[i], groups[j]
                x1, x2 = wide_df[g1].values, wide_df[g2].values

                # Welch's t-test (unequal variances allowed)
                t_stat, p_val = stats.ttest_ind(x1, x2, equal_var=False)

                # Standard error
                se1 = x1.std(ddof=1) / np.sqrt(len(x1))
                se2 = x2.std(ddof=1) / np.sqrt(len(x2))
                se = np.sqrt(se1**2 + se2**2)

                # Welch-Satterthwaite degrees of freedom
                var1, var2 = x1.var(ddof=1), x2.var(ddof=1)
                n1, n2 = len(x1), len(x2)
                df = (var1/n1 + var2/n2)**2 / (
                    (var1/n1)**2/(n1-1) + (var2/n2)**2/(n2-1)
                )

                results.append({
                    "Comparison": f"{g1} vs {g2}",
                    "Group1": g1,
                    "Group2": g2,
                    "mean_diff": x1.mean() - x2.mean(),
                    "t_statistic": t_stat,
                    "p_value": p_val,
                    "se": se,
                    "df": df
                })

        results_df = pd.DataFrame(results).sort_values("p_value").reset_index(drop=True)

        self.logger.info(f"Computed {len(results_df)} pairwise comparisons")
        sig_count = (results_df["p_value"] < self.alpha).sum()
        self.logger.info(f"Significant at α={self.alpha}: {sig_count}")

        return results_df

    def apply_corrections(self, results_df: pd.DataFrame) -> pd.DataFrame:
        """Apply multiple testing corrections to pairwise results.

        Corrections applied:
            - Bonferroni: α/m
            - Holm: Step-down Bonferroni
            - Šidák: 1 - (1-α)^(1/m)
            - Benjamini-Hochberg (FDR control, bonus)

        Args:
            results_df: DataFrame from pairwise_ttests().

        Returns:
            Enriched DataFrame with corrected p-values and significance flags.
        """
        self.logger.info("Applying multiple testing corrections...")

        m = len(results_df)
        pvals = results_df["p_value"].values

        # Bonferroni
        alpha_bonf = self.alpha / m
        bonf_p = np.minimum(pvals * m, 1.0)
        bonf_sig = pvals < alpha_bonf

        # Holm
        holm_reject, holm_p, _, _ = multipletests(pvals, alpha=self.alpha, method="holm")

        # Šidák
        alpha_sidak = 1 - (1 - self.alpha) ** (1 / m)
        sidak_p = 1 - (1 - pvals) ** m
        sidak_p = np.minimum(sidak_p, 1.0)
        sidak_sig = pvals < alpha_sidak

        # Benjamini-Hochberg (FDR)
        bh_reject, bh_p, _, _ = multipletests(pvals, alpha=self.alpha, method="fdr_bh")

        results_df = results_df.copy()
        results_df["alpha_bonferroni"] = alpha_bonf
        results_df["p_bonferroni"] = bonf_p
        results_df["sig_bonferroni"] = bonf_sig
        results_df["p_holm"] = holm_p
        results_df["sig_holm"] = holm_reject
        results_df["alpha_sidak"] = alpha_sidak
        results_df["p_sidak"] = sidak_p
        results_df["sig_sidak"] = sidak_sig
        results_df["p_bh"] = bh_p
        results_df["sig_bh"] = bh_reject

        self.logger.info(f"Bonferroni α = {alpha_bonf:.6f}")
        self.logger.info(f"Šidák α = {alpha_sidak:.6f}")
        self.logger.info(
            f"Significant: Bonferroni={bonf_sig.sum()}, "
            f"Holm={holm_reject.sum()}, Šidák={sidak_sig.sum()}, BH={bh_reject.sum()}"
        )

        return results_df

    def tukey_hsd(self, long_df: pd.DataFrame) -> Any:
        """Perform Tukey HSD post-hoc test.

        Args:
            long_df: Long-format DataFrame.

        Returns:
            TukeyHSDResults object or None if error occurs.
        """
        self.logger.info("Performing Tukey HSD...")

        try:
            tukey = pairwise_tukeyhsd(
                long_df["Growth"], 
                long_df["Fertilizer"], 
                alpha=self.alpha
            )
            sig_count = tukey.reject.sum() if hasattr(tukey.reject, "sum") else sum(tukey.reject)
            self.logger.info(f"Tukey HSD significant comparisons: {sig_count}")
            return tukey
        except Exception as e:
            self.logger.error(f"Tukey HSD failed: {e}")
            return None


# =============================================================================
# MONTE CARLO SIMULATION
# =============================================================================

class MonteCarloSimulator:
    """Simulates false positive rates under the null hypothesis."""

    def __init__(
        self,
        n_groups: int = 5,
        n_per_group: int = 30,
        alpha: float = 0.05,
        seed: Optional[int] = None,
        logger: Optional[logging.Logger] = None
    ):
        self.n_groups = n_groups
        self.n_per_group = n_per_group
        self.alpha = alpha
        self.seed = seed
        self.logger = logger or logging.getLogger("fwer_lecture")
        self._rng = np.random.default_rng(seed)

    def run(
        self,
        n_simulations: int = 1000,
        methods: Optional[List[str]] = None
    ) -> pd.DataFrame:
        """Run Monte Carlo simulation.

        Args:
            n_simulations: Number of simulation iterations.
            methods: List of methods to evaluate. Defaults to all.

        Returns:
            DataFrame with FWER estimates for each method.
        """
        methods = methods or ["raw", "bonferroni", "holm", "tukey"]
        self.logger.info(
            f"Running {n_simulations} Monte Carlo simulations "
            f"({self.n_groups} groups, n={self.n_per_group})..."
        )

        n_comparisons = self.n_groups * (self.n_groups - 1) // 2
        results = {m: [] for m in methods}

        for sim in range(n_simulations):
            if (sim + 1) % 100 == 0:
                self.logger.info(f"  Progress: {sim + 1}/{n_simulations}")

            # Generate null data (all means equal)
            data = {
                f"G{i}": self._rng.normal(0, 1, self.n_per_group)
                for i in range(self.n_groups)
            }
            df_wide = pd.DataFrame(data)
            df_long = df_wide.melt(var_name="Group", value_name="Value")

            # Pairwise p-values
            p_values = []
            cols = list(df_wide.columns)
            for i in range(self.n_groups):
                for j in range(i + 1, self.n_groups):
                    _, p = stats.ttest_ind(df_wide[cols[i]], df_wide[cols[j]])
                    p_values.append(p)
            p_values = np.array(p_values)

            # Evaluate each method
            if "raw" in methods:
                results["raw"].append(any(p_values < self.alpha))

            if "bonferroni" in methods:
                results["bonferroni"].append(any(p_values < self.alpha / n_comparisons))

            if "holm" in methods:
                holm_reject, _, _, _ = multipletests(p_values, alpha=self.alpha, method="holm")
                results["holm"].append(any(holm_reject))

            if "tukey" in methods:
                try:
                    tukey = pairwise_tukeyhsd(
                        df_long["Value"], df_long["Group"], alpha=self.alpha
                    )
                    results["tukey"].append(any(tukey.reject))
                except Exception:
                    results["tukey"].append(False)

        # Compile results
        summary = {
            method: np.mean(flags) for method, flags in results.items()
        }

        expected_fwer = 1 - (1 - self.alpha) ** n_comparisons
        self.logger.info(f"Expected FWER (no correction): {expected_fwer:.4f}")
        for method, rate in summary.items():
            self.logger.info(f"  {method}: {rate:.4f}")

        return pd.DataFrame({
            "Method": list(summary.keys()),
            "FWER": list(summary.values()),
            "Expected": [expected_fwer if m == "raw" else self.alpha for m in summary.keys()]
        })


# =============================================================================
# VISUALIZATION SYSTEM
# =============================================================================

class FigureManager:
    """Manages figure creation, styling, and saving."""

    def __init__(self, config: OutputConfig, logger: Optional[logging.Logger] = None):
        self.config = config
        self.logger = logger or logging.getLogger("fwer_lecture")
        self._setup_style()

    def _setup_style(self) -> None:
        """Configure matplotlib and seaborn styling."""
        plt.style.use("seaborn-v0_8-whitegrid")
        sns.set_palette("husl")
        plt.rcParams["figure.dpi"] = 100
        plt.rcParams["savefig.dpi"] = self.config.dpi
        plt.rcParams["font.size"] = 10
        plt.rcParams["axes.titlesize"] = 12
        plt.rcParams["axes.labelsize"] = 10

    def save(self, fig: plt.Figure, name: str) -> Path:
        """Save figure and return the path."""
        path = self.config.figure_path(name)
        fig.savefig(path, bbox_inches="tight", facecolor="white")
        plt.close(fig)
        self.logger.info(f"Saved figure: {path}")
        return path

    def create_figure(self, nrows: int = 1, ncols: int = 1, figsize: Tuple[float, float] = (10, 6)) -> plt.Figure:
        """Create a new figure with the specified layout."""
        return plt.figure(figsize=figsize)


class Visualizer:
    """Creates all lecture visualizations."""

    def __init__(
        self,
        fig_manager: FigureManager,
        exp_config: ExperimentConfig,
        logger: Optional[logging.Logger] = None
    ):
        self.fig = fig_manager
        self.exp = exp_config
        self.logger = logger or logging.getLogger("fwer_lecture")

    # -------------------------------------------------------------------------
    # Distribution Visualizations
    # -------------------------------------------------------------------------

    def plot_distributions(self, wide_df: pd.DataFrame, long_df: pd.DataFrame) -> Path:
        """Create comprehensive distribution plots."""
        self.logger.info("Creating distribution plots...")

        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        groups = list(self.exp.group_names)
        colors = sns.color_palette("husl", len(groups))

        # 1. Overlapping histograms with KDE
        ax = axes[0, 0]
        for group, color in zip(groups, colors):
            ax.hist(wide_df[group], bins=15, alpha=0.4, label=group, 
                   color=color, density=True, edgecolor="black", linewidth=0.5)
            # Add KDE
            from scipy.stats import gaussian_kde
            kde = gaussian_kde(wide_df[group])
            x_range = np.linspace(wide_df[group].min(), wide_df[group].max(), 200)
            ax.plot(x_range, kde(x_range), color=color, linewidth=2)
        ax.set_xlabel("Growth (cm)", fontweight="bold")
        ax.set_ylabel("Density", fontweight="bold")
        ax.set_title("Distribution of Growth by Fertilizer", fontweight="bold")
        ax.legend(frameon=True, fancybox=True, shadow=True)

        # 2. Box plots with swarm overlay
        ax = axes[0, 1]
        sns.boxplot(data=long_df, x="Fertilizer", y="Growth", ax=ax, 
                   palette="husl", width=0.6)
        sns.stripplot(data=long_df, x="Fertilizer", y="Growth", ax=ax,
                     color="black", alpha=0.3, size=3, jitter=True)
        ax.set_title("Box Plots with Individual Points", fontweight="bold")
        ax.set_xlabel("")
        ax.tick_params(axis="x", rotation=30)

        # 3. Means with 95% CI
        ax = axes[1, 0]
        means = wide_df.mean()
        stds = wide_df.std()
        n = len(wide_df)
        ci = 1.96 * stds / np.sqrt(n)

        x_pos = np.arange(len(groups))
        bars = ax.bar(x_pos, means, yerr=ci, capsize=8, alpha=0.8,
                     color=colors, edgecolor="black", linewidth=1)
        ax.set_xticks(x_pos)
        ax.set_xticklabels(groups, rotation=30, ha="right")
        ax.set_ylabel("Mean Growth (cm)", fontweight="bold")
        ax.set_title("Mean Growth with 95% Confidence Intervals", fontweight="bold")
        ax.axhline(y=means.mean(), color="red", linestyle="--", alpha=0.5, label="Grand Mean")
        ax.legend()

        # Add value labels on bars
        for bar, mean, ci_val in zip(bars, means, ci):
            ax.text(bar.get_x() + bar.get_width()/2, mean + ci_val + 0.3,
                   f"{mean:.1f}", ha="center", va="bottom", fontsize=9, fontweight="bold")

        # 4. Violin plots
        ax = axes[1, 1]
        sns.violinplot(data=long_df, x="Fertilizer", y="Growth", ax=ax,
                      palette="husl", inner="box")
        ax.set_title("Violin Plots (Distribution Shape)", fontweight="bold")
        ax.set_xlabel("")
        ax.tick_params(axis="x", rotation=30)

        plt.tight_layout()
        return self.fig.save(fig, "01_distributions")

    # -------------------------------------------------------------------------
    # ANOVA Visualization
    # -------------------------------------------------------------------------

    def plot_anova_table(self, anova_table: pd.DataFrame) -> Path:
        """Visualize ANOVA results as a formatted table."""
        self.logger.info("Creating ANOVA table visualization...")

        fig, ax = plt.subplots(figsize=(10, 4))
        ax.axis("off")

        # Format table data
        cell_text = []
        for idx, row in anova_table.iterrows():
            cell_text.append([
                idx,
                f"{row['sum_sq']:.2f}",
                f"{row['df']:.0f}",
                f"{row.get('mean_sq', row['sum_sq']/row['df']):.2f}",
                f"{row['F']:.3f}",
                f"{row['PR(>F)']:.4f}"
            ])

        table = ax.table(
            cellText=cell_text,
            colLabels=["Source", "SS", "df", "MS", "F", "p-value"],
            cellLoc="center",
            loc="center",
            colColours=["#4472C4"] * 6,
            colWidths=[0.25, 0.15, 0.1, 0.15, 0.15, 0.2]
        )
        table.auto_set_font_size(False)
        table.set_fontsize(11)
        table.scale(1.2, 2)

        # Style header
        for i in range(6):
            table[(0, i)].set_text_props(color="white", fontweight="bold")
            table[(0, i)].set_facecolor("#4472C4")

        # Style rows
        for i in range(1, len(cell_text) + 1):
            for j in range(6):
                table[(i, j)].set_facecolor("#E7E6E6" if i % 2 == 0 else "white")

        ax.set_title("One-Way ANOVA Results", fontsize=14, fontweight="bold", pad=20)
        plt.tight_layout()
        return self.fig.save(fig, "02_anova_table")

    # -------------------------------------------------------------------------
    # Multiple Testing Problem
    # -------------------------------------------------------------------------

    def plot_multiple_testing_problem(self) -> Path:
        """Visualize the multiple testing problem and FWER growth."""
        self.logger.info("Creating multiple testing problem visualization...")

        n_groups = len(self.exp.group_names)
        n_comparisons = n_groups * (n_groups - 1) // 2
        alpha = self.exp.alpha
        fwer = 1 - (1 - alpha) ** n_comparisons

        fig, axes = plt.subplots(1, 2, figsize=(14, 6))

        # Left: Comparison matrix heatmap
        ax = axes[0]
        matrix = np.zeros((n_groups, n_groups))
        comparisons = []
        for i in range(n_groups):
            for j in range(i + 1, n_groups):
                matrix[i, j] = 1
                comparisons.append(f"{self.exp.group_names[i]} vs {self.exp.group_names[j]}")

        im = ax.imshow(matrix, cmap="Blues", aspect="auto", vmin=0, vmax=1)
        ax.set_xticks(range(n_groups))
        ax.set_yticks(range(n_groups))
        ax.set_xticklabels(self.exp.group_names, rotation=45, ha="right")
        ax.set_yticklabels(self.exp.group_names)
        ax.set_title(f"Pairwise Comparison Matrix\n({n_comparisons} total comparisons)", 
                    fontweight="bold")

        for i in range(n_groups):
            for j in range(n_groups):
                if matrix[i, j] == 1:
                    ax.text(j, i, "✓", ha="center", va="center", 
                           color="white", fontsize=16, fontweight="bold")

        # Right: FWER growth curve
        ax = axes[1]
        m_values = np.arange(1, 51)
        fwer_values = 1 - (1 - alpha) ** m_values

        ax.plot(m_values, fwer_values, "b-", linewidth=2.5, 
               label=f"FWER = 1 − (1 − α)ᵐ, α = {alpha}")
        ax.axhline(y=alpha, color="red", linestyle="--", linewidth=2, label=f"α = {alpha}")
        ax.axvline(x=n_comparisons, color="green", linestyle="--", linewidth=2,
                  label=f"m = {n_comparisons} (our experiment)")
        ax.scatter([n_comparisons], [fwer], color="green", s=150, zorder=5, 
                  edgecolors="black", linewidth=2)
        ax.annotate(f"FWER = {fwer:.3f}",
                   xy=(n_comparisons, fwer), xytext=(n_comparisons + 5, fwer + 0.05),
                   fontsize=11, fontweight="bold",
                   bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.8),
                   arrowprops=dict(arrowstyle="->", color="black"))

        ax.set_xlabel("Number of Tests (m)", fontweight="bold")
        ax.set_ylabel("Family-Wise Error Rate (FWER)", fontweight="bold")
        ax.set_title("FWER Inflation Without Correction", fontweight="bold")
        ax.legend(loc="lower right", frameon=True, fancybox=True, shadow=True)
        ax.set_xlim(0, 50)
        ax.set_ylim(0, 1)
        ax.grid(True, alpha=0.3)

        plt.tight_layout()
        return self.fig.save(fig, "03_multiple_testing_problem")

    # -------------------------------------------------------------------------
    # Pairwise Comparisons
    # -------------------------------------------------------------------------

    def plot_raw_pvalues(self, results_df: pd.DataFrame) -> Path:
        """Plot raw p-values from pairwise t-tests."""
        self.logger.info("Creating raw p-values plot...")

        fig, ax = plt.subplots(figsize=(12, 6))

        colors = ["#E74C3C" if p < self.exp.alpha else "#95A5A6" 
                 for p in results_df["p_value"]]

        bars = ax.barh(results_df["Comparison"], results_df["p_value"], color=colors,
                      edgecolor="black", linewidth=0.5)
        ax.axvline(x=self.exp.alpha, color="red", linestyle="--", linewidth=2,
                  label=f"α = {self.exp.alpha}")
        ax.set_xlabel("p-value", fontweight="bold")
        ax.set_title("Raw p-values for Pairwise Comparisons\nRed = Significant", 
                    fontweight="bold")
        ax.legend()
        ax.grid(True, alpha=0.3, axis="x")
        ax.set_xlim(0, max(results_df["p_value"]) * 1.1)

        # Add value labels
        for bar, p in zip(bars, results_df["p_value"]):
            ax.text(p + 0.002, bar.get_y() + bar.get_height()/2,
                   f"{p:.4f}", va="center", fontsize=9)

        plt.tight_layout()
        return self.fig.save(fig, "04_raw_pvalues")

    def plot_correction_comparison(self, results_df: pd.DataFrame) -> Path:
        """Compare all correction methods side-by-side."""
        self.logger.info("Creating correction comparison plot...")

        fig, axes = plt.subplots(1, 2, figsize=(16, 7))

        # Left: Adjusted p-values
        ax = axes[0]
        x = np.arange(len(results_df))
        width = 0.18

        methods = [
            ("Raw", "p_value", "#3498DB"),
            ("Bonferroni", "p_bonferroni", "#E74C3C"),
            ("Holm", "p_holm", "#2ECC71"),
            ("Šidák", "p_sidak", "#F39C12"),
            ("Benjamini-Hochberg", "p_bh", "#9B59B6")
        ]

        for i, (label, col, color) in enumerate(methods):
            offset = (i - 2) * width
            ax.bar(x + offset, results_df[col], width, label=label, color=color,
                  edgecolor="black", linewidth=0.5, alpha=0.85)

        ax.axhline(y=self.exp.alpha, color="red", linestyle="--", linewidth=2,
                  label=f"α = {self.exp.alpha}")
        ax.set_xticks(x)
        ax.set_xticklabels(results_df["Comparison"], rotation=45, ha="right")
        ax.set_ylabel("Adjusted p-value", fontweight="bold")
        ax.set_title("Comparison of Correction Methods", fontweight="bold")
        ax.legend(loc="upper left", frameon=True, fancybox=True, shadow=True, ncol=2)
        ax.grid(True, alpha=0.3, axis="y")

        # Right: Significance matrix
        ax = axes[1]
        sig_cols = ["p_value < 0.05", "sig_bonferroni", "sig_holm", 
                   "sig_sidak", "sig_bh"]
        sig_labels = ["Raw", "Bonferroni", "Holm", "Šidák", "BH (FDR)"]

        sig_matrix = np.array([
            results_df["p_value"] < self.exp.alpha,
            results_df["sig_bonferroni"],
            results_df["sig_holm"],
            results_df["sig_sidak"],
            results_df["sig_bh"]
        ], dtype=int)

        im = ax.imshow(sig_matrix, cmap="RdYlGn", aspect="auto", vmin=0, vmax=1)
        ax.set_yticks(range(len(sig_labels)))
        ax.set_yticklabels(sig_labels)
        ax.set_xticks(range(len(results_df)))
        ax.set_xticklabels(results_df["Comparison"], rotation=90, fontsize=9)
        ax.set_title("Significance Matrix\n(Green = Significant)", fontweight="bold")

        for i in range(sig_matrix.shape[0]):
            for j in range(sig_matrix.shape[1]):
                text = "✓" if sig_matrix[i, j] else "✗"
                color = "white" if sig_matrix[i, j] else "black"
                ax.text(j, i, text, ha="center", va="center", 
                       color=color, fontsize=14, fontweight="bold")

        plt.tight_layout()
        return self.fig.save(fig, "05_correction_comparison")

    # -------------------------------------------------------------------------
    # Tukey HSD
    # -------------------------------------------------------------------------

    def plot_tukey(self, tukey_results: Any) -> Path:
        """Visualize Tukey HSD results."""
        self.logger.info("Creating Tukey HSD visualization...")

        fig, ax = plt.subplots(figsize=(12, 8))

        try:
            n_comp = len(tukey_results.reject)
            y_pos = np.arange(n_comp)

            # Extract data safely
            meandiffs = np.array(tukey_results.meandiffs)
            conf_int = np.array(tukey_results.conf_int)
            reject = np.array(tukey_results.reject)

            ci_lower = conf_int[:, 0]
            ci_upper = conf_int[:, 1]

            colors = ["#E74C3C" if r else "#3498DB" for r in reject]

            for i in range(n_comp):
                ax.errorbar(meandiffs[i], y_pos[i],
                           xerr=[[meandiffs[i] - ci_lower[i]], 
                                [ci_upper[i] - meandiffs[i]]],
                           fmt="o", capsize=8, color=colors[i], 
                           markersize=10, ecolor="gray", alpha=0.8)

            ax.axvline(x=0, color="black", linestyle="-", linewidth=1.5)
            ax.set_yticks(y_pos)

            labels = [f"{g1} vs {g2}" for g1, g2 in 
                     zip(tukey_results.group1, tukey_results.group2)]
            ax.set_yticklabels(labels, fontsize=10)
            ax.set_xlabel("Mean Difference", fontweight="bold")
            ax.set_title("Tukey HSD: Mean Differences with 95% Simultaneous CI\n"
                        "Red = Significant (CI excludes 0)", fontweight="bold")
            ax.grid(True, alpha=0.3, axis="x")

            # Add significance markers
            for i, (rej, diff) in enumerate(zip(reject, meandiffs)):
                if rej:
                    ax.text(diff + 0.3, i, "*", ha="center", va="center",
                           fontsize=24, color="#E74C3C", fontweight="bold")

        except Exception as e:
            self.logger.warning(f"Could not create detailed Tukey plot: {e}")
            ax.text(0.5, 0.5, "Tukey HSD Results\n(Visualization limited)",
                   ha="center", va="center", transform=ax.transAxes, fontsize=14)

        plt.tight_layout()
        return self.fig.save(fig, "06_tukey_hsd")

    # -------------------------------------------------------------------------
    # Monte Carlo Results
    # -------------------------------------------------------------------------

    def plot_monte_carlo(self, mc_results: pd.DataFrame) -> Path:
        """Visualize Monte Carlo simulation results."""
        self.logger.info("Creating Monte Carlo results plot...")

        fig, axes = plt.subplots(1, 2, figsize=(14, 6))

        # Left: FWER bar chart
        ax = axes[0]
        colors = ["#3498DB", "#E74C3C", "#2ECC71", "#F39C12"]
        bars = ax.bar(mc_results["Method"], mc_results["FWER"], 
                     color=colors[:len(mc_results)], edgecolor="black", 
                     linewidth=1, alpha=0.85)

        ax.axhline(y=self.exp.alpha, color="red", linestyle="--", linewidth=2,
                  label=f"Target α = {self.exp.alpha}")
        ax.set_ylabel("Family-Wise Error Rate (FWER)", fontweight="bold")
        ax.set_title("Empirical FWER from Monte Carlo Simulation", fontweight="bold")
        ax.legend()
        ax.grid(True, alpha=0.3, axis="y")
        ax.set_ylim(0, max(mc_results["FWER"]) * 1.2)

        for bar, rate in zip(bars, mc_results["FWER"]):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005,
                   f"{rate:.3f}", ha="center", va="bottom", 
                   fontsize=11, fontweight="bold")

        # Right: FWER growth theoretical curve
        ax = axes[1]
        m_vals = np.linspace(1, 100, 500)
        fwer_vals = 1 - (1 - self.exp.alpha) ** m_vals

        ax.plot(m_vals, fwer_vals, "b-", linewidth=2.5,
               label=f"FWER = 1 − (1 − {self.exp.alpha})ᵐ")
        ax.axhline(y=self.exp.alpha, color="red", linestyle="--", linewidth=2,
                  label=f"α = {self.exp.alpha}")
        ax.axhline(y=0.5, color="orange", linestyle="--", alpha=0.7, label="FWER = 0.50")

        # Highlight key points
        key_m = [1, 5, 10, 20, 50, 100]
        for m in key_m:
            fwer = 1 - (1 - self.exp.alpha) ** m
            ax.scatter([m], [fwer], s=80, color="red", zorder=5, edgecolors="black")
            ax.annotate(f"m={m}\n{fwer:.3f}", xy=(m, fwer),
                       xytext=(10, 10), textcoords="offset points",
                       fontsize=8, alpha=0.8)

        ax.set_xlabel("Number of Tests (m)", fontweight="bold")
        ax.set_ylabel("FWER", fontweight="bold")
        ax.set_title("Theoretical FWER Growth", fontweight="bold")
        ax.legend(loc="lower right")
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 1)
        ax.grid(True, alpha=0.3)

        plt.tight_layout()
        return self.fig.save(fig, "07_monte_carlo")

    # -------------------------------------------------------------------------
    # Confidence Intervals
    # -------------------------------------------------------------------------

    def plot_confidence_intervals(self, results_df: pd.DataFrame) -> Path:
        """Plot confidence intervals for all pairwise comparisons."""
        self.logger.info("Creating confidence interval plot...")

        fig, ax = plt.subplots(figsize=(12, 8))

        # Sort by mean difference for better visualization
        df_sorted = results_df.sort_values("mean_diff").reset_index(drop=True)
        n = len(df_sorted)
        y_pos = np.arange(n)

        # Calculate 95% CI for each comparison
        ci_lower = []
        ci_upper = []

        for _, row in df_sorted.iterrows():
            mean_diff = row["mean_diff"]
            se = row["se"]
            df_val = row["df"]
            t_crit = stats.t.ppf(0.975, df_val)
            margin = t_crit * se
            ci_lower.append(mean_diff - margin)
            ci_upper.append(mean_diff + margin)

        ci_lower = np.array(ci_lower)
        ci_upper = np.array(ci_upper)
        mean_diffs = df_sorted["mean_diff"].values

        colors = ["#E74C3C" if p < self.exp.alpha else "#3498DB" 
                 for p in df_sorted["p_value"]]

        for i in range(n):
            ax.errorbar(mean_diffs[i], y_pos[i],
                       xerr=[[mean_diffs[i] - ci_lower[i]], 
                            [ci_upper[i] - mean_diffs[i]]],
                       fmt="o", capsize=8, color=colors[i], 
                       markersize=10, ecolor="gray", alpha=0.8)

        ax.axvline(x=0, color="black", linestyle="-", linewidth=1.5)
        ax.set_yticks(y_pos)
        ax.set_yticklabels(df_sorted["Comparison"], fontsize=10)
        ax.set_xlabel("Mean Difference", fontweight="bold")
        ax.set_title("95% Confidence Intervals for Pairwise Comparisons\n"
                    "Red = Significant (p < 0.05)", fontweight="bold")
        ax.grid(True, alpha=0.3, axis="x")

        # Add significance stars
        for i, (diff, p) in enumerate(zip(mean_diffs, df_sorted["p_value"])):
            if p < self.exp.alpha:
                ax.text(diff + (ci_upper[i] - diff) + 0.2, i, "*",
                       ha="center", va="center", fontsize=20, 
                       color="#E74C3C", fontweight="bold")

        plt.tight_layout()
        return self.fig.save(fig, "08_confidence_intervals")

    # -------------------------------------------------------------------------
    # Decision Flow Diagram
    # -------------------------------------------------------------------------

    def plot_decision_flow(self) -> Path:
        """Create a decision flow diagram for multiple testing."""
        self.logger.info("Creating decision flow diagram...")

        fig, ax = plt.subplots(figsize=(14, 10))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis("off")

        # Node definitions: (x, y, text, type, width, height)
        nodes = [
            (5.0, 9.5, "Start:\nHypothesis Testing", "start", 2.0, 0.6),
            (5.0, 8.3, "Perform\nOne-Way ANOVA", "process", 1.8, 0.6),
            (5.0, 7.1, "Is ANOVA\nSignificant?", "decision", 1.6, 0.6),
            (2.0, 5.8, "Stop:\nNo differences\ndetected", "end", 1.6, 0.6),
            (8.0, 5.8, "Perform\nPairwise\nComparisons", "process", 1.6, 0.8),
            (8.0, 4.3, "Choose\nCorrection\nMethod", "decision", 1.6, 0.8),
            (2.5, 3.0, "Bonferroni\n(Most Conservative)", "process", 1.8, 0.6),
            (5.0, 3.0, "Holm\n(Balanced)", "process", 1.6, 0.6),
            (8.0, 3.0, "Tukey HSD\n(Best for ANOVA)", "process", 1.8, 0.6),
            (5.0, 1.5, "Interpret\nResults", "process", 1.6, 0.6),
            (5.0, 0.5, "End", "end", 1.2, 0.5),
        ]

        colors = {
            "start": "#AED6F1",
            "process": "#ABEBC6",
            "decision": "#F9E79F",
            "end": "#F5B7B1"
        }

        # Draw nodes
        for x, y, text, node_type, w, h in nodes:
            if node_type == "decision":
                # Diamond shape
                pts = np.array([
                    [x, y + h/2], [x + w/2, y], 
                    [x, y - h/2], [x - w/2, y]
                ])
                ax.fill(pts[:, 0], pts[:, 1], facecolor=colors[node_type],
                       edgecolor="black", linewidth=2, alpha=0.9)
            else:
                rect = Rectangle((x - w/2, y - h/2), w, h,
                               facecolor=colors[node_type], edgecolor="black",
                               linewidth=2, alpha=0.9, 
                               joinstyle="round")
                ax.add_patch(rect)

            ax.text(x, y, text, ha="center", va="center", 
                   fontsize=9, fontweight="bold")

        # Arrows: (start_node_idx, end_node_idx, label)
        arrows = [
            (0, 1, ""),
            (1, 2, ""),
            (2, 3, "No"),
            (2, 4, "Yes"),
            (4, 5, ""),
            (5, 6, ""),
            (5, 7, ""),
            (5, 8, ""),
            (6, 9, ""),
            (7, 9, ""),
            (8, 9, ""),
            (9, 10, ""),
        ]

        for start_idx, end_idx, label in arrows:
            x1, y1, _, _, w1, h1 = nodes[start_idx]
            x2, y2, _, _, w2, h2 = nodes[end_idx]

            # Calculate edge points
            dx, dy = x2 - x1, y2 - y1
            dist = np.sqrt(dx**2 + dy**2)

            if dist > 0:
                # Offset from center to edge
                offset1 = h1 / 2 if abs(dy) > abs(dx) else w1 / 2
                offset2 = h2 / 2 if abs(dy) > abs(dx) else w2 / 2

                ratio1 = offset1 / dist
                ratio2 = offset2 / dist

                start_x = x1 + dx * ratio1 * 1.2
                start_y = y1 + dy * ratio1 * 1.2
                end_x = x2 - dx * ratio2 * 1.2
                end_y = y2 - dy * ratio2 * 1.2

                ax.annotate("", xy=(end_x, end_y), xytext=(start_x, start_y),
                           arrowprops=dict(arrowstyle="->", lw=1.5, color="#555"))

                if label:
                    mid_x = (start_x + end_x) / 2
                    mid_y = (start_y + end_y) / 2
                    ax.text(mid_x, mid_y, label, fontsize=10, fontweight="bold",
                           bbox=dict(boxstyle="round,pad=0.2", facecolor="white", alpha=0.8))

        ax.set_title("Decision Flow for Multiple Hypothesis Testing", 
                    fontsize=16, fontweight="bold", pad=20)
        plt.tight_layout()
        return self.fig.save(fig, "09_decision_flow")

    def plot_fwer_growth_detailed(self) -> Path:
        """Create a detailed FWER growth visualization."""
        self.logger.info("Creating detailed FWER growth plot...")

        fig, ax = plt.subplots(figsize=(12, 7))

        alpha = self.exp.alpha
        m_continuous = np.linspace(0, 100, 1000)
        fwer_continuous = 1 - (1 - alpha) ** m_continuous

        ax.plot(m_continuous, fwer_continuous, "b-", linewidth=2.5,
               label=f"FWER = 1 − (1 − α)ᵐ")
        ax.fill_between(m_continuous, 0, fwer_continuous, alpha=0.1, color="blue")

        # Key reference lines
        ax.axhline(y=alpha, color="red", linestyle="--", linewidth=2, label=f"α = {alpha}")
        ax.axhline(y=0.5, color="orange", linestyle="--", alpha=0.7, label="FWER = 50%")
        ax.axhline(y=0.99, color="purple", linestyle="--", alpha=0.7, label="FWER = 99%")

        # Highlight specific points
        key_points = [1, 5, 10, 20, 50, 100]
        for m in key_points:
            fwer = 1 - (1 - alpha) ** m
            ax.scatter([m], [fwer], s=120, color="red", zorder=5, 
                      edgecolors="black", linewidth=1.5)
            ax.annotate(f"m={m}\nFWER={fwer:.3f}",
                       xy=(m, fwer), xytext=(0, 15),
                       textcoords="offset points", ha="center",
                       fontsize=9, fontweight="bold",
                       bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))

        # Add annotation for rapid growth region
        ax.annotate("Rapid FWER inflation!\nEven with α=0.05,\n10 tests → 40% chance\nof false positive",
                   xy=(10, 1 - (1 - alpha)**10), xytext=(35, 0.3),
                   fontsize=11, fontweight="bold",
                   bbox=dict(boxstyle="round,pad=0.5", facecolor="lightyellow", alpha=0.9),
                   arrowprops=dict(arrowstyle="->", color="darkred", lw=2))

        ax.set_xlabel("Number of Tests (m)", fontweight="bold")
        ax.set_ylabel("Family-Wise Error Rate (FWER)", fontweight="bold")
        ax.set_title("FWER Growth: Why Multiple Testing Correction Matters", 
                    fontsize=14, fontweight="bold")
        ax.legend(loc="lower right", frameon=True, fancybox=True, shadow=True)
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 1)
        ax.grid(True, alpha=0.3)

        plt.tight_layout()
        return self.fig.save(fig, "10_fwer_growth_detailed")


# =============================================================================
# MAIN APPLICATION
# =============================================================================

class FWERLecture:
    """Main application orchestrating the entire lecture workflow."""

    def __init__(
        self,
        exp_config: Optional[ExperimentConfig] = None,
        out_config: Optional[OutputConfig] = None,
        logger: Optional[logging.Logger] = None
    ):
        self.exp_config = exp_config or ExperimentConfig()
        self.out_config = out_config or OutputConfig()
        self.logger = logger or setup_logging()

        # Initialize components
        self.out_config.ensure_dirs()
        self.data_gen = DataGenerator(self.exp_config, self.logger)
        self.analyzer = StatisticalAnalyzer(self.exp_config.alpha, self.logger)
        self.fig_manager = FigureManager(self.out_config, self.logger)
        self.visualizer = Visualizer(self.fig_manager, self.exp_config, self.logger)

    def run(self, n_simulations: int = 1000) -> Dict[str, Any]:
        """Execute the complete lecture workflow.

        Args:
            n_simulations: Number of Monte Carlo iterations.

        Returns:
            Dictionary containing all results and artifacts.
        """
        self.logger.info("=" * 60)
        self.logger.info("DoE Lecture 8: Multiple Testing with FWER")
        self.logger.info("=" * 60)

        artifacts = {}

        # Part 1: Generate Data
        self.logger.info("\n" + "─" * 50)
        self.logger.info("PART 1: DATA GENERATION")
        self.logger.info("─" * 50)

        wide_df, long_df = self.data_gen.generate()
        summary = self.data_gen.summary_stats(long_df)
        self.logger.info(f"\nSummary Statistics:\n{summary}")

        long_df.to_csv(self.out_config.data_path("fertilizer_data"), index=False)
        artifacts["data"] = long_df

        # Part 2: Visualize Distributions
        self.logger.info("\n" + "─" * 50)
        self.logger.info("PART 2: DISTRIBUTION VISUALIZATION")
        self.logger.info("─" * 50)

        artifacts["fig_distributions"] = self.visualizer.plot_distributions(wide_df, long_df)

        # Part 3: ANOVA
        self.logger.info("\n" + "─" * 50)
        self.logger.info("PART 3: ONE-WAY ANOVA")
        self.logger.info("─" * 50)

        model, anova_table = self.analyzer.anova(long_df)
        joblib.dump(model, self.out_config.model_path("anova_model"))
        artifacts["anova_model"] = model
        artifacts["anova_table"] = anova_table
        artifacts["fig_anova"] = self.visualizer.plot_anova_table(anova_table)

        # Part 4: Multiple Testing Problem
        self.logger.info("\n" + "─" * 50)
        self.logger.info("PART 4: MULTIPLE TESTING PROBLEM")
        self.logger.info("─" * 50)

        n_groups = len(self.exp_config.group_names)
        n_comparisons = n_groups * (n_groups - 1) // 2
        fwer = 1 - (1 - self.exp_config.alpha) ** n_comparisons
        self.logger.info(f"Groups: {n_groups}, Comparisons: {n_comparisons}")
        self.logger.info(f"FWER without correction: {fwer:.4f} ({fwer*100:.1f}%)")

        artifacts["fig_mtp"] = self.visualizer.plot_multiple_testing_problem()

        # Part 5: Pairwise T-Tests
        self.logger.info("\n" + "─" * 50)
        self.logger.info("PART 5: PAIRWISE T-TESTS")
        self.logger.info("─" * 50)

        pairwise_df = self.analyzer.pairwise_ttests(wide_df, self.exp_config.group_names)
        self.logger.info(f"\n{pairwise_df[['Comparison', 'mean_diff', 'p_value']].to_string(index=False)}")
        joblib.dump(pairwise_df, self.out_config.model_path("pairwise_results"))
        artifacts["pairwise"] = pairwise_df
        artifacts["fig_raw_pvalues"] = self.visualizer.plot_raw_pvalues(pairwise_df)

        # Part 6-8: Corrections
        self.logger.info("\n" + "─" * 50)
        self.logger.info("PART 6-8: MULTIPLE TESTING CORRECTIONS")
        self.logger.info("─" * 50)

        corrected_df = self.analyzer.apply_corrections(pairwise_df)
        joblib.dump(corrected_df, self.out_config.model_path("corrected_results"))
        artifacts["corrected"] = corrected_df
        artifacts["fig_corrections"] = self.visualizer.plot_correction_comparison(corrected_df)

        # Part 9: Tukey HSD
        self.logger.info("\n" + "─" * 50)
        self.logger.info("PART 9: TUKEY HSD")
        self.logger.info("─" * 50)

        tukey = self.analyzer.tukey_hsd(long_df)
        if tukey:
            joblib.dump(tukey, self.out_config.model_path("tukey_results"))
            artifacts["tukey"] = tukey
            artifacts["fig_tukey"] = self.visualizer.plot_tukey(tukey)

        # Part 10: Monte Carlo Simulation
        self.logger.info("\n" + "─" * 50)
        self.logger.info("PART 10: MONTE CARLO SIMULATION")
        self.logger.info("─" * 50)

        simulator = MonteCarloSimulator(
            n_groups=n_groups,
            n_per_group=self.exp_config.n_per_group,
            alpha=self.exp_config.alpha,
            seed=self.exp_config.seed,
            logger=self.logger
        )
        mc_results = simulator.run(n_simulations=n_simulations)
        joblib.dump(mc_results, self.out_config.model_path("simulation_results"))
        artifacts["mc_results"] = mc_results
        artifacts["fig_mc"] = self.visualizer.plot_monte_carlo(mc_results)

        # Part 11-12: Additional Visualizations
        self.logger.info("\n" + "─" * 50)
        self.logger.info("PART 11-12: ADDITIONAL VISUALIZATIONS")
        self.logger.info("─" * 50)

        artifacts["fig_fwer_growth"] = self.visualizer.plot_fwer_growth_detailed()
        artifacts["fig_ci"] = self.visualizer.plot_confidence_intervals(corrected_df)

        # Part 13: Decision Flow
        self.logger.info("\n" + "─" * 50)
        self.logger.info("PART 13: DECISION FLOW DIAGRAM")
        self.logger.info("─" * 50)

        artifacts["fig_decision"] = self.visualizer.plot_decision_flow()

        # Summary
        self.logger.info("\n" + "=" * 60)
        self.logger.info("COMPLETED SUCCESSFULLY!")
        self.logger.info("=" * 60)
        self.logger.info(f"\nGenerated artifacts:")
        self.logger.info(f"  Figures: {self.out_config.figures_dir}/")
        self.logger.info(f"  Models: {self.out_config.models_dir}/")
        self.logger.info(f"  Data: {self.out_config.data_dir}/")

        return artifacts


# =============================================================================
# CLI INTERFACE
# =============================================================================

def create_parser() -> argparse.ArgumentParser:
    """Create command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="DoE Lecture 8: Multiple Testing with FWER",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                           # Run with defaults
  %(prog)s --n-groups 4 --alpha 0.01 # Custom experiment
  %(prog)s --n-simulations 5000      # More simulation iterations
        """
    )

    parser.add_argument(
        "--n-groups", type=int, default=5,
        help="Number of experimental groups (default: 5)"
    )
    parser.add_argument(
        "--n-per-group", type=int, default=30,
        help="Sample size per group (default: 30)"
    )
    parser.add_argument(
        "--alpha", type=float, default=0.05,
        help="Significance level (default: 0.05)"
    )
    parser.add_argument(
        "--std-dev", type=float, default=4.0,
        help="Standard deviation (default: 4.0)"
    )
    parser.add_argument(
        "--seed", type=int, default=42,
        help="Random seed (default: 42)"
    )
    parser.add_argument(
        "--n-simulations", type=int, default=1000,
        help="Monte Carlo iterations (default: 1000)"
    )
    parser.add_argument(
        "--output-dir", type=str, default=".",
        help="Base output directory (default: current directory)"
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Enable verbose logging"
    )

    return parser


def main() -> None:
    """Main entry point with CLI support."""
    parser = create_parser()
    args = parser.parse_args()

    # Setup logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logger = setup_logging(log_level)

    # Create configurations
    base_dir = Path(args.output_dir)

    exp_config = ExperimentConfig(
        group_names=tuple(f"Group_{i}" for i in range(args.n_groups)),
        true_means=tuple(50.0 + i * 2.5 for i in range(args.n_groups)),
        n_per_group=args.n_per_group,
        std_dev=args.std_dev,
        alpha=args.alpha,
        seed=args.seed
    )

    out_config = OutputConfig(
        figures_dir=base_dir / "figures",
        models_dir=base_dir / "models",
        data_dir=base_dir / "data",
    )

    # Run lecture
    lecture = FWERLecture(exp_config, out_config, logger)
    lecture.run(n_simulations=args.n_simulations)


if __name__ == "__main__":
    main()