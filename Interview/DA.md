Yes. For your **Data Analysis interview-prep README**, I’d structure the 100 Q&A around the areas repeatedly appearing in current analyst interviews: SQL, Python/Pandas, Excel, statistics, EDA/data cleaning, visualization/BI, and business cases. ([Prepare.sh][1])

Here is a concise README you can use directly:

# 📊 Top 100 Data Analysis Interview Questions & Answers

A practical collection of **100 Data Analysis interview questions and concise answers**, covering the core skills expected from Data Analysts: **SQL, Python/Pandas, Excel, Statistics, EDA, Data Cleaning, Visualization, BI, and Business Analysis**.

> 🎯 Goal: Build strong fundamentals and answer common Data Analyst interview questions clearly and confidently.

---

## 📚 Topics

| # | Topic                      | Questions |
| - | -------------------------- | --------: |
| 1 | Data Analysis Fundamentals |      1–15 |
| 2 | Data Cleaning & EDA        |     16–30 |
| 3 | Statistics & Probability   |     31–50 |
| 4 | SQL                        |     51–70 |
| 5 | Python & Pandas            |     71–82 |
| 6 | Excel                      |     83–90 |
| 7 | Visualization & BI         |     91–95 |
| 8 | Business & Case Analysis   |    96–100 |

---

# 1. Data Analysis Fundamentals

### 1. What is Data Analysis?

**Answer:** The process of collecting, cleaning, transforming, exploring, and interpreting data to extract useful information and support decisions.

### 2. Why is Data Analysis important?

**Answer:** It helps organizations understand performance, identify problems, discover patterns, and make evidence-based decisions.

### 3. What is the difference between data and information?

**Answer:** Data is raw facts; information is processed data with meaningful context.

### 4. What are structured and unstructured data?

**Answer:** Structured data follows a defined schema, such as SQL tables. Unstructured data includes text, images, audio, and video.

### 5. What are qualitative and quantitative data?

**Answer:** Qualitative data describes categories or qualities; quantitative data represents measurable numerical values.

### 6. What is descriptive analysis?

**Answer:** Analysis that summarizes what has already happened using metrics such as mean, totals, percentages, and distributions.

### 7. What is diagnostic analysis?

**Answer:** Analysis focused on understanding **why** something happened.

### 8. What is predictive analysis?

**Answer:** Using historical data and statistical/ML methods to estimate future outcomes.

### 9. What is prescriptive analysis?

**Answer:** Analysis that recommends actions based on predicted outcomes and constraints.

### 10. What is EDA?

**Answer:** Exploratory Data Analysis is the process of examining data using statistics and visualizations to discover patterns, anomalies, relationships, and data-quality problems.

### 11. What is a dataset?

**Answer:** A structured collection of observations and variables used for analysis.

### 12. What is a variable?

**Answer:** A measurable characteristic represented by a column or feature.

### 13. What is an observation?

**Answer:** A single record or row representing one entity, event, or measurement.

### 14. What is data granularity?

**Answer:** The level of detail represented by each observation, such as one row per customer, order, or transaction.

### 15. What is a KPI?

**Answer:** A Key Performance Indicator is a measurable value used to evaluate progress toward a business objective.

---

# 2. Data Cleaning & EDA

### 16. What is data cleaning?

**Answer:** Identifying and correcting missing, duplicate, invalid, inconsistent, or incorrectly formatted data.

### 17. Why is data cleaning important?

**Answer:** Poor-quality input can produce misleading analysis and incorrect business decisions.

### 18. How do you handle missing values?

**Answer:** First investigate why they are missing. Depending on the situation, remove records, impute values, use a separate category, or leave them missing.

### 19. What is imputation?

**Answer:** Replacing missing values with estimated values such as the mean, median, mode, or model-based estimate.

### 20. When should you use median instead of mean for imputation?

**Answer:** Often when the variable is skewed or contains extreme values because the median is more robust to outliers.

### 21. How do you detect duplicates?

**Answer:** Compare records using unique identifiers or combinations of columns and use tools such as `duplicated()` in Pandas.

### 22. What is an outlier?

**Answer:** An observation unusually far from the rest of the data.

### 23. How can you detect outliers?

**Answer:** Common methods include IQR, Z-scores, boxplots, scatterplots, and domain-specific thresholds.

### 24. Should every outlier be removed?

**Answer:** No. First determine whether it represents an error, a legitimate rare event, or an important business case.

### 25. What is data validation?

**Answer:** Checking whether data satisfies expected rules, formats, ranges, relationships, and constraints.

### 26. What is data profiling?

**Answer:** Systematically examining columns, types, missingness, uniqueness, distributions, and quality issues.

### 27. What is normalization?

**Answer:** In statistics/ML, transforming numerical variables to a common range, often 0–1.

### 28. What is standardization?

**Answer:** Transforming a variable so it has approximately mean 0 and standard deviation 1.

### 29. What is skewness?

**Answer:** A measure of asymmetry in a distribution.

### 30. What is the typical EDA workflow?

**Answer:** Understand the business question → inspect data → validate quality → clean → summarize → analyze distributions → investigate relationships → visualize → generate insights.

---

# 3. Statistics & Probability

### 31. What is the mean?

