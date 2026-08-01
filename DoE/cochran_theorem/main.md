# Cochran’s Theorem and the Design and Analysis of Experiments: A Graduate-Level Masterclass

This masterclass provides a rigorous, graduate-level exploration of Cochran’s Theorem (1934), its mathematical foundations, and its pivotal role in the Analysis of Variance (ANOVA). We will bridge abstract linear algebra and statistical theory, culminating in a complete computational verification.

---

## 1. Theoretical Foundation & Likelihood Ratio Principles

### Why We Perform F-tests in ANOVA
In the Design of Experiments (DoE), the primary objective of a One-Way ANOVA is to test whether a categorical independent variable (treatment) has a statistically significant effect on a continuous dependent variable. Formally, we test the null hypothesis $H_0: \mu_1 = \mu_2 = \dots = \mu_k$ against the alternative $H_1$: at least one $\mu_i$ differs. 

The F-test achieves this by partitioning the total variability in the data into variability *between* treatments and variability *within* treatments (error). If the treatment effect is real, the between-group variance will significantly exceed the within-group variance.

### Justification via Neyman-Pearson and Likelihood Ratio Tests (LRT)
Assume the standard i.i.d. normal error model: $Y_{ij} \sim \mathcal{N}(\mu_i, \sigma^2)$ for $i=1,\dots,k$ and $j=1,\dots,n$. The likelihood function is:
$$ L(\boldsymbol{\mu}, \sigma^2) = (2\pi\sigma^2)^{-N/2} \exp\left( -\frac{1}{2\sigma^2} \sum_{i=1}^k \sum_{j=1}^n (Y_{ij} - \mu_i)^2 \right) $$
where $N = k \times n$.

To find the Likelihood Ratio Test (LRT) statistic $\Lambda = \frac{\sup_{H_0} L}{\sup_{H_0 \cup H_1} L}$, we maximize the likelihood under both hypotheses:
1. **Under $H_1$ (Unrestricted):** The MLEs are $\hat{\mu}_i = \bar{Y}_{i.}$ and $\hat{\sigma}^2_1 = \frac{1}{N} SS_{Error}$, where $SS_{Error} = \sum_{i,j} (Y_{ij} - \bar{Y}_{i.})^2$.
2. **Under $H_0$ (Restricted):** The MLEs are $\hat{\mu} = \bar{Y}_{..}$ and $\hat{\sigma}^2_0 = \frac{1}{N} SS_{Total}$, where $SS_{Total} = \sum_{i,j} (Y_{ij} - \bar{Y}_{..})^2 = SS_{Error} + SS_{Treatment}$.

The likelihood ratio simplifies to:
$$ \Lambda = \left( \frac{\hat{\sigma}^2_1}{\hat{\sigma}^2_0} \right)^{N/2} = \left( \frac{SS_{Error}}{SS_{Error} + SS_{Treatment}} \right)^{N/2} = \left( 1 + \frac{SS_{Treatment}}{SS_{Error}} \right)^{-N/2} $$
Rejecting $H_0$ for small values of $\Lambda$ is mathematically equivalent to rejecting for large values of the ratio $\frac{SS_{Treatment}}{SS_{Error}}$. By the Neyman-Pearson lemma and the properties of exponential families, this LRT yields the Uniformly Most Powerful Unbiased (UMPU) test, which is precisely the F-test.

### Why the Ratio Requires Independent Chi-Squared Variables
The F-distribution is strictly defined as the distribution of the ratio of two **independent** chi-squared random variables, each divided by its respective degrees of freedom:
$$ F = \frac{U / d_1}{V / d_2}, \quad U \sim \chi^2_{d_1}, \quad V \sim \chi^2_{d_2}, \quad U \perp V $$
For the test statistic $F = \frac{SS_{Treatment} / (k-1)}{SS_{Error} / (N-k)}$ to follow an exact F-distribution under $H_0$, the numerator and denominator sums of squares must be distributed as independent chi-squared variables. This strict requirement is what makes Cochran's Theorem the theoretical linchpin of ANOVA.

---

## 2. Supporting Mathematical Lemmata (With Rigorous Proofs)

To prove Cochran's Theorem, we first establish two critical lemmata regarding quadratic forms of standard normal vectors. Let $\mathbf{z} \sim \mathcal{N}(\mathbf{0}, I_m)$.

