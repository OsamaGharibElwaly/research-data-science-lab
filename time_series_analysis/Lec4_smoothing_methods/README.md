# Lecture 4 — Smoothing Methods for Time Series

## Overview

Time series data are often noisy. Short-term fluctuations can make it difficult to identify the underlying:

* Trend
* Seasonality
* Long-term movement
* General structure

**Smoothing** reduces short-term noise so that the underlying pattern becomes easier to see.

> **Main idea:** Smoothing is primarily an **exploratory data analysis (EDA)** tool. It helps us understand a time series, but the smoothed series should not automatically be treated as the original data for statistical testing or forecasting.

---

# 1. Why Do We Smooth Time Series?

Suppose we observe:

$$
X_1,X_2,\ldots,X_T
$$

The observed values contain both meaningful structure and random variation.

A useful conceptual representation is:

$$
X_t = \text{Signal}_t + \text{Noise}_t
$$

Smoothing attempts to reduce the noise component:

$$
X_t \longrightarrow M_t
$$

where \(M_t\) is the smoothed process.

### Why smoothing is useful

Smoothing can help us:

* Identify trends
* Visualize seasonality
* Reduce short-term fluctuations
* Detect large-scale changes
* Explore patterns before building a model
* Compare different levels of variability

---

# 2. Moving Average Smoother

The simplest smoothing method is the **moving average**.

For a window of \(2r+1\):

$$
M_t =
\sum_{j=-r}^{r}
\theta_j X_{t-j}
$$

where the weights satisfy:

$$
\sum_{j=-r}^{r}\theta_j=1
$$

## Simple Moving Average

The simplest choice gives every observation equal weight:

$$
\theta_j = \frac{1}{2r+1}
$$

Therefore:

$$
M_t =
\frac{1}{2r+1}
\sum_{j=-r}^{r}X_{t-j}
$$

For example, a 7-point moving average is:

$$
M_t =
\frac{
X_{t-3}+X_{t-2}+X_{t-1}
+X_t
+X_{t+1}+X_{t+2}+X_{t+3}
}{7}
$$

### Interpretation

A **7-day moving average** means:

> At each time point, average the values across a 7-day window.

This reduces daily fluctuations and makes the general trend easier to see.

---

# 3. Moving Average in Python

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Example time series
np.random.seed(42)

n = 100
time = np.arange(n)

trend = 0.1 * time
noise = np.random.normal(0, 2, n)

x = trend + noise

ts = pd.Series(x, index=time)

# 7-point moving average
ma7 = ts.rolling(window=7, center=True).mean()

plt.figure(figsize=(12, 5))

plt.plot(ts, label="Original")
plt.plot(ma7, linewidth=2, label="7-point Moving Average")

plt.title("Moving Average Smoothing")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.show()
```

### Important parameter

```python
center=True
```

means the moving average is centered around the current observation.

Without centering:

```python
ts.rolling(window=7).mean()
```

the window uses the current value and previous observations.

---

# 4. Comparing Different Moving Average Windows

The window size controls how much smoothing occurs.

```python
ma3 = ts.rolling(window=3, center=True).mean()
ma7 = ts.rolling(window=7, center=True).mean()
ma15 = ts.rolling(window=15, center=True).mean()

plt.figure(figsize=(12, 6))

plt.plot(ts, alpha=0.5, label="Original")
plt.plot(ma3, linewidth=2, label="3-point MA")
plt.plot(ma7, linewidth=2, label="7-point MA")
plt.plot(ma15, linewidth=2, label="15-point MA")

