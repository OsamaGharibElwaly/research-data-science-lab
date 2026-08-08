"""
DoE Lecture 12: Fractional Factorial Design
=============================================
A comprehensive Python implementation of 2^(k-p) fractional factorial designs
including design construction, aliasing analysis, visualization, and case studies.

Author: DoE Lecture Series
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations, product
from fractions import Fraction
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# FRACTIONAL FACTORIAL DESIGN CLASS
# ============================================================
class FractionalFactorialDesign:
    """
    General 2^(k-p) Fractional Factorial Design implementation.

    Parameters:
    -----------
    k : int - Number of factors
    p : int - Number of generators (fraction = 1/2^p)
    generators : list of str - Design generators (e.g., ['ABC', 'ABD'])
    coded : bool - Whether to use coded levels (-1, +1)
    """

    def __init__(self, k, p, generators=None, coded=True):
        self.k = k
        self.p = p
        self.n = 2 ** (k - p)
        self.fraction = Fraction(1, 2**p)
        self.coded = coded
        self.generators = generators if generators else []

        if not self.generators and p > 0:
            self.generators = self._auto_generators()

        self.design_matrix = None
        self.defining_relation = None
        self.resolution = None
        self.alias_structure = {}
        self._build_design()
        self._compute_defining_relation()
        self._compute_resolution()
        self._compute_alias_structure()

    def _auto_generators(self):
        """Auto-generate high-order interaction generators."""
        base_k = self.k - self.p
        base_factors = [chr(64 + i) for i in range(1, base_k + 1)]
        added_factors = [chr(64 + i) for i in range(base_k + 1, self.k + 1)]

        from itertools import combinations as comb
        all_interactions = []
        for order in range(2, base_k + 1):
            for interaction in comb(base_factors, order):
                all_interactions.append(''.join(interaction))

        generators = []
        used = set()

        for af in added_factors:
            for interaction in all_interactions:
                if interaction in used:
                    continue
                temp_gens = generators + [interaction]
                if self._check_resolution(temp_gens) >= 3:
                    generators.append(interaction)
                    used.add(interaction)
                    break

        return generators

    def _check_resolution(self, generators):
        if not generators:
            return self.k
        words = list(generators)
        for combo_len in range(2, len(generators) + 1):
            for combo in combinations(generators, combo_len):
                word = self._multiply_words(*combo)
                words.append(word)
        return min(len(w) for w in words)

    def _multiply_words(self, *words):
        from collections import Counter
        letters = []
        for w in words:
            letters.extend(list(w))
        counts = Counter(letters)
        result = ''.join(sorted([l for l, c in counts.items() if c % 2 == 1]))
        return result

    def _build_design(self):
        base_k = self.k - self.p
        base_matrix = np.array(list(product([-1, 1], repeat=base_k)))
        factor_names = [chr(64 + i) for i in range(1, self.k + 1)]
        df = pd.DataFrame(base_matrix, columns=factor_names[:base_k])

        for i, gen in enumerate(self.generators):
            col_name = factor_names[base_k + i]
            col_vals = np.ones(len(df))
            for letter in gen:
                col_vals *= df[letter].values
            df[col_name] = col_vals

        self.design_matrix = df
        return df

    def _compute_defining_relation(self):
        if self.p == 0:
            self.defining_relation = "I"
            return
        words = list(self.generators)
        for combo_len in range(2, len(self.generators) + 1):
            for combo in combinations(self.generators, combo_len):
                word = self._multiply_words(*combo)
                words.append(word)
        self.defining_relation = "I = " + " = ".join(sorted(words, key=len))

    def _compute_resolution(self):
        if self.p == 0:
            self.resolution = self.k
            return
        words = self.generators.copy()
        for combo_len in range(2, len(self.generators) + 1):
            for combo in combinations(self.generators, combo_len):
                word = self._multiply_words(*combo)
                words.append(word)
        self.resolution = min(len(w) for w in words)

    def _compute_alias_structure(self):
        if self.p == 0:
            return
        factor_names = [chr(64 + i) for i in range(1, self.k + 1)]
        all_effects = ['I']
        for order in range(1, self.k + 1):
            for combo in combinations(factor_names, order):
                all_effects.append(''.join(combo))

        def_words = self.generators.copy()
        for combo_len in range(2, len(self.generators) + 1):
            for combo in combinations(self.generators, combo_len):
                word = self._multiply_words(*combo)
                def_words.append(word)

        aliased_groups = {}
        processed = set()

        for effect in all_effects:
            if effect in processed:
                continue
            group = [effect]
            processed.add(effect)
            for word in def_words:
                aliased = self._multiply_words(effect, word)
                if aliased != effect and aliased not in processed:
                    group.append(aliased)
                    processed.add(aliased)
            group = sorted(group, key=lambda x: (len(x), x))
            if len(group) > 1:
                aliased_groups[group[0]] = group

        self.alias_structure = aliased_groups

    def get_alias_string(self, effect):
        for key, group in self.alias_structure.items():
            if effect in group:
                return ' = '.join(group)
        return effect

    def summary(self):
        roman = {3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII'}
        res_roman = roman.get(self.resolution, str(self.resolution))
        print("=" * 60)
        print(f"  FRACTIONAL FACTORIAL DESIGN: 2^({self.k}-{self.p})")
        print("=" * 60)
        print(f"  Factors (k):           {self.k}")
        print(f"  Generators (p):        {self.p}")
        print(f"  Runs (n):              {self.n}")
        print(f"  Fraction:              {self.fraction}")
        print(f"  Resolution:            {res_roman}")
        print(f"  Generators:            {', '.join(self.generators)}")
        print(f"  Defining Relation:     {self.defining_relation}")
        print("=" * 60)


# ============================================================
# VISUALIZATION FUNCTIONS
# ============================================================

def plot_design_matrix(design, title="Fractional Factorial Design Matrix", save_path=None):
    fig, ax = plt.subplots(figsize=(max(8, design.k * 0.8), max(4, design.n * 0.3)))
    matrix = design.design_matrix.values
    im = ax.imshow(matrix, cmap='RdYlBu', aspect='auto', vmin=-1, vmax=1)
    ax.set_xticks(range(design.k))
    ax.set_xticklabels(design.design_matrix.columns, fontsize=12, fontweight='bold')
    ax.set_yticks(range(design.n))
    ax.set_yticklabels([f"Run {i+1}" for i in range(design.n)], fontsize=9)
    for i in range(design.n):
        for j in range(design.k):
            ax.text(j, i, f"{matrix[i, j]:+.0f}", ha="center", va="center", color="black", fontsize=9)
    ax.set_title(title, fontsize=14, fontweight='bold', pad=15)
    plt.colorbar(im, ax=ax, label='Factor Level', shrink=0.6)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    return fig

def plot_alias_structure(design, max_order=3, save_path=None):
    fig, ax = plt.subplots(figsize=(14, 10))
    groups_to_plot = []
    for key, group in design.alias_structure.items():
        if len(key) <= max_order:
            groups_to_plot.append(group)

    if not groups_to_plot:
        ax.text(0.5, 0.5, "No aliasing up to specified order", ha='center', va='center', fontsize=14)
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
        plt.close()
        return fig

    y_pos = 0
    colors = plt.cm.Set3(np.linspace(0, 1, len(groups_to_plot)))

    for idx, group in enumerate(groups_to_plot):
        display_group = [g for g in group if len(g) <= max_order + 2]
        if len(display_group) < 2:
            continue
        x_positions = np.linspace(0.05, 0.95, len(display_group))
        for i, effect in enumerate(display_group):
            order = len(effect)
            alpha = 1.0 if order <= max_order else 0.4
            circle = plt.Circle((x_positions[i], y_pos), 0.03, color=colors[idx], alpha=alpha, ec='black', linewidth=1.5)
            ax.add_patch(circle)
            ax.text(x_positions[i], y_pos, effect, ha='center', va='center', fontsize=9, fontweight='bold')
            if i < len(display_group) - 1:
                ax.plot([x_positions[i] + 0.03, x_positions[i+1] - 0.03], [y_pos, y_pos], 'k--', alpha=0.5, linewidth=1.5)
                ax.text((x_positions[i] + x_positions[i+1])/2, y_pos + 0.02, '≡', ha='center', va='bottom', fontsize=12, color='red')
        y_pos -= 0.12

    ax.set_xlim(0, 1)
    ax.set_ylim(y_pos - 0.05, 0.1)
    ax.set_aspect('equal')
    ax.axis('off')
    roman = {3: 'III', 4: 'IV', 5: 'V', 6: 'VI'}
    res = roman.get(design.resolution, str(design.resolution))
    ax.set_title(f"Alias Structure: 2^({design.k}-{design.p}) Resolution {res}", fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    return fig

def plot_resolution_comparison(save_path=None):
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    designs = [
        ("Resolution III\n(2^(5-2))", "Main effects aliased\nwith 2FIs", 'red'),
        ("Resolution IV\n(2^(6-2))", "Main effects clear\n2FIs aliased", 'orange'),
        ("Resolution V\n(2^(5-1))", "Main effects & 2FIs clear\naliased with 3FIs+", 'green')
    ]
    for ax, (title, desc, color) in zip(axes, designs):
        levels = ['Main\nEffects', '2FIs', '3FIs', '4FIs+']
        y_positions = [0.7, 0.5, 0.3, 0.1]
        for level, y in zip(levels, y_positions):
            ax.barh(y, 0.8, height=0.12, color=color, alpha=0.3 + 0.15 * (0.7 - y))
            ax.text(0.4, y, level, ha='center', va='center', fontsize=10, fontweight='bold')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 0.9)
        ax.set_title(title, fontsize=12, fontweight='bold')
        ax.text(0.5, 0.02, desc, ha='center', va='bottom', fontsize=9, style='italic', transform=ax.transAxes)
        ax.axis('off')
    plt.suptitle("Design Resolution Hierarchy", fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    return fig

def plot_fraction_size_comparison(save_path=None):
    fig, ax = plt.subplots(figsize=(12, 7))
    factors = list(range(3, 11))
    full_factorial = [2**k for k in factors]
    half_fraction = [2**(k-1) for k in factors]
    quarter_fraction = [2**(k-2) for k in factors]
    eighth_fraction = [2**(k-3) for k in factors]
    x = np.arange(len(factors))
    width = 0.2
    bars1 = ax.bar(x - 1.5*width, full_factorial, width, label='Full Factorial (2^k)', color='#e74c3c', alpha=0.9)
    bars2 = ax.bar(x - 0.5*width, half_fraction, width, label='Half Fraction (2^(k-1))', color='#f39c12', alpha=0.9)
    bars3 = ax.bar(x + 0.5*width, quarter_fraction, width, label='Quarter Fraction (2^(k-2))', color='#3498db', alpha=0.9)
    bars4 = ax.bar(x + 1.5*width, eighth_fraction, width, label='Eighth Fraction (2^(k-3))', color='#2ecc71', alpha=0.9)
    ax.set_xlabel('Number of Factors (k)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Number of Runs', fontsize=12, fontweight='bold')
    ax.set_title('Run Size Comparison: Full vs Fractional Factorial Designs', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(factors)
    ax.set_yscale('log')
    ax.legend(fontsize=10, loc='upper left')
    ax.grid(axis='y', alpha=0.3)
    for bars in [bars1, bars2, bars3, bars4]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height, f'{int(height)}', ha='center', va='bottom', fontsize=7, fontweight='bold')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    return fig

def plot_generator_selection_guide(save_path=None):
    fig, ax = plt.subplots(figsize=(14, 8))
    scenarios = [
        {"label": "k=5, p=2\n(8 runs)", "gens": "D=AB, E=AC", "res": "III", "use": "Screening only"},
        {"label": "k=6, p=2\n(16 runs)", "gens": "E=ABC, F=BCD", "res": "IV", "use": "Main effects + some 2FIs"},
        {"label": "k=7, p=3\n(16 runs)", "gens": "E=ABC, F=ABD, G=ACD", "res": "IV", "use": "Screening many factors"},
        {"label": "k=5, p=1\n(16 runs)", "gens": "E=ABCD", "res": "V", "use": "Main effects + all 2FIs"},
        {"label": "k=8, p=3\n(32 runs)", "gens": "F=ABCD, G=ABCE, H=ABDE", "res": "IV", "use": "Large screening"},
    ]
    colors_res = {'III': '#e74c3c', 'IV': '#f39c12', 'V': '#2ecc71'}
    for i, sc in enumerate(scenarios):
        x = (i % 3) * 0.33 + 0.1
        y = 0.85 - (i // 3) * 0.45
        rect = plt.Rectangle((x, y - 0.15), 0.28, 0.35, facecolor=colors_res[sc["res"]], alpha=0.2, edgecolor=colors_res[sc["res"]], linewidth=2)
        ax.add_patch(rect)
        ax.text(x + 0.14, y + 0.15, sc["label"], ha='center', va='center', fontsize=11, fontweight='bold')
        ax.text(x + 0.14, y + 0.05, f"Gens: {sc['gens']}", ha='center', va='center', fontsize=9, family='monospace')
        ax.text(x + 0.14, y - 0.02, f"Resolution: {sc['res']}", ha='center', va='center', fontsize=10, fontweight='bold', color=colors_res[sc["res"]])
        ax.text(x + 0.14, y - 0.10, sc["use"], ha='center', va='center', fontsize=8, style='italic', color='#555')
    ax.set_xlim(0, 1.1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title("Generator Selection Guide for Common Designs", fontsize=14, fontweight='bold', pad=20)
    for res, color in colors_res.items():
        ax.add_patch(plt.Rectangle((0.75, 0.95 - list(colors_res.keys()).index(res)*0.06), 0.03, 0.03, facecolor=color, alpha=0.5))
        ax.text(0.80, 0.965 - list(colors_res.keys()).index(res)*0.06, f"Resolution {res}", fontsize=9, va='center')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    return fig

def plot_foldover_technique(save_path=None):
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    orig = np.array([
        [-1, -1, -1, -1], [+1, -1, -1, +1], [-1, +1, -1, +1], [+1, +1, -1, -1],
        [-1, -1, +1, +1], [+1, -1, +1, -1], [-1, +1, +1, -1], [+1, +1, +1, +1]
    ])
    fold = -orig
    im1 = axes[0].imshow(orig, cmap='RdYlBu', aspect='auto', vmin=-1, vmax=1)
    axes[0].set_title("Original Design (Resolution III)\nD = ABC", fontsize=12, fontweight='bold')
    axes[0].set_xticks(range(4))
    axes[0].set_xticklabels(['A', 'B', 'C', 'D'], fontsize=11, fontweight='bold')
    axes[0].set_yticks(range(8))
    axes[0].set_yticklabels([f"Run {i+1}" for i in range(8)], fontsize=9)
    for i in range(8):
        for j in range(4):
            axes[0].text(j, i, f"{orig[i,j]:+.0f}", ha='center', va='center', fontsize=9)
    im2 = axes[1].imshow(fold, cmap='RdYlBu', aspect='auto', vmin=-1, vmax=1)
    axes[1].set_title("Foldover Design\nD = -ABC", fontsize=12, fontweight='bold')
    axes[1].set_xticks(range(4))
    axes[1].set_xticklabels(['A', 'B', 'C', 'D'], fontsize=11, fontweight='bold')
    axes[1].set_yticks(range(8))
    axes[1].set_yticklabels([f"Run {i+1}" for i in range(8)], fontsize=9)
    for i in range(8):
        for j in range(4):
            axes[1].text(j, i, f"{fold[i,j]:+.0f}", ha='center', va='center', fontsize=9)
    plt.suptitle("Foldover Technique: Reverse All Signs to De-alias Main Effects", fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    return fig

def plot_minimum_aberration_concept(save_path=None):
    fig, ax = plt.subplots(figsize=(12, 7))
    designs = {
        "Design A\n(Minimum Aberration)": {
            "gens": ["ABCE", "BCDF"], "def_rel": "I = ABCE = BCDF = ADEF",
            "word_lengths": [4, 4, 4], "A4": 3, "color": "#2ecc71"
        },
        "Design B\n(Non-Minimum Aberration)": {
            "gens": ["ABC", "DEF"], "def_rel": "I = ABC = DEF = ABCDEF",
            "word_lengths": [3, 3, 6], "A4": 0, "color": "#e74c3c"
        }
    }
    x_offset = 0
    for name, info in designs.items():
        y_base = 0.5
        for i, wl in enumerate(info["word_lengths"]):
            bar = plt.Rectangle((x_offset + 0.05 + i*0.12, y_base), 0.08, wl*0.08, facecolor=info["color"], alpha=0.7, edgecolor='black')
            ax.add_patch(bar)
            ax.text(x_offset + 0.09 + i*0.12, y_base + wl*0.08 + 0.02, f"L={wl}", ha='center', fontsize=9, fontweight='bold')
        ax.text(x_offset + 0.2, 0.95, name, ha='center', fontsize=12, fontweight='bold')
        ax.text(x_offset + 0.2, 0.88, info["def_rel"], ha='center', fontsize=8, family='monospace', wrap=True)
        ax.text(x_offset + 0.2, 0.15, f"A4 = {info['A4']}", ha='center', fontsize=11, fontweight='bold', color=info["color"])
        x_offset += 0.5
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title("Minimum Aberration Criterion: Minimize A4 (Number of Length-4 Words)", fontsize=13, fontweight='bold', pad=20)
    ax.text(0.5, -0.05, "Lower A4 = fewer confounded 2FIs = better design", ha='center', fontsize=10, style='italic', transform=ax.transAxes)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    return fig


# ============================================================
# CASE STUDIES
# ============================================================

def case_study_1_screening():
    print("\n" + "="*70)
    print("CASE STUDY 1: Chemical Process Screening Experiment")
    print("="*70)
    design = FractionalFactorialDesign(k=7, p=4, generators=['AB', 'AC', 'BC', 'ABC'])
    design.summary()
    print("\nAlias Structure (Main Effects):")
    for factor in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        print(f"  {design.get_alias_string(factor)}")
    np.random.seed(42)
    true_effects = {'A': 3.5, 'B': -2.1, 'C': 0.8, 'D': 0.3, 'E': 0.1, 'F': -0.2, 'G': 0.05}
    Y = np.zeros(design.n)
    for i, row in design.design_matrix.iterrows():
        y = 50
        for factor, effect in true_effects.items():
            y += effect * row[factor]
        y += np.random.normal(0, 0.5)
        Y[i] = y
    effects = {}
    for col in design.design_matrix.columns:
        effects[col] = np.dot(design.design_matrix[col].values, Y) / (design.n / 2)
    print("\nEstimated Effects (with aliasing):")
    for factor, effect in sorted(effects.items(), key=lambda x: abs(x[1]), reverse=True):
        alias = design.get_alias_string(factor)
        print(f"  {alias:30s} -> {effect:+.3f}")
    return design, effects

def case_study_2_optimization():
    print("\n" + "="*70)
    print("CASE STUDY 2: Injection Molding Process Optimization")
    print("="*70)
    design = FractionalFactorialDesign(k=6, p=2, generators=['ABC', 'BCD'])
    design.summary()
    print("\nAlias Structure (up to 2FIs):")
    for key, group in design.alias_structure.items():
        if len(key) <= 2:
            print(f"  {' = '.join(group)}")
    np.random.seed(123)
    true_effects = {'A': 4.2, 'B': -3.5, 'C': 1.8, 'D': 0.5, 'E': -0.3, 'F': 0.2,
                    'AB': 2.5, 'AC': -1.2, 'AD': 0.1, 'BC': 0.8, 'BD': -0.4, 'CD': 0.3}
    Y = np.zeros(design.n)
    for i, row in design.design_matrix.iterrows():
        y = 100
        for effect_name, effect_val in true_effects.items():
            if len(effect_name) == 1:
                y += effect_val * row[effect_name]
            else:
                prod = 1
                for letter in effect_name:
                    prod *= row[letter]
                y += effect_val * prod
        y += np.random.normal(0, 0.8)
        Y[i] = y
    effects = {}
    for col in design.design_matrix.columns:
        effects[col] = np.dot(design.design_matrix[col].values, Y) / (design.n / 2)
    for combo in combinations(design.design_matrix.columns, 2):
        col = design.design_matrix[combo[0]] * design.design_matrix[combo[1]]
        effects[''.join(combo)] = np.dot(col.values, Y) / (design.n / 2)
    print("\nEstimated Effects:")
    print("  Main Effects:")
    for factor in ['A', 'B', 'C', 'D', 'E', 'F']:
        print(f"    {factor}: {effects[factor]:+.3f}")
    print("\n  Two-Factor Interactions (aliased pairs):")
    for key, group in design.alias_structure.items():
        if len(key) == 2:
            est = effects[key]
            print(f"    {' = '.join(group)}: {est:+.3f}")
    return design, effects

def case_study_3_robust_design():
    print("\n" + "="*70)
    print("CASE STUDY 3: Robust Parameter Design")
    print("="*70)
    design = FractionalFactorialDesign(k=5, p=1, generators=['ABCD'])
    design.summary()
    print("\nAlias Structure (up to 2FIs):")
    for key, group in design.alias_structure.items():
        if len(key) <= 2:
            print(f"  {' = '.join(group)}")
    np.random.seed(456)
    true_model = {'A': 5.0, 'B': -4.0, 'C': 2.5, 'D': -1.5, 'E': 0.8,
                  'AB': 3.0, 'AC': -2.0, 'AD': 1.0, 'AE': -0.5,
                  'BC': 1.5, 'BD': -1.0, 'BE': 0.5, 'CD': 0.8, 'CE': -0.3, 'DE': 0.2}
    Y = np.zeros(design.n)
    for i, row in design.design_matrix.iterrows():
        y = 200
        for effect_name, effect_val in true_model.items():
            if len(effect_name) == 1:
                y += effect_val * row[effect_name]
            else:
                prod = 1
                for letter in effect_name:
                    prod *= row[letter]
                y += effect_val * prod
        y += np.random.normal(0, 1.0)
        Y[i] = y
    effects = {}
    for col in design.design_matrix.columns:
        effects[col] = np.dot(design.design_matrix[col].values, Y) / (design.n / 2)
    for combo in combinations(design.design_matrix.columns, 2):
        col = design.design_matrix[combo[0]] * design.design_matrix[combo[1]]
        effects[''.join(combo)] = np.dot(col.values, Y) / (design.n / 2)
    print("\nEstimated Main Effects:")
    for factor in ['A', 'B', 'C', 'D', 'E']:
        print(f"  {factor}: {effects[factor]:+.3f}")
    print("\nEstimated 2FIs (clear of main effects and other 2FIs):")
    for combo in combinations(['A', 'B', 'C', 'D', 'E'], 2):
        name = ''.join(combo)
        alias = design.get_alias_string(name)
        print(f"  {alias}: {effects[name]:+.3f}")
    return design, effects

def case_study_4_plackett_burman():
    print("\n" + "="*70)
    print("CASE STUDY 4: Plackett-Burman vs Regular Fractional Factorial")
    print("="*70)
    pb_base = np.array([
        [1, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1],
        [1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 1],
        [-1, 1, 1, 1, -1, -1, -1, 1, -1, 1, 1],
        [1, 1, 1, -1, -1, -1, 1, -1, 1, 1, -1],
        [1, 1, -1, -1, -1, 1, -1, 1, 1, -1, 1],
        [1, -1, -1, -1, 1, -1, 1, 1, -1, 1, 1],
        [-1, -1, -1, 1, -1, 1, 1, -1, 1, 1, 1],
        [-1, -1, 1, -1, 1, 1, -1, 1, 1, 1, -1],
        [-1, 1, -1, 1, 1, -1, 1, 1, 1, -1, -1],
        [1, -1, 1, 1, -1, 1, 1, 1, -1, -1, -1],
        [-1, 1, 1, -1, 1, 1, 1, -1, -1, -1, 1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    ])
    pb_df = pd.DataFrame(pb_base, columns=[chr(64+i) for i in range(1, 12)])
    print("\nPlackett-Burman Design Matrix (12 runs, 11 factors):")
    print(pb_df.to_string())
    return pb_df

def case_study_5_sequential():
    print("\n" + "="*70)
    print("CASE STUDY 5: Sequential Experimentation Strategy")
    print("="*70)
    phase1 = FractionalFactorialDesign(k=8, p=4, generators=['ABC', 'ABD', 'ACD', 'BCD'])
    print("\n--- PHASE 1: Screening Design ---")
    phase1.summary()
    print("\nAlias Structure (Main Effects):")
    for factor in [chr(64+i) for i in range(1, 9)]:
        alias = phase1.get_alias_string(factor)
        if len(alias) > 40:
            print(f"  {factor} = [3FIs and higher]")
        else:
            print(f"  {alias}")
    np.random.seed(789)
    true_effects = {'A': 6.0, 'B': -5.0, 'C': 3.5, 'D': 0.2, 'E': 0.1, 'F': -0.3, 'G': 0.4, 'H': 0.05}
    Y1 = np.zeros(phase1.n)
    for i, row in phase1.design_matrix.iterrows():
        y = 30
        for factor, effect in true_effects.items():
            y += effect * row[factor]
        y += np.random.normal(0, 1.0)
        Y1[i] = y
    effects_p1 = {}
    for col in phase1.design_matrix.columns:
        effects_p1[col] = np.dot(phase1.design_matrix[col].values, Y1) / (phase1.n / 2)
    print("\nPhase 1 Results (Main Effects):")
    significant = []
    for factor, effect in sorted(effects_p1.items(), key=lambda x: abs(x[1]), reverse=True):
        sig = "***" if abs(effect) > 3 else "*" if abs(effect) > 1 else ""
        if abs(effect) > 3:
            significant.append(factor)
        print(f"  {factor}: {effect:+.3f} {sig}")
    print(f"\nSignificant factors identified: {', '.join(significant)}")
    print("\n--- PHASE 2: Foldover Design ---")
    foldover_matrix = -phase1.design_matrix.values
    Y2 = np.zeros(phase1.n)
    for i, row in enumerate(foldover_matrix):
        y = 30
        for j, factor in enumerate(phase1.design_matrix.columns):
            y += true_effects[factor] * row[j]
        y += np.random.normal(0, 1.0)
        Y2[i] = y
    combined_Y = np.concatenate([Y1, Y2])
    combined_matrix = np.vstack([phase1.design_matrix.values, foldover_matrix])
    effects_combined = {}
    for j, factor in enumerate(phase1.design_matrix.columns):
        effects_combined[factor] = np.dot(combined_matrix[:, j], combined_Y) / 16
    print("\nCombined Analysis (32 runs):")
    for factor, effect in sorted(effects_combined.items(), key=lambda x: abs(x[1]), reverse=True):
        print(f"  {factor}: {effect:+.3f}")
    return phase1, effects_p1, effects_combined


# ============================================================
# MAIN EXECUTION
# ============================================================
if __name__ == "__main__":
    os.makedirs('./figures', exist_ok=True)
    os.makedirs('./models', exist_ok=True)

    print("="*70)
    print("  DoE Lecture 12: Fractional Factorial Design")
    print("="*70)

    # Generate visualizations
    print("\nGenerating visualizations...")
    d6 = FractionalFactorialDesign(k=6, p=2, generators=['ABC', 'BCD'])
    plot_design_matrix(d6, "2^(6-2) Resolution IV Design Matrix (16 runs)", save_path='./figures/fig01_design_matrix.png')
    plot_alias_structure(d6, max_order=2, save_path='./figures/fig02_alias_structure.png')
    plot_resolution_comparison(save_path='./figures/fig03_resolution_comparison.png')
    plot_fraction_size_comparison(save_path='./figures/fig04_fraction_size.png')
    plot_generator_selection_guide(save_path='./figures/fig05_generator_guide.png')
    plot_foldover_technique(save_path='./figures/fig06_foldover.png')
    plot_minimum_aberration_concept(save_path='./figures/fig07_min_aberration.png')
    print("All visualizations generated!")

    # Run case studies
    print("\n" + "="*70)
    print("Running Case Studies...")
    print("="*70)
    case_study_1_screening()
    case_study_2_optimization()
    case_study_3_robust_design()
    case_study_4_plackett_burman()
    case_study_5_sequential()
    print("\n" + "="*70)
    print("All case studies completed!")
    print("="*70)