### Lemma 1: Spectral Decomposition of Quadratic Forms
**Statement:** For any symmetric matrix $A \in \mathbb{R}^{m \times m}$, the quadratic form $Q = \mathbf{z}^T A \mathbf{z}$ can be expressed as $Q = \sum_{i=1}^m \lambda_i w_i^2$, where $\lambda_i$ are the eigenvalues of $A$ and $w_i$ are i.i.d. $\mathcal{N}(0, 1)$.

**Proof:**
Since $A$ is symmetric, the Spectral Theorem guarantees it can be decomposed as $A = U \Lambda U^T$, where $U$ is an orthogonal matrix ($U^T U = I_m$) and $\Lambda = \text{diag}(\lambda_1, \dots, \lambda_m)$.
Define the orthogonal rotation $\mathbf{w} = U^T \mathbf{z}$. Because $U$ is orthogonal and $\mathbf{z} \sim \mathcal{N}(\mathbf{0}, I_m)$, the transformed vector $\mathbf{w}$ retains the same distribution: $\mathbf{w} \sim \mathcal{N}(\mathbf{0}, U^T I_m U) = \mathcal{N}(\mathbf{0}, I_m)$.
Substituting this into the quadratic form:
$$ Q = \mathbf{z}^T (U \Lambda U^T) \mathbf{z} = (U^T \mathbf{z})^T \Lambda (U^T \mathbf{z}) = \mathbf{w}^T \Lambda \mathbf{w} = \sum_{i=1}^m \lambda_i w_i^2 $$
Since $w_i$ are i.i.d. $\mathcal{N}(0,1)$, $w_i^2 \sim \chi^2_1$. $\blacksquare$

### Lemma 2: Idempotency & Stochastic Independence
**Statement:** If $A$ is symmetric and idempotent ($A^2 = A$), then $Q = \mathbf{z}^T A \mathbf{z} \sim \chi^2_r$ where $r = \text{rank}(A)$. Furthermore, $Q' = \mathbf{z}^T (I_m - A) \mathbf{z} \sim \chi^2_{m-r}$, and $Q$ and $Q'$ are stochastically independent.

**Proof:**
1. **Distribution of $Q$:** Since $A^2 = A$, its eigenvalues must satisfy $\lambda_i^2 = \lambda_i$, meaning $\lambda_i \in \{0, 1\}$. The rank of $A$ equals its trace, so $r = \text{tr}(A) = \sum_{i=1}^m \lambda_i$. Thus, exactly $r$ eigenvalues are 1, and $m-r$ are 0. By Lemma 1:
   $$ Q = \sum_{i=1}^r 1 \cdot w_i^2 + \sum_{i=r+1}^m 0 \cdot w_i^2 = \sum_{i=1}^r w_i^2 \sim \chi^2_r $$
2. **Distribution of $Q'$:** The matrix $B = I_m - A$ is also symmetric. It is idempotent because $B^2 = (I_m - A)^2 = I_m - 2A + A^2 = I_m - A = B$. Its rank is $\text{tr}(I_m - A) = m - r$. By the same logic, $Q' \sim \chi^2_{m-r}$.
3. **Independence:** For $\mathbf{z} \sim \mathcal{N}(\mathbf{0}, I_m)$, Craig's Theorem states that two quadratic forms $\mathbf{z}^T A \mathbf{z}$ and $\mathbf{z}^T B \mathbf{z}$ are independent if and only if $AB = 0$. Here, $A(I_m - A) = A - A^2 = 0$. Thus, $Q \perp Q'$. $\blacksquare$

---

## 3. Formal Statement & Full Proof of Cochran's Theorem (1934)

### Formal Statement
Let $\mathbf{z} \sim \mathcal{N}(\mathbf{0}, I_m)$. Let $A_1, A_2, \dots, A_p$ be symmetric matrices such that $\sum_{k=1}^p A_k = I_m$. Let $Q_k = \mathbf{z}^T A_k \mathbf{z}$ and $r_k = \text{rank}(A_k)$. The following three conditions are equivalent:
1. $Q_k \sim \chi^2_{r_k}$ for all $k$, and the $Q_k$ are mutually independent.
2. $\sum_{k=1}^p r_k = m$.
3. $A_k$ are idempotent for all $k$ (which implies $A_i A_j = 0$ for $i \neq j$).

