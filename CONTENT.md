***

# Part 1: Margin of Error, Bootstrapping & Hypothesis Testing Fundamentals

## Section A: Margin of Error & Sample Size for Confidence Intervals
*This topic answers two practical questions: (1) How accurate is my estimate? → Margin of Error (ME), and (2) How many observations should I collect? → Sample Size (n).*

### 1. Big Picture
Suppose you want to estimate the average height of 20,000 university students. Instead of measuring everyone, you measure 100 students and find a sample mean = 170 cm. Since you only measured a sample, your estimate is not exact. Rather than saying "The average height is exactly 170 cm," you report **170 ± 2 cm**, where ±2 cm is the Margin of Error. Therefore, the 95% confidence interval is **(168 cm, 172 cm)**.

### 2. What is Margin of Error?
The Margin of Error (ME) tells you how far your estimate might be from the true population value. 
* A **smaller ME** means a more precise estimate.
* A **larger ME** means less precision. 
* *Example:* If a poll estimates Candidate A has 60% support with a Margin of Error of ±3%, the true support is likely between 57% and 63%.

### 3. Formula
For a confidence interval of the mean:
$$ ME = z \times \frac{\sigma}{\sqrt{n}} $$
Where:
* $z$ = confidence level critical value
* $\sigma$ = population standard deviation
* $n$ = sample size  
*Note: Only $n$ is under the square root, which is why increasing the sample size has diminishing returns.*

### 4. What Affects Margin of Error?
There are three factors:
1. **Confidence Level:** Higher confidence (e.g., 99% instead of 95%) uses a larger $z$-value, so the Margin of Error becomes larger. *(Example: 95% → 170 ± 2, while 99% → 170 ± 3).*
2. **Standard Deviation ($\sigma$):** More variability in the data increases uncertainty, leading to a larger Margin of Error.
3. **Sample Size ($n$):** A larger sample decreases the Margin of Error because $ME \propto \frac{1}{\sqrt{n}}$.  
   *Example:* $n = 25 \rightarrow ME \approx 4$; $n = 100 \rightarrow ME \approx 2$; $n = 400 \rightarrow ME \approx 1$. **To cut the Margin of Error in half, you must collect four times as much data.**

### 5. Why the Square Root?
Uncertainty decreases *more slowly* than the sample size increases. For example, if $n = 100$ gives $ME = 2$, doubling the sample to $n = 200$ gives:
$$ ME = 2 \times \sqrt{\frac{100}{200}} \approx 1.41 $$
The Margin of Error decreases, but not by half.

### 6. Sample Size Formula
If you want a specific Margin of Error before collecting data, rearrange the formula:
$$ n = \left(\frac{z\sigma}{ME}\right)^2 $$
Everything is squared, so reducing the desired Margin of Error requires many more observations.

### 7. Example Calculation
Suppose $\sigma = 10$, 95% confidence ($z \approx 1.96$), and you want $ME = 2$.
$$ n = \left(\frac{1.96 \times 10}{2}\right)^2 = 96.04 $$
*Always round up*, so the required sample size is **97**.

### 8. Effect of Desired Precision
Smaller Margins of Error require much larger samples:
* $ME = 5 \rightarrow n \approx 16$
* $ME = 2 \rightarrow n \approx 97$
* $ME = 1 \rightarrow n \approx 385$

### 9. Key Relationships
| Increase... | Effect on Margin of Error |
| :--- | :--- |
| Confidence level | Increases |
| Standard deviation | Increases |
| Sample size | Decreases |

### 10. Things to Remember
✔ Bigger sample → Smaller Margin of Error.  
✔ Bigger confidence level → Bigger Margin of Error.  
✔ Greater variability → Bigger Margin of Error.  
✔ To halve the Margin of Error, collect **4×** more data.  
✔ Always round the required sample size **up**.

---

## Section B: Bootstrapping and Resampling in Statistics

### 1. Big Picture
Usually, we want to understand a population, but we only have a sample.  
*Example:* A company wants to know the average salary of 50,000 employees. Impossible to measure everyone. So we take a sample of 100 employees: `[4000, 4500, 5000, 6000, 7000]`. Sample mean = 5300.  
*Question:* How reliable is this mean? **Bootstrapping helps us answer this.**

### 2. What is Resampling?
Resampling means repeatedly taking samples from existing data to understand uncertainty, instead of collecting new data every time.  
*Original sample:* `[10, 20, 30, 40, 50]`  
*New samples created from it:*  
- Sample 1: `[10, 20, 20, 40, 50]`  
- Sample 2: `[30, 30, 40, 50, 50]`  
- Sample 3: `[10, 10, 20, 40, 50]`  
Then calculate the mean each time.

### 3. What is Bootstrapping?
Bootstrapping is a resampling method where you:
1. Take your original sample.
2. Randomly sample from it **with replacement**.
3. Create many bootstrap samples (e.g., 10,000).
4. Calculate the statistic (mean, median, regression coefficient...) for each.
5. Look at the distribution of these statistics.  
*Idea:* The bootstrap distribution approximates the true sampling distribution.

### 4. What Does "With Replacement" Mean?
Original data: `[5, 10, 15, 20, 25]`  
A bootstrap sample can be: `[5, 5, 10, 20, 25]` because after selecting 5, we put it back. So a value can appear multiple times.

### 5. Why Do We Need Bootstrapping?
Traditional statistics often require strict assumptions: normal distribution, known population variance, large sample size.  
Bootstrapping is useful when:
* Sample size is small
* Distribution is unknown
* Data is not normal

### 6. Bootstrap Confidence Interval
After generating bootstrap means, we take the middle 95%.  
*Example:* 2.5% percentile = 13.1, 97.5% percentile = 15.4.  
Confidence interval: **(13.1, 15.4)**. Based on our sample, the true population mean is likely inside this range.

### 7. Bootstrap vs Traditional Confidence Interval
| Method | Requires assumptions? |
| :--- | :--- |
| Normal CI | Needs normality assumptions |
| Bootstrap CI | Uses data itself (more flexible) |

### 8. Simple Workflow
Original Sample → Random sampling with replacement → Bootstrap samples (1000+) → Calculate statistic each time → Bootstrap distribution → Confidence Interval.

---

## Section C: Hypothesis Testing: Calculations and Interpretations

### 1. Big Picture
Hypothesis testing is a statistical method used to make decisions about a population using sample data.  
*Main question:* "Is the difference we observe real, or could it happen by random chance?"

