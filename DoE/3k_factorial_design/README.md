
Absolutely. **DoE Lecture 14: (3^k) Full Factorial Designs** is basically the extension of the (2^k) design you were studying—but instead of **2 levels per factor**, every factor has **3 levels**.

# 🎯 1. The big idea

In a factorial experiment, we change **several factors simultaneously** and observe their effects on a response (Y).

For a (2^k) design:

> Each factor → 2 levels

For a (3^k) design:

> Each factor → **3 levels**

So:

[
\boxed{3^k = \text{number of experimental runs}}
]

where (k) = number of factors.

---

# 🧩 2. Visual comparison: (2^k) vs (3^k)

Imagine we have **two factors**:

* Temperature (A)
* Pressure (B)

### (2^2) design

Each factor has:

[
Low,\ High
]

So we get:

```text
             Pressure B
              Low    High
             ┌───────┬───────┐
Temperature  │       │       │
A            │       │       │
 Low         │  (1)  │   b   │
             ├───────┼───────┤
 High        │   a   │  ab   │
             └───────┴───────┘
```

Total:

[
2^2=4
]

---

# 🌟 3. Now introduce 3 levels

For (3^2):

Temperature:

```text
A = Low
A = Medium
A = High
```

Pressure:

```text
B = Low
B = Medium
B = High
```

Now the experiment becomes:

```text
                 PRESSURE
              B₁      B₂      B₃
           ┌───────┬───────┬───────┐
        A₁ │   ●   │   ●   │   ●   │
           ├───────┼───────┼───────┤
        A₂ │   ●   │   ●   │   ●   │
           ├───────┼───────┼───────┤
        A₃ │   ●   │   ●   │   ●   │
           └───────┴───────┴───────┘
```

Therefore:

[
\boxed{3^2=9\text{ runs}}
]

Instead of 4 runs in (2^2).

---

# 📐 4. Why do we use 3 levels?

This is one of the **most important ideas**.

With 2 levels, you're essentially asking:

> "Does increasing (A) from Low → High change the response?"

But you don't know what happens **in between**.

With 3 levels:

```text
Response
  ↑
  │             ●
  │          ●     ●
  │       ●           ●
  │    ●
  │ ●
  └────────────────────→ A
     Low   Mid   High
```

You can detect **curvature**.

For example:

### Two-level experiment

```text
Y
│
│       ●
│
│
│ ●
└────────────── A
 Low          High
```

You conclude:

> Increasing A increases Y.

But maybe the real relationship is:

```text
Y
│       ●
│     /   \
│   /       \
│ ●           ●
└──────────────── A
 Low    Mid    High
```

That's **curvature**.

The 3-level design can detect it.

---

# 🔢 5. General formula

For (k) factors, each with 3 levels:

[
\boxed{N=3^k}
]

### Examples

| Factors | Runs |
| ------: | ---: |
|   (3^1) |    3 |
|   (3^2) |    9 |
|   (3^3) |   27 |
|   (3^4) |   81 |
|   (3^5) |  243 |
|   (3^6) |  729 |

Notice how quickly the experiment becomes expensive.

---

# 🧪 6. Example: manufacturing process

Suppose we're manufacturing a component.

We want to maximize:

[
Y=\text{strength}
]

We have 3 factors:

### Factor A — Temperature

```text
A₁ = 100°C
A₂ = 150°C
A₃ = 200°C
```

### Factor B — Pressure

```text
B₁ = 10 bar
B₂ = 20 bar
B₃ = 30 bar
```

### Factor C — Time

```text
C₁ = 5 min
C₂ = 10 min
C₃ = 15 min
```

This is:

[
3^3
]

Therefore:

[
\boxed{27\text{ experiments}}
]

---

# 🧊 7. Visualizing (3^3)

For (3^3), we have a **3 × 3 × 3 cube**.

Think of each factor as one dimension:

```text
                 C = Time
                    ↑
                   /|
                  / |
                 /  |
                ●---●
               /|  /|
              ●---● |
              | ●-|-●
              |/  |/
              ●---●
             /
            /
           →
       A = Temperature

       B = Pressure
       goes into the page
```

More conceptually:

```text
                 C
                 ↑
                 │
        ┌────────┼────────┐
       /│       /│       /│
      ●─┼──────●─┼──────● │
      │ ●──────│─●──────│ ●
      │/       │/       │/
      ●────────●────────● → A
       \       \       \
        \       \       \
         └───────┴───────→ B
```

There are:

[
3\times3\times3=27
]

points.

---

# 🧮 8. The design matrix

Let's create a (3^2) design.

Factors:

* (A)
* (B)

Levels:

[
-1,\quad0,\quad+1
]

where:

```text
-1 = Low
 0 = Center
+1 = High
```

The design matrix is:

| Run |  A |  B |
| --: | -: | -: |
|   1 | -1 | -1 |
|   2 | -1 |  0 |
|   3 | -1 | +1 |
|   4 |  0 | -1 |
|   5 |  0 |  0 |
|   6 |  0 | +1 |
|   7 | +1 | -1 |
|   8 | +1 |  0 |
|   9 | +1 | +1 |

Visually:

```text
B
↑

+1       ●       ●       ●

 0       ●       ●       ●

-1       ●       ●       ●

         -1      0      +1
                 → A
```

This is the fundamental geometry of (3^2).

---

# 🎯 9. Main effects

Suppose we obtain these average responses:

```text
             A

       Low    Mid    High

        50     70      90
```

Graphically:

```text
Y
↑
90                    ●
│
80
│
70             ●
│
60
│
50      ●
│
└────────────────────────→ A
       Low    Mid    High
```

That's approximately a **linear main effect**.

---

But imagine:

```text
             A

       Low    Mid    High

        50     90      55
```

Then:

```text
Y
↑
90             ●
│
80
│
70
│
60
│
50      ●              ●
│
└────────────────────────→ A
       Low    Mid    High
```

Now we clearly have **curvature**.

That's something a (2^k) design struggles to identify directly.

---

# 🔥 10. Linear + quadratic effects

This is the key statistical reason for the third level.

For each factor we can investigate:

### Linear effect

[
A_L
]

### Quadratic effect

[
A_Q
]

So instead of simply:

[
A
]

we can decompose the effect into:

[
\boxed{A=A_L+A_Q}
]

Conceptually:

```text
Effect of A
     │
     ├──────── Linear
     │
     └──────── Quadratic
```

---

# 📈 11. What does quadratic mean?

Suppose:

[
Y=50+20A-15A^2
]

The relationship is:

```text
Y
↑
│          ●
│        /   \
│      /       \
│    /           \
│  ●               ●
│
└────────────────────→ A
    -1      0      +1
```

The (A^2) term creates the curvature.

With three levels:

[
A=-1,0,+1
]

we can estimate:

[
\boxed{A}
]

and

[
\boxed{A^2}
]

---

# 🤝 12. Interactions

Now let's consider two factors.

Suppose:

* (A) = Temperature
* (B) = Pressure

The response might depend on their combination.

Mathematically:

