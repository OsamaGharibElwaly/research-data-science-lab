"""
================================================================================
DoE Lecture 14: 3^k Full Factorial Designs — code.py
================================================================================
A comprehensive Python implementation for designing, analyzing, and visualizing
3^k full factorial experiments. Includes 7+ visualization functions, 5 case 
studies, polynomial regression models, ANOVA, response surface analysis, and 
interactive 3D plots.

Author: DoE Lecture Series
Date: 2026-08-09
================================================================================
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from itertools import product
from collections import OrderedDict
from typing import Dict, List, Tuple, Optional, Callable
import warnings
import os
warnings.filterwarnings('ignore')

# Statistical libraries
from scipy import stats
from scipy.optimize import minimize
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import cross_val_score
import joblib

# Visualization
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.patches as mpatches

# Set random seed for reproducibility
np.random.seed(42)

# =============================================================================
# SECTION 1: 3^k FULL FACTORIAL DESIGN CLASS
# =============================================================================

class FullFactorial3k:
    """
    Complete 3^k Full Factorial Design implementation.
    
    Generates all 3^k treatment combinations for k factors at 3 levels each.
    Supports coded levels (-1, 0, +1) and natural levels.
    
    Parameters
    ----------
    factors : dict
        Dictionary mapping factor names to (low, center, high) tuples.
    replicates : int, default=1
        Number of replicate runs per treatment combination.
    randomize : bool, default=True
        Whether to randomize the run order.
    """
    
    def __init__(self, factors: Dict[str, Tuple], replicates: int = 1, 
                 randomize: bool = True):
        self.factors = OrderedDict(factors)
        self.k = len(factors)
        self.replicates = replicates
        self.randomize = randomize
        self.coded_levels = [-1, 0, +1]
        self.n_runs = (3 ** self.k) * self.replicates
        self.design = None
        self._build_design()
    
    def _build_design(self):
        """Construct the full 3^k design matrix."""
        # Generate all combinations of coded levels
        coded_combinations = list(product(self.coded_levels, repeat=self.k))
        
        # Create base design
        base_design = pd.DataFrame(
            coded_combinations,
            columns=list(self.factors.keys())
        )
        
        # Add replicates
        designs = []
        for rep in range(self.replicates):
            rep_design = base_design.copy()
            rep_design['Replicate'] = rep + 1
            designs.append(rep_design)
        
        self.design = pd.concat(designs, ignore_index=True)
        
        # Convert coded to natural levels
        for factor_name, (low, center, high) in self.factors.items():
            self.design[f'{factor_name}_natural'] = self.design[factor_name].map({
                -1: low, 0: center, +1: high
            })
        
        # Add run order
        if self.randomize:
            self.design['Run_Order'] = np.random.permutation(len(self.design)) + 1
            self.design = self.design.sort_values('Run_Order').reset_index(drop=True)
        else:
            self.design['Run_Order'] = range(1, len(self.design) + 1)
        
        # Add standard order
        self.design['Std_Order'] = range(1, len(self.design) + 1)
    
    def add_response(self, response_name: str, values: np.ndarray):
        """Add response variable to the design."""
        if len(values) != len(self.design):
            raise ValueError(f"Response length {len(values)} != design length {len(self.design)}")
        self.design[response_name] = values
    
    def get_design_matrix(self, coded: bool = True, include_interactions: bool = True,
                          include_quadratic: bool = True) -> np.ndarray:
        """
        Get the design matrix for regression analysis.
        
        For 3^k designs, we can model:
        - Linear terms: x_i
        - Quadratic terms: x_i^2 (captures curvature)
        - Two-factor interactions: x_i * x_j
        - Three-factor interactions: x_i * x_j * x_k
        - Mixed quadratic interactions: x_i^2 * x_j, etc.
        """
        factor_cols = list(self.factors.keys())
        X = self.design[factor_cols].values.copy()
        
        if not coded:
            # Convert to natural levels
            for i, factor_name in enumerate(factor_cols):
                low, center, high = self.factors[factor_name]
                # Normalize to [-1, +1] for regression
                X[:, i] = (X[:, i] - center) / ((high - low) / 2)
        
        features = [X.copy()]
        feature_names = factor_cols.copy()
        
        # Linear terms already included
        
        if include_quadratic:
            # Quadratic terms: x_i^2
            for i, name in enumerate(factor_cols):
                features.append((X[:, i] ** 2).reshape(-1, 1))
                feature_names.append(f'{name}²')
        
        if include_interactions and self.k >= 2:
            # Two-factor interactions
            for i in range(self.k):
                for j in range(i + 1, self.k):
                    features.append((X[:, i] * X[:, j]).reshape(-1, 1))
                    feature_names.append(f'{factor_cols[i]}×{factor_cols[j]}')
            
            # Three-factor interactions (if k >= 3)
            if self.k >= 3:
                for i in range(self.k):
                    for j in range(i + 1, self.k):
                        for l in range(j + 1, self.k):
                            features.append(
                                (X[:, i] * X[:, j] * X[:, l]).reshape(-1, 1)
                            )
                            feature_names.append(
                                f'{factor_cols[i]}×{factor_cols[j]}×{factor_cols[l]}'
                            )
            
            # Quadratic × linear interactions (for response surface)
            if include_quadratic and self.k >= 2:
                for i in range(self.k):
                    for j in range(self.k):
                        if i != j:
                            features.append(
                                (X[:, i] ** 2 * X[:, j]).reshape(-1, 1)
                            )
                            feature_names.append(f'{factor_cols[i]}²×{factor_cols[j]}')
        
        X_full = np.hstack(features)
        self.feature_names = feature_names
        return X_full
    
    def get_summary(self) -> str:
        """Return a summary string of the design."""
        lines = [
            "=" * 60,
            "3^k FULL FACTORIAL DESIGN SUMMARY",
            "=" * 60,
            f"Number of factors (k): {self.k}",
            f"Levels per factor: 3 (Low=-1, Center=0, High=+1)",
            f"Total treatment combinations: {3**self.k}",
            f"Replicates per combination: {self.replicates}",
            f"Total experimental runs: {self.n_runs}",
            f"Randomization: {'Yes' if self.randomize else 'No'}",
            "-" * 60,
            "Factor Definitions:",
        ]
        for name, (low, center, high) in self.factors.items():
            lines.append(f"  {name}: Low={low}, Center={center}, High={high}")
        lines.append("=" * 60)
        return "\\n".join(lines)


# =============================================================================
# SECTION 2: ANALYSIS FUNCTIONS
# =============================================================================

def compute_main_effects(design_df: pd.DataFrame, response_col: str,
                         factor_cols: List[str]) -> Dict[str, np.ndarray]:
    """
    Compute main effects for each factor at each level.
    
    For 3-level designs, main effect is the change in response as factor
    moves from low to center to high, averaged over all other factors.
    """
    effects = {}
    for factor in factor_cols:
        effect_by_level = []
        for level in [-1, 0, +1]:
            mask = design_df[factor] == level
            avg_response = design_df.loc[mask, response_col].mean()
            effect_by_level.append(avg_response)
        effects[factor] = np.array(effect_by_level)
    return effects


def compute_two_factor_interactions(design_df: pd.DataFrame, response_col: str,
                                     factor_cols: List[str]) -> Dict[str, np.ndarray]:
    """
    Compute two-factor interaction effects.
    
    For 3^k designs, interaction between factors A and B is assessed by
    examining the response at all 9 combinations of A and B levels.
    """
    interactions = {}
    for i, f1 in enumerate(factor_cols):
        for j, f2 in enumerate(factor_cols):
            if i < j:
                interaction_matrix = np.zeros((3, 3))
                for li, l1 in enumerate([-1, 0, +1]):
                    for lj, l2 in enumerate([-1, 0, +1]):
                        mask = (design_df[f1] == l1) & (design_df[f2] == l2)
                        interaction_matrix[li, lj] = design_df.loc[mask, response_col].mean()
                interactions[f'{f1}×{f2}'] = interaction_matrix
    return interactions


def anova_3k(design_df: pd.DataFrame, response_col: str,
              factor_cols: List[str], replicates: int = 1) -> pd.DataFrame:
    """
    Perform ANOVA for 3^k full factorial design.
    
    For 3^k designs with replicates, we can estimate pure error and
    test significance of main effects and interactions.
    """
    n_total = len(design_df)
    y = design_df[response_col].values
    y_mean = y.mean()
    ss_total = ((y - y_mean) ** 2).sum()
    df_total = n_total - 1
    
    results = []
    ss_model = 0
    
    # Main effects
    for factor in factor_cols:
        ss_factor = 0
        for level in [-1, 0, +1]:
            mask = design_df[factor] == level
            n_level = mask.sum()
            y_level_mean = design_df.loc[mask, response_col].mean()
            ss_factor += n_level * (y_level_mean - y_mean) ** 2
        df_factor = 2  # 3 levels - 1
        ms_factor = ss_factor / df_factor
        
        # F-statistic (using pure error if replicates > 1)
        if replicates > 1:
            ss_error = 0
            df_error = 0
            for _, group in design_df.groupby(factor_cols):
                if len(group) > 1:
                    group_y = group[response_col].values
                    ss_error += ((group_y - group_y.mean()) ** 2).sum()
                    df_error += len(group) - 1
            if df_error > 0:
                ms_error = ss_error / df_error
                f_stat = ms_factor / ms_error
                p_value = 1 - stats.f.cdf(f_stat, df_factor, df_error)
            else:
                f_stat = np.nan
                p_value = np.nan
                ms_error = np.nan
        else:
            f_stat = np.nan
            p_value = np.nan
            ms_error = np.nan
        
        results.append({
            'Source': factor,
            'SS': ss_factor,
            'df': df_factor,
            'MS': ms_factor,
            'F': f_stat,
            'p-value': p_value,
            'Significant': p_value < 0.05 if not np.isnan(p_value) else False
        })
        ss_model += ss_factor
    
    # Two-factor interactions
    for i, f1 in enumerate(factor_cols):
        for j, f2 in enumerate(factor_cols):
            if i < j:
                ss_int = 0
                for l1 in [-1, 0, +1]:
                    for l2 in [-1, 0, +1]:
                        mask = (design_df[f1] == l1) & (design_df[f2] == l2)
                        n_cell = mask.sum()
                        y_cell_mean = design_df.loc[mask, response_col].mean()
                        
                        # Subtract main effects
                        mask_f1 = design_df[f1] == l1
                        y_f1_mean = design_df.loc[mask_f1, response_col].mean()
                        mask_f2 = design_df[f2] == l2
                        y_f2_mean = design_df.loc[mask_f2, response_col].mean()
                        
                        ss_int += n_cell * (y_cell_mean - y_f1_mean - y_f2_mean + y_mean) ** 2
                
                df_int = 4  # (3-1)*(3-1)
                ms_int = ss_int / df_int
                
                if replicates > 1 and df_error > 0:
                    f_stat = ms_int / ms_error
                    p_value = 1 - stats.f.cdf(f_stat, df_int, df_error)
                else:
                    f_stat = np.nan
                    p_value = np.nan
                
                results.append({
                    'Source': f'{f1}×{f2}',
                    'SS': ss_int,
                    'df': df_int,
                    'MS': ms_int,
                    'F': f_stat,
                    'p-value': p_value,
                    'Significant': p_value < 0.05 if not np.isnan(p_value) else False
                })
                ss_model += ss_int
    
    # Pure error (if replicates exist)
    if replicates > 1:
        ss_error = 0
        df_error = 0
        for _, group in design_df.groupby(factor_cols):
            if len(group) > 1:
                group_y = group[response_col].values
                ss_error += ((group_y - group_y.mean()) ** 2).sum()
                df_error += len(group) - 1
        
        if df_error > 0:
            ms_error = ss_error / df_error
            results.append({
                'Source': 'Error',
                'SS': ss_error,
                'df': df_error,
                'MS': ms_error,
                'F': np.nan,
                'p-value': np.nan,
                'Significant': False
            })
            
            ss_residual = ss_total - ss_model
            df_residual = df_total - sum(r['df'] for r in results if r['Source'] != 'Error')
            
            if df_residual > 0:
                ms_residual = ss_residual / df_residual
                results.append({
                    'Source': 'Lack of Fit',
                    'SS': ss_residual,
                    'df': df_residual,
                    'MS': ms_residual,
                    'F': ms_residual / ms_error if ms_error > 0 else np.nan,
                    'p-value': 1 - stats.f.cdf(ms_residual / ms_error, df_residual, df_error) if ms_error > 0 else np.nan,
                    'Significant': False
                })
    
    results.append({
        'Source': 'Total',
        'SS': ss_total,
        'df': df_total,
        'MS': np.nan,
        'F': np.nan,
        'p-value': np.nan,
        'Significant': False
    })
    
    return pd.DataFrame(results)


def fit_polynomial_model(design_df: pd.DataFrame, response_col: str,
                         factor_cols: List[str], degree: int = 2,
                         include_interactions: bool = True) -> Tuple:
    """
    Fit a polynomial regression model to 3^k design data.
    
    For 3^k designs, a full quadratic model includes:
    - Linear terms
    - Pure quadratic terms
    - Two-factor interactions
    """
    X = design_df[factor_cols].values
    y = design_df[response_col].values
    
    # Build polynomial features
    poly_terms = []
    feature_names = []
    
    # Linear terms
    for i, name in enumerate(factor_cols):
        poly_terms.append(X[:, i])
        feature_names.append(name)
    
    # Quadratic terms
    if degree >= 2:
        for i, name in enumerate(factor_cols):
            poly_terms.append(X[:, i] ** 2)
            feature_names.append(f'{name}²')
    
    # Two-factor interactions
    if include_interactions and degree >= 2:
        for i in range(len(factor_cols)):
            for j in range(i + 1, len(factor_cols)):
                poly_terms.append(X[:, i] * X[:, j])
                feature_names.append(f'{factor_cols[i]}×{factor_cols[j]}')
    
    X_poly = np.column_stack(poly_terms)
    
    model = LinearRegression()
    model.fit(X_poly, y)
    y_pred = model.predict(X_poly)
    
    r2 = r2_score(y, y_pred)
    rmse = np.sqrt(mean_squared_error(y, y_pred))
    
    # Create results DataFrame
    coef_df = pd.DataFrame({
        'Term': ['Intercept'] + feature_names,
        'Coefficient': [model.intercept_] + list(model.coef_)
    })
    
    return model, coef_df, r2, rmse, y_pred, X_poly


# =============================================================================
# SECTION 3: VISUALIZATION FUNCTIONS (7+)
# =============================================================================

def viz_main_effects_plot(design_df: pd.DataFrame, response_col: str,
                          factor_cols: List[str], save_path: str = None):
    """
    VIZ 1: Main Effects Plot
    Shows the average response at each level of each factor.
    For 3^k designs, this reveals curvature (non-linearity) in main effects.
    """
    n_factors = len(factor_cols)
    fig, axes = plt.subplots(1, n_factors, figsize=(5 * n_factors, 5))
    if n_factors == 1:
        axes = [axes]
    
    colors = plt.cm.viridis(np.linspace(0.2, 0.8, n_factors))
    
    for idx, (factor, ax) in enumerate(zip(factor_cols, axes)):
        level_means = []
        level_stds = []
        for level in [-1, 0, +1]:
            mask = design_df[factor] == level
            responses = design_df.loc[mask, response_col]
            level_means.append(responses.mean())
            level_stds.append(responses.std() / np.sqrt(len(responses)))
        
        ax.errorbar([-1, 0, 1], level_means, yerr=level_stds,
                    marker='o', markersize=10, linewidth=2.5,
                    color=colors[idx], capsize=5, capthick=2)
        ax.set_xlabel(f'{factor} Level', fontsize=11)
        ax.set_ylabel(f'Mean {response_col}', fontsize=11)
        ax.set_title(f'Main Effect: {factor}', fontsize=13, fontweight='bold')
        ax.set_xticks([-1, 0, 1])
        ax.set_xticklabels(['Low\\n(-1)', 'Center\\n(0)', 'High\\n(+1)'])
        ax.grid(True, alpha=0.3)
        ax.axhline(y=np.mean(level_means), color='gray', linestyle='--', alpha=0.5)
    
    plt.suptitle('Main Effects Plot — 3^k Full Factorial Design',
                 fontsize=15, fontweight='bold', y=1.02)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()
    return fig


def viz_interaction_plot(design_df: pd.DataFrame, response_col: str,
                         factor_cols: List[str], save_path: str = None):
    """
    VIZ 2: Two-Factor Interaction Plot

    Shows how the effect of one factor changes at different
    levels of another factor.

    Non-parallel lines indicate possible interaction.
    """

    n_pairs = len(factor_cols) * (len(factor_cols) - 1) // 2

    if n_pairs == 0:
        print("Need at least 2 factors for interaction plots.")
        return None

    ncols = min(3, n_pairs)
    nrows = (n_pairs + ncols - 1) // ncols

    fig, axes = plt.subplots(
        nrows,
        ncols,
        figsize=(5 * ncols, 4.5 * nrows),
        squeeze=False
    )

    # ALWAYS flatten axes into a 1-D array
    axes = axes.ravel()

    colors = ['#E74C3C', '#3498DB', '#2ECC71']
    markers = ['o', 's', '^']

    pair_idx = 0

    for i, f1 in enumerate(factor_cols):

        for j, f2 in enumerate(factor_cols):

            if i >= j:
                continue

            ax = axes[pair_idx]

            for li, level_f2 in enumerate([-1, 0, 1]):

                mask = design_df[f2] == level_f2

                subset = (
                    design_df.loc[mask]
                    .groupby(f1)[response_col]
                    .agg(['mean', 'std', 'count'])
                    .reindex([-1, 0, 1])
                )

                # Standard error
                sem = subset['std'] / np.sqrt(subset['count'])

                ax.errorbar(
                    subset.index,
                    subset['mean'],
                    yerr=sem,
                    marker=markers[li],
                    markersize=8,
                    linewidth=2,
                    color=colors[li],
                    capsize=4,
                    capthick=1.5,
                    label=f'{f2} = {level_f2}'
                )

            ax.set_xlabel(f'{f1} Level', fontsize=11)
            ax.set_ylabel(f'Mean {response_col}', fontsize=11)

            ax.set_title(
                f'{f1} × {f2} Interaction',
                fontsize=12,
                fontweight='bold'
            )

            ax.set_xticks([-1, 0, 1])
            ax.set_xticklabels(['Low', 'Center', 'High'])

            ax.legend(title=f2, loc='best')
            ax.grid(True, alpha=0.3)

            pair_idx += 1

    # Hide unused subplots
    for idx in range(pair_idx, len(axes)):
        axes[idx].set_visible(False)

    plt.suptitle(
        'Two-Factor Interaction Plots — 3^k Full Factorial Design',
        fontsize=15,
        fontweight='bold',
        y=1.02
    )

    plt.tight_layout()

    if save_path:
        plt.savefig(
            save_path,
            dpi=150,
            bbox_inches='tight'
        )

    plt.show()

    return fig


def viz_response_surface_3d(design_df: pd.DataFrame, response_col: str,
                            factor_cols: List[str], model: LinearRegression = None,
                            save_path: str = None):
    """
    VIZ 3: 3D Response Surface Plot
    Visualizes the response surface for the first two factors.
    Shows curvature that 2^k designs cannot capture.
    """
    if len(factor_cols) < 2:
        print("Need at least 2 factors for 3D surface plot.")
        return None
    
    f1, f2 = factor_cols[0], factor_cols[1]
    
    fig = plt.figure(figsize=(14, 6))
    
    # Left: 3D Surface
    ax1 = fig.add_subplot(121, projection='3d')
    
    # Create meshgrid
    x1_range = np.linspace(-1.2, 1.2, 50)
    x2_range = np.linspace(-1.2, 1.2, 50)
    X1, X2 = np.meshgrid(x1_range, x2_range)
    
    if model is not None and len(factor_cols) == 2:
        # Use fitted model for prediction
        X_grid = np.column_stack([X1.ravel(), X2.ravel(),
                                   X1.ravel()**2, X2.ravel()**2,
                                   X1.ravel() * X2.ravel()])
        Z = model.predict(X_grid).reshape(X1.shape)
    else:
        # Simple quadratic interpolation
        from scipy.interpolate import griddata
        points = design_df[[f1, f2]].values
        values = design_df[response_col].values
        Z = griddata(points, values, (X1, X2), method='cubic')
    
    surf = ax1.plot_surface(X1, X2, Z, cmap=cm.coolwarm, alpha=0.8,
                            linewidth=0, antialiased=True)
    
    # Scatter actual data points
    ax1.scatter(design_df[f1], design_df[f2], design_df[response_col],
                c='black', s=50, depthshade=True, label='Observed')
    
    ax1.set_xlabel(f1, fontsize=11)
    ax1.set_ylabel(f2, fontsize=11)
    ax1.set_zlabel(response_col, fontsize=11)
    ax1.set_title('3D Response Surface', fontsize=13, fontweight='bold')
    fig.colorbar(surf, ax=ax1, shrink=0.5, aspect=10)
    
    # Right: Contour plot
    ax2 = fig.add_subplot(122)
    contour = ax2.contourf(X1, X2, Z, levels=20, cmap=cm.coolwarm)
    ax2.scatter(design_df[f1], design_df[f2], c='black', s=50, edgecolors='white')
    ax2.set_xlabel(f1, fontsize=11)
    ax2.set_ylabel(f2, fontsize=11)
    ax2.set_title('Contour Plot', fontsize=13, fontweight='bold')
    fig.colorbar(contour, ax=ax2)
    
    plt.suptitle(f'Response Surface: {response_col} vs {f1} & {f2}',
                 fontsize=15, fontweight='bold')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()
    return fig


def viz_pareto_chart(effects_df: pd.DataFrame, save_path: str = None):
    """
    VIZ 4: Pareto Chart of Standardized Effects
    Identifies the most significant effects in the model.
    """
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Sort by absolute effect
    effects_df = effects_df.copy()
    effects_df['Abs_Effect'] = effects_df['Coefficient'].abs()
    effects_df = effects_df.sort_values('Abs_Effect', ascending=True)
    
    # Exclude intercept
    plot_df = effects_df[effects_df['Term'] != 'Intercept']
    
    colors = ['#E74C3C' if c > 0 else '#3498DB' for c in plot_df['Coefficient']]
    
    bars = ax.barh(range(len(plot_df)), plot_df['Abs_Effect'], color=colors, alpha=0.8)
    ax.set_yticks(range(len(plot_df)))
    ax.set_yticklabels(plot_df['Term'], fontsize=10)
    ax.set_xlabel('Absolute Standardized Effect', fontsize=12)
    ax.set_title('Pareto Chart of Effects — 3^k Full Factorial Design',
                 fontsize=14, fontweight='bold')
    ax.axvline(x=plot_df['Abs_Effect'].mean(), color='gray', linestyle='--',
                label=f'Mean = {plot_df["Abs_Effect"].mean():.3f}')
    ax.legend()
    ax.grid(True, alpha=0.3, axis='x')
    
    # Add value labels
    for i, (bar, val) in enumerate(zip(bars, plot_df['Coefficient'])):
        ax.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height()/2,
                f'{val:+.3f}', va='center', fontsize=9)
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()
    return fig


def viz_residual_analysis(design_df: pd.DataFrame, response_col: str,
                          y_pred: np.ndarray, save_path: str = None):
    """
    VIZ 5: Residual Analysis Plots
    Four-panel diagnostic: residuals vs fitted, Q-Q plot, histogram, scale-location.
    """
    y = design_df[response_col].values
    residuals = y - y_pred
    fitted = y_pred
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Residuals vs Fitted
    ax1 = axes[0, 0]
    ax1.scatter(fitted, residuals, alpha=0.7, edgecolors='black', linewidth=0.5)
    ax1.axhline(y=0, color='red', linestyle='--', linewidth=2)
    ax1.set_xlabel('Fitted Values', fontsize=11)
    ax1.set_ylabel('Residuals', fontsize=11)
    ax1.set_title('Residuals vs Fitted', fontsize=12, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # Q-Q Plot
    ax2 = axes[0, 1]
    stats.probplot(residuals, dist="norm", plot=ax2)
    ax2.set_title('Normal Q-Q Plot', fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    # Histogram
    ax3 = axes[1, 0]
    ax3.hist(residuals, bins=15, edgecolor='black', alpha=0.7, color='steelblue')
    ax3.set_xlabel('Residuals', fontsize=11)
    ax3.set_ylabel('Frequency', fontsize=11)
    ax3.set_title('Distribution of Residuals', fontsize=12, fontweight='bold')
    ax3.axvline(x=0, color='red', linestyle='--', linewidth=2)
    
    # Scale-Location (sqrt of standardized residuals)
    ax4 = axes[1, 1]
    std_residuals = residuals / np.std(residuals)
    ax4.scatter(fitted, np.sqrt(np.abs(std_residuals)), alpha=0.7,
                edgecolors='black', linewidth=0.5)
    ax4.set_xlabel('Fitted Values', fontsize=11)
    ax4.set_ylabel('√|Standardized Residuals|', fontsize=11)
    ax4.set_title('Scale-Location Plot', fontsize=12, fontweight='bold')
    ax4.grid(True, alpha=0.3)
    
    plt.suptitle('Residual Analysis — 3^k Full Factorial Model Diagnostics',
                 fontsize=15, fontweight='bold')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()
    return fig


def viz_cube_plot(design_df: pd.DataFrame, response_col: str,
                  factor_cols: List[str], save_path: str = None):
    """
    VIZ 6: Cube Plot for 3-Factor Design
    Shows response values at all 27 vertices of the 3^3 cube.
    """
    if len(factor_cols) != 3:
        print("Cube plot is specifically designed for 3-factor designs.")
        return None
    
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    f1, f2, f3 = factor_cols
    
    # Get mean response at each combination
    grouped = design_df.groupby(factor_cols)[response_col].mean().reset_index()
    
    # Normalize response for color mapping
    norm = plt.Normalize(grouped[response_col].min(), grouped[response_col].max())
    cmap = cm.coolwarm
    
    for _, row in grouped.iterrows():
        x, y, z = row[f1], row[f2], row[f3]
        resp = row[response_col]
        color = cmap(norm(resp))
        ax.scatter(x, y, z, c=[color], s=200, alpha=0.9, edgecolors='black', linewidth=1.5)
        ax.text(x, y, z, f'{resp:.1f}', fontsize=8, ha='center', va='bottom')
    
    # Draw cube edges
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            ax.plot([x, x], [y, y], [-1, 1], 'k-', alpha=0.2, linewidth=0.5)
    for x in [-1, 0, 1]:
        for z in [-1, 0, 1]:
            ax.plot([x, x], [-1, 1], [z, z], 'k-', alpha=0.2, linewidth=0.5)
    for y in [-1, 0, 1]:
        for z in [-1, 0, 1]:
            ax.plot([-1, 1], [y, y], [z, z], 'k-', alpha=0.2, linewidth=0.5)
    
    ax.set_xlabel(f1, fontsize=12)
    ax.set_ylabel(f2, fontsize=12)
    ax.set_zlabel(f3, fontsize=12)
    ax.set_title(f'3³ Cube Plot: {response_col} at All Treatment Combinations',
                 fontsize=14, fontweight='bold')
    
    # Add colorbar
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    fig.colorbar(sm, ax=ax, shrink=0.5, aspect=10, label=response_col)
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()
    return fig


def viz_half_normal_plot(effects: Dict[str, float], save_path: str = None):
    """
    VIZ 7: Half-Normal Probability Plot of Effects
    Used to identify significant effects in unreplicated designs.
    """
    fig, ax = plt.subplots(figsize=(10, 7))
    
    effect_names = list(effects.keys())
    effect_values = np.array(list(effects.values()))
    abs_effects = np.abs(effect_values)
    
    # Sort effects
    sorted_idx = np.argsort(abs_effects)
    sorted_names = [effect_names[i] for i in sorted_idx]
    sorted_effects = abs_effects[sorted_idx]
    
    n = len(sorted_effects)
    # Half-normal scores
    half_normal_scores = stats.norm.ppf(0.5 + 0.5 * (np.arange(1, n + 1) - 0.5) / n)
    
    ax.scatter(half_normal_scores, sorted_effects, s=80, c='steelblue',
               edgecolors='black', linewidth=1, zorder=3)
    
    # Add labels for large effects
    threshold = np.percentile(sorted_effects, 75)
    for i, (score, effect, name) in enumerate(zip(half_normal_scores, sorted_effects, sorted_names)):
        if effect > threshold:
            ax.annotate(name, (score, effect), textcoords="offset points",
                       xytext=(5, 5), fontsize=9, fontweight='bold')
    
    # Fit line through small effects
    small_mask = sorted_effects <= np.median(sorted_effects)
    if small_mask.sum() >= 2:
        z = np.polyfit(half_normal_scores[small_mask], sorted_effects[small_mask], 1)
        p = np.poly1d(z)
        ax.plot(half_normal_scores, p(half_normal_scores), "r--", alpha=0.7,
                label='Reference Line')
    
    ax.set_xlabel('Half-Normal Score', fontsize=12)
    ax.set_ylabel('Absolute Effect', fontsize=12)
    ax.set_title('Half-Normal Plot of Effects — 3^k Full Factorial Design',
                 fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()
    return fig


def viz_anova_barplot(anova_df: pd.DataFrame, save_path: str = None):
    """
    VIZ 8: ANOVA Bar Plot
    Visualizes sum of squares contribution and F-statistics.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Filter out Total and Error for main plot
    plot_df = anova_df[~anova_df['Source'].isin(['Total', 'Error', 'Lack of Fit'])].copy()
    
    # SS contribution
    ss_total = anova_df[anova_df['Source'] == 'Total']['SS'].values[0]
    plot_df['SS_Pct'] = 100 * plot_df['SS'] / ss_total
    
    colors = ['#E74C3C' if sig else '#95A5A6' for sig in plot_df['Significant']]
    
    bars1 = ax1.bar(range(len(plot_df)), plot_df['SS_Pct'], color=colors, alpha=0.8, edgecolor='black')
    ax1.set_xticks(range(len(plot_df)))
    ax1.set_xticklabels(plot_df['Source'], rotation=45, ha='right', fontsize=9)
    ax1.set_ylabel('% of Total SS', fontsize=12)
    ax1.set_title('Sum of Squares Contribution', fontsize=13, fontweight='bold')
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Add percentage labels
    for bar, pct in zip(bars1, plot_df['SS_Pct']):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{pct:.1f}%', ha='center', fontsize=8)
    
    # F-statistics (log scale for visibility)
    f_df = plot_df[plot_df['F'].notna()].copy()
    if len(f_df) > 0:
        bars2 = ax2.bar(range(len(f_df)), f_df['F'], color=colors[:len(f_df)],
                        alpha=0.8, edgecolor='black')
        ax2.set_xticks(range(len(f_df)))
        ax2.set_xticklabels(f_df['Source'], rotation=45, ha='right', fontsize=9)
        ax2.set_ylabel('F-Statistic', fontsize=12)
        ax2.set_title('F-Statistics by Source', fontsize=13, fontweight='bold')
        ax2.set_yscale('log')
        ax2.grid(True, alpha=0.3, axis='y')
        ax2.axhline(y=stats.f.ppf(0.95, 2, 18), color='red', linestyle='--',
                    label='F-critical (α=0.05)')
        ax2.legend()
    
    plt.suptitle('ANOVA Summary — 3^k Full Factorial Design',
                 fontsize=15, fontweight='bold')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()
    return fig


