"""
================================================================================
DoE Lecture 10: Full Factorial Design — Complete Python Implementation
================================================================================

This module provides a comprehensive implementation of Full Factorial Design
analysis including:
  - Design generation (2^k, 3^k, general full factorial)
  - Effect estimation and ANOVA
  - Interaction plots and diagnostic checks
  - 5 real-world case studies with full analysis pipelines
  - Model serialization and figure generation

Dependencies:
  - numpy, pandas, scipy, matplotlib, seaborn, statsmodels, scikit-learn, joblib

Usage:
  python code.py

Output:
  - ./figures/   : All generated plots (PNG format)
  - ./models/    : Serialized models (joblib format)
================================================================================
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import combinations, product
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import joblib
import warnings
import os
warnings.filterwarnings('ignore')

# Set plotting style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['axes.labelsize'] = 11

# =============================================================================
# SECTION 1: CORE FULL FACTORIAL DESIGN FUNCTIONS
# =============================================================================

class FullFactorialDesign:
    """
    Core class for generating and analyzing full factorial designs.
    
    Supports:
      - 2^k designs (two-level factorial)
      - 3^k designs (three-level factorial)  
      - General full factorial (mixed levels)
      - Center point addition
      - Effect estimation and ANOVA
    """
    
    def __init__(self, factors, levels=None, replicates=1, center_points=0):
        """
        Initialize full factorial design.
        
        Parameters:
        -----------
        factors : dict or int
            If dict: {factor_name: [level1, level2, ...]}
            If int: number of factors for 2^k design
        levels : list or None
            If factors is int, levels specifies levels per factor (default: 2)
        replicates : int
            Number of replicates per run
        center_points : int
            Number of center points to add
        """
        self.replicates = replicates
        self.center_points = center_points
        
        if isinstance(factors, dict):
            self.factor_names = list(factors.keys())
            self.factor_levels = factors
            self.k = len(factors)
        else:
            self.k = factors
            self.factor_names = [f"X{i+1}" for i in range(factors)]
            if levels is None:
                levels = [2] * factors
            elif isinstance(levels, int):
                levels = [levels] * factors
            self.factor_levels = {name: list(range(levels[i])) for i, name in enumerate(self.factor_names)}
        
        self.design_matrix = None
        self.coded_matrix = None
        self.response = None
        self.model = None
        self.anova_table = None
        self.effects = None
        
    def generate_design(self):
        """Generate the full factorial design matrix."""
        level_lists = [self.factor_levels[name] for name in self.factor_names]
        
        # Generate all combinations
        base_runs = list(product(*level_lists))
        
        # Create DataFrame
        df = pd.DataFrame(base_runs, columns=self.factor_names)
        
        # Add replicates
        if self.replicates > 1:
            df = pd.concat([df] * self.replicates, ignore_index=True)
            df['Replicate'] = np.repeat(range(1, self.replicates + 1), len(base_runs))
        else:
            df['Replicate'] = 1
        
        # Add center points
        if self.center_points > 0:
            center_df = pd.DataFrame(
                {name: [np.mean(levels)] * self.center_points 
                 for name, levels in self.factor_levels.items()}
            )
            center_df['Replicate'] = range(self.replicates + 1, self.replicates + self.center_points + 1)
            df = pd.concat([df, center_df], ignore_index=True)
        
        self.design_matrix = df
        self._create_coded_matrix()
        return df
    
    def _create_coded_matrix(self):
        """Create coded (-1, 0, +1) design matrix for analysis."""
        coded = self.design_matrix.copy()
        for name in self.factor_names:
            levels = sorted(self.factor_levels[name])
            if len(levels) == 2:
                # Two-level: map to -1, +1
                low, high = levels[0], levels[1]
                coded[name] = coded[name].apply(lambda x: -1 if x == low else (0 if x == (low + high)/2 else 1))
            elif len(levels) == 3:
                # Three-level: map to -1, 0, +1
                low, mid, high = levels[0], levels[1], levels[2]
                coded[name] = coded[name].apply(
                    lambda x: -1 if x == low else (0 if x == mid else 1)
                )
        self.coded_matrix = coded
    
    def add_response(self, response_values, response_name="Response"):
        """Add response values to the design."""
        if len(response_values) != len(self.design_matrix):
            raise ValueError(f"Response length {len(response_values)} must match design runs {len(self.design_matrix)}")
        self.design_matrix[response_name] = response_values
        self.coded_matrix[response_name] = response_values
        self.response = response_values
        self.response_name = response_name
        return self.design_matrix
    
    def estimate_effects(self):
        """Estimate main effects and interaction effects."""
        if self.response is None:
            raise ValueError("No response data. Use add_response() first.")
        
        effects = {}
        
        # Main effects
        for name in self.factor_names:
            df = self.coded_matrix[self.coded_matrix['Replicate'] <= self.replicates]
            high = df[df[name] == 1][self.response_name].mean()
            low = df[df[name] == -1][self.response_name].mean()
            effects[name] = high - low
        
        # Interaction effects (up to all orders)
        df_main = self.coded_matrix[self.coded_matrix['Replicate'] <= self.replicates].copy()
        for order in range(2, self.k + 1):
            for combo in combinations(self.factor_names, order):
                col_name = ':'.join(combo)
                df_main[col_name] = df_main[list(combo)].prod(axis=1)
                high = df_main[df_main[col_name] == 1][self.response_name].mean()
                low = df_main[df_main[col_name] == -1][self.response_name].mean()
                effects[col_name] = high - low
        
        self.effects = effects
        return effects
    
    def fit_model(self, include_interactions=True, max_order=None):
        """Fit regression model using statsmodels."""
        if self.response is None:
            raise ValueError("No response data. Use add_response() first.")
        
        df = self.coded_matrix[self.coded_matrix['Replicate'] <= self.replicates].copy()
        
        # Build formula
        terms = self.factor_names.copy()
        
        if include_interactions:
            if max_order is None:
                max_order = self.k
            for order in range(2, max_order + 1):
                for combo in combinations(self.factor_names, order):
                    terms.append(':'.join(combo))
        
        formula = f"{self.response_name} ~ " + " + ".join(terms)
        
        self.model = smf.ols(formula=formula, data=df).fit()
        
        # Handle ANOVA - use type I for saturated models to avoid singular matrix issues
        try:
            if self.model.df_resid == 0:
                # Saturated model - no error df, skip ANOVA
                self.anova_table = None
            else:
                self.anova_table = anova_lm(self.model, typ=1)
        except Exception:
            self.anova_table = None
            
        return self.model
    
    def get_anova_table(self):
        """Return ANOVA table."""
        if self.anova_table is None and self.model is not None:
            try:
                self.anova_table = anova_lm(self.model, typ=1)
            except Exception:
                self.anova_table = None
        return self.anova_table
    
    def predict(self, new_data):
        """Make predictions using fitted model."""
        if self.model is None:
            raise ValueError("No model fitted. Use fit_model() first.")
        return self.model.predict(new_data)
    
    def save_model(self, filepath):
        """Save fitted model to disk."""
        if self.model is None:
            raise ValueError("No model fitted. Use fit_model() first.")
        joblib.dump({
            'model': self.model,
            'design': self.design_matrix,
            'effects': self.effects,
            'anova': self.anova_table,
            'factor_names': self.factor_names,
            'factor_levels': self.factor_levels
        }, filepath)
        print(f"Model saved to {filepath}")
    
    def load_model(self, filepath):
        """Load model from disk."""
        data = joblib.load(filepath)
        self.model = data['model']
        self.design_matrix = data['design']
        self.effects = data['effects']
        self.anova_table = data['anova']
        self.factor_names = data['factor_names']
        self.factor_levels = data['factor_levels']
        print(f"Model loaded from {filepath}")
        return self


# =============================================================================
# SECTION 2: VISUALIZATION FUNCTIONS
# =============================================================================

def plot_main_effects(design_obj, save_path=None):
    """Plot main effects for all factors."""
    if design_obj.effects is None:
        design_obj.estimate_effects()
    
    fig, axes = plt.subplots(1, design_obj.k, figsize=(4*design_obj.k, 4))
    if design_obj.k == 1:
        axes = [axes]
    
    df = design_obj.coded_matrix[design_obj.coded_matrix['Replicate'] <= design_obj.replicates]
    
    for idx, name in enumerate(design_obj.factor_names):
        ax = axes[idx]
        
        # Get factor levels
        levels = sorted(design_obj.factor_levels[name])
        means = []
        stds = []
        
        for level in levels:
            subset = df[df[name] == level][design_obj.response_name]
            means.append(subset.mean())
            stds.append(subset.std() / np.sqrt(len(subset)) if len(subset) > 1 else 0)
        
        ax.errorbar(range(len(levels)), means, yerr=stds, marker='o', 
                   markersize=8, linewidth=2, capsize=5, color='steelblue')
        ax.set_xticks(range(len(levels)))
        ax.set_xticklabels([str(l) for l in levels])
        ax.set_xlabel(f"{name} Level")
        ax.set_ylabel(design_obj.response_name)
        ax.set_title(f"Main Effect: {name}")
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Saved: {save_path}")
    plt.show()
    return fig


def plot_interaction_effects(design_obj, save_path=None):
    """Plot 2-way interaction effects."""
    df = design_obj.coded_matrix[design_obj.coded_matrix['Replicate'] <= design_obj.replicates]
    
    if design_obj.k < 2:
        print("Need at least 2 factors for interaction plots.")
        return None
    
    n_pairs = len(list(combinations(design_obj.factor_names, 2)))
    n_cols = min(3, n_pairs)
    n_rows = (n_pairs + n_cols - 1) // n_cols
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(5*n_cols, 4*n_rows))
    if n_pairs == 1:
        axes = np.array([axes])
    axes = axes.flatten()
    
    for idx, (f1, f2) in enumerate(combinations(design_obj.factor_names, 2)):
        ax = axes[idx]
        
        levels1 = sorted(design_obj.factor_levels[f1])
        levels2 = sorted(design_obj.factor_levels[f2])
        
        for level2 in levels2:
            subset = df[df[f2] == level2]
            means = [subset[subset[f1] == l][design_obj.response_name].mean() for l in levels1]
            ax.plot(levels1, means, marker='o', label=f"{f2}={level2}", linewidth=2)
        
        ax.set_xlabel(f1)
        ax.set_ylabel(design_obj.response_name)
        ax.set_title(f"Interaction: {f1} × {f2}")
        ax.legend(title=f2)
        ax.grid(True, alpha=0.3)
    
    # Hide unused subplots
    for idx in range(n_pairs, len(axes)):
        axes[idx].set_visible(False)
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Saved: {save_path}")
    plt.show()
    return fig


def plot_pareto_chart(design_obj, save_path=None):
    """Create Pareto chart of effect magnitudes."""
    if design_obj.effects is None:
        design_obj.estimate_effects()
    
    effects = design_obj.effects
    names = list(effects.keys())
    values = [abs(effects[n]) for n in names]
    
    # Sort by absolute value
    sorted_idx = np.argsort(values)[::-1]
    names = [names[i] for i in sorted_idx]
    values = [values[i] for i in sorted_idx]
    
    # Calculate reference line (Lenth's method for unreplicated designs)
    if design_obj.replicates == 1:
        s0 = 1.5 * np.median(values)
        trimmed = [v for v in values if v <= 2.5 * s0]
        PSE = 1.5 * np.median(trimmed) if trimmed else s0
        margin_error = 2 * PSE  # Approximate for alpha=0.05
    else:
        # Use standard error from ANOVA
        if design_obj.model is None:
            design_obj.fit_model()
        if design_obj.model and design_obj.model.df_resid > 0:
            mse = design_obj.model.mse_resid
            margin_error = 2 * np.sqrt(mse / (2**design_obj.k * design_obj.replicates / 2))
        else:
            margin_error = np.percentile(values, 80)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = ['crimson' if v > margin_error else 'steelblue' for v in values]
    bars = ax.barh(range(len(names)), values, color=colors)
    ax.axvline(margin_error, color='red', linestyle='--', linewidth=2, label=f'Reference Line ({margin_error:.3f})')
    ax.set_yticks(range(len(names)))
    ax.set_yticklabels(names)
    ax.set_xlabel('|Effect|')
    ax.set_title('Pareto Chart of Effect Magnitudes')
    ax.legend()
    ax.invert_yaxis()
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Saved: {save_path}")
    plt.show()
    return fig


def plot_normal_probability(design_obj, save_path=None):
    """Create normal probability plot of effects."""
    if design_obj.effects is None:
        design_obj.estimate_effects()
    
    effects = list(design_obj.effects.values())
    names = list(design_obj.effects.keys())
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Sort effects
    sorted_effects = np.sort(effects)
    n = len(sorted_effects)
    
    # Calculate theoretical quantiles
    theoretical = stats.norm.ppf((np.arange(1, n+1) - 0.5) / n)
    
    # Plot
    ax.scatter(theoretical, sorted_effects, s=60, color='steelblue', edgecolors='black')
    
    # Fit line through middle points
    mid_idx = slice(n//4, 3*n//4)
    z = np.polyfit(theoretical[mid_idx], sorted_effects[mid_idx], 1)
    p = np.poly1d(z)
    ax.plot(theoretical, p(theoretical), 'r--', linewidth=2, label='Reference Line')
    
    # Annotate significant effects
    for i, (name, effect) in enumerate(design_obj.effects.items()):
        if abs(effect) > np.percentile(np.abs(effects), 80):
            idx = np.where(sorted_effects == effect)[0]
            if len(idx) > 0:
                ax.annotate(name, (theoretical[idx[0]], effect), 
                           textcoords="offset points", xytext=(10, 5), fontsize=8)
    
    ax.set_xlabel('Theoretical Quantiles')
    ax.set_ylabel('Effect Estimates')
    ax.set_title('Normal Probability Plot of Effects')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Saved: {save_path}")
    plt.show()
    return fig


def plot_residual_diagnostics(design_obj, save_path=None):
    """Create residual diagnostic plots."""
    if design_obj.model is None:
        design_obj.fit_model()
    
    if design_obj.model.df_resid == 0:
        print("Saturated model - no residual degrees of freedom. Skipping residual diagnostics.")
        return None
    
    residuals = design_obj.model.resid
    fitted = design_obj.model.fittedvalues
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Residuals vs Fitted
    ax = axes[0, 0]
    ax.scatter(fitted, residuals, alpha=0.7, edgecolors='black')
    ax.axhline(y=0, color='red', linestyle='--')
    ax.set_xlabel('Fitted Values')
    ax.set_ylabel('Residuals')
    ax.set_title('Residuals vs Fitted')
    ax.grid(True, alpha=0.3)
    
    # Normal Q-Q Plot
    ax = axes[0, 1]
    stats.probplot(residuals, dist="norm", plot=ax)
    ax.set_title('Normal Q-Q Plot')
    ax.grid(True, alpha=0.3)
    
    # Scale-Location Plot
    ax = axes[1, 0]
    ax.scatter(fitted, np.sqrt(np.abs(residuals)), alpha=0.7, edgecolors='black')
    ax.set_xlabel('Fitted Values')
    ax.set_ylabel('√|Residuals|')
    ax.set_title('Scale-Location Plot')
    ax.grid(True, alpha=0.3)
    
    # Residuals vs Run Order
    ax = axes[1, 1]
    ax.scatter(range(len(residuals)), residuals, alpha=0.7, edgecolors='black')
    ax.axhline(y=0, color='red', linestyle='--')
    ax.set_xlabel('Run Order')
    ax.set_ylabel('Residuals')
    ax.set_title('Residuals vs Run Order')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Saved: {save_path}")
    plt.show()
    return fig


def plot_contour_surface(design_obj, response_func=None, save_path=None):
    """Create contour and surface plots for 2-factor designs."""
    if design_obj.k != 2:
        print("Contour plots only supported for 2-factor designs.")
        return None
    
    f1, f2 = design_obj.factor_names
    levels1 = sorted(design_obj.factor_levels[f1])
    levels2 = sorted(design_obj.factor_levels[f2])
    
    if design_obj.model is None:
        design_obj.fit_model()
    
    # Create grid
    x1 = np.linspace(min(levels1), max(levels1), 50)
    x2 = np.linspace(min(levels2), max(levels2), 50)
    X1, X2 = np.meshgrid(x1, x2)
    
    # Predict
    grid_df = pd.DataFrame({f1: X1.ravel(), f2: X2.ravel()})
    
    # For coded model, we need to code the grid
    for name in design_obj.factor_names:
        lvls = sorted(design_obj.factor_levels[name])
        if len(lvls) == 2:
            low, high = lvls[0], lvls[1]
            grid_df[name] = grid_df[name].apply(lambda x: -1 if x <= low else 1)
    
    # Add interaction term
    grid_df[f'{f1}:{f2}'] = grid_df[f1] * grid_df[f2]
    
    Z = design_obj.model.predict(grid_df).values.reshape(X1.shape)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Contour plot
    ax = axes[0]
    cs = ax.contourf(X1, X2, Z, levels=20, cmap='viridis')
    ax.contour(X1, X2, Z, levels=20, colors='black', linewidths=0.5)
    plt.colorbar(cs, ax=ax, label=design_obj.response_name)
    ax.set_xlabel(f1)
    ax.set_ylabel(f2)
    ax.set_title(f'Contour Plot: {design_obj.response_name}')
    
    # Surface plot
    ax = axes[1]
    surf = ax.contourf(X1, X2, Z, levels=20, cmap='viridis')
    ax.set_xlabel(f1)
    ax.set_ylabel(f2)
    ax.set_title(f'Surface Plot: {design_obj.response_name}')
    plt.colorbar(surf, ax=ax, label=design_obj.response_name)
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Saved: {save_path}")
    plt.show()
    return fig


def plot_design_matrix_heatmap(design_obj, save_path=None):
    """Visualize the design matrix as a heatmap."""
    if design_obj.coded_matrix is None:
        design_obj.generate_design()
    
    df = design_obj.coded_matrix[design_obj.factor_names].copy()
    
    fig, ax = plt.subplots(figsize=(max(6, design_obj.k*1.5), max(4, len(df)*0.3)))
    
    # Create custom colormap
    cmap = sns.color_palette("RdYlBu_r", as_cmap=True)
    
    sns.heatmap(df, annot=True, cmap=cmap, center=0, 
                cbar_kws={'label': 'Coded Level'}, 
                linewidths=0.5, linecolor='gray',
                ax=ax, fmt='.0f')
    ax.set_title(f'Design Matrix: {design_obj.k}-Factor Full Factorial')
    ax.set_xlabel('Factors')
    ax.set_ylabel('Run Number')
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Saved: {save_path}")
    plt.show()
    return fig


# =============================================================================
# SECTION 3: CASE STUDIES
# =============================================================================

def case_study_1_ceramic_strength():
    """
    ===================================================================
    CASE STUDY 1: Ceramic Strength Optimization (NIST Example)
    ===================================================================
    2^5 full factorial design with 32 runs.
    Factors: Table Speed, Feed Rate, Wheel Grit, Direction, Batch
    Response: Ceramic Strength
    
    Key Finding: Direction is the most important factor.
    ===================================================================
    """
    print("\\n" + "="*70)
    print("CASE STUDY 1: Ceramic Strength Optimization (2^5 Design)")
    print("="*70)
    
    # Define factors and levels
    factors = {
        'Table_Speed': [0.025, 0.125],      # m/s
        'Feed_Rate': [0.005, 0.125],         # mm
        'Wheel_Grit': [0, 1],                # 140/170 vs 170/200 (coded)
        'Direction': [0, 1],                 # Longitudinal vs Transverse
        'Batch': [0, 1]                      # Batch 1 vs Batch 2
    }
    
    # Generate design
    design = FullFactorialDesign(factors, replicates=1)
    design.generate_design()
    
    # Simulate realistic response data (based on NIST patterns)
    np.random.seed(42)
    
    # True model coefficients (Direction dominates)
    true_effects = {
        'Table_Speed': 2.5,
        'Feed_Rate': 1.8,
        'Wheel_Grit': 0.5,
        'Direction': 8.2,      # Dominant effect
        'Batch': 3.1,
        'Table_Speed:Feed_Rate': 1.2,
        'Table_Speed:Direction': 0.8,
        'Feed_Rate:Batch': 1.5,
    }
    
    df = design.coded_matrix.copy()
    y = 50  # Base mean
    
    for term, coef in true_effects.items():
        if ':' in term:
            cols = term.split(':')
            y += coef * df[cols].prod(axis=1) / 2
        else:
            y += coef * df[term] / 2
    
    y += np.random.normal(0, 1.5, len(y))  # Add noise
    design.add_response(y, "Strength_MPa")
    
    print(f"\\nDesign: 2^{design.k} = {2**design.k} runs")
    print(f"Factors: {design.factor_names}")
    print(f"\\nFirst 5 runs:")
    print(design.design_matrix.head())
    
    # Analysis
    effects = design.estimate_effects()
    model = design.fit_model()
    
    print(f"\\n--- Effect Estimates ---")
    for name, eff in sorted(effects.items(), key=lambda x: abs(x[1]), reverse=True):
        sig = "***" if abs(eff) > 5 else "**" if abs(eff) > 2 else ""
        print(f"  {name:30s}: {eff:+.3f} {sig}")
    
    print(f"\\n--- Model Summary ---")
    print(f"  R-squared: {model.rsquared:.4f}")
    print(f"  Adjusted R-squared: {model.rsquared_adj:.4f}")
    if model.df_resid > 0:
        print(f"  MSE: {model.mse_resid:.4f}")
    else:
        print(f"  Note: Saturated model (no error df)")
    
    # Visualizations
    plot_main_effects(design, save_path='./figures/cs1_main_effects.png')
    plot_interaction_effects(design, save_path='./figures/cs1_interaction_effects.png')
    plot_pareto_chart(design, save_path='./figures/cs1_pareto_chart.png')
    plot_normal_probability(design, save_path='./figures/cs1_normal_probability.png')
    plot_residual_diagnostics(design, save_path='./figures/cs1_residual_diagnostics.png')
    plot_design_matrix_heatmap(design, save_path='./figures/cs1_design_matrix.png')
    
    # Save model
    design.save_model('./models/cs1_ceramic_strength_model.joblib')
    
    print("\\n✓ Case Study 1 complete. Figures saved to ./figures/, model to ./models/")
    return design


def case_study_2_ginger_extraction():
    """
    ===================================================================
    CASE STUDY 2: Ginger Essential Oil Extraction (Shah et al., 2014)
    ===================================================================
    2^3 full factorial with 2 replicates (16 total runs).
    Factors: Extraction Time, Microwave Power, Sample Type
    Response: Oil Yield (%)
    
    Key Finding: All main effects significant; interactions influence yield.
    ===================================================================
    """
    print("\\n" + "="*70)
    print("CASE STUDY 2: Ginger Essential Oil Extraction (2^3 with Replicates)")
    print("="*70)
    
    factors = {
        'Extraction_Time': [10, 30],      # minutes
        'Microwave_Power': [288, 640],    # Watts
        'Sample_Type': [0, 1]             # Crushed=0, Sliced=1
    }
    
    design = FullFactorialDesign(factors, replicates=2)
    design.generate_design()
    
    # Simulate response
    np.random.seed(123)
    df = design.coded_matrix.copy()
    
    y = 2.5  # Base yield
    y += 1.2 * df['Extraction_Time'] / 2
    y += 0.8 * df['Microwave_Power'] / 2
    y += 0.6 * df['Sample_Type'] / 2
    y += 0.4 * df['Extraction_Time'] * df['Microwave_Power'] / 2
    y += 0.3 * df['Extraction_Time'] * df['Sample_Type'] / 2
    y += np.random.normal(0, 0.15, len(y))
    
    design.add_response(y, "Oil_Yield_pct")
    
    print(f"\\nDesign: 2^{design.k} with {design.replicates} replicates = {len(design.design_matrix)} runs")
    print(f"Factors: {design.factor_names}")
    print(f"\\nDesign Matrix:")
    print(design.design_matrix)
    
    # Analysis
    effects = design.estimate_effects()
    model = design.fit_model()
    anova = design.get_anova_table()
    
    if anova is not None:
        print(f"\\n--- ANOVA Table ---")
        print(anova.round(4))
    
    print(f"\\n--- Effect Estimates ---")
    for name, eff in sorted(effects.items(), key=lambda x: abs(x[1]), reverse=True):
        print(f"  {name:35s}: {eff:+.4f}")
    
    print(f"\\n--- Model Summary ---")
    print(f"  R-squared: {model.rsquared:.4f}")
    print(f"  Adjusted R-squared: {model.rsquared_adj:.4f}")
    
    # Visualizations
    plot_main_effects(design, save_path='./figures/cs2_main_effects.png')
    plot_interaction_effects(design, save_path='./figures/cs2_interaction_effects.png')
    plot_pareto_chart(design, save_path='./figures/cs2_pareto_chart.png')
    plot_normal_probability(design, save_path='./figures/cs2_normal_probability.png')
    plot_residual_diagnostics(design, save_path='./figures/cs2_residual_diagnostics.png')
    plot_contour_surface(design, save_path='./figures/cs2_contour_surface.png')
    plot_design_matrix_heatmap(design, save_path='./figures/cs2_design_matrix.png')
    
    # Save model
    design.save_model('./models/cs2_ginger_extraction_model.joblib')
    
    print("\\n✓ Case Study 2 complete. Figures saved to ./figures/, model to ./models/")
    return design


def case_study_3_fluoride_removal():
    """
    ===================================================================
    CASE STUDY 3: Fluoride Removal by Donnan Dialysis (Boubakri et al., 2014)
    ===================================================================
    2^4 full factorial + 4 center points (20 total runs).
    Factors: Concentration, Flow Rate, Agitation Speed, Temperature
    Response: Removal Efficiency (%)
    
    Key Finding: All effects evaluated; center points test for curvature.
    ===================================================================
    """
    print("\\n" + "="*70)
    print("CASE STUDY 3: Fluoride Removal (2^4 + Center Points)")
    print("="*70)
    
    factors = {
        'Concentration': [5, 15],        # mg/L
        'Flow_Rate': [0.4, 1.0],         # L/h
        'Agitation_Speed': [167, 833],   # rpm
        'Temperature': [25, 35]          # °C
    }
    
    design = FullFactorialDesign(factors, replicates=1, center_points=4)
    design.generate_design()
    
    # Simulate response with curvature
    np.random.seed(456)
    df = design.coded_matrix.copy()
    
    y = 55  # Base removal
    y += 8 * df['Concentration'] / 2
    y += 5 * df['Flow_Rate'] / 2
    y += 3 * df['Agitation_Speed'] / 2
    y += 4 * df['Temperature'] / 2
    y += 2 * df['Concentration'] * df['Flow_Rate'] / 2
    y += 1.5 * df['Agitation_Speed'] * df['Temperature'] / 2
    
    # Add curvature effect for center points
    center_mask = df['Replicate'] > 1
    y[center_mask] += 3  # Curvature: center points higher than linear model predicts
    
    y += np.random.normal(0, 2, len(y))
    
    design.add_response(y, "Removal_Efficiency_pct")
    
    print(f"\\nDesign: 2^{design.k} + {design.center_points} center points = {len(design.design_matrix)} runs")
    print(f"Factors: {design.factor_names}")
    
    # Separate center points for curvature test
    main_runs = design.design_matrix[design.design_matrix['Replicate'] == 1]
    center_runs = design.design_matrix[design.design_matrix['Replicate'] > 1]
    
    print(f"\\nCenter points analysis:")
    print(f"  Main runs mean: {main_runs['Removal_Efficiency_pct'].mean():.2f}%")
    print(f"  Center points mean: {center_runs['Removal_Efficiency_pct'].mean():.2f}%")
    print(f"  Difference (curvature indicator): {center_runs['Removal_Efficiency_pct'].mean() - main_runs['Removal_Efficiency_pct'].mean():.2f}%")
    
    # Analysis on main runs only
    effects = design.estimate_effects()
    model = design.fit_model()
    
    print(f"\\n--- Effect Estimates ---")
    for name, eff in sorted(effects.items(), key=lambda x: abs(x[1]), reverse=True)[:8]:
        print(f"  {name:40s}: {eff:+.3f}")
    
    print(f"\\n--- Model Summary ---")
    print(f"  R-squared: {model.rsquared:.4f}")
    print(f"  Adjusted R-squared: {model.rsquared_adj:.4f}")
    if model.df_resid > 0:
        print(f"  MSE: {model.mse_resid:.4f}")
    else:
        print(f"  Note: Saturated model (no error df)")
    
    # Visualizations
    plot_main_effects(design, save_path='./figures/cs3_main_effects.png')
    plot_interaction_effects(design, save_path='./figures/cs3_interaction_effects.png')
    plot_pareto_chart(design, save_path='./figures/cs3_pareto_chart.png')
    plot_normal_probability(design, save_path='./figures/cs3_normal_probability.png')
    plot_residual_diagnostics(design, save_path='./figures/cs3_residual_diagnostics.png')
    plot_design_matrix_heatmap(design, save_path='./figures/cs3_design_matrix.png')
    
    # Save model
    design.save_model('./models/cs3_fluoride_removal_model.joblib')
    
    print("\\n✓ Case Study 3 complete. Figures saved to ./figures/, model to ./models/")
    return design


def case_study_4_wind_tunnel():
    """
    ===================================================================
    CASE STUDY 4: NASA Wind Tunnel Testing — OH-58F Helicopter
    ===================================================================
    2^4 full factorial design for aerodynamic characterization.
    Factors: Angle of Attack, Sideslip Angle, Advance Ratio, Thrust Coefficient
    Response: Download Force (normalized)
    
    Key Finding: DOE reveals interactions missed by OFAT testing.
    ===================================================================
    """
    print("\\n" + "="*70)
    print("CASE STUDY 4: NASA Wind Tunnel — Helicopter Download (2^4 Design)")
    print("="*70)
    
    factors = {
        'Angle_of_Attack': [-3, 3],        # degrees
        'Sideslip_Angle': [-5, 5],         # degrees
        'Advance_Ratio': [0.15, 0.30],     # dimensionless
        'Thrust_Coefficient': [0.004, 0.010]  # dimensionless
    }
    
    design = FullFactorialDesign(factors, replicates=1)
    design.generate_design()
    
    # Simulate aerodynamic response with strong interactions
    np.random.seed(789)
    df = design.coded_matrix.copy()
    
    y = 0.35  # Base download coefficient
    y += 0.12 * df['Angle_of_Attack'] / 2
    y += 0.08 * df['Sideslip_Angle'] / 2
    y += 0.15 * df['Advance_Ratio'] / 2
    y += 0.10 * df['Thrust_Coefficient'] / 2
    
    # Strong interaction: Angle of Attack × Advance Ratio
    y += 0.09 * df['Angle_of_Attack'] * df['Advance_Ratio'] / 2
    # Interaction: Sideslip × Thrust
    y += 0.06 * df['Sideslip_Angle'] * df['Thrust_Coefficient'] / 2
    # 3-way interaction
    y += 0.04 * df['Angle_of_Attack'] * df['Sideslip_Angle'] * df['Advance_Ratio'] / 2
    
    y += np.random.normal(0, 0.008, len(y))
    
    design.add_response(y, "Download_Coefficient")
    
    print(f"\\nDesign: 2^{design.k} = {2**design.k} runs")
    print(f"Factors: {design.factor_names}")
    
    # Analysis
    effects = design.estimate_effects()
    model = design.fit_model()
    
    print(f"\\n--- Top Effect Estimates ---")
    for name, eff in sorted(effects.items(), key=lambda x: abs(x[1]), reverse=True)[:10]:
        print(f"  {name:50s}: {eff:+.5f}")
    
    print(f"\\n--- Model Summary ---")
    print(f"  R-squared: {model.rsquared:.4f}")
    print(f"  Adjusted R-squared: {model.rsquared_adj:.4f}")
    if model.df_resid > 0:
        print(f"  MSE: {model.mse_resid:.4f}")
    else:
        print(f"  Note: Saturated model (no error df)")
    
    # Visualizations
    plot_main_effects(design, save_path='./figures/cs4_main_effects.png')
    plot_interaction_effects(design, save_path='./figures/cs4_interaction_effects.png')
    plot_pareto_chart(design, save_path='./figures/cs4_pareto_chart.png')
    plot_normal_probability(design, save_path='./figures/cs4_normal_probability.png')
    plot_residual_diagnostics(design, save_path='./figures/cs4_residual_diagnostics.png')
    plot_design_matrix_heatmap(design, save_path='./figures/cs4_design_matrix.png')
    
    # Save model
    design.save_model('./models/cs4_wind_tunnel_model.joblib')
    
    print("\\n✓ Case Study 4 complete. Figures saved to ./figures/, model to ./models/")
    return design


def case_study_5_membrane_cleaning():
    """
    ===================================================================
    CASE STUDY 5: Membrane Cleaning Optimization (Chen et al., 2003)
    ===================================================================
    Sequential approach: Fractional factorial → Foldover → Full factorial.
    Demonstrates augmentation strategy.
    
    Factors: Cleaning Time, Temperature, pH, Pressure, Flow Rate, Detergent Conc.
    Response: Flux Recovery (%)
    ===================================================================
    """
    print("\\n" + "="*70)
    print("CASE STUDY 5: Membrane Cleaning Optimization (2^6 Design)")
    print("="*70)
    
    factors = {
        'Cleaning_Time': [10, 30],        # minutes
        'Temperature': [25, 45],          # °C
        'pH': [6, 10],                    # pH units
        'Pressure': [1, 3],               # bar
        'Flow_Rate': [5, 15],             # L/min
        'Detergent_Conc': [0.1, 0.5]      # % w/v
    }
    
    design = FullFactorialDesign(factors, replicates=1)
    design.generate_design()
    
    # Simulate response
    np.random.seed(321)
    df = design.coded_matrix.copy()
    
    y = 60  # Base flux recovery
    y += 8 * df['Cleaning_Time'] / 2
    y += 12 * df['Temperature'] / 2
    y += 6 * df['pH'] / 2
    y += 4 * df['Pressure'] / 2
    y += 3 * df['Flow_Rate'] / 2
    y += 5 * df['Detergent_Conc'] / 2
    
    # Key interactions
    y += 5 * df['Temperature'] * df['pH'] / 2
    y += 3 * df['Cleaning_Time'] * df['Detergent_Conc'] / 2
    y += 2 * df['Temperature'] * df['Cleaning_Time'] / 2
    
    y += np.random.normal(0, 3, len(y))
    
    design.add_response(y, "Flux_Recovery_pct")
    
    print(f"\\nDesign: 2^{design.k} = {2**design.k} runs")
    print(f"Factors: {design.factor_names}")
    print(f"\\nNote: In practice, a 2^6 = 64 run design is large.")
    print(f"      A sequential approach might start with 2^(6-2) = 16 runs,")
    print(f"      then foldover to 32 runs, then augment to full 64 if needed.")
    
    # Analysis
    effects = design.estimate_effects()
    model = design.fit_model()
    
    print(f"\\n--- Top 15 Effect Estimates ---")
    for name, eff in sorted(effects.items(), key=lambda x: abs(x[1]), reverse=True)[:15]:
        print(f"  {name:50s}: {eff:+.3f}")
    
    print(f"\\n--- Model Summary ---")
    print(f"  R-squared: {model.rsquared:.4f}")
    print(f"  Adjusted R-squared: {model.rsquared_adj:.4f}")
    if model.df_resid > 0:
        print(f"  MSE: {model.mse_resid:.4f}")
    else:
        print(f"  Note: Saturated model (no error df)")
    
    # Visualizations
    plot_main_effects(design, save_path='./figures/cs5_main_effects.png')
    plot_interaction_effects(design, save_path='./figures/cs5_interaction_effects.png')
    plot_pareto_chart(design, save_path='./figures/cs5_pareto_chart.png')
    plot_normal_probability(design, save_path='./figures/cs5_normal_probability.png')
    plot_residual_diagnostics(design, save_path='./figures/cs5_residual_diagnostics.png')
    plot_design_matrix_heatmap(design, save_path='./figures/cs5_design_matrix.png')
    
    # Save model
    design.save_model('./models/cs5_membrane_cleaning_model.joblib')
    
    print("\\n✓ Case Study 5 complete. Figures saved to ./figures/, model to ./models/")
    return design


# =============================================================================
# SECTION 4: ADDITIONAL UTILITY FUNCTIONS
# =============================================================================

def generate_summary_report(design_objects, output_file='./models/summary_report.txt'):
    """Generate a text summary report for all case studies."""
    with open(output_file, 'w') as f:
        f.write("="*80 + "\\n")
        f.write("FULL FACTORIAL DESIGN ANALYSIS — SUMMARY REPORT\\n")
        f.write("="*80 + "\\n\\n")
        
        for i, design in enumerate(design_objects, 1):
            f.write(f"CASE STUDY {i}\\n")
            f.write("-"*40 + "\\n")
            f.write(f"Factors: {design.k} ({', '.join(design.factor_names)})\\n")
            f.write(f"Total Runs: {len(design.design_matrix)}\\n")
            f.write(f"Replicates: {design.replicates}\\n")
            f.write(f"Center Points: {design.center_points}\\n")
            f.write(f"Response: {design.response_name}\\n")
            
            if design.model:
                f.write(f"R-squared: {design.model.rsquared:.4f}\\n")
                f.write(f"Adjusted R-squared: {design.model.rsquared_adj:.4f}\\n")
                if design.model.df_resid > 0:
                    f.write(f"MSE: {design.model.mse_resid:.4f}\\n")
            
            if design.effects:
                f.write("\\nTop 5 Effects:\\n")
                for name, eff in sorted(design.effects.items(), key=lambda x: abs(x[1]), reverse=True)[:5]:
                    f.write(f"  {name}: {eff:+.4f}\\n")
            
            f.write("\\n" + "="*80 + "\\n\\n")
    
    print(f"\\nSummary report saved to {output_file}")


def compare_designs_table():
    """Print a comparison table of different factorial designs."""
    print("\\n" + "="*70)
    print("FULL FACTORIAL DESIGN COMPARISON TABLE")
    print("="*70)
    
    data = []
    for k in range(2, 8):
        for levels in [2, 3]:
            runs = levels ** k
            data.append({
                'Design': f"{levels}^{k}",
                'Factors': k,
                'Levels': levels,
                'Runs': runs,
                'Main Effects': k,
                '2-Way Interactions': len(list(combinations(range(k), 2))),
                '3-Way Interactions': len(list(combinations(range(k), 3))),
            })
    
    df = pd.DataFrame(data)
    print(df.to_string(index=False))
    
    # Save as CSV
    df.to_csv('./models/design_comparison_table.csv', index=False)
    print(f"\\nComparison table saved to ./models/design_comparison_table.csv")
    return df


# =============================================================================
# SECTION 5: MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("="*70)
    print("DoE LECTURE 10: FULL FACTORIAL DESIGN — COMPLETE IMPLEMENTATION")
    print("="*70)
    print("\\nThis script demonstrates full factorial design analysis through")
    print("5 real-world case studies with complete visualization and modeling.")
    print("\\nOutput directories:")
    print("  - ./figures/  : All generated plots")
    print("  - ./models/   : Serialized models and data tables")
    
    # Create output directories
    os.makedirs('./figures', exist_ok=True)
    os.makedirs('./models', exist_ok=True)
    
    # Run all case studies
    designs = []
    
    designs.append(case_study_1_ceramic_strength())
    designs.append(case_study_2_ginger_extraction())
    designs.append(case_study_3_fluoride_removal())
    designs.append(case_study_4_wind_tunnel())
    designs.append(case_study_5_membrane_cleaning())
    
    # Generate summary report
    generate_summary_report(designs)
    
    # Print design comparison table
    compare_designs_table()
    
    print("\\n" + "="*70)
    print("ALL CASE STUDIES COMPLETE")
    print("="*70)
    print("\\nGenerated files:")
    print("  Figures (./figures/):")
    for f in sorted(os.listdir('./figures')):
        print(f"    - {f}")
    print("\\n  Models (./models/):")
    for f in sorted(os.listdir('./models')):
        print(f"    - {f}")
    print("\\n✓ Analysis complete. Review figures and models for detailed results.")