[
Y=\beta_0+\beta_AA+\beta_BB+\beta_{AB}AB+\epsilon
]

The (AB) term is the interaction.

Visual idea:

```text
                    B
                    ↑

High B       ───────────────
            /
Medium B   ───────────────
          /
Low B    ────────────────
        └──────────────────→ A
```

If the lines are **parallel**:

```text
──────────────
──────────────
──────────────
```

then:

[
A\times B \approx 0
]

No strong interaction.

But if:

```text
───────────────
       ─────────────
             ───────
```

or the lines cross:

```text
\          /
 \        /
  \      /
   \    /
    \  /
     \/
     /\
    /  \
```

then:

[
\boxed{A\times B\neq0}
]

---

# 🧠 13. (3^2) can investigate more than (2^2)

Compare:

### (2^2)

```text
●────────●
│        │
│        │
●────────●
```

Only 4 combinations.

### (3^2)

```text
●────●────●
│    │    │
●────●────●
│    │    │
●────●────●
```

9 combinations.

The middle points are extremely useful because they allow us to see what happens **between the extremes**.

---

# 🧩 14. Model for a (3^2) factorial

For two factors:

[
\boxed{
Y=
\beta_0
+\beta_1A
+\beta_2B
+\beta_{12}AB
+\beta_{11}A^2
+\beta_{22}B^2
+\epsilon
}
]

Notice the new terms:

[
A^2,\quad B^2
]

These are the **quadratic effects**.

So the (3^2) design can estimate a second-order model.

---

# 🚀 15. Why (3^k) is useful for optimization

Imagine you're trying to find the best operating conditions.

Suppose:

```text
Temperature
Low     → weak
Medium  → VERY STRONG
High    → weak
```

Then:

```text
              ★
             / \
            /   \
           /     \
          /       \
─────────●─────────●──────
       Low   Mid   High
```

The optimum is somewhere around the middle.

A 2-level design could completely miss this.

A 3-level design gives you the first indication that:

[
\boxed{\text{The optimum may be inside the experimental region}}
]

---

# ⚠️ 16. But there's a problem: number of runs

The price we pay is:

[
3^k
]

For example:

```text
2 factors → 9
3 factors → 27
4 factors → 81
5 factors → 243
6 factors → 729
```

Compare that with (2^k):

```text
             2-level      3-level

2 factors       4            9
3 factors       8           27
4 factors      16           81
5 factors      32          243
6 factors      64          729
```

So (3^k) becomes expensive very quickly.

---

# 🧠 17. Connection to Response Surface Methodology

This is very important for your DoE roadmap.

Think of the progression as:

```text
                 DoE
                  │
        ┌─────────┴─────────┐
        │                   │
     2-level              3-level
      2^k                  3^k
        │                   │
        │             curvature
        │                   │
        └─────────┬─────────┘
                  ↓
        Response Surface
           Methodology
                  │
          ┌───────┴───────┐
          │               │
         CCD             Box-Behnken
```

The big conceptual progression is:

[
\boxed{
\text{Factor screening}
\rightarrow
\text{interaction}
\rightarrow
\text{curvature}
\rightarrow
\text{optimization}
}
]

---

# 📊 18. The most important visual to remember

If you remember only one picture from Lecture 14, remember this:

### (2^k)

```text
LOW ───────── HIGH

Only endpoints
```

### (3^k)

```text
LOW ───── MID ───── HIGH

Endpoints + center
```

Therefore:

```text
2-level factorial
       ↓
"Is the effect increasing/decreasing?"

3-level factorial
       ↓
"Is it increasing/decreasing?
 Is there curvature?
 Where might the optimum be?"
```

---

# 📝 19. Exam cheat sheet

| Concept                   | (3^k)     |
| ------------------------- | --------- |
| Number of factors         | (k)       |
| Levels/factor             | **3**     |
| Runs                      | (3^k)     |
| Typical coding            | (-1,0,+1) |
| Detects main effects      | ✅         |
| Detects interactions      | ✅         |
| Detects curvature         | ✅         |
| Quadratic effects         | ✅         |
| More expensive than (2^k) | ✅         |
| Useful for optimization   | ✅         |

### Core formula

[
\boxed{N=3^k}
]

### Two-factor design

[
\boxed{3^2=9}
]

### Three-factor design

[
\boxed{3^3=27}
]

### Second-order model

[
\boxed{
Y=\beta_0+
\sum\beta_iX_i+
\sum\beta_{ii}X_i^2+
\sum\beta_{ij}X_iX_j+\epsilon
}
]

The **big idea** is:

> **(2^k) tells you about direction and interactions; (3^k) adds enough information to see curvature.**

That connection becomes especially important when you move from **Factorial Designs → Response Surface Methodology → CCD/Box-Behnken → Optimization**.

---
Yes — but **a truth table is not the main tool for interpreting a (3^k) full factorial design**.

Think of the tools as a progression:

```text
                 3^k FULL FACTORIAL
                        │
          ┌─────────────┼─────────────┐
          ↓             ↓             ↓
    Design Matrix    ANOVA/Model    Visualization
          │             │             │
          ↓             ↓             ↓
    -1, 0, +1      Main effects    Interaction plots
                   Quadratic       Contour plots
                   Interaction     Surface plots
                        │
                        ↓
                 Optimization
```

## 1. First: Design Matrix

This is your fundamental tool.

For a (3^2) design:

| Run |  A |  B | Response |
| --: | -: | -: | -------: |
|   1 | -1 | -1 |    (Y_1) |
|   2 | -1 |  0 |    (Y_2) |
|   3 | -1 | +1 |    (Y_3) |
|   4 |  0 | -1 |    (Y_4) |
|   5 |  0 |  0 |    (Y_5) |
|   6 |  0 | +1 |    (Y_6) |
|   7 | +1 | -1 |    (Y_7) |
|   8 | +1 |  0 |    (Y_8) |
|   9 | +1 | +1 |    (Y_9) |

This is essentially your **truth table equivalent**, but I would call it a **factorial design matrix**, not a truth table.

---

# 2. Why a (3^k) design isn't really a truth-table problem

Truth tables are particularly natural for **two-level factors**:

```text
A B
0 0
0 1
1 0
1 1
```

because you're dealing with binary states.

For (3^k):

```text
A B

-1 -1
-1  0
-1 +1
 0 -1
 0  0
 0 +1
+1 -1
+1  0
+1 +1
```

It's better to think:

> **Cartesian product of factor levels**

rather than Boolean logic.

Mathematically:

[
{-1,0,+1}\times{-1,0,+1}
]

giving:

[
3\times3=9
]

combinations.

---

# 3. The real interpretation tool: ANOVA

After collecting your responses, you typically fit a model.

For (3^2):

[
Y =
\beta_0+
\beta_AA+
\beta_BB+
\beta_{AB}AB+
\beta_{AA}A^2+
\beta_{BB}B^2+
\epsilon
]

Then ANOVA helps answer:

### Is A important?

[
H_0:\beta_A=0
]

### Is B important?

[
H_0:\beta_B=0
]