### 2. The Two Hypotheses
* **Null Hypothesis ($H_0$):** The default assumption. "Nothing changed" or "No difference exists." *(Example: $H_0: \mu = 10$)*
* **Alternative Hypothesis ($H_a$ or $H_1$):** What we are trying to find evidence for. *(Example: $H_a: \mu \neq 10$)*

### 3. Hypothesis Testing Logic
Population → Take Sample → Calculate Test Statistic → Find p-value → Decision.

### 4. Test Statistic
Measures how far our sample result is from the value claimed in $H_0$. For a mean:
$$ z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}} $$

### 5. P-value
Answers: *If the null hypothesis is true, how likely is it to observe this result?*
* **Small p-value:** Evidence against $H_0$.
* **Large p-value:** Not enough evidence against $H_0$.

### 6. Significance Level ($\alpha$)
Before testing, choose $\alpha$ (common: $\alpha = 0.05$). Meaning: We accept a 5% chance of rejecting a true null hypothesis.

### 7. Decision Rule
* If $p < 0.05$: **Reject $H_0$**. There is significant evidence.
* If $p > 0.05$: **Fail to reject $H_0$**. Not enough evidence.

### 8. Types of Hypothesis Tests
* **Two-tailed test:** Looking for *any* difference ($H_a: \mu \neq \mu_0$).
* **Left-tailed test:** Looking for a *decrease* ($H_a: \mu < \mu_0$).
* **Right-tailed test:** Looking for an *increase* ($H_a: \mu > \mu_0$).

### 9. Errors in Hypothesis Testing
* **Type I Error (False Positive):** Reject $H_0$ when it is actually true. Probability = $\alpha$.
* **Type II Error (False Negative):** Fail to reject $H_0$ when it is false. Probability = $\beta$.

### 10. Important Interpretation
❌ Never say: "We accept $H_0$".  
✅ Always say: "We fail to reject $H_0$". (Because statistics cannot prove $H_0$ is true).

---

## Section D: Hypothesis Testing: One-Sided vs Two-Sided Alternative

### 1. Big Picture
The alternative hypothesis ($H_1$) can be two-sided (looking for any difference) or one-sided (looking for a difference in a specific direction). This choice changes how we calculate the p-value and where we reject $H_0$.

### 2. Two-Sided Alternative Test
Asks: "Is the population parameter different from the claimed value?"  
Rejection areas exist in **both tails**.  
*Example:* $z = 2.19$. Right tail $P(Z > 2.19) = 0.0143$. Left tail $P(Z < -2.19) = 0.0143$.  
Total p-value = $0.0143 + 0.0143 = 0.0286$.

### 3. One-Sided Alternative Test
Asks: "Is the parameter only bigger or only smaller?"
* **Right-Tailed Test:** Only the right tail matters. *(Example: Did the new method increase scores? $H_a: \mu > 70$)*
* **Left-Tailed Test:** Only the left tail matters. *(Example: Did the new machine reduce time? $H_a: \mu < 10$)*

### 4. Difference in P-value Calculation
For $z = 2.19$:
* **Two-sided:** Multiply by 2 $\rightarrow p = 0.0286$
* **Right-sided:** Only one tail $\rightarrow p = 0.0143$  
*Notice: The one-sided test gives a smaller p-value because we only look in one direction.*

### 5. Critical Values (for $\alpha = 0.05$)
* **Two-sided:** Split alpha (0.025 + 0.025). Critical values: $z = \pm 1.96$
* **One-sided:** All alpha goes to one side. Critical values: $z = 1.645$ (Right) or $z = -1.645$ (Left).  
*Therefore, it is easier to reject $H_0$ in a one-sided test.*

### 6. Important Rule
You **must** choose one-sided or two-sided **before seeing the data**.  
❌ Wrong: "I got a positive result, so I will use a right-tailed test."  
✅ Correct: "Before collecting data, I decided I only care about increases."

***
Here is the fully formatted and cleaned-up Markdown for this section. I have fixed all the garbled mathematical formulas, structured the tables, and properly formatted the R script for maximum readability.

***

## Section E: When to Use Each Test?

| Situation | Test |
| :--- | :--- |
| Is the value different? | Two-sided |
| Did it increase? | Right-sided |
| Did it decrease? | Left-sided |
| Research without direction | Two-sided |
| Strong theory predicts direction | One-sided |

---

## Section F: Hypothesis Test vs. Confidence Interval

### 1. Big Picture
Both **hypothesis testing** and **confidence intervals** are methods of statistical inference. They use sample data to learn about a population.
* **Hypothesis Test:** "Is my claim supported or not?"
* **Confidence Interval:** "What range of values is reasonable for the population parameter?"

### 2. Example
A company claims: $\mu = 50$ (Average battery life is 50 hours).  
You collect a sample: $n = 30$, sample mean $= 52$.  
You can answer two different questions.

**Question 1: Hypothesis Test**  
"Is the true mean different from 50?"  
* Hypotheses: $H_0: \mu = 50$, $H_a: \mu \neq 50$  
* Result: p-value $= 0.03$  
* Since: $0.03 < 0.05 \rightarrow$ **Reject $H_0$**.  
* Conclusion: There is evidence that the average battery life is different from 50.

**Question 2: Confidence Interval**  
Instead of a yes/no decision: "What values are possible for the true mean?"  
* Example: $95\% \text{ CI} = (50.5, 53.5)$  
* Meaning: The true population mean is likely between 50.5 and 53.5.

### 3. Relationship Between Them
There is a direct connection. For a two-sided hypothesis test with $\alpha = 0.05$, we use a $95\% \text{ Confidence Interval}$.

**Decision rule:**
* If the null value is **outside** the confidence interval $\rightarrow$ **Reject $H_0$**.  
  *(Example: CI is $(51, 54)$. $50$ is outside $\rightarrow$ Reject $H_0$.)*
* If the null value is **inside** the confidence interval $\rightarrow$ **Fail to reject $H_0$**.  
  *(Example: CI is $(48, 53)$. $50$ is inside $\rightarrow$ Fail to reject $H_0$.)*

### 4. The Connection Formula
For a two-sided test:
* $p < 0.05$ is equivalent to: $\text{Null value is NOT inside 95\% CI}$
* $p > 0.05$ is equivalent to: $\text{Null value IS inside 95\% CI}$

### 5. Differences
| Hypothesis Test | Confidence Interval |
| :--- | :--- |
| Gives decision | Gives range |
| Uses p-value | Uses interval |
| Reject or fail to reject $H_0$ | Shows possible parameter values |
| Answers "Is there evidence?" | Answers "What values are plausible?" |

