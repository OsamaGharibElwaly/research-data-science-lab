# Part 1: Margin of Error, Bootstrapping & Hypothesis Testing Fundamentals

## 1.1 Margin of Error & Confidence Intervals
Calculates the Margin of Error (ME) and constructs a 95% Confidence Interval for a sample mean, demonstrating how sample size and standard deviation affect precision.

```r
# Margin of Error & 95% Confidence Interval
set.seed(123)
sample_data <- rnorm(100, mean = 170, sd = 10)
n <- length(sample_data)
x_bar <- mean(sample_data)
sigma <- sd(sample_data)
z <- 1.96 # Critical value for 95% CI

ME <- z * (sigma / sqrt(n))
CI_lower <- x_bar - ME
CI_upper <- x_bar + ME

cat(sprintf("Sample Mean: %.2f\n", x_bar))
cat(sprintf("Margin of Error: %.2f\n", ME))
cat(sprintf("95%% CI: (%.2f, %.2f)\n", CI_lower, CI_upper))
```

## 1.2 Sample Size Calculation
Determines the required sample size to achieve a specific target Margin of Error, illustrating the squared relationship between precision and sample size.

```r
# Sample Size Calculation for Target Margin of Error
sigma <- 10       # Population standard deviation estimate
target_ME <- 2    # Desired Margin of Error
z <- 1.96         # 95% Confidence Level

# Formula: n = (z * sigma / ME)^2
n_required <- (z * sigma / target_ME)^2
n_required <- ceiling(n_required) # Always round up to ensure sufficient precision

cat("Required sample size to achieve ME of", target_ME, "is:", n_required, "\n")
```

## 1.3 Bootstrapping for Confidence Intervals
Uses resampling with replacement to empirically estimate the sampling distribution and calculate a non-parametric confidence interval without relying on normality assumptions.

```r
# Bootstrapping for Confidence Intervals
set.seed(123)
sample_data <- c(4000, 4500, 5000, 6000, 7000)
B <- 10000
bootstrap_means <- numeric(B)

for(i in 1:B) {
  # Sample with replacement
  boot_sample <- sample(sample_data, size = length(sample_data), replace = TRUE)
  bootstrap_means[i] <- mean(boot_sample)
}

# Extract the 2.5th and 97.5th percentiles for a 95% CI
CI_boot <- quantile(bootstrap_means, c(0.025, 0.975))
cat("Bootstrap 95% Confidence Interval:\n")
print(CI_boot)
```

## 1.4 Classical One-Sample t-Test
Performs a traditional parametric hypothesis test to determine if a sample mean is significantly different from a hypothesized population value.

```r
# Classical One-Sample t-Test
set.seed(123)
battery_life <- rnorm(30, mean = 9.5, sd = 1.5)

# H0: mu = 10, Ha: mu != 10 (Two-sided test)
t_result <- t.test(battery_life, mu = 10)

cat("t-statistic:", round(t_result$statistic, 3), "\n")
cat("p-value:", round(t_result$p.value, 4), "\n")

if(t_result$p.value < 0.05) {
  cat("Decision: Reject H0 (Significant evidence against null)\n")
} else {
  cat("Decision: Fail to Reject H0\n")
}
```

## 1.5 Bootstrap Hypothesis Testing
Simulates the null hypothesis by shifting the sample data so its mean equals the hypothesized value, then uses resampling to calculate an empirical p-value.

```r
# Bootstrap Hypothesis Testing
set.seed(123)
sample_data <- c(72, 75, 70, 78, 74, 80, 77, 73, 76, 79)
obs_mean <- mean(sample_data)
null_mean <- 70

# Shift data to satisfy H0 (mean = 70)
shifted_data <- sample_data - obs_mean + null_mean 

B <- 10000
boot_means <- numeric(B)
for(i in 1:B) {
  boot_means[i] <- mean(sample(shifted_data, size = length(shifted_data), replace = TRUE))
}

# Calculate p-value
obs_diff <- abs(obs_mean - null_mean)
boot_diff <- abs(boot_means - null_mean)
p_value <- mean(boot_diff >= obs_diff)

cat("Observed Mean:", obs_mean, "| Null Mean:", null_mean, "\n")
cat("Bootstrap p-value:", round(p_value, 4), "\n")
```

---

# Part 2: ANOVA, Sum of Squares & Simple Linear Regression Concept

## 2.1 Calculating Sum of Squares (SST, SSB, SSW)
Manually partitions the total variance into between-group and within-group variations to verify the fundamental ANOVA identity: SST = SSB + SSW.

```r
# Calculating Sum of Squares (SST, SSB, SSW)
group_A <- c(82, 85, 88, 84, 86)
group_B <- c(75, 78, 74, 77, 76)
group_C <- c(90, 92, 91, 89, 93)
scores <- c(group_A, group_B, group_C)
groups <- factor(rep(c("A", "B", "C"), each = 5))
data <- data.frame(Group = groups, Score = scores)

grand_mean <- mean(data$Score)
SST <- sum((data$Score - grand_mean)^2)
SSW <- sum(ave(data$Score, data$Group, FUN = function(x) sum((x - mean(x))^2)))
SSB <- SST - SSW # Alternatively, calculate directly from group means

cat("Total Variation (SST):", SST, "\n")
cat("Between-Group (SSB):", SSB, "| Within-Group (SSW):", SSW, "\n")
```

## 2.2 One-Way ANOVA Execution
Uses the `aov()` function to compute the F-statistic and p-value, determining if at least one group mean is statistically different from the others.

```r
# One-Way ANOVA Execution
anova_model <- aov(Score ~ Group, data = data)
anova_table <- summary(anova_model)

print(anova_table)

f_value <- anova_table[[1]]$`F value`[1]
p_value <- anova_table[[1]]$`Pr(>F)`[1]
cat("\nF-statistic:", round(f_value, 2), "| p-value:", round(p_value, 4), "\n")
```

## 2.3 Post-Hoc Analysis & Group Means
Calculates group means, visualizes the distributions using boxplots, and applies Tukey's HSD to identify exactly which groups differ from one another.

```r
# Post-Hoc Analysis & Group Means
group_means <- aggregate(Score ~ Group, data = data, FUN = mean)
print(group_means)

# Visualize distributions
boxplot(Score ~ Group, data = data, main = "ANOVA Group Comparison",
        xlab = "Group", ylab = "Score", col = c("lightblue", "lightgreen", "lightpink"))

# Tukey HSD for pairwise comparisons
tukey_results <- TukeyHSD(anova_model)
print(tukey_results$Group)
```

## 2.4 Simple Linear Regression Fitting
Fits an Ordinary Least Squares (OLS) regression line to predict a continuous outcome (Y) based on a single predictor (X), extracting the intercept and slope.

```r
# Simple Linear Regression Fitting
hours <- c(1, 2, 3, 4, 5, 6, 7, 8)
score <- c(55, 60, 65, 72, 78, 82, 88, 95)
data_reg <- data.frame(hours, score)

model <- lm(score ~ hours, data = data_reg)
coefficients <- coef(model)

cat("Regression Equation: Score =", round(coefficients[1], 2), "+", 
    round(coefficients[2], 2), "* Hours\n")
cat("Intercept (a):", round(coefficients[1], 2), "\n")
cat("Slope (b):", round(coefficients[2], 2), "\n")
```

## 2.5 Regression Predictions & Visualization
Uses the fitted model to predict outcomes for new data points and overlays the regression line on a scatter plot of the original data.

```r
# Regression Predictions & Visualization
# Predict score for 10 hours of study
new_data <- data.frame(hours = 10)
predicted_score <- predict(model, newdata = new_data)
cat("Predicted score for 10 hours:", round(predicted_score, 2), "\n")

# Plot data and regression line
plot(data_reg$hours, data_reg$score, main = "Simple Linear Regression",
     xlab = "Study Hours", ylab = "Exam Score", pch = 19, col = "blue")
abline(model, lwd = 2, col = "red")
```

---

# Part 3: Linearity, Nonlinearity & R-Squared in Linear Regression

## 3.1 Detecting Nonlinearity via Residuals
Generates a residual plot to check for systematic patterns. A curved pattern in the residuals indicates that a simple linear model is missing nonlinear structure.

```r
# Detecting Nonlinearity via Residuals
set.seed(123)
x_curve <- 1:20
y_curve <- x_curve^2 + rnorm(20, 0, 20)
data_nl <- data.frame(x = x_curve, y = y_curve)

# Fit a wrong linear model to nonlinear data
wrong_model <- lm(y ~ x, data = data_nl)

# Residual plot to check for patterns
plot(wrong_model$fitted.values, residuals(wrong_model), 
     main = "Residual Plot (Nonlinear Data)",
     xlab = "Fitted Values", ylab = "Residuals", pch = 19, col = "darkred")
abline(h = 0, lwd = 2, col = "blue")
```

## 3.2 Polynomial Regression for Curves
Addresses nonlinearity by adding a squared term (`I(x^2)`) to the model, allowing the regression line to bend and capture quadratic relationships.

```r
# Polynomial Regression for Curves
# Adding a squared term to capture the curve
poly_model <- lm(y ~ x + I(x^2), data = data_nl)

# Generate smooth curve for plotting
x_new <- seq(1, 20, length.out = 100)
preds <- predict(poly_model, newdata = data.frame(x = x_new))

plot(data_nl$x, data_nl$y, main = "Polynomial Regression",
     xlab = "X", ylab = "Y", pch = 19, col = "gray")
lines(x_new, preds, lwd = 2, col = "blue")
```

## 3.3 Log Transformation for Skewed Data
Applies a natural log transformation to the dependent variable to linearize an exponential relationship, satisfying the linearity assumption of OLS.

```r
# Log Transformation for Skewed Data
set.seed(123)
x_exp <- 1:50
y_exp <- exp(0.1 * x_exp) + rnorm(50, 0, 5)
data_log <- data.frame(x = x_exp, y = y_exp)

# Transform Y using natural log to linearize exponential growth
log_model <- lm(log(y) ~ x, data = data_log)

# Plot on a log-scale Y axis to visualize the linearized relationship
plot(data_log$x, data_log$y, log = "y", main = "Log-Linear Relationship",
     xlab = "X", ylab = "Y (log scale)", pch = 19, col = "darkgreen")
# Overlay the exponential prediction curve
lines(data_log$x, exp(predict(log_model)), lwd = 2, col = "red")
```

## 3.4 Manual R-Squared Calculation
Manually computes the Total Sum of Squares (SST), Error Sum of Squares (SSE), and Regression Sum of Squares (SSR) to verify the R² formula: SSR / SST.

```r
# Manual R-Squared Calculation
hours <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
score <- c(50, 55, 60, 65, 72, 75, 82, 85, 90, 95)
data_r2 <- data.frame(hours, score)

model_r2 <- lm(score ~ hours, data = data_r2)
predicted <- predict(model_r2)
y_bar <- mean(data_r2$score)

SST <- sum((data_r2$score - y_bar)^2)       # Total Variation
SSE <- sum((data_r2$score - predicted)^2)   # Unexplained Variation
SSR <- sum((predicted - y_bar)^2)           # Explained Variation

manual_R2 <- SSR / SST
cat("Manual R-squared:", round(manual_R2, 4), "\n")
cat("R-squared from summary:", round(summary(model_r2)$r.squared, 4), "\n")
```

## 3.5 Adjusted R-Squared & Model Comparison
Demonstrates how Adjusted R² penalizes the addition of useless predictors, making it a more reliable metric than standard R² for comparing multiple regression models.

```r
# Adjusted R-Squared & Model Comparison
set.seed(123)
n <- 100
area <- rnorm(n, 1500, 200)
useless_feature <- rnorm(n) # Random noise
price <- 100000 + 50 * area + rnorm(n, 0, 10000)
data_adj <- data.frame(price, area, useless_feature)

# Model 1: Only Area
model1 <- lm(price ~ area, data = data_adj)
# Model 2: Area + Useless Feature
model2 <- lm(price ~ area + useless_feature, data = data_adj)

cat("Model 1 (Area only):\n")
cat("  R²:", round(summary(model1)$r.squared, 4), "| Adj R²:", round(summary(model1)$adj.r.squared, 4), "\n\n")

cat("Model 2 (Area + Noise):\n")
cat("  R²:", round(summary(model2)$r.squared, 4), "| Adj R²:", round(summary(model2)$adj.r.squared, 4), "\n")
cat("\nNote: R² increased, but Adjusted R² decreased due to the penalty for the useless feature.\n")