**Answer:** The arithmetic average:
`sum(values) / number_of_values`.

### 32. What is the median?

**Answer:** The middle value after sorting observations.

### 33. What is the mode?

**Answer:** The most frequently occurring value.

### 34. When is median better than mean?

**Answer:** When data is strongly skewed or contains influential outliers.

### 35. What is variance?

**Answer:** A measure of how far observations vary from the mean.

### 36. What is standard deviation?

**Answer:** The square root of variance and a measure of typical spread around the mean.

### 37. What is correlation?

**Answer:** A measure of the strength and direction of association between variables.

### 38. Does correlation imply causation?

**Answer:** No. Two variables can move together because of coincidence, confounding variables, reverse causality, or another underlying factor.

### 39. What is a population?

**Answer:** The complete group of entities or observations of interest.

### 40. What is a sample?

**Answer:** A subset of the population used to draw conclusions about that population.

### 41. What is sampling bias?

**Answer:** Systematic distortion caused when the sample does not adequately represent the target population.

### 42. What is a probability?

**Answer:** A numerical measure between 0 and 1 representing the likelihood of an event.

### 43. What is a normal distribution?

**Answer:** A symmetric, bell-shaped distribution characterized by its mean and standard deviation.

### 44. What is the Central Limit Theorem?

**Answer:** Under suitable conditions, the sampling distribution of the sample mean approaches a normal distribution as sample size increases.

### 45. What is a hypothesis?

**Answer:** A testable statement about a population parameter or relationship.

### 46. What are the null and alternative hypotheses?

**Answer:** The null hypothesis represents the baseline/no-effect claim; the alternative represents the effect or difference being investigated.

### 47. What is a p-value?

**Answer:** The probability, assuming the null hypothesis is true, of observing a result at least as extreme as the one obtained.

### 48. What is statistical significance?

**Answer:** Evidence that a result would be relatively unlikely under the specified null hypothesis, according to a chosen significance threshold.

### 49. What is a confidence interval?

**Answer:** An interval produced by a statistical procedure that quantifies uncertainty around an estimated parameter.

### 50. What is A/B testing?

**Answer:** A controlled experiment comparing two variants to determine whether a measurable outcome differs between them.

---

# 4. SQL

### 51. What is SQL?

**Answer:** Structured Query Language used to store, retrieve, manipulate, and analyze relational data.

### 52. What is `SELECT`?

**Answer:** Retrieves specified columns or expressions from a table.

```sql
SELECT name, salary
FROM employees;
```

### 53. What is `WHERE`?

**Answer:** Filters individual rows before aggregation.

```sql
SELECT *
FROM orders
WHERE amount > 100;
```

### 54. What is `GROUP BY`?

**Answer:** Groups rows so aggregate functions can be calculated for each group.

```sql
SELECT customer_id, SUM(amount)
FROM orders
GROUP BY customer_id;
```

### 55. What is `HAVING`?

**Answer:** Filters groups after aggregation.

```sql
SELECT customer_id, SUM(amount) AS total
FROM orders
GROUP BY customer_id
HAVING SUM(amount) > 1000;
```

### 56. What is the difference between WHERE and HAVING?

**Answer:** `WHERE` filters rows before grouping; `HAVING` filters groups after aggregation.

### 57. What is an INNER JOIN?

**Answer:** Returns rows with matching values in both tables.

### 58. What is a LEFT JOIN?

**Answer:** Returns all rows from the left table and matching rows from the right table; unmatched right-side values become `NULL`.

### 59. What is a primary key?

**Answer:** A column or combination of columns that uniquely identifies each row.

### 60. What is a foreign key?

**Answer:** A column that references a key in another table and establishes a relationship between tables.

### 61. What is `COUNT(*)`?

**Answer:** Counts rows.

### 62. What is `COUNT(column)`?

**Answer:** Counts non-NULL values in that column.

### 63. What is `DISTINCT`?

**Answer:** Removes duplicate combinations from the selected result.

### 64. How do you find the top 5 customers by spending?

```sql
SELECT customer_id,
       SUM(amount) AS total_spend
FROM orders
GROUP BY customer_id
ORDER BY total_spend DESC
LIMIT 5;
```

### 65. What is a subquery?

**Answer:** A query nested inside another SQL statement.

### 66. What is a CTE?

**Answer:** A Common Table Expression temporarily names a query result using `WITH`, improving readability and organization.

### 67. What is a window function?

**Answer:** A function that calculates across related rows while preserving individual rows.

```sql
SELECT employee,
       salary,
       RANK() OVER (ORDER BY salary DESC) AS salary_rank
FROM employees;
```

### 68. What is the difference between RANK and ROW_NUMBER?

**Answer:** `ROW_NUMBER()` gives every row a unique sequential number; `RANK()` gives tied rows the same rank and leaves gaps afterward.

### 69. How do you find duplicate values?

```sql
SELECT email, COUNT(*) AS cnt
FROM customers
GROUP BY email
HAVING COUNT(*) > 1;
```

### 70. How do you calculate a percentage of total?

```sql
SELECT
    category,
    SUM(sales) AS sales,
    100.0 * SUM(sales) / SUM(SUM(sales)) OVER () AS pct_total
FROM orders
GROUP BY category;
```

