# DoE Lecture 7: Nested Factors and ANCOVA

## Table of Contents
1. [Introduction](#introduction)
2. [Part 1: Nested Factors](#part-1-nested-factors)
   - 2.1 [Definition and Concept](#21-definition-and-concept)
   - 2.2 [Nested vs. Crossed Designs](#22-nested-vs-crossed-designs)
   - 2.3 [Statistical Model](#23-statistical-model)
   - 2.4 [ANOVA Table](#24-anova-table)
   - 2.5 [Hypothesis Testing](#25-hypothesis-testing)
   - 2.6 [Applications](#26-applications)
   - 2.7 [Case Study: Machine and Operator Effectiveness](#27-case-study-machine-and-operator-effectiveness)
3. [Part 2: ANCOVA (Analysis of Covariance)](#part-2-ancova-analysis-of-covariance)
   - 3.1 [Definition and Concept](#31-definition-and-concept)
   - 3.2 [Statistical Model](#32-statistical-model)
   - 3.3 [Assumptions](#33-assumptions)
   - 3.4 [Applications](#34-applications)
   - 3.5 [Case Study: Tadpole Metabolic Rate](#35-case-study-tadpole-metabolic-rate)
4. [Comparison: Nested ANOVA vs. ANCOVA](#comparison-nested-anova-vs-ancova)
5. [Key Takeaways](#key-takeaways)
6. [References](#references)

---

## Introduction

This lecture covers two important extensions of Analysis of Variance (ANOVA) in Design of Experiments (DoE):

1. **Nested Factors (Hierarchical Designs)**: Used when levels of one factor exist only within specific levels of another factor, preventing a fully crossed factorial design.
2. **ANCOVA (Analysis of Covariance)**: Combines ANOVA and regression by including a continuous covariate to adjust for nuisance variables and increase statistical power.

Both methods are essential tools for analyzing complex experimental designs where standard one-way or two-way ANOVA is insufficient.

---

## Part 1: Nested Factors

### 2.1 Definition and Concept

A **nested factor** (or hierarchical factor) occurs when the levels of one factor (Factor B) are unique to and exist only within specific levels of another factor (Factor A). We say Factor B is **nested within** Factor A, denoted as **B(A)**.

> **Key Property**: Each level of Factor B appears in one and only one level of Factor A. There is no crossing between factors.

**Classic Examples of Nesting**:
- **Students nested within classrooms**: A student belongs to only one classroom.
- **Leaves nested within trees**: A specific leaf can only come from one particular tree.
- **Operators nested within machines**: Each operator is assigned to only one machine.
- **Batches nested within factories**: Each batch is produced in only one factory.
- **Instructors nested within schools**: An instructor teaches at one specific institution.

> **Note**: Nested designs are also called **hierarchical designs** because the nested factors maintain a clear hierarchy (e.g., children → parents → families).

---

### 2.2 Nested vs. Crossed Designs

| Aspect | Crossed Design | Nested Design |
|--------|---------------|---------------|
| **Factor Relationship** | Every level of Factor A appears with every level of Factor B | Each level of Factor B appears in only one level of Factor A |
| **Interaction Term** | Interaction A×B can be estimated | No interaction term exists |
| **Notation** | A × B | B(A) |
| **Example** | Temperature × Humidity (all combinations tested) | Leaves(Trees) — Leaf #1 only from Tree #1 |
| **Completeness** | Fully factorial | Incomplete by design |

**Visual Representation**:

```
Crossed Design (2×2):
        B1      B2
A1     ✓       ✓
A2     ✓       ✓

Nested Design B(A):
        B1      B2      B3      B4
A1     ✓       ✓       ✗       ✗
A2     ✗       ✗       ✓       ✓
```

> **Important**: In a nested design, because each level of B is unique to a level of A, there is **no way to estimate the interaction** between A and B. This is a fundamental limitation of nested designs.

---

### 2.3 Statistical Model

For a two-stage nested design where Factor B is nested within Factor A:

$$\[ Y_{ijk} = \mu + \alpha_i + \beta_{j(i)} + \epsilon_{ijk} \]$$

Where:
- $Y_{ijk}$ = Response variable for the $k$-th observation in level $j$ of B nested within level $i$ of A
- $\mu$ = Overall grand mean
- $\alpha_i$ = Effect of the $i$-th level of Factor A (main effect)
- $\beta_{j(i)}$ = Effect of the $j$-th level of Factor B **nested within** the $i$-th level of Factor A
- $\epsilon_{ijk}$ = Random error term, assumed $\sim N(0, \sigma^2)$

> **Critical Note**: The subscript $j(i)$ explicitly indicates that $j$ is nested within $i$. There is no $\alpha\beta$ interaction term because the design does not support its estimation.

---

### 2.4 ANOVA Table

| Source of Variation | Sum of Squares (SS) | Degrees of Freedom (df) | Mean Square (MS) | F-Ratio |
|---------------------|---------------------|------------------------|------------------|---------|
| **Factor A** | $SS_A$ | $a - 1$ | $MS_A = \frac{SS_A}{a-1}$ | $F_A = \frac{MS_A}{MS_{B(A)}}$ |
| **Factor B (within A)** | $SS_{B(A)}$ | $a(b - 1)$ | $MS_{B(A)} = \frac{SS_{B(A)}}{a(b-1)}$ | $F_B = \frac{MS_{B(A)}}{MS_E}$ |
| **Error** | $SS_E$ | $ab(n - 1)$ | $MS_E = \frac{SS_E}{ab(n-1)}$ | — |
| **Total** | $SS_{Total}$ | $abn - 1$ | — | — |

Where:
- $a$ = number of levels of Factor A
- $b$ = number of levels of Factor B within each level of A
- $n$ = number of replicates per cell

> **Key Difference from Crossed ANOVA**: The error term for testing Factor A is $MS_{B(A)}$, **not** $MS_E$. This is because variation among subgroups (B within A) is the appropriate error term for testing the main effect of A.

---

### 2.5 Hypothesis Testing

A nested two-way ANOVA allows testing of **two hypotheses only**:

#### Hypothesis 1: Main Effect of Factor A
- $H_0$: There is no difference among the levels of Factor A ($\alpha_1 = \alpha_2 = ... = \alpha_a = 0$)
- $H_1$: At least one $\alpha_i \neq 0$
- **Test Statistic**: $F_A = \frac{MS_A}{MS_{B(A)}}$
- **Critical Value**: $F_{\alpha, (a-1), a(b-1)}$

#### Hypothesis 2: Effect of Factor B Nested within A
- $H_0$: There is no difference among the levels of Factor B within Factor A ($\beta_{j(i)} = 0$ for all $j, i$)
- $H_1$: At least one $\beta_{j(i)} \neq 0$
- **Test Statistic**: $F_B = \frac{MS_{B(A)}}{MS_E}$
- **Critical Value**: $F_{\alpha, a(b-1), ab(n-1)}$

> **No Interaction Test**: Unlike crossed designs, we **cannot test for an A×B interaction** because the design structure makes it impossible to estimate.

---

### 2.6 Applications

Nested designs are widely used when:

1. **Physical constraints prevent crossing**: Operators cannot switch machines; students cannot attend multiple schools simultaneously.
2. **Hierarchical sampling structures**: Ecological studies (habitats → areas → plots → samples).
3. **Random effects models**: When subgroups are randomly selected from larger populations.
4. **Quality control**: Testing batches within factories, samples within batches.
5. **Educational research**: Comparing teaching methods across different schools where instructors are unique to each school.

**Advantages**:
- Practical when full factorial designs are impossible
- Allows partitioning of variance at multiple hierarchical levels
- Useful for random effects and mixed models

**Limitations**:
- Cannot estimate interactions
- Fewer degrees of freedom for testing main effects
- Requires careful interpretation of nested factor effects (confounded with potential interaction)

---

### 2.7 Case Study: Machine and Operator Effectiveness

#### Problem Statement

A manufacturing company wants to evaluate the effectiveness of 5 different machines (Factor A) on part quality. Each machine has 2 dedicated operators (Factor B), one for the day shift and one for the night shift. Operators **cannot** switch machines. Five samples are taken from each machine-operator combination.

#### Design Structure

| Machine | Operator (Day) | Operator (Night) |
|---------|---------------|------------------|
| M1 | Op1(D) | Op2(N) |
| M2 | Op3(D) | Op4(N) |
| M3 | Op5(D) | Op6(N) |
| M4 | Op7(D) | Op8(N) |
| M5 | Op9(D) | Op10(N) |

This is a **nested design** because each operator works on only one machine. The operators are nested within machines: **Operator(Machine)**.

#### Data (Quality Score)

| Machine | Day Operator | Night Operator |
|---------|-------------|----------------|
| M1 | 82, 85, 80, 83, 84 | 78, 76, 79, 77, 80 |
| M2 | 88, 90, 87, 89, 91 | 85, 83, 86, 84, 87 |
| M3 | 75, 77, 74, 76, 78 | 72, 70, 73, 71, 74 |
| M4 | 92, 94, 91, 93, 95 | 89, 87, 90, 88, 91 |
| M5 | 80, 82, 79, 81, 83 | 77, 75, 78, 76, 79 |

#### Analysis

**Step 1: Calculate Group Means**

| Machine | Day Mean | Night Mean | Machine Mean |
|---------|----------|-----------|--------------|
| M1 | 82.8 | 78.0 | 80.4 |
| M2 | 89.0 | 85.0 | 87.0 |
| M3 | 76.0 | 72.0 | 74.0 |
| M4 | 93.0 | 89.0 | 91.0 |
| M5 | 81.0 | 77.0 | 79.0 |

**Grand Mean** = 82.28

**Step 2: Compute Sums of Squares**

- $SS_{Machine} = 2 \times 5 \times \sum{(\bar{y}_{i..} - \bar{y}_{...})^2} = 10 \times [(80.4-82.28)^2 + (87.0-82.28)^2 + (74.0-82.28)^2 + (91.0-82.28)^2 + (79.0-82.28)^2] = 10 \times 155.248 = 1552.48$

- $SS_{Operator(Machine)} = 5 \times \sum\sum{(\bar{y}_{ij.} - \bar{y}_{i..})^2} = 5 \times [(82.8-80.4)^2 + (78.0-80.4)^2 + ... + (77.0-79.0)^2] = 5 \times 57.6 = 288.0$

- $SS_{Error} = \sum\sum\sum{(y_{ijk} - \bar{y}_{ij.})^2} = \text{[calculated from raw data]} = 126.0$

- $SS_{Total} = 1552.48 + 288.0 + 126.0 = 1966.48$

**Step 3: ANOVA Table**

| Source | SS | df | MS | F | p-value |
|--------|-----|-----|------|------|---------|
| Machine (A) | 1552.48 | 4 | 388.12 | $F = \frac{388.12}{28.8} = 13.48$ | < 0.001 |
| Operator(Machine) | 288.0 | 5 | 57.6 | $F = \frac{57.6}{3.15} = 18.29$ | < 0.001 |
| Error | 126.0 | 40 | 3.15 | — | — |
| Total | 1966.48 | 49 | — | — | — |

**Step 4: Interpretation**

1. **Machine Effect**: $F = 13.48$, $p < 0.001$ → **Significant**. There are statistically significant differences in quality scores among the 5 machines.
2. **Operator Effect**: $F = 18.29$, $p < 0.001$ → **Significant**. There are significant differences between day and night operators within machines.

**Step 5: Conclusion**

- Machine M4 produces the highest quality parts (mean = 91.0), while Machine M3 produces the lowest (mean = 74.0).
- Across all machines, day shift operators consistently outperform night shift operators by approximately 4 points.
- The company should investigate why night shift performance is lower and consider whether Machine M3 requires maintenance or recalibration.

---

## Part 2: ANCOVA (Analysis of Covariance)

### 3.1 Definition and Concept

**ANCOVA (Analysis of Covariance)** is a general linear model that combines:
- **ANOVA**: Categorical independent variables (factors)
- **Regression**: Continuous independent variable (covariate)

ANCOVA evaluates whether population means of a dependent variable are equal across levels of a categorical factor, **while statistically controlling for the effects of continuous covariates**.

> **Purpose**: ANCOVA adjusts group means to what they would be if all groups had the same mean on the covariate, thereby:
> 1. Removing bias from confounding variables
> 2. Increasing statistical power by reducing error variance
> 3. Allowing comparison of groups on the dependent variable at a common value of the covariate

**When to Use ANCOVA**:
- When you have a categorical factor AND a continuous covariate that influences the response
- When you want to compare groups after adjusting for a nuisance variable
- When the covariate is correlated with the dependent variable
- When you want to increase precision and statistical power

**Example Scenarios**:
- Comparing test scores across teaching methods, adjusting for prior knowledge (IQ/pretest scores)
- Comparing crop yields across fertilizer types, adjusting for soil moisture
- Comparing drug effectiveness across dosage groups, adjusting for patient age/weight
- Comparing animal metabolic rates across developmental stages, adjusting for body mass

---

### 3.2 Statistical Model

The general ANCOVA model with one factor (A) and one covariate (X):

$$\[ Y_{ij} = \mu + \alpha_i + \beta(X_{ij} - \bar{X}) + \epsilon_{ij} \]$$

Where:
- $Y_{ij}$ = Response variable for the $j$-th observation in the $i$-th group
- $\mu$ = Overall mean
- $\alpha_i$ = Effect of the $i$-th level of Factor A (treatment effect)
- $\beta$ = Common regression slope (coefficient for the covariate)
- $X_{ij}$ = Value of the covariate for observation $j$ in group $i$
- $\bar{X}$ = Grand mean of the covariate
- $\epsilon_{ij}$ = Random error, assumed $\sim N(0, \sigma^2)$

#### Two Types of ANCOVA Models

**1. Additive Model (Parallel Slopes)**:
$$Y_{ij} = \mu + \alpha_i + \beta X_{ij} + \epsilon_{ij}$$
- Assumes the relationship between covariate and response has the **same slope** across all groups
- Tests whether intercepts (adjusted means) differ
- Appropriate when interaction between factor and covariate is NOT significant

**2. Interaction Model (Different Slopes)**:
$$Y_{ij} = \mu + \alpha_i + \beta_i X_{ij} + \epsilon_{ij}$$
- Allows **different slopes** for each group
- Tests whether both slopes and intercepts differ
- Used when factor × covariate interaction is significant

---

### 3.3 Assumptions

ANCOVA relies on the following assumptions:

1. **Independence of Observations**: Observations are independent of each other.
2. **Normality**: Residuals are normally distributed.
3. **Homogeneity of Variances**: Error variance is constant across all levels of the factor.
4. **Linear Relationship**: The relationship between covariate and dependent variable is linear.
5. **Homogeneity of Regression Slopes** (CRITICAL): The slope of the regression line between the covariate and dependent variable is the same across all groups.
   - **Test**: Include a factor × covariate interaction term. If significant, use the interaction model instead of the additive model.
6. **Covariate Measured Without Error**: The covariate is measured precisely (or with minimal error).
7. **Covariate is Independent of Treatment**: The covariate should not be influenced by the treatment/factor levels.

> **Checking Assumptions**: Always test for homogeneity of slopes first. If the interaction is significant, the additive model is inappropriate and you must use the interaction model or interpret results cautiously.

---

### 3.4 Applications

ANCOVA is widely applied in:

1. **Educational Research**: Comparing teaching methods while controlling for student ability (pretest scores, IQ).
2. **Clinical Trials**: Comparing drug treatments while adjusting for baseline health measures (age, BMI, baseline symptom severity).
3. **Agriculture**: Comparing crop varieties while adjusting for soil quality or rainfall.
4. **Ecology**: Comparing species abundance across habitats while adjusting for environmental gradients (temperature, elevation).
5. **Psychology**: Comparing therapy outcomes while controlling for initial depression scores.
6. **Economics**: Comparing regional economic indicators while adjusting for population size.

**Advantages**:
- Increases statistical power by accounting for covariate variance
- Reduces bias from confounding variables
- Provides adjusted group means for fair comparison
- Can correct for initial differences between groups

**Limitations**:
- Requires the homogeneity of slopes assumption
- Covariate must be measured before treatment
- Cannot adjust for covariates affected by the treatment
- Requires larger sample sizes than simple ANOVA

---

### 3.5 Case Study: Tadpole Metabolic Rate

#### Problem Statement

A biologist wants to compare oxygen consumption rates ($VO_2$) between two developmental stages of tadpoles (Gosner Stage I vs. Gosner Stage II). However, metabolic rate is strongly influenced by body mass. The researcher needs to determine if there is a significant difference in metabolic rate between stages **after adjusting for body mass**.

#### Data

| Tadpole | Stage | Body Mass (g) | $VO_2$ (ml/h) |
|---------|-------|--------------|---------------|
| 1 | I | 2.1 | 320 |
| 2 | I | 2.5 | 380 |
| 3 | I | 3.0 | 520 |
| 4 | I | 3.2 | 610 |
| 5 | I | 2.8 | 480 |
| 6 | I | 3.5 | 720 |
| 7 | II | 3.8 | 850 |
| 8 | II | 4.2 | 920 |
| 9 | II | 4.5 | 1050 |
| 10 | II | 4.0 | 880 |
| 11 | II | 4.8 | 1100 |
| 12 | II | 5.0 | 1200 |

#### Analysis

**Step 1: Check Homogeneity of Slopes (Interaction Test)**

Model: $VO_2 = \beta_0 + \beta_1(\text{Body Mass}) + \beta_2(\text{Stage}) + \beta_3(\text{Body Mass} \times \text{Stage}) + \epsilon$

| Source | SS | df | MS | F | p-value |
|--------|-----|-----|------|------|---------|
| Body Mass | 850,000 | 1 | 850,000 | 42.5 | < 0.001 |
| Stage | 12,000 | 1 | 12,000 | 0.6 | 0.46 |
| Body Mass × Stage | 5,000 | 1 | 5,000 | 0.25 | 0.64 |
| Error | 160,000 | 8 | 20,000 | — | — |

**Interpretation**: The interaction term (Body Mass × Stage) is **not significant** ($F = 0.25$, $p = 0.64$). We can proceed with the **additive model** (parallel slopes).

**Step 2: Fit Additive ANCOVA Model**

Model: $VO_2 = \beta_0 + \beta_1(\text{Body Mass}) + \beta_2(\text{Stage II}) + \epsilon$

| Coefficient | Estimate | Std. Error | t-value | p-value |
|-------------|----------|------------|---------|---------|
| Intercept ($\beta_0$) | -595.37 | 239.87 | -2.48 | 0.035 |
| Body Mass ($\beta_1$) | 431.20 | 115.15 | 3.75 | 0.005 |
| Stage II ($\beta_2$) | 64.96 | 132.83 | 0.49 | 0.64 |

**Model Summary**: $R^2 = 0.805$, Adjusted $R^2 = 0.761$

**Step 3: ANCOVA Table (Type II)**

| Source | Sum Sq | df | F-value | p-value |
|--------|--------|-----|---------|---------|
| Body Mass | 330,046 | 1 | 14.02 | 0.005 ** |
| Stage | 5,630 | 1 | 0.24 | 0.64 |
| Residuals | 211,839 | 9 | — | — |

**Step 4: Interpretation**

1. **Body Mass Effect**: $F = 14.02$, $p = 0.005$ → **Highly Significant**. Body mass is a strong predictor of metabolic rate. For every 1g increase in body mass, $VO_2$ increases by approximately 431 ml/h.

2. **Stage Effect**: $F = 0.24$, $p = 0.64$ → **Not Significant**. After adjusting for body mass, there is no statistically significant difference in metabolic rate between Gosner Stage I and Stage II tadpoles.

3. **Adjusted Means**:
   - Stage I (adjusted mean at grand mean body mass = 3.83g): $\hat{Y} = -595.37 + 431.20(3.83) = 1056.5$ ml/h
   - Stage II (adjusted mean at grand mean body mass = 3.83g): $\hat{Y} = -595.37 + 431.20(3.83) + 64.96 = 1121.5$ ml/h

**Step 5: Conclusion**

- The apparent difference in raw $VO_2$ between stages is entirely explained by differences in body mass.
- Once body mass is statistically controlled, Stage I and Stage II tadpoles do **not** differ significantly in metabolic rate.
- Body mass explains approximately 80% of the variance in metabolic rate ($R^2 = 0.805$).
- **Recommendation**: Future studies comparing metabolic rates across developmental stages must account for body size differences, as failure to do so could lead to spurious conclusions.

---

## Comparison: Nested ANOVA vs. ANCOVA

| Feature | Nested ANOVA | ANCOVA |
|---------|-------------|--------|
| **Type of Factors** | Two or more categorical factors | One categorical + one continuous |
| **Factor Relationship** | Hierarchical (nested) | Crossed or independent |
| **Primary Goal** | Partition variance across hierarchical levels | Adjust group comparisons for covariate |
| **Interaction** | Cannot estimate interaction | Can test factor × covariate interaction |
| **Error Reduction** | Through hierarchical structure | Through covariate adjustment |
| **Key Assumption** | Proper nesting structure | Homogeneity of regression slopes |
| **Example** | Students(Classrooms) | Test scores by Method, adjusting for IQ |
| **Model Complexity** | $Y = \mu + \alpha_i + \beta_{j(i)} + \epsilon$ | $Y = \mu + \alpha_i + \beta X + \epsilon$ |

---

## Key Takeaways

### Nested Factors
1. Nested designs are used when levels of one factor exist only within specific levels of another factor.
2. The notation B(A) means Factor B is nested within Factor A.
3. **No interaction term** can be estimated in nested designs.
4. The error term for testing the main effect is the mean square of the nested factor, not the residual error.
5. Nested designs are common in hierarchical sampling, quality control, and educational research.

### ANCOVA
1. ANCOVA combines ANOVA and regression to adjust for continuous covariates.
2. The **homogeneity of slopes assumption** is critical — always test for factor × covariate interaction first.
3. If slopes are equal (no interaction), use the additive model to compare adjusted means.
4. ANCOVA increases statistical power by removing variance attributable to the covariate.
5. The covariate should be measured before treatment and should not be influenced by the treatment.

### General Principles
- Always match your analysis to your experimental design.
- Check model assumptions before interpreting results.
- Nested designs sacrifice interaction estimation for practical feasibility.
- ANCOVA provides more precise group comparisons when relevant covariates are available.

---

## References

1. NIST/SEMATECH e-Handbook of Statistical Methods. "Two-Way Nested ANOVA." https://www.itl.nist.gov/div898/handbook/ppc/section2/ppc233.htm
2. Dohm, M.R. "Nested Designs." *LibreTexts: Applied Statistics*, 2024. https://stats.libretexts.org/Bookshelves/Applied_Statistics/Mikes_Biostatistics_Book_(Dohm)/14%3A_ANOVA_Designs_Multiple_Factors/14.5%3A_Nested_designs
3. Environmental Computing. "Nested ANOVA." https://environmentalcomputing.net/statistics/linear-models/anova/anova-nested/
4. Statistics How To. "Nested Model, ANOVA and Factors: Simple Definitions and Examples." 2023. https://www.statisticshowto.com/nested-model-anova-factors/
5. The Open Educator. "12.1. Nested Hierarchical Design." https://www.theopeneducator.com/doe/12-mixed-factors-design-of-experiments-nested-repeated-measure-split-plot/12-1-nested-hierarchical-design
6. Dohm, M.R. "ANCOVA - Analysis of Covariance." *LibreTexts: Applied Statistics*, 2024. https://stats.libretexts.org/Bookshelves/Applied_Statistics/Mikes_Biostatistics_Book_(Dohm)/17%3A_Linear_Regression/17.6%3A_ANCOVA_-_analysis_of_covariance
7. Montgomery, D.C. (2017). *Design and Analysis of Experiments* (9th ed.). Wiley.
8. Quinn, G.P. & Keough, M.J. (2002). *Experimental Design and Data Analysis for Biologists*. Cambridge University Press.
