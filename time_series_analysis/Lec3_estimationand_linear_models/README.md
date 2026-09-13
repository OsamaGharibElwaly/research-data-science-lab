# Lecture 3 — Time Series Analysis

## Overview

This lecture develops the main statistical tools for understanding **dependence in time series data**.

The main topics are:

1. Weak stationarity revisited
2. Autocovariance
3. Autocorrelation
4. Estimating autocovariance and autocorrelation
5. Cross-covariance and cross-correlation
6. Interpreting the ACF
7. Detecting white noise
8. Approximate confidence bounds for the ACF
9. Backshift operator
10. Difference operator
11. Time-series models vs. linear regression
12. Removing deterministic trends
13. Stationarity testing with the Augmented Dickey-Fuller test
14. Real-world analysis of U.S. prescription drug prices in R

The central idea is:

> **Autocorrelation allows us to detect and understand temporal dependence in a time series.**

---

# 1. Weak Stationarity

A stochastic process \(X_t\) is **weakly stationary** if its important statistical properties do not change when we shift the process through time.

The two key requirements are:

### Constant mean

$$
E[X_t] = \mu
$$

The expected value does not depend on \(t\).

### Time-shift invariant autocovariance

$$
Cov(X_s,X_t)
=
Cov(X_{s+r},X_{t+r})
$$

for any appropriate time shift \(r\).

This means that covariance depends on the **distance between observations**, rather than their absolute positions in time.

For a stationary process, we can therefore write:

$$
\gamma(h) = Cov(X_t,X_{t+h})
$$

where \(h\) is called the **lag**.

---

# 2. Why Stationarity Matters

Suppose the mean of a process is:

* approximately 0 at the beginning
* approximately 20 near the end

Then using all observations to estimate one global mean would not make much sense.

If the process is stationary, however, all observations provide information about the same underlying mean.

The same idea applies to covariance.

If observations separated by one month have a particular covariance at the beginning of the series, stationarity assumes that observations separated by one month have the same covariance later in the series.

This makes it possible to estimate temporal dependence using the entire dataset.

---

# 3. Sample Mean

For \(T\) observations, the sample mean is

$$
\bar X =
\frac{1}{T}
\sum_{t=1}^{T}X_t
$$

For a stationary process, this provides an estimator of the process mean.

However, unlike independent observations, time-series observations can be dependent.

Therefore, the variance of the sample mean is affected by autocovariance.

This dependence is one of the fundamental differences between ordinary independent-data statistics and time-series statistics.

---

# 4. Autocovariance

For a stationary process, the autocovariance function is

$$
\gamma(h)
=
Cov(X_t,X_{t+h})
$$

where:

* \(h\) = lag
* \(X_t\) = observation at time \(t\)
* \(X_{t+h}\) = observation \(h\) time units later

### Interpretation

Autocovariance tells us how strongly observations separated by \(h\) time units vary together.

For example:

* \(h=0\): observation compared with itself
* \(h=1\): current observation compared with one previous/next observation
* \(h=2\): observations two time units apart
* \(h=12\): observations one year apart for monthly data

For \(h=0\):

$$
\gamma(0)
=
Cov(X_t,X_t)
=
Var(X_t)
$$

So the autocovariance at lag zero is simply the variance.

---

# 5. Estimating Autocovariance

Given \(T\) observations, the estimated autocovariance at lag \(h\) is

$$
\hat{\gamma}(h)
=
\frac{1}{T}
\sum_{t=1}^{T-h}
(X_{t+h}-\bar X)(X_t-\bar X)
$$

The important details are:

* the observations are separated by \(h\)
* the sample mean is removed
* the sum only goes to \(T-h\)
* the estimator divides by \(T\)

---

## Why Does the Number of Terms Decrease?

At lag \(h\), there are only

$$
T-h
$$

valid pairs.

For example, if:

$$
T=100
$$

then:

| Lag | Number of pairs |
| --: | --------------: |
|   0 |             100 |
|   1 |              99 |
|   2 |              98 |
|  10 |              90 |
|  50 |              50 |
|  90 |              10 |

Therefore, estimates at large lags are generally based on fewer observations and can be less reliable.

