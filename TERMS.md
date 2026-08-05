If you're studying **Design of Experiments (DoE)** for research, data science, quality engineering, or statistics, the fastest way to remember the terminology is to think of DoE as:

> **"Change inputs systematically, measure outputs objectively, then use statistics to determine which inputs truly matter."**

Here is a practical **Rule of Thumb Cheat Sheet** for the most common DoE terms.

---

# 1. Experiment

**Definition**
A planned test where you deliberately change one or more variables to observe their effect.

### Rule of Thumb

> **Experiment = Controlled learning**

Example:
Change fertilizer amount and measure plant growth.

---

# 2. Factor

**Definition**

The variable you intentionally change.

Examples

* Temperature
* Pressure
* Fertilizer
* Algorithm
* CPU cores

### Rule of Thumb

> **Factor = Input**

---

# 3. Level

**Definition**

The possible values of a factor.

Temperature

* 20°C
* 40°C
* 60°C

### Rule of Thumb

> **Level = Setting of a factor**

---

# 4. Response Variable

**Definition**

The outcome you measure.

Examples

* Accuracy
* Yield
* Runtime
* Strength
* Latency

### Rule of Thumb

> **Response = Output**

---

# 5. Treatment

**Definition**

One complete combination of factor levels.

Example

Temperature = 60°C

Pressure = 3 bar

This combination is one treatment.

### Rule of Thumb

> **Treatment = One recipe**

---

# 6. Experimental Unit

**Definition**

The smallest object receiving a treatment.

Examples

* One patient
* One machine
* One website visitor
* One metal sample

### Rule of Thumb

> **Experimental Unit = Who gets tested**

---

# 7. Replication

**Definition**

Repeating the same treatment several times.

Purpose

Reduce random error.

### Rule of Thumb

> **Replication = Repeat to increase confidence**

---

# 8. Randomization

**Definition**

Assign treatments randomly.

Purpose

Prevent bias.

### Rule of Thumb

> **Randomization = Fair assignment**

---

# 9. Blocking

**Definition**

Group similar experimental units before randomization.

Example

Morning workers

Evening workers

Run experiments separately.

### Rule of Thumb

> **Blocking removes known variation**

---

# 10. Control Group

**Definition**

A baseline group receiving standard treatment or no treatment.

### Rule of Thumb

> **Control = Reference point**

---

# 11. Noise Factor

**Definition**

Variables you cannot easily control.

Examples

Humidity

Operator skill

Room temperature

### Rule of Thumb

> **Noise = Unwanted variation**

---

# 12. Confounding

**Definition**

Two effects are mixed together and cannot be separated.

### Rule of Thumb

> **Confounding = Can't tell who caused the effect**

---

# 13. Main Effect

**Definition**

Effect of changing one factor alone.

Example

Increasing temperature increases yield.

### Rule of Thumb

> **Main Effect = Individual influence**

---

# 14. Interaction Effect

**Definition**

The effect of one factor depends on another.

Example

Temperature helps only when pressure is high.

### Rule of Thumb

> **Interaction = Teamwork between factors**

---

# 15. Full Factorial Design

**Definition**

Test every possible combination.

2 factors

2 levels each

Total runs

2² = 4

### Rule of Thumb

> **Full Factorial = Test everything**

---

# 16. Fractional Factorial Design

**Definition**

Test only part of all combinations.

Purpose

Save time and cost.

### Rule of Thumb

> **Fractional = Smart shortcut**

---

# 17. One Factor at a Time (OFAT)

**Definition**

Change one variable while keeping others fixed.

### Rule of Thumb

> **Easy but inefficient**

Cannot detect interactions.

---

# 18. Factorial Design

**Definition**

Change multiple factors simultaneously.

### Rule of Thumb

> **Efficient learning**

---

# 19. Resolution (Fractional Designs)

**Definition**

Indicates how much confounding exists.

Higher resolution

Better separation.

### Rule of Thumb

| Resolution | Meaning                                        |
| ---------- | ---------------------------------------------- |
| III        | Main effects mixed with interactions           |
| IV         | Main effects clear                             |
| V          | Main effects and two-factor interactions clear |

---

# 20. Alias Structure

**Definition**

Which effects are confounded together.

### Rule of Thumb

> **Alias = Hidden identity**

---

# 21. Response Surface Methodology (RSM)

**Definition**

Optimize a response after finding important factors.

### Rule of Thumb

> **RSM = Find the best settings**

---

# 22. Center Point

**Definition**

Middle level of quantitative factors.

Purpose

Detect curvature.

### Rule of Thumb

> **Center Point checks whether the relationship is curved**

---

# 23. Curvature

**Definition**

Relationship isn't a straight line.

Example

Yield increases then decreases.

### Rule of Thumb

> **Curvature = Not linear**

---

# 24. DOE Run

**Definition**

One execution of one treatment.

### Rule of Thumb

> **Run = One experiment**

---

# 25. Design Matrix

**Definition**

Table listing every experimental run.

### Rule of Thumb

> **Design Matrix = Experiment blueprint**

---

# 26. Statistical Significance

**Definition**

Observed effect is unlikely due to chance.

Usually

P-value < 0.05

### Rule of Thumb

> **Significant = Probably real**

---

# 27. Effect Size

**Definition**

How large the effect actually is.

### Rule of Thumb

> **Significance says "real"; Effect size says "important."**

---

# 28. Power

**Definition**

Probability of detecting a true effect.

### Rule of Thumb

> **Power = Chance of finding real differences**

Higher power generally comes from larger sample sizes, lower variability, or stronger effects.

---

# 29. Sample Size

**Definition**

Number of experimental units.

### Rule of Thumb

> **Too small → miss effects; Too large → waste resources.**

---

# 30. Residual Error

**Definition**

Variation not explained by the model.

### Rule of Thumb

> **Residual = What's left unexplained**

---

# Mental Model of DoE

```text
Research Question
        │
        ▼
Choose Factors
        │
        ▼
Choose Levels
        │
        ▼
Create Treatments
        │
        ▼
Randomize Runs
        │
        ▼
Run Experiment
        │
        ▼
Collect Responses
        │
        ▼
Analyze (ANOVA / Regression)
        │
        ▼
Main Effects?
Interactions?
Curvature?
        │
        ▼
Optimize Process
```

## The 10 DoE Terms You Should Never Confuse

| Term              | Think of it as                                      |
| ----------------- | --------------------------------------------------- |
| Factor            | Input you control                                   |
| Level             | Value of that input                                 |
| Treatment         | One combination of levels                           |
| Response          | Output you measure                                  |
| Experimental Unit | What receives the treatment                         |
| Replication       | Repeating a treatment                               |
| Randomization     | Random assignment/order                             |
| Blocking          | Grouping similar units to reduce unwanted variation |
| Main Effect       | Effect of one factor alone                          |
| Interaction       | Effect of one factor depends on another             |

These concepts form the foundation for understanding more advanced topics such as factorial designs, response surface methodology, ANOVA, regression modeling, and power analysis in Design of Experiments.