### Is there interaction?

[
H_0:\beta_{AB}=0
]

### Is there curvature?

[
H_0:\beta_{AA}=0
]

and/or

[
H_0:\beta_{BB}=0
]

So:

```text
                  ANOVA
                    │
       ┌────────────┼────────────┐
       ↓            ↓            ↓
    Main A       Main B       A × B
       │            │            │
       └────────────┼────────────┘
                    ↓
                Quadratic
                A² , B²
```

---

# 4. Main Effects Plot

This is one of the first visual tools I'd use.

Suppose:

```text
Temperature

Low       50
Medium    80
High      55
```

You plot:

```text
Y
↑
90          ●
│         /   \
80       /     \
│
60
│
50  ●             ●
│
└────────────────────→ Temperature
    Low  Mid  High
```

Immediately you see:

> **There is curvature.**

That's one of the major reasons for using 3 levels.

---

# 5. Interaction Plot

For two factors:

```text
Temperature →

Pressure
High      ●───────╲
                   ╲
Medium    ●─────────●
             ╲
Low         ●───────╱
```

If lines are parallel:

```text
────────────
────────────
────────────
```

→ little/no interaction.

If they aren't parallel:

```text
──────────╲
───────────╲
────────────╲
```

→ interaction.

If they cross:

```text
╲       ╱
 ╲     ╱
  ╲   ╱
   ╲ ╱
   ╱ ╲
  ╱   ╲
```

→ potentially strong interaction.

---

# 6. Contour Plot ⭐

This becomes **very useful** with (3^2).

Suppose:

* X-axis = Temperature
* Y-axis = Pressure
* Color/contours = Strength

You might get:

```text
Pressure
   ↑
30 │       ╭────────╮
   │      ╱          ╲
20 │     │    ★       │
   │      ╲          ╱
10 │       ╰────────╯
   │
   └────────────────────→ Temperature
       100  150  200
```

The ★ is approximately the region where:

[
Y=\text{maximum}
]

This is where (3^k) starts becoming very useful for **optimization**.

---

# 7. Response Surface Plot

Same idea, but in 3D:

```text
             Y
             ↑
             │          /\
             │        /    \
             │      /   ★    \
             │_____/___________\____
                  A       B
```

You are essentially trying to visualize:

[
Y=f(A,B)
]

A (3^2) design gives you 9 experimental points from which you can begin estimating that surface.

---

# 8. Polynomial regression

This is another major tool.

For two factors:

[
Y=
\beta_0+
\beta_1A+
\beta_2B+
\beta_{12}AB+
\beta_{11}A^2+
\beta_{22}B^2
]

Then you can use:

* coefficient estimates
* p-values
* confidence intervals
* (R^2)
* adjusted (R^2)
* residual analysis
* lack-of-fit tests

to determine whether the model is appropriate.

---

# 9. Contrast analysis

This is actually a very nice connection to your **(2^k)** studies.

With 3 levels, you can decompose each factor into:

[
\boxed{\text{Linear contrast}}
]

and

[
\boxed{\text{Quadratic contrast}}
]

For levels:

[
-1,;0,;+1
]

the linear contrast is approximately:

[
L=(-1)Y_{-1}+0Y_0+(+1)Y_{+1}
]

while the quadratic contrast is:

[
Q=Y_{-1}-2Y_0+Y_{+1}
]

So visually:

```text
3 levels
  │
  ├── Linear
  │     "Does Y trend upward/downward?"
  │
  └── Quadratic
        "Does Y bend?"
```

This is a **very important interpretation technique**.

---

# 10. What software can you use?

You can do essentially the entire workflow in:

### Python

```text
Python
 │
 ├── pandas
 ├── numpy
 ├── scipy
 ├── statsmodels
 ├── matplotlib
 └── seaborn
```

For example:

```python
import statsmodels.formula.api as smf

model = smf.ols(
    "Y ~ A + B + A:B + I(A**2) + I(B**2)",
    data=df
).fit()

print(model.summary())
```

Then visualize with:

```text
matplotlib
      ↓
main effects
interaction plots
contours
3D response surfaces
residual plots
```

---

# 11. Minitab / JMP / R

For industrial DoE, specialized software is extremely useful.

### Minitab

Very strong for:

```text
Design
  ↓
Factorial analysis
  ↓
ANOVA
  ↓
Main effects
  ↓
Interaction
  ↓
Contour
  ↓
Response optimization
```

### JMP

Especially strong for:

```text
Interactive visualization
       +
Response surface
       +
Optimization
```

### R

You can use packages such as:

```text
FrF2
DoE.base
rsm
```

---

# 12. The complete (3^k) workflow

This is the workflow I'd recommend you memorize:

```text
                 Define Factors
                       ↓
                Choose 3 Levels
                       ↓
                  3^k Design
                       ↓
                Design Matrix
                       ↓
                 Run Experiment
                       ↓
                 Collect Y
                       ↓
              ┌────────┴────────┐
              ↓                 ↓
           Visualize          ANOVA
              │                 │
       ┌──────┼──────┐          │
       ↓      ↓      ↓          ↓
     Main   Inter-  Contour   Linear
    Effects action   /Surface Quadratic
                              Interaction
                                   │
                                   ↓
                              Fit Model
                                   │
                                   ↓
                              Optimization
```

## 🧠 So, where does "truth table" fit?

I'd make this distinction:

| Tool                  | (2^k) | (3^k) |
| --------------------- | ----: | ----: |
| Design matrix         |   ⭐⭐⭐ |   ⭐⭐⭐ |
| Truth table           |   ⭐⭐⭐ |     ⭐ |
| ANOVA                 |   ⭐⭐⭐ |   ⭐⭐⭐ |
| Main effects plot     |   ⭐⭐⭐ |   ⭐⭐⭐ |
| Interaction plot      |   ⭐⭐⭐ |   ⭐⭐⭐ |
| Linear contrast       |   ⭐⭐⭐ |   ⭐⭐⭐ |
| Quadratic contrast    |     ❌ |   ⭐⭐⭐ |
| Contour plot          |     ⭐ |   ⭐⭐⭐ |
| Response surface      |     ⭐ |   ⭐⭐⭐ |
| Polynomial regression |    ⭐⭐ |   ⭐⭐⭐ |
| Optimization          |    ⭐⭐ |   ⭐⭐⭐ |

### The key conceptual difference

```text
2^k
 │
 ├── Design matrix
 ├── ANOVA
 ├── Main effects
 └── Interactions

3^k
 │
 ├── Everything above
 │
 ├── Linear contrast
 ├── Quadratic contrast
 ├── Curvature
 ├── Response surface
 └── Optimization
```

So **don't approach (3^k) as a bigger truth table**. Approach it as a **factorial design that gives you enough information to study main effects + interactions + curvature**.
---
Yes. The easiest way to understand **where (3^k) full factorial designs are used** is to think:

> **“I have several factors, and I suspect the response may not change linearly—I want to study low/medium/high settings and possibly find a good operating region.”**

## 1. Manufacturing & Process Engineering ⭐