---

# 5. Python & Pandas

### 71. What is Pandas?

**Answer:** A Python library for data manipulation, analysis, and tabular data processing.

### 72. What is a DataFrame?

**Answer:** A two-dimensional labeled data structure consisting of rows and columns.

### 73. How do you inspect a DataFrame?

```python
df.head()
df.shape
df.info()
df.describe()
```

### 74. How do you find missing values?

```python
df.isna().sum()
```

### 75. How do you remove duplicates?

```python
df = df.drop_duplicates()
```

### 76. How do you filter rows?

```python
df[df["sales"] > 1000]
```

### 77. What is `groupby()`?

**Answer:** It splits data into groups and allows aggregation or transformation within each group.

```python
df.groupby("region")["sales"].sum()
```

### 78. What is the difference between `loc` and `iloc`?

**Answer:** `loc` primarily selects using labels; `iloc` selects using integer positions.

### 79. What is `merge()`?

**Answer:** Pandas' method for combining DataFrames based on matching keys.

```python
df.merge(customers, on="customer_id", how="left")
```

### 80. What is `concat()`?

**Answer:** Combines DataFrames along rows or columns.

### 81. What is `apply()`?

**Answer:** Applies a function across Series values or DataFrame rows/columns.

### 82. How do you calculate multiple aggregations?

```python
df.groupby("category").agg(
    sales_sum=("sales", "sum"),
    sales_mean=("sales", "mean"),
    orders=("order_id", "count")
)
```

---

# 6. Excel

### 83. What is a Pivot Table?

**Answer:** A tool for quickly summarizing and aggregating large datasets by dimensions and measures.

### 84. What is XLOOKUP?

**Answer:** A lookup function that searches for a value and returns a corresponding value from another range.

### 85. What is the difference between XLOOKUP and VLOOKUP?

**Answer:** XLOOKUP is more flexible because it can look left or right and does not depend on a fixed column index.

### 86. What is SUMIFS?

**Answer:** Calculates a sum based on multiple conditions.

### 87. What is COUNTIFS?

**Answer:** Counts cells or rows satisfying multiple criteria.

### 88. What is conditional formatting?

**Answer:** Automatically formats cells based on specified rules or values.

### 89. What is an Excel Table?

**Answer:** A structured range that provides automatic filtering, formatting, references, and expansion.

### 90. How do you clean data in Excel?

**Answer:** Check duplicates, missing values, data types, inconsistent categories, whitespace, invalid values, and formatting.

---

# 7. Visualization & BI

### 91. When should you use a line chart?

**Answer:** Mainly for showing trends or changes over an ordered dimension such as time.

### 92. When should you use a bar chart?

**Answer:** For comparing values across discrete categories.

### 93. When should you use a scatter plot?

**Answer:** To examine relationships between two numerical variables and identify patterns or outliers.

### 94. What makes a good dashboard?

**Answer:** Clear KPIs, appropriate visualizations, logical layout, useful filters, consistent definitions, and minimal unnecessary clutter.

### 95. What is data storytelling?

**Answer:** Communicating data findings through a clear combination of context, evidence, visualization, and business meaning.

---

# 8. Business & Case Analysis

### 96. How would you approach a new business problem?

**Answer:**
**Business question → KPI → Data → Data quality → EDA → Analysis → Insight → Recommendation → Measurement.**

### 97. Sales dropped 20%. What would you investigate?

**Answer:**

1. Validate the metric and data.
2. Compare time periods.
3. Segment by product, region, channel, and customer.
4. Check price, volume, promotions, and availability.
5. Investigate external factors.
6. Identify the largest contributors.
7. Test possible explanations.

### 98. A dashboard shows revenue increased but profit decreased. Why?

**Answer:** Possible causes include higher costs, lower margins, discounts, product mix changes, shipping costs, returns, or increased operating expenses.

### 99. How do you communicate an unexpected finding?

**Answer:** Clearly state the finding, validate the data, explain the evidence, identify uncertainty, provide possible causes, and recommend the next analysis or action.

### 100. What makes a strong Data Analyst?

**Answer:** A strong analyst combines **SQL, statistics, data manipulation, visualization, business understanding, critical thinking, and communication**. The goal is not merely to produce numbers, but to turn reliable data into useful decisions.

---

# 🧠 Interview Framework

For scenario questions, use:

```text
1. Clarify the business question
2. Define the KPI
3. Understand the data
4. Check data quality
5. Explore the data
6. Segment the problem
7. Analyze relationships
8. Validate the finding
9. Explain the business impact
10. Recommend next steps
```

# 🛠️ Core Tools to Practice

* **SQL:** PostgreSQL / MySQL
* **Python:** NumPy / Pandas
* **Visualization:** Matplotlib / Seaborn
* **BI:** Power BI / Tableau
* **Spreadsheet:** Excel
* **Statistics:** Descriptive statistics / Probability / Hypothesis testing
* **Analysis:** EDA / A-B testing / Regression / Time Series

# 🎯 Priority Order

If preparing for a Data Analyst interview, prioritize:

**SQL → EDA & Data Cleaning → Statistics → Python/Pandas → Excel → Visualization/Power BI → Business Cases**