In practice, we usually focus on relatively small lags.

---

# 6. Autocorrelation

Autocorrelation standardizes autocovariance.

The theoretical autocorrelation function (ACF) is

$$
\rho(h)
=
\frac{\gamma(h)}
{\gamma(0)}
$$

because

$$
\gamma(0)=Var(X_t)
$$

Therefore:

$$
-1 \leq \rho(h) \leq 1
$$

The estimated ACF is

$$
\hat{\rho}(h)
=
\frac{\hat{\gamma}(h)}
{\hat{\gamma}(0)}
$$

### Important property

At lag zero:

$$
\hat{\rho}(0)=1
$$

because

$$
\frac{\hat{\gamma}(0)}
{\hat{\gamma}(0)}
=1
$$

---

# 7. Autocorrelation Intuition

The ACF answers:

> **How similar is the series to itself after shifting it by \(h\) time units?**

For example:

### Strong positive autocorrelation

If

$$
\rho(1) \approx 0.9
$$

then consecutive observations tend to move together.

### Negative autocorrelation

If

$$
\rho(1) \approx -0.8
$$

then high observations tend to be followed by low observations, and vice versa.

### Near-zero autocorrelation

If

$$
\rho(h) \approx 0
$$

then there is little linear dependence at lag \(h\).

---

# 8. Symmetry of the ACF

The autocovariance and autocorrelation functions are symmetric:

$$
\gamma(-h)=\gamma(h)
$$

and

$$
\rho(-h)=\rho(h)
$$

Therefore, when plotting the ACF, we usually only need to examine **positive lags**.

---

# 9. Cross-Covariance

When we have two stationary processes \(X_t\) and \(Y_t\), we can study their relationship using cross-covariance.

At lag \(h\):

$$
\gamma_{XY}(h)
=
Cov(X_{t+h},Y_t)
$$

A sample estimator is approximately

$$
\hat{\gamma}_{XY}(h)
=
\frac{1}{T}
\sum_{t=1}^{T-h}
(X_{t+h}-\bar X)
(Y_t-\bar Y)
$$

This measures the relationship between one series and another series at different time offsets.

---

# 10. Cross-Correlation

Cross-correlation standardizes cross-covariance:

$$
\rho_{XY}(h)
=
\frac{
\gamma_{XY}(h)
}{
\sqrt{\gamma_X(0)\gamma_Y(0)}
}
$$

The estimated version is

$$
\hat{\rho}_{XY}(h)
=
\frac{
\hat{\gamma}_{XY}(h)
}{
\sqrt{
\hat{\gamma}_X(0)
\hat{\gamma}_Y(0)
}
}
$$

This is useful when trying to determine whether changes in one time series are associated with changes in another at different lags.

---

# 11. ACF in R

R provides the `acf()` function for estimating and plotting the autocorrelation function.

```r
acf(x)
```

You can control the maximum lag:

```r
acf(x, lag.max = 24)
```

For monthly data, `lag.max = 24` lets us inspect approximately two years of lagged relationships.

---

# 12. Understanding an ACF Plot

An ACF plot usually contains:

* lag on the horizontal axis
* estimated autocorrelation on the vertical axis
* a large spike at lag 0
* approximate confidence bounds

The lag-0 value should always be:

$$
\rho(0)=1
$$

The interesting information is therefore in the remaining lags.

---

# 13. White Noise

A white-noise process has no temporal correlation.

For white noise:

$$
\rho(h)=0
$$

for all

$$
h\neq0
$$

while

$$
\rho(0)=1
$$

Therefore, its ACF should look approximately like:

```text
ACF
 1 | *
   |
 0 | . . . . . . . . . .
   +----------------------
     0 1 2 3 4 5 6 7 ...
```

Small random spikes around zero are expected because we are estimating the ACF from finite data.

---

# 14. White Noise Example in R

Generate Gaussian white noise:

```r
set.seed(42)

wn <- rnorm(100)

plot.ts(wn)

acf(wn)
```

Because the observations are independent:

```text
ACF ≈ 0
```

for positive lags.

The exact sample ACF will not be zero because the dataset is finite.

---

# 15. Random Walk and ACF

A random walk can be written as:

$$
X_t=X_{t-1}+W_t
$$

where \(W_t\) is white noise.

A random walk is **not stationary**.

Its ACF can show very strong positive autocorrelation over many lags.

```r
set.seed(42)

wn <- rnorm(100)

random_walk <- cumsum(wn)

plot.ts(random_walk)

acf(random_walk)
```

The ACF typically decreases slowly and remains strongly positive across many lags.

This can be a warning sign of **non-stationarity**.

---

# 16. Moving Average Process and ACF

Consider a moving-average process of order 9:

$$
X_t
=
\frac{1}{9}
\sum_{i=0}^{8}W_{t-i}
$$

where \(W_t\) is white noise.

The ACF of an MA(9) process has a characteristic cutoff.

It tends to decline toward zero and becomes approximately zero after lag 9.

This provides an important modeling intuition:

> **An MA(q) process has an ACF that cuts off after approximately lag \(q\).**

This becomes useful later when identifying ARMA/ARIMA models.

---

# 17. AR Processes and ACF

An autoregressive process has a different ACF pattern.

For example, an AR(2) model can be written as:

$$
X_t
=
\phi_1X_{t-1}
+
\phi_2X_{t-2}
+
W_t
$$

For a stationary AR process, the ACF generally decreases gradually rather than cutting off sharply.

The decrease may look approximately geometric or exponential.

### Important intuition

| Process     | Typical ACF behavior              |
| ----------- | --------------------------------- |
| White noise | Approximately zero after lag 0    |
| Random walk | Very strong, slowly declining ACF |
| MA(q)       | ACF cuts off after \(q\)          |
| AR(p)       | ACF gradually decays              |
| ARMA        | More complicated combination      |

These are useful **diagnostic patterns**, not absolute rules.

---

# 18. Why ACF Is Important

The ACF is one of the most useful exploratory tools in time-series analysis.

It can help us investigate:

* stationarity
* temporal dependence
* white noise
* seasonality
* possible MA structure
* possible AR structure
* model residuals

Time-series analysis is not simply:

> collect data → run statistical test → get answer

Instead, exploratory analysis is extremely important.

We often ask:

> What structure is present in the data?

before deciding which model to use.

---

# 19. Why Divide by \(T\) Instead of \(T-h\)?

The autocovariance estimator is written as:

$$
\hat{\gamma}(h)
=
\frac{1}{T}
\sum_{t=1}^{T-h}
(X_{t+h}-\bar X)(X_t-\bar X)
$$

even though there are \(T-h\) terms.

This choice is useful because it gives the estimator an important mathematical property:

> **Positive definiteness.**

Covariance matrices need to be positive semidefinite/positive definite in the appropriate sense.

The \(1/T\) normalization helps ensure that the estimated autocovariance sequence has the appropriate covariance structure.

---

# 20. Detecting White Noise

Suppose \(W_t\) is white noise.

For positive lags:

$$
\rho_W(h)=0
$$

Therefore, we expect:

$$
\hat{\rho}_W(h)
\approx0
$$

However, with finite data, the estimate will not be exactly zero.

The question becomes:

> How far away from zero should we expect the estimated ACF to be?

---

# 21. Variance of the Estimated ACF

For white noise, approximately:

$$
E[\hat{\rho}(h)]\approx0
$$

and

$$
Var[\hat{\rho}(h)]
\approx
\frac{1}{T}
$$

for nonzero lags under the assumptions discussed in the lecture.

Therefore:

$$
SD[\hat{\rho}(h)]
\approx
\frac{1}{\sqrt{T}}
$$

---

# 22. Approximate ACF Confidence Bounds

Using approximately two standard deviations gives:

$$
\pm
\frac{2}{\sqrt{T}}
$$

These are the approximate blue dotted lines commonly displayed by R's `acf()` plot.

For example, if:

$$
T=100
$$

then:

$$
\frac{2}{\sqrt{100}}
=
0.2
$$

So we expect most white-noise ACF estimates to fall roughly between:

$$
-0.2
\quad\text{and}\quad
0.2
$$

---

# 23. Important Warning About ACF Bounds

The ACF bounds are a **rough diagnostic**, not a complete white-noise hypothesis test.

