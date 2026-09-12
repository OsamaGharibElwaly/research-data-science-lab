# Time Series Analysis — Lecture 2

## Autocovariance, Autocorrelation, Stationarity & Estimation

This lecture moves from identifying different time-series processes to understanding their **statistical properties**.

The main idea is:

> A time series is not only described by how it is generated. We also need to understand how its observations relate to each other across time.

The key concepts introduced are:

* Covariance
* Autocovariance
* Autocorrelation
* Cross-covariance and cross-correlation
* Weak stationarity
* Strong stationarity
* Joint stationarity
* AR(1) with drift
* Linear-process representation
* Estimation of the mean
* Variance of the sample mean for dependent observations

---

# 1. Learning Objectives

By the end of this lecture, you should understand:

1. What covariance measures.
2. Why covariance between two variables does not generally imply independence.
3. How covariance extends to time series through **autocovariance**.
4. How autocorrelation normalizes autocovariance.
5. Why autocovariance functions must satisfy symmetry and positive-semidefinite properties.
6. How an AR(1) process with drift can be represented as a linear process.
7. How to calculate its mean, variance, and autocovariance.
8. What stationarity means.
9. The difference between weak and strong stationarity.
10. Why stationarity is important for statistical estimation.
11. How cross-covariance describes relationships between two time series.
12. Why dependence between observations changes the variance of the sample mean.

---

# 2. Covariance

Before studying autocovariance, we need the ordinary covariance.

For two random variables \(X\) and \(Y\):

$$
\operatorname{Cov}(X,Y)
=
E[(X-E[X])(Y-E[Y])]
$$

Covariance measures the **linear relationship** between two random variables.

### Interpretation

* Positive covariance → variables tend to move together.
* Negative covariance → variables tend to move in opposite directions.
* Zero covariance → no linear relationship is detected.

However:

$$
\operatorname{Cov}(X,Y)=0
$$

does **not generally imply independence**.

The reverse implication does hold:

$$
X \perp Y
\Rightarrow
\operatorname{Cov}(X,Y)=0
$$

For jointly Gaussian random variables, zero covariance does imply independence:

$$
X,Y \text{ jointly Gaussian}
\quad\text{and}\quad
\operatorname{Cov}(X,Y)=0
\Rightarrow
X\perp Y
$$

---

# 3. Python: Covariance Example

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

x = np.random.normal(size=100)
y = 0.8 * x + np.random.normal(scale=0.5, size=100)

covariance = np.cov(x, y, ddof=1)[0, 1]

print("Sample covariance:", covariance)