One of the most natural applications.

Imagine optimizing a manufacturing process:

```text
Temperature:  100 ─ 150 ─ 200 °C
Pressure:      10 ─  20 ─  30 bar
Time:           5 ─  10 ─  15 min
```

You measure:

[
Y=\text{product strength}
]

A (3^3) design requires:

[
3^3=27\text{ runs}
]

You can discover:

```text
Temperature
     ↓
Low ─── Medium ─── High
             ↑
          optimum?
```

Useful for:

* machining
* welding
* injection molding
* heat treatment
* chemical processing
* manufacturing quality

---

# 2. Chemical & Pharmaceutical Experiments 🧪

Suppose you're developing a chemical reaction.

Factors:

```text
A = Temperature
B = Catalyst concentration
C = Reaction time
```

Each has:

```text
Low ─ Medium ─ High
```

Response:

[
Y=\text{reaction yield}
]

You might discover:

```text
Yield
 ↑
 │          ★
 │        /   \
 │      /       \
 │____/___________\____
       Factor level
```

The reaction may have an **optimal middle region**, rather than:

> "Higher temperature is always better."

This is particularly important in:

* pharmaceutical formulation
* chemical synthesis
* material processing
* reaction optimization

---

# 3. Agriculture 🌱

Suppose you're studying crop yield.

Factors:

```text
A = Fertilizer
B = Irrigation
C = Plant density
```

Each has three levels:

```text
Fertilizer:
Low ─ Medium ─ High

Water:
Low ─ Medium ─ High

Density:
Low ─ Medium ─ High
```

Response:

[
Y=\text{crop yield}
]

You may find:

```text
Too little fertilizer → low yield
Optimal fertilizer    → high yield
Too much fertilizer   → lower yield
```

That's exactly the type of **curvature** that 3-level experiments can reveal.

---

# 4. Food & Beverage Industry 🍞

Very common optimization problem.

Suppose you're developing bread.

Factors:

```text
A = Baking temperature
B = Baking time
C = Water percentage
```

Response:

[
Y=\text{taste / texture / volume}
]

You might discover:

```text
                    ★
                   / \
                  /   \
                 /     \
──────────────────────────
 Low          Medium       High
```

Applications include:

* baking
* brewing
* coffee processing
* food formulation
* fermentation
* cooking processes

---

# 5. Materials Engineering 🔩

Suppose you're developing a stronger material.

Factors:

```text
A = Temperature
B = Pressure
C = Composition
```

Response:

[
Y=\text{strength}
]

You can investigate:

[
A,\quad B,\quad C
]

plus:

[
A^2,\quad B^2,\quad C^2
]

and interactions:

[
AB,\quad AC,\quad BC
]

This helps determine whether:

> increasing temperature always improves strength

or:

> strength increases until an optimum and then decreases.

---

# 6. Electronics & Engineering ⚡

Example: optimizing a circuit.

Factors:

```text
A = Voltage
B = Frequency
C = Resistance
```

Response:

[
Y=\text{signal quality}
]

You could test:

```text
Voltage
Low ─ Medium ─ High

Frequency
Low ─ Medium ─ High

Resistance
Low ─ Medium ─ High
```

and determine the combination producing the best performance.

Applications:

* circuit design
* sensors
* batteries
* power electronics
* communication systems
* semiconductor processing

---

# 7. Computer Science / Machine Learning 🤖

This is particularly relevant to you.

You can use the same experimental-design concept for **hyperparameter experiments**.

For example:

```text
Learning rate:
0.001 ─ 0.01 ─ 0.1

Batch size:
16 ─ 32 ─ 64

Dropout:
0.1 ─ 0.3 ─ 0.5
```

That's:

[
3^3=27
]

experiments.

Response:

[
Y=\text{validation accuracy}
]

You can investigate:

```text
Learning rate × Batch size
Learning rate × Dropout
Batch size × Dropout
```

and potentially identify curvature.

### But an important caveat

In modern ML, we don't usually call a hyperparameter grid search a **(3^k) factorial experiment** unless we're deliberately applying experimental-design principles.

Grid search:

```text
Try everything
     ↓
Pick best
```

DoE:

```text
Systematically vary factors
     ↓
Estimate effects
     ↓
Estimate interactions
     ↓
Estimate curvature
     ↓
Build model
     ↓
Optimize
```

That's a very important distinction.

---

# 8. Software Performance Engineering 💻

You could study how a system performs under different configurations.

Factors:

```text
A = Number of workers
B = Cache size
C = Batch size
```

Three levels each.

Response:

[
Y=\text{throughput}
]

or:

[
Y=\text{latency}
]

or:

[
Y=\text{CPU utilization}
]

For example:

```text
             Throughput
                  ↑
                  │       ★
                  │     /   \
                  │   /       \
                  │__/_________\__
                    Configuration
```

This is useful for:

* databases
* APIs
* distributed systems
* cloud infrastructure
* ML pipelines
* server optimization

---

# 9. Environmental Engineering 🌍

Example:

```text
A = pH
B = Temperature
C = Treatment concentration
```

Response:

[
Y=\text{pollutant removal efficiency}
]

You might discover:

```text
Removal %
 ↑
 │             ★
 │           /   \
 │         /       \
 │_______/___________\____
```

Applications:

* wastewater treatment
* air pollution
* water purification
* environmental remediation

---

# 10. Human Factors / Psychology

You can also use factorial designs with controlled experimental factors.

For example:

```text
A = Interface complexity
B = Notification frequency
C = Task difficulty
```

Response:

[
Y=\text{task completion time}
]

or:

[
Y=\text{error rate}
]

You can determine whether factors interact.

For example:

> Notifications might be harmless for easy tasks but dramatically increase errors for difficult tasks.

That's an **interaction**.

---

# 11. Agriculture / Biology / Life Sciences

Another important application.

Suppose:

```text
A = Temperature
B = Nutrient concentration
C = Light intensity
```

Response:

[
Y=\text{growth rate}
]

The organism might have an optimal middle temperature:

```text
Growth
 ↑
 │         ★
 │       /   \
 │     /       \
 │   /           \
 └──────────────────→ Temperature
    Low  Mid  High
```

Again, the 3 levels help reveal this curvature.

---

# 12. When should you actually choose (3^k)?

A useful decision rule:

```text
                 Do you have k factors?
                         │
                         ↓
                ┌─────────────────┐
                │ Need only low/  │
                │ high comparison?│
                └───────┬─────────┘
                        │
              YES ──────┴────── NO
               ↓                 ↓
             2^k          Suspect curvature?
                               │
                         YES ──┴── NO
                          ↓         ↓
                        3^k       2^k
```

More specifically, (3^k) is attractive when:

### ✅ You suspect curvature

```text
Low → Medium → High
```

may reveal:

[
\cap \quad\text{or}\quad \cup
]

### ✅ You want to explore an optimum

You don't just want to know:

> "Does A matter?"

You want:

> "Where is the best operating region?"

### ✅ Factors naturally have three meaningful settings

For example:

```text
Low
Recommended
High
```

