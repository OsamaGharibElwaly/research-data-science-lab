
"""
DoE Lecture 9: Multiple Testing with FDR
Clean implementation - Visualizations + Figure Saving + Results Text

Covers:
1. Multiple testing problem (FWER vs FDR)
2. Benjamini-Hochberg (BH) procedure
3. Benjamini-Yekutieli (BY) procedure
4. Storey's q-value method
5. Case studies: Genomic data, A/B testing
6. Simulation study
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from pathlib import Path
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Create output directory
OUTPUT_DIR = Path("fdr_output")
OUTPUT_DIR.mkdir(exist_ok=True)


def save_figure(fig, name, dpi=300):
    """Save figure as PNG and PDF"""
    png_path = OUTPUT_DIR / f"{name}.png"
    pdf_path = OUTPUT_DIR / f"{name}.pdf"
    fig.savefig(png_path, dpi=dpi, bbox_inches='tight', facecolor='white')
    fig.savefig(pdf_path, bbox_inches='tight', facecolor='white')
    print(f"  Saved: {png_path.name}, {pdf_path.name}")
    return str(png_path)


def save_results_text(content, name):
    """Save results as plain text file"""
    filepath = OUTPUT_DIR / f"{name}.txt"
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"  Saved: {filepath.name}")
    return str(filepath)


class FDRControl:
    """FDR control methods: BH, BY, and Storey's q-value"""

    def __init__(self, p_values, alpha=0.05, method='BH'):
        self.p_values = np.array(p_values)
        self.alpha = alpha
        self.method = method
        self.m = len(p_values)
        self.sorted_indices = np.argsort(p_values)
        self.sorted_p = self.p_values[self.sorted_indices]

        self.rejected = None
        self.rejected_indices = None
        self.adj_p_values = None
        self.q_values = None
        self.pi0 = None

    def benjamini_hochberg(self):
        """Benjamini-Hochberg procedure"""
        sorted_p = self.sorted_p
        m = self.m

        bh_critical = np.arange(1, m + 1) * self.alpha / m
        comparisons = sorted_p <= bh_critical

        k = np.max(np.where(comparisons)[0]) + 1 if np.any(comparisons) else 0

        rejected = np.zeros(m, dtype=bool)
        if k > 0:
            rejected[self.sorted_indices[:k]] = True

        adj_p = np.zeros(m)
        for i, idx in enumerate(self.sorted_indices):
            adj_p[idx] = min(sorted_p[i] * m / (i + 1), 1.0)

        for i in range(m - 2, -1, -1):
            if adj_p[self.sorted_indices[i]] > adj_p[self.sorted_indices[i + 1]]:
                adj_p[self.sorted_indices[i]] = adj_p[self.sorted_indices[i + 1]]

        self.rejected = rejected
        self.rejected_indices = np.where(rejected)[0]
        self.adj_p_values = adj_p

        return {
            'rejected': rejected,
            'rejected_indices': self.rejected_indices,
            'adj_p_values': adj_p,
            'k': k,
            'method': 'Benjamini-Hochberg'
        }

    def benjamini_yekutieli(self):
        """Benjamini-Yekutieli procedure (works under dependence)"""
        sorted_p = self.sorted_p
        m = self.m

        h_m = np.sum(1 / np.arange(1, m + 1))
        by_critical = np.arange(1, m + 1) * self.alpha / (m * h_m)
        comparisons = sorted_p <= by_critical

        k = np.max(np.where(comparisons)[0]) + 1 if np.any(comparisons) else 0

        rejected = np.zeros(m, dtype=bool)
        if k > 0:
            rejected[self.sorted_indices[:k]] = True

        adj_p = np.zeros(m)
        for i, idx in enumerate(self.sorted_indices):
            adj_p[idx] = min(sorted_p[i] * m * h_m / (i + 1), 1.0)

        for i in range(m - 2, -1, -1):
            if adj_p[self.sorted_indices[i]] > adj_p[self.sorted_indices[i + 1]]:
                adj_p[self.sorted_indices[i]] = adj_p[self.sorted_indices[i + 1]]

        self.rejected = rejected
        self.rejected_indices = np.where(rejected)[0]
        self.adj_p_values = adj_p

        return {
            'rejected': rejected,
            'rejected_indices': self.rejected_indices,
            'adj_p_values': adj_p,
            'k': k,
            'method': 'Benjamini-Yekutieli'
        }

    def storey_qvalue(self, lambda_param=0.5):
        """Storey's q-value method"""
        p = self.p_values
        m = self.m

        pi0 = min(np.sum(p > lambda_param) / (m * (1 - lambda_param)), 1.0)
        self.pi0 = pi0

        sorted_p = self.sorted_p
        q_values = np.zeros(m)
        prev_q = 1.0

        for i in range(m - 1, -1, -1):
            q_value = min(pi0 * m * sorted_p[i] / (i + 1), 1.0)
            q_values[self.sorted_indices[i]] = min(q_value, prev_q)
            prev_q = q_values[self.sorted_indices[i]]

        self.q_values = q_values
        self.rejected = q_values <= self.alpha
        self.rejected_indices = np.where(self.rejected)[0]

        return {
            'rejected': self.rejected,
            'rejected_indices': self.rejected_indices,
            'q_values': q_values,
            'pi0': pi0,
            'method': "Storey's q-value"
        }

    def apply_method(self):
        """Apply the specified FDR method"""
        if self.method == 'BH':
            return self.benjamini_hochberg()
        elif self.method == 'BY':
            return self.benjamini_yekutieli()
        elif self.method == 'qvalue':
            return self.storey_qvalue()
        else:
            raise ValueError(f"Unknown method: {self.method}")

    def plot_results(self, title=None):
        """Create visualization of FDR results"""
        if title is None:
            title = f"FDR Analysis: {self.method} Method"

        fig, axes = plt.subplots(2, 3, figsize=(18, 10))

        # 1. P-value distribution
        ax1 = axes[0, 0]
        ax1.hist(self.p_values, bins=30, alpha=0.7, color='steelblue', edgecolor='black')
        ax1.axvline(self.alpha, color='red', linestyle='--', label=f'alpha = {self.alpha}')
        ax1.set_xlabel('P-values')
        ax1.set_ylabel('Frequency')
        ax1.set_title('Distribution of P-values')
        ax1.legend()

        # 2. P-value vs Adjusted / Q-value
        ax2 = axes[0, 1]
        if self.method == 'qvalue' and self.q_values is not None:
            y_values, y_label = self.q_values, 'Q-values'
        elif self.adj_p_values is not None:
            y_values, y_label = self.adj_p_values, 'Adjusted P-values'
        else:
            y_values, y_label = self.p_values, 'P-values'

        ax2.scatter(self.p_values, y_values, alpha=0.6, color='coral', s=10)
        ax2.plot([0, 1], [0, 1], 'k--', alpha=0.5, label='y=x')
        ax2.axhline(self.alpha, color='red', linestyle='--', label=f'alpha = {self.alpha}')
        ax2.set_xlabel('Original P-values')
        ax2.set_ylabel(y_label)
        ax2.set_title(f'Original vs {y_label}')
        ax2.legend()

        # 3. Rejected hypotheses
        ax3 = axes[0, 2]
        if self.rejected is not None:
            colors = ['coral' if r else 'steelblue' for r in self.rejected]
            ax3.bar(range(len(self.rejected)), self.p_values, color=colors, alpha=0.7)
            ax3.axhline(self.alpha, color='red', linestyle='--', label=f'alpha = {self.alpha}')
            ax3.set_xlabel('Test Index')
            ax3.set_ylabel('P-values')
            ax3.set_title(f'Rejected Hypotheses ({np.sum(self.rejected)} rejected)')
            ax3.legend()

        # 4. Rejection count vs threshold
        ax4 = axes[1, 0]
        thresholds = np.linspace(0, 0.1, 100)
        n_rejected = []
        for thresh in thresholds:
            if self.method == 'qvalue' and self.q_values is not None:
                n_rej = np.sum(self.q_values <= thresh)
            elif self.adj_p_values is not None:
                n_rej = np.sum(self.adj_p_values <= thresh)
            else:
                n_rej = np.sum(self.p_values <= thresh)
            n_rejected.append(n_rej)

        ax4.plot(thresholds, n_rejected, 'b-', linewidth=2)
        ax4.axvline(self.alpha, color='red', linestyle='--', label=f'alpha = {self.alpha}')
        if self.rejected is not None:
            ax4.axhline(np.sum(self.rejected), color='green', linestyle='--', alpha=0.5,
                       label=f'Rejected at alpha = {np.sum(self.rejected)}')
        ax4.set_xlabel('Threshold')
        ax4.set_ylabel('Number of Rejected Hypotheses')
        ax4.set_title('Rejection Count vs Threshold')
        ax4.legend()
        ax4.grid(True, alpha=0.3)

        # 5. Q-Q plot
        ax5 = axes[1, 1]
        expected_p = np.linspace(0, 1, len(self.p_values))
        observed_p = np.sort(self.p_values)
        ax5.plot(expected_p, observed_p, 'bo', alpha=0.3, markersize=3)
        ax5.plot([0, 1], [0, 1], 'r--', alpha=0.5)
        ax5.set_xlabel('Expected P-values (Uniform)')
        ax5.set_ylabel('Observed P-values')
        ax5.set_title('Q-Q Plot of P-values')
        ax5.grid(True, alpha=0.3)

        # 6. FDR / Adjusted p-value curve
        ax6 = axes[1, 2]
        if self.method == 'qvalue' and self.q_values is not None:
            ax6.plot(sorted(self.p_values), sorted(self.q_values), 'b-', linewidth=2)
            ax6.axhline(self.alpha, color='red', linestyle='--', label=f'alpha = {self.alpha}')
            ax6.set_ylabel('Estimated FDR / Q-value')
            ax6.set_title('FDR Estimate Curve')
        elif self.adj_p_values is not None:
            ax6.plot(sorted(self.p_values), sorted(self.adj_p_values), 'b-', linewidth=2)
            ax6.axhline(self.alpha, color='red', linestyle='--', label=f'alpha = {self.alpha}')
            ax6.set_ylabel('Adjusted P-value')
            ax6.set_title('Adjusted P-value Curve')
        ax6.set_xlabel('P-value Threshold')
        ax6.legend()
        ax6.grid(True, alpha=0.3)

        plt.suptitle(title, fontsize=14, fontweight='bold')
        plt.tight_layout()
        return fig