Current interview-prep resources similarly emphasize SQL, Python/Pandas, statistics, Excel, visualization, and business reasoning as the core areas tested in analyst interviews. ([Prepare.sh][1])

# 📌 Recommended Practice

Don't only memorize these answers.

For each topic:

**Learn → Solve → Explain → Apply to a dataset → Repeat**

The strongest preparation is to take real datasets and reproduce the questions using **SQL + Pandas + visualization + business interpretation**.

This is intentionally **concise enough to use as a GitHub README**, while still covering the 100-question interview scope. ([Mahila Bharti][2])

If you want, I can also turn this into a **much stronger “Top 100 Data Analysis Questions” repository structure with `easy / medium / hard`, SQL coding questions, Python coding questions, and real case-study questions**.

[1]: https://prepare.sh/articles/data-analysis-interview-questions-and-answers?utm_source=chatgpt.com "Data Analysis Interview Questions, With Worked Answers | Prepare.sh"
[2]: https://mahilabharti.in/data-analyst-interview-questions/?utm_source=chatgpt.com "Top 100 Data Analyst Interview Questions&A: Excel SQL Python"

---

# 💼 50 Business Questions for Data Analysis Interviews

A practical collection of **50 business-focused Data Analyst interview questions and concise answers** covering sales, marketing, customers, products, operations, finance, supply chain, and decision-making.

---

## 📈 Sales & Revenue

### 1. Sales dropped 20%. How would you investigate?

**Answer:** Validate the metric, compare periods, segment by product/region/channel/customer, check price and volume, identify the largest contributors, and investigate possible causes.

### 2. Revenue increased but profit decreased. Why?

**Answer:** Possible causes include higher costs, discounts, lower margins, product-mix changes, shipping costs, returns, or operating expenses.

### 3. Which products generate the most revenue?

**Answer:** Calculate total revenue by product and compare their contribution to overall revenue.

### 4. Which products are most profitable?

**Answer:** Compare revenue with product-level costs and calculate profit or profit margin.

### 5. Sales are growing. How do you determine whether growth is healthy?

**Answer:** Examine profit, margins, customer retention, acquisition costs, product mix, and whether growth is sustainable.

### 6. How would you forecast next month's sales?

**Answer:** Analyze historical trends, seasonality, promotions, external factors, and use an appropriate forecasting method.

### 7. How would you identify the main drivers of revenue growth?

**Answer:** Decompose revenue into factors such as customers, orders, average order value, price, volume, and product mix.

### 8. Average order value increased. What could explain it?

**Answer:** Customers may be buying more items, purchasing more expensive products, responding to bundles, or experiencing price increases.

### 9. Revenue is increasing but the number of customers is falling. What would you investigate?

**Answer:** Check customer spending, retention, pricing, customer segments, and whether a smaller group of customers is generating more revenue.

### 10. How would you identify underperforming sales regions?

**Answer:** Compare revenue, growth, profit, customers, orders, and relevant market-size or target metrics across regions.

---

## 👥 Customers

### 11. How would you measure customer retention?

**Answer:** Calculate the percentage of customers who remain active or purchase again during a defined period.

### 12. What is customer churn?

**Answer:** The rate at which customers stop using or purchasing from a business during a specified period.

### 13. Churn increased suddenly. What would you investigate?

**Answer:** Segment churn by customer type, product, region, acquisition channel, tenure, complaints, pricing, and recent changes.

### 14. How would you identify the most valuable customers?

**Answer:** Use metrics such as revenue, profit, purchase frequency, retention, lifetime value, and recency.

### 15. What is Customer Lifetime Value?

**Answer:** An estimate of the value a customer generates throughout their relationship with the business.

### 16. How would you segment customers?

**Answer:** Use meaningful characteristics such as demographics, behavior, purchase frequency, monetary value, geography, or lifecycle stage.

### 17. New customers increased but total revenue did not. Why?

**Answer:** New customers may have lower spending, low retention, high discounts, or a lower conversion rate.

### 18. How would you identify customers at risk of churn?

**Answer:** Analyze declining purchase frequency, reduced activity, complaints, usage changes, and other historical churn indicators.

### 19. Customers are buying less frequently. What would you investigate?

**Answer:** Examine product satisfaction, pricing, competition, seasonality, customer segments, marketing activity, and purchasing behavior.

### 20. How would you measure customer satisfaction?

**Answer:** Use metrics such as CSAT, NPS, ratings, complaints, returns, reviews, and repeat-purchase behavior.

---

## 📣 Marketing

### 21. Which marketing channel generates the most customers?

**Answer:** Compare customers acquired by channel while considering the measurement period and attribution method.

### 22. Which marketing channel is most profitable?

**Answer:** Compare profit or contribution margin against the costs associated with each channel.

### 23. What is Customer Acquisition Cost (CAC)?

**Answer:** The average cost required to acquire a new customer.

### 24. CAC increased by 30%. What would you investigate?

**Answer:** Check advertising costs, conversion rates, campaign performance, channel mix, audience quality, and attribution changes.

### 25. How would you measure campaign performance?

**Answer:** Compare impressions, clicks, conversions, revenue, CAC, ROAS, retention, and profit against the campaign objective.