plt.title("Effect of Moving Average Window Size")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.show()
```

### Interpretation

| Window | Smoothing | Detail                            |
| ------ | --------- | --------------------------------- |
| Small  | Low       | Preserves fluctuations            |
| Medium | Moderate  | Reveals general trend             |
| Large  | High      | Removes more short-term variation |

### Key principle

> **Larger window → more smoothing → less local detail.**

---

# 5. Boundary Problem

Centered moving averages have an important limitation.

For a 7-point moving average, we need:

$$
t-3,\ldots,t,\ldots,t+3
$$

At the beginning and end of the series, some of these observations do not exist.

Therefore, centered moving averages produce missing values near the boundaries.

```python
ma7.isna().sum()
```

You can visualize where the missing values occur:

```python
print(ma7.head())
print(ma7.tail())
```

This is one reason other smoothing methods can be useful.

---

# 6. Kernel Smoothing

A moving average gives every observation in the window the same weight.

Kernel smoothing provides a more flexible approach.

The general idea is:

$$
M_t =
\frac{
\sum_i K_h(t-i)X_i
}{
\sum_i K_h(t-i)
}
$$

where:

* \(K_h\) = kernel function
* \(h\) = bandwidth
* \(t\) = point being smoothed

The kernel determines **how much weight each nearby observation receives**.

---

# 7. What Is a Kernel?

A kernel assigns larger weights to observations closer to the center.

Conceptually:

```text
Weight
  ^
  |           /\
  |          /  \
  |         /    \
  |________/______\________> Distance
             center
```

Observations close to the target time receive greater weight.

Observations farther away receive smaller weights.

---

# 8. Bandwidth

The **bandwidth \(h\)** controls how wide the kernel is.

### Small bandwidth

```text
        /\
       /  \
______/    \______
```

* Less smoothing
* More local detail
* More sensitive to noise

### Large bandwidth

```text
       ______
     /        \
____/          \____
```

* More smoothing
* Less local detail
* Stronger trend extraction

### Key principle

> **Small \(h\) → less smoothing.**

> **Large \(h\) → more smoothing.**

---

# 9. Gaussian Kernel

A common kernel is the Gaussian kernel:

$$
K_h(x,x_0)
=
\exp
\left(
-\frac{(x-x_0)^2}{2h^2}
\right)
$$

It has a bell-shaped form.

Important properties:

* Maximum weight at the center
* Weight decreases with distance
* Theoretically extends to infinity
* Larger \(h\) produces a wider kernel

---

# 10. Triangular Kernel

The triangular kernel can be written using the positive-part notation:

$$
K_h(x,x_0)
=
\left(
1-\frac{|x-x_0|}{h}
\right)_+
$$

where:

$$
y_+ =
\begin{cases}
y & y>0\\
0 & y\leq0
\end{cases}
$$

The kernel looks approximately like:

```text
Weight
  ^
  |          /\
  |         /  \
  |        /    \
  |_______/______\_______> x
           x₀
```

Unlike the Gaussian kernel, it becomes exactly zero outside the bandwidth.

---

# 11. Epanechnikov Kernel

Another popular kernel is the **Epanechnikov kernel**:

$$
K_h(x,x_0)
=
\left(
1-\frac{(x-x_0)^2}{h^2}
\right)_+
$$

It has a parabolic shape:

```text
Weight
  ^
  |         __
  |       /    \
  |     /        \
  |____/__________\____> x
            x₀
```

It is widely used in nonparametric statistics.

---

# 12. Kernel Smoothing vs Moving Average

A moving average can be viewed as a special type of weighted smoother.

### Moving average

All observations receive equal weight:

$$
\theta_j =
\frac{1}{2r+1}
$$

### Kernel smoother

Weights depend on distance:

$$
\theta_j \propto K_h(j,0)
$$

Therefore:

> A kernel smoother is essentially a moving average with more intelligently chosen weights.

Nearby observations receive more influence than distant observations.

---

# 13. Gaussian Kernel Smoothing in Python

We can implement kernel smoothing directly with NumPy.

```python
import numpy as np
import matplotlib.pyplot as plt

def gaussian_kernel_smoother(x, bandwidth):
    x = np.asarray(x)
    n = len(x)

    smoothed = np.zeros(n)

    for i in range(n):

        distances = x - i

        weights = np.exp(
            -(distances ** 2) /
            (2 * bandwidth ** 2)
        )

        weights /= weights.sum()

        smoothed[i] = np.sum(weights * x)

    return smoothed