class CaseStudy:
    """Case studies with visualizations and saved outputs"""

    def genomic_data_case(self):
        """Case Study 1: Genomic Data Analysis"""
        print("\n" + "="*60)
        print("CASE STUDY 1: Genomic Data Analysis")
        print("="*60)

        np.random.seed(42)
        n_genes, n_samples = 1000, 30
        n_null = int(0.8 * n_genes)
        n_alt = n_genes - n_null

        group1 = np.random.normal(0, 1, (n_genes, n_samples//2))
        group2 = np.random.normal(0, 1, (n_genes, n_samples//2))
        group2[:n_alt, :] += 1.0

        p_values = [stats.ttest_ind(group1[i, :], group2[i, :])[1] for i in range(n_genes)]
        t_stats = [stats.ttest_ind(group1[i, :], group2[i, :])[0] for i in range(n_genes)]

        fdr = FDRControl(p_values, alpha=0.05, method='BH')
        results = fdr.apply_method()

        gene_data = pd.DataFrame({
            'gene_id': [f'GENE_{i:04d}' for i in range(n_genes)],
            'p_value': p_values,
            't_statistic': t_stats,
            'true_alternative': [i < n_alt for i in range(n_genes)],
            'rejected': results['rejected'],
            'adjusted_p_value': results['adj_p_values']
        })

        tp = np.sum(gene_data['rejected'] & gene_data['true_alternative'])
        fp = np.sum(gene_data['rejected'] & ~gene_data['true_alternative'])

        # Build results text
        results_text = f"""GENOMIC DATA FDR ANALYSIS
{'='*50}
Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Parameters:
  Total genes: {n_genes}
  True differentially expressed: {n_alt}
  Alpha: 0.05
  Method: Benjamini-Hochberg

Results:
  Rejected hypotheses: {np.sum(results['rejected'])}
  True positives: {int(tp)}
  False positives: {int(fp)}
  Estimated FDR: {fp / max(1, int(np.sum(results['rejected']))):.4f}
  Power: {tp / max(1, n_alt):.4f}

Top 10 Significant Genes (by adjusted p-value):
{gene_data[gene_data['rejected']].nsmallest(10, 'adjusted_p_value')[['gene_id', 'p_value', 'adjusted_p_value', 't_statistic']].to_string(index=False)}
"""

        print(f"Total genes: {n_genes}")
        print(f"True differentially expressed: {n_alt}")
        print(f"Rejected (FDR BH): {np.sum(results['rejected'])}")
        print(f"Estimated FDR: {fp / max(1, int(np.sum(results['rejected']))):.3f}")
        print(f"Power: {tp / max(1, n_alt):.3f}")

        fig = fdr.plot_results(title="Genomic Data FDR Analysis")
        save_figure(fig, "genomic_fdr_analysis")
        save_results_text(results_text, "genomic_results")

        return fdr, results, gene_data, fig

    def ab_testing_case(self):
        """Case Study 2: A/B Testing with Multiple Metrics"""
        print("\n" + "="*60)
        print("CASE STUDY 2: A/B Testing with Multiple Metrics")
        print("="*60)

        np.random.seed(123)
        n_metrics, n_users = 50, 1000

        control = np.random.normal(0, 1, (n_metrics, n_users))
        treatment = np.random.normal(0, 1, (n_metrics, n_users))

        effect_metrics = np.random.choice(n_metrics, size=int(0.2*n_metrics), replace=False)
        for i in effect_metrics:
            treatment[i, :] += 0.3

        p_values = []
        effect_sizes = []
        for i in range(n_metrics):
            _, p_val = stats.ttest_ind(control[i, :], treatment[i, :])
            p_values.append(p_val)
            effect_sizes.append(np.mean(treatment[i, :]) - np.mean(control[i, :]))

        ab_data = pd.DataFrame({
            'metric': [f'metric_{i:02d}' for i in range(n_metrics)],
            'p_value': p_values,
            'effect_size': effect_sizes,
            'true_effect': [i in effect_metrics for i in range(n_metrics)]
        })

        results_dict = {}
        results_lines = ["A/B TESTING FDR ANALYSIS", "="*50, f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"]

        for method in ['BH', 'BY', 'qvalue']:
            fdr = FDRControl(p_values, alpha=0.05, method=method)
            results = fdr.apply_method()
            results_dict[method] = results

            ab_data[f'rejected_{method}'] = results['rejected']
            if method == 'qvalue':
                ab_data['q_value'] = results['q_values']
            else:
                ab_data[f'adj_p_{method}'] = results['adj_p_values']

            n_rej = int(np.sum(results['rejected']))
            tp = np.sum(results['rejected'] & ab_data['true_effect'])
            fp = n_rej - tp

            results_lines.append(f"\n{method} Method:")
            results_lines.append(f"  Rejected: {n_rej}")
            results_lines.append(f"  True positives: {int(tp)}")
            results_lines.append(f"  False positives: {int(fp)}")
            if method == 'qvalue':
                results_lines.append(f"  Estimated pi0: {fdr.pi0:.3f}")

            print(f"\n{method} method:")
            print(f"  Rejected: {n_rej}")
            if method == 'qvalue':
                print(f"  Estimated pi0: {fdr.pi0:.3f}")

        # Comparison visualization
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        for idx, method in enumerate(['BH', 'BY', 'qvalue']):
            ax = axes[idx]
            results = results_dict[method]
            colors = ['red' if r else 'blue' for r in results['rejected']]
            ax.scatter(range(len(p_values)), p_values, c=colors, alpha=0.6, s=20)
            ax.axhline(0.05, color='green', linestyle='--', alpha=0.5, label='alpha = 0.05')
            ax.set_title(f'{method}\nRejected: {np.sum(results["rejected"])}')
            ax.set_xlabel('Test Index')
            ax.set_ylabel('P-value')
            ax.set_ylim(0, 1)
            ax.legend()
        plt.suptitle('A/B Testing Methods Comparison', fontsize=14, fontweight='bold')
        plt.tight_layout()

        save_figure(fig, "ab_testing_comparison")
        save_results_text("\n".join(results_lines), "ab_testing_results")

        return results_dict, ab_data, fig


class SimulationStudy:
    """Simulation studies with visualizations and saved outputs"""

    def fdr_power_comparison(self, n_sims=100, n_tests=500):
        """Compare power of different FDR methods"""
        print("\n" + "="*60)
        print("SIMULATION: FDR Power Comparison")
        print("="*60)

        np.random.seed(789)
        pi0_values = [0.5, 0.7, 0.9]
        effect_sizes = [0.5, 1.0, 1.5]

        all_results = []

        for pi0 in pi0_values:
            for effect in effect_sizes:
                fdr_rates, powers = [], []

                for _ in range(n_sims):
                    n_null = int(pi0 * n_tests)
                    n_alt = n_tests - n_null

                    null_p = np.random.uniform(0, 1, n_null)
                    alt_p = np.random.beta(0.5, 1/effect, n_alt)
                    p_values = np.concatenate([null_p, alt_p])
                    np.random.shuffle(p_values)

                    true_alt = np.concatenate([np.zeros(n_null), np.ones(n_alt)])
                    np.random.shuffle(true_alt)

                    fdr_bh = FDRControl(p_values, alpha=0.05, method='BH')
                    results_bh = fdr_bh.apply_method()

                    rejected = results_bh['rejected']
                    tp = np.sum(rejected & (true_alt == 1))
                    fp = np.sum(rejected & (true_alt == 0))

                    fdr_rates.append(fp / max(1, tp + fp))
                    powers.append(tp / max(1, n_alt))

                all_results.append({
                    'pi0': pi0,
                    'effect_size': effect,
                    'mean_fdr': np.mean(fdr_rates),
                    'std_fdr': np.std(fdr_rates),
                    'mean_power': np.mean(powers),
                    'std_power': np.std(powers)
                })

        df_results = pd.DataFrame(all_results)

        # Visualization
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))

        ax1 = axes[0]
        for pi0 in df_results['pi0'].unique():
            subset = df_results[df_results['pi0'] == pi0]
            ax1.plot(subset['effect_size'], subset['mean_fdr'], 
                    'o-', label=f'pi0 = {pi0}', linewidth=2, markersize=8)
        ax1.axhline(0.05, color='red', linestyle='--', label='Target FDR = 0.05')
        ax1.set_xlabel('Effect Size')
        ax1.set_ylabel('Actual FDR')
        ax1.set_title('FDR Control Performance')
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        ax2 = axes[1]
        for pi0 in df_results['pi0'].unique():
            subset = df_results[df_results['pi0'] == pi0]
            ax2.plot(subset['effect_size'], subset['mean_power'], 
                    'o-', label=f'pi0 = {pi0}', linewidth=2, markersize=8)
        ax2.set_xlabel('Effect Size')
        ax2.set_ylabel('Statistical Power')
        ax2.set_title('Power Performance')
        ax2.legend()
        ax2.grid(True, alpha=0.3)

        plt.suptitle('FDR Simulation Study Results', fontsize=14, fontweight='bold')
        plt.tight_layout()

        # Build results text
        results_text = f"""FDR SIMULATION STUDY RESULTS
{'='*50}
Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Parameters:
  Simulations: {n_sims}
  Tests per simulation: {n_tests}
  pi0 values: {pi0_values}
  Effect sizes: {effect_sizes}

Results Table:
{df_results.to_string(index=False)}

Interpretation:
- FDR should be controlled near 0.05 (target alpha)
- Power increases with effect size and decreases with pi0
- pi0 = proportion of true null hypotheses
"""

        print("\nSimulation Results Summary:")
        print(df_results.to_string(index=False))

        save_figure(fig, "simulation_results")
        save_results_text(results_text, "simulation_results")

        return df_results, fig


def main():
    """Run all analyses, save figures and results text"""
    print("="*80)
    print("DESIGN OF EXPERIMENTS - LECTURE 9: MULTIPLE TESTING WITH FDR")
    print("="*80)
    print(f"\nOutput directory: {OUTPUT_DIR.absolute()}")
    print("Saving figures (PNG + PDF) and results text files...")
    print("="*80)

    case_study = CaseStudy()

    print("\n[1/3] Running Case Study 1: Genomic Data...")
    fdr1, results1, gene_data, fig1 = case_study.genomic_data_case()

    print("\n[2/3] Running Case Study 2: A/B Testing...")
    results_dict, ab_data, fig2 = case_study.ab_testing_case()

    print("\n[3/3] Running Simulation Study...")
    simulation = SimulationStudy()
    df_sim, fig3 = simulation.fdr_power_comparison(n_sims=50, n_tests=500)

    print("\n" + "="*80)
    print("ANALYSIS COMPLETE!")
    print(f"All outputs saved to: {OUTPUT_DIR.absolute()}")
    print("="*80)
    print("\nGenerated files:")
    for f in sorted(OUTPUT_DIR.iterdir()):
        print(f"  - {f.name}")

    plt.show()


if __name__ == "__main__":
    main()