### 6. Example With Numbers
Suppose: Sample mean $\bar{x} = 52$, Standard error $SE = 1$.  
$95\% \text{ CI}: 52 \pm 1.96(1) \rightarrow (50.04, 53.96)$  
The claimed value: $\mu_0 = 50$.  
$50$ is outside the interval $\rightarrow$ **Reject $H_0$**. (Same conclusion as the hypothesis test).

### 7. Why Confidence Intervals Are Often Better
A hypothesis test only says: *Significant* or *Not significant*.  
But confidence intervals tell you:
1. Direction
2. Size of difference
3. Precision  

*Example:*  
❌ Bad conclusion: "The new model is significantly better."  
✅ Better conclusion: "The new model improves accuracy by 2% to 5%."

### 8. Real Data Science Example (A/B Testing)
* Old website: $\text{Conversion} = 10\%$
* New website: $\text{Conversion} = 12\%$
* **Hypothesis test:** Is the improvement statistically significant?
* **Confidence interval:** The improvement is between 1% and 3%.  
*Both are useful.*

### Key Takeaway
**Hypothesis Test:** "Is there enough evidence against $H_0$?"  
**Confidence Interval:** "What values are reasonable for the population?"  

**The connection:**
* Reject $H_0$ = Null value outside Confidence Interval
* Fail to reject $H_0$ = Null value inside Confidence Interval

*For AI/Data Science, this relationship appears in: A/B testing, ML model comparison, Feature significance, Research experiments, Paper results interpretation.*

---

## Section G: Errors and Power in Hypothesis Testing

### 1. Big Picture
In hypothesis testing, we make decisions based on sample data. But because we use samples, mistakes can happen.
* There are two possible errors: **Type I Error** and **Type II Error**.
* We also have a concept called **Statistical Power**, which measures how good our test is at detecting real effects.

### 2. Hypothesis Testing Decision Table
Assume: $H_0: \text{No difference}$, $H_a: \text{There is a difference}$

| Reality | Decision | Result |
| :--- | :--- | :--- |
| $H_0$ true | Fail to reject $H_0$ | Correct |
| $H_0$ true | Reject $H_0$ | **Type I Error** |
| $H_0$ false | Reject $H_0$ | Correct |
| $H_0$ false | Fail to reject $H_0$ | **Type II Error** |

### 3. Type I Error (False Positive)
* **Definition:** Rejecting $H_0$ when $H_0$ is actually true. (We found an effect that does not really exist).
* **Example:** A medical test says "Patient has disease" but the patient is healthy.
* **Probability:** $\alpha$ (Usually $\alpha = 0.05$, meaning a 5% chance of making this mistake).

### 4. Type II Error (False Negative)
* **Definition:** Failing to reject $H_0$ when $H_0$ is false. (We missed a real effect).
* **Example:** A medical test says "No disease" but the patient is sick.
* **Probability:** $\beta$

### 5. Power of a Test
Power measures the probability of detecting a real effect.
* **Formula:** $\text{Power} = 1 - \beta$
* **Example:** If $\beta = 0.20$, then $\text{Power} = 1 - 0.20 = 0.80$. (The test has an 80% chance of detecting a true effect).

### 6. Factors Affecting Power
* **A. Sample Size ($n$):** Larger sample $\rightarrow$ Less uncertainty $\rightarrow$ Higher power.
* **B. Effect Size:** A bigger difference is easier to detect. ($50 \rightarrow 70$ is easier to detect than $50 \rightarrow 51$).
* **C. Significance Level ($\alpha$):** Higher $\alpha$ $\rightarrow$ Easier to reject $H_0$ $\rightarrow$ Higher power. *(But higher $\alpha$ increases Type I error).*
* **D. Variability:** Less noise $\rightarrow$ Higher power. More variation $\rightarrow$ Lower power.

### 7. Relationship Between Errors
Usually, increasing power decreases Type II Error ($\text{Power} = 1 - \beta$). But reducing Type II Error often requires: Larger sample size, Larger effect, or Higher alpha.

### 8. Important Difference
| Error | Meaning |
| :--- | :--- |
| Type I | False alarm |
| Type II | Missed detection |
| Power | Ability to detect true effects |

### Key Takeaway & Final Summary
* **Type I Error:** Reject $H_0$ when it is true (False Positive) $\rightarrow \alpha$
* **Type II Error:** Fail to reject $H_0$ when it is false (False Negative) $\rightarrow \beta$
* **Power:** Detecting a true effect $\rightarrow \text{Power} = 1 - \beta$
* **Higher power comes from:** $\uparrow$ Sample size, $\uparrow$ Effect size, $\downarrow$ Variability, $\uparrow$ Alpha.
* **Common target:** $\text{Power} = 80\%$

### Connection to Previous Topics (Your Roadmap)
```text
Confidence Intervals
        ↓
Hypothesis Testing
        ↓
One vs Two Sided Tests
        ↓
Errors (Type I / II)
        ↓
Power Calculations  ← YOU ARE HERE
        ↓
One Sample t-test
        ↓
Two Sample t-test
        ↓
ANOVA
        ↓
Regression
```

---

## Section H: Power Calculations in Hypothesis Testing

### 1. Big Picture
In hypothesis testing, we want to know: *"If a real effect exists, how likely are we to detect it?"*  
This probability is called **Power**.
$$ \text{Power} = P(\text{Reject } H_0 \mid H_0 \text{ is false}) $$
In simple words: Power is the ability of a statistical test to find a true difference.

### 2. Why Do We Calculate Power?
Before collecting data, researchers ask: *"How many observations do I need?"*  
Power calculation helps determine the required sample size to achieve a specific confidence, significance level, and probability of detecting an effect.

### 3. Effect Size Calculation
For a one-sample mean test:
$$ d = \frac{\mu_1 - \mu_0}{\sigma} $$
Where $\mu_0$ = null hypothesis mean, $\mu_1$ = true mean, $\sigma$ = standard deviation.  
*Example:* Old average $\mu_0 = 50$, New true average $\mu_1 = 52$, $\sigma = 5$.  
Effect size: $d = \frac{52 - 50}{5} = 0.4$

### 4. Small vs Large Effect Size
| Effect Size | Meaning |
| :--- | :--- |
| 0.2 | Small |
| 0.5 | Medium |
| 0.8+ | Large |

*Note: Small effects require larger samples.*

### 5. Increasing Power
To increase power:
1. Increase sample size ✅ *(Most common solution: $\boxed{\text{Increase sample size}}$)*
2. Increase effect size
3. Reduce variability
4. Increase $\alpha$