```

However, if the index and data values are different concepts, it is better to explicitly provide the time values:

```python
def gaussian_kernel_smoother(time, values, bandwidth):
    time = np.asarray(time)
    values = np.asarray(values)

    smoothed = np.zeros(len(values))

    for i, t0 in enumerate(time):

        distances = time - t0

        weights = np.exp(
            -(distances ** 2) /
            (2 * bandwidth ** 2)
        )

        weights /= weights.sum()

        smoothed[i] = np.sum(weights * values)

    return smoothed
```

Apply it:

```python
ks_1 = gaussian_kernel_smoother(
    time,
    x,
    bandwidth=2
)

ks_5 = gaussian_kernel_smoother(
    time,
    x,
    bandwidth=5
)

plt.figure(figsize=(12, 6))

plt.plot(time, x, alpha=0.4, label="Original")
plt.plot(time, ks_1, linewidth=2, label="Bandwidth = 2")
plt.plot(time, ks_5, linewidth=2, label="Bandwidth = 5")

plt.title("Gaussian Kernel Smoothing")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.show()
```

---

# 14. Comparing Kernel Bandwidths

```python
bandwidths = [1, 3, 7, 15]

plt.figure(figsize=(12, 7))

plt.plot(time, x, alpha=0.35, label="Original")

for h in bandwidths:
    smoothed = gaussian_kernel_smoother(
        time,
        x,
        bandwidth=h
    )

    plt.plot(
        time,
        smoothed,
        linewidth=2,
        label=f"h = {h}"
    )

plt.title("Effect of Kernel Bandwidth")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.show()
```

### Interpretation

If:

```python
h = 1
```

the smoother follows local changes closely.

If:

```python
h = 15
```

the smoother captures broad-scale structure and removes much more noise.

---

# 15. LOWESS

Another important smoother is:

**LOWESS**

which stands for:

> Locally Weighted Scatterplot Smoothing

It works approximately by:

1. Selecting a local neighborhood
2. Giving nearby observations larger weights
3. Fitting a low-degree polynomial locally
4. Evaluating the fitted polynomial
5. Moving to the next time point

Therefore LOWESS is a **local regression smoother**.

---

# 16. LOWESS in Python

Python's `statsmodels` package provides LOWESS.

```python
import numpy as np
import matplotlib.pyplot as plt

from statsmodels.nonparametric.smoothers_lowess import lowess

lowess_result = lowess(
    endog=x,
    exog=time,
    frac=0.2
)

plt.figure(figsize=(12, 5))

plt.plot(time, x, alpha=0.4, label="Original")
plt.plot(
    lowess_result[:, 0],
    lowess_result[:, 1],
    linewidth=2,
    label="LOWESS"
)

plt.title("LOWESS Smoothing")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.show()
```

---

# 17. LOWESS Smoothing Parameter

The main parameter is:

```python
frac
```

It determines approximately how much of the data is used for each local regression.

### Small `frac`

```python
frac=0.1
```

* More local
* Less smoothing
* More fluctuations

### Large `frac`

```python
frac=0.5
```

* More global
* More smoothing
* Smoother trend

Compare them:

```python
fractions = [0.1, 0.3, 0.6]

plt.figure(figsize=(12, 6))

plt.plot(time, x, alpha=0.3, label="Original")

for frac in fractions:

    result = lowess(
        x,
        time,
        frac=frac
    )

    plt.plot(
        result[:, 0],
        result[:, 1],
        linewidth=2,
        label=f"frac={frac}"
    )

