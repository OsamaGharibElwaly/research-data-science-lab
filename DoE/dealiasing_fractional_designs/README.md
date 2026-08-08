### One-sentence intuition

> **Aliasing is like two people wearing the same name tag; dealiasing is giving them different name tags so you can tell who is who.**

## Table of Contents
1. [Overview](#overview)
2. [Core Concepts](#core-concepts)
3. [Rules of Thumb](#rules-of-thumb)
4. [Case Studies](#case-studies)
5. [Workflow](#workflow)
6. [Common Pitfalls](#common-pitfalls)
7. [Comparisons](#comparisons)
8. [References](#references)

---

## Overview

Fractional factorial designs are powerful tools for screening experiments, but they come with a critical trade-off: **aliasing**. When we run a fraction of a full factorial, some effects become confounded (aliased) with each other, making it impossible to estimate them independently. **Dealiasing** refers to the family of techniques used to separate these confounded effects and recover clean estimates.

This lecture covers:
- Understanding the alias structure of fractional factorial designs
- Sequential experimentation (foldover, augmenting)
- Optimal follow-up designs
- Dealiasing via projection and model selection
- Advanced techniques: Bayesian dealiasing, D-optimal augmentation

### Why Dealiasing Matters

In a \(2^{7-4}\) design with 8 runs, 7 main effects and 21 two-factor interactions are estimated using only 7 degrees of freedom. The alias structure is dense. Without dealiasing, you cannot distinguish between real effects and their aliases, leading to false conclusions and missed opportunities for process improvement.

---

## Core Concepts

### 1. Alias Structure and the Defining Relation

In a \(2^{k-p}\) fractional factorial design, the defining relation determines which effects are confounded:

```
I = ABC       (for a 2^{3-1} design)
I = ABCD      (for a 2^{4-1} design)
I = ABCDE     (for a 2^{5-1} design)
```

The generalized interaction of any effect with the defining relation gives its alias set. For example, in a \(2^{5-1}\) with \(I = ABCDE\):
- \(A \leftrightarrow BCDE\)
- \(AB \leftrightarrow CDE\)
- \(ABC \leftrightarrow DE\)

### 2. Resolution

Resolution indicates the degree of aliasing:
- **Resolution III**: Main effects are not aliased with each other, but may be aliased with two-factor interactions
- **Resolution IV**: Main effects are not aliased with each other or with two-factor interactions; two-factor interactions may be aliased with each other
- **Resolution V**: Main effects and two-factor interactions are not aliased with each other

Higher resolution = less aliasing = more runs required.

### 3. Dealiasing Techniques

#### 3.1 Foldover Design
A foldover reverses the signs of one or more columns in the original design matrix and appends the new runs. This breaks specific alias chains.

**Types of foldover:**
- **Full foldover**: Reverse all signs → increases resolution by 1
- **Single-factor foldover**: Reverse one column → dealiases that factor's interactions
- **Partial foldover**: Reverse a subset of columns

#### 3.2 Optimal Follow-Up Designs
Instead of a full foldover, add runs optimally (e.g., D-optimal) to resolve specific ambiguities.

#### 3.3 Projection
If some factors are found inactive, the design projects into a full factorial in the remaining active factors, automatically dealiasing interactions among the active factors.

#### 3.4 Bayesian Model Selection
Use prior knowledge and the data to probabilistically assign effects to alias chains.

#### 3.5 All-Subsets Regression with Heredity
Screen alias chains using effect heredity principles (interactions are likely only if parent main effects are significant).

---

## Rules of Thumb

1. **Start with Resolution IV if possible** — it protects main effects from two-factor interaction aliasing, which is the most common source of confusion.

2. **Use foldover when you need to resolve a specific ambiguity** — if one or two alias chains are problematic, a targeted foldover is efficient.

3. **Use D-optimal augmentation when you need flexibility** — optimal designs can be tailored to resolve exactly the confounding you care about, minimizing extra runs.

4. **Check projection before augmenting** — if inactive factors exist, the design may already project to a higher-resolution subdesign.

5. **Apply effect heredity** — an interaction is unlikely to be significant if neither parent main effect is significant. Use this to break alias chains.

6. **Always examine the alias matrix** — before analyzing data, know exactly what is confounded with what.

7. **Sequential experimentation is your friend** — run a small fraction first, analyze, then augment strategically rather than running a large full factorial upfront.

8. **Resolution III designs should be followed by a foldover** — never interpret a Resolution III design without follow-up; main effects are hopelessly confounded with two-factor interactions.

9. **Use Bayesian methods when prior information exists** — if you have strong priors about which effects are likely, Bayesian dealiasing can resolve ambiguities with fewer runs.

10. **Document the alias structure** — always report the defining relation and alias chains in your analysis.

---

## Case Studies

### Case Study 1: Chemical Process Optimization (2^{5-1} → Foldover)

**Context**: A chemical plant wants to optimize yield by studying 5 factors: Temperature (A), Pressure (B), Catalyst (C), Stirring Rate (D), and Concentration (E). They run a \(2^{5-1}\) Resolution V design (16 runs).

**Initial Results**: Significant effects observed for A, B, and the alias chain AB + CDE.

**Problem**: Cannot tell if AB or CDE (or both) is real.

**Dealiasing Strategy**: Perform a full foldover (reverse all signs) adding 16 more runs. The combined 32-run design becomes a full \(2^5\) factorial, completely dealiasing all effects.

**Outcome**: AB is significant, CDE is negligible. The interaction between Temperature and Pressure is driving yield.

### Case Study 2: Semiconductor Etching (2^{7-4} → Sequential Augmentation)

**Context**: A semiconductor fab screens 7 factors in 8 runs using a \(2^{7-4}\) Resolution III design.

**Initial Results**: Factors A, C, and F appear significant. But A is confounded with BD + CE + FG.

**Problem**: Cannot distinguish A from the two-factor interaction alias chain.

**Dealiasing Strategy**: Instead of a full foldover (8 more runs), use a D-optimal augmentation adding only 4 runs specifically chosen to break the A alias chain.

**Outcome**: A is confirmed significant. The alias chain is resolved with minimal additional experimentation cost.

### Case Study 3: Pharmaceutical Tablet Formulation (2^{4-1} → Projection)

**Context**: A pharma company studies 4 factors: Binder type (A), Disintegrant (B), Lubricant (C), and Compression force (D) using a \(2^{4-1}\) design (8 runs).

**Initial Results**: Only A and B are significant. C and D show negligible effects.

**Dealiasing Strategy**: Since C and D are inactive, the design projects into a full \(2^2\) factorial in A and B. The AB interaction is now cleanly estimated without any aliasing.

**Outcome**: AB interaction is significant. The optimal formulation requires a specific combination of binder and disintegrant.

### Case Study 4: Automotive Coating (2^{6-2} → Partial Foldover)

**Context**: An automotive manufacturer studies 6 coating process factors in 16 runs (\(2^{6-2}\) Resolution IV).

**Initial Results**: Main effects A, B, C, D significant. Alias chain AB + CE + DF is significant.

**Problem**: Three two-factor interactions are aliased. Need to determine which is real.

**Dealiasing Strategy**: Perform a partial foldover reversing signs of factors A and B only. This changes the alias structure for the AB-related chain while preserving other estimates.

**Outcome**: AB is the significant interaction. CE and DF are noise.

### Case Study 5: Food Processing (2^{8-4} → Bayesian Dealiasing)

**Context**: A food company screens 8 factors in 16 runs (\(2^{8-4}\) Resolution IV).

**Initial Results**: Multiple ambiguous alias chains with significant contrast sums.

**Dealiasing Strategy**: Instead of physical augmentation, apply Bayesian model selection with strong priors (based on domain knowledge) that main effects are more likely than interactions, and interactions require parent main effects.

**Outcome**: Bayesian posterior probabilities clearly identify the active effects within each alias chain, avoiding the need for additional runs.

---

## Workflow

### Step-by-Step Dealiasing Workflow

```
┌─────────────────────────────────────────────────────────────┐
│  STEP 1: Run Initial Fractional Factorial Design            │
│  → Choose resolution based on budget and risk tolerance     │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 2: Analyze Main Effects and Identify Significant      │
│          Alias Chains                                       │
│  → Use normal probability plots, half-normal plots,         │
│    Lenth's method, or Bayesian methods                      │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 3: Examine Alias Structure                            │
│  → Write out defining relation                              │
│  → Identify which effects are confounded                    │
│  → Check for projection opportunities                       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 4: Choose Dealiasing Strategy                         │
│  ├─ If inactive factors exist → PROJECT                     │
│  ├─ If one factor ambiguous → SINGLE FOLDOVER               │
│  ├─ If many ambiguities → FULL FOLDOVER                     │
│  ├─ If budget constrained → D-OPTIMAL AUGMENTATION          │
│  └─ If strong priors exist → BAYESIAN DEALIASING            │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 5: Execute Follow-Up Experiment (if physical)         │
│  → Run additional runs                                      │
│  → Combine with original data                               │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 6: Re-analyze Combined Data                           │
│  → Fit full model or reduced model                          │
│  → Verify dealiasing success                                │
│  → Check residuals and model adequacy                       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 7: Report Results with Full Alias Disclosure          │
│  → Document original alias structure                        │
│  → Explain dealiasing method used                           │
│  → Present clean effect estimates                           │
└─────────────────────────────────────────────────────────────┘
```

---

## Common Pitfalls

### Pitfall 1: Ignoring the Alias Structure

**Problem**: Analysts run a fractional factorial and interpret effects as if they were from a full factorial.

**Consequence**: Significant "main effects" may actually be two-factor interactions, leading to wrong factor settings.

**Solution**: Always compute and report the defining relation and alias chains before interpreting results.

### Pitfall 2: Running a Resolution III Design Without Follow-Up

**Problem**: \(2^{k-p}\) Resolution III designs alias main effects with two-factor interactions. Interpreting main effects from such a design alone is unreliable.

**Consequence**: False positives and missed interactions.

**Solution**: Always follow a Resolution III design with a foldover or augmentation before drawing conclusions.

### Pitfall 3: Choosing the Wrong Foldover

**Problem**: A full foldover doubles the run size. A single-factor foldover may not resolve all ambiguities.

**Consequence**: Wasted runs or unresolved confounding.

**Solution**: Carefully plan which columns to fold over based on the specific alias chains you need to break.

### Pitfall 4: Overlooking Projection

**Problem**: Augmenting a design when inactive factors could simply be dropped.

**Consequence**: Unnecessary experimental runs.

**Solution**: Always check if the design projects to a higher-resolution design in the active factors before augmenting.

### Pitfall 5: Violating Effect Heredity

**Problem**: Claiming a two-factor interaction is significant when neither parent main effect is significant.

**Consequence**: Spurious findings that don't replicate.

**Solution**: Apply the strong heredity principle: interactions should only be considered if at least one parent main effect is significant.

### Pitfall 6: Inadequate Power in Follow-Up

**Problem**: Adding too few follow-up runs to resolve the ambiguity.

**Consequence**: Alias chains remain partially confounded.

**Solution**: Use power analysis or D-optimality criteria to determine the minimum number of additional runs needed.

---

## Comparisons

| Method | Run Increase | Best For | Pros | Cons |
|--------|-------------|----------|------|------|
| **Full Foldover** | 2× original | Resolving all ambiguities | Simple, increases resolution by 1 | Expensive, may be overkill |
| **Single-Factor Foldover** | 1× original | Dealiasing one factor's interactions | Targeted, efficient | Only resolves specific chains |
| **Partial Foldover** | Variable | Dealiasing selected chains | Flexible run size | Complex to design |
| **D-Optimal Augmentation** | Minimal | Budget-constrained follow-up | Most runs-efficient | Requires optimization software |
| **Projection** | 0 runs | Inactive factors present | Free dealiasing | Only works if factors are truly inactive |
| **Bayesian Dealiasing** | 0 runs | Strong prior knowledge | No additional runs needed | Depends on prior validity |
| **All-Subsets + Heredity** | 0 runs | Screening with many factors | Uses data structure | Can miss unexpected effects |

### When to Use What

- **Resolution III initial design** → Full foldover (mandatory)
- **Resolution IV initial design** → Single-factor foldover or D-optimal augmentation
- **Many inactive factors suspected** → Check projection first
- **Strong domain knowledge** → Bayesian dealiasing
- **Tight budget, specific ambiguity** → D-optimal augmentation
- **Multiple ambiguous chains** → Partial foldover or full foldover

---

## References

1. **Box, G.E.P., Hunter, J.S., & Hunter, W.G.** (2005). *Statistics for Experimenters: Design, Innovation, and Discovery* (2nd ed.). Wiley-Interscience. — Chapters on fractional factorials and foldover designs.

2. **Montgomery, D.C.** (2017). *Design and Analysis of Experiments* (10th ed.). Wiley. — Comprehensive coverage of alias structures, foldover, and follow-up designs.

3. **Wu, C.F.J. & Hamada, M.** (2009). *Experiments: Planning, Analysis, and Optimization* (2nd ed.). Wiley. — Advanced treatment of optimal follow-up designs and Bayesian methods.

4. **Mee, R.W.** (2009). *A Comprehensive Guide to Factorial Two-Level Experimentation*. Springer. — Detailed discussion of foldover and partial foldover strategies.

5. **Li, W. & Lin, D.K.J.** (2003). Optimal Foldover Plans for Two-Level Fractional Factorial Designs. *Technometrics*, 45(2), 142-149. — Foundational paper on optimal foldover selection.

6. **Meyer, R.D., Steinberg, D.M., & Box, G.** (1996). Follow-up Designs to Resolve Confounding in Multifactor Experiments. *Technometrics*, 38(4), 303-313. — Key paper on D-optimal follow-up designs.

7. **Chipman, H.** (1996). Bayesian Variable Selection with Related Predictors. *The Canadian Journal of Statistics*, 24(1), 17-36. — Bayesian approach to dealiasing in factorial designs.

8. **Ye, K.Q.** (2003). Indicator Function and Its Application in Two-Level Factorial Designs. *The Annals of Statistics*, 31(3), 984-994. — Mathematical foundation for alias structure analysis.

---

*Generated for DoE Lecture 13: Dealiasing Fractional Designs*

---

Absolutely. **Dealiasing** is one of the most important ideas in **fractional factorial designs**, because it tells you:

> **When you estimate an effect, which other effect(s) are mixed together with it?**

The easiest way to understand it is visually.

---

# 1. Start with a full (2^3) factorial

Suppose we have 3 factors:

* (A) = Temperature
* (B) = Pressure
* (C) = Time

A full (2^3) design has:

[
2^3=8\text{ runs}
]

Visually:

```text
                 C
              -     +
             /       \
            /         \
       B -             B +
          |             |
          |             |
       A -             A +
```

More concretely:

```text
       A     B     C
       ─────────────
       -     -     -
       +     -     -
       -     +     -
       +     +     -
       -     -     +
       +     -     +
       -     +     +
       +     +     +
```

Because we have **all 8 combinations**, every main effect and interaction can be estimated separately:

```text
A       → A
B       → B
C       → C

AB      → AB
AC      → AC
BC      → BC

ABC     → ABC
```

There is **no aliasing**.

---

# 2. What happens when we use a fraction?

Suppose 8 runs are too expensive.

We use only **half** of the (2^3) design:

[
2^{3-1}=4\text{ runs}
]

Let's choose the defining rule:

[
\boxed{C=AB}
]

This means we don't independently choose (C).

Instead:

[
C=A\times B
]

So:

```text
A     B     C=AB
────────────────
-     -      +
+     -      -
-     +      -
+     +      +
```

Only 4 runs!

---

# 3. Here's where aliasing appears

The defining equation is:

[
C=AB
]

Multiply both sides by (C):

[
C^2=ABC
]

Since:

[
C^2=1
]

we get:

[
\boxed{I=ABC}
]

This is called the **defining relation**.

Now we can discover the aliases.

---

# 4. The visual "alias machine"

Our defining relation is:

[
\boxed{I=ABC}
]

Think of it as an **alias generator**.

To find what is aliased with (A):

[
A(I)=A(ABC)
]

Therefore:

[
A=A^2BC
]

Since (A^2=I):

[
\boxed{A=BC}
]

So:

```text
A  ←────────→  BC
```

You cannot distinguish the effect of (A) from the effect of (BC).

---

## Find the alias for B

[
B(I)=B(ABC)
]

[
B=ABC^2
]

[
\boxed{B=AC}
]

Therefore:

```text
B  ←────────→  AC
```

---

## Find the alias for C

[
C(I)=C(ABC)
]

[
\boxed{C=AB}
]

Therefore:

```text
C  ←────────→  AB
```

---

# 5. The complete alias structure

For this design:

[
\boxed{I=ABC}
]

we get:

```text
MAIN EFFECTS          INTERACTIONS

A  ────────────────  BC

B  ────────────────  AC

C  ────────────────  AB
```

And:

```text
ABC ──────────────── I
```

So there are **4 alias groups**:

[
\boxed{I=ABC}
]

[
\boxed{A=BC}
]

[
\boxed{B=AC}
]

[
\boxed{C=AB}
]

---

# 6. Why does this happen?

This is the key intuition.

In the full (2^3) design, imagine:

```text
             FULL DESIGN

          8 experimental runs

       ┌───────────────────┐
       │                   │
       │  A can be seen    │
       │  independently    │
       │                   │
       │  BC can be seen   │
       │  independently    │
       │                   │
       └───────────────────┘
```

But when we take only half:

```text
             FRACTION

          4 experimental runs

       ┌───────────────────┐
       │                   │
       │   A and BC have   │
       │   exactly the     │
       │   same pattern    │
       │                   │
       └───────────────────┘
```

That's the essence of aliasing.

The columns representing (A) and (BC) become **identical**.

---

# 7. See it directly in the data

Look at our design:

| Run |  A |  B |  C | (BC) |
| --: | -: | -: | -: | ---: |
|   1 |  − |  − |  + |    − |
|   2 |  + |  − |  − |    + |
|   3 |  − |  + |  − |    + |
|   4 |  + |  + |  + |   +? |

Let's calculate carefully.

Using multiplication:

| Run |  A |  B | C=AB | BC |
| --: | -: | -: | ---: | -: |
|   1 |  − |  − |    + |  − |
|   2 |  + |  − |    − |  + |
|   3 |  − |  + |    − |  − |
|   4 |  + |  + |    + |  + |

Actually, let's use the standard ±1 coding consistently:

[
BC=B\times C
]

Since (C=AB):

[
BC=B(AB)
]

[
BC=A B^2
]

[
BC=A
]

Therefore:

[
\boxed{BC=A}
]

So the columns are literally identical:

```text
A       BC
────────────
-       -
+       +
-       -
+       +
```

That's why the experiment **cannot tell them apart**.

---

# 8. This is DEaliasing

Now suppose you run the experiment and estimate:

[
\hat{\beta}_A=10
]

Can you say:

> "A has an effect of 10"?

❌ Not necessarily.

Because:

[
A=BC
]

The experiment actually estimates the combined contribution:

[
\boxed{A+BC}
]

Conceptually:

```text
                  observed effect
                        │
                        ▼
                  ┌───────────┐
                  │     A     │
                  │     +     │
                  │    BC     │
                  └───────────┘
```

You don't know how much belongs to (A) and how much belongs to (BC).

This is **aliasing**.

---

# 9. So what does "dealiasing" mean?

**Dealiasing means designing or augmenting the experiment so that aliased effects can be separated.**

For example:

### Experiment 1

```text
A  ↔ BC
B  ↔ AC
C  ↔ AB
```

You don't know whether the observed effect is caused by:

```text
A
```

or:

```text
BC
```

---

### Add the complementary fraction

Run the **other 4 combinations**.

Now:

```text
FIRST FRACTION
A ↔ BC

        +

SECOND FRACTION
A ↔ -BC
```

The aliasing pattern changes.

Together:

```text
Fraction 1:     A =  BC

Fraction 2:     A = -BC
```

Now the two effects can be separated.

This process is called:

[
\boxed{\text{Foldover}}
]

and it is one of the major methods of **dealiasing**.

---

# 10. Visualize foldover

Imagine the original fraction:

```text
             FRACTION 1

              A = BC

       A       BC
       │       │
       ▼       ▼
       ────────
       Same column
```

Now perform a foldover:

```text
             FRACTION 2

              A = -BC

       A       BC
       │       │
       ▼       ▼
       ────────
      Opposite columns
```

Combine them:

```text
                 BOTH FRACTIONS

          Fraction 1    Fraction 2

A              +             +

BC             +             -

              ↓

        A and BC are
        now distinguishable
```

So:

[
\boxed{\text{Foldover} \rightarrow \text{Dealiasing}}
]

---

# 11. A very important distinction

Don't confuse:

### Aliasing

```text
A = BC
```

means:

> "These effects are confounded."

### Dealiasing

means:

> "We add information/design runs so we can distinguish them."

### Foldover

is:

> "A specific experimental strategy for doing that."

---

# 12. The bigger picture: Resolution

Dealiasing becomes especially important when choosing the **resolution** of a fractional factorial design.

For example:

### Resolution III

```text
A ↔ BC
```

Main effects are aliased with two-factor interactions.

Very dangerous if interactions are important.

---

### Resolution IV

Typically:

```text
A ↔ BCD
AB ↔ CD
```

Main effects are **not** aliased with two-factor interactions.

Better.

---

### Resolution V

Typically:

```text
A ↔ BCDE
AB ↔ CDE
```

Main effects are separated from two-factor interactions, and two-factor interactions are separated from other two-factor interactions.

Even better.

---

# 13. The visual hierarchy

Think of it like this:

```text
                 FULL 2^k
                    │
                    │ expensive
                    ▼
          ┌──────────────────┐
          │ FRACTIONAL 2^k   │
          └──────────────────┘
                    │
                    ▼
                ALIASING
                    │
          ┌─────────┴─────────┐
          │                   │
       A = BC              B = AC
          │                   │
          └─────────┬─────────┘
                    │
                    ▼
               "Can't tell
                them apart"
                    │
                    ▼
             ADD INFORMATION
                    │
          ┌─────────┴─────────┐
          │                   │
       Foldover        Additional runs
          │                   │
          └─────────┬─────────┘
                    ▼
                DEALIASING
                    │
                    ▼
             Effects separated
```

---

# 14. The one formula you should remember

For a fractional factorial design:

[
\boxed{\text{Defining relation} \rightarrow \text{Alias structure}}
]

For example:

[
C=AB
]

gives:

[
I=ABC
]

Then multiply any effect by (I=ABC).

```text
A × ABC = BC
B × ABC = AC
C × ABC = AB
AB × ABC = C
AC × ABC = B
BC × ABC = A
ABC × ABC = I
```

Therefore:

[
\boxed{
A=BC,\quad
B=AC,\quad
C=AB,\quad
I=ABC
}
]

That's the **alias structure**.

And **dealiasing** means collecting additional experimental information—often via **foldover**—to break these alias relationships.

---

### One-sentence intuition

> **Aliasing is like two people wearing the same name tag; dealiasing is giving them different name tags so you can tell who is who.**