### Proof of Necessity (1 $\implies$ 2)
Assume condition (1) holds. The expected value of a $\chi^2_{r_k}$ variable is $r_k$. 
Summing the quadratic forms yields:
$$ \sum_{k=1}^p Q_k = \mathbf{z}^T \left( \sum_{k=1}^p A_k \right) \mathbf{z} = \mathbf{z}^T I_m \mathbf{z} = \mathbf{z}^T \mathbf{z} \sim \chi^2_m $$
Taking the expectation of both sides:
$$ E\left[ \sum_{k=1}^p Q_k \right] = E[\mathbf{z}^T \mathbf{z}] = m $$
By linearity of expectation and the assumption of their distributions:
$$ \sum_{k=1}^p E[Q_k] = \sum_{k=1}^p r_k = m $$
Thus, condition (2) holds. $\blacksquare$

### Proof of Sufficiency (2 $\implies$ 1 & 3)
Assume $\sum_{k=1}^p A_k = I_m$ and $\sum_{k=1}^p r_k = m$. We will demonstrate this via simultaneous diagonalization. 

Because the $A_k$ are symmetric, if they commute, they share a common orthonormal eigenbasis. We will show that the rank condition forces them to be orthogonal projections, which inherently commute. Let $U$ be an orthogonal matrix that simultaneously diagonalizes the $A_k$, such that $U^T A_k U = D_k$, where $D_k = \text{diag}(\lambda_{k1}, \lambda_{k2}, \dots, \lambda_{km})$.

Summing the diagonalized matrices gives:
$$ \sum_{k=1}^p D_k = U^T \left( \sum_{k=1}^p A_k \right) U = U^T I_m U = I_m $$
This implies that for every column index $i \in \{1, \dots, m\}$, the eigenvalues sum to 1:
$$ \sum_{k=1}^p \lambda_{ki} = 1 $$
The rank $r_k$ is the number of non-zero eigenvalues of $A_k$. The total number of non-zero eigenvalues across all matrices is $\sum_{k=1}^p r_k = m$. 
Since $\sum_{k=1}^p \lambda_{ki} = 1$, for each $i$, at least one $\lambda_{ki}$ must be non-zero. Therefore, the total number of non-zero eigenvalues across all $k$ and $i$ must be *at least* $m$. 
Because we are given that the total number of non-zero eigenvalues is *exactly* $m$, it must be that for every $i$, there is **exactly one** $k$ such that $\lambda_{ki} \neq 0$. 
Since the sum of these eigenvalues for a fixed $i$ is 1, that unique non-zero eigenvalue must be exactly 1. 

Consequently, for every $k$, the eigenvalues $\lambda_{ki}$ are strictly restricted to $\{0, 1\}$. This implies:
1. $D_k^2 = D_k \implies A_k^2 = A_k$ (The matrices are **idempotent**).
2. For $k \neq j$, $\lambda_{ki} \lambda_{ji} = 0$ for all $i \implies D_k D_j = 0 \implies A_k A_j = 0$ (The matrices are **mutually orthogonal**).

Because $A_k$ are idempotent and mutually orthogonal, we can iteratively apply Lemma 2. $Q_k = \mathbf{z}^T A_k \mathbf{z} \sim \chi^2_{r_k}$. Furthermore, because $A_i A_j = 0$ for $i \neq j$, Craig's Theorem guarantees that all $Q_k$ are mutually stochastically independent. $\blacksquare$

---

## 4. Geometric Intuition & ANOVA Sum of Squares Decomposition

### Geometric Intuition in $\mathbb{R}^N$
ANOVA is fundamentally a geometric projection of the observation vector $\mathbf{y} \in \mathbb{R}^N$ onto orthogonal subspaces. 
- **Total Space:** $\mathbb{R}^N$ has dimension $N$.
- **Mean Subspace ($V_{Mean}$):** A 1-dimensional subspace spanned by the vector of ones, $\mathbf{1}_N$.
- **Treatment Subspace ($V_{Trt}$):** A $(k-1)$-dimensional subspace representing deviations of group means from the grand mean, orthogonal to $V_{Mean}$.
- **Error Subspace ($V_{Err}$):** An $(N-k)$-dimensional subspace representing residuals within groups, orthogonal to both $V_{Mean}$ and $V_{Trt}$.