### 6. Sample Size Planning
Usually, researchers choose $\text{Power} = 0.80$ before collecting data (meaning they want an 80% chance of detecting a real effect).  
*Example for A/B testing:* Minimum detectable improvement $= +5\%$, Power $= 80\% \rightarrow$ Required users $= 10,000$.

---

## Section I: Bootstrap Hypothesis Testing

### 1. Big Picture
**Bootstrap Hypothesis Testing** is a non-parametric hypothesis testing method. Instead of relying on theoretical distributions (t-distribution or normal distribution), it uses **resampling** to estimate the sampling distribution.  
*Main idea:* "If the null hypothesis is true, how unusual is our observed statistic?" Instead of using formulas, we let the computer answer by repeatedly sampling the data.

### 2. Why Bootstrap?
Traditional hypothesis tests assume normal distribution, equal variance, and large sample size. Bootstrap provides an alternative when data is skewed, sample size is small, or the distribution is unknown.

### 3. Bootstrap Under the Null Hypothesis
To simulate the null hypothesis, shift the data so its mean equals the hypothesized value.  
*Original sample:* `72 75 70 78 74` (Observed mean = 73.8)  
*Hypothesized mean:* 70  
*Shifted data:* `Data - 73.8 + 70` (Now the shifted sample satisfies $H_0$). Bootstrap from this shifted sample.

### 4. Calculate the Bootstrap p-value
The p-value is approximately:  
$$ \frac{\text{Number of bootstrap statistics at least as extreme as observed}}{\text{Total bootstrap samples}} $$

### 5. Traditional vs Bootstrap
| Traditional t-test | Bootstrap Test |
| :--- | :--- |
| Uses t-distribution | Uses resampling |
| Parametric | Non-parametric |
| Fast | Slower |
| Formula-based | Simulation-based |
| Assumptions required | Fewer assumptions |

### 6. Applied R Studio Script
*Script name: Save this file as `21_Bootstrap_Hypothesis_Testing.R`*

```r
############################################################
# Bootstrap Hypothesis Testing
############################################################
set.seed(123)

############################################################
# 1. Create Sample Data
############################################################
sample_data <- c(
  72, 75, 70, 78, 74,
  80, 77, 73, 76, 79
)
sample_data

############################################################
# 2. Observed Mean
############################################################
observed_mean <- mean(sample_data)
observed_mean

############################################################
# 3. Define Null Hypothesis
############################################################
null_mean <- 70

############################################################
# 4. Shift Data Under H0
############################################################
shifted_data <- sample_data - observed_mean + null_mean
mean(shifted_data)

############################################################
# 5. Bootstrap Resampling
############################################################
B <- 10000
bootstrap_means <- numeric(B)
n <- length(shifted_data)

for(i in 1:B){
  bootstrap_sample <- sample(
    shifted_data,
    size = n,
    replace = TRUE
  )
  bootstrap_means[i] <- mean(bootstrap_sample)
}

############################################################
# 6. Plot Bootstrap Distribution
############################################################
hist(
  bootstrap_means,
  breaks = 30,
  main = "Bootstrap Distribution Under H0",
  xlab = "Bootstrap Means"
)
abline(v = observed_mean, lwd = 2, col = "red")

############################################################
# 7. Bootstrap p-value
############################################################
observed_difference <- abs(observed_mean - null_mean)
bootstrap_difference <- abs(bootstrap_means - null_mean)

p_value <- mean(bootstrap_difference >= observed_difference)
p_value

############################################################
# 8. Decision
############################################################
alpha <- 0.05
if(p_value < alpha){
  cat("Reject H0\n")
} else {
  cat("Fail to Reject H0\n")
}

############################################################
# 9. Compare with Classical t-test
############################################################
t.test(sample_data, mu = null_mean)

############################################################
# 10. Confidence Interval Using Bootstrap
############################################################
bootstrap_original <- numeric(B)
for(i in 1:B){
  bootstrap_sample <- sample(
    sample_data,
    size = n,
    replace = TRUE
  )
  bootstrap_original[i] <- mean(bootstrap_sample)
}
quantile(bootstrap_original, c(0.025, 0.975))

############################################################
# END
############################################################
```

### 7. Comparison of Tests
| Method | When to Use |
| :--- | :--- |
| One-sample t-test | Data approximately normal |
| Paired t-test | Same subjects measured twice |
| Independent t-test | Two independent groups |
| Wilcoxon Signed Rank | Paired, non-normal data |
| Mann-Whitney U | Independent, non-normal data |
| **Bootstrap Hypothesis Test** | **Unknown distribution, small sample, or avoiding parametric assumptions** |

***
***

# Part 2: ANOVA, Sum of Squares & Simple Linear Regression Concept

## Section A: Where Bootstrap is Used (Wrap-up)
Bootstrap hypothesis testing is widely used in:
* Machine Learning model evaluation
* A/B testing
* Clinical research
* Data Science experiments
* Bioinformatics
* Financial risk analysis
* Estimating uncertainty when theoretical distributions are unreliable

---

## Section B: ANOVA (Analysis of Variance) and Sum of Squares
*Script name: Save this file as `25_ANOVA_Sum_of_Squares.R` or `anova_sum_of_squares.R`*

### 1. Big Picture
In the previous lesson, we learned that ANOVA compares the means of three or more groups. But how does ANOVA actually measure differences? The answer is through **Sum of Squares (SS)**. 
The idea is simple: ANOVA measures variation in the data and separates it into different sources.

### 2. What is Sum of Squares (SS)?
Sum of Squares (SS) measures the **total variability** in the data. It is calculated by:
1. Find the difference from a reference value.
2. Square the difference.
3. Add all squared differences.

**Formula:**
$$ SS = \sum (x_i - \text{Reference})^2 $$

**Why square?**
1. Negative values become positive.
2. Larger deviations receive more weight.
3. Prevents positive and negative differences from canceling each other.

### 3. Example
**Scores:** 80, 82, 84 | **Mean:** 82

| Score | Difference | Squared Difference |
| :--- | :--- | :--- |
| 80 | -2 | 4 |
| 82 | 0 | 0 |
| 84 | 2 | 4 |

**Total Sum of Squares:** $SS = 4 + 0 + 4 = 8$. Larger SS means greater variability.

### 4. Three Types of Sum of Squares
ANOVA splits the total variation into two parts. This is the most important ANOVA relationship:
$$ SST = SSB + SSW $$
Where:
* **SST** = Total Sum of Squares
* **SSB** = Between-Groups Sum of Squares
* **SSW** = Within-Groups Sum of Squares