plt.title("LOWESS: Effect of Smoothing Parameter")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.show()
```

---

# 18. Cubic Splines

A spline is a piecewise polynomial function.

Instead of fitting one polynomial across the entire dataset, we divide the time domain into intervals.

These dividing points are called:

> **Knots**

Suppose we have:

$$
1=t_1<t_2<\cdots<t_{k+1}=T
$$

This produces \(k\) intervals.

Within each interval, a cubic polynomial can be fitted:

$$
M_t^{(i)}
=
\beta_0^{(i)}
+
\beta_1^{(i)}t
+
\beta_2^{(i)}t^2
+
\beta_3^{(i)}t^3
$$

The pieces are joined together smoothly.

---

# 19. Why Cubic Splines?

Cubic splines are popular because they provide enough flexibility to model curvature while maintaining smoothness.

They are useful in:

* Statistics
* Data science
* Engineering
* Computer graphics
* CAD
* Interpolation
* Nonlinear regression

A cubic spline can model nonlinear trends without forcing the entire dataset to follow one high-degree polynomial.

---

# 20. Cubic Smoothing Splines

A cubic smoothing spline balances two objectives:

### 1. Fit the data

We want:

$$
\sum_{t=1}^{T}
(X_t-M_t)^2
$$

to be small.

### 2. Keep the curve smooth

We penalize curvature:

$$
\lambda
\int
[M''(s)]^2ds
$$

Therefore, the optimization problem is:

$$
\boxed{
\min_M
\left[
\sum_{t=1}^{T}(X_t-M_t)^2
+
\lambda
\int[M''(s)]^2ds
\right]
}
$$

---

# 21. Understanding λ

The parameter:

$$
\lambda
$$

controls the smoothing strength.

### λ = 0

No curvature penalty.

The model focuses entirely on fitting the observations.

```text
Small λ
   ↓
More flexible
   ↓
Less smoothing
```

### Large λ

Strong curvature penalty.

```text
Large λ
   ↓
Less flexible
   ↓
More smoothing
```

As:

$$
\lambda\rightarrow\infty
$$

the second derivative approaches zero:

$$
M''(t)\approx0
$$

The result approaches a straight line.

---

# 22. Connection to Ridge Regression

This is conceptually similar to ridge regression.

Ridge regression minimizes:

$$
\|y-X\beta\|^2
+
\lambda\|\beta\|^2
$$

A smoothing spline minimizes:

$$
\|X-F\beta\|^2
+
\lambda\beta^T\Omega\beta
$$

The important idea is the same:

> **Add a penalty to control model complexity.**

This creates a **bias-variance trade-off**.

---

# 23. Bias-Variance Trade-off

### Too little smoothing

The curve follows the noise.

```text
High variance
Low bias
```

### Too much smoothing

The curve misses important structure.

```text
Low variance
High bias
```

The goal is to find an appropriate balance.

---

# 24. Cubic Smoothing Splines in Python

SciPy provides a useful implementation through `UnivariateSpline`.

```python
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt

# Larger s = stronger smoothing
spline = UnivariateSpline(
    time,
    x,
    s=100
)

smooth_x = spline(time)

plt.figure(figsize=(12, 5))

plt.plot(time, x, alpha=0.4, label="Original")
plt.plot(
    time,
    smooth_x,
    linewidth=2,
    label="Smoothing Spline"
)

plt.title("Cubic Smoothing Spline")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.show()
```

---

# 25. Comparing Spline Smoothing Strength

```python
s_values = [10, 100, 500]

plt.figure(figsize=(12, 6))

plt.plot(
    time,
    x,
    alpha=0.3,
    label="Original"
)

for s in s_values:

    spline = UnivariateSpline(
        time,
        x,
        s=s
    )

    plt.plot(
        time,
        spline(time),
        linewidth=2,
        label=f"s={s}"
    )

plt.title("Effect of Smoothing Spline Parameter")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.show()
```

### Interpretation

Depending on the implementation, the exact parameterization differs from the lecture's mathematical \(\lambda\), so always check the library documentation.

The conceptual relationship remains:

> More smoothing → smoother curve.

---

# 26. Comparing All Smoothing Methods

We can put the main methods together.

```python
import numpy as np
import matplotlib.pyplot as plt

from statsmodels.nonparametric.smoothers_lowess import lowess
from scipy.interpolate import UnivariateSpline

# Moving average
ma = pd.Series(x).rolling(
    window=9,
    center=True
).mean()

# Gaussian kernel
kernel = gaussian_kernel_smoother(
    time,
    x,
    bandwidth=4
)

# LOWESS
lowess_result = lowess(
    x,
    time,
    frac=0.2
)

# Smoothing spline
spline = UnivariateSpline(
    time,
    x,
    s=100
)

spline_values = spline(time)

# Plot
plt.figure(figsize=(14, 7))

plt.plot(
    time,
    x,
    alpha=0.3,
    label="Original"
)

