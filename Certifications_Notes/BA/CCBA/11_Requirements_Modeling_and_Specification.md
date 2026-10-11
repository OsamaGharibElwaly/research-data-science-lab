# 11 — Business Intelligence and Analytics

## 1. Introduction

The Business Intelligence perspective focuses on collecting, integrating, analyzing, and presenting data to support business decisions.

Business analysts working in this perspective help stakeholders define the questions that need to be answered, establish meaningful measures, understand data requirements, assess data quality, and translate analytical findings into business actions.

Business intelligence is not simply dashboard development. Its value depends on whether the information is trustworthy, relevant, and useful for decision-making.

## 2. Data, Information, and Knowledge

### Data

Raw observations, records, measurements, or events.

Examples:

* Individual sales transactions.
* Product quantities.
* Customer support timestamps.
* Inventory movements.

### Information

Data organized and interpreted within a meaningful context.

Example: Monthly sales revenue by product category.

### Knowledge

Understanding developed through analysis, experience, and interpretation.

Example: Sales of a particular product category decline when delivery times exceed a certain threshold.

### Business action

A decision or intervention based on the available evidence.

Example: Improve delivery capacity for the affected category and monitor the resulting sales performance.

Data does not automatically create knowledge. Interpretation, validation, and business context are essential.

## 3. Business Intelligence Lifecycle

A typical BI lifecycle includes:

1. Identify business questions.
2. Define decision requirements.
3. Identify data sources.
4. Assess data availability and quality.
5. Define metrics and business rules.
6. Integrate and transform data.
7. Model and analyze information.
8. Present results.
9. Validate findings with stakeholders.
10. Monitor outcomes and improve reporting.

The lifecycle may be iterative rather than strictly sequential.

### Example

A retail manager asks: "Why are profits declining?"

The analyst should clarify whether the question concerns:

* Revenue.
* Gross margin.
* Operating expenses.
* Product mix.
* Discounts.
* Returns.
* Inventory losses.

A dashboard cannot answer a poorly defined question reliably unless the relevant measures and business definitions are established first.

## 4. Business Questions and Analytical Requirements

Analytical requirements describe the information needed to support decisions.

Examples:

* Sales managers need revenue by region and product.
* Operations managers need late deliveries by warehouse.
* Finance needs gross margin by customer segment.
* Executives need monthly performance against targets.

A strong analytical requirement specifies:

* The decision or question.
* The intended audience.
* Required dimensions.
* Required measures.
* Time period.
* Level of detail.
* Filters and drill-downs.
* Refresh frequency.
* Data access restrictions.
* Performance expectations.

### Weak requirement

"Create a sales dashboard."

### Improved requirement

"Sales managers shall be able to compare monthly revenue and gross margin by region and product category for the previous 24 months, with filters for sales channel and customer segment."

The improved requirement describes a specific analytical capability.

## 5. Metrics and KPIs

A metric is a defined measure of a business attribute or activity.

A KPI is a metric selected to assess progress toward an important objective.

### Common business metrics

**Revenue:** Income generated from business activities under the applicable accounting definition.

**Gross profit:** Revenue minus cost of goods sold.

**Gross margin percentage:**

$$
Gross\ Margin\% =
\frac{Revenue-COGS}{Revenue}\times100
$$

**Conversion rate:**

$$
Conversion\ Rate =
\frac{Completed\ Conversions}{Eligible\ Visitors}\times100
$$

**Customer retention rate:** The proportion of existing customers retained over a defined period, calculated using a consistent methodology.

**Inventory turnover:**

$$
Inventory\ Turnover =
\frac{Cost\ of\ Goods\ Sold}{Average\ Inventory}
$$

The definitions and units must be consistent. For example, inventory turnover typically uses cost-based measures rather than mixing sales revenue with inventory valued at cost.

### Leading and lagging indicators

**Leading indicators** provide signals that may help anticipate future performance.

Example: Percentage of sales opportunities receiving a follow-up within 24 hours.

**Lagging indicators** reflect outcomes that have already occurred.

Example: Quarterly revenue.

A balanced set of measures can combine early warning signals with actual outcomes.

## 6. Data Sources and Integration

Business data may come from:

* ERP systems.
* CRM platforms.
* Financial applications.
* Web analytics.
* Operational databases.
* Spreadsheets.
* External APIs.
* Customer surveys.
* Transaction logs.
* Data warehouses and data lakes.

### Integration challenges

* Different identifiers.
* Inconsistent formats.
* Duplicate records.
* Missing values.
* Different update frequencies.
* Conflicting business definitions.
* Time-zone differences.
* Inconsistent historical periods.
* Access restrictions.

### Example

A customer appears as `C-102` in a CRM and `102` in an order system.

The analyst must determine whether these records refer to the same customer and how the identifiers should be reconciled.

Incorrect joins can inflate sales totals, duplicate customers, or produce misleading conclusions.

## 7. Data Quality

Data quality refers to how well data supports its intended use.

Important dimensions include:

**Accuracy:** Data correctly represents the underlying reality.

**Completeness:** Required data is present.

**Consistency:** Data agrees across relevant sources and definitions.

**Validity:** Data conforms to defined rules and formats.

**Uniqueness:** Unwanted duplicates are controlled.

**Timeliness:** Data is available when needed.

### Example

A delivery dashboard reports that 98% of shipments are on time.

However, the timestamp for dispatch is used instead of the timestamp for customer delivery.

The calculation may be internally consistent but does not measure the intended business outcome.

The analyst should clarify the metric definition and correct the data logic.

## 8. Data Governance

Data governance establishes policies, responsibilities, standards, and controls for managing data.

It may define:

* Data ownership.
* Data stewardship.
* Business definitions.
* Access rights.
* Data quality standards.
* Privacy requirements.
* Retention rules.
* Audit procedures.
* Metadata standards.
* Change management.

### Data owner vs. data steward

A data owner typically has accountability for a data domain and its appropriate use.

A data steward commonly supports day-to-day data quality, definitions, documentation, and governance practices.

The exact roles vary by organization.

Business analysts should identify who can clarify data definitions and who has authority to approve relevant decisions.

## 9. Descriptive, Diagnostic, Predictive, and Prescriptive Analytics

### Descriptive analytics

Answers: What happened?

Examples:

* Monthly revenue.
* Number of late deliveries.
* Average customer support time.

### Diagnostic analytics

Answers: Why might it have happened?

Examples:

* Investigating which products contributed to declining margins.
* Examining causes of increased customer complaints.

### Predictive analytics

Answers: What is likely to happen?

Examples:

* Forecasting demand.
* Predicting late deliveries.
* Estimating customer churn risk.

Predictions are uncertain and depend on the quality of the data and assumptions.

### Prescriptive analytics

Answers: What action may be most appropriate?

Examples:

* Recommending replenishment quantities.
* Suggesting delivery routes.
* Comparing staffing plans.

Prescriptive recommendations should consider constraints, costs, risks, and business objectives.

## 10. Dashboards and Data Visualization

A dashboard presents selected information in a form that supports monitoring and decisions.

### Design principles

* Match visualizations to the question.
* Use clear labels and units.
* Show relevant targets and baselines.
* Avoid unnecessary decoration.
* Provide appropriate detail.
* Make filters understandable.
* Explain important definitions.
* Distinguish missing data from zero.
* Avoid misleading axes or scales.
* Consider accessibility and readability.

### Choosing visualizations

| Purpose                        | Common Visualization                                |
| ------------------------------ | --------------------------------------------------- |
| Compare categories             | Bar chart                                           |
| Examine trends over time       | Line chart                                          |
| Show part-to-whole composition | Stacked bar or carefully selected composition chart |
| Examine distributions          | Histogram or box plot                               |
| Explore relationships          | Scatter plot                                        |
| Monitor key values             | KPI card or compact table                           |

The visualization should make the relevant comparison easy to understand.

## 11. Data Warehouses, Data Lakes, and ETL

### Data warehouse

A structured environment designed to support reporting and analytical queries, often integrating data from multiple sources.

### Data lake

A repository that can store large volumes of data in different formats, including structured and unstructured data.

### ETL

Extract, Transform, Load:

1. Extract data from sources.
2. Transform it into the required structure or quality.
3. Load it into the target environment.

### ELT

Extract, Load, Transform:

1. Extract data.
2. Load it into the target platform.
3. Transform it within that environment.

Business analysts need not implement every pipeline, but they should understand how data flows affect accuracy, timeliness, and reporting.

## 12. Statistical Interpretation and Analytical Limitations

BI findings must be interpreted carefully.

### Correlation vs. causation

Two variables may move together without one causing the other.

Example: Ice cream sales and swimming incidents may both increase during hot weather. This does not establish that ice cream causes swimming incidents.

A third variable, such as temperature, may influence both.

### Selection bias

A sample may not represent the population being studied.

Example: A customer satisfaction survey sent only to highly active app users may overlook dissatisfied customers who stopped using the app.

### Simpson's paradox

A trend observed within individual groups can reverse when the groups are combined, often because group sizes or distributions differ.

This illustrates why segmentation and context matter when interpreting aggregated metrics.

### Forecast uncertainty

Forecasts should be evaluated using suitable error measures and historical validation. A single predicted value should not be presented as a guaranteed outcome.

## 13. Practical Case Study: Sales Performance Dashboard

A retailer reports increasing revenue but declining profitability.

### Business question

Which products, channels, and regions explain the margin decline?

### Requirements

* Monthly revenue.
* Cost of goods sold.
* Gross margin percentage.
* Discount rates.
* Returns.
* Region and product filters.
* Historical comparison.

### Data investigation

The analyst discovers:

* One source records returns as negative sales.
* Another records returns in a separate table.
* Product costs are updated at different intervals.
* Promotional discounts are inconsistently categorized.

### Recommended analysis

1. Establish common metric definitions.
2. Reconcile return treatment.
3. Validate product costs.
4. Compare margin by category and channel.
5. Separate volume growth from margin changes.
6. Confirm findings with finance.
7. Recommend targeted business actions.
8. Monitor results after the changes.

### Key lesson

A polished dashboard cannot compensate for inconsistent data definitions. Reliable analysis begins with the business question, metric definitions, and data quality.

## 14. Knowledge Check

**Question 1:** Which type of analytics answers "What happened?"

A. Prescriptive
B. Descriptive
C. Predictive
D. Diagnostic

**Question 2:** Which data quality dimension concerns unwanted duplicate records?

A. Timeliness
B. Uniqueness
C. Availability
D. Visualization

**Question 3:** A company finds that advertising spend and sales increase together. What can it conclude immediately?

A. Advertising definitely caused all additional sales.
B. The variables are associated, but causation requires further investigation.
C. The data must be incorrect.
D. No further analysis is possible.

**Question 4:** Which measure is most suitable for monitoring gross profitability as a proportion of revenue?

A. Gross margin percentage
B. Number of dashboard views
C. Total customer count only
D. Average login duration

**Question 5:** What is the primary purpose of data governance?

A. To create charts automatically
B. To establish responsibilities, standards, and controls for data
C. To eliminate all data storage costs
D. To replace business requirements

**Question 6:** A dashboard reports delivery performance using dispatch time instead of delivery time. What is the principal problem?

A. The metric does not accurately represent the intended business outcome.
B. The chart should always be a pie chart.
C. The data must be predictive.
D. The dashboard needs more colors.

### Answers and Explanations

1. **B.** Descriptive analytics summarizes what occurred.
2. **B.** Uniqueness addresses unwanted duplicates.
3. **B.** Association alone does not establish causation.
4. **A.** Gross margin percentage measures gross profit relative to revenue.
5. **B.** Governance establishes accountability and standards for data management.
6. **A.** The calculation does not measure the intended outcome.

## 14. Revision Summary

* BI supports decisions by turning data into meaningful information.
* Analytical requirements should define business questions, measures, dimensions, and refresh needs.
* KPIs should connect to business objectives.
* Data quality and governance are essential for reliable reporting.
* Descriptive, diagnostic, predictive, and prescriptive analytics answer different questions.
* Visualizations should match the analytical purpose.
* Correlation does not prove causation.
* Findings should be validated with business stakeholders.

## 15. Further Study

Review the BABOK Guide's Business Intelligence perspective and study foundational topics in data modeling, KPI design, data quality, dimensional analysis, and dashboard design. Practice translating business questions into measurable analytical requirements.
