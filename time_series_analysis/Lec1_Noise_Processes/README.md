# Time Series Analysis — Lecture 1: Noise Processes

This project implements the fundamental stochastic processes introduced in **Lecture 1 of Time Series Analysis** using Python.

The main goal is to understand the basic building blocks of time-series models before working with real-world datasets.

---

## 📌 Learning Objectives

By completing this notebook, you should understand:

* Why time series analysis differs from ordinary linear regression
* Temporal dependence
* White noise and its different strengths
* Gaussian white noise
* Autoregressive processes
* Random walks
* Random walks with drift
* Moving-average processes
* Discrete and uniformly spaced time
* Markov processes
* Martingales
* Gaussian processes
* Linear processes
* The relationship between AR processes and linear processes
* Why `|θ| < 1` is important for an AR(1) process

---

# 1. Why Time Series Analysis?

In ordinary regression, observations are often assumed to be independent.

For example:

$$
Y = \beta_0 + \beta_1X_1 + \cdots + \beta_pX_p + \epsilon
$$

In time series, observations are ordered in time and may depend on previous observations.

For example, today's temperature may depend strongly on:

* yesterday's temperature
* the temperature several days ago
* seasonal effects
* random fluctuations

Therefore, instead of simply modeling:

$$
Y_t = f(X_t) + \epsilon_t
$$

we may model the relationship between:

$$
X_t, X_{t-1}, X_{t-2}, \ldots
$$

and the current observation.

This introduces **temporal dependence**.

---

# 2. Time Series Notation

We will use:

* \(t\) — current time
* \(X_t\) — observation at time \(t\)
* \(W_t\) — white-noise process
* \(\sigma^2\) — variance
* \(p\) — autoregressive order
* \(q\) — moving-average order
* \(\theta_i\), \(\phi_i\) — model coefficients

For this introductory project, time is assumed to be discrete and equally spaced:

$$
t = 0,1,2,\ldots,T
$$

Examples:

* daily observations
* weekly observations
* monthly observations
* hourly observations

---

# 3. White Noise

White noise is one of the fundamental building blocks of time-series analysis.

A weak white-noise process \(W_t\) satisfies:

$$
E[W_t] = 0
$$

$$
Var(W_t) = \sigma^2
$$

and for:

$$
t \neq s
$$

we have:

$$
Cov(W_t,W_s)=0
$$

Therefore:

> White noise has zero mean, constant variance, and no linear correlation between different time points.

Importantly:

**Uncorrelated does not necessarily mean independent.**

---

## 3.1 Weak White Noise

The basic conditions are:

$$
E[W_t]=0
$$

$$
Var(W_t)=\sigma^2
$$

$$
Cov(W_t,W_s)=0,\quad t\neq s
$$

---

## 3.2 IID White Noise

A stronger assumption is that observations are independent and identically distributed:

$$
W_t \overset{iid}{\sim} F
$$

with:

$$
E[W_t]=0
$$

and:

$$
Var(W_t)=\sigma^2
$$

---

## 3.3 Gaussian White Noise

An even stronger assumption is:

$$
W_t \sim N(0,\sigma^2)
$$

for every \(t\), with the observations independent.

Gaussian white noise is particularly useful because linear combinations of Gaussian variables remain Gaussian.

---

# 4. Python: Simulating White Noise

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

n = 500
sigma = 1

white_noise = np.random.normal(
    loc=0,
    scale=sigma,
    size=n
)

plt.figure(figsize=(12, 4))
plt.plot(white_noise)
plt.axhline(0, linestyle="--")
plt.title("Gaussian White Noise")
plt.xlabel("Time")
plt.ylabel("Value")
plt.show()
```

### Expected behavior

The series should:

* fluctuate around zero
* have approximately constant variance
* show no obvious trend
* show no obvious persistence

---

# 5. Checking White Noise

We can calculate its basic statistics.

```python
print("Mean:", white_noise.mean())
print("Variance:", white_noise.var())
```

For a sufficiently large sample, we expect:

$$
\bar W \approx 0
$$

and:

$$
s^2 \approx \sigma^2
$$

---

## Autocorrelation

White noise should have approximately zero autocorrelation at non-zero lags.

```python
from statsmodels.graphics.tsaplots import plot_acf