A single spike slightly outside the bounds does not automatically mean:

> "This is definitely not white noise."

The bounds are useful for visual exploration.

Formal tests for white noise can be introduced separately, such as the **Ljung-Box test**.

---

# 24. Backshift Operator

The next part of the lecture introduces notation that makes time-series models easier to write.

The **backshift operator** is denoted by:

$$
B
$$

and is defined by:

$$
BX_t=X_{t-1}
$$

Applying it twice:

$$
B^2X_t=X_{t-2}
$$

More generally:

$$
B^kX_t=X_{t-k}
$$

The backshift operator simply moves a time series backward in time.

---

# 25. Forward Shift

The inverse of the backshift operator is the forward-shift operator:

$$
B^{-1}X_t=X_{t+1}
$$

Therefore:

$$
BB^{-1}=B^{-1}B=I
$$

where \(I\) is the identity operator.

---

# 26. Difference Operator

The first difference measures the change between consecutive observations.

Define:

$$
\Delta X_t
=
X_t-X_{t-1}
$$

Using the backshift operator:

$$
\Delta X_t
=
(1-B)X_t
$$

This is extremely important in time-series analysis.

---

# 27. Why Differencing Is Useful

Suppose a series contains a trend:

```text
      /
     /
    /
   /
  /
 /
/
```

The raw series may be non-stationary.

Taking first differences:

$$
\Delta X_t=X_t-X_{t-1}
$$

removes much of the trend.

For example:

```text
Original:
100, 103, 106, 109, 112

First difference:
3, 3, 3, 3
```

Differencing converts levels into changes.

This becomes a central idea in ARIMA models.

---

# 28. Higher-Order Differences

The second difference is:

$$
\Delta^2X_t
=
\Delta(\Delta X_t)
$$

Using the backshift operator:

$$
\Delta^2
=
(1-B)^2
$$

Expanding:

$$
(1-B)^2
=
1-2B+B^2
$$

Therefore:

$$
\Delta^2X_t
=
X_t-2X_{t-1}+X_{t-2}
$$

---

# 29. General \(k\)-th Difference

The \(k\)-th difference can be represented as:

$$
\Delta^kX_t
=
(1-B)^kX_t
$$

Using the binomial theorem:

$$
(1-B)^k
=
\sum_{i=0}^{k}
(-1)^i
\binom{k}{i}
B^i
$$

Therefore:

$$
\Delta^kX_t
=
\sum_{i=0}^{k}
(-1)^i
\binom{k}{i}
X_{t-i}
$$

The lecture also briefly mentions **fractional differencing**, where \(k\) can be generalized beyond positive integers. This idea is important in advanced models but is not required for the current course section.

---

# 30. Time-Series Models vs. Linear Regression

Consider a standard linear regression model:

$$
X_t
=
\beta_0
+
\beta_1Z_{t1}
+\cdots+
\beta_pZ_{tp}
+
\epsilon_t
$$

where the errors are typically assumed to be independent or at least uncorrelated under the standard regression framework.

In matrix notation:

$$
X=Z\beta+\epsilon
$$

The ordinary least-squares estimator is:

$$
\hat{\beta}
=
(Z^TZ)^{-1}Z^TX
$$

---

# 31. The Difference in Time-Series Modeling

A time-series model can instead be written as:

$$
X_t
=
\beta_0
+
\beta_1Z_{t1}
+\cdots+
\beta_pZ_{tp}
+
Y_t
$$

where \(Y_t\) is a **stationary stochastic process**.

The important difference is:

$$
Y_t
$$

does not necessarily represent independent white noise.

It could contain temporal dependence.

For example, \(Y_t\) could be:

* AR
* MA
* ARMA
* another stationary stochastic process

Therefore, the errors themselves may have a time-series structure.

---

# 32. Why Residual Dependence Matters

Suppose we fit:

$$
X_t=Z_t\beta+Y_t
$$

and obtain residuals:

$$
R_t=X_t-\hat X_t
$$

If the residuals contain autocorrelation, then there is still temporal structure that our model has not explained.

This is why residuals should be analyzed as a time series.

A good time-series model should generally leave residuals that resemble uncorrelated noise.