### 5. Total Sum of Squares (SST)
SST measures how much all observations vary from the overall (grand) mean.
$$ SST = \sum (x_i - \bar{x})^2 $$
*(Where $\bar{x}$ is the grand mean. Example: Every observation is compared to the grand mean of 82).*

### 6. Within-Group Sum of Squares (SSW)
SSW measures variation **inside** each group. Each observation is compared with its *own group mean*. Small SSW means members of each group are very similar.

### 7. Between-Group Sum of Squares (SSB)
SSB measures how far each **group mean** is from the grand mean. Large SSB suggests the groups differ.

### 8. Visual Interpretation
```text
                Total Variation (SST)
                        |
        -------------------------------------
        |                                   |
        ↓                                   ↓
Between Groups (SSB)              Within Groups (SSW)
(Group Means Differ)          (Individuals Differ)
```
**Remember:** $SST = SSB + SSW$

### 9. Why ANOVA Uses Variance
Variance is simply:
$$ \text{Variance} = \frac{SS}{df} $$
*(Where $df$ is the degrees of freedom).*
ANOVA converts Sum of Squares into **Mean Squares (MS)**:
$$ MS = \frac{SS}{df} $$
There are two mean squares:
$$ MSB = \frac{SSB}{df_B} \quad \text{and} \quad MSW = \frac{SSW}{df_W} $$

### 10. F Statistic
The ANOVA test statistic is:
$$ F = \frac{MSB}{MSW} $$
**Interpretation:**
* If $MSB \approx MSW$, then $F \approx 1 \rightarrow$ The groups are probably similar.
* If $MSB \gg MSW$, then $F$ is large $\rightarrow$ The groups likely differ.

### 11. Example Calculation
Suppose $SSB = 180$, $df_B = 2 \rightarrow MSB = 90$
And $SSW = 60$, $df_W = 12 \rightarrow MSW = 5$
$$ F = \frac{90}{5} = 18 $$
A very large F-statistic provides strong evidence that at least one group mean differs.

### 12. ANOVA Table
A typical ANOVA table looks like this:

| Source | SS | df | MS | F |
| :--- | :--- | :--- | :--- | :--- |
| **Between Groups** | 180 | 2 | 90 | 18 |
| **Within Groups** | 60 | 12 | 5 | |
| **Total** | 240 | 14 | | |

*Notice: Total SS = Between SS + Within SS*

### 13. Real Data Science Example
Suppose we compare three machine learning algorithms: Random Forest, XGBoost, Neural Network. Each model is tested on multiple datasets. If the model accuracies differ greatly, Between-group variation increases, making the F-statistic larger.

**Workflow:**
```text
Collect Data → Compute Grand Mean → Compute SST → Split Into SSB and SSW 
→ Compute MSB and MSW → Compute F Statistic → Calculate p-value → Decision
```

### 14. Applied R Studio Script
```r
############################################################
# ANOVA and Sum of Squares
############################################################

############################################################
# 1. Create Three Groups
############################################################
group_A <- c(82, 85, 88, 84, 86)
group_B <- c(75, 78, 74, 77, 76)
group_C <- c(90, 92, 91, 89, 93)

############################################################
# 2. Combine Data
############################################################
scores <- c(group_A, group_B, group_C)
groups <- factor(c(
  rep("A", length(group_A)),
  rep("B", length(group_B)),
  rep("C", length(group_C))
))
data <- data.frame(Group = groups, Score = scores)

############################################################
# 3. Grand Mean
############################################################
grand_mean <- mean(data$Score)
grand_mean

############################################################
# 4. Total Sum of Squares (SST)
############################################################
SST <- sum((data$Score - grand_mean)^2)
SST

############################################################
# 5. Within-Group Sum of Squares (SSW)
############################################################
SSW <- sum(ave(data$Score, data$Group, FUN = function(x) (x - mean(x))^2))
SSW

############################################################
# 6. Between-Group Sum of Squares (SSB)
############################################################
SSB <- SST - SSW
SSB

############################################################
# 7. Verify Relationship
############################################################
SST
SSB + SSW

############################################################
# 8. Perform ANOVA
############################################################
anova_model <- aov(Score ~ Group, data = data)
summary(anova_model)

############################################################
# 9. Extract ANOVA Table
############################################################
anova_table <- summary(anova_model)[[1]]
anova_table

############################################################
# 10. Extract Components
############################################################
anova_table$`Sum Sq`
anova_table$`Mean Sq`
anova_table$`F value`
anova_table$`Pr(>F)`

############################################################
# 11. Boxplot
############################################################
boxplot(Score ~ Group, data = data, main = "ANOVA Example", 
        xlab = "Group", ylab = "Score")

############################################################
# 12. Compare Group Means
############################################################
aggregate(Score ~ Group, data = data, mean)

############################################################
# END
############################################################
```

### 15. Key Takeaway & Summary
```text
Total Variation (SST)
          |
 -------------------------
 |                       |
 ↓                       ↓
Between (SSB)      Within (SSW)

SST = SSB + SSW
      ↓
MSB = SSB / df
MSW = SSW / df
      ↓
F = MSB / MSW
      ↓
Large F → Evidence that at least one group mean differs
```

| Quantity | Meaning |
| :--- | :--- |
| **SST** | Total variability in all observations |
| **SSB** | Variability due to differences between group means |
| **SSW** | Variability within each group |
| **MS** | Average variability (SS ÷ df) |
| **F-statistic** | Ratio of between-group to within-group variability |

**Connection to Data Science:** ANOVA and Sum of Squares are widely used in comparing multiple ML models, A/B/C testing, clinical trials, manufacturing quality control, marketing/agricultural/educational experiments.

**Learning Roadmap:**
```text
One-Sample t-test → Independent t-test → One-Way ANOVA → ANOVA Sum of Squares (← You are here) 
→ F Distribution → Post-hoc Tests (Tukey HSD) → Two-Way ANOVA → Linear Regression
```

---

## Section C: Simple Linear Regression Concept
*Script name: Save this file as `31_Simple_Linear_Regression_Concept.R` or `simple_linear_regression_concept.R`*

### 1. Big Picture
Simple Linear Regression answers: *"Can we predict one numerical variable using another numerical variable?"*
It studies the relationship between:
1. **Independent Variable (X)** → Predictor / Feature
2. **Dependent Variable (Y)** → Response / Outcome

*Example:* Can we predict house price (Y) using house size (X)?

