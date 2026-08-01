# 📋 Master Cheat Sheet: Cochran's Theorem · ANOVA · Tukey's HSD

---

## PART A — GENERAL DESIGN OF EXPERIMENTS (DoE) TERMS
*These terms are shared across all three topics.*

| Term | Definition |
|:---|:---|
| **Experiment** | A planned procedure carried out under controlled conditions to discover an unknown effect, test a hypothesis, or demonstrate a known law. |
| **Experimental Unit** | The smallest physical entity to which a treatment is independently applied (e.g., a single plant, a patient, a plot of land). |
| **Response Variable (Dependent Variable)** | The measurable outcome of interest that is observed and recorded for each experimental unit (denoted $Y_{ij}$). |
| **Factor** | An independent variable whose effect on the response is being studied. A factor is categorical in ANOVA (e.g., "Fertilizer Type"). |
| **Level** | A specific value or category of a factor (e.g., if the factor is "Fertilizer Type," the levels might be "Organic," "Synthetic," "None"). |
| **Treatment** | A specific combination of factor levels applied to an experimental unit. In a one-factor design, a treatment is synonymous with a factor level. |
| **Replicate** | An independent repetition of a treatment on a distinct experimental unit. Replicates provide an estimate of experimental error. |
| **Control** | A baseline treatment (often "no treatment" or "standard treatment") used as a reference for comparing the effects of other treatments. |
| **Randomization** | The process of randomly assigning treatments to experimental units to eliminate systematic bias and ensure the validity of statistical tests. |
| **Blocking** | A design technique that groups similar experimental units into homogeneous blocks to reduce unexplained variability (e.g., blocking by age group). |
| **Confounding** | A situation where the effect of one factor cannot be distinguished from the effect of another factor or lurking variable. |
| **Main Effect** | The average effect of a single factor on the response, averaged over all levels of other factors. |
| **Interaction** | A situation where the effect of one factor on the response depends on the level of another factor (i.e., the factors are not additive). |
| **Balanced Design** | An experimental design where every treatment combination has the same number of replicates ($n_1 = n_2 = \dots = n_k$). |
| **Unbalanced Design** | A design where the number of replicates differs across treatments ($n_i \neq n_j$ for some $i, j$). |
| **Null Hypothesis ($H_0$)** | The default assumption of "no effect" or "no difference" (e.g., $H_0: \mu_1 = \mu_2 = \dots = \mu_k$). |
| **Alternative Hypothesis ($H_1$ or $H_a$)** | The hypothesis that contradicts $H_0$; at least one parameter differs from the null value. |
| **Type I Error ($\alpha$)** | The error of rejecting $H_0$ when it is actually true (a "false positive"). The probability is the significance level $\alpha$. |
| **Type II Error ($\beta$)** | The error of failing to reject $H_0$ when it is actually false (a "false negative"). |
| **Significance Level ($\alpha$)** | The pre-specified maximum acceptable probability of a Type I error (commonly 0.05 or 0.01). |
| **Statistical Power ($1 - \beta$)** | The probability of correctly rejecting $H_0$ when $H_1$ is true. Power increases with sample size, effect size, and $\alpha$. |
| **Effect Size** | A quantitative measure of the magnitude of a treatment difference (e.g., Cohen's $d$, $\eta^2$), independent of sample size. |

---

## PART B — COCHRAN'S THEOREM TERMS
*Terms specific to the mathematical and linear-algebraic foundations.*

| Term | Definition |
|:---|:---|
| **Cochran's Theorem (1934)** | A theorem stating that if $\sum_{k=1}^p A_k = I_N$ and $\mathbf{z} \sim \mathcal{N}(\mathbf{0}, I_N)$, then the quadratic forms $Q_k = \mathbf{z}^T A_k \mathbf{z}$ are independent $\chi^2_{r_k}$ variables **if and only if** each $A_k$ is idempotent (equivalently, $\sum r_k = N$). |
| **Quadratic Form** | A scalar-valued function of a vector $\mathbf{z}$ defined as $Q = \mathbf{z}^T A \mathbf{z}$, where $A$ is a symmetric matrix. In ANOVA, sums of squares are quadratic forms. |
| **Symmetric Matrix** | A square matrix $A$ satisfying $A = A^T$ (i.e., $a_{ij} = a_{ji}$ for all $i, j$). All projection matrices in ANOVA are symmetric. |
| **Idempotent Matrix** | A matrix $A$ satisfying $A^2 = A$. Geometrically, applying the projection twice is the same as applying it once. This is the key algebraic condition in Cochran's Theorem. |
| **Orthogonal Projection Matrix** | A symmetric, idempotent matrix $P$ that projects vectors onto a subspace. It satisfies $P = P^T = P^2$ and $P(I - P) = 0$. |
| **Mutual Orthogonality of Matrices** | Two matrices $A_i$ and $A_j$ are mutually orthogonal if $A_i A_j = 0$ (the zero matrix). This ensures the corresponding quadratic forms are independent. |
| **Spectral Decomposition (Eigendecomposition)** | The factorization of a symmetric matrix as $A = U \Lambda U^T$, where $U$ is orthogonal and $\Lambda$ is diagonal containing the eigenvalues. Used to analyze quadratic forms. |
| **Eigenvalue ($\lambda$)** | A scalar such that $A\mathbf{v} = \lambda \mathbf{v}$ for some non-zero vector $\mathbf{v}$. For idempotent matrices, eigenvalues are restricted to $\{0, 1\}$. |
| **Eigenvector ($\mathbf{v}$)** | A non-zero vector that is only scaled (not rotated) by the matrix $A$: $A\mathbf{v} = \lambda \mathbf{v}$. |
| **Rank of a Matrix** | The number of linearly independent rows (or columns). For an idempotent matrix, $\text{rank}(A) = \text{tr}(A) = \sum \lambda_i$. |
| **Trace of a Matrix ($\text{tr}$)** | The sum of the diagonal elements of a square matrix. For idempotent matrices, the trace equals the rank and the degrees of freedom. |
| **Degrees of Freedom (df)** | The number of independent pieces of information available to estimate a parameter. In Cochran's context, $df_k = \text{rank}(A_k)$. |
| **Chi-Squared Distribution ($\chi^2_r$)** | The distribution of the sum of $r$ independent squared standard normal variables: $\chi^2_r = \sum_{i=1}^r Z_i^2$. Mean $= r$, Variance $= 2r$. |
| **Stochastic Independence** | Two random variables $X$ and $Y$ are independent if their joint distribution factors: $f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y)$. Cochran's Theorem guarantees this for the $Q_k$. |
| **Craig's Theorem** | A result stating that for $\mathbf{z} \sim \mathcal{N}(\mathbf{0}, I)$, two quadratic forms $\mathbf{z}^T A \mathbf{z}$ and $\mathbf{z}^T B \mathbf{z}$ are independent **if and only if** $AB = 0$. |
| **Simultaneous Diagonalization** | The process of finding a single orthogonal matrix $U$ that diagonalizes multiple symmetric matrices at once. Possible when the matrices commute ($A_i A_j = A_j A_i$). |
| **Positive Semi-Definite (PSD) Matrix** | A symmetric matrix $A$ where $\mathbf{z}^T A \mathbf{z} \geq 0$ for all $\mathbf{z}$. All idempotent matrices are PSD (eigenvalues $\geq 0$). |
| **Orthogonal Subspaces** | Two subspaces $V_1, V_2 \subseteq \mathbb{R}^N$ are orthogonal if every vector in $V_1$ is perpendicular to every vector in $V_2$. Cochran's theorem decomposes $\mathbb{R}^N$ into orthogonal subspaces. |
| **i.i.d. Normal Errors** | The assumption that error terms $\epsilon_{ij}$ are independent and identically distributed as $\mathcal{N}(0, \sigma^2)$. This is the foundational assumption enabling Cochran's Theorem in ANOVA. |