---

# 33. Real Data: Prescription Drug Prices

The lecture uses monthly U.S. prescription drug price data.

The dataset contains monthly average prescription drug prices over several years, beginning around 1986.

The series shows a clear upward trend.

Conceptually:

```text
Price
  |
  |                         /
  |                     ___/
  |                 ___/
  |             ___/
  |         ___/
  |_____ ___/
  +------------------------> Time
```

The first question is:

> Is the original series stationary?

The visual answer is clearly no in the mean because the average level changes over time.

---

# 34. Loading Time-Series Data in R

The lecture uses several R time-series packages.

```r
library(tsa)
library(tseries)
library(forecast)
```

The exact package requirements may depend on the version of the original course materials.

---

# 35. Exploring a Time-Series Object

Suppose the prescription data is stored as:

```r
prescript
```

Plot it:

```r
plot(prescript)
```

Inspect its time index:

```r
time(prescript)
```

A monthly time-series object contains information about:

* starting period
* ending period
* frequency
* time index

For monthly data:

$$
frequency = 12
$$

---

# 36. First Visual Analysis

Plot the prescription series:

```r
plot(
  prescript,
  main = "Prescription Drug Prices",
  ylab = "Price",
  xlab = "Time"
)
```

The series has an increasing trend.

Therefore:

$$
E[X_t]
$$

does not appear constant.

This is evidence against stationarity.

---

# 37. Fit a Linear Trend

We can model the deterministic trend using time:

```r
model1 <- lm(
  prescript ~ time(prescript)
)

summary(model1)
```

Conceptually:

$$
X_t
=
\beta_0+\beta_1t+Y_t
$$

where:

* \(\beta_0\) = intercept
* \(\beta_1\) = trend/slope
* \(Y_t\) = remaining stochastic component

---

# 38. Plot the Linear Trend

First plot the original series:

```r
plot(prescript)
```

Then add the fitted regression line:

```r
abline(
  model1,
  lty = 2
)
```

This allows us to visually compare the observed data with the estimated deterministic trend.

---

# 39. Interpreting the Slope

The lecture's fitted model produces a positive coefficient for time.

The approximate interpretation is:

> Prescription prices increase by roughly a few dollars per month on average over the observed period.

The exact numerical interpretation depends on the actual version of the dataset and its units.

The important methodological idea is:

$$
\text{Observed series}
=
\text{trend}
+
\text{stationary component}
$$

---

# 40. Residuals After Removing the Trend

The residuals are:

```r
residuals1 <- residuals(model1)
```

or:

```r
residuals1 <- prescript -
  fitted(model1)
```

Plot them:

```r
plot.ts(residuals1)

abline(
  h = 0,
  lty = 2
)
```

The goal is to determine whether the remaining process looks stationary.

---

# 41. Why We Cannot Immediately Interpret the Original ACF

We can technically calculate:

```r
acf(prescript)
```

but the original series is non-stationary.

Therefore, the resulting ACF can be misleading.

This demonstrates an important principle:

> **Being able to calculate a statistic does not mean that the statistic is meaningful for the process.**

We should first understand the properties of the series.

---

# 42. ACF of the Detrended Series

After removing the linear trend:

```r
acf(
  residuals1,
  lag.max = 24
)
```

The ACF can reveal additional structure.

In this example, the ACF shows a periodic pattern.

There are noticeable relationships around:

$$
h=12
$$

and potentially:

$$
h=24
$$

Because the data is monthly, lag 12 corresponds to approximately one year.

---

# 43. Detecting Seasonality

The ACF therefore suggests an annual seasonal component.

For monthly data:

$$
12\text{ months}=1\text{ year}
$$

If the ACF has repeated peaks at:

$$
12,\ 24,\ 36,\ldots
$$

this is strong evidence of yearly seasonality.

This is one of the most useful applications of the ACF.

---

# 44. Augmented Dickey-Fuller Test

The lecture introduces the **Augmented Dickey-Fuller (ADF) test** as a formal tool for investigating stationarity.

In R:

```r
library(tseries)

adf.test(residuals1)
```

The ADF test is associated with testing for a **unit root**.