### 2. Examples of Linear Regression
| X (Predictor) | Y (Outcome) |
| :--- | :--- |
| Study hours | Exam score |
| Advertising spending | Sales |
| Temperature | Ice cream sales |
| Age | Income |
| Number of features | Model accuracy |

### 3. The Idea of a Line
Linear regression finds the **best straight line** that describes the relationship.
**The equation:**
$$ Y = a + bX $$
Where:
* $Y$ = predicted value
* $a$ = intercept
* $b$ = slope
* $X$ = predictor variable

### 4. Example
Suppose: $Y = 50 + 5X$ (Intercept = 50, Slope = 5).
If $X = 4$ hours studying:
$$ Y = 50 + 5(4) = 70 $$
*Interpretation:* A student studying 4 hours is predicted to score 70.

### 5. Intercept ($a$)
The expected value of $Y$ when $X = 0$. *(Example: When hours = 0, predicted score = 50).*

### 6. Slope ($b$)
How much $Y$ changes when $X$ increases by one unit. *(Example: Every additional study hour increases predicted score by 5 points).*

### 7, 8, 9. Types of Relationships
* **Positive Relationship ($b > 0$):** More advertising → More sales.
* **Negative Relationship ($b < 0$):** More exercise → Lower body fat.
* **No Relationship ($b \approx 0$):** Random scatter.

### 10. How Does Regression Find the Line?
Regression chooses the line that minimizes prediction errors. The errors are called **Residuals**:
$$ \text{Residual} = \text{Actual} - \text{Predicted} $$

### 11. Least Squares Method
Regression minimizes the sum of squared residuals:
$$ \sum (Y - \hat{Y})^2 $$
This is called **Ordinary Least Squares (OLS)**.

### 12. Regression Example
| Hours | Score |
| :--- | :--- |
| 1 | 55 |
| 2 | 60 |
| 3 | 65 |
| 4 | 72 |
| 5 | 78 |

Regression finds: $\text{Score} = 49 + 6X$. 
Prediction for 6 hours: $\text{Score} = 49 + 6(6) = 85$.

### 13. Correlation vs Regression
* **Correlation:** Answers "How strongly are two variables related?" (Range: $-1 \le r \le 1$).
* **Regression:** Answers "Can we predict Y from X?" (e.g., Every extra hour predicts +6 points).

### 14. R² (Coefficient of Determination)
R² measures how much variation in $Y$ is explained by $X$ (Range: $0 \rightarrow 1$). 
*Example:* $R^2 = 0.80$ means 80% of score variation is explained by study hours.

### 15. Assumptions of Linear Regression
1. **Linearity:** Relationship should be approximately straight.
2. **Independence:** Observations should not depend on each other.
3. **Constant Variance:** Residual spread should be similar (Homoscedasticity).
4. **Normality of Residuals:** Errors should approximately follow a normal distribution.

### 16. Real Data Science Example
* **Simple regression:** $\text{Price} = a + b(\text{Area})$
* **Multiple regression:** $\text{Price} = a + b_1(\text{Area}) + b_2(\text{Rooms}) + b_3(\text{Age})$

### 17. Applied R Studio Script
```r
############################################################
# Simple Linear Regression Concept
############################################################

############################################################
# 1. Create Data
############################################################
hours <- c(1, 2, 3, 4, 5, 6, 7, 8)
score <- c(55, 60, 65, 72, 78, 82, 88, 95)
data <- data.frame(hours, score)
data

############################################################
# 2. Visualize Data
############################################################
plot(data$hours, data$score, main="Study Hours vs Exam Score", 
     xlab="Study Hours", ylab="Score")

############################################################
# 3. Build Linear Regression Model
############################################################
model <- lm(score ~ hours, data=data)

############################################################
# 4. View Model Results
############################################################
summary(model)

############################################################
# 5. Extract Coefficients
############################################################
coef(model)

############################################################
# 6. Intercept
############################################################
intercept <- coef(model)[1]
intercept

############################################################
# 7. Slope
############################################################
slope <- coef(model)[2]
slope

############################################################
# 8. Make Prediction
############################################################
new_hours <- data.frame(hours=10)
prediction <- predict(model, newdata=new_hours)
prediction

############################################################
# 9. Add Regression Line
############################################################
plot(data$hours, data$score, main="Linear Regression", 
     xlab="Hours", ylab="Score")
abline(model, lwd=2)

############################################################
# 10. Residuals
############################################################
residuals(model)

############################################################
# 11. R-squared
############################################################
summary(model)$r.squared

############################################################
# 12. Diagnostic Plots
############################################################
par(mfrow=c(2,2))
plot(model)

############################################################
# END
############################################################
```

### 18. Key Takeaway & Summary
```text
X Variable → Find Best Line (Y = a + bX) → a = Starting point, b = Change in Y per 1 unit of X → Prediction + Interpretation
```

| Term | Meaning |
| :--- | :--- |
| **X** | Predictor variable |
| **Y** | Response variable |
| **Intercept** | Value when X = 0 |
| **Slope** | Change in Y for one X unit |
| **Residual** | Actual - Predicted |
| **Least Squares** | Method to find best line |
| **R²** | Explained variation |

**Simple rule:** Linear Regression = Find the best line that predicts Y from X.

***
***

# Part 3: Linearity, Nonlinearity & R-Squared in Linear Regression

## Section A: Linearity and Nonlinearity in Linear Regression
*Script name: Save this file as `32_Linearity_and_Nonlinearity_Linear_Regression.R` or `linearity_nonlinearity_linear_regression.R`*

### 1. Big Picture
One of the most important assumptions of linear regression is: **The relationship between X and Y should be approximately linear.**  
*Meaning:* When X changes, Y changes at a relatively constant rate.  
*Example:* Study hours → Exam score. Every additional hour gives approximately +5 points.

### 2. What Does Linear Mean?
A linear relationship can be represented by:
$$ Y = a + bX $$
The change in Y is constant.  
*Example:* $\text{Score} = 50 + 5(\text{Hours})$

| Hours | Score |
| :--- | :--- |
| 1 | 55 |
| 2 | 60 |
| 3 | 65 |
| 4 | 70 |

Each extra hour: $+5$. The slope stays constant.

### 3. Visual Meaning of Linearity
```text
Y
|          *
|       *
|    *
| *
|________________ X
```
The points follow a straight line.

### 4. Positive Linearity
As X increases, Y increases.  
*Example:* Advertising → Sales
```text
Sales
|          *
|       *
|    *
| *
|________________ Advertising
```
Slope: $b > 0$