plot_acf(white_noise, lags=30)
plt.title("ACF of White Noise")
plt.show()
```

Most autocorrelation values should be close to zero.

---

# 6. Why Is It Called "White" Noise?

The term comes from **signal processing**.

White noise contains power across a broad range of frequencies.

An analogy is white light, which contains many visible frequencies.

In time-series analysis, white noise therefore represents a process without a preferred temporal frequency structure.

---

# 7. Autoregressive Process

An autoregressive process uses previous values of the same variable to explain the current value.

A general AR(\(p\)) model is:

$$
X_t =
\theta_1X_{t-1}
+
\theta_2X_{t-2}
+\cdots+
\theta_pX_{t-p}
+
W_t
$$

where \(W_t\) is white noise.

The key idea is:

> The past values of the process help determine its present value.

---

# 8. AR(1)

The simplest autoregressive model is:

$$
X_t = \theta X_{t-1}+W_t
$$

For example:

$$
X_t = 0.7X_{t-1}+W_t
$$

This means that the previous observation influences the current observation.

---

## Python Implementation

```python
def simulate_ar1(n, theta=0.7, sigma=1):
    noise = np.random.normal(0, sigma, n)

    x = np.zeros(n)

    for t in range(1, n):
        x[t] = theta * x[t - 1] + noise[t]

    return x
```

```python
ar1 = simulate_ar1(
    n=500,
    theta=0.7
)

plt.figure(figsize=(12, 4))
plt.plot(ar1)
plt.title("AR(1): Xₜ = 0.7Xₜ₋₁ + Wₜ")
plt.xlabel("Time")
plt.ylabel("Value")
plt.show()
```

---

# 9. AR(1) and Stability

A particularly important condition is:

$$
|\theta| < 1
$$

When:

$$
|\theta|<1
$$

the effect of old observations gradually decreases.

For example:

$$
0.7^1,\quad
0.7^2,\quad
0.7^3,\quad
\ldots
$$

become progressively smaller.

This gives the process a tendency to return toward its long-run behavior.

---

## What happens for different values?

### \(|\theta| < 1\)

Stable behavior.

### \(|\theta| = 1\)

Boundary case.

For:

$$
\theta=1
$$

we obtain a random walk:

$$
X_t=X_{t-1}+W_t
$$

### \(|\theta| > 1\)

The process becomes explosive rather than stable.

---

# 10. Random Walk

A random walk is:

$$
X_t=X_{t-1}+W_t
$$

Each new observation is the previous observation plus a random shock.

```python
def simulate_random_walk(n, sigma=1):
    noise = np.random.normal(0, sigma, n)

    x = np.zeros(n)

    for t in range(1, n):
        x[t] = x[t - 1] + noise[t]

    return x
```

```python
random_walk = simulate_random_walk(500)

plt.figure(figsize=(12, 4))
plt.plot(random_walk)
plt.title("Random Walk")
plt.xlabel("Time")
plt.ylabel("Value")
plt.show()
```

Unlike white noise, the observations of a random walk are highly dependent over time.

---

# 11. Random Walk with Drift

A random walk can include a constant drift term:

$$
X_t = a + X_{t-1}+W_t
$$

where \(a\) is a constant.

If:

$$
a>0
$$

the process tends upward.

If:

$$
a<0
$$

the process tends downward.

---

## Python

```python
def simulate_random_walk_drift(n, drift=0.05, sigma=1):
    noise = np.random.normal(0, sigma, n)

    x = np.zeros(n)

    for t in range(1, n):
        x[t] = drift + x[t - 1] + noise[t]

    return x
```

```python
rw_drift = simulate_random_walk_drift(
    n=500,
    drift=0.05
)