---

## PART C — ANOVA (Analysis of Variance) TERMS
*Terms specific to the F-test and variance decomposition.*

| Term | Definition |
|:---|:---|
| **ANOVA (Analysis of Variance)** | A collection of statistical models and procedures that partition the total observed variance into components attributable to different sources (treatments, blocks, error) to test hypotheses about group means. |
| **One-Way ANOVA** | ANOVA with a single factor. Tests $H_0: \mu_1 = \mu_2 = \dots = \mu_k$ using one F-test. |
| **Two-Way ANOVA** | ANOVA with two factors. Tests main effects of each factor and their interaction using three separate F-tests. |
| **Omnibus Test** | A test that evaluates a global null hypothesis (e.g., "all means are equal") rather than specific pairwise differences. The ANOVA F-test is an omnibus test. |
| **Grand Mean ($\bar{Y}_{..}$)** | The overall average of all $N$ observations across all treatments: $\bar{Y}_{..} = \frac{1}{N}\sum_{i,j} Y_{ij}$. |
| **Group Mean ($\bar{Y}_{i.}$)** | The average of the $n_i$ observations within treatment group $i$: $\bar{Y}_{i.} = \frac{1}{n_i}\sum_{j} Y_{ij}$. |
| **$SS_{Total}$ (Total Sum of Squares)** | The total variability in the data: $SS_{Total} = \sum_{i,j}(Y_{ij} - \bar{Y}_{..})^2$. Has $N-1$ degrees of freedom. |
| **$SS_{Treatment}$ (Between-Group SS)** | The variability explained by differences among group means: $SS_{Trt} = \sum_i n_i(\bar{Y}_{i.} - \bar{Y}_{..})^2$. Has $k-1$ df. |
| **$SS_{Error}$ (Within-Group SS / Residual SS)** | The unexplained variability within groups: $SS_{Err} = \sum_{i,j}(Y_{ij} - \bar{Y}_{i.})^2$. Has $N-k$ df. |
| **$SS_{Mean}$ (Correction for the Mean)** | The sum of squares due to the grand mean: $SS_{Mean} = N\bar{Y}_{..}^2$. Has 1 df. Often omitted from the ANOVA table. |
| **Mean Square ($MS$)** | A sum of squares divided by its degrees of freedom: $MS = SS / df$. It is an unbiased estimate of a variance component. |
| **$MS_{Treatment}$ ($MS_{Trt}$)** | $SS_{Trt} / (k-1)$. Estimates $\sigma^2 + \frac{\sum n_i \tau_i^2}{k-1}$. Inflated above $\sigma^2$ when treatment effects exist. |
| **$MS_{Error}$ ($MS_{Err}$ or $MSE$)** | $SS_{Err} / (N-k)$. An unbiased estimate of $\sigma^2$ regardless of whether $H_0$ is true. The "pooled within-group variance." |
| **F-Statistic** | The test statistic $F = MS_{Trt} / MS_{Err}$. Under $H_0$, $F \sim F_{k-1, \, N-k}$. Large values indicate evidence against $H_0$. |
| **F-Distribution ($F_{d_1, d_2}$)** | The distribution of the ratio of two independent chi-squared variables divided by their df: $F = \frac{\chi^2_{d_1}/d_1}{\chi^2_{d_2}/d_2}$. Right-skewed, always positive. |
| **ANOVA Table** | A summary table with columns: Source, df, SS, MS, F, p-value. Rows typically include Treatment, Error, and Total. |
| **Residual ($e_{ij}$)** | The difference between an observed value and its group mean: $e_{ij} = Y_{ij} - \bar{Y}_{i.}$. Residuals estimate the true errors $\epsilon_{ij}$. |
| **Homoscedasticity (Equal Variances)** | The assumption that all treatment groups share a common variance: $\sigma_1^2 = \sigma_2^2 = \dots = \sigma_k^2 = \sigma^2$. Violated → use Welch's ANOVA. |
| **Heteroscedasticity** | The condition where group variances are unequal. Invalidates the standard F-test and Tukey's test. |
| **Normality Assumption** | The assumption that the error terms $\epsilon_{ij} \sim \mathcal{N}(0, \sigma^2)$. Checked via Q-Q plots or Shapiro-Wilk test on residuals. |
| **Independence Assumption** | The assumption that observations are statistically independent of each other. Ensured by proper randomization. |
| **Eta-Squared ($\eta^2$)** | An effect size measure: $\eta^2 = SS_{Trt} / SS_{Total}$. Represents the proportion of total variance explained by the treatment. Ranges from 0 to 1. |
| **Adjusted $R^2$** | A modified version of $\eta^2$ that penalizes for the number of groups, preventing overestimation of effect size in small samples. |
| **P-value** | The probability, under $H_0$, of observing an F-statistic as extreme or more extreme than the one calculated. If $p < \alpha$, reject $H_0$. |
| **Fixed Effects Model** | An ANOVA model where the treatment levels are the only levels of interest (e.g., specific drug doses). Inferences apply only to those levels. |
| **Random Effects Model** | An ANOVA model where the treatment levels are a random sample from a larger population of levels. Inferences generalize to the population. |
| **Welch's ANOVA** | A robust alternative to the standard F-test that does not assume equal variances. Uses a modified F-statistic with adjusted df (Welch-Satterthwaite). |
| **Kruskal-Wallis Test** | A non-parametric alternative to one-way ANOVA that ranks the data and tests whether group medians differ. Used when normality fails. |