### 5. Negative Linearity
As X increases, Y decreases.  
*Example:* Speed → Travel time
```text
Time
| *
|    *
|       *
|          *
|________________ Speed
```
Slope: $b < 0$

### 6. What is Nonlinearity?
A relationship is nonlinear when the rate of change between X and Y is **not constant**.  
*Example:* Exercise and health benefits. At first: Small exercise → Large improvement. Later: More exercise → Smaller improvement. The relationship becomes curved.

### 7. Nonlinear Examples
**Example 1: Quadratic Relationship** ($Y = X^2$)
| X | Y |
| :--- | :--- |
| 1 | 1 |
| 2 | 4 |
| 3 | 9 |
| 4 | 16 |
```text
Y
|        *
|     *
|  *
|*
|____________ X
```

**Example 2: Logarithmic Relationship** ($Y = \log(X)$)
Fast increase at first:
```text
Y
|******
|    *
|      *
|        *
|____________ X
```

**Example 3: Exponential Relationship** ($Y = e^X$)
Slow first, then rapid growth:
```text
Y
|        *
|      *
|   *
| *
|____________ X
```

### 8. Why Does Linearity Matter?
Linear regression assumes:
$$ Y = a + bX + \epsilon $$
*(Where $a$ = intercept, $b$ = slope, $\epsilon$ = error).*  
If the true relationship is curved, regression will force a straight line. This causes:
1. Bad predictions
2. Incorrect conclusions
3. Poor model performance

### 9. Example
*True relationship:* Temperature → Ice Cream Sales.  
At low temperatures: Sales increase slowly. At hot temperatures: Sales increase rapidly. A straight line may miss this pattern.

### 10. How To Detect Nonlinearity
**1. Scatter Plot** (The easiest method)  
Plot X against Y. Look for:
* Straight pattern: ✅ Linear
* Curve pattern: ❌ Nonlinear

**2. Residual Plot**  
$\text{Residual} = \text{Observed} - \text{Predicted}$
* **Good model:** Residuals randomly scattered.
```text
Residual
 *
    *
 *
      *
________________
```
* **Bad model:** Pattern appears (A curve means missing nonlinearity).
```text
Residual
*
 *
  *
   *
  *
 *
________________
```

### 11. What To Do With Nonlinear Data?
* **Option 1: Transform Variables**  
  Example: Log transformation: $Y' = \log(Y)$. Useful for growth data, income, population.
* **Option 2: Add Polynomial Terms**  
  Instead of $Y = a + bX$, use: $Y = a + b_1X + b_2X^2$  
  *Example:* $\text{House price} = a + b_1(\text{area}) + b_2(\text{area}^2)$
* **Option 3: Use Nonlinear Models**  
  Examples: Decision Trees, Random Forest, Neural Networks, Support Vector Machines.

### 12. Linear Model Can Have Nonlinear Features
*Important:* A model can be called "linear regression" even with $X^2$ because it is linear in the **coefficients**.  
Example: $Y = a + b_1X + b_2X^2$ is still a linear regression model.

### 13. Real Data Science Example
*Predicting salary:*  
* Simple model: $\text{Salary} = a + b(\text{Years})$  
* Assumption: Each year adds the same salary increase.  
* Reality: Junior (+10%), Senior (+30%), Manager (+50%). The relationship is nonlinear.  
* Solution: Add $\text{Experience}^2$, Job level, Role category.

**Workflow:**
```text
Collect Data
      |
      ↓
Plot X vs Y
      |
      ↓
Linear Pattern?
      |
  Yes ↓       No
      |        |
Linear Model   Transform/
               Polynomial/
               Nonlinear Model
```

### 14. Applied R Studio Script
```r
############################################################
# Linearity and Nonlinearity in Linear Regression
############################################################

############################################################
# 1. Create Linear Data
############################################################
x_linear <- 1:10
y_linear <- 5 + 3*x_linear + rnorm(10, 0, 2)
linear_data <- data.frame(x=x_linear, y=y_linear)

############################################################
# 2. Scatter Plot Linear Relationship
############################################################
plot(linear_data$x, linear_data$y, main="Linear Relationship", 
     xlab="X", ylab="Y")

############################################################
# 3. Fit Linear Model
############################################################
linear_model <- lm(y ~ x, data=linear_data)
summary(linear_model)

############################################################
# 4. Add Regression Line
############################################################
abline(linear_model, lwd=2)

############################################################
# 5. Residual Plot
############################################################
plot(linear_model$fitted.values, residuals(linear_model), 
     main="Residual Plot", xlab="Predicted", ylab="Residuals")
abline(h=0, lwd=2)

############################################################
# 6. Create Nonlinear Data
############################################################
x_curve <- 1:20
y_curve <- x_curve^2 + rnorm(20, 0, 20)
nonlinear_data <- data.frame(x=x_curve, y=y_curve)

############################################################
# 7. Plot Nonlinear Relationship
############################################################
plot(nonlinear_data$x, nonlinear_data$y, main="Nonlinear Relationship", 
     xlab="X", ylab="Y")

############################################################
# 8. Wrong Linear Model
############################################################
wrong_model <- lm(y ~ x, data=nonlinear_data)
abline(wrong_model, lwd=2)

############################################################
# 9. Polynomial Regression
############################################################
poly_model <- lm(y ~ x + I(x^2), data=nonlinear_data)
summary(poly_model)

############################################################
# 10. Polynomial Prediction Curve
############################################################
x_new <- seq(1, 20, length=100)
pred <- predict(poly_model, newdata=data.frame(x=x_new))
lines(x_new, pred, lwd=2)

############################################################
# 11. Compare Models
############################################################
summary(wrong_model)$r.squared
summary(poly_model)$r.squared

############################################################
# END
############################################################
```

### 15. Key Takeaway & Remember
**Linear Regression assumes:** X → Y relationship is approximately a straight line.  
* **Linear:** $Y = a + bX$  
* **Nonlinear:** Y changes at different rates.  
* **Solutions:** 1. Transform variables, 2. Add polynomial terms, 3. Use nonlinear ML models.

| Pattern | Meaning |
| :--- | :--- |
| Straight line | Linear relationship |
| Curve | Nonlinear relationship |
| Random residuals | Good linear fit |
| Residual pattern | Missing nonlinear structure |

*Simple rule:* Before trusting linear regression, always check the scatter plot and residual plot for nonlinearity.

---

## Section B: R Squared (R²) or Coefficient of Determination
*Script name: Save this file as `33_R_Squared_Coefficient_of_Determination.R` or `r_squared_coefficient_of_determination.R`*