### 26. What is conversion rate?

**Answer:** The percentage of eligible users who complete a desired action.

### 27. Website traffic increased but sales did not. Why?

**Answer:** Traffic quality may have decreased, conversion may have fallen, or there may be problems with pricing, product availability, UX, or checkout.

### 28. How would you evaluate an advertising campaign?

**Answer:** Compare outcomes with costs and, where possible, use experiments or appropriate controls to estimate incremental impact.

### 29. How would you determine whether a promotion worked?

**Answer:** Compare sales and profit against an appropriate baseline or control while accounting for seasonality and other factors.

### 30. What is ROAS?

**Answer:** Return on Ad Spend: revenue attributed to advertising divided by advertising spend.

---

## 📦 Products & Operations

### 31. A product has high sales but low profit. What would you investigate?

**Answer:** Examine unit cost, discounts, returns, shipping, promotions, pricing, and product mix.

### 32. Product returns increased. How would you investigate?

**Answer:** Segment returns by product, supplier, region, reason, customer type, and time period.

### 33. How would you identify products that should be discontinued?

**Answer:** Analyze profitability, demand, growth, inventory costs, returns, strategic importance, and customer impact.

### 34. Inventory levels are increasing. What could be happening?

**Answer:** Demand may have fallen, purchasing may be excessive, forecasting may be inaccurate, or products may be slow-moving.

### 35. How would you identify slow-moving inventory?

**Answer:** Analyze sales velocity, days of inventory, turnover, and time since the last sale.

### 36. Delivery times increased. What would you investigate?

**Answer:** Examine suppliers, warehouses, transportation, order volume, geography, staffing, and operational bottlenecks.

### 37. How would you measure operational efficiency?

**Answer:** Use metrics such as processing time, cycle time, throughput, utilization, defect rate, cost per order, and on-time delivery.

### 38. On-time delivery decreased. How would you investigate?

**Answer:** Segment delays by carrier, warehouse, supplier, region, product, order type, and time period.

### 39. Customer complaints increased. What would you analyze?

**Answer:** Categorize complaints, identify trends, compare products/locations/channels, and investigate whether operational changes correlate with the increase.

### 40. How would you identify an operational bottleneck?

**Answer:** Map the process, measure each stage's throughput and processing time, and identify where work accumulates or capacity is constrained.

---

## 💰 Finance & Business Performance

### 41. What is profit margin?

**Answer:** Profit expressed as a percentage of revenue.

### 42. Revenue increased but margin decreased. What could cause this?

**Answer:** Rising costs, lower prices, heavier discounts, or a shift toward lower-margin products.

### 43. How would you analyze monthly business performance?

**Answer:** Compare revenue, costs, profit, customers, orders, margins, and KPIs against previous periods and targets.

### 44. How would you identify the largest cost drivers?

**Answer:** Break total costs into categories and calculate each category's contribution to total costs.

### 45. A company's costs increased 15%. How would you investigate?

**Answer:** Compare costs by category, supplier, product, region, and time period, then identify which components explain most of the increase.

---

## 🧠 Business Case Questions

### 46. The CEO asks: "What should we improve?"

**Answer:** First clarify the business objective, identify relevant KPIs, analyze performance gaps, find their largest drivers, and quantify potential impact.

### 47. A manager asks for a dashboard. What would you ask first?

**Answer:** Ask who will use it, what decisions they need to make, which KPIs matter, how frequently they need the information, and what actions should follow from the dashboard.

### 48. You discover a surprising pattern. What do you do?

**Answer:** Validate the data and methodology first, investigate possible explanations, test whether the pattern persists across relevant segments, and communicate the finding with appropriate uncertainty.

### 49. Two departments report different numbers for the same KPI. What would you do?

**Answer:** Compare their definitions, filters, time periods, data sources, joins, calculations, and business rules before determining why the numbers differ.

### 50. How do you turn analysis into a business recommendation?

**Answer:**

**Finding → Evidence → Business impact → Possible actions → Trade-offs → Measurement plan**

The recommendation should connect the analysis to a specific business decision and measurable outcome.

---

# 🎯 Business Analysis Framework

For almost any business case, use:

```text
1. Understand the business objective
2. Define the KPI
3. Establish the baseline
4. Validate the data
5. Segment the problem
6. Identify the largest drivers
7. Investigate possible causes
8. Quantify the impact
9. Consider alternatives and trade-offs
10. Recommend an action
11. Define how success will be measured
```

# 🔑 Key Business Metrics

| Area                | Metrics                                             |
| ------------------- | --------------------------------------------------- |
| Sales               | Revenue, Orders, AOV, Growth                        |
| Profitability       | Profit, Margin, Contribution                        |
| Customers           | Retention, Churn, LTV                               |
| Marketing           | CAC, Conversion Rate, ROAS                          |
| Product             | Adoption, Usage, Returns                            |
| Operations          | Cycle Time, Throughput, Defect Rate                 |
| Supply Chain        | Inventory Turnover, Stockout Rate, On-Time Delivery |
| Customer Experience | CSAT, NPS, Complaints                               |
| Finance             | Revenue, Costs, Profit, Cash Flow                   |

# 💡 Golden Rule