plt.figure(figsize=(12, 4))
plt.plot(rw_drift)
plt.title("Random Walk with Drift")
plt.xlabel("Time")
plt.ylabel("Value")
plt.show()
```

---

# 12. Moving Average Process

The moving-average process is another fundamental time-series model.

An MA(\(q\)) process is:

$$
X_t =
W_t+
\phi_1W_{t-1}
+\phi_2W_{t-2}
+\cdots+
\phi_qW_{t-q}
$$

The important distinction is:

### AR

Uses **past values of \(X\)**.

$$
X_t=f(X_{t-1},X_{t-2},...)
$$

### MA

Uses **past shocks/noise values**.

$$
X_t=f(W_t,W_{t-1},W_{t-2},...)
$$

---

# 13. MA(1)

The simplest moving-average process is:

$$
X_t=W_t+\phi W_{t-1}
$$

For example:

$$
X_t=W_t+0.8W_{t-1}
$$

```python
def simulate_ma1(n, phi=0.8, sigma=1):
    noise = np.random.normal(0, sigma, n)

    x = np.zeros(n)

    for t in range(1, n):
        x[t] = noise[t] + phi * noise[t - 1]

    return x
```

```python
ma1 = simulate_ma1(
    n=500,
    phi=0.8
)

plt.figure(figsize=(12, 4))
plt.plot(ma1)
plt.title("MA(1): Xₜ = Wₜ + 0.8Wₜ₋₁")
plt.xlabel("Time")
plt.ylabel("Value")
plt.show()
```

---

# 14. Intuition Behind MA Processes

Think of \(W_t\) as a **random shock**.

Suppose a sudden event occurs at time \(t\).

An MA model allows that shock to affect subsequent observations.

For an MA(1):

$$
X_t=W_t+\phi W_{t-1}
$$

the shock from the previous period can still influence the current observation.

If:

$$
\phi>0
$$

the shock continues in the same direction.

If:

$$
\phi<0
$$

the shock has an opposite effect in the next period.

---

# 15. Smoothing vs MA Time-Series Models

A common source of confusion is that "moving average" can mean two related but different things.

A conventional rolling average might be:

$$
MA_t=
\frac{1}{q}
\sum_{j=0}^{q-1}X_{t-j}
$$

This is primarily a **smoothing technique**.

An MA(\(q\)) stochastic process is instead:

$$
X_t=
W_t+\sum_{j=1}^{q}\phi_jW_{t-j}
$$

It models the current observation as a linear combination of current and past shocks.

---

# 16. Comparing White Noise, AR and MA

```python
np.random.seed(42)

n = 500

white_noise = np.random.normal(0, 1, n)
ar1 = simulate_ar1(n, theta=0.7)
ma1 = simulate_ma1(n, phi=0.7)

fig, axes = plt.subplots(3, 1, figsize=(12, 10))

axes[0].plot(white_noise)
axes[0].set_title("White Noise")

axes[1].plot(ar1)
axes[1].set_title("AR(1)")

axes[2].plot(ma1)
axes[2].set_title("MA(1)")