# =============================================================================
# SECTION 4: CASE STUDIES
# =============================================================================

def case_study_1_baking_process():
    """
    CASE STUDY 1: Cookie Baking Optimization (3² Design)
    
    A bakery wants to optimize cookie crispness using two factors:
    - Temperature: 160°C (low), 175°C (center), 190°C (high)
    - Baking Time: 10 min (low), 13 min (center), 16 min (high)
    
    Response: Crispness score (1-10 scale)
    """
    print("\\n" + "=" * 70)
    print("CASE STUDY 1: Cookie Baking Optimization — 3² Full Factorial Design")
    print("=" * 70)
    
    factors = {
        'Temperature': (160, 175, 190),
        'Time': (10, 13, 16)
    }
    
    design = FullFactorial3k(factors, replicates=2, randomize=True)
    print(design.get_summary())
    
    # Generate synthetic response data with curvature and interaction
    np.random.seed(42)
    responses = []
    for _, row in design.design.iterrows():
        T = row['Temperature']
        t = row['Time']
        # True model: quadratic in both factors with interaction
        crispness = (0.02 * (T - 175)**2 + 0.15 * (t - 13)**2 
                     - 0.008 * (T - 175) * (t - 13)
                     + 0.3 * (T - 175) + 0.5 * (t - 13) + 6.5)
        crispness += np.random.normal(0, 0.4)
        responses.append(max(1, min(10, crispness)))
    
    design.add_response('Crispness', np.array(responses))
    print("\\nDesign with Responses:")
    print(design.design.to_string())
    
    # Analysis
    factor_cols = list(factors.keys())
    
    # Main effects
    effects = compute_main_effects(design.design, 'Crispness', factor_cols)
    print("\\n--- Main Effects ---")
    for factor, eff in effects.items():
        print(f"  {factor}: Low={eff[0]:.3f}, Center={eff[1]:.3f}, High={eff[2]:.3f}")
    
    # Polynomial model
    model, coef_df, r2, rmse, y_pred, X_poly = fit_polynomial_model(
        design.design, 'Crispness', factor_cols, degree=2
    )
    print(f"\\n--- Polynomial Model (R² = {r2:.4f}, RMSE = {rmse:.4f}) ---")
    print(coef_df.to_string(index=False))
    
    # ANOVA
    anova_df = anova_3k(design.design, 'Crispness', factor_cols, replicates=2)
    print("\\n--- ANOVA Table ---")
    print(anova_df.to_string(index=False))
    
    # Visualizations
    viz_main_effects_plot(design.design, 'Crispness', factor_cols,
                          save_path='./figures/case1_main_effects.png')
    viz_interaction_plot(design.design, 'Crispness', factor_cols,
                         save_path='./figures/case1_interaction.png')
    viz_response_surface_3d(design.design, 'Crispness', factor_cols, model,
                            save_path='./figures/case1_response_surface.png')
    viz_pareto_chart(coef_df,
                     save_path='./figures/case1_pareto.png')
    viz_residual_analysis(design.design, 'Crispness', y_pred,
                          save_path='./figures/case1_residuals.png')
    
    # Save model
    joblib.dump(model, './models/case1_baking_model.pkl')
    
    return design, model, anova_df


