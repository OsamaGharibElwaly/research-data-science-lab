"""
DoE Lecture 13: Dealiasing Fractional Designs
=============================================
A comprehensive Python module for dealiasing fractional factorial designs.

Includes:
- Design generation and alias structure computation
- 7+ visualization functions
- 5 case studies with realistic data
- Foldover, D-optimal augmentation, projection, and Bayesian dealiasing
- Model fitting with scikit-learn + joblib persistence

Author: DoE Lecture Series
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations, product
from typing import List, Tuple, Dict, Optional
import warnings
warnings.filterwarnings('ignore')

# Machine learning and optimization
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# For D-optimal design
from scipy.optimize import differential_evolution
from scipy.linalg import det
from scipy import stats

# Set random seed for reproducibility
np.random.seed(42)



# =============================================================================
# SECTION 1: DESIGN CLASS - FractionalFactorialDesign
# =============================================================================

class FractionalFactorialDesign:
    """
    A class to generate and analyze fractional factorial designs.

    Parameters
    ----------
    k : int
        Number of factors
    p : int
        Number of generators (design is 2^{k-p})
    generators : list of str, optional
        Custom generator strings (e.g., ['ABC', 'ABD'])
        IMPORTANT: Generators must use ONLY basic factor letters.
        Basic factors are the first (k-p) factors: A, B, C, ...
    """

    def __init__(self, k: int, p: int, generators: Optional[List[str]] = None):
        self.k = k
        self.p = p
        self.n = 2 ** (k - p)  # Number of runs
        self.factors = [chr(65 + i) for i in range(k)]  # A, B, C, ...

        # Generate the design matrix
        self.design_matrix = self._generate_design(generators)
        self.defining_relation = self._compute_defining_relation(generators)
        self.alias_structure = self._compute_alias_structure()

    def _generate_design(self, generators: Optional[List[str]] = None) -> pd.DataFrame:
        """Generate the fractional factorial design matrix."""
        n_basic = self.k - self.p
        basic_factors = self.factors[:n_basic]

        # Basic full factorial for basic factors
        levels = list(product([-1, 1], repeat=n_basic))
        df = pd.DataFrame(levels, columns=basic_factors)

        # Add generated factors
        if generators is None:
            generators = self._default_generators()

        for i, gen in enumerate(generators):
            factor_name = self.factors[n_basic + i]
            df[factor_name] = self._compute_interaction(df, gen)

        return df

    def _default_generators(self) -> List[str]:
        """Generate default generators for standard designs.

        CRITICAL: Generators are products of BASIC factors ONLY.
        Basic factors = first (k-p) factors (A, B, C, ...).
        Generated factors = remaining p factors.
        A generator like 'AB' means: generated_factor = A * B.
        """
        n_basic = self.k - self.p
        basic = self.factors[:n_basic]

        # Standard generators - each uses ONLY basic factor letters
        standard_generators = {
            # 2^3-1: basic=A,B (2); gen=C (1). C = AB
            (3, 1): ['AB'],
            # 2^4-1: basic=A,B,C (3); gen=D (1). D = ABC
            (4, 1): ['ABC'],
            # 2^5-1: basic=A,B,C,D (4); gen=E (1). E = ABCD
            (5, 1): ['ABCD'],
            # 2^5-2: basic=A,B,C (3); gen=D,E (2). D=AB, E=AC (Resolution III)
            (5, 2): ['AB', 'AC'],
            # 2^6-1: basic=A,B,C,D,E (5); gen=F (1). F = ABCDE
            (6, 1): ['ABCDE'],
            # 2^6-2: basic=A,B,C,D (4); gen=E,F (2). E=ABC, F=ABD (Resolution IV)
            (6, 2): ['ABC', 'ABD'],
            # 2^7-1: basic=A,B,C,D,E,F (6); gen=G (1). G = ABCDEF
            (7, 1): ['ABCDEF'],
            # 2^7-4: basic=A,B,C (3); gen=D,E,F,G (4). D=AB, E=AC, F=BC, G=ABC (Res III)
            (7, 4): ['AB', 'AC', 'BC', 'ABC'],
            # 2^8-4: basic=A,B,C,D (4); gen=E,F,G,H (4). E=ABC, F=ABD, G=ACD, H=BCD (Res IV)
            (8, 4): ['ABC', 'ABD', 'ACD', 'BCD'],
        }

        key = (self.k, self.p)
        if key in standard_generators:
            return standard_generators[key]

        # Fallback: generate from basic factors using simple combinations
        generators = []
        remaining = self.factors[n_basic:]
        basic_combos = []
        for r in range(2, n_basic + 1):
            for combo in combinations(basic, r):
                basic_combos.append(''.join(combo))

        for i, f in enumerate(remaining):
            if i < len(basic_combos):
                generators.append(basic_combos[i])
            else:
                generators.append(basic_combos[i % len(basic_combos)])

        return generators

    def _compute_interaction(self, df: pd.DataFrame, term: str) -> pd.Series:
        """Compute an interaction term from factor columns."""
        result = pd.Series(np.ones(len(df)))
        for char in term:
            result *= df[char]
        return result

    def _multiply_terms(self, term1: str, term2: str) -> str:
        """Multiply two terms in the group algebra, reducing squares (mod 2)."""
        from collections import Counter
        combined = list(term1 + term2)
        counts = Counter(combined)
        # Keep only letters that appear an odd number of times
        result = ''.join(sorted([k for k, v in counts.items() if v % 2 == 1]))
        return result if result else 'I'

    def _compute_defining_relation(self, generators: Optional[List[str]] = None) -> str:
        """Compute the defining relation I = ...

        The defining relation comes from equating each generated factor
        to its generator: generated_factor = generator.
        This gives: generated_factor * generator = I for each.
        The full defining relation includes all generalized interactions
        of these individual relations.
        """
        if generators is None:
            generators = self._default_generators()

        n_basic = self.k - self.p
        remaining = self.factors[n_basic:]

        # Build terms: generated_factor * generator = I
        # So each term in defining relation is: generated_factor * generator
        terms = []
        for i, gen in enumerate(generators):
            term = self._multiply_terms(remaining[i], gen)
            terms.append(term)

        # Compute all generalized interactions of these terms
        all_terms = ['I']
        for r in range(1, len(terms) + 1):
            for combo in combinations(range(len(terms)), r):
                product_term = 'I'
                for idx in combo:
                    product_term = self._multiply_terms(product_term, terms[idx])
                if product_term not in all_terms:
                    all_terms.append(product_term)

        return ' = '.join(all_terms)

    def _compute_alias_structure(self) -> Dict[str, List[str]]:
        """Compute the alias structure for all effects."""
        alias_map = {}

        # Parse defining relation terms
        def_terms = self.defining_relation.split(' = ')

        # Generate all possible effects
        all_effects = ['I']
        for r in range(1, self.k + 1):
            for combo in combinations(self.factors, r):
                all_effects.append(''.join(combo))

        # For each effect, find its alias set
        for effect in all_effects:
            aliases = [effect]
            for def_term in def_terms:
                if def_term != 'I':
                    alias = self._multiply_terms(effect, def_term)
                    if alias not in aliases:
                        aliases.append(alias)
            alias_map[effect] = sorted(aliases)

        return alias_map

    def get_alias_chain(self, effect: str) -> List[str]:
        """Get the alias chain for a specific effect."""
        return self.alias_structure.get(effect, [effect])

    def resolution(self) -> int:
        """Compute the resolution of the design.

        Resolution is the minimum number of letters in any term 
        (other than I) in the defining relation.
        """
        def_terms = self.defining_relation.split(' = ')
        min_len = float('inf')
        for term in def_terms:
            if term != 'I':
                min_len = min(min_len, len(term))
        return min_len if min_len != float('inf') else self.k

    def foldover(self, columns: Optional[List[str]] = None) -> pd.DataFrame:
        """
        Create a foldover design.

        Parameters
        ----------
        columns : list of str, optional
            Columns to reverse signs. If None, full foldover (all columns).
        """
        if columns is None:
            columns = self.factors

        folded = self.design_matrix.copy()
        for col in columns:
            if col in folded.columns:
                folded[col] = -folded[col]

        return folded

    def combine_with_foldover(self, columns: Optional[List[str]] = None) -> pd.DataFrame:
        """Combine original design with foldover."""
        folded = self.foldover(columns)
        combined = pd.concat([self.design_matrix, folded], ignore_index=True)
        combined['Run'] = range(1, len(combined) + 1)
        return combined

    def __repr__(self):
        return "FractionalFactorialDesign(2^{}-{}, n={}, resolution={})".format(
            self.k, self.p, self.n, self.resolution())


# =============================================================================
# SECTION 2: VISUALIZATION FUNCTIONS
# =============================================================================

def plot_design_matrix(design: FractionalFactorialDesign, save_path: Optional[str] = None):
    """Visualize the design matrix as a heatmap."""
    fig, ax = plt.subplots(figsize=(max(8, design.k * 0.8), max(4, design.n * 0.3)))

    data = design.design_matrix.values
    im = ax.imshow(data, cmap='RdBu_r', aspect='auto', vmin=-1, vmax=1)

    ax.set_xticks(range(design.k))
    ax.set_xticklabels(design.factors, fontsize=12)
    ax.set_yticks(range(design.n))
    ax.set_yticklabels(['Run {}'.format(i+1) for i in range(design.n)], fontsize=9)

    # Add text annotations
    for i in range(design.n):
        for j in range(design.k):
            text = ax.text(j, i, '{:+.0f}'.format(data[i, j]),
                          ha="center", va="center", color="black", fontsize=9)

    ax.set_title('Design Matrix: 2^{}-{} (Resolution {})'.format(
        design.k, design.p, design.resolution()), fontsize=14, fontweight='bold')
    plt.colorbar(im, ax=ax, label='Factor Level')
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()


def plot_alias_structure(design: FractionalFactorialDesign, max_order: int = 3, 
                         save_path: Optional[str] = None):
    """Visualize the alias structure as text."""
    fig, ax = plt.subplots(figsize=(14, 10))

    # Collect alias chains up to max_order
    chains = []
    for r in range(1, max_order + 1):
        for combo in combinations(design.factors, r):
            effect = ''.join(combo)
            alias_chain = design.get_alias_chain(effect)
            if len(alias_chain) > 1:
                chains.append((effect, alias_chain))

    # Create a simple text-based visualization
    colors = plt.cm.Set3(np.linspace(0, 1, max(len(chains), 1)))

    for idx, (effect, aliases) in enumerate(chains[:20]):  # Limit to 20 for readability
        alias_parts = [a for a in aliases if a != effect]
        chain_text = effect + "  <->  " + "  <->  ".join(alias_parts)
        ax.text(0.02, 1 - (idx * 0.05), chain_text, fontsize=10, 
                transform=ax.transAxes, color=colors[idx],
                family='monospace', va='top')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    title_text = 'Alias Structure: {}\n(Showing up to {}-factor interactions)'.format(
        design.defining_relation, max_order)
    ax.set_title(title_text, fontsize=14, fontweight='bold', pad=20)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()


def plot_half_normal(effects: pd.Series, title: str = "Half-Normal Plot", 
                     save_path: Optional[str] = None):
    """Create a half-normal probability plot of effects."""
    fig, ax = plt.subplots(figsize=(10, 6))

    effects_sorted = effects.abs().sort_values()
    n = len(effects_sorted)

    # Half-normal scores
    ranks = np.arange(1, n + 1)
    half_normal_scores = stats.norm.ppf(0.5 + 0.5 * (ranks - 0.5) / n)

    ax.scatter(half_normal_scores, effects_sorted.values, s=80, alpha=0.7, c='steelblue', edgecolors='black')

    # Label significant effects
    for i, (idx, val) in enumerate(effects_sorted.items()):
        if val > np.percentile(effects_sorted, 75):
            ax.annotate(idx, (half_normal_scores[i], val), 
                       textcoords="offset points", xytext=(5, 5), fontsize=9)

    ax.set_xlabel('Half-Normal Score', fontsize=12)
    ax.set_ylabel('|Effect|', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()


def plot_pareto(effects: pd.Series, title: str = "Pareto Chart of Effects",
                save_path: Optional[str] = None):
    """Create a Pareto chart of effect magnitudes."""
    fig, ax = plt.subplots(figsize=(12, 6))

    effects_abs = effects.abs().sort_values(ascending=True)

    colors = ['crimson' if v > np.percentile(effects_abs, 80) else 'steelblue' 
              for v in effects_abs.values]

    bars = ax.barh(range(len(effects_abs)), effects_abs.values, color=colors, edgecolor='black', alpha=0.8)

    ax.set_yticks(range(len(effects_abs)))
    ax.set_yticklabels(effects_abs.index, fontsize=10)
    ax.set_xlabel('|Effect|', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.grid(True, axis='x', alpha=0.3)

    # Add threshold line
    threshold = np.percentile(effects_abs, 80)
    ax.axvline(threshold, color='red', linestyle='--', linewidth=2, label='80th percentile ({:.2f})'.format(threshold))
    ax.legend()

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()


def plot_foldover_comparison(original: pd.DataFrame, folded: pd.DataFrame, 
                             response_orig: np.ndarray, response_fold: np.ndarray,
                             save_path: Optional[str] = None):
    """Compare original and foldover designs with responses."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Original design
    ax1 = axes[0]
    x = np.arange(len(response_orig))
    ax1.bar(x, response_orig, color='steelblue', alpha=0.7, edgecolor='black')
    ax1.set_xlabel('Run', fontsize=11)
    ax1.set_ylabel('Response', fontsize=11)
    ax1.set_title('Original Design', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels([str(i+1) for i in x], fontsize=9)
    ax1.grid(True, axis='y', alpha=0.3)

    # Foldover design
    ax2 = axes[1]
    x = np.arange(len(response_fold))
    ax2.bar(x, response_fold, color='coral', alpha=0.7, edgecolor='black')
    ax2.set_xlabel('Run', fontsize=11)
    ax2.set_ylabel('Response', fontsize=11)
    ax2.set_title('Foldover Design', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels([str(i+1) for i in x], fontsize=9)
    ax2.grid(True, axis='y', alpha=0.3)

    plt.suptitle('Original vs. Foldover Design Responses', fontsize=14, fontweight='bold')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()


def plot_dealiasing_results(effects_before: pd.Series, effects_after: pd.Series,
                            title: str = "Dealiasing Results", save_path: Optional[str] = None):
    """Compare effect estimates before and after dealiasing."""
    fig, ax = plt.subplots(figsize=(12, 7))

    common_effects = list(set(effects_before.index) & set(effects_after.index))
    common_effects.sort()

    x = np.arange(len(common_effects))
    width = 0.35

    before_vals = [effects_before.get(e, 0) for e in common_effects]
    after_vals = [effects_after.get(e, 0) for e in common_effects]

    bars1 = ax.bar(x - width/2, before_vals, width, label='Before Dealiasing', 
                   color='lightcoral', alpha=0.8, edgecolor='black')
    bars2 = ax.bar(x + width/2, after_vals, width, label='After Dealiasing', 
                   color='lightgreen', alpha=0.8, edgecolor='black')

    ax.set_xlabel('Effect', fontsize=12)
    ax.set_ylabel('Effect Estimate', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(common_effects, rotation=45, ha='right', fontsize=9)
    ax.legend(fontsize=11)
    ax.grid(True, axis='y', alpha=0.3)
    ax.axhline(0, color='black', linewidth=0.8)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()


def plot_projection(design: FractionalFactorialDesign, active_factors: List[str],
                    response: np.ndarray, save_path: Optional[str] = None):
    """Visualize the projected full factorial in active factors."""
    fig, axes = plt.subplots(1, len(active_factors), figsize=(5 * len(active_factors), 5))

    if len(active_factors) == 1:
        axes = [axes]

    for idx, factor in enumerate(active_factors):
        ax = axes[idx]
        factor_levels = design.design_matrix[factor].values

        low_mask = factor_levels == -1
        high_mask = factor_levels == 1

        ax.scatter([-1] * sum(low_mask), response[low_mask], 
                  s=100, alpha=0.7, color='steelblue', edgecolors='black', label='Low (-1)')
        ax.scatter([1] * sum(high_mask), response[high_mask], 
                  s=100, alpha=0.7, color='coral', edgecolors='black', label='High (+1)')

        ax.set_xlabel('{} Level'.format(factor), fontsize=11)
        ax.set_ylabel('Response', fontsize=11)
        ax.set_title('Main Effect of {}'.format(factor), fontsize=12, fontweight='bold')
        ax.set_xticks([-1, 1])
        ax.set_xticklabels(['Low', 'High'])
        ax.legend()
        ax.grid(True, alpha=0.3)

    plt.suptitle('Projected Design in Active Factors: {}'.format(", ".join(active_factors)), 
                 fontsize=14, fontweight='bold')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()


def plot_d_optimal_aug(original_design: pd.DataFrame, augmented_design: pd.DataFrame,
                       save_path: Optional[str] = None):
    """Visualize D-optimal augmentation."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    factors = [c for c in original_design.columns if c not in ['Run']]

    # Original
    ax1 = axes[0]
    im1 = ax1.imshow(original_design[factors].values, cmap='RdBu_r', aspect='auto', vmin=-1, vmax=1)
    ax1.set_xticks(range(len(factors)))
    ax1.set_xticklabels(factors, fontsize=10)
    ax1.set_yticks(range(len(original_design)))
    ax1.set_yticklabels(['R{}'.format(i+1) for i in range(len(original_design))], fontsize=8)
    ax1.set_title('Original Design ({} runs)'.format(len(original_design)), fontsize=12, fontweight='bold')
    plt.colorbar(im1, ax=ax1)

    # Augmented
    ax2 = axes[1]
    im2 = ax2.imshow(augmented_design[factors].values, cmap='RdBu_r', aspect='auto', vmin=-1, vmax=1)
    ax2.set_xticks(range(len(factors)))
    ax2.set_xticklabels(factors, fontsize=10)
    ax2.set_yticks(range(len(augmented_design)))
    n_orig = len(original_design)
    n_aug = len(augmented_design)
    ylabels = ['R{}'.format(i+1) for i in range(n_orig)] + ['A{}'.format(i+1) for i in range(n_aug - n_orig)]
    ax2.set_yticklabels(ylabels, fontsize=8)
    ax2.set_title('Augmented Design ({} runs)'.format(n_aug), fontsize=12, fontweight='bold')
    plt.colorbar(im2, ax=ax2)

    plt.suptitle('D-Optimal Augmentation', fontsize=14, fontweight='bold')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()


# =============================================================================
# SECTION 3: ANALYSIS FUNCTIONS
# =============================================================================

def compute_effects(design_df: pd.DataFrame, response: np.ndarray, 
                    max_order: int = 2) -> pd.Series:
    """
    Compute effect estimates for all terms up to max_order.
    """
    factors = [c for c in design_df.columns if c not in ['Run']]

    effects = {}

    # Main effects
    for f in factors:
        effects[f] = np.mean(response[design_df[f].values == 1]) - \
                     np.mean(response[design_df[f].values == -1])

    # Interactions
    for order in range(2, max_order + 1):
        for combo in combinations(factors, order):
            interaction_col = np.ones(len(design_df))
            for f in combo:
                interaction_col *= design_df[f].values

            effect = np.mean(response[interaction_col == 1]) - \
                     np.mean(response[interaction_col == -1])
            effects[''.join(combo)] = effect

    return pd.Series(effects)


def lenths_method(effects: pd.Series, alpha: float = 0.05) -> pd.Series:
    """
    Apply Lenth's method to identify significant effects.
    """
    effects_array = effects.values
    s0 = 1.5 * np.median(np.abs(effects_array))

    # Pseudo standard error
    filtered = effects_array[np.abs(effects_array) < 2.5 * s0]
    if len(filtered) > 0:
        PSE = 1.5 * np.median(np.abs(filtered))
    else:
        PSE = s0

    # Marginal error (approximate critical value)
    n = len(effects_array)
    ME = PSE * stats.t.ppf(1 - alpha / 2, n / 3)

    significant = np.abs(effects) > ME
    return significant


def fit_model(design_df: pd.DataFrame, response: np.ndarray, 
              terms: List[str], model_type: str = 'ols') -> object:
    """
    Fit a regression model to the design data.
    """
    # Build X matrix
    X = np.ones((len(design_df), 1))  # Intercept
    term_names = ['Intercept']

    for term in terms:
        if term == 'Intercept':
            continue
        col = np.ones(len(design_df))
        for char in term:
            col *= design_df[char].values
        X = np.column_stack([X, col])
        term_names.append(term)

    if model_type == 'ols':
        model = LinearRegression(fit_intercept=False)
    elif model_type == 'ridge':
        model = Ridge(alpha=1.0, fit_intercept=False)
    elif model_type == 'lasso':
        model = Lasso(alpha=0.1, fit_intercept=False)
    else:
        raise ValueError("Unknown model_type: {}".format(model_type))

    model.fit(X, response)
    model.term_names_ = term_names
    model.X_design_ = X

    return model


def d_optimal_augment(original_design: pd.DataFrame, n_add: int, 
                      factors: List[str]) -> pd.DataFrame:
    """
    Generate D-optimal augmentation runs.
    """
    k = len(factors)

    # Build model matrix for original design (main effects + 2FI)
    X_orig = np.ones((len(original_design), 1))
    for f in factors:
        X_orig = np.column_stack([X_orig, original_design[f].values])
    for combo in combinations(factors, 2):
        col = original_design[combo[0]].values * original_design[combo[1]].values
        X_orig = np.column_stack([X_orig, col])

    # Objective: maximize det(X'X) for combined matrix
    def objective(candidate_flat):
        candidate = candidate_flat.reshape(n_add, k)
        X_cand = np.ones((n_add, 1))
        for i, f in enumerate(factors):
            X_cand = np.column_stack([X_cand, candidate[:, i]])
        for combo in combinations(range(k), 2):
            col = candidate[:, combo[0]] * candidate[:, combo[1]]
            X_cand = np.column_stack([X_cand, col])

        X_combined = np.vstack([X_orig, X_cand])
        XtX = X_combined.T @ X_combined
        # Add small regularization for numerical stability
        return -np.log(det(XtX + 0.001 * np.eye(XtX.shape[0])))

    # Optimize using differential evolution
    bounds = [(-1, 1)] * (n_add * k)
    result = differential_evolution(objective, bounds, maxiter=500, seed=42, 
                                   polish=True, tol=1e-6)

    # Round to -1 or 1
    best_runs = np.sign(result.x.reshape(n_add, k))

    # Create augmented dataframe
    augmented = original_design.copy()
    for i in range(n_add):
        new_row = {f: best_runs[i, j] for j, f in enumerate(factors)}
        augmented = pd.concat([augmented, pd.DataFrame([new_row])], ignore_index=True)

    return augmented


def bayesian_dealiasing(effects: pd.Series, alias_structure: Dict[str, List[str]],
                        prior_main: float = 0.3, prior_interaction: float = 0.1,
                        sigma: float = 1.0) -> pd.DataFrame:
    """
    Bayesian dealiasing using effect heredity priors.
    """
    results = []

    for effect, observed_effect in effects.items():
        aliases = alias_structure.get(effect, [effect])

        # Prior for this effect being the true source
        if len(effect) == 1:
            prior = prior_main
        elif len(effect) == 2:
            prior = prior_interaction
        else:
            prior = 0.05  # Higher-order interactions unlikely

        # Likelihood
        likelihood = stats.norm.pdf(observed_effect, loc=observed_effect, scale=sigma)

        # Posterior (simplified)
        posterior = prior * likelihood

        results.append({
            'Effect': effect,
            'Observed': observed_effect,
            'Alias_Chain': ', '.join(aliases),
            'Prior': prior,
            'Likelihood': likelihood,
            'Posterior': posterior
        })

    df = pd.DataFrame(results)
    # Normalize posteriors
    total = df['Posterior'].sum()
    if total > 0:
        df['Posterior_Norm'] = df['Posterior'] / total
    else:
        df['Posterior_Norm'] = 1.0 / len(df)

    return df


# =============================================================================
# SECTION 4: CASE STUDIES
# =============================================================================

def case_study_1_chemical_process():
    """
    Case Study 1: Chemical Process Optimization (2^5-1 -> Full Foldover)
    """
    print("=" * 70)
    print("CASE STUDY 1: Chemical Process Optimization")
    print("2^5-1 Resolution V Design -> Full Foldover -> Full 2^5")
    print("=" * 70)

    # Create 2^5-1 design
    design = FractionalFactorialDesign(k=5, p=1)
    print("\nDesign: {}".format(design))
    print("Defining Relation: {}".format(design.defining_relation))
    print("Resolution: {}".format(design.resolution()))

    # True model: Y = 50 + 8A + 6B + 5AB + 3C + noise
    np.random.seed(42)
    true_effects = {'A': 8, 'B': 6, 'C': 3, 'AB': 5}
    noise = np.random.normal(0, 1.5, design.n)

    response = (50 + 
                true_effects['A'] * design.design_matrix['A'].values +
                true_effects['B'] * design.design_matrix['B'].values +
                true_effects['C'] * design.design_matrix['C'].values +
                true_effects['AB'] * (design.design_matrix['A'].values * 
                                       design.design_matrix['B'].values) +
                noise)

    # Compute effects from fractional design
    effects_frac = compute_effects(design.design_matrix, response, max_order=2)
    print("\nEffects from 2^5-1 Fractional Design:")
    print(effects_frac.round(3))

    print("\nAB effect estimate: {:.3f} (True: 5.0)".format(effects_frac['AB']))

    # Full foldover to create full 2^5
    combined = design.combine_with_foldover()
    folded_response = (50 + 
                       true_effects['A'] * combined['A'].values[design.n:] +
                       true_effects['B'] * combined['B'].values[design.n:] +
                       true_effects['C'] * combined['C'].values[design.n:] +
                       true_effects['AB'] * (combined['A'].values[design.n:] * 
                                            combined['B'].values[design.n:]) +
                       np.random.normal(0, 1.5, design.n))

    full_response = np.concatenate([response, folded_response])
    effects_full = compute_effects(combined, full_response, max_order=2)

    print("\nEffects from Full 2^5 (after foldover):")
    print(effects_full.round(3))

    # Visualizations
    plot_design_matrix(design, save_path='./figures/cs1_design_matrix.png')
    plot_half_normal(effects_frac, title="CS1: Half-Normal Plot (Fractional)",
                     save_path='./figures/cs1_half_normal_frac.png')
    plot_dealiasing_results(effects_frac, effects_full,
                            title="CS1: Dealiasing via Full Foldover",
                            save_path='./figures/cs1_dealiasing.png')

    # Save model
    model = fit_model(combined, full_response, ['A', 'B', 'C', 'AB'], model_type='ols')
    joblib.dump(model, './models/cs1_model.joblib')
    print("\nModel saved to models/cs1_model.joblib")

    return design, effects_frac, effects_full


def case_study_2_semiconductor():
    """
    Case Study 2: Semiconductor Etching (2^7-4 -> D-Optimal Augmentation)
    """
    print("\n" + "=" * 70)
    print("CASE STUDY 2: Semiconductor Etching")
    print("2^7-4 Resolution III Design -> D-Optimal Augmentation")
    print("=" * 70)

    design = FractionalFactorialDesign(k=7, p=4)
    print("\nDesign: {}".format(design))
    print("Defining Relation: {}".format(design.defining_relation))
    print("Resolution: {}".format(design.resolution()))

    # True model: A, C, F main effects + AF interaction
    np.random.seed(123)
    true_effects = {'A': 5, 'C': 4, 'F': 3, 'AF': 4}
    noise = np.random.normal(0, 2, design.n)

    response = (30 +
                true_effects['A'] * design.design_matrix['A'].values +
                true_effects['C'] * design.design_matrix['C'].values +
                true_effects['F'] * design.design_matrix['F'].values +
                true_effects['AF'] * (design.design_matrix['A'].values * 
                                     design.design_matrix['F'].values) +
                noise)

    effects_frac = compute_effects(design.design_matrix, response, max_order=2)
    print("\nEffects from 2^7-4 Fractional Design (Resolution III):")
    print(effects_frac.round(3))

    print("\nAlias chains (showing A's confounding):")
    print("A aliases with: {}".format(design.get_alias_chain('A')))

    # D-optimal augmentation: add 4 runs
    factors = design.factors
    augmented = d_optimal_augment(design.design_matrix, n_add=4, factors=factors)

    # Generate responses for augmented runs
    aug_response = (30 +
                    true_effects['A'] * augmented['A'].values[design.n:] +
                    true_effects['C'] * augmented['C'].values[design.n:] +
                    true_effects['F'] * augmented['F'].values[design.n:] +
                    true_effects['AF'] * (augmented['A'].values[design.n:] * 
                                         augmented['F'].values[design.n:]) +
                    np.random.normal(0, 2, 4))

    full_response = np.concatenate([response, aug_response])
    effects_aug = compute_effects(augmented, full_response, max_order=2)

    print("\nEffects after D-Optimal Augmentation (12 runs total):")
    print(effects_aug.round(3))

    # Visualizations
    plot_alias_structure(design, max_order=2, 
                         save_path='./figures/cs2_alias_structure.png')
    plot_pareto(effects_frac, title="CS2: Pareto Chart (Resolution III)",
                save_path='./figures/cs2_pareto.png')
    plot_d_optimal_aug(design.design_matrix, augmented,
                       save_path='./figures/cs2_d_optimal.png')
    plot_dealiasing_results(effects_frac, effects_aug,
                            title="CS2: Dealiasing via D-Optimal Augmentation",
                            save_path='./figures/cs2_dealiasing.png')

    model = fit_model(augmented, full_response, ['A', 'C', 'F', 'AF'], model_type='ols')
    joblib.dump(model, './models/cs2_model.joblib')
    print("\nModel saved to models/cs2_model.joblib")

    return design, effects_frac, effects_aug


def case_study_3_pharmaceutical():
    """
    Case Study 3: Pharmaceutical Tablet Formulation (2^4-1 -> Projection)
    """
    print("\n" + "=" * 70)
    print("CASE STUDY 3: Pharmaceutical Tablet Formulation")
    print("2^4-1 Resolution IV Design -> Projection to 2^2")
    print("=" * 70)

    design = FractionalFactorialDesign(k=4, p=1)
    print("\nDesign: {}".format(design))
    print("Defining Relation: {}".format(design.defining_relation))
    print("Resolution: {}".format(design.resolution()))

    # True model: A, B main effects + AB interaction (C and D are inactive)
    np.random.seed(456)
    true_effects = {'A': 7, 'B': 5, 'AB': 4}
    noise = np.random.normal(0, 1, design.n)

    response = (40 +
                true_effects['A'] * design.design_matrix['A'].values +
                true_effects['B'] * design.design_matrix['B'].values +
                true_effects['AB'] * (design.design_matrix['A'].values * 
                                     design.design_matrix['B'].values) +
                noise)

    effects_frac = compute_effects(design.design_matrix, response, max_order=2)
    print("\nEffects from 2^4-1 Fractional Design:")
    print(effects_frac.round(3))

    # Check projection: C and D are inactive
    print("\nC and D appear inactive. Projecting to 2^2 in A and B...")
    active_factors = ['A', 'B']

    # In the projected 2^2, AB is cleanly estimated
    projected_effects = compute_effects(design.design_matrix[active_factors], response, max_order=2)
    print("\nEffects in projected 2^2 design:")
    print(projected_effects.round(3))

    # Visualizations
    plot_projection(design, active_factors, response,
                    save_path='./figures/cs3_projection.png')
    plot_half_normal(effects_frac, title="CS3: Half-Normal Plot (Before Projection)",
                     save_path='./figures/cs3_half_normal.png')
    plot_dealiasing_results(effects_frac, projected_effects,
                            title="CS3: Dealiasing via Projection",
                            save_path='./figures/cs3_dealiasing.png')

    model = fit_model(design.design_matrix[active_factors], response, ['A', 'B', 'AB'], model_type='ols')
    joblib.dump(model, './models/cs3_model.joblib')
    print("\nModel saved to models/cs3_model.joblib")

    return design, effects_frac, projected_effects


def case_study_4_automotive():
    """
    Case Study 4: Automotive Coating (2^6-2 -> Partial Foldover)
    """
    print("\n" + "=" * 70)
    print("CASE STUDY 4: Automotive Coating Process")
    print("2^6-2 Resolution IV Design -> Partial Foldover (A, B)")
    print("=" * 70)

    design = FractionalFactorialDesign(k=6, p=2)
    print("\nDesign: {}".format(design))
    print("Defining Relation: {}".format(design.defining_relation))
    print("Resolution: {}".format(design.resolution()))

    # True model: A, B, C, D main effects + AB interaction
    np.random.seed(789)
    true_effects = {'A': 6, 'B': 5, 'C': 4, 'D': 3, 'AB': 4}
    noise = np.random.normal(0, 1.5, design.n)

    response = (25 +
                true_effects['A'] * design.design_matrix['A'].values +
                true_effects['B'] * design.design_matrix['B'].values +
                true_effects['C'] * design.design_matrix['C'].values +
                true_effects['D'] * design.design_matrix['D'].values +
                true_effects['AB'] * (design.design_matrix['A'].values * 
                                     design.design_matrix['B'].values) +
                noise)

    effects_frac = compute_effects(design.design_matrix, response, max_order=2)
    print("\nEffects from 2^6-2 Fractional Design:")
    print(effects_frac.round(3))

    # Partial foldover: reverse A and B
    print("\nPerforming partial foldover (reversing A and B)...")
    combined = design.combine_with_foldover(columns=['A', 'B'])

    folded_response = (25 +
                       true_effects['A'] * combined['A'].values[design.n:] +
                       true_effects['B'] * combined['B'].values[design.n:] +
                       true_effects['C'] * combined['C'].values[design.n:] +
                       true_effects['D'] * combined['D'].values[design.n:] +
                       true_effects['AB'] * (combined['A'].values[design.n:] * 
                                            combined['B'].values[design.n:]) +
                       np.random.normal(0, 1.5, design.n))

    full_response = np.concatenate([response, folded_response])
    effects_fold = compute_effects(combined, full_response, max_order=2)

    print("\nEffects after Partial Foldover (32 runs total):")
    print(effects_fold.round(3))

    # Visualizations
    plot_foldover_comparison(design.design_matrix, design.foldover(['A', 'B']),
                             response, folded_response,
                             save_path='./figures/cs4_foldover.png')
    plot_pareto(effects_frac, title="CS4: Pareto Chart (Before Foldover)",
                save_path='./figures/cs4_pareto_before.png')
    plot_dealiasing_results(effects_frac, effects_fold,
                            title="CS4: Dealiasing via Partial Foldover",
                            save_path='./figures/cs4_dealiasing.png')

    model = fit_model(combined, full_response, ['A', 'B', 'C', 'D', 'AB'], model_type='ols')
    joblib.dump(model, './models/cs4_model.joblib')
    print("\nModel saved to models/cs4_model.joblib")

    return design, effects_frac, effects_fold


def case_study_5_food_processing():
    """
    Case Study 5: Food Processing (2^8-4 -> Bayesian Dealiasing)
    """
    print("\n" + "=" * 70)
    print("CASE STUDY 5: Food Processing")
    print("2^8-4 Resolution IV Design -> Bayesian Dealiasing")
    print("=" * 70)

    design = FractionalFactorialDesign(k=8, p=4)
    print("\nDesign: {}".format(design))
    print("Defining Relation: {}".format(design.defining_relation))
    print("Resolution: {}".format(design.resolution()))

    # True model: A, B, E main effects + AE interaction
    np.random.seed(321)
    true_effects = {'A': 5, 'B': 4, 'E': 3, 'AE': 3.5}
    noise = np.random.normal(0, 2, design.n)

    response = (35 +
                true_effects['A'] * design.design_matrix['A'].values +
                true_effects['B'] * design.design_matrix['B'].values +
                true_effects['E'] * design.design_matrix['E'].values +
                true_effects['AE'] * (design.design_matrix['A'].values * 
                                     design.design_matrix['E'].values) +
                noise)

    effects_frac = compute_effects(design.design_matrix, response, max_order=2)
    print("\nEffects from 2^8-4 Fractional Design:")
    print(effects_frac.round(3))

    # Apply Bayesian dealiasing
    print("\nApplying Bayesian Dealiasing...")
    bayesian_results = bayesian_dealiasing(effects_frac, design.alias_structure,
                                           prior_main=0.3, prior_interaction=0.1,
                                           sigma=2.0)

    print("\nTop 10 effects by posterior probability:")
    top_effects = bayesian_results.nlargest(10, 'Posterior_Norm')[['Effect', 'Observed', 'Posterior_Norm']]
    print(top_effects.to_string(index=False))

    # Visualizations
    fig, ax = plt.subplots(figsize=(12, 7))
    top_15 = bayesian_results.nlargest(15, 'Posterior_Norm')
    colors = ['crimson' if p > 0.05 else 'steelblue' for p in top_15['Posterior_Norm']]
    ax.barh(range(len(top_15)), top_15['Posterior_Norm'].values, color=colors, alpha=0.8, edgecolor='black')
    ax.set_yticks(range(len(top_15)))
    ax.set_yticklabels(top_15['Effect'].values, fontsize=10)
    ax.set_xlabel('Posterior Probability', fontsize=12)
    ax.set_title('CS5: Bayesian Posterior Probabilities', fontsize=14, fontweight='bold')
    ax.grid(True, axis='x', alpha=0.3)
    plt.tight_layout()
    plt.savefig('./figures/cs5_bayesian.png', dpi=150, bbox_inches='tight')
    plt.show()

    plot_half_normal(effects_frac, title="CS5: Half-Normal Plot (Before Bayesian)",
                     save_path='./figures/cs5_half_normal.png')

    # Save results
    bayesian_results.to_csv('./models/cs5_bayesian_results.csv', index=False)
    print("\nBayesian results saved to models/cs5_bayesian_results.csv")

    return design, effects_frac, bayesian_results


# =============================================================================
# SECTION 5: MAIN EXECUTION
# =============================================================================
import os

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("DoE LECTURE 13: DEALIASING FRACTIONAL DESIGNS")
    print("=" * 70)
    os.makedirs('./figures', exist_ok=True)
    os.makedirs('./models', exist_ok=True)

    # Run all case studies
    cs1 = case_study_1_chemical_process()
    cs2 = case_study_2_semiconductor()
    cs3 = case_study_3_pharmaceutical()
    cs4 = case_study_4_automotive()
    cs5 = case_study_5_food_processing()

    print("\n" + "=" * 70)
    print("ALL CASE STUDIES COMPLETED SUCCESSFULLY")
    print("=" * 70)
    print("\nGenerated outputs:")
    print("  - README.md (overview and concepts)")
    print("  - code.py (this module)")
    print("  - figures/ (7+ visualization files)")
    print("  - models/ (5 fitted models + 1 CSV)")