The exact hypotheses require more time-series theory, but the practical interpretation introduced here is:

* small p-value → evidence supporting stationarity
* large p-value → insufficient evidence to reject non-stationarity

Always check the exact test specification because ADF tests can include different deterministic components.

---

# 45. White Noise with the ADF Test

Generate Gaussian white noise:

```r
set.seed(42)

wn <- rnorm(100)
```

Test it:

```r
adf.test(wn)
```

White noise is stationary, so we expect strong evidence against a unit-root/non-stationary process.

---

# 46. Random Walk with the ADF Test

Create a random walk:

```r
random_walk <- cumsum(wn)
```

Plot it:

```r
plot.ts(random_walk)
```

Then test:

```r
adf.test(random_walk)
```

A random walk is non-stationary, so we expect the test to provide much weaker evidence for stationarity.

This gives us two useful examples:

```text
Gaussian white noise → stationary

Random walk          → non-stationary
```

---

# 47. Trend + Stationary Noise

A useful conceptual model for the prescription series is:

$$
X_t
=
m(t)+Y_t
$$

where:

* \(m(t)\) = deterministic trend
* \(Y_t\) = stationary stochastic process

For a simple linear trend:

$$
m(t)=\beta_0+\beta_1t
$$

Therefore:

$$
X_t
=
\beta_0+\beta_1t+Y_t
$$

Removing \(m(t)\) leaves:

$$
Y_t
=
X_t-(\beta_0+\beta_1t)
$$

This is exactly the purpose of detrending.

---

# 48. Adding Seasonality with Trigonometric Terms

If we know that a monthly series has an annual cycle, we can model it using sine/cosine terms.

For example:

```r
model2 <- lm(
  prescript ~
    time(prescript) +
    cos(2 * pi * time(prescript))
)

summary(model2)
```

A more complete seasonal representation can use both:

```r
model2 <- lm(
  prescript ~
    time(prescript) +
    sin(2 * pi * time(prescript)) +
    cos(2 * pi * time(prescript))
)

summary(model2)
```

The trigonometric terms allow the model to represent periodic behavior.

---

# 49. Why \(2\pi\)?

The sine and cosine functions have a natural period of:

$$
2\pi
$$

Using:

$$
\cos(2\pi t)
$$

creates a repeating cycle.

For actual monthly data, the time variable and scaling must be chosen carefully so that the desired period corresponds to 12 months.

The general seasonal form is:

$$
\cos\left(\frac{2\pi t}{P}\right)
$$

where \(P\) is the desired period.

For annual seasonality in monthly data:

$$
P=12
$$

so:

$$
\cos\left(\frac{2\pi t}{12}\right)
$$

and similarly:

$$
\sin\left(\frac{2\pi t}{12}\right)
$$

---

# 50. Fitted Seasonal Model

A conceptual model is:

$$
X_t
=
\beta_0
+
\beta_1t
+
\beta_2
\cos\left(\frac{2\pi t}{12}\right)
+
\beta_3
\sin\left(\frac{2\pi t}{12}\right)
+
Y_t
$$

This model contains:

1. intercept
2. linear trend
3. seasonal cosine component
4. seasonal sine component
5. remaining stochastic process

---

# 51. Plot Model Predictions

Predicted values can be obtained with:

```r
pred2 <- fitted(model2)
```

Then:

```r
plot(prescript)

lines(
  time(prescript),
  pred2,
  lty = 2,
  lwd = 2
)
```

The fitted line should follow both the overall trend and the repeating seasonal pattern if the model captures those components well.

---

# 52. Important Lesson from the Example

The lecture demonstrates that modeling a time series is often iterative.

A possible workflow is:

```text
Raw data
   ↓
Visualize
   ↓
Identify trend
   ↓
Remove/model trend
   ↓
Check stationarity
   ↓
Compute ACF
   ↓
Identify seasonality/dependence
   ↓
Choose a time-series model
   ↓
Analyze residuals
```

The process is rarely perfectly linear.

A model may appear reasonable but fail a later diagnostic, requiring us to reconsider the model.

---

# 53. Common R Commands from the Lecture

## Generate Gaussian white noise

```r
set.seed(42)

wn <- rnorm(100)
```