> **Don't start with "What data do I have?"**
>
> Start with **"What business decision are we trying to make?"**

A Data Analyst's job is not simply to calculate metrics. It is to connect:

**Business Problem → Data → Analysis → Insight → Decision → Measurable Impact**

---

# 🛒 75 E-Commerce, Marketing & Sales Analytics Questions

A practical collection of **75 business and data-analysis interview questions** focused on **E-commerce, Marketing, Sales, Customers, Products, Conversion, Retention, and Revenue**.

> 🎯 Goal: Learn how to investigate real business problems using data and translate analysis into actionable insights.

---

# 📚 Contents

| # | Topic                          | Questions |
| - | ------------------------------ | --------: |
| 1 | E-Commerce Fundamentals        |      1–10 |
| 2 | Sales & Revenue                |     11–25 |
| 3 | Customers & Retention          |     26–38 |
| 4 | Marketing & Acquisition        |     39–52 |
| 5 | Conversion & Product Analytics |     53–63 |
| 6 | Business Cases                 |     64–75 |

---

# 🛒 1. E-Commerce Fundamentals

### 1. What are the most important E-commerce KPIs?

**Answer:** Revenue, orders, AOV, conversion rate, customers, CAC, retention, churn, CLV, profit margin, and return rate.

### 2. What is Gross Merchandise Value (GMV)?

**Answer:** The total value of merchandise sold through a platform before deductions such as refunds, discounts, or fees, depending on the business definition.

### 3. What is the difference between GMV and revenue?

**Answer:** GMV represents the value of transactions, while revenue represents the amount recognized by the business under its accounting model.

### 4. What is Average Order Value (AOV)?

**Answer:**

```text
AOV = Total Revenue / Number of Orders
```

### 5. What is conversion rate?

**Answer:**

```text
Conversion Rate = Conversions / Eligible Visitors × 100
```

### 6. What is cart abandonment?

**Answer:** The percentage of users who add products to their cart but do not complete the purchase.

### 7. What is checkout abandonment?

**Answer:** The percentage of users who begin checkout but fail to complete the transaction.

### 8. What is repeat purchase rate?

**Answer:** The proportion of customers who make more than one purchase during a defined period.

### 9. What is customer lifetime value?

**Answer:** An estimate of the value a customer generates over the duration of their relationship with the business.

### 10. What is an E-commerce funnel?

**Answer:**

```text
Traffic
   ↓
Product View
   ↓
Add to Cart
   ↓
Checkout
   ↓
Purchase
```

The funnel helps identify where customers leave the buying process.

---

# 💰 2. Sales & Revenue

### 11. Revenue decreased 15%. How would you investigate?

**Answer:**

```text
Validate metric
→ Compare periods
→ Segment revenue
→ Analyze orders
→ Analyze AOV
→ Analyze customers
→ Identify largest drivers
```

### 12. What can cause revenue to increase?

**Answer:** More customers, more orders per customer, higher AOV, higher prices, or a favorable product mix.

### 13. Revenue increased but orders decreased. What could explain this?

**Answer:** AOV may have increased because customers purchased more expensive products or prices increased.

### 14. Revenue increased but profit decreased. Why?

**Answer:** Higher costs, discounts, shipping costs, returns, or a shift toward lower-margin products.

### 15. How would you calculate sales growth?

```text
Growth % =
(Current Sales - Previous Sales)
/
Previous Sales × 100
```

### 16. How would you identify the best-selling products?

**Answer:** Rank products by units sold and revenue, then examine whether "best-selling" means volume, revenue, or profit.

### 17. Is the highest-revenue product always the best product?

**Answer:** No. A product can generate high revenue while having low margins, high returns, or high acquisition costs.

### 18. How would you analyze sales by region?

**Answer:** Compare revenue, orders, customers, AOV, growth, margin, and other relevant KPIs across regions.

### 19. Sales increased after a discount. How do you determine whether the discount worked?

**Answer:** Compare incremental sales and profit against an appropriate baseline or control while accounting for seasonality and other factors.

### 20. How would you identify seasonal sales patterns?

**Answer:** Analyze sales over time and compare equivalent periods across years or seasons.

### 21. What is sales velocity?

**Answer:** The rate at which products or orders are sold during a defined period.

### 22. How would you forecast sales?

**Answer:** Analyze historical trends, seasonality, promotions, product changes, external factors, and select an appropriate forecasting method.

### 23. How would you identify declining products?

**Answer:** Analyze sales trends, growth rates, order volume, customer demand, returns, and product-level performance over time.

### 24. How would you measure sales performance against targets?

**Answer:**

```text
Achievement % = Actual Sales / Target Sales × 100
```

Then investigate the reasons for any gap.

### 25. How would you decompose revenue?

**Answer:**

```text
Revenue
= Customers
× Orders per Customer
× Average Order Value
```

This helps identify which component is driving change.

---

# 👥 3. Customers & Retention

### 26. What is customer retention?

**Answer:** The ability of a business to keep customers active or purchasing over time.

### 27. What is customer churn?

**Answer:** The proportion of customers who stop purchasing or using the service during a defined period.

### 28. How would you calculate churn?

**Answer:**

```text
Churn Rate =
Customers Lost / Customers at Start
× 100
```