def case_study_2_chemical_reaction():
    """
    CASE STUDY 2: Chemical Reaction Yield (3³ Design)
    
    A chemical plant wants to maximize reaction yield using three factors:
    - Temperature: 150°C, 175°C, 200°C
    - Pressure: 2 atm, 3 atm, 4 atm
    - Catalyst Concentration: 1%, 2%, 3%
    
    Response: Yield (%)
    """
    print("\\n" + "=" * 70)
    print("CASE STUDY 2: Chemical Reaction Yield — 3³ Full Factorial Design")
    print("=" * 70)
    
    factors = {
        'Temperature': (150, 175, 200),
        'Pressure': (2, 3, 4),
        'Catalyst': (1, 2, 3)
    }
    
    design = FullFactorial3k(factors, replicates=2, randomize=True)
    print(design.get_summary())
    
    np.random.seed(123)
    responses = []
    for _, row in design.design.iterrows():
        T = row['Temperature']
        P = row['Pressure']
        C = row['Catalyst']
        # Complex quadratic model with three-way interaction
        yield_pct = (85 + 0.3 * (T - 175) + 2.5 * (P - 3) + 3.0 * (C - 2)
                     - 0.004 * (T - 175)**2 - 0.8 * (P - 3)**2 - 1.2 * (C - 2)**2
                     + 0.05 * (T - 175) * (P - 3)
                     + 0.15 * (P - 3) * (C - 2)
                     - 0.02 * (T - 175) * (C - 2)
                     + 0.001 * (T - 175) * (P - 3) * (C - 2))
        yield_pct += np.random.normal(0, 1.5)
        responses.append(max(0, min(100, yield_pct)))
    
    design.add_response('Yield', np.array(responses))
    
    factor_cols = list(factors.keys())
    
    # Main effects
    effects = compute_main_effects(design.design, 'Yield', factor_cols)
    print("\\n--- Main Effects ---")
    for factor, eff in effects.items():
        print(f"  {factor}: Low={eff[0]:.2f}%, Center={eff[1]:.2f}%, High={eff[2]:.2f}%")
    
    # Two-factor interactions
    interactions = compute_two_factor_interactions(design.design, 'Yield', factor_cols)
    print("\\n--- Two-Factor Interaction Matrices ---")
    for name, matrix in interactions.items():
        print(f"\\n  {name}:")
        print(f"    Low    Center   High")
        for i, level in enumerate(['Low', 'Center', 'High']):
            print(f"  {level} {matrix[i]}")
    
    # Model
    model, coef_df, r2, rmse, y_pred, X_poly = fit_polynomial_model(
        design.design, 'Yield', factor_cols, degree=2
    )
    print(f"\\n--- Polynomial Model (R² = {r2:.4f}, RMSE = {rmse:.4f}) ---")
    print(coef_df.to_string(index=False))
    
    # ANOVA
    anova_df = anova_3k(design.design, 'Yield', factor_cols, replicates=2)
    print("\\n--- ANOVA Table ---")
    print(anova_df.to_string(index=False))
    
    # Visualizations
    viz_main_effects_plot(design.design, 'Yield', factor_cols,
                          save_path='./figures/case2_main_effects.png')
    viz_interaction_plot(design.design, 'Yield', factor_cols,
                         save_path='./figures/case2_interaction.png')
    viz_cube_plot(design.design, 'Yield', factor_cols,
                  save_path='./figures/case2_cube.png')
    viz_pareto_chart(coef_df,
                     save_path='./figures/case2_pareto.png')
    viz_residual_analysis(design.design, 'Yield', y_pred,
                          save_path='./figures/case2_residuals.png')
    viz_anova_barplot(anova_df,
                      save_path='./figures/case2_anova.png')
    
    joblib.dump(model, './models/case2_chemical_model.pkl')
    
    return design, model, anova_df