---

## PART D — TUKEY'S HSD TEST TERMS
*Terms specific to post-hoc pairwise comparisons.*

| Term | Definition |
|:---|:---|
| **Post-Hoc Test** | A statistical procedure performed *after* a significant omnibus ANOVA to determine which specific group means differ from each other. "Post-hoc" = "after the fact." |
| **Tukey's HSD (Honestly Significant Difference)** | A post-hoc test that compares all $\binom{k}{2}$ pairwise mean differences while controlling the Family-Wise Error Rate at level $\alpha$. Developed by John W. Tukey (1949). |
| **Pairwise Comparison** | A hypothesis test comparing exactly two group means: $H_0^{(ij)}: \mu_i = \mu_j$ vs. $H_1^{(ij)}: \mu_i \neq \mu_j$. |
| **Multiple Comparisons Problem** | The inflation of the overall Type I error rate when conducting many simultaneous hypothesis tests. With $m$ tests at level $\alpha$, the probability of ≥1 false positive is $1-(1-\alpha)^m$. |
| **Family-Wise Error Rate (FWER)** | The probability of making **at least one** Type I error across an entire *family* of $m$ simultaneous tests. Tukey's HSD controls FWER at exactly $\alpha$. |
| **Per-Comparison Error Rate (PCER)** | The Type I error rate for a single individual test. If unadjusted, PCER = $\alpha$ for each test, but FWER inflates. |
| **Studentized Range Distribution ($q_{k, \nu}$)** | The sampling distribution of the range of $k$ independent standard normal variables divided by an independent estimate of their standard deviation with $\nu$ df. The reference distribution for Tukey's test. |
| **Studentized Range Statistic ($q$)** | The test statistic for Tukey's test: $q = \frac{\bar{Y}_{max} - \bar{Y}_{min}}{\sqrt{MS_{Err}/n}}$. Compared against critical values from the $q$-distribution. |
| **HSD Critical Value** | The minimum mean difference required for significance: $\text{HSD} = q_{\alpha, k, N-k} \cdot \sqrt{MS_{Err}/n}$. Any pair with $|\bar{Y}_i - \bar{Y}_j| > \text{HSD}$ is significant. |
| **Simultaneous Confidence Intervals** | A set of confidence intervals constructed so that the probability that **all** intervals simultaneously contain their true parameter values is $1 - \alpha$. Tukey's intervals: $(\bar{Y}_i - \bar{Y}_j) \pm \text{HSD}$. |
| **Tukey-Kramer Method** | An extension of Tukey's HSD for **unbalanced designs** ($n_i \neq n_j$). Replaces $\sqrt{MS_{Err}/n}$ with $\sqrt{\frac{MS_{Err}}{2}\left(\frac{1}{n_i} + \frac{1}{n_j}\right)}$. |
| **Compact Letter Display (CLD)** | A visual summary of Tukey's results where groups sharing a common letter are not significantly different (e.g., "a", "ab", "b"). |
| **Bonferroni Correction** | A simpler (more conservative) alternative to Tukey. Divides $\alpha$ by the number of comparisons: $\alpha_{adj} = \alpha / \binom{k}{2}$. Controls FWER but has lower power. |
| **Scheffé's Method** | A post-hoc procedure that controls FWER for **all possible contrasts** (not just pairwise). More conservative than Tukey for pairwise comparisons, but more flexible. |
| **Dunnett's Test** | A post-hoc test that compares each treatment group to a **single control group** only. More powerful than Tukey when only control comparisons are of interest. |
| **Games-Howell Test** | A post-hoc test similar to Tukey but designed for **unequal variances and unequal sample sizes**. Uses Welch-type df adjustments. The go-to when homoscedasticity fails. |
| **Contrast** | A linear combination of group means $\sum c_i \mu_i$ where $\sum c_i = 0$. Pairwise differences are a special case ($c_i = 1, c_j = -1$, rest 0). |
| **Orthogonal Contrasts** | A set of contrasts whose coefficient vectors are mutually orthogonal. They partition $SS_{Trt}$ into independent 1-df components. |
| **Margin of Error (for Tukey)** | The half-width of the Tukey confidence interval: $ME = q_{\alpha, k, N-k} \cdot \sqrt{MS_{Err}/n}$. |
| **Adjusted P-value** | A p-value that has been corrected for multiple comparisons. In Tukey's test, the adjusted p-value reflects the FWER, not the PCER. |