### 1. Big Picture
After building a linear regression model, we ask: *"How well does my model explain the variation in the data?"*  
The answer is: **R² (R Squared)**.  
R² tells us the proportion of variation in Y that is explained by X.  
*Example:* Predicting exam scores using study hours. If $R^2 = 0.80$, it means 80% of the differences in exam scores can be explained by study hours. The remaining $20\%$ comes from other factors (Intelligence, Sleep, Stress, Random error).

### 2. The Idea Behind R²
Suppose we want to predict student scores. The total variation in scores has two parts:
```text
Total Variation
        |
        +----------------+
        |                |
 Explained          Unexplained
 by model           Error
```
R² measures:
$$ R^2 = \frac{\text{Explained Variation}}{\text{Total Variation}} $$

### 3. Formula
$$ \hat{y} = b_0 + b_1x $$
*(Example: $\hat{y} = 8.49 - 0.54x$. $R^2 = 0.72$. $b_0$ = intercept, $b_1$ = slope. Least squares minimizes squared vertical residual gaps).*

The formula:
$$ R^2 = \frac{SSR}{SST} $$
Where:
* **SST (Total Sum of Squares):** Total variation in Y. $\rightarrow SST = \sum(Y - \bar{Y})^2$
* **SSR (Regression Sum of Squares):** Variation explained by the model. $\rightarrow SSR = \sum(\hat{Y} - \bar{Y})^2$
* **SSE (Error Sum of Squares):** Unexplained variation. $\rightarrow SSE = \sum(Y - \hat{Y})^2$

**Relationship:** $SST = SSR + SSE$

### 4. Simple Example
Suppose exam scores: 50, 60, 70, 80, 90. Mean = 70.  
Total variation: $SST = 1000$  
Regression explains: $SSR = 800$  
Then: $R^2 = \frac{800}{1000} = 0.8$  
*Interpretation:* The model explains 80% of score variation.

### 5. Interpretation of R²
* **$R^2 = 1$:** Perfect prediction. All points exactly on the line.
* **$R^2 = 0$:** Model explains nothing. X does not help predict Y.

| R² | Meaning |
| :--- | :--- |
| 0.90 | Very strong explanation |
| 0.70 | Good explanation |
| 0.40 | Moderate |
| 0.10 | Weak |

*Note: The acceptable value depends on the field.*

### 6. R² and Correlation
For simple linear regression:
$$ R^2 = r^2 $$
*(Where $r$ = correlation coefficient, $R^2$ = explained variance).*  
*Example:* Correlation $r = 0.8 \rightarrow R^2 = 0.8^2 = 0.64$. Meaning: 64% of variation is explained.

### 7. Important: R² Does Not Mean Causation
*Example:* Ice cream sales and drowning incidents. They may have $R^2 = 0.85$, but ice cream does not cause drowning. The relationship may be caused by a confounding variable (Hot weather). A high R² means good prediction, not necessarily cause.

### 8. R² in Machine Learning
*Example:* Predict house prices. Features: Area, Bedrooms, Location, Age.  
* Results: Training $R^2 = 0.95$, Testing $R^2 = 0.72$.  
* Meaning: The model explains 72% of unseen price variation.

### 9. Problem with R²
Adding more variables almost always increases R².  
*Example:* Model 1 (Area only) $R^2 = 0.70$. Model 2 (Area + Bedrooms + Random useless feature) $R^2 = 0.73$. The extra variable may not actually help.  
*Solution:* **Adjusted R²** (penalizes unnecessary variables).

### 10. R² vs Adjusted R²
| R² | Adjusted R² |
| :--- | :--- |
| Always increases with variables | Can decrease |
| Simple measure | More reliable for multiple regression |
| Good for simple regression | Better for feature selection |

### 11. Residual Connection
A good regression model has small residuals ($\text{Actual} \approx \text{Predicted}$).  
Therefore:
```text
Small SSE
      ↓
Large R²
```
Bad model: Large errors $\rightarrow$ Small R².

**Workflow:**
```text
Collect Data → Fit Linear Regression → Calculate Predictions 
→ Calculate Errors → Calculate R² → Interpret Explained Variation
```

### 12. Applied R Studio Script
```r
############################################################
# R Squared (Coefficient of Determination)
############################################################

############################################################
# 1. Create Data
############################################################
hours <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
score <- c(50, 55, 60, 65, 72, 75, 82, 85, 90, 95)
data <- data.frame(hours, score)
data

############################################################
# 2. Build Linear Regression Model
############################################################
model <- lm(score ~ hours, data=data)

############################################################
# 3. Model Summary
############################################################
summary(model)

############################################################
# 4. Extract R Squared
############################################################
r_squared <- summary(model)$r.squared
r_squared

############################################################
# 5. Adjusted R Squared
############################################################
adjusted_r_squared <- summary(model)$adj.r.squared
adjusted_r_squared

############################################################
# 6. Predictions
############################################################
predicted <- predict(model)
predicted

############################################################
# 7. Calculate SST
############################################################
SST <- sum((data$score - mean(data$score))^2)
SST

############################################################
# 8. Calculate SSE
############################################################
SSE <- sum((data$score - predicted)^2)
SSE

############################################################
# 9. Calculate SSR
############################################################
SSR <- sum((predicted - mean(data$score))^2)
SSR

############################################################
# 10. Manual R Squared
############################################################
manual_R2 <- SSR / SST
manual_R2

############################################################
# 11. Plot Regression
############################################################
plot(data$hours, data$score, main="Linear Regression and R Squared", 
     xlab="Study Hours", ylab="Exam Score")
abline(model, lwd=2)

############################################################
# 12. Residual Plot
############################################################
plot(predicted, residuals(model), main="Residual Plot", 
     xlab="Predicted Values", ylab="Residuals")
abline(h=0, lwd=2)

############################################################
# END
############################################################
```

### 13. Key Takeaway & Remember
```text
Linear Regression
        X
        |
        ↓
Predict Y
        |
        ↓
Compare: Total Variation
        |
        ↓
Explained + Error
        |
        ↓
R² = Explained Variation / Total Variation
```

| Term | Meaning |
| :--- | :--- |
| **R²** | Percentage of variation explained by model |
| **High R²** | Better explanation of data |
| **Low R²** | Weak prediction |
| **R² = 0** | No explanatory power |
| **R² = 1** | Perfect prediction |
| **Adjusted R²** | Better for multiple regression |

*Simple rule:* R² tells you how much of the movement in Y your model can explain using X.

***