The exact definition should match the business context.

### 29. Customer churn increased. What would you investigate?

**Answer:** Segment churn by customer type, product, region, acquisition channel, tenure, complaints, pricing, and recent changes.

### 30. How would you identify loyal customers?

**Answer:** Analyze purchase frequency, recency, lifetime revenue, retention, and repeat-purchase behavior.

### 31. What is RFM analysis?

**Answer:** A customer segmentation method based on:

* **Recency** — how recently they purchased
* **Frequency** — how often they purchase
* **Monetary** — how much they spend

### 32. How would you find high-value customers?

**Answer:** Rank customers using revenue, profit, purchase frequency, retention, and estimated lifetime value.

### 33. New customers increased but revenue stayed flat. Why?

**Answer:** New customers may have lower AOV, lower purchase frequency, poor retention, or heavy discount usage.

### 34. How would you measure repeat purchase behavior?

**Answer:** Track the percentage of customers who make additional purchases and analyze the time between purchases.

### 35. How would you calculate Customer Lifetime Value?

**Answer:** A simplified model can use:

```text
CLV ≈
Average Purchase Value
× Purchase Frequency
× Customer Lifespan
```

More advanced models account for margins, retention, discounting, and acquisition costs.

### 36. How would you identify customers at risk of churn?

**Answer:** Look for declining purchase frequency, reduced engagement, long periods since purchase, complaints, or changes in behavior associated with historical churn.

### 37. How would you compare new and returning customers?

**Answer:** Compare conversion rate, AOV, purchase frequency, revenue, profitability, retention, and lifetime value.

### 38. Why can returning customers have higher conversion rates?

**Answer:** They may already trust the brand, understand the product, and have less uncertainty about purchasing.

---

# 📣 4. Marketing & Acquisition

### 39. What are the main marketing KPIs?

**Answer:** Impressions, reach, clicks, CTR, CPC, conversion rate, CAC, ROAS, revenue, retention, and CLV.

### 40. What is Customer Acquisition Cost (CAC)?

```text
CAC =
Total Acquisition Cost
/
Number of New Customers
```

### 41. What is ROAS?

```text
ROAS =
Attributed Revenue
/
Advertising Cost
```

### 42. What is CTR?

```text
CTR =
Clicks / Impressions × 100
```

### 43. What is CPC?

```text
CPC =
Advertising Cost / Clicks
```

### 44. Which marketing channel generates the most customers?

**Answer:** Compare new customers acquired by channel using a clearly defined attribution methodology.

### 45. Which marketing channel is most profitable?

**Answer:** Compare channel-level profit or contribution margin against acquisition and other relevant costs.

### 46. CAC increased by 30%. What would you investigate?

**Answer:** Check ad costs, conversion rate, traffic quality, channel mix, campaign performance, audience targeting, and attribution.

### 47. Website traffic increased but sales did not. Why?

**Answer:** Traffic quality may have declined, conversion may have decreased, or there may be issues with pricing, products, UX, availability, or checkout.

### 48. How would you compare organic and paid traffic?

**Answer:** Compare traffic, conversion, revenue, CAC, retention, and long-term customer value.

### 49. How would you measure campaign effectiveness?

**Answer:**

```text
Campaign
→ Traffic
→ Engagement
→ Conversion
→ Revenue
→ Cost
→ Profit
→ Retention
```

### 50. How would you determine whether marketing caused an increase in sales?

**Answer:** Ideally use an experiment or suitable control group; simple before/after comparisons can be confounded by seasonality and other changes.

### 51. What is attribution?

**Answer:** The method used to assign credit for a conversion or business outcome to marketing touchpoints.

### 52. Why can marketing attribution be misleading?

**Answer:** Customers may interact with multiple channels, tracking can be incomplete, attribution rules can differ, and correlation does not necessarily establish incremental causation.

---

# 🛍️ 5. Conversion & Product Analytics

### 53. What is funnel analysis?

**Answer:** Examining user progression through sequential stages to identify where users drop out.

### 54. Conversion rate suddenly dropped. What would you investigate?

**Answer:**

```text
Validate tracking
→ Compare devices
→ Compare traffic sources
→ Check product availability
→ Check prices
→ Check UX
→ Check checkout
→ Check technical errors
```

### 55. Add-to-cart rate increased but purchases decreased. What could explain it?

**Answer:** Checkout problems, unexpected costs, shipping fees, payment failures, inventory issues, or lower purchase intent.

### 56. Cart abandonment increased. What would you investigate?

**Answer:** Shipping costs, taxes, payment problems, delivery times, checkout complexity, technical issues, and unexpected fees.

### 57. How would you identify the weakest funnel stage?

**Answer:** Calculate conversion between every consecutive stage and compare the drop-off rates.

### 58. Product views increased but add-to-cart rate decreased. Why?

**Answer:** Traffic quality may have changed, the audience may be less relevant, or product price, presentation, availability, or competitiveness may have changed.

### 59. How would you measure product performance?

**Answer:** Analyze views, conversion, units sold, revenue, margin, returns, reviews, repeat purchases, and inventory behavior.

### 60. How would you identify products frequently bought together?

