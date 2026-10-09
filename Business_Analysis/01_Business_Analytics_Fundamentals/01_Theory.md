# Business Analytics Fundamentals — Theory

## 1. From Data to Decisions

Business analytics is the systematic use of data, quantitative methods, business knowledge, and reasoning to understand performance and improve decisions.

A useful workflow is:

**Business context → Decision → Question → Evidence → Interpretation → Recommendation → Action → Monitoring**

Key terminology:

* **Data:** Recorded observations, such as order dates, prices, and delivery status.
* **Information:** Data organized into a meaningful structure, such as monthly revenue by region.
* **Evidence:** Information used to support or challenge a claim, considering its reliability and limitations.
* **Insight:** An interpretation that matters to a business decision.
* **Decision:** A choice among alternatives.
* **Action:** The operational step taken after a decision.

A large dataset does not automatically produce reliable evidence. Poor definitions, biased samples, duplicate records, and inaccurate measurements can undermine even sophisticated analyses.

## 2. Related Disciplines

| Discipline            | Main emphasis                                         | Example                           |
| --------------------- | ----------------------------------------------------- | --------------------------------- |
| Reporting             | Presenting agreed measures                            | Weekly sales report               |
| Business intelligence | Governed data, dashboards, and performance monitoring | KPI dashboard                     |
| Data analysis         | Examining and interpreting data                       | Investigating a sales decline     |
| Business analytics    | Applying evidence to business decisions               | Recommending a retention strategy |
| Data science          | Statistical learning and computational methods        | Churn prediction                  |
| Operations research   | Mathematical optimization under constraints           | Delivery-route optimization       |

These disciplines overlap. The distinctions are useful for framing a project, not for creating rigid boundaries.

## 3. Four Types of Business Analytics

### 3.1 Descriptive Analytics — What Happened?

Descriptive analytics summarizes past or current performance.

Examples:

* Total revenue last month.
* Number of complaints by region.
* Average delivery time.
* Conversion rate by marketing channel.

A statement such as “sales increased by 12%” is incomplete unless the comparison period, population, and sales definition are clear.

### 3.2 Diagnostic Analytics — Why Might It Have Happened?

Diagnostic analytics investigates patterns and plausible explanations.

Common techniques include:

* Segmentation and drill-downs.
* Comparing periods or business units.
* Examining process stages.
* Checking relationships between variables.
* Reviewing operational context.

A sales decline after a price increase does not prove that the price increase caused the decline. Seasonality, stockouts, competitor actions, or changes in marketing may also explain the pattern.

### 3.3 Predictive Analytics — What May Happen?

Predictive analytics estimates future or unknown outcomes.

Examples:

* Forecasting demand.
* Estimating the risk of late delivery.
* Predicting customer churn.
* Estimating the probability of a payment default.

Predictions are uncertain. Their usefulness depends on data quality, target definition, evaluation design, model stability, and the consequences of incorrect predictions.

### 3.4 Prescriptive Analytics — What Should We Do?

Prescriptive analytics evaluates possible actions and their consequences.

Examples:

* Allocating limited delivery capacity.
* Selecting inventory reorder quantities.
* Choosing which retention offers to test.
* Balancing cost against service levels.

A useful recommendation must consider feasibility, cost, risk, and fairness—not just a model's output.

## 4. Business Problem Framing

A good analytics project starts with a decision rather than a tool.

Define:

1. **Stakeholder:** Who needs the answer?
2. **Decision:** What choice will the analysis support?
3. **Outcome:** What does success mean?
4. **Population:** Which customers, orders, stores, or periods are included?
5. **Time horizon:** What period matters?
6. **Constraints:** What limits exist on budget, staff, time, or data?
7. **Baseline:** What is the current performance?
8. **Target:** What outcome would be valuable?
9. **Risks:** What could make the conclusion misleading or harmful?

**Weak problem statement:** “Analyze our customers.”

**Stronger problem statement:** “For online customers who placed an order in the previous quarter, identify characteristics associated with repeat purchasing and determine which retention strategy is worth testing within the available budget.”

The stronger version specifies a population, outcome, period, and decision.

### Hypotheses and alternative explanations

A hypothesis is a proposition that can be examined using evidence.

Example:

* Hypothesis: Late deliveries are associated with lower customer satisfaction.
* Alternative explanations: Region, order complexity, product type, and seasonal demand may affect both delivery time and satisfaction.
* Evidence needed: Consistent definitions, sufficient observations, relevant comparisons, and possibly a suitable experimental or observational design.

Exploratory findings should often be treated as hypotheses to investigate further rather than established facts.

## 5. Data Fundamentals

### Rows, columns, and observations

A dataset typically contains:

* **Rows:** observations or records.
* **Columns:** variables or attributes.
* **Identifiers:** fields used to identify entities.
* **Unit of analysis:** the entity represented by one row.

Examples of units of analysis include orders, customers, transactions, stores, and store-days.

Before calculating a metric, ask:

* What does one row represent?
* Is the identifier unique at this level?
* Are there repeated observations?
* Can a join duplicate records?
* Are the dates and time periods consistent?

A join that duplicates orders can inflate revenue. Customer-level averages and order-level averages answer different questions.

### Variable types

| Type                 | Example                  | Appropriate treatment         |
| -------------------- | ------------------------ | ----------------------------- |
| Nominal categorical  | Region, product category | Group or count                |
| Ordinal categorical  | Low, medium, high        | Preserve ordering             |
| Discrete numerical   | Items per order          | Count or summarize            |
| Continuous numerical | Revenue, elapsed time    | Measure or summarize          |
| Date/time            | Order date               | Analyze chronologically       |
| Identifier           | Order ID                 | Identify records, not average |

A numeric code does not necessarily represent a numerical quantity. Averaging regional codes is usually meaningless.

## 6. Measures, Metrics, Dimensions, and KPIs

* **Measure:** A value that can be aggregated, such as revenue.
* **Metric:** A defined quantitative measure used to answer a question.
* **Dimension:** A field used to group or filter results, such as region or month.
* **KPI:** A key performance indicator linked to an important business objective.
* **Target:** The desired value or range.
* **Threshold:** A boundary that triggers attention or action.
* **Guardrail metric:** A measure that helps ensure improvement in one area does not cause unacceptable harm elsewhere.

A KPI should have a documented formula, owner, source, population, reporting frequency, target, and decision rule.

### Metric dictionary template

| Field              | Example                                                     |
| ------------------ | ----------------------------------------------------------- |
| Name               | On-time delivery rate                                       |
| Formula            | Eligible on-time deliveries ÷ eligible completed deliveries |
| Unit               | Percentage                                                  |
| Population         | Eligible completed deliveries                               |
| Period             | Calendar week                                               |
| Exclusions         | Documented customer-requested delays                        |
| Source             | Order and delivery systems                                  |
| Owner              | Operations manager                                          |
| Caveat             | Missing timestamps may affect the result                    |
| Decision supported | Identify process issues requiring investigation             |

## 7. Core Business Formulas

Definitions must be consistent. Document what is included in every numerator and denominator.

### Percentage change

$$
\text{Percentage Change} =
\frac{\text{New Value}-\text{Old Value}}
{\text{Old Value}}\times100\%
$$

If the old value is zero, this formula is undefined. Report the absolute change or explain an alternative comparison.

### Average order value

$$
\text{AOV} =
\frac{\text{Net Order Revenue}}
{\text{Number of Eligible Orders}}
$$

Clarify whether revenue includes taxes, shipping, discounts, cancellations, and refunds.

### Conversion rate

$$
\text{Conversion Rate} =
\frac{\text{Conversions}}
{\text{Eligible Opportunities}}\times100\%
$$

The denominator must match the question. Sessions, visitors, leads, and qualified leads are not interchangeable.

### Gross profit

$$
\text{Gross Profit}=\text{Revenue}-\text{Cost of Goods Sold}
$$

### Gross margin percentage

$$
\text{Gross Margin \%} =
\frac{\text{Revenue}-\text{Cost of Goods Sold}}
{\text{Revenue}}\times100\%
$$

Margin is not the same as markup.

### On-time delivery rate

$$
\text{On-Time Rate} =
\frac{\text{Eligible Deliveries On or Before Promise Date}}
{\text{Eligible Completed Deliveries}}\times100\%
$$

Specify how partial deliveries, missing timestamps, and customer-requested delays are handled.

### Weighted and unweighted averages

Suppose Store A has 10 orders with an average basket value of 100, while Store B has 90 orders with an average of 50.

The overall order-level average is:

$$
\frac{10(100)+90(50)}{10+90}=55
$$

The unweighted average of store averages is:

$$
\frac{100+50}{2}=75
$$

The two calculations answer different questions. Choose the weighting that matches the business question.

## 8. The Analytics Lifecycle

A reliable workflow is iterative.

1. **Frame:** Define the decision, scope, success criteria, and constraints.
2. **Acquire:** Identify data sources, access rights, and data owners.
3. **Validate:** Check schema, missing values, duplicates, and plausible ranges.
4. **Prepare:** Clean and transform data using documented rules.
5. **Explore:** Inspect distributions, trends, segments, and anomalies.
6. **Analyze:** Apply methods appropriate to the question and available evidence.
7. **Validate findings:** Check assumptions, baselines, and robustness.
8. **Communicate:** Separate results, interpretations, recommendations, and caveats.
9. **Act:** Assign an owner and implementation plan.
10. **Monitor:** Evaluate outcomes and identify changing conditions.

Not every problem needs an advanced model. A well-defined metric and a carefully designed operational comparison may be more useful than a complex algorithm.

## 9. Data Quality and Reproducibility

Important data-quality dimensions include:

* **Completeness:** Required values are present.
* **Validity:** Values follow defined formats and rules.
* **Consistency:** Values agree across systems and periods.
* **Uniqueness:** Records are not duplicated beyond the intended data grain.
* **Timeliness:** Data are available when decisions must be made.
* **Accuracy:** Recorded values reflect the real-world quantity or event.

Cleaning should not silently remove inconvenient observations. Document the rule, quantify the affected records, and assess whether exclusions change the conclusion.

Reproducible work documents:

* Source and extraction date.
* Data definitions and date ranges.
* Transformation rules.
* Assumptions and exclusions.
* Code and relevant package versions.
* Validation checks and results.

Never commit credentials or confidential business data to a public repository.

## 10. Bias, Causality, and Responsible Analytics

### Correlation is not causation

Two variables may move together because:

* One influences the other.
* A third variable affects both.
* The sample was selected in a biased way.
* The relationship occurred by chance.

A causal claim generally requires a stronger design and assumptions than a simple correlation.

### Common risks

* **Selection bias:** Observed cases differ systematically from the target population.
* **Survivorship bias:** Only entities that remain observable are analyzed.
* **Confounding:** Another factor affects both the proposed cause and outcome.
* **Measurement bias:** A recorded variable does not consistently measure the intended concept.
* **Data leakage:** Information unavailable at decision time enters a predictive analysis.
* **Aggregation bias:** Overall results hide important differences between groups.
* **Multiple comparisons:** Testing many patterns increases the chance of false discoveries.

### Responsible-use checklist

* Collect only data needed for a legitimate purpose.
* Follow applicable laws, agreements, and company policies.
* Restrict access to sensitive information.
* Remove or mask direct identifiers when appropriate.
* Evaluate whether errors disproportionately harm particular groups.
* Explain material limitations to decision-makers.
* Provide human review for consequential decisions.

## 11. Statistical Significance and Business Significance

A statistically detectable difference is not automatically valuable to a business.

A small effect can be statistically significant in a very large sample but have negligible financial impact. A potentially valuable effect can remain uncertain when the sample is small.

Evaluate:

* Effect size and uncertainty.
* Implementation and ongoing costs.
* Operational feasibility.
* Downside risk and reversibility.
* Impact across customer and employee groups.
* Whether findings generalize to the deployment setting.

Use pilots or controlled experiments when appropriate and ethical. Do not promise business benefits based only on an observational association or a model-performance score.

## 12. Communicating Business Insights

A useful executive summary answers seven questions:

1. What decision needs to be made?
2. What did the evidence show?
3. Why does the finding matter?
4. What action is recommended?
5. How will success be measured?
6. What remains uncertain?
7. Who should act next, and when?

**Weak statement:** “Late delivery causes unhappy customers.”

**Better statement:** “In the observed sample, orders delivered late had lower average satisfaction. This association does not establish that delivery delay alone caused the difference.”

## 13. Common Mistakes and Best Practices

| Common mistake                              | Professional practice                            |
| ------------------------------------------- | ------------------------------------------------ |
| Starting with a tool rather than a decision | Define the decision and success criteria first   |
| Using a metric without a denominator        | Document the complete metric definition          |
| Treating every row as independent           | Confirm the unit of analysis                     |
| Ignoring missing values                     | Profile missingness and document handling        |
| Treating correlation as causation           | Consider confounding and study design            |
| Reporting percentages without counts        | Include counts and the comparison period         |
| Overloading dashboards                      | Focus on metrics linked to decisions             |
| Hiding uncertainty                          | State assumptions and limitations                |
| Optimizing a proxy that can be gamed        | Include outcome and guardrail metrics            |
| Producing irreproducible analysis           | Document data sources, transformations, and code |

## 14. Final Analytical Checklist

Before presenting an analysis, confirm:

* [ ] The business decision and audience are explicit.
* [ ] The population, time period, and unit of analysis are defined.
* [ ] Metrics have clear formulas and denominators.
* [ ] Data-quality checks are documented.
* [ ] The method matches the question.
* [ ] Alternative explanations and limitations are discussed.
* [ ] Business value and implementation cost are considered.
* [ ] Recommendations include an owner, success metric, and review date.
* [ ] Sensitive data are handled appropriately.
* [ ] Another analyst could reproduce the work.