plt.plot(
    time,
    ma,
    linewidth=2,
    label="Moving Average"
)

plt.plot(
    time,
    kernel,
    linewidth=2,
    label="Gaussian Kernel"
)

plt.plot(
    lowess_result[:, 0],
    lowess_result[:, 1],
    linewidth=2,
    label="LOWESS"
)

plt.plot(
    time,
    spline_values,
    linewidth=2,
    label="Cubic Spline"
)

plt.title("Comparison of Time Series Smoothing Methods")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.show()
```

---

# 27. What Should We Look For?

When comparing smoothers, ask:

### Trend

Is there a long-term increase or decrease?

### Seasonality

Are there repeated patterns?

### Cycles

Are there medium-term fluctuations?

### Structural changes

Does the behavior change at some point?

### Noise

Which fluctuations appear to be random?

---

# 28. Smoothing Is Not Forecasting

This distinction is important.

Smoothing answers:

> **"What does the underlying structure of this data look like?"**

Forecasting asks:

> **"What will happen in the future?"**

A smoother can help us understand a time series, but it is not automatically a forecasting model.

For example:

```text
Observed data
      ↓
   Smoothing
      ↓
Understand trend / structure
      ↓
Choose an appropriate model
      ↓
Forecast
```

---

# 29. The Major Warning: Don't Smooth Before Statistical Testing

Smoothing removes noise.

Many statistical methods depend on the presence and structure of that noise.

Therefore:

```text
Original Time Series
        │
        ├──→ Statistical Analysis
        │
        └──→ Smoothing → Visualization / EDA
```

Do not automatically do:

```text
Original
   ↓
Smooth
   ↓
ACF / hypothesis testing / regression
```

because the smoothing operation has changed the statistical properties of the data.

---

# 30. Example: Differencing and Smoothing

Suppose a time series is non-stationary.

We can first difference it:

$$
Y_t=X_t-X_{t-1}
$$

In Python:

```python
diff = pd.Series(x).diff().dropna()
```

Plot it:

```python
plt.figure(figsize=(12, 5))

plt.plot(diff)

plt.title("First Difference")
plt.xlabel("Time")
plt.ylabel("Differenced Value")

plt.show()
```

We can then smooth it for exploratory visualization:

```python
diff_smooth = diff.rolling(
    window=7,
    center=True
).mean()

plt.figure(figsize=(12, 5))

plt.plot(
    diff,
    alpha=0.4,
    label="Differenced"
)

plt.plot(
    diff_smooth,
    linewidth=2,
    label="Smoothed Difference"
)

plt.title("Differenced Series with Smoothing")
plt.xlabel("Time")
plt.ylabel("Value")

plt.legend()
plt.show()
```

The smoother may reveal periodicity or other structure.

But statistical analysis should generally be performed on the **appropriate original/transformed series**, not blindly on the smoothed version.

---

# 31. ACF Warning

The Autocorrelation Function is sensitive to the structure of a time series.

If we smooth the series first, we introduce dependence between nearby observations through the smoothing operation itself.

Therefore:

```python
from statsmodels.graphics.tsaplots import plot_acf

plot_acf(diff.dropna(), lags=30)
plt.show()
```

is conceptually different from:

```python
plot_acf(diff_smooth.dropna(), lags=30)
plt.show()
```

The second ACF describes the **smoothed process**, not necessarily the original process.

This can lead to misleading conclusions.

---

# 32. Practical Interpretation Workflow

A useful workflow is:

```text
1. Plot original time series
             ↓
2. Inspect noise and variability
             ↓
3. Apply smoothing for EDA
             ↓
4. Identify trend / seasonality / cycles
             ↓
5. Transform if necessary
             ↓
6. Analyze the appropriate original/transformed series
             ↓