## Plot a time series

```r
plot.ts(wn)
```

## Generate a random walk

```r
random_walk <- cumsum(wn)

plot.ts(random_walk)
```

## Calculate ACF

```r
acf(wn)
```

## Change maximum lag

```r
acf(wn, lag.max = 24)
```

## Fit linear regression

```r
model1 <- lm(
  prescript ~ time(prescript)
)
```

## Inspect model

```r
summary(model1)
```

## Extract residuals

```r
residuals1 <- residuals(model1)
```

## Plot residuals

```r
plot.ts(residuals1)
```

## Add horizontal zero line

```r
abline(
  h = 0,
  lty = 2
)
```

## Add fitted regression line

```r
abline(
  model1,
  lty = 2
)
```

## ADF test

```r
library(tseries)

adf.test(residuals1)
```

---

# 54. Complete Mini Practice

The following example reproduces the main statistical ideas from the lecture without requiring the prescription dataset.

## Step 1 — Generate white noise

```r
set.seed(42)

wn <- rnorm(200)

plot.ts(
  wn,
  main = "Gaussian White Noise",
  ylab = "Value",
  xlab = "Time"
)
```

## Step 2 — Examine the ACF

```r
acf(
  wn,
  lag.max = 30,
  main = "ACF of White Noise"
)
```

Expected behavior:

$$
\rho(h)\approx0
$$

for positive lags.

---

## Step 3 — Generate a Random Walk

```r
random_walk <- cumsum(wn)

plot.ts(
  random_walk,
  main = "Random Walk",
  ylab = "Value",
  xlab = "Time"
)
```

## Step 4 — Examine its ACF

```r
acf(
  random_walk,
  lag.max = 30,
  main = "ACF of Random Walk"
)
```

Expected behavior:

* strong positive autocorrelation
* slow decay
* indication of non-stationarity

---

# 55. MA(9) Simulation

A simple moving-average-style process can be constructed using a rolling mean:

```r
set.seed(42)

wn <- rnorm(200)

ma9 <- stats::filter(
  wn,
  rep(1 / 9, 9),
  sides = 1
)

plot.ts(
  ma9,
  main = "Moving Average Process",
  ylab = "Value",
  xlab = "Time"
)
```

Examine the ACF:

```r
acf(
  na.omit(ma9),
  lag.max = 30,
  main = "ACF of Moving Average Process"
)
```

The ACF should show dependence over a finite range of lags.

---

# 56. Second-Difference Example

Create a simple time series:

```r
x <- c(
  10, 13, 18, 25, 34,
  45, 58, 73
)
```

First difference:

```r
diff(x)
```

Second difference:

```r
diff(x, differences = 2)
```

The second difference corresponds to:

$$
\Delta^2X_t
=
X_t-2X_{t-1}+X_{t-2}
$$

---

# 57. Key Formulas

### Sample mean

$$
\boxed{
\bar X=
\frac{1}{T}
\sum_{t=1}^{T}X_t
}
$$

### Autocovariance

$$
\boxed{
\gamma(h)=Cov(X_t,X_{t+h})
}
$$

### Estimated autocovariance

$$
\boxed{
\hat{\gamma}(h)
=
\frac{1}{T}
\sum_{t=1}^{T-h}
(X_{t+h}-\bar X)(X_t-\bar X)
}
$$

### Autocorrelation

$$
\boxed{
\rho(h)=
\frac{\gamma(h)}
{\gamma(0)}
}
$$

### Estimated autocorrelation

$$
\boxed{
\hat{\rho}(h)=
\frac{\hat{\gamma}(h)}
{\hat{\gamma}(0)}
}
$$

### White-noise ACF

$$
\boxed{
\rho(h)=0,\quad h>0
}
$$

### Approximate ACF bounds

$$
\boxed{
\pm\frac{2}{\sqrt{T}}
}
$$

### Backshift

$$
\boxed{
BX_t=X_{t-1}
}
$$

### \(k\)-step backshift

$$
\boxed{
B^kX_t=X_{t-k}
}
$$

### First difference

$$
\boxed{
\Delta X_t=(1-B)X_t
}
$$

### Second difference