### ✅ You need linear + quadratic information

[
X,\quad X^2
]

---

# 13. But (3^k) is NOT always the best choice

This is important.

If you have:

```text
6 factors
```

then:

[
3^6=729
]

runs.

That's expensive.

You might instead do:

```text
Screening
   ↓
2-level factorial
   ↓
Find important factors
   ↓
Response Surface Methodology
   ↓
CCD / Box-Behnken
   ↓
Optimization
```

This is often much more efficient.

---

# 🧠 The bigger picture

Don't think of (3^k) as an isolated technique.

Think of it inside the **DoE strategy**:

```text
                    EXPERIMENT
                        │
                        ↓
                Many possible factors
                        │
                        ↓
                  2^k Screening
                        │
                  Important factors
                        │
                        ↓
              ┌───────────────────┐
              │ Is curvature       │
              │ important?         │
              └─────────┬─────────┘
                        ↓
                      YES
                        │
                        ↓
                3-level / RSM
                        │
              ┌─────────┴─────────┐
              ↓                   ↓
             CCD             Box-Behnken
              │                   │
              └─────────┬─────────┘
                        ↓
                   Optimization
```

### In one sentence:

[
\boxed{\text{(3^k) is mainly useful when you want to study three-level factor behavior,}}
]

[
\boxed{\text{including curvature and interactions, and potentially locate an optimum.}}
]

For your **DoE learning path**, I would especially connect Lecture 14 to **(3^k) → quadratic models → response surfaces → CCD → Box-Behnken → optimization**, because that's where the concepts really start fitting together.

---
---

> **Design of Experiments — Lecture 14**  
> *Three-Level Full Factorial Designs: Detecting Curvature, Modeling Quadratic Effects, and Optimizing Nonlinear Processes*

---

## Table of Contents