def case_study_3_welding_optimization():
    """
    CASE STUDY 3: Welding Process Optimization (3² Design with Replicates)
    
    Optimize weld strength using:
    - Current: 100A, 120A, 140A
    - Travel Speed: 5 mm/s, 8 mm/s, 11 mm/s
    
    Response: Tensile Strength (MPa)
    """
    print("\\n" + "=" * 70)
    print("CASE STUDY 3: Welding Process Optimization — 3² Full Factorial Design")
    print("=" * 70)
    
    factors = {
        'Current': (100, 120, 140),
        'Speed': (5, 8, 11)
    }
    
    design = FullFactorial3k(factors, replicates=3, randomize=True)
    print(design.get_summary())
    
    np.random.seed(456)
    responses = []
    for _, row in design.design.iterrows():
        I = row['Current']
        S = row['Speed']
        # Model with strong curvature in current
        strength = (400 + 2.5 * (I - 120) - 8 * (S - 8)
                    - 0.08 * (I - 120)**2 + 0.3 * (S - 8)**2
                    + 0.15 * (I - 120) * (S - 8))
        strength += np.random.normal(0, 8)
        responses.append(max(0, strength))
    
    design.add_response('Strength_MPa', np.array(responses))
    
    factor_cols = list(factors.keys())
    
    effects = compute_main_effects(design.design, 'Strength_MPa', factor_cols)
    print("\\n--- Main Effects ---")
    for factor, eff in effects.items():
        print(f"  {factor}: Low={eff[0]:.1f}, Center={eff[1]:.1f}, High={eff[2]:.1f} MPa")
    
    model, coef_df, r2, rmse, y_pred, X_poly = fit_polynomial_model(
        design.design, 'Strength_MPa', factor_cols, degree=2
    )
    print(f"\\n--- Polynomial Model (R² = {r2:.4f}, RMSE = {rmse:.4f}) ---")
    print(coef_df.to_string(index=False))
    
    anova_df = anova_3k(design.design, 'Strength_MPa', factor_cols, replicates=3)
    print("\\n--- ANOVA Table ---")
    print(anova_df.to_string(index=False))
    
    viz_main_effects_plot(design.design, 'Strength_MPa', factor_cols,
                          save_path='./figures/case3_main_effects.png')
    viz_interaction_plot(design.design, 'Strength_MPa', factor_cols,
                         save_path='./figures/case3_interaction.png')
    viz_response_surface_3d(design.design, 'Strength_MPa', factor_cols, model,
                            save_path='./figures/case3_response_surface.png')
    viz_pareto_chart(coef_df,
                     save_path='./figures/case3_pareto.png')
    viz_residual_analysis(design.design, 'Strength_MPa', y_pred,
                          save_path='./figures/case3_residuals.png')
    
    joblib.dump(model, './models/case3_welding_model.pkl')
    
    return design, model, anova_df