plt.tight_layout()
plt.show()
```

The important lesson is:

> Visual inspection alone is often insufficient to identify the underlying stochastic process.

A random-looking series does not necessarily mean that it is white noise.

---

# 17. Markov Process

A process is Markov when the conditional behavior of the future depends on the present rather than requiring the entire past.

Conceptually:

$$
P(X_t\mid X_{t-1},X_{t-2},\ldots)
=
P(X_t\mid X_{t-1})
$$

An AR(1) process is a common example:

$$
X_t=\theta X_{t-1}+W_t
$$

Once \(X_{t-1}\) is known, older values are not additionally required to generate \(X_t\).

---

# 18. Martingale

A martingale can be thought of as a generalized "fair game."

The defining idea is:

$$
E[X_t\mid X_{t-1},X_{t-2},\ldots]
=
X_{t-1}
$$

The best prediction of the next value, given the available history, is the current value.

The random walk:

$$
X_t=X_{t-1}+W_t
$$

with:

$$
E[W_t]=0
$$

is a basic example.

---

# 19. Gaussian Process

A Gaussian process generalizes the multivariate normal distribution to a collection of random variables indexed by time.

For any finite collection of time points:

$$
t_1,t_2,\ldots,t_k
$$

the vector:

$$
(X_{t_1},X_{t_2},\ldots,X_{t_k})
$$

has a multivariate Gaussian distribution.

A Gaussian process is characterized by its:

* mean function
* covariance function

This is one reason Gaussian processes are mathematically convenient.

---

# 20. Linear Process

A general linear process can be written as:

$$
X_t=
\mu+
\sum_{j=-\infty}^{\infty}
\theta_jW_{t-j}
$$

where \(W_t\) is white noise.

A condition ensuring that the infinite sum behaves appropriately is:

$$
\sum_{j=-\infty}^{\infty}\theta_j^2<\infty
$$

A causal linear process restricts the process to present and past shocks:

$$
X_t=
\mu+
\sum_{j=0}^{\infty}
\theta_jW_{t-j}
$$

---

# 21. AR(1) as a Linear Process

Consider:

$$
X_t=\theta X_{t-1}+W_t
$$

Substitute recursively:

$$
X_t
=
\theta(\theta X_{t-2}+W_{t-1})
+
W_t
$$

Therefore:

$$
X_t=
\theta^2X_{t-2}
+
\theta W_{t-1}
+
W_t
$$

Continuing recursively gives:

$$
X_t=
W_t+
\theta W_{t-1}
+
\theta^2W_{t-2}
+
\theta^3W_{t-3}
+\cdots
$$

or:

$$
X_t=
\sum_{j=0}^{\infty}
\theta^jW_{t-j}
$$

provided:

$$
|\theta|<1
$$

This shows that an AR(1) can be represented as a linear process.

---

# 22. Why \(|\theta| < 1\)?

The coefficients are:

$$
1,\theta,\theta^2,\theta^3,\ldots
$$

When:

$$
|\theta|<1
$$

these coefficients decrease toward zero.

For example, if:

$$
\theta=0.7
$$

then:

$$
1,\;0.7,\;0.49,\;0.343,\;0.2401,\ldots
$$

The influence of increasingly old shocks becomes smaller.

The corresponding variance is:

$$
Var(X_t)
=
\sigma^2
\sum_{j=0}^{\infty}\theta^{2j}
$$

Using the geometric-series formula:

$$
Var(X_t)
=
\frac{\sigma^2}{1-\theta^2}
$$

for:

$$
|\theta|<1
$$

---

# 23. Simulation: Different AR(1) Values

```python
np.random.seed(42)

thetas = [0.2, 0.7, 0.95, 1.0, -0.7]

fig, axes = plt.subplots(
    len(thetas),
    1,
    figsize=(12, 14)
)

for ax, theta in zip(axes, thetas):
    series = simulate_ar1(300, theta=theta)

    ax.plot(series)
    ax.set_title(f"AR(1), θ = {theta}")
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")

plt.tight_layout()
plt.show()
```

Observe how changing \(\theta\) changes the temporal dependence.

---

# 24. Simulating an AR(2)

An AR(2) process is:

$$
X_t=
\theta_1X_{t-1}
+
\theta_2X_{t-2}
+
W_t
$$

```python
def simulate_ar2(
    n,
    theta1=0.7,
    theta2=-0.2,
    sigma=1
):
    noise = np.random.normal(0, sigma, n)

    x = np.zeros(n)

    for t in range(2, n):
        x[t] = (
            theta1 * x[t - 1]
            + theta2 * x[t - 2]
            + noise[t]
        )

    return x
```

```python
ar2 = simulate_ar2(
    n=500,
    theta1=0.7,
    theta2=-0.2
)