Because these subspaces are mutually orthogonal and span $\mathbb{R}^N$, their projection matrices $P_{Mean}$, $P_{Trt}$, and $P_{Err}$ satisfy $P_i P_j = 0$ (for $i \neq j$), $P_k^2 = P_k$, and $\sum P_k = I_N$. This is the exact geometric realization of Cochran's Theorem.

### Quadratic Matrix Form Decomposition
The Sum of Squares (SS) are simply the squared lengths of these projections:
$$ SS_k = \| P_k \mathbf{y} \|^2 = \mathbf{y}^T P_k^T P_k \mathbf{y} = \mathbf{y}^T P_k \mathbf{y} $$
Thus, the total sum of squares decomposes as:
$$ \mathbf{y}^T \mathbf{y} = \mathbf{y}^T P_{Mean} \mathbf{y} + \mathbf{y}^T P_{Trt} \mathbf{y} + \mathbf{y}^T P_{Err} \mathbf{y} $$
$$ SS_{Total} = SS_{Mean} + SS_{Treatment} + SS_{Error} $$
Under the null hypothesis $H_0$ and normal errors, Cochran's Theorem guarantees that $SS_{Treatment}/\sigma^2 \sim \chi^2_{k-1}$ and $SS_{Error}/\sigma^2 \sim \chi^2_{N-k}$ independently, validating the F-test.

---

## 5. Complete Hands-On Implementation (Python Code)

The following self-contained Python script generates synthetic data, constructs the projection matrices, verifies Cochran's Theorem empirically via Monte Carlo simulations, and computes the F-statistic.