---

## PART E — QUICK-REFERENCE RELATIONSHIP MAP

```
                    ┌─────────────────────────────────┐
                    │       COCHRAN'S THEOREM          │
                    │  (Mathematical Foundation)       │
                    │                                  │
                    │  • Proves SS decomposition       │
                    │  • Guarantees independence       │
                    │  • Validates χ² distributions    │
                    └──────────┬──────────────────────┘
                               │
                    provides theoretical
                    justification for
                               │
                    ┌──────────▼──────────────────────┐
                    │         ANOVA (F-TEST)           │
                    │    (Global Omnibus Procedure)    │
                    │                                  │
                    │  • F = MS_Trt / MS_Err          │
                    │  • Tests: ALL means equal?       │
                    │  • Controls PEER at α            │
                    └──────────┬──────────────────────┘
                               │
                    if F is significant
                    (reject H₀), proceed to
                               │
                    ┌──────────▼──────────────────────┐
                    │       TUKEY'S HSD TEST           │
                    │   (Post-Hoc Localization)        │
                    │                                  │
                    │  • q = (Ȳᵢ - Ȳⱼ) / √(MSE/n)   │
                    │  • Tests: WHICH means differ?    │
                    │  • Controls FWER at α            │
                    │  • Uses same MSE from ANOVA      │
                    └─────────────────────────────────┘
```

> **One-liner summary:** Cochran's Theorem *proves the math works*, ANOVA *tells you something happened*, and Tukey's HSD *tells you exactly what happened*.