7. Build statistical / forecasting model
```

---

# 33. Choosing a Smoothing Method

| Method           | Main Idea                 | Main Parameter      |
| ---------------- | ------------------------- | ------------------- |
| Moving Average   | Equal weights             | Window              |
| Kernel Smoothing | Distance-based weights    | Bandwidth \(h\)     |
| LOWESS           | Local weighted regression | `frac`              |
| Smoothing Spline | Penalized flexible curve  | Smoothing parameter |

### Moving Average

Best when you want a simple and interpretable smoother.

### Kernel

Useful when you want distance-dependent weights.

### LOWESS

Useful for flexible local nonlinear trends.

### Smoothing Spline

Useful when you want a smooth nonlinear function controlled by a complexity penalty.

---

# 34. Key Parameter Relationships

Remember these relationships:

### Moving Average

$$
\boxed{\text{Larger window} \Rightarrow \text{More smoothing}}
$$

### Kernel

$$
\boxed{\text{Larger bandwidth }h
\Rightarrow \text{More smoothing}}
$$

### LOWESS

$$
\boxed{\text{Larger frac}
\Rightarrow \text{More smoothing}}
$$

### Smoothing Spline

$$
\boxed{\text{Larger penalty}
\Rightarrow \text{More smoothing}}
$$

---

# 35. Quick Experiment

Use the following dataset:

```python
np.random.seed(123)

n = 200

time = np.arange(n)

trend = 0.03 * time
seasonality = 2 * np.sin(2 * np.pi * time / 30)
noise = np.random.normal(0, 1, n)

x = trend + seasonality + noise
```

Plot the original data:

```python
plt.figure(figsize=(14, 5))

plt.plot(time, x)

plt.title("Simulated Time Series")
plt.xlabel("Time")
plt.ylabel("Value")

plt.show()
```

Now apply a moving average:

```python
ma = pd.Series(x).rolling(
    window=15,
    center=True
).mean()

plt.figure(figsize=(14, 5))

plt.plot(
    time,
    x,
    alpha=0.35,
    label="Original"
)

plt.plot(
    time,
    ma,
    linewidth=2,
    label="15-point MA"
)

plt.legend()
plt.show()
```

Try different values:

```python
for window in [5, 15, 30, 60]:

    smooth = pd.Series(x).rolling(
        window=window,
        center=True
    ).mean()

    plt.figure(figsize=(12, 4))

    plt.plot(
        time,
        x,
        alpha=0.3,
        label="Original"
    )

    plt.plot(
        time,
        smooth,
        linewidth=2,
        label=f"Window = {window}"
    )

    plt.title(
        f"Moving Average with Window = {window}"
    )

    plt.legend()
    plt.show()
```

Observe how increasing the window gradually removes more short-term variation.

---

# 36. Important Concepts to Remember

### Smoothing

A method for reducing short-term variation to reveal larger-scale structure.

### Moving Average

A weighted average of neighboring observations.

### Kernel

A function that determines the weights assigned to nearby observations.

### Bandwidth

Controls how wide the kernel is.

### LOWESS

Locally weighted polynomial regression.

### Spline

A piecewise polynomial function joined smoothly at knots.

### Smoothing Spline

A spline that balances data fit against curvature.

### Penalty

A mechanism that discourages overly complex curves.

### Bias-Variance Trade-off

More smoothing generally means:

* Higher bias
* Lower variance

Less smoothing generally means:

* Lower bias
* Higher variance

---

# 37. Final Takeaways

1. **Time series can be noisy**, making trends difficult to see.

2. **Smoothing helps reveal large-scale structure.**

3. A **moving average** gives observations within a window equal or predefined weights.

4. **Kernel smoothing** uses distance-based weights.

5. **Bandwidth \(h\)** controls the amount of kernel smoothing.

6. **LOWESS** performs local weighted regression.

7. **Cubic smoothing splines** balance data fit and smoothness through a penalty.

8. The smoothing parameter controls the **bias-variance trade-off**.

9. Larger smoothing parameters generally produce smoother curves.

10. Smoothing is primarily an **EDA tool**.

11. Do not automatically perform statistical inference on a smoothed series.

12. Use smoothing to understand the data, then return to the appropriate original/transformed series for formal statistical modeling.

---

## One-Sentence Summary

> **Smoothing transforms a noisy time series into a cleaner representation that helps us see its underlying trend and structure, but the smoothed series should generally be treated as an exploratory visualization rather than a replacement for the original data in statistical inference.**