def case_study_4_pharmaceutical_formulation():
    """
    CASE STUDY 4: Tablet Dissolution Rate (3³ Design)
    
    Optimize tablet dissolution using:
    - Binder Amount: 2%, 4%, 6%
    - Compression Force: 5 kN, 10 kN, 15 kN
    - Lubricant: 0.5%, 1.0%, 1.5%
    
    Response: Dissolution Rate (% at 30 min)
    """
    print("\\n" + "=" * 70)
    print("CASE STUDY 4: Pharmaceutical Dissolution — 3³ Full Factorial Design")
    print("=" * 70)
    
    factors = {
        'Binder': (2, 4, 6),
        'Force': (5, 10, 15),
        'Lubricant': (0.5, 1.0, 1.5)
    }
    
    design = FullFactorial3k(factors, replicates=2, randomize=True)
    print(design.get_summary())
    
    np.random.seed(789)
    responses = []
    for _, row in design.design.iterrows():
        B = row['Binder']
        F = row['Force']
        L = row['Lubricant']
        # Model: dissolution decreases with binder and force, increases with lubricant
        dissolution = (92 - 3.5 * (B - 4) - 2.0 * (F - 10) + 4.0 * (L - 1.0)
                     - 0.3 * (B - 4)**2 - 0.1 * (F - 10)**2 - 2.0 * (L - 1.0)**2
                     + 0.2 * (B - 4) * (F - 10)
                     - 0.5 * (B - 4) * (L - 1.0)
                     + 0.3 * (F - 10) * (L - 1.0))
        dissolution += np.random.normal(0, 2)
        responses.append(max(0, min(100, dissolution)))
    
    design.add_response('Dissolution', np.array(responses))
    
    factor_cols = list(factors.keys())
    
    effects = compute_main_effects(design.design, 'Dissolution', factor_cols)
    print("\\n--- Main Effects ---")
    for factor, eff in effects.items():
        print(f"  {factor}: Low={eff[0]:.1f}%, Center={eff[1]:.1f}%, High={eff[2]:.1f}%")
    
    model, coef_df, r2, rmse, y_pred, X_poly = fit_polynomial_model(
        design.design, 'Dissolution', factor_cols, degree=2
    )
    print(f"\\n--- Polynomial Model (R² = {r2:.4f}, RMSE = {rmse:.4f}) ---")
    print(coef_df.to_string(index=False))
    
    anova_df = anova_3k(design.design, 'Dissolution', factor_cols, replicates=2)
    print("\\n--- ANOVA Table ---")
    print(anova_df.to_string(index=False))
    
    viz_main_effects_plot(design.design, 'Dissolution', factor_cols,
                          save_path='./figures/case4_main_effects.png')
    viz_interaction_plot(design.design, 'Dissolution', factor_cols,
                         save_path='./figures/case4_interaction.png')
    viz_cube_plot(design.design, 'Dissolution', factor_cols,
                  save_path='./figures/case4_cube.png')
    viz_pareto_chart(coef_df,
                     save_path='./figures/case4_pareto.png')
    viz_residual_analysis(design.design, 'Dissolution', y_pred,
                          save_path='./figures/case4_residuals.png')
    viz_anova_barplot(anova_df,
                      save_path='./figures/case4_anova.png')
    
    joblib.dump(model, './models/case4_pharma_model.pkl')
    
    return design, model, anova_df