1. [Overview](#1-overview)
2. [Core Concepts](#2-core-concepts)
3. [Mathematical Foundation](#3-mathematical-foundation)
4. [Rules of Thumb](#4-rules-of-thumb)
5. [Workflow](#5-workflow)
6. [Five Case Studies](#6-five-case-studies)
7. [Pitfalls & Common Mistakes](#7-pitfalls--common-mistakes)
8. [Comparisons with Other Designs](#8-comparisons-with-other-designs)
9. [Advanced Topics](#9-advanced-topics)
10. [References](#10-references)

---

## 1. Overview

### What is a 3^k Full Factorial Design?

A **3^k full factorial design** is an experimental design in which **k factors** are each studied at **three levels**: low, center, and high. The design includes **all possible combinations** of these levels, resulting in **3^k treatment combinations** (runs).

| Design Notation | Factors (k) | Levels per Factor | Total Runs | Purpose |
|----------------|-------------|-------------------|------------|---------|
| 3² | 2 | 3 | 9 | Detect curvature in two factors |
| 3³ | 3 | 3 | 27 | Full quadratic modeling |
| 3⁴ | 4 | 3 | 81 | Complex process optimization |
| 3⁵ | 5 | 3 | 243 | High-dimensional exploration |

### Why Three Levels?

Unlike 2^k designs (which only test low and high levels), 3^k designs add a **center level** that enables:

1. **Detection of curvature (quadratic effects)** — The response may peak or valley within the experimental region, not just at the boundaries.
2. **Estimation of pure quadratic terms** — Terms like βᵢᵢxᵢ² can be fitted.
3. **More accurate response surface modeling** — Essential for process optimization where the optimum lies inside the factor space.
4. **Better interpolation** — Predictions between factor levels are more reliable.

### When to Use 3^k vs. 2^k

| Scenario | Recommended Design |
|---------|-------------------|
| Screening many factors (k > 5) | 2^k or 2^(k-p) fractional |
| Known or suspected curvature | 3^k or 2^k + center points |
| Process optimization (RSM) | 3^k, CCD, or Box-Behnken |
| Small k (2–4) with complex response | 3^k full factorial |
| Limited budget | 2^k with center points |

---

## 2. Core Concepts

### 2.1 Factor Levels

Each factor is set at three distinct levels, typically coded as:

| Coded Level | Natural Level | Interpretation |
|------------|---------------|----------------|
| -1 | Low (L) | Lower bound of experimental range |
| 0 | Center (C) | Midpoint of experimental range |
| +1 | High (H) | Upper bound of experimental range |

> **Note:** The coding scheme uses {0, 1, 2} in some literature (especially in the context of confounding and orthogonal arrays), but {-1, 0, +1} is more common for regression analysis and response surface methodology.

### 2.2 The 3² Design (Simplest Case)

For two factors A and B, the 9 treatment combinations are:

| Run | A | B | Notation |
|-----|---|---|----------|
| 1 | -1 | -1 | a₀b₀ (or "00") |
| 2 | -1 | 0 | a₀b₁ (or "01") |
| 3 | -1 | +1 | a₀b₂ (or "02") |
| 4 | 0 | -1 | a₁b₀ (or "10") |
| 5 | 0 | 0 | a₁b₁ (or "11") |
| 6 | 0 | +1 | a₁b₂ (or "12") |
| 7 | +1 | -1 | a₂b₀ (or "20") |
| 8 | +1 | 0 | a₂b₁ (or "21") |
| 9 | +1 | +1 | a₂b₂ (or "22") |

### 2.3 The 3³ Design

For three factors, the design has 27 runs. These can be visualized as a 3×3×3 cube with points at all vertices, edge centers, face centers, and the body center.

### 2.4 Main Effects in 3^k Designs

The **main effect** of a factor is the change in the average response as the factor moves from low to center to high, averaged over all other factors.

For factor A with levels {-1, 0, +1}:

```
Effect_A(-1) = Average response at A = -1
Effect_A(0)  = Average response at A = 0
Effect_A(+1) = Average response at A = +1
```

The **linear effect** is: (Effect(+1) - Effect(-1)) / 2
The **quadratic effect** is: (Effect(+1) - 2·Effect(0) + Effect(-1)) / 2

### 2.5 Two-Factor Interactions

In 3^k designs, the interaction between two factors A and B is assessed using a **3×3 table** of mean responses:

```
        B=-1    B=0     B=+1
A=-1    μ₁₁     μ₁₂     μ₁₃
A=0     μ₂₁     μ₂₂     μ₂₃
A=+1    μ₃₁     μ₃₂     μ₃₃
```

If the rows are not parallel (when plotted), an interaction exists. Unlike 2^k designs where interactions are single numbers, 3^k interactions have **4 degrees of freedom** (df = (3-1)×(3-1) = 4).

### 2.6 Interaction Components (Advanced)

For 3^k designs, the A×B interaction can be partitioned into two **orthogonal components**:
- **AB component**: Uses linear × linear contrast
- **AB² component**: Uses linear × quadratic contrast

These are useful for blocking and fractional factorial construction.

### 2.7 Quadratic (Curvature) Effects

The defining advantage of 3^k designs. A full quadratic model for k factors includes:

```
y = β₀ + Σ βᵢxᵢ + Σ βᵢᵢxᵢ² + Σ Σ βᵢⱼxᵢxⱼ + ε
```

Where:
- βᵢ = linear coefficients
- βᵢᵢ = pure quadratic (curvature) coefficients
- βᵢⱼ = two-factor interaction coefficients

---

## 3. Mathematical Foundation

### 3.1 Model Specification

For a 3^k design with k factors, the full second-order (quadratic) model is:

```
y = β₀ + Σᵢ βᵢxᵢ + Σᵢ βᵢᵢxᵢ² + Σᵢ<ⱼ βᵢⱼxᵢxⱼ + ε
```

**Number of parameters:**
- 1 intercept
- k linear terms
- k quadratic terms
- k(k-1)/2 two-factor interaction terms
- **Total: 1 + 2k + k(k-1)/2**

| k | Linear Only | Full Quadratic |
|---|-------------|----------------|
| 2 | 3 | 6 |
| 3 | 4 | 10 |
| 4 | 5 | 15 |
| 5 | 6 | 21 |

### 3.2 ANOVA for 3^k Designs

The ANOVA table partitions the total variation:

| Source | df | SS | MS | F |
|--------|----|----|----|---|
| A | 2 | SSA | MSA | MSA/MSE |
| B | 2 | SSB | MSB | MSB/MSE |
| ... | ... | ... | ... | ... |
| A×B | 4 | SSAB | MSAB | MSAB/MSE |
| A×B×C | 8 | SSABC | MSABC | MSABC/MSE |
| Error | N - 3^k | SSE | MSE | — |
| Total | N - 1 | SST | — | — |

Where:
- df for main effect = 3 - 1 = **2**
- df for two-factor interaction = (3-1)(3-1) = **4**
- df for three-factor interaction = (3-1)³ = **8**
- N = total number of observations (including replicates)

### 3.3 Coding of Factor Levels

**Standard coding (-1, 0, +1):**

```python
x_coded = (x_natural - x_center) / ((x_high - x_low) / 2)
```

**Alternative coding (0, 1, 2):**

Used in some contexts (e.g., confounding, Taguchi methods):

```python
x_alt = (x_coded + 1)  # Maps -1→0, 0→1, +1→2
```

### 3.4 Confounding in 3^k Designs

For blocking, 3^k designs can be confounded into 3^p blocks. The general rule:

```
L = (a₁x₁ + a₂x₂ + ... + aₖxₖ) mod 3
```

Where aᵢ are coefficients (0, 1, or 2) and xᵢ are factor levels in {0, 1, 2} coding. Runs with the same L value go into the same block.

### 3.5 Fractional Factorial: 3^(k-p)

When the full 3^k is too large, a 1/3^p fraction can be used:

| Design | Fraction | Runs |
|--------|----------|------|
| 3^(3-1) | 1/3 | 9 |
| 3^(4-1) | 1/3 | 27 |
| 3^(4-2) | 1/9 | 9 |
| 3^(5-2) | 1/9 | 27 |

Resolution III designs confound main effects with two-factor interactions. Resolution IV designs do not.

---

## 4. Rules of Thumb

### 4.1 Design Selection

1. **Use 3^k when you need to model curvature.** If linearity is assumed, 2^k is more efficient.
2. **For k ≤ 3, full 3^k is practical.** For k = 4, consider whether 81 runs are feasible.
3. **For k ≥ 4, consider alternatives:**
   - 2^k with added center points (detect curvature with fewer runs)
   - Central Composite Design (CCD)
   - Box-Behnken Design
   - 3^(k-p) fractional factorial

### 4.2 Replication Strategy

| Situation | Replicates |
|-----------|-----------|
| Unreplicated (no pure error estimate) | Use half-normal plots, Lenth's method |
| Preliminary study | 1 replicate + center points |
| Confirmatory study | 2–3 replicates |
| High variability process | 3+ replicates |

### 4.3 Sample Size Guidelines

- **Minimum for ANOVA:** At least 2 replicates to estimate pure error
- **For model validation:** Reserve 10–20% of runs for validation
- **Power analysis:** For detecting medium effects (f = 0.25) with α = 0.05 and power = 0.80, typically need n ≥ 20 per cell

### 4.4 Factor Level Spacing

1. **Choose levels wide enough** to detect effects but not so wide that the process becomes unstable.
2. **Center points should be the current operating conditions** if optimizing an existing process.
3. **Equal spacing** (-1, 0, +1) is standard but not required.

### 4.5 Randomization

- **Always randomize run order** to protect against time trends and nuisance variables.
- If blocking is necessary, use the confounding rules for 3^k designs.

### 4.6 Model Building

1. Start with the **full quadratic model**.
2. Use **backward elimination** or **AIC/BIC** to remove non-significant terms.
3. Check **lack-of-fit** using pure error from replicates.
4. Validate with **residual analysis** (normality, homoscedasticity, independence).

---

## 5. Workflow

### Step-by-Step Implementation Guide

```
┌─────────────────────────────────────────────────────────────────┐
│  STEP 1: Define Objective & Response Variable                   │
│  ├── What are you trying to optimize?                           │
│  └── Is the response continuous, binary, or count?              │
├─────────────────────────────────────────────────────────────────┤
│  STEP 2: Identify Factors & Select Levels                       │
│  ├── Brainstorm potential factors (Ishikawa, FMEA)              │
│  ├── Narrow to 2–5 critical factors                             │
│  └── Define Low (-1), Center (0), High (+1) levels              │
├─────────────────────────────────────────────────────────────────┤
│  STEP 3: Choose Design & Calculate Runs                         │
│  ├── Full 3^k: 3^k × r runs (r = replicates)                  │
│  ├── Consider fractional if 3^k is too large                    │
│  └── Add center points if using 2^k as alternative              │
├─────────────────────────────────────────────────────────────────┤
│  STEP 4: Randomize & Conduct Experiments                          │
│  ├── Generate design matrix with all combinations               │
│  ├── Randomize run order                                        │
│  └── Execute experiments, record responses                      │
├─────────────────────────────────────────────────────────────────┤
│  STEP 5: Analyze Data                                             │
│  ├── Compute main effects (low, center, high)                   │
│  ├── Compute two-factor interactions                            │
│  ├── Fit full quadratic polynomial model                          │
│  ├── Perform ANOVA                                              │
│  └── Assess model fit (R², adjusted R², prediction R²)          │
├─────────────────────────────────────────────────────────────────┤
│  STEP 6: Visualize Results                                        │
│  ├── Main effects plots (check for curvature)                     │
│  ├── Interaction plots (check for non-parallelism)                │
│  ├── 3D response surface plots                                    │
│  ├── Contour plots for optimization                               │
│  └── Residual diagnostic plots                                    │
├─────────────────────────────────────────────────────────────────┤
│  STEP 7: Optimize & Validate                                      │
│  ├── Use regression model to find optimal factor settings       │
│  ├── Verify predictions with confirmation runs                    │
│  └── Document and implement optimal settings                      │
└─────────────────────────────────────────────────────────────────┘
```

### Analysis Checklist

- [ ] Check for significant main effects (p < 0.05)
- [ ] Check for significant interactions
- [ ] Check for significant quadratic terms (curvature)
- [ ] Verify model assumptions (normality, constant variance)
- [ ] Check for outliers and influential points
- [ ] Assess lack-of-fit if replicates exist
- [ ] Validate model with confirmation experiments

---

## 6. Five Case Studies

### Case Study 1: Cookie Baking Optimization (3² Design)

**Context:** A bakery wants to optimize cookie crispness.

| Factor | Low (-1) | Center (0) | High (+1) |
|--------|----------|------------|-----------|
| Temperature (°C) | 160 | 175 | 190 |
| Baking Time (min) | 10 | 13 | 16 |

**Response:** Crispness score (1–10 scale)

**Key Findings:**
- Temperature shows strong quadratic effect (optimum around 175–190°C)
- Time shows moderate linear effect with slight curvature
- Temperature × Time interaction is significant
- Optimal settings: ~185°C, ~13–14 minutes

**Visualizations:** Main effects plot, interaction plot, 3D response surface, Pareto chart, residual analysis

---

### Case Study 2: Chemical Reaction Yield (3³ Design)

**Context:** A chemical plant wants to maximize reaction yield.

| Factor | Low (-1) | Center (0) | High (+1) |
|--------|----------|------------|-----------|
| Temperature (°C) | 150 | 175 | 200 |
| Pressure (atm) | 2 | 3 | 4 |
| Catalyst (%) | 1 | 2 | 3 |

**Response:** Yield (%)

**Key Findings:**
- All three main effects are significant
- Quadratic effects in Pressure and Catalyst are significant
- Temperature × Pressure interaction is present
- Three-way interaction is weak
- Optimal yield: ~92% at T=190°C, P=3.5 atm, C=2.5%

**Visualizations:** Main effects, interaction plots, cube plot, Pareto chart, ANOVA bar chart, residuals

---

### Case Study 3: Welding Process Optimization (3² with Replicates)

**Context:** Optimize weld tensile strength.

| Factor | Low (-1) | Center (0) | High (+1) |
|--------|----------|------------|-----------|
| Current (A) | 100 | 120 | 140 |
| Travel Speed (mm/s) | 5 | 8 | 11 |

**Response:** Tensile Strength (MPa)

**Replicates:** 3 per treatment combination (54 total runs)

**Key Findings:**
- Current has strong negative quadratic effect (strength peaks then drops)
- Speed has moderate linear negative effect
- No significant interaction
- Pure error estimated from replicates enables proper F-tests
- Optimal: ~125A, ~6 mm/s

**Visualizations:** Main effects with error bars, interaction plots, response surface, Pareto, residuals

---

### Case Study 4: Pharmaceutical Tablet Dissolution (3³ Design)

**Context:** Optimize tablet dissolution rate.

| Factor | Low (-1) | Center (0) | High (+1) |
|--------|----------|------------|-----------|
| Binder (%) | 2 | 4 | 6 |
| Compression Force (kN) | 5 | 10 | 15 |
| Lubricant (%) | 0.5 | 1.0 | 1.5 |

**Response:** Dissolution Rate (% at 30 min)

**Key Findings:**
- Binder and Compression Force reduce dissolution (negative linear effects)
- Lubricant increases dissolution (positive linear effect)
- Quadratic effects in Binder and Lubricant are significant
- Binder × Lubricant interaction is significant
- Target: >85% dissolution achieved at Binder=2%, Force=5kN, Lubricant=1.5%

**Visualizations:** Main effects, interactions, cube plot, Pareto, ANOVA, residuals

---

### Case Study 5: Semiconductor Etching Rate (3⁴ Design)

**Context:** Optimize plasma etching rate in semiconductor manufacturing.

| Factor | Low (-1) | Center (0) | High (+1) |
|--------|----------|------------|-----------|
| RF Power (W) | 100 | 150 | 200 |
| Gas Flow (sccm) | 50 | 100 | 150 |
| Pressure (mTorr) | 10 | 20 | 30 |
| Temperature (°C) | 25 | 50 | 75 |

**Response:** Etch Rate (nm/min)

**Key Findings:**
- 81 runs (unreplicated) — large but manageable with automation
- RF Power and Gas Flow are the dominant factors
- Pressure has strong negative quadratic effect
- Several two-factor interactions are significant
- Half-normal plot used to identify significant effects (no pure error)
- Optimal etch rate: ~280 nm/min at P=180W, G=120sccm, Pr=15mTorr, T=60°C

**Visualizations:** Main effects, interactions, Pareto, half-normal plot, residuals

---

## 7. Pitfalls & Common Mistakes

### 7.1 Design Pitfalls

| Mistake | Why It\'s Wrong | How to Fix |
|---------|----------------|------------|
| **Using 3^k for screening** | Too many runs for exploratory phase | Use 2^k or Plackett-Burman first |
| **Unequal level spacing** | Distorts quadratic effect estimation | Use equal spacing unless justified |
| **Ignoring run order** | Time trends confound with factor effects | Always randomize |
| **Too few replicates** | Cannot estimate pure error | Minimum 2 replicates for ANOVA |
| **Extrapolating beyond design space** | Model may not hold outside tested range | Stay within [-1, +1] for predictions |

### 7.2 Analysis Pitfalls

| Mistake | Why It\'s Wrong | How to Fix |
|---------|----------------|------------|
| **Fitting only linear model** | Misses curvature that 3^k is designed to detect | Always include quadratic terms |
| **Ignoring lack-of-fit** | Model may be inadequate | Test LOF against pure error |
| **Overfitting with high k** | Too many parameters for limited data | Use AIC/BIC; consider fractional designs |
| **Not checking residuals** | Assumptions may be violated | Always do residual diagnostics |
| **Interpreting non-significant interactions** | Type I error inflation | Use Bonferroni or FDR correction |

### 7.3 Interpretation Pitfalls

| Mistake | Why It\'s Wrong | How to Fix |
|---------|----------------|------------|
| **Assuming optimum at center** | Optimum may be at edge or outside | Use optimization (e.g., gradient descent) |
| **Ignoring three-factor interactions** | May be important in some systems | Check significance before dropping |
| **Confusing coded and natural units** | Coefficients depend on coding | Always report in natural units for implementation |

---

## 8. Comparisons with Other Designs

### 8.1 3^k vs. 2^k + Center Points

| Feature | 3^k Full Factorial | 2^k + Center Points |
|--------|-------------------|----------------------|
| Runs for k=3 | 27 | 8 + n_center |
| Curvature detection | Yes (at all factor levels) | Yes (only at center) |
| Quadratic model fitting | Full model | Aliased (confounded) |
| Pure quadratic estimation | Unconfounded | Confounded with interactions |
| Best for | Detailed modeling | Screening + curvature check |

### 8.2 3^k vs. Central Composite Design (CCD)

| Feature | 3^k | CCD |
|--------|-----|-----|
| Runs for k=3 | 27 | 14–20 |
| Rotatability | No | Yes (with proper α) |
| Orthogonality | No (for quadratic) | Yes (with proper choice) |
| Prediction variance | Higher at edges | More uniform |
| Best for | Exact level requirements | Response surface optimization |

### 8.3 3^k vs. Box-Behnken Design

| Feature | 3^k | Box-Behnken |
|--------|-----|-------------|
| Runs for k=3 | 27 | 12–15 |
| Factor levels | 3 | 3 |
| Corner points | All 27 included | Excludes corners |
| Safety | May hit extreme combinations | Avoids extreme combinations |
| Best for | Full exploration | When corner runs are dangerous |

### 8.4 3^k vs. 3^(k-p) Fractional

| Feature | 3^k Full | 3^(k-p) Fractional |
|--------|----------|------------------|
| Runs | 3^k | 3^(k-p) |
| Information | Complete | Partial |
| Confounding | None | Some interactions confounded |
| Best for | k ≤ 4 | k ≥ 4, limited budget |

### 8.5 Decision Tree

```
Need to model curvature?
├── NO → Use 2^k or 2^(k-p)
└── YES
    ├── k ≤ 3 and budget allows?
    │   ├── YES → Use 3^k full factorial
    │   └── NO → Use 2^k + center points
    ├── k = 3–5 and moderate budget?
    │   └── Use CCD or Box-Behnken
    ├── k ≥ 4 and limited budget?
    │   └── Use 3^(k-p) fractional
    └── Need to avoid extreme combinations?
        └── Use Box-Behnken
```

---

## 9. Advanced Topics

### 9.1 Confounding and Blocking

3^k designs can be arranged in 3^p blocks. The defining contrast is:

```
L = a₁x₁ + a₂x₂ + ... + aₖxₖ (mod 3)
```

For example, a 3³ design in 3 blocks using AB² as the defining contrast:
- Block 1: L = 0
- Block 2: L = 1
- Block 3: L = 2

### 9.2 Fractional Factorial Construction

A 3^(k-p) design is constructed by setting p factors equal to generalized interactions of the remaining k-p factors.

Example: 3^(3-1) with I = ABC
- Set C = A + B (mod 3)
- This gives 9 runs (1/3 fraction)

### 9.3 Orthogonal Polynomial Contrasts

For 3-level factors, orthogonal polynomial contrasts are:

| Level | Linear (L) | Quadratic (Q) |
|-------|-----------|---------------|
| -1 | -1 | +1 |
| 0 | 0 | -2 |
| +1 | +1 | +1 |

These are used to decompose main effects into linear and quadratic components.

### 9.4 Response Surface Methodology (RSM)

3^k designs are a foundation of RSM. The full second-order model:

```
y = β₀ + Σ βᵢxᵢ + Σ βᵢᵢxᵢ² + Σ Σ βᵢⱼxᵢxⱼ + ε
```

is fitted and then optimized using:
- **Steepest ascent/descent** for first-order regions
- **Canonical analysis** for second-order regions
- **Ridge analysis** for constrained optimization

### 9.5 Mixed-Level Designs

When factors have different numbers of levels (e.g., 2-level and 3-level factors combined), use:
- General full factorial designs
- Mixed-level orthogonal arrays
- D-optimal designs

### 9.6 Software Implementation

| Software | 3^k Design Support |
|----------|-------------------|
| Python (pyDOE2) | `fullfact([3, 3, 3])` |
| R (DoE.base) | `fac.design(nlevels=c(3,3,3))` |
| Minitab | Stat → DOE → Factorial → General Full Factorial |
| JMP | DOE → Classical → Full Factorial |
| Design-Expert | Factorial → 3-Level |

---

## 10. References

### Books

1. **Montgomery, D. C.** (2017). *Design and Analysis of Experiments* (10th ed.). Wiley. — Chapter 9: Three-Level and Mixed-Level Factorial and Fractional Factorial Designs.

2. **Box, G. E. P., Hunter, J. S., & Hunter, W. G.** (2005). *Statistics for Experimenters: Design, Innovation, and Discovery* (2nd ed.). Wiley. — Chapters on response surface methodology and curvature detection.

3. **Myers, R. H., Montgomery, D. C., & Anderson-Cook, C. M.** (2016). *Response Surface Methodology: Process and Product Optimization Using Designed Experiments* (4th ed.). Wiley. — Comprehensive coverage of 3^k designs in RSM context.

4. **Wu, C. F. J., & Hamada, M.** (2021). *Experiments: Planning, Analysis, and Optimization* (3rd ed.). Wiley. — Chapter on three-level designs and orthogonal arrays.

5. **Shina, S.** (2022). *Industrial Design of Experiments*. Springer. — Chapter 5: Three-Level Factorial Design and Analysis Techniques.

### Articles & Papers

6. **NIST/SEMATECH** (2025). *e-Handbook of Statistical Methods*, Section 5.3.3.9: Three-level full factorial designs. https://www.itl.nist.gov/div898/handbook/pri/section3/pri339.htm

7. **Penn State University** (2025). *STAT 503: Design and Analysis of Experiments*, Lesson 9: 3-level and Mixed-level Factorials and Fractional Factorials. https://online.stat.psu.edu/stat503/

### Online Resources

8. **NIST Engineering Statistics Handbook** — Three-level full factorial designs: https://www.itl.nist.gov/div898/handbook/pri/section3/pri339.htm

9. **Penn State STAT 503** — 3-level and Mixed-level Factorials: https://online.stat.psu.edu/stat503/book/export/html/677

10. **Air Academy Associates** — Full Factorial Design Explained: https://airacad.com/full-factorial-design/

---

## Appendix: Quick Reference Card

### 3^k Design Summary

```
Factors:        k
Levels:         3 per factor (Low=-1, Center=0, High=+1)
Runs:           3^k (without replicates)
Main effect df: 2 per factor
Interaction df: 4 per 2-factor, 8 per 3-factor, etc.
Model:          y = β₀ + Σβᵢxᵢ + Σβᵢᵢxᵢ² + ΣΣβᵢⱼxᵢxⱼ + ε
```

### Key Formulas

```
Coded level:        x = (X - X_center) / ((X_high - X_low) / 2)
Linear effect:      E_L = (ȳ_+1 - ȳ_-1) / 2
Quadratic effect:   E_Q = (ȳ_+1 - 2ȳ_0 + ȳ_-1) / 2
SS for factor A:    SSA = 3^(k-1) * Σ(ȳ_i - ȳ̄)²  [for i = -1, 0, +1]
F-statistic:        F = MS_effect / MSE
```

### When to Use What

| Goal | Design |
|------|--------|
| Screen many factors | 2^k, Plackett-Burman |
| Detect curvature cheaply | 2^k + center points |
| Model curvature precisely | 3^k, CCD, Box-Behnken |
| Optimize with constraints | CCD, D-optimal |
| Avoid extreme runs | Box-Behnken |
| Limited runs, k > 4 | 3^(k-p), D-optimal |

---

*Generated for DoE Lecture 14: 3^k Full Factorial Designs*  
*Date: 2026-08-09*