plt.figure(figsize=(12, 4))
plt.plot(ar2)
plt.title("AR(2)")
plt.xlabel("Time")
plt.ylabel("Value")
plt.show()
```

---

# 25. Important Conceptual Comparison

| Process                | Depends primarily on                         |
| ---------------------- | -------------------------------------------- |
| White Noise            | Random shocks                                |
| AR(1)                  | Previous value                               |
| AR(p)                  | Previous \(p\) values                        |
| Random Walk            | Previous value + shock                       |
| Random Walk with Drift | Previous value + constant + shock            |
| MA(1)                  | Current and previous shock                   |
| MA(q)                  | Current and previous \(q\) shocks            |
| Markov Process         | Current state for predicting future          |
| Martingale             | Conditional expectation equals current value |
| Gaussian Process       | Joint Gaussian distributions                 |
| Linear Process         | Linear combination of white-noise shocks     |

---

# 26. Key Mathematical Relationships

### White Noise

$$
E[W_t]=0
$$

$$
Var(W_t)=\sigma^2
$$

$$
Cov(W_t,W_s)=0,\quad t\neq s
$$

### AR(p)

$$
X_t=
\sum_{i=1}^{p}\theta_iX_{t-i}+W_t
$$

### AR(1)

$$
X_t=\theta X_{t-1}+W_t
$$

### Random Walk

$$
X_t=X_{t-1}+W_t
$$

### Random Walk with Drift

$$
X_t=a+X_{t-1}+W_t
$$

### MA(q)

$$
X_t=
W_t+
\sum_{j=1}^{q}\phi_jW_{t-j}
$$

### Linear Process

$$
X_t=
\mu+
\sum_{j=-\infty}^{\infty}
\theta_jW_{t-j}
$$

### Causal Linear Process

$$
X_t=
\mu+
\sum_{j=0}^{\infty}
\theta_jW_{t-j}
$$

---

# 27. Practical Experiment

Run the following experiment to develop intuition.

Generate:

1. White noise
2. AR(1) with \(\theta=0.2\)
3. AR(1) with \(\theta=0.7\)
4. AR(1) with \(\theta=0.95\)
5. Random walk
6. Random walk with drift
7. MA(1) with \(\phi=0.7\)
8. MA(1) with \(\phi=-0.7\)

Then compare:

* mean
* variance
* visual behavior
* ACF
* persistence
* effect of shocks

---

# 28. Suggested Analysis Code

```python
from statsmodels.graphics.tsaplots import plot_acf

processes = {
    "White Noise": white_noise,
    "AR(1)": ar1,
    "MA(1)": ma1,
    "Random Walk": random_walk,
    "Random Walk + Drift": rw_drift
}

for name, series in processes.items():

    print(f"\n{name}")
    print("-" * len(name))
    print(f"Mean: {np.mean(series):.4f}")
    print(f"Variance: {np.var(series):.4f}")

    plot_acf(series, lags=30)
    plt.title(f"ACF — {name}")
    plt.show()
```

This provides an initial connection between:

$$
\text{Mathematical Model}
\rightarrow
\text{Simulation}
\rightarrow
\text{Observed Behavior}
$$

---

# 29. Main Takeaways

### 1. Time series are different because observations can be dependent.

The ordering of observations matters.

### 2. White noise is a fundamental building block.

It provides random shocks from which many models are constructed.

### 3. AR models use past values.

$$
X_t=f(X_{t-1},X_{t-2},...)
$$

### 4. MA models use past shocks.

$$
X_t=f(W_t,W_{t-1},...)
$$

### 5. Random walks are closely related to AR(1).

When:

$$
\theta=1
$$

the AR(1) becomes:

$$
X_t=X_{t-1}+W_t
$$

### 6. Stability matters.

For AR(1):

$$
|\theta|<1
$$

gives the standard stable case.

### 7. Visual appearance is not enough.

Different stochastic processes can look surprisingly similar.

Statistical tools such as:

* autocorrelation
* partial autocorrelation
* stationarity analysis
* parameter estimation
* hypothesis tests

are needed to identify and model time-series behavior.

---

# 30. Next Topics

The natural next step is to study the properties that allow us to formally analyze these processes:

* Autocovariance
* Autocorrelation
* Cross-covariance
* Stationarity
* Weak stationarity
* Strict stationarity
* Ergodicity
* ACF
* PACF
* More properties of AR and MA processes

These concepts will eventually lead toward:

$$
AR
\rightarrow
MA
\rightarrow
ARMA
\rightarrow
ARIMA
\rightarrow
Forecasting
$$

---

## Technologies

* Python
* NumPy
* Pandas
* Matplotlib
* Statsmodels
* Jupyter Notebook / Google Colab

---

## References

This notebook is based on the concepts covered in **Time Series Analysis — Lecture 1: Noise Processes**, including white noise, autoregressive processes, moving-average processes, random walks, Markov processes, martingales, Gaussian processes, and linear processes.