$$
\boxed{
\Delta^2X_t=(1-B)^2X_t
}
$$

### General difference

$$
\boxed{
\Delta^kX_t=(1-B)^kX_t
}
$$

---

# 58. ACF Pattern Cheat Sheet

| Data/process            | Typical ACF                        |
| ----------------------- | ---------------------------------- |
| White noise             | Near zero after lag 0              |
| Random walk             | Strong positive, slow decay        |
| MA(q)                   | Cuts off after approximately \(q\) |
| AR(p)                   | Gradual/geometric decay            |
| Seasonal series         | Peaks at seasonal lags             |
| Detrended seasonal data | Repeating ACF peaks                |

These patterns are **diagnostic clues**, not automatic proofs of a particular model.

---

# 59. Main Conceptual Takeaways

### 1. Stationarity

A stationary process has statistical properties that remain stable through time.

### 2. Autocovariance

Measures covariance between observations separated by a given lag.

### 3. Autocorrelation

Standardizes autocovariance and makes temporal dependence easier to interpret.

### 4. ACF

The ACF is one of the most important exploratory tools in time-series analysis.

### 5. White noise

White noise has approximately zero autocorrelation at all nonzero lags.

### 6. ACF confidence bounds

The approximate bounds

$$
\pm2/\sqrt{T}
$$

help us visually assess whether ACF values are unusually large.

### 7. Backshift

The backshift operator provides compact notation for lagged observations.

$$
BX_t=X_{t-1}
$$

### 8. Differencing

Differencing measures changes and can help transform a non-stationary series into a stationary one.

### 9. Regression vs. time-series models

Regression errors do not necessarily behave like independent noise in time-series applications.

The residual process can itself contain temporal dependence.

### 10. Trend removal

A time series can often be viewed as:

$$
\boxed{
\text{Time series}
=
\text{deterministic structure}
+
\text{stationary stochastic process}
}
$$

### 11. Seasonality

Repeating ACF peaks at seasonal lags can reveal periodic structure.

For monthly data, a peak at lag 12 can indicate annual seasonality.

### 12. Model diagnostics

After fitting a model, always examine what remains in the residuals.

---

# 60. Recommended Analysis Workflow

For a new time series, a practical workflow is:

```text
                 TIME SERIES
                      │
                      ▼
                 Plot the data
                      │
                      ▼
             Is there a trend?
                /           \
              Yes            No
               │              │
               ▼              ▼
        Model/remove trend   Continue
               │              │
               └──────┬───────┘
                      ▼
             Check stationarity
                      │
                      ▼
                  Compute ACF
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       White       Seasonal      AR/MA
       Noise       Pattern       Structure
          │           │           │
          └───────────┼───────────┘
                      ▼
                Build model
                      │
                      ▼
              Analyze residuals
                      │
                      ▼
              Refine if necessary
```

---

# 61. What Comes Next

This lecture completes the introductory treatment of:

* mean
* autocovariance
* autocorrelation
* white noise
* stationarity
* basic time-series modeling notation

It then begins the transition toward formal **statistical models for time series**.

The next stages will build toward:

* smoothing
* autoregressive models
* moving-average models
* ARMA
* ARIMA
* seasonal models
* unit roots
* forecasting
* residual diagnostics

The ACF introduced in this lecture will become one of the central tools for identifying and diagnosing these models.

---

## Final Mental Model

When looking at a time series, think:

> **First understand the level and trend. Then ask whether observations depend on previous observations.**

The ACF helps answer that second question.

```text
Observed Time Series
        │
        ├── Trend?
        │
        ├── Seasonality?
        │
        ├── Stationary?
        │
        └── Temporal dependence?
                │
                ▼
               ACF
                │
        ┌───────┼────────┐
        ▼       ▼        ▼
    White     Seasonal   AR/MA
    Noise     Pattern    Structure
```

The most important intuition from Lecture 3 is therefore:

$$
\boxed{
\text{ACF}
\rightarrow
\text{detect and understand temporal dependence}
}
$$

and:

$$
\boxed{
\text{Good time-series analysis}
=
\text{exploration}
+
\text{stationarity}
+
\text{dependence analysis}
+
\text{model diagnostics}
}
$$