**Answer:** Analyze transaction-level basket data using co-occurrence or market-basket analysis.

### 61. What is cross-selling?

**Answer:** Encouraging customers to purchase complementary products.

### 62. What is upselling?

**Answer:** Encouraging customers to purchase a higher-value version of a product or service.

### 63. How would you evaluate a recommendation system?

**Answer:** Measure recommendation engagement, conversion, AOV, revenue, retention, and ideally incremental impact using controlled experiments.

---

# 🧠 6. Business Case Questions

### 64. The CEO says: "Sales are falling. Find out why."

**Answer:**

```text
Validate sales
→ Compare time periods
→ Segment by product
→ Segment by region
→ Segment by channel
→ Analyze customers
→ Analyze orders
→ Identify largest contributors
→ Investigate causes
```

### 65. A product has high traffic but low sales. What would you investigate?

**Answer:** Product price, reviews, product quality, availability, competitors, UX, conversion rate, shipping costs, and traffic quality.

### 66. A product has low traffic but high conversion. What does this suggest?

**Answer:** Existing traffic may be highly relevant, while the main opportunity may involve increasing qualified traffic.

### 67. A product has high sales but high return rates. What would you investigate?

**Answer:** Return reasons, product quality, sizing, descriptions, customer expectations, suppliers, and specific customer segments.

### 68. A campaign has high CTR but low conversion. Why?

**Answer:** The campaign may attract clicks without attracting qualified users, or there may be a mismatch between the advertisement and landing page/product.

### 69. A campaign has low CTR but high conversion. What would you investigate?

**Answer:** The audience may be small but highly qualified. Investigate reach, creative, targeting, and whether increasing qualified traffic could scale results.

### 70. Revenue is growing but customer retention is falling. What would you investigate?

**Answer:** Determine whether growth comes from new customers, whether acquisition is becoming more important, and investigate changes in product, service, pricing, or customer experience.

### 71. Customers are buying more but profit is falling. Why?

**Answer:** Discounts, increased costs, lower-margin products, shipping expenses, returns, or changes in customer/product mix.

### 72. Marketing spend increased but revenue did not. What would you investigate?

**Answer:** Channel performance, CAC, conversion rate, traffic quality, attribution, campaign targeting, and incremental revenue.

### 73. How would you decide which marketing channel deserves more investigation?

**Answer:** Compare channels using consistent definitions for cost, customers, conversion, revenue, margin, retention, and incremental impact.

### 74. Management asks for "the most important KPI." What would you do?

**Answer:** First clarify the business objective. The appropriate KPI depends on whether the objective is growth, profitability, acquisition, retention, efficiency, or another goal.

### 75. What would you do if your analysis contradicts management's expectation?

**Answer:**

```text
1. Recheck the data
2. Validate calculations
3. Check definitions
4. Test alternative explanations
5. Present the evidence clearly
6. Explain uncertainty
7. Discuss implications
```

The goal is to provide reliable evidence rather than force the analysis to match an expectation.

---

# 🔥 E-Commerce Analysis Framework

For most E-commerce problems:

```text
BUSINESS QUESTION
       ↓
      KPI
       ↓
    BASELINE
       ↓
   DATA QUALITY
       ↓
  SEGMENTATION
       ↓
     EDA
       ↓
  DRIVER ANALYSIS
       ↓
 CAUSE / HYPOTHESIS
       ↓
 BUSINESS IMPACT
       ↓
     ACTION
       ↓
   MEASUREMENT
```

# 📊 Core E-Commerce Metrics

| Category      | Metrics                                    |
| ------------- | ------------------------------------------ |
| Revenue       | Revenue, GMV, Growth                       |
| Sales         | Orders, Units Sold, AOV                    |
| Customers     | New Customers, Returning Customers         |
| Retention     | Retention Rate, Churn, Repeat Purchase     |
| Marketing     | CAC, CTR, CPC, ROAS                        |
| Conversion    | Conversion Rate, Cart Rate                 |
| Funnel        | View → Cart → Checkout → Purchase          |
| Product       | Revenue, Margin, Returns, Reviews          |
| Operations    | Delivery Time, Cancellation Rate           |
| Profitability | Gross Profit, Margin, Contribution         |
| Loyalty       | CLV, Purchase Frequency                    |
| Inventory     | Turnover, Stockouts, Slow-Moving Inventory |

# 🧩 Key Decompositions

### Revenue

```text
Revenue
= Customers × Orders per Customer × AOV
```

### AOV

```text
AOV
= Revenue / Orders
```

### Conversion

```text
Conversion Rate
= Purchases / Eligible Visitors
```

### CAC

```text
CAC
= Acquisition Cost / New Customers
```

### ROAS

```text
ROAS
= Attributed Revenue / Ad Spend
```

### Profit

```text
Profit
= Revenue - Costs
```

# 🎯 The Analyst Mindset

Don't stop at:

> **"What happened?"**

Continue with:

```text
What happened?
       ↓
Where did it happen?
       ↓
When did it happen?
       ↓
Who/what drove it?
       ↓
Why might it have happened?
       ↓
How large is the impact?
       ↓
What should be measured next?
```

> **Good E-commerce analysis connects customer behavior, marketing activity, sales performance, and business outcomes.**

---