def case_study_5_semiconductor_etching():
    """
    CASE STUDY 5: Semiconductor Etching Rate (3⁴ Design)
    
    Optimize etching rate using four factors:
    - RF Power: 100W, 150W, 200W
    - Gas Flow Rate: 50 sccm, 100 sccm, 150 sccm
    - Chamber Pressure: 10 mTorr, 20 mTorr, 30 mTorr
    - Temperature: 25°C, 50°C, 75°C
    
    Response: Etch Rate (nm/min)
    """
    print("\\n" + "=" * 70)
    print("CASE STUDY 5: Semiconductor Etching — 3⁴ Full Factorial Design")
    print("=" * 70)
    
    factors = {
        'RF_Power': (100, 150, 200),
        'Gas_Flow': (50, 100, 150),
        'Pressure': (10, 20, 30),
        'Temperature': (25, 50, 75)
    }
    
    design = FullFactorial3k(factors, replicates=1, randomize=True)
    print(design.get_summary())
    
    np.random.seed(101)
    responses = []
    for _, row in design.design.iterrows():
        P = row['RF_Power']
        G = row['Gas_Flow']
        Pr = row['Pressure']
        T = row['Temperature']
        # Complex model with curvature and interactions
        etch_rate = (200 + 1.5 * (P - 150) + 0.8 * (G - 100) 
                     - 3.0 * (Pr - 20) + 0.5 * (T - 50)
                     - 0.008 * (P - 150)**2 - 0.003 * (G - 100)**2
                     + 0.05 * (Pr - 20)**2 - 0.01 * (T - 50)**2
                     + 0.02 * (P - 150) * (G - 100)
                     - 0.03 * (P - 150) * (Pr - 20)
                     + 0.01 * (G - 100) * (T - 50))
        etch_rate += np.random.normal(0, 5)
        responses.append(max(0, etch_rate))
    
    design.add_response('Etch_Rate', np.array(responses))
    
    factor_cols = list(factors.keys())
    
    effects = compute_main_effects(design.design, 'Etch_Rate', factor_cols)
    print("\\n--- Main Effects ---")
    for factor, eff in effects.items():
        print(f"  {factor}: Low={eff[0]:.1f}, Center={eff[1]:.1f}, High={eff[2]:.1f} nm/min")
    
    model, coef_df, r2, rmse, y_pred, X_poly = fit_polynomial_model(
        design.design, 'Etch_Rate', factor_cols, degree=2
    )
    print(f"\\n--- Polynomial Model (R² = {r2:.4f}, RMSE = {rmse:.4f}) ---")
    print(coef_df.to_string(index=False))
    
    # For unreplicated design, use half-normal plot
    effect_dict = dict(zip(coef_df['Term'][1:], coef_df['Coefficient'][1:]))
    viz_half_normal_plot(effect_dict,
                         save_path='./figures/case5_half_normal.png')
    
    viz_main_effects_plot(design.design, 'Etch_Rate', factor_cols,
                          save_path='./figures/case5_main_effects.png')
    viz_interaction_plot(design.design, 'Etch_Rate', factor_cols,
                         save_path='./figures/case5_interaction.png')
    viz_pareto_chart(coef_df,
                     save_path='./figures/case5_pareto.png')
    viz_residual_analysis(design.design, 'Etch_Rate', y_pred,
                          save_path='./figures/case5_residuals.png')
    
    joblib.dump(model, './models/case5_semiconductor_model.pkl')
    
    return design, model


# =============================================================================
# SECTION 5: RUNTIME EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("DoE LECTURE 14: 3^k FULL FACTORIAL DESIGNS — CODE EXECUTION")
    print("=" * 70)
    os.makedirs('./figures', exist_ok=True)
    os.makedirs('./models', exist_ok=True)
    
    # Run all case studies
    case_study_1_baking_process()
    case_study_2_chemical_reaction()
    case_study_3_welding_optimization()
    case_study_4_pharmaceutical_formulation()
    case_study_5_semiconductor_etching()
    
    print("\\n" + "=" * 70)
    print("ALL CASE STUDIES COMPLETED SUCCESSFULLY!")
    print("Figures saved to: ./figures/")
    print("Models saved to: ./models/")
    print("=" * 70)