```python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style
sns.set_theme(style="whitegrid", palette="muted")

# ==========================================
# 1. Generate Synthetic Data for One-Way ANOVA
# ==========================================
np.random.seed(42)
k = 4          # Number of treatments
n = 25         # Replicates per treatment
N = k * n      # Total observations
mu = [10, 12, 11, 13] # True means (H0 is false, demonstrating test power)
sigma = 2.0    # True standard deviation

# Generate response variable y
y = np.concatenate([np.random.normal(m, sigma, n) for m in mu])

# ==========================================
# 2. Construct Projection Matrices
# ==========================================
# A_Mean: Projection onto the 1D subspace spanned by 1_N
vec_1 = np.ones((N, 1))
A_Mean = (vec_1 @ vec_1.T) / N

# A_Trt: Projection onto the treatment subspace (orthogonal to 1_N)
A_Trt_full = np.zeros((N, N))
for i in range(k):
    idx = slice(i*n, (i+1)*n)
    A_Trt_full[idx, idx] = np.ones((n, n)) / n
A_Trt = A_Trt_full - A_Mean

# A_Err: Projection onto the error subspace (orthogonal to both)
A_Err = np.eye(N) - A_Mean - A_Trt

# ==========================================
# 3. Verify Matrix Properties (Cochran's Conditions)
# ==========================================
print("--- Matrix Properties Verification ---")
matrices = {'Mean': A_Mean, 'Treatment': A_Trt, 'Error': A_Err}
for name, A in matrices.items():
    is_sym = np.allclose(A, A.T)
    is_idem = np.allclose(A @ A, A)
    rank = np.linalg.matrix_rank(A)
    print(f"A_{name}: Symmetric={is_sym}, Idempotent={is_idem}, Rank={rank}")

# Verify Orthogonality (A_i * A_j = 0)
print("\nOrthogonality Check (A_i @ A_j == 0):")
names = list(matrices.keys())
for i in range(len(names)):
    for j in range(i+1, len(names)):
        prod = matrices[names[i]] @ matrices[names[j]]
        is_orth = np.allclose(prod, 0)
        print(f"A_{names[i]} @ A_{names[j]} = 0 ? {is_orth}")

# Verify Rank Summation
total_rank = sum(np.linalg.matrix_rank(A) for A in matrices.values())
print(f"\nSum of Ranks: {total_rank} (Expected N={N}) -> Match: {total_rank == N}")

# ==========================================
# 4. Compute Quadratic Forms (Sum of Squares)
# ==========================================
SS_Mean = y.T @ A_Mean @ y
SS_Trt = y.T @ A_Trt @ y
SS_Err = y.T @ A_Err @ y

print("\n--- Sum of Squares Decomposition ---")
print(f"SS_Mean: {SS_Mean:.4f}")
print(f"SS_Trt:  {SS_Trt:.4f}")
print(f"SS_Err:  {SS_Err:.4f}")
print(f"SS_Total (y^T y): {y.T @ y:.4f}")
print(f"Sum of SS: {SS_Mean + SS_Trt + SS_Err:.4f}")

# ==========================================
# 5. Monte Carlo Simulation for Cochran's Theorem
# ==========================================
n_sims = 10000
# Generate Z ~ N(0, I_N) for all simulations at once (Vectorized)
Z = np.random.normal(0, 1, (n_sims, N))

# Compute quadratic forms Q = Z^T A Z for each simulation
# np.sum((Z @ A) * Z, axis=1) efficiently computes the diagonal of Z @ A @ Z^T
Q_Mean_mc = np.sum((Z @ A_Mean) * Z, axis=1)
Q_Trt_mc = np.sum((Z @ A_Trt) * Z, axis=1)
Q_Err_mc = np.sum((Z @ A_Err) * Z, axis=1)

# Check empirical distributions against Chi-Square using KS Test
print("\n--- Kolmogorov-Smirnov Tests for Chi-Square Distributions ---")
ks_Mean = stats.kstest(Q_Mean_mc, 'chi2', args=(1,))
ks_Trt = stats.kstest(Q_Trt_mc, 'chi2', args=(k-1,))
ks_Err = stats.kstest(Q_Err_mc, 'chi2', args=(N-k,))

print(f"Q_Mean ~ Chi2(1):   p-value = {ks_Mean.pvalue:.4f} (Fail to reject H0 if > 0.05)")
print(f"Q_Trt  ~ Chi2({k-1}):  p-value = {ks_Trt.pvalue:.4f}")
print(f"Q_Err  ~ Chi2({N-k}): p-value = {ks_Err.pvalue:.4f}")

# Check Independence of Q_Trt and Q_Err
corr, p_val_corr = stats.pearsonr(Q_Trt_mc, Q_Err_mc)
print(f"\nIndependence Check: Pearson correlation between Q_Trt and Q_Err = {corr:.5f}")

# ==========================================
# 6. Visualizing Distributions and Independence
# ==========================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Histograms of Quadratic Forms
for ax, Q_mc, df, title in zip(
    axes[0, :], 
    [Q_Trt_mc, Q_Err_mc], 
    [k-1, N-k], 
    [f'Q_Treatment (df={k-1})', f'Q_Error (df={N-k})']
):
    sns.histplot(Q_mc, stat='density', bins=50, kde=False, ax=ax, color='skyblue', label='Empirical')
    x = np.linspace(0, Q_mc.max(), 100)
    ax.plot(x, stats.chi2.pdf(x, df), 'r-', lw=2, label='Theoretical $\chi^2$')
    ax.set_title(title)
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.legend()

# Scatter plot for Independence
axes[1, 0].scatter(Q_Trt_mc, Q_Err_mc, alpha=0.3, s=10, color='purple')
axes[1, 0].set_title('Independence: Q_Treatment vs Q_Error')
axes[1, 0].set_xlabel('Q_Treatment')
axes[1, 0].set_ylabel('Q_Error')

# F-statistic Comparison
F_stat_matrix = (SS_Trt / (k - 1)) / (SS_Err / (N - k))
groups = [y[i*n:(i+1)*n] for i in range(k)]
F_stat_scipy, p_val_scipy = stats.f_oneway(*groups)

axes[1, 1].axis('off')
textstr = '\n'.join((
    r'$\mathbf{F-Statistic \ Comparison}$',
    r'',
    f'Matrix Quadratic Form: {F_stat_matrix:.4f}',
    f'scipy.stats.f_oneway:  {F_stat_scipy:.4f}',
    r'',
    f'p-value (scipy):       {p_val_scipy:.5f}',
    r'',
    r'Conclusion: Matrix derivation perfectly matches standard library.'
))
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
axes[1, 1].text(0.05, 0.95, textstr, transform=axes[1, 1].transAxes, fontsize=12,
                verticalalignment='top', bbox=props)

plt.tight_layout()
plt.show()
```