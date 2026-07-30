# Data Science Statistics R Scripts Guide

## Part 1: Margin of Error, Bootstrapping & Hypothesis Testing Fundamentals

### 1.1 Bootstrap Hypothesis Testing
A non-parametric method that uses resampling with replacement to estimate the sampling distribution and calculate p-values, bypassing the need for theoretical distributions like the t-distribution.

```r
############################################################
# Bootstrap Hypothesis Testing
# Script: 21_Bootstrap_Hypothesis_Testing.R
############################################################
set.seed(123)

# 1. Create Sample Data
sample_data <- c(72, 75, 70, 78, 74, 80, 77, 73, 76, 79)

# 2. Observed Mean
observed_mean <- mean(sample_data)

# 3. Define Null Hypothesis
null_mean <- 70

# 4. Shift Data Under H0
shifted_data <- sample_data - observed_mean + null_mean

# 5. Bootstrap Resampling
B <- 10000
bootstrap_means <- numeric(B)
n <- length(shifted_data)

for(i in 1:B){
  bootstrap_sample <- sample(shifted_data, size = n, replace = TRUE)
  bootstrap_means[i] <- mean(bootstrap_sample)
}

# 6. Plot Bootstrap Distribution
hist(bootstrap_means, breaks = 30, 
     main = "Bootstrap Distribution Under H0", 
     xlab = "Bootstrap Means")
abline(v = observed_mean, lwd = 2, col = "red")

# 7. Bootstrap p-value
observed_difference <- abs(observed_mean - null_mean)
bootstrap_difference <- abs(bootstrap_means - null_mean)
p_value <- mean(bootstrap_difference >= observed_difference)

# 8. Decision
alpha <- 0.05
if(p_value < alpha){
  cat("Reject H0\n")
} else {
  cat("Fail to Reject H0\n")
}

# 9. Compare with Classical t-test
t.test(sample_data, mu = null_mean)

# 10. Confidence Interval Using Bootstrap
bootstrap_original <- numeric(B)
for(i in 1:B){
  bootstrap_sample <- sample(sample_data, size = n, replace = TRUE)
  bootstrap_original[i] <- mean(bootstrap_sample)
}
quantile(bootstrap_original, c(0.025, 0.975))
```

---

## Part 2: ANOVA, Sum of Squares & Simple Linear Regression Concept

### 2.1 ANOVA and Sum of Squares
ANOVA compares the means of three or more groups by partitioning the total variability (SST) into between-group (SSB) and within-group (SSW) variation to calculate the F-statistic.

```r
############################################################
# ANOVA and Sum of Squares
# Script: 25_ANOVA_Sum_of_Squares.R
############################################################

# 1. Create Three Groups
group_A <- c(82, 85, 88, 84, 86)
group_B <- c(75, 78, 74, 77, 76)
group_C <- c(90, 92, 91, 89, 93)

# 2. Combine Data
scores <- c(group_A, group_B, group_C)
groups <- factor(c(rep("A", length(group_A)),
                   rep("B", length(group_B)),
                   rep("C", length(group_C))))
data <- data.frame(Group = groups, Score = scores)

# 3. Grand Mean
grand_mean <- mean(data$Score)

# 4. Total Sum of Squares (SST)
SST <- sum((data$Score - grand_mean)^2)

# 5. Within-Group Sum of Squares (SSW)
SSW <- sum(ave(data$Score, data$Group, FUN = function(x) (x - mean(x))^2))

# 6. Between-Group Sum of Squares (SSB)
SSB <- SST - SSW

# 7. Verify Relationship: SST = SSB + SSW
SST
SSB + SSW

# 8. Perform ANOVA
anova_model <- aov(Score ~ Group, data = data)
summary(anova_model)

# 9. Extract ANOVA Table Components
anova_table <- summary(anova_model)[[1]]
anova_table$`Sum Sq`
anova_table$`Mean Sq`
anova_table$`F value`
anova_table$`Pr(>F)`

# 10. Boxplot & Compare Group Means
boxplot(Score ~ Group, data = data, main = "ANOVA Example", 
        xlab = "Group", ylab = "Score")
aggregate(Score ~ Group, data = data, mean)
```

### 2.2 Simple Linear Regression Concept
Models the relationship between a predictor (X) and a response (Y) using the equation Y = a + bX, finding the best-fit line by minimizing the sum of squared residuals (Ordinary Least Squares).

```r
############################################################
# Simple Linear Regression Concept
# Script: 31_Simple_Linear_Regression_Concept.R
############################################################

# 1. Create Data
hours <- c(1, 2, 3, 4, 5, 6, 7, 8)
score <- c(55, 60, 65, 72, 78, 82, 88, 95)
data <- data.frame(hours, score)

# 2. Visualize Data
plot(data$hours, data$score, main = "Study Hours vs Exam Score",
     xlab = "Study Hours", ylab = "Score")

# 3. Build Linear Regression Model
model <- lm(score ~ hours, data = data)
summary(model)

# 4. Extract Coefficients (Intercept & Slope)
coef(model)
intercept <- coef(model)[1]
slope <- coef(model)[2]

# 5. Make Prediction
new_hours <- data.frame(hours = 10)
prediction <- predict(model, newdata = new_hours)

# 6. Add Regression Line & View Diagnostics
plot(data$hours, data$score, main = "Linear Regression",
     xlab = "Hours", ylab = "Score")
abline(model, lwd = 2, col = "blue")

# 7. Residuals & R-squared
residuals(model)
summary(model)$r.squared

# 8. Diagnostic Plots
par(mfrow = c(2, 2))
plot(model)
par(mfrow = c(1, 1)) # Reset plot layout
```

---

## Part 3: Linearity, Nonlinearity & R-Squared in Linear Regression

### 3.1 Linearity and Nonlinearity
Evaluates whether the X-Y relationship is a straight line. If nonlinear patterns are detected via scatter or residual plots, solutions include variable transformations, adding polynomial terms, or using non-linear ML models.

```r
############################################################
# Linearity and Nonlinearity in Linear Regression
# Script: 32_Linearity_and_Nonlinearity_Linear_Regression.R
############################################################

# 1. Create & Plot Linear Data
x_linear <- 1:10
y_linear <- 5 + 3*x_linear + rnorm(10, 0, 2)
linear_data <- data.frame(x = x_linear, y = y_linear)

plot(linear_data$x, linear_data$y, main = "Linear Relationship", 
     xlab = "X", ylab = "Y")
linear_model <- lm(y ~ x, data = linear_data)
abline(linear_model, lwd = 2)

# 2. Residual Plot for Linear Model
plot(linear_model$fitted.values, residuals(linear_model), 
     main = "Residual Plot", xlab = "Predicted", ylab = "Residuals")
abline(h = 0, lwd = 2)

# 3. Create & Plot Nonlinear Data
x_curve <- 1:20
y_curve <- x_curve^2 + rnorm(20, 0, 20)
nonlinear_data <- data.frame(x = x_curve, y = y_curve)

plot(nonlinear_data$x, nonlinear_data$y, main = "Nonlinear Relationship", 
     xlab = "X", ylab = "Y")

# 4. Fit Wrong Linear Model vs Correct Polynomial Model
wrong_model <- lm(y ~ x, data = nonlinear_data)
abline(wrong_model, lwd = 2, col = "red")

poly_model <- lm(y ~ x + I(x^2), data = nonlinear_data)

# 5. Polynomial Prediction Curve
x_new <- seq(1, 20, length = 100)
pred <- predict(poly_model, newdata = data.frame(x = x_new))
lines(x_new, pred, lwd = 2, col = "blue")

# 6. Compare Models (R-squared)
summary(wrong_model)$r.squared
summary(poly_model)$r.squared
```

### 3.2 R Squared (Coefficient of Determination)
Measures the proportion of variance in the dependent variable (Y) that is predictable from the independent variable(s) (X), calculated as SSR/SST, with Adjusted R² penalizing unnecessary predictors.

```r
############################################################
# R Squared (Coefficient of Determination)
# Script: 33_R_Squared_Coefficient_of_Determination.R
############################################################

# 1. Create Data
hours <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
score <- c(50, 55, 60, 65, 72, 75, 82, 85, 90, 95)
data <- data.frame(hours, score)

# 2. Build Model & Extract Standard R-squared
model <- lm(score ~ hours, data = data)
summary(model)

r_squared <- summary(model)$r.squared
adjusted_r_squared <- summary(model)$adj.r.squared

# 3. Manual Calculation of SST, SSE, SSR
predicted <- predict(model)

SST <- sum((data$score - mean(data$score))^2) # Total Variation
SSE <- sum((data$score - predicted)^2)        # Unexplained Variation
SSR <- sum((predicted - mean(data$score))^2)  # Explained Variation

manual_R2 <- SSR / SST

# 4. Plot Regression Line
plot(data$hours, data$score, main = "Linear Regression and R Squared",
     xlab = "Study Hours", ylab = "Exam Score")
abline(model, lwd = 2, col = "blue")

# 5. Residual Plot
plot(predicted, residuals(model), main = "Residual Plot",
     xlab = "Predicted Values", ylab = "Residuals")
abline(h = 0, lwd = 2)