plt.scatter(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Positive Covariance")
plt.show()
```

The positive covariance occurs because larger values of `x` tend to be associated with larger values of `y`.

---

# 4. Autocovariance

A time series is indexed by time:

$$
X_t
$$

Instead of comparing two different variables \(X\) and \(Y\), we can compare the same process at two different times.

The **autocovariance** is:

$$
K_X(s,t)
=
\operatorname{Cov}(X_s,X_t)
$$

or

$$
K_X(s,t)
=
E[(X_s-\mu_s)(X_t-\mu_t)]
$$

where:

$$
\mu_t=E[X_t]
$$

The prefix **auto** means that we are measuring the relationship of a process with itself.

---

# 5. Properties of Autocovariance

The autocovariance function has important mathematical properties.

## Symmetry

$$
K_X(s,t)=K_X(t,s)
$$

This follows from the symmetry of covariance.

## Variance

When both time points are the same:

$$
K_X(t,t)
=
\operatorname{Var}(X_t)
$$

Therefore, the diagonal of an autocovariance matrix contains the variances.

## Positive Semidefinite

For any collection of time points:

$$
t_1,t_2,\ldots,t_n
$$

we can construct:

$$
\mathbf K_{ij}=K_X(t_i,t_j)
$$

This matrix must be positive semidefinite:

$$
\mathbf a^T\mathbf K\mathbf a\geq0
$$

for every vector \(\mathbf a\).

This is analogous to the fact that a variance cannot be negative.

---

# 6. Python: Autocovariance

A simple way to calculate sample autocovariance at different lags:

```python
import numpy as np

def autocovariance(x, lag):
    x = np.asarray(x)
    mean = np.mean(x)

    if lag == 0:
        return np.mean((x - mean) ** 2)

    return np.mean(
        (x[:-lag] - mean) *
        (x[lag:] - mean)
    )

x = np.random.normal(size=1000)

for lag in range(6):
    print(f"Lag {lag}: {autocovariance(x, lag):.4f}")
```

For white noise, autocovariance should be approximately:

$$
K(0)=\sigma^2
$$

and:

$$
K(h)\approx0
$$

for \(h>0\).

---

# 7. Autocorrelation

Autocorrelation is the **normalized autocovariance**.

For a stationary process:

$$
\rho(h)
=
\frac{\gamma(h)}
{\gamma(0)}
$$

where:

$$
\gamma(h)=\operatorname{Cov}(X_t,X_{t+h})
$$

and:

$$
\gamma(0)=\operatorname{Var}(X_t)
$$

Therefore:

$$
-1\leq\rho(h)\leq1
$$

Autocorrelation is useful because it allows us to compare dependence at different lags on a standardized scale.

---

# 8. Python: Autocorrelation

```python
import numpy as np
import matplotlib.pyplot as plt

def autocorrelation(x, max_lag):
    x = np.asarray(x)
    x = x - np.mean(x)

    result = []

    for lag in range(max_lag + 1):
        numerator = np.sum(x[:len(x) - lag] * x[lag:])
        denominator = np.sum(x ** 2)

        result.append(numerator / denominator)

    return np.array(result)

np.random.seed(42)

white_noise = np.random.normal(size=500)

lags = np.arange(21)
acf = autocorrelation(white_noise, 20)

plt.stem(lags, acf)
plt.xlabel("Lag")
plt.ylabel("Autocorrelation")
plt.title("Autocorrelation of White Noise")
plt.show()
```

The autocorrelation at lag zero is:

$$
\rho(0)=1
$$

For white noise, correlations at other lags should be close to zero.

---

# 9. AR(1) with Drift

The lecture uses an AR(1) process with a constant:

$$
X_t=a+\theta X_{t-1}+W_t
$$

where:

* \(a\) = constant/drift term
* \(\theta\) = autoregressive coefficient
* \(W_t\) = white noise
* \(E[W_t]=0\)
* \(\operatorname{Var}(W_t)=\sigma^2\)

For the process to have a stable stationary solution:

$$
|\theta|<1
$$

---

# 10. Expanding the AR(1) Recursively

Starting with:

$$
X_t=a+\theta X_{t-1}+W_t
$$

Substitute:

$$
X_{t-1}=a+\theta X_{t-2}+W_{t-1}
$$

Then:

$$
X_t
=
a+\theta(a+\theta X_{t-2}+W_{t-1})+W_t
$$

Therefore:

$$
X_t
=
a(1+\theta)
+\theta^2X_{t-2}
+\theta W_{t-1}
+W_t
$$

Continuing indefinitely gives:

$$
X_t
=
\frac{a}{1-\theta}
+
\sum_{j=0}^{\infty}\theta^jW_{t-j}
$$

This is the **linear-process representation**.

It is extremely useful because it makes the mean and covariance easier to calculate.

---

# 11. Mean of AR(1) with Drift

From:

$$
X_t
=
\frac{a}{1-\theta}
+
\sum_{j=0}^{\infty}\theta^jW_{t-j}
$$

and:

$$
E[W_t]=0
$$

we obtain:

$$
E[X_t]
=
\frac{a}{1-\theta}
$$

Therefore:

$$
\boxed{\mu=\frac{a}{1-\theta}}
$$

The mean does not depend on \(t\).

---

# 12. Variance of AR(1)

For:

$$
X_t-\mu
=
\sum_{j=0}^{\infty}\theta^jW_{t-j}
$$

the variance is:

$$
\operatorname{Var}(X_t)
=
\sigma^2
\sum_{j=0}^{\infty}\theta^{2j}
$$

Using the geometric series:

$$
\sum_{j=0}^{\infty}\theta^{2j}
=
\frac{1}{1-\theta^2}
$$

we obtain:

$$
\boxed{
\operatorname{Var}(X_t)
=
\frac{\sigma^2}{1-\theta^2}
}
$$

Again, the variance does not depend on \(t\).

---

# 13. Autocovariance of AR(1)

For a stationary AR(1):

$$
\gamma(h)
=
\operatorname{Cov}(X_t,X_{t+h})
$$

and the result is:

$$
\boxed{
\gamma(h)
=
\frac{\sigma^2}{1-\theta^2}
\theta^{|h|}
}
$$

Notice the absolute value.

This is necessary because autocovariance must be symmetric:

$$
\gamma(h)=\gamma(-h)
$$

At lag zero:

$$
\gamma(0)
=
\frac{\sigma^2}{1-\theta^2}
$$

which is exactly the variance.

---

# 14. Autocorrelation of AR(1)

Since:

$$
\rho(h)=\frac{\gamma(h)}{\gamma(0)}
$$

we get:

$$
\boxed{
\rho(h)=\theta^{|h|}
}
$$

This gives us a very useful result:

> The autocorrelation of an AR(1) decays geometrically with the lag.

If:

$$
\theta=0.8
$$

then:

$$
\rho(1)=0.8
$$

$$
\rho(2)=0.64
$$

$$
\rho(3)=0.512
$$

and so on.

---

# 15. Python: Simulating AR(1) with Drift

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

n = 500

a = 1.0
theta = 0.8
sigma = 1.0

x = np.zeros(n)

for t in range(1, n):
    w = np.random.normal(0, sigma)
    x[t] = a + theta * x[t - 1] + w

plt.plot(x)
plt.xlabel("Time")
plt.ylabel("X")
plt.title("AR(1) Process with Drift")
plt.show()
```

The theoretical mean is:

```python
theoretical_mean = a / (1 - theta)

print("Theoretical mean:", theoretical_mean)
print("Sample mean:", np.mean(x))
```

The theoretical variance is:

```python
theoretical_variance = sigma**2 / (1 - theta**2)

print("Theoretical variance:", theoretical_variance)
print("Sample variance:", np.var(x))
```

Because the process is simulated from a finite sample, the sample statistics will not exactly equal the theoretical values.

---

# 16. Stationarity

Stationarity is one of the most important concepts in time-series analysis.

The basic idea is:

> The statistical properties of a stationary process do not change when we shift the process through time.

There are two important definitions:

1. Weak stationarity
2. Strong stationarity

---

# 17. Weak Stationarity

A process is **weakly stationary** if:

### Constant mean

$$
E[X_t]=\mu
$$

for every \(t\).

### Time-invariant autocovariance

$$
\operatorname{Cov}(X_s,X_t)
=
\operatorname{Cov}(X_{s+r},X_{t+r})
$$

for every shift \(r\).

In other words, the covariance depends only on the distance between observations, not on their absolute position in time.

Therefore:

$$
\gamma(s,t)
=
\gamma(s-t)
$$

or, using the lag:

$$
\gamma(h)
$$

---

# 18. Strong Stationarity

Strong stationarity is a stronger requirement.

For any finite collection of time points:

$$
t_1,t_2,\ldots,t_k
$$

the joint distribution must remain unchanged after shifting all time points by \(r\):

$$
(X_{t_1},...,X_{t_k})
\overset{d}{=}
(X_{t_1+r},...,X_{t_k+r})
$$

Therefore, strong stationarity concerns the **entire joint distribution**, not just its first two moments.

### Practical distinction

| Weak Stationarity              | Strong Stationarity                                   |
| ------------------------------ | ----------------------------------------------------- |
| Constant mean                  | Entire distribution invariant                         |
| Covariance depends only on lag | Joint distribution depends only on relative positions |
| Uses first and second moments  | Uses full distribution                                |
| Commonly used in this course   | Stronger theoretical condition                        |

---

# 19. Why Stationarity Matters

Suppose we want to estimate the mean.

We might calculate:

$$
\bar X
=
\frac{1}{T}
\sum_{t=1}^{T}X_t
$$

This only makes meaningful sense as an estimator of **one common mean** if the mean does not change with time.

If:

$$
E[X_t]=\mu_t
$$

and \(\mu_t\) changes over time, averaging observations from different time periods mixes different means.

Therefore, stationarity gives us a stable statistical environment in which we can estimate properties such as:

* Mean
* Variance
* Autocovariance
* Autocorrelation

---

# 20. Lag Representation

For a stationary process:

$$
\gamma(s,t)
=
\gamma(s+r,t+r)
$$

We can shift both time points until one of them becomes zero.

Therefore, autocovariance depends only on their difference:

$$
h=s-t
$$

and we can write:

$$
\gamma(h)
$$

where \(h\) is called the **lag**.

This is a fundamental simplification in time-series analysis.

Instead of:

$$
\gamma(s,t)
$$

we work with:

$$
\gamma(h)
$$

---

# 21. Properties of Stationary Autocovariance

For a stationary process:

### Symmetry

$$
\gamma(h)=\gamma(-h)
$$

### Maximum at zero lag

$$
|\gamma(h)|\leq\gamma(0)
$$

because:

$$
\gamma(0)=\operatorname{Var}(X_t)
$$

Thus:

$$
|\gamma(h)|
\leq
\operatorname{Var}(X_t)
$$

This follows from the Cauchy-Schwarz inequality.

---

# 22. Non-Stationary Example

Consider:

$$
X_t=a+bt+Y_t
$$

where \(Y_t\) is stationary with mean zero.

The expected value is:

$$
E[X_t]
=
a+bt
$$

Because the mean depends on \(t\):

$$
E[X_t]\neq\text{constant}
$$

Therefore:

$$
X_t
$$

is **not stationary**.

However:

$$
X_t-a-bt
=
Y_t
$$

is stationary.

This demonstrates an important practical idea:

> A non-stationary time series may sometimes be transformed into a stationary series by removing a deterministic trend.

---

# 23. Python: Stationary vs Non-Stationary Process

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

n = 300
t = np.arange(n)

# Stationary noise
y = np.random.normal(0, 1, n)

# Add deterministic trend
a = 5
b = 0.05

x = a + b * t + y

plt.plot(t, x)
plt.xlabel("Time")
plt.ylabel("X")
plt.title("Non-Stationary Series with Deterministic Trend")
plt.show()
```

Remove the trend:

```python
detrended = x - (a + b * t)

plt.plot(t, detrended)
plt.xlabel("Time")
plt.ylabel("Detrended X")
plt.title("Stationary Component After Removing Trend")
plt.show()
```

The first series has a changing mean, while the second is centered around a constant level.

---

# 24. Cross-Covariance

Autocovariance compares a time series with itself.

Cross-covariance compares **two different time series**.

For processes \(X_t\) and \(Y_t\):

$$
K_{XY}(s,t)
=
\operatorname{Cov}(X_s,Y_t)
$$

This can help answer questions such as:

> Does movement in one time series relate to movement in another?

For example:

* Oil prices
* Gasoline prices

We may also investigate whether one series is related to another at different time offsets.

---

# 25. Cross-Correlation

Cross-correlation is the normalized cross-covariance:

$$
\rho_{XY}(s,t)
=
\frac{
\operatorname{Cov}(X_s,Y_t)
}{
\sqrt{
\operatorname{Var}(X_s)
\operatorname{Var}(Y_t)
}
}
$$

The square root is important because the denominator is the square root of the product of the two variances.

Cross-correlation becomes particularly useful when investigating **lags and lead-lag relationships**.

---

# 26. Joint Stationarity

Two time series can also be considered jointly stationary.

For \(X_t\) and \(Y_t\), we need:

1. \(X_t\) to be stationary.
2. \(Y_t\) to be stationary.
3. Their cross-covariance to remain unchanged under simultaneous time shifts.

That is:

$$
K_{XY}(s,t)
=
K_{XY}(s+r,t+r)
$$

This extends the idea of stationarity from one time series to multiple related time series.

---

# 27. Estimating the Mean

Suppose:

$$
X_1,X_2,\ldots,X_T
$$

is a weakly stationary time series with:

$$
E[X_t]=\mu
$$

The natural estimator is the sample mean:

$$
\boxed{
\hat\mu
=
\frac{1}{T}
\sum_{t=1}^{T}X_t
}
$$

The estimator is unbiased:

$$
E[\hat\mu]=\mu
$$

---

# 28. IID Case vs Time-Series Case

In classical statistics, if observations are IID:

$$
\operatorname{Var}(\bar X)
=
\frac{\sigma^2}{T}
$$

As \(T\) increases, the variance decreases.

But time-series observations are usually **dependent**.

Therefore:

$$
\operatorname{Var}(\bar X)
$$

must account for covariance between different observations.

---

# 29. Variance of the Sample Mean for a Time Series

Start with:

$$
\bar X
=
\frac{1}{T}
\sum_{t=1}^{T}X_t
$$

Then:

$$
\operatorname{Var}(\bar X)
=
\frac{1}{T^2}
\sum_{t=1}^{T}
\sum_{s=1}^{T}
\operatorname{Cov}(X_t,X_s)
$$

For a stationary process:

$$
\operatorname{Cov}(X_t,X_s)
=
\gamma(|t-s|)
$$

Therefore:

$$
\boxed{
\operatorname{Var}(\bar X)
=
\frac{\gamma(0)}{T}
+
\frac{2}{T}
\sum_{h=1}^{T-1}
\left(1-\frac{h}{T}\right)
\gamma(h)
}
$$

This is one of the most important results of the lecture.

---

# 30. Why the Extra Term Matters

For IID observations:

$$
\gamma(h)=0
$$

for all:

$$
h>0
$$

Therefore:

$$
\operatorname{Var}(\bar X)
=
\frac{\gamma(0)}{T}
=
\frac{\sigma^2}{T}
$$

But for dependent time-series observations:

$$
\gamma(h)\neq0
$$

and the additional autocovariance terms contribute to the variance.

If the autocovariances are positive, the variance of the sample mean becomes larger than the IID result.

### Key idea

> Dependence between observations reduces the amount of independent information contained in the sample.

---

# 31. Python: Sample Mean Variance Under Dependence

```python
import numpy as np

np.random.seed(42)

def simulate_ar1(n, theta, sigma=1.0):
    x = np.zeros(n)

    for t in range(1, n):
        noise = np.random.normal(0, sigma)
        x[t] = theta * x[t - 1] + noise

    return x


n = 100
theta = 0.8

x = simulate_ar1(n, theta)

sample_mean = np.mean(x)

print("Sample mean:", sample_mean)
```

Compare an IID process with an AR(1) process:

```python
np.random.seed(42)

n = 100

iid = np.random.normal(size=n)
ar1 = simulate_ar1(n, theta=0.8)

print("IID mean:", np.mean(iid))
print("AR(1) mean:", np.mean(ar1))

print("IID variance:", np.var(iid))
print("AR(1) variance:", np.var(ar1))
```

The important difference is not simply the sample variance itself, but the **dependence structure** between observations.

---

# 32. Visualizing Autocorrelation of an AR(1)

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

x = simulate_ar1(1000, theta=0.8)

lags = np.arange(31)
acf = autocorrelation(x, 30)

theoretical_acf = 0.8 ** lags

plt.stem(lags, acf, label="Sample ACF")
plt.plot(lags, theoretical_acf, label="Theoretical ACF")

plt.xlabel("Lag")
plt.ylabel("Autocorrelation")
plt.title("AR(1) Autocorrelation")
plt.legend()
plt.show()
```

The theoretical relationship is:

$$
\rho(h)=0.8^{|h|}
$$

The sample autocorrelation should approximately follow this pattern.

---

# 33. Core Formulas

## Covariance

$$
\operatorname{Cov}(X,Y)
=
E[(X-E[X])(Y-E[Y])]
$$

## Autocovariance

$$
\gamma(s,t)
=
\operatorname{Cov}(X_s,X_t)
$$

## Stationary autocovariance

$$
\gamma(h)
=
\operatorname{Cov}(X_t,X_{t+h})
$$

## Autocorrelation

$$
\rho(h)
=
\frac{\gamma(h)}{\gamma(0)}
$$

## AR(1) with drift

$$
X_t=a+\theta X_{t-1}+W_t
$$

## AR(1) mean

$$
\mu=
\frac{a}{1-\theta}
$$

## AR(1) variance

$$
\gamma(0)
=
\frac{\sigma^2}{1-\theta^2}
$$

## AR(1) autocovariance

$$
\gamma(h)
=
\frac{\sigma^2}{1-\theta^2}
\theta^{|h|}
$$

## AR(1) autocorrelation

$$
\rho(h)=\theta^{|h|}
$$

## Sample mean

$$
\hat\mu
=
\frac{1}{T}\sum_{t=1}^{T}X_t
$$

## Variance of sample mean

$$
\operatorname{Var}(\bar X)
=
\frac{\gamma(0)}{T}
+
\frac{2}{T}
\sum_{h=1}^{T-1}
\left(1-\frac{h}{T}\right)\gamma(h)
$$

---

# 34. Key Takeaways

The central progression of Lecture 2 is:

```text
Covariance
    ↓
Autocovariance
    ↓
Autocorrelation
    ↓
Stationarity
    ↓
Lag-based representation
    ↓
Cross-covariance / Cross-correlation
    ↓
Statistical estimation
```

The most important conceptual points are:

* **Autocovariance** measures dependence between observations of the same time series at different times.
* **Autocorrelation** is the normalized autocovariance.
* **Stationarity** means that important statistical properties remain stable under time shifts.
* For weak stationarity, the **mean is constant** and the **autocovariance depends only on lag**.
* An AR(1) with \(|\theta|<1\) has a stationary solution.
* For AR(1), autocorrelation decays geometrically.
* Time-series observations are generally dependent, so the variance of the sample mean contains covariance terms.
* Positive autocorrelation generally makes the sample mean less precise than the IID formula would suggest.
* Stationarity provides the stable statistical structure needed for estimation.

---

# 35. Suggested Practice

### Exercise 1 — Covariance

Generate two variables with:

1. Positive covariance.
2. Negative covariance.
3. Approximately zero covariance.

Plot each relationship.

### Exercise 2 — White Noise

Generate Gaussian white noise and calculate:

$$
\gamma(0),\gamma(1),\ldots,\gamma(20)
$$

Then plot the autocovariance.

### Exercise 3 — AR(1)

Generate AR(1) processes with:

$$
\theta=0.2,\quad0.5,\quad0.9
$$

Compare their autocorrelation functions.

### Exercise 4 — Stationarity

Create:

$$
X_t=5+0.05t+\epsilon_t
$$

and determine why it is non-stationary.

Then remove the deterministic trend and examine the resulting series.

### Exercise 5 — Dependence

Simulate IID data and an AR(1) process with:

$$
\theta=0.8
$$

Compare their sample means and autocorrelation structures.

---

# 36. Connection to the Next Lecture

The next step is moving from **theoretical properties** to **estimation from real data**.

The key questions become:

> How do we estimate autocovariance from observations?

> How do we estimate autocorrelation?

> How can we determine whether observed data behaves like white noise?

These estimated quantities will become important tools for identifying and diagnosing time-series models.
