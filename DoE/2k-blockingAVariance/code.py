"""
DoE Lecture 11: 2^k Blocking and Variance
==========================================

A comprehensive Python implementation for blocking in 2^k factorial designs.
Includes: design generation, confounding analysis, partial confounding,
variance components, ANOVA with blocks, and visualization functions.

Usage:
    python code.py

Author: DoE Lecture Series
Date: 2026-08-07
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations, product
from typing import List, Dict, Tuple, Optional
import json
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Create output directories
os.makedirs('./figures', exist_ok=True)
os.makedirs('./models', exist_ok=True)


# ============================================================
# CLASS: BlockingDesign
# ============================================================

class BlockingDesign:
    """
    2^k Blocking and Variance Analysis

    Handles full factorial designs with blocking, confounding structures,
    partial confounding, generalized interaction tables, and ANOVA with blocks.

    Parameters
    ----------
    factors : list of str
        Factor names, e.g., ['A', 'B', 'C']
    block_defining_contrast : str, optional
        Pre-defined block contrast (auto-computed if not provided)

    Attributes
    ----------
    k : int
        Number of factors
    n_runs : int
        Total number of experimental runs (2^k)
    design_matrix : ndarray
        Coded design matrix (-1, +1)
    design_df : DataFrame
        Design matrix as pandas DataFrame
    blocks : ndarray
        Block assignment for each run
    aliases : dict
        Confounding/alias structure
    """

    def __init__(self, factors: List[str], block_defining_contrast: Optional[str] = None):
        self.factors = factors
        self.k = len(factors)
        self.n_runs = 2 ** self.k
        self.block_defining_contrast = block_defining_contrast
        self.design_matrix = None
        self.blocks = None
        self.aliases = {}
        self.block_generators = []
        self.n_blocks = 1
        self._build_design()

    def _build_design(self):
        """Build full 2^k design matrix in standard Yates order."""
        levels = [-1, 1]
        self.design_matrix = np.array(list(product(*[levels]*self.k)))
        self.design_df = pd.DataFrame(
            self.design_matrix, 
            columns=self.factors
        )

    def set_blocks(self, block_generators: List[str]):
        """
        Set blocking using generators (partial or complete confounding).

        Parameters
        ----------
        block_generators : list of str
            Block defining generators, e.g., ['ABC'] for 2 blocks,
            ['ABC', 'CDE'] for 4 blocks in a 2^5 design.
        """
        self.block_generators = block_generators
        self.n_blocks = 2 ** len(block_generators)

        # Calculate block defining contrast (generalized interaction)
        if len(block_generators) == 1:
            self.block_defining_contrast = block_generators[0]
        else:
            self.block_defining_contrast = self._generalized_interaction(block_generators)

        # Assign blocks using binary encoding of generator signs
        self.blocks = np.zeros(self.n_runs, dtype=int)
        for i, gen in enumerate(block_generators):
            col = self._interaction_column(gen)
            self.blocks += (col == 1).astype(int) * (2 ** i)

        self.design_df['Block'] = self.blocks

        # Build alias structure
        self._build_alias_structure()

    def _interaction_column(self, term: str) -> np.ndarray:
        """
        Get interaction column for a term like 'ABC'.

        Parameters
        ----------
        term : str
            Interaction term, e.g., 'AB', 'ABC'

        Returns
        -------
        ndarray
            Column of +1/-1 values
        """
        col = np.ones(self.n_runs)
        for char in term:
            if char in self.factors:
                idx = self.factors.index(char)
                col *= self.design_matrix[:, idx]
        return col

    def _generalized_interaction(self, terms: List[str]) -> str:
        """
        Calculate generalized interaction of multiple terms.

        Uses mod-2 multiplication: each factor appears in result if it
        appears an odd number of times across all terms.

        Parameters
        ----------
        terms : list of str
            Terms to multiply, e.g., ['ABC', 'ABD']

        Returns
        -------
        str
            Generalized interaction, e.g., 'CD'
        """
        all_chars = set()
        for term in terms:
            all_chars.update(list(term))

        result = []
        for char in sorted(all_chars):
            count = sum(1 for t in terms if char in t)
            if count % 2 == 1:
                result.append(char)

        return ''.join(result) if result else 'I'

    def _multiply_terms(self, term1: str, term2: str) -> str:
        """
        Multiply two terms (mod 2 on each factor).

        Parameters
        ----------
        term1, term2 : str
            Terms to multiply

        Returns
        -------
        str
            Product term
        """
        chars1 = list(term1)
        chars2 = list(term2)

        all_chars = set(chars1 + chars2)
        result = []
        for char in sorted(all_chars):
            count = (1 if char in chars1 else 0) + (1 if char in chars2 else 0)
            if count % 2 == 1:
                result.append(char)

        return ''.join(result) if result else 'I'

    def _build_alias_structure(self):
        """Build confounding/alias structure from block defining contrast."""
        if not self.block_generators:
            return

        # All possible effects
        all_effects = []
        for r in range(1, self.k + 1):
            for combo in combinations(self.factors, r):
                all_effects.append(''.join(combo))

        # Group by alias
        aliases = {}
        processed = set()

        for effect in all_effects:
            if effect in processed:
                continue
            confounded = self._multiply_terms(effect, self.block_defining_contrast)
            if confounded != effect:
                aliases[effect] = [effect, confounded]
                processed.add(effect)
                processed.add(confounded)
            else:
                aliases[effect] = [effect]  # Self-confounded (rare)
                processed.add(effect)

        self.aliases = aliases

    def get_block_layout(self) -> List[pd.DataFrame]:
        """
        Get experimental runs organized by block.

        Returns
        -------
        list of DataFrame
            One DataFrame per block with factor levels
        """
        layout = []
        for b in range(self.n_blocks):
            block_runs = self.design_df[self.design_df['Block'] == b].copy()
            block_runs['Run'] = range(1, len(block_runs) + 1)
            layout.append(block_runs)
        return layout

    def calculate_effects(self, response: np.ndarray) -> Dict[str, float]:
        """
        Calculate main effects and interactions, accounting for blocks.

        Parameters
        ----------
        response : ndarray
            Response values for each run

        Returns
        -------
        dict
            Effect estimates for all terms
        """
        effects = {}

        # Main effects
        for factor in self.factors:
            col = self.design_df[factor].values
            effects[factor] = np.mean(response[col == 1]) - np.mean(response[col == -1])

        # Interactions
        for r in range(2, self.k + 1):
            for combo in combinations(self.factors, r):
                term = ''.join(combo)
                col = self._interaction_column(term)
                effects[term] = np.mean(response[col == 1]) - np.mean(response[col == -1])

        return effects

    def anova_with_blocks(self, response: np.ndarray) -> pd.DataFrame:
        """
        ANOVA accounting for block effects.

        Parameters
        ----------
        response : ndarray
            Response values

        Returns
        -------
        DataFrame
            ANOVA table with blocks, treatments, and error
        """
        n = len(response)
        grand_mean = np.mean(response)
        ss_total = np.sum((response - grand_mean) ** 2)

        # Block SS
        ss_blocks = 0
        for b in range(self.n_blocks):
            mask = self.blocks == b
            n_b = np.sum(mask)
            if n_b > 0:
                block_mean = np.mean(response[mask])
                ss_blocks += n_b * (block_mean - grand_mean) ** 2

        # Factor SS
        ss_factors = {}
        for factor in self.factors:
            col = self.design_df[factor].values
            contrast = np.mean(response[col == 1]) - np.mean(response[col == -1])
            ss_factors[factor] = n * contrast ** 2 / 4

        for r in range(2, self.k + 1):
            for combo in combinations(self.factors, r):
                term = ''.join(combo)
                col = self._interaction_column(term)
                contrast = np.mean(response[col == 1]) - np.mean(response[col == -1])
                ss_factors[term] = n * contrast ** 2 / 4

        # Error SS (higher-order interactions as proxy)
        ss_error = 0
        df_error = max(0, n - 1 - (self.n_blocks - 1) - len(ss_factors))

        anova_table = pd.DataFrame({
            'Source': ['Blocks'] + list(ss_factors.keys()) + ['Error', 'Total'],
            'SS': [ss_blocks] + list(ss_factors.values()) + [ss_error, ss_total],
            'df': [self.n_blocks - 1] + [1]*len(ss_factors) + [df_error, n-1]
        })

        anova_table['MS'] = anova_table['SS'] / anova_table['df'].replace(0, np.nan)

        return anova_table

    def get_confounded_effects(self) -> List[str]:
        """Return list of all confounded effects."""
        confounded = set()
        for effects in self.aliases.values():
            confounded.update(effects)
        return sorted(list(confounded))

    def get_estimable_effects(self) -> List[str]:
        """Return list of all estimable (unconfounded) effects."""
        all_effects = []
        for r in range(1, self.k + 1):
            for combo in combinations(self.factors, r):
                all_effects.append(''.join(combo))

        confounded = set(self.get_confounded_effects())
        return [e for e in all_effects if e not in confounded]

    def save_design(self, filepath: str):
        """Save design matrix to CSV."""
        self.design_df.to_csv(filepath, index=False)

    def __repr__(self):
        return f"BlockingDesign(k={self.k}, n_runs={self.n_runs}, n_blocks={self.n_blocks})"


# ============================================================
# VISUALIZATION FUNCTIONS
# ============================================================

def plot_block_design(design: BlockingDesign, response: Optional[np.ndarray] = None,
                      title: str = "2^k Blocking Design", save_path: Optional[str] = None):
    """Visualize blocked design layout with block assignments."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Left: Design matrix with block colors
    ax1 = axes[0]
    colors = plt.cm.Set3(np.linspace(0, 1, design.n_blocks))

    for b in range(design.n_blocks):
        mask = design.blocks == b
        subset = design.design_matrix[mask]
        if subset.shape[1] >= 2:
            ax1.scatter(subset[:, 0], subset[:, 1], 
                       c=[colors[b]], label=f'Block {b+1}', s=150, alpha=0.8, edgecolors='black')

    ax1.set_xlabel(f'{design.factors[0]} (coded)', fontsize=12)
    ax1.set_ylabel(f'{design.factors[1]} (coded)', fontsize=12)
    ax1.set_title('Experimental Layout by Block', fontsize=14, fontweight='bold')
    ax1.legend(title='Blocks')
    ax1.grid(True, alpha=0.3)
    ax1.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    ax1.axvline(x=0, color='k', linestyle='-', linewidth=0.5)

    # Right: Block assignment table
    ax2 = axes[1]
    ax2.axis('off')

    table_data = []
    for b in range(design.n_blocks):
        block_runs = design.design_df[design.design_df['Block'] == b]
        factor_levels = []
        for _, row in block_runs.iterrows():
            level = '(' + ','.join([f'{f}={int(row[f])}' for f in design.factors]) + ')'
            factor_levels.append(level)
        table_data.append([f'Block {b+1}', '\n'.join(factor_levels)])

    table = ax2.table(cellText=table_data, 
                     colLabels=['Block', 'Factor Levels'],
                     cellLoc='left', loc='center',
                     colWidths=[0.2, 0.8])
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 2.5)

    for i in range(design.n_blocks + 1):
        for j in range(2):
            cell = table[(i, j)]
            if i == 0:
                cell.set_facecolor('#4472C4')
                cell.set_text_props(color='white', fontweight='bold')
            else:
                cell.set_facecolor(colors[i-1])

    ax2.set_title('Block Assignment', fontsize=14, fontweight='bold', pad=20)
    plt.suptitle(title, fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()
    return fig


def plot_confounding_structure(design: BlockingDesign, save_path: Optional[str] = None):
    """Visualize confounding/alias structure as a table."""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('off')

    if not design.aliases:
        ax.text(0.5, 0.5, 'No confounding structure (full factorial, no blocks)', 
               ha='center', va='center', fontsize=14)
        plt.show()
        return fig

    alias_data = []
    for key, effects in design.aliases.items():
        alias_data.append([' ≡ '.join(effects), 'Confounded'])

    confounded = set()
    for effects in design.aliases.values():
        confounded.update(effects)

    all_effects = []
    for r in range(1, design.k + 1):
        for combo in combinations(design.factors, r):
            all_effects.append(''.join(combo))

    unconfounded = [e for e in all_effects if e not in confounded]
    for e in unconfounded[:10]:
        alias_data.append([e, 'Estimable'])

    table = ax.table(cellText=alias_data,
                    colLabels=['Effect', 'Status'],
                    cellLoc='center', loc='center',
                    colWidths=[0.5, 0.3])
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 2)

    for i in range(len(alias_data) + 1):
        for j in range(2):
            cell = table[(i, j)]
            if i == 0:
                cell.set_facecolor('#4472C4')
                cell.set_text_props(color='white', fontweight='bold')
            elif alias_data[i-1][1] == 'Confounded':
                cell.set_facecolor('#FFE699')
            else:
                cell.set_facecolor('#C6E0B4')

    ax.set_title(f'Confounding Structure\nBlock Defining Contrast: {design.block_defining_contrast} = I', 
                fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()
    return fig


def plot_partial_confounding_comparison(save_path: Optional[str] = None):
    """Compare complete vs partial confounding."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    ax1 = axes[0]
    categories = ['ABC\n(Confounded)', 'AB', 'AC', 'BC', 'A', 'B', 'C']
    complete_values = [0, 8.5, 6.2, 4.1, 12.3, 9.8, 7.5]
    colors1 = ['#FF6B6B' if v == 0 else '#4ECDC4' for v in complete_values]

    bars1 = ax1.bar(categories, complete_values, color=colors1, edgecolor='black')
    ax1.set_ylabel('Effect Estimate', fontsize=12)
    ax1.set_title('Complete Confounding\n(ABC lost in single replicate)', fontsize=13, fontweight='bold')
    ax1.axhline(y=0, color='black', linewidth=0.8)
    ax1.grid(axis='y', alpha=0.3)

    for bar, val in zip(bars1, complete_values):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 0.3,
                f'{val:.1f}' if val > 0 else 'Lost', ha='center', fontsize=9, fontweight='bold')

    ax2 = axes[1]
    categories2 = ['ABC\n(Rep1)', 'ABC\n(Rep2)', 'AB', 'AC', 'BC', 'A', 'B', 'C']
    partial_values = [5.2, 6.8, 8.5, 6.2, 4.1, 12.3, 9.8, 7.5]
    colors2 = ['#FFE66D', '#FFE66D'] + ['#4ECDC4'] * 6

    bars2 = ax2.bar(categories2, partial_values, color=colors2, edgecolor='black')
    ax2.set_ylabel('Effect Estimate', fontsize=12)
    ax2.set_title('Partial Confounding\n(ABC recoverable from 2 replicates)', fontsize=13, fontweight='bold')
    ax2.axhline(y=0, color='black', linewidth=0.8)
    ax2.grid(axis='y', alpha=0.3)

    for bar, val in zip(bars2, partial_values):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.3,
                f'{val:.1f}', ha='center', fontsize=9, fontweight='bold')

    plt.suptitle('Complete vs Partial Confounding in 2^3 Design', fontsize=15, fontweight='bold')
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()
    return fig


def plot_intrablock_interblock_variance(save_path: Optional[str] = None):
    """Visualize intra-block vs inter-block variance."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    ax1 = axes[0]
    np.random.seed(42)
    blocks = ['Block 1', 'Block 2', 'Block 3', 'Block 4']
    treatments = ['T1', 'T2', 'T3', 'T4']
    block_effects = [5, 8, 3, 10]

    intra_data = []
    for i, block in enumerate(blocks):
        for j, treat in enumerate(treatments):
            y = block_effects[i] + np.random.normal(0, 1.5)
            intra_data.append({'Block': block, 'Treatment': treat, 'Response': y})

    intra_df = pd.DataFrame(intra_data)

    for i, block in enumerate(blocks):
        block_data = intra_df[intra_df['Block'] == block]
        x_pos = np.arange(len(treatments)) + i * 0.2
        ax1.scatter(x_pos, block_data['Response'], label=block, s=100, alpha=0.7)
        ax1.plot(x_pos, block_data['Response'], alpha=0.3)

    ax1.set_xticks(np.arange(len(treatments)) + 0.3)
    ax1.set_xticklabels(treatments)
    ax1.set_ylabel('Response', fontsize=12)
    ax1.set_xlabel('Treatment', fontsize=12)
    ax1.set_title('Intra-block Variability\n(Within-block, treatment differences)', fontsize=13, fontweight='bold')
    ax1.legend(title='Blocks')
    ax1.grid(True, alpha=0.3)

    ax2 = axes[1]
    inter_data = []
    for treat in treatments:
        for i, block in enumerate(blocks):
            y = block_effects[i] + np.random.normal(0, 1.5)
            inter_data.append({'Treatment': treat, 'Block': block, 'Response': y})

    inter_df = pd.DataFrame(inter_data)

    for j, treat in enumerate(treatments):
        treat_data = inter_df[inter_df['Treatment'] == treat]
        x_pos = np.arange(len(blocks)) + j * 0.2
        ax2.scatter(x_pos, treat_data['Response'], label=treat, s=100, alpha=0.7)
        ax2.plot(x_pos, treat_data['Response'], alpha=0.3)

    ax2.set_xticks(np.arange(len(blocks)) + 0.3)
    ax2.set_xticklabels(blocks)
    ax2.set_ylabel('Response', fontsize=12)
    ax2.set_xlabel('Block', fontsize=12)
    ax2.set_title('Inter-block Variability\n(Between-block, same treatment)', fontsize=13, fontweight='bold')
    ax2.legend(title='Treatments')
    ax2.grid(True, alpha=0.3)

    plt.suptitle('Intra-block vs Inter-block Variance', fontsize=15, fontweight='bold')
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()
    return fig


def plot_variance_components_analysis(save_path: Optional[str] = None):
    """Visualize variance components in blocked design."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))

    np.random.seed(42)
    n_blocks = 4
    n_treatments = 4
    n_reps = 3

    sigma_block = 4.0
    sigma_treatment = 3.0
    sigma_error = 2.0

    block_effects = np.random.normal(0, sigma_block, n_blocks)
    treatment_effects = np.random.normal(0, sigma_treatment, n_treatments)

    data = []
    for b in range(n_blocks):
        for t in range(n_treatments):
            for r in range(n_reps):
                y = 50 + block_effects[b] + treatment_effects[t] + np.random.normal(0, sigma_error)
                data.append({'Block': f'B{b+1}', 'Treatment': f'T{t+1}', 'Rep': r+1, 'Response': y})

    df = pd.DataFrame(data)

    # Raw data
    ax1 = axes[0, 0]
    for b in range(n_blocks):
        block_data = df[df['Block'] == f'B{b+1}']
        ax1.scatter(block_data['Treatment'], block_data['Response'], 
                   label=f'B{b+1}', alpha=0.6, s=60)
    ax1.set_title('Raw Data by Block & Treatment', fontweight='bold')
    ax1.set_xlabel('Treatment')
    ax1.set_ylabel('Response')
    ax1.legend(title='Block')
    ax1.grid(True, alpha=0.3)

    # Block means
    ax2 = axes[0, 1]
    block_means = df.groupby('Block')['Response'].mean()
    ax2.bar(block_means.index, block_means.values, color='skyblue', edgecolor='black')
    ax2.axhline(y=df['Response'].mean(), color='red', linestyle='--', label='Grand Mean')
    ax2.set_title('Block Means', fontweight='bold')
    ax2.set_ylabel('Mean Response')
    ax2.legend()
    ax2.grid(axis='y', alpha=0.3)

    # Treatment means
    ax3 = axes[1, 0]
    treatment_means = df.groupby('Treatment')['Response'].mean()
    ax3.bar(treatment_means.index, treatment_means.values, color='lightgreen', edgecolor='black')
    ax3.axhline(y=df['Response'].mean(), color='red', linestyle='--', label='Grand Mean')
    ax3.set_title('Treatment Means (Unadjusted)', fontweight='bold')
    ax3.set_ylabel('Mean Response')
    ax3.legend()
    ax3.grid(axis='y', alpha=0.3)

    # Variance components
    ax4 = axes[1, 1]
    ms_block = df.groupby('Block')['Response'].mean().var() * n_treatments * n_reps
    ms_treatment = df.groupby('Treatment')['Response'].mean().var() * n_blocks * n_reps
    ms_error = df.groupby(['Block', 'Treatment'])['Response'].var().mean()

    components = [max(0, (ms_block - ms_error) / (n_treatments * n_reps)),
                 max(0, (ms_treatment - ms_error) / (n_blocks * n_reps)),
                 ms_error]
    labels = ['Block Variance', 'Treatment Variance', 'Error Variance']
    colors = ['#FF6B6B', '#4ECDC4', '#95E1D3']

    ax4.pie(components, labels=labels, colors=colors, autopct='%1.1f%%', 
           startangle=90, explode=(0.05, 0.05, 0))
    ax4.set_title('Variance Components', fontweight='bold')

    plt.suptitle('Variance Components Analysis in Blocked Design', fontsize=15, fontweight='bold')
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()
    return fig


def plot_repeated_confounding_patterns(save_path: Optional[str] = None):
    """Show repeated confounding patterns for partial confounding."""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.axis('off')

    table_data = [
        ['Replicate', 'Block Generator', 'Confounded Effect', 'ABC Estimate'],
        ['1', 'ABC', 'ABC', 'Not estimable'],
        ['2', 'AB', 'AB (C free)', 'Estimable'],
        ['3', 'AC', 'AC (B free)', 'Estimable'],
        ['Combined', 'Mixed', 'Partial', 'Recoverable via pooling']
    ]

    table = ax.table(cellText=table_data[1:],
                    colLabels=table_data[0],
                    cellLoc='center', loc='center',
                    colWidths=[0.2, 0.25, 0.25, 0.3])
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 2.5)

    for i in range(len(table_data)):
        for j in range(4):
            cell = table[(i, j)]
            if i == 0:
                cell.set_facecolor('#4472C4')
                cell.set_text_props(color='white', fontweight='bold')
            elif table_data[i][3] == 'Not estimable':
                cell.set_facecolor('#FF6B6B')
            elif 'Estimable' in table_data[i][3]:
                cell.set_facecolor('#C6E0B4')
            elif 'Recoverable' in table_data[i][3]:
                cell.set_facecolor('#FFE66D')
            else:
                cell.set_facecolor('#E7E6E6' if i % 2 == 0 else 'white')

    ax.set_title('Partial Confounding Strategy\n(2^3 Design, 3 Replicates)', 
                fontsize=14, fontweight='bold', pad=20)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()
    return fig


def plot_generalized_interaction_table(save_path: Optional[str] = None):
    """Visualize generalized interaction table."""
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.axis('off')

    table_data = [
        ['Block', 'Block Generators', 'Generalized Interaction', 'Confounded Effects'],
        ['1', 'ABC, CDE', 'ABDE', 'ABC, CDE, ABDE'],
        ['2', 'AB, ACD', 'BCD', 'AB, ACD, BCD'],
        ['3', 'ABC, ABD', 'CD', 'ABC, ABD, CD'],
        ['4', 'ABCD, BCDE', 'AE', 'ABCD, BCDE, AE'],
        ['5', 'ACE, BDE', 'ABCD', 'ACE, BDE, ABCD'],
    ]

    table = ax.table(cellText=table_data[1:],
                    colLabels=table_data[0],
                    cellLoc='center', loc='center',
                    colWidths=[0.1, 0.25, 0.3, 0.35])
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 2.5)

    for i in range(len(table_data)):
        for j in range(4):
            cell = table[(i, j)]
            if i == 0:
                cell.set_facecolor('#4472C4')
                cell.set_text_props(color='white', fontweight='bold')
            else:
                cell.set_facecolor('#E7E6E6' if i % 2 == 0 else 'white')

    ax.set_title('Generalized Interaction Table\n(2^k Designs in Multiple Blocks)', 
                fontsize=14, fontweight='bold', pad=20)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()
    return fig


# ============================================================
# CASE STUDIES
# ============================================================

def case_study_1_chemical_reactor() -> Tuple[BlockingDesign, np.ndarray]:
    """
    Case Study 1: Chemical Reactor Yield (2^3 in 2 blocks)

    Factors: Temperature (A), Pressure (B), Catalyst (C)
    Block on ABC (day shift vs night shift)
    """
    print("=" * 60)
    print("CASE STUDY 1: Chemical Reactor Yield")
    print("2^3 Design in 2 Blocks (Complete Confounding)")
    print("=" * 60)

    factors = ['A', 'B', 'C']
    design = BlockingDesign(factors)
    design.set_blocks(['ABC'])

    np.random.seed(123)
    true_effects = {'A': 8, 'B': -5, 'C': 3, 'AB': 2, 'AC': -1, 'BC': 1.5, 'ABC': 0.5}
    block_effect = [2, -2]

    response = []
    for i in range(8):
        y = 75
        for term, effect in true_effects.items():
            col = design._interaction_column(term)
            y += 0.5 * effect * col[i]
        y += block_effect[design.blocks[i]]
        y += np.random.normal(0, 1)
        response.append(y)

    response = np.array(response)

    print(f"\nBlock Defining Contrast: {design.block_defining_contrast} = I")
    print(f"Confounded Effects: {design.get_confounded_effects()}")

    effects = design.calculate_effects(response)
    print("\nEffect Estimates:")
    for term, effect in effects.items():
        status = "[Confounded]" if term in design.get_confounded_effects() else ""
        print(f"  {term}: {effect:.3f} {status}")

    return design, response


def case_study_2_semiconductor_etching() -> BlockingDesign:
    """
    Case Study 2: Semiconductor Etching Rate (2^4 in 4 blocks)

    Factors: Power (A), Gas Flow (B), Pressure (C), Temperature (D)
    4 blocks using ABC and ABD as generators
    """
    print("\n" + "=" * 60)
    print("CASE STUDY 2: Semiconductor Etching Rate")
    print("2^4 Design in 4 Blocks")
    print("=" * 60)

    factors = ['A', 'B', 'C', 'D']
    design = BlockingDesign(factors)
    design.set_blocks(['ABC', 'ABD'])

    print(f"\nBlock Generators: {design.block_generators}")
    print(f"Generalized Interaction: {design.block_defining_contrast}")
    print(f"Confounded Effects: {design.get_confounded_effects()}")

    return design


def case_study_3_pharmaceutical() -> BlockingDesign:
    """
    Case Study 3: Pharmaceutical Tablet Dissolution (2^5 in 8 blocks)
    """
    print("\n" + "=" * 60)
    print("CASE STUDY 3: Pharmaceutical Tablet Dissolution")
    print("2^5 Design in 8 Blocks")
    print("=" * 60)

    factors = ['A', 'B', 'C', 'D', 'E']
    design = BlockingDesign(factors)
    design.set_blocks(['ABC', 'ABD', 'CDE'])

    print(f"\nBlock Generators: {design.block_generators}")
    print(f"Generalized Interactions:")
    gens = design.block_generators
    print(f"  {gens[0]} x {gens[1]} = {design._generalized_interaction([gens[0], gens[1]])}")
    print(f"  {gens[0]} x {gens[2]} = {design._generalized_interaction([gens[0], gens[2]])}")
    print(f"  {gens[1]} x {gens[2]} = {design._generalized_interaction([gens[1], gens[2]])}")
    print(f"  {gens[0]} x {gens[1]} x {gens[2]} = {design._generalized_interaction(gens)}")

    return design


def case_study_4_variance_reduction():
    """
    Case Study 4: Variance Reduction through Blocking
    Compare CRD vs RCBD
    """
    print("\n" + "=" * 60)
    print("CASE STUDY 4: Variance Reduction (CRD vs RCBD)")
    print("=" * 60)

    np.random.seed(42)
    n_treatments = 4
    n_blocks = 4
    tau = [0, 3, 6, 9]
    beta = [0, 8, -5, 12]
    sigma = 2

    # CRD
    crd_data = []
    for t in range(n_treatments):
        for b in range(n_blocks):
            random_block = np.random.randint(0, n_blocks)
            y = 50 + tau[t] + beta[random_block] + np.random.normal(0, sigma)
            crd_data.append(y)

    crd_array = np.array(crd_data)
    crd_mse = np.var(crd_array) * (len(crd_array) - n_treatments) / (len(crd_array) - n_treatments)

    # RCBD
    rcbd_data = []
    for b in range(n_blocks):
        for t in range(n_treatments):
            y = 50 + tau[t] + beta[b] + np.random.normal(0, sigma)
            rcbd_data.append(y)

    rcbd_array = np.array(rcbd_data).reshape(n_blocks, n_treatments)
    grand_mean = np.mean(rcbd_array)
    ss_total = np.sum((rcbd_array - grand_mean)**2)
    ss_treatment = n_blocks * np.sum((np.mean(rcbd_array, axis=0) - grand_mean)**2)
    ss_block = n_treatments * np.sum((np.mean(rcbd_array, axis=1) - grand_mean)**2)
    ss_error = ss_total - ss_treatment - ss_block
    rcbd_mse = ss_error / ((n_blocks - 1) * (n_treatments - 1))

    print(f"\nCRD MSE: {crd_mse:.2f}")
    print(f"RCBD MSE: {rcbd_mse:.2f}")
    print(f"Efficiency Gain: {crd_mse / rcbd_mse:.1f}x")

    return crd_mse, rcbd_mse


# ============================================================
# MAIN EXECUTION
# ============================================================

if __name__ == "__main__":
    print("DoE Lecture 11: 2^k Blocking and Variance")
    print("=" * 60)

    # Run case studies
    d1, r1 = case_study_1_chemical_reactor()
    d2 = case_study_2_semiconductor_etching()
    d3 = case_study_3_pharmaceutical()
    crd_mse, rcbd_mse = case_study_4_variance_reduction()

    # Generate visualizations
    print("\n" + "=" * 60)
    print("GENERATING VISUALIZATIONS")
    print("=" * 60)

    plot_block_design(d1, r1, "2^3 Design in 2 Blocks", './figures/fig1_block_design.png')
    plot_confounding_structure(d2, './figures/fig2_confounding_structure.png')
    plot_partial_confounding_comparison('./figures/fig3_partial_confounding.png')
    plot_intrablock_interblock_variance('./figures/fig4_variance_types.png')
    plot_variance_components_analysis('./figures/fig7_variance_components.png')
    plot_repeated_confounding_patterns('./figures/fig8_repeated_confounding.png')
    plot_generalized_interaction_table('./figures/fig6_gen_interaction_table.png')

    print("\nAll outputs saved to ./figures/")
