# 09 — Advanced Business Analysis Techniques

## 1. Introduction

Advanced Business Analysis Techniques enable senior business analysts to investigate complex business problems, evaluate competing alternatives, manage uncertainty, and support evidence-based decisions.

This module covers analytical frameworks, quantitative methods, process investigation, root-cause analysis, decision modeling, forecasting, and advanced stakeholder techniques relevant to CBAP preparation.

## 2. Root-Cause Analysis

Root-cause analysis identifies the underlying reasons for a problem rather than treating its visible symptoms.

### 2.1 Five Whys

The Five Whys technique repeatedly asks why a problem occurred.

Example:

* Problem: Customer orders are delivered late.
* Why? Orders are released to the warehouse late.
* Why? Payment confirmation is delayed.
* Why? The payment integration frequently times out.
* Why? The integration has insufficient capacity during peak periods.
* Why? Capacity planning did not account for seasonal transaction volumes.

The investigation suggests that capacity planning and integration performance require attention.

The technique does not require exactly five questions. Continue until a sufficiently supported underlying cause is identified.

### 2.2 Fishbone Diagram

A fishbone diagram organizes potential causes into categories.

Typical categories include:

* People.
* Processes.
* Technology.
* Data.
* Policies.
* Environment.

The analyst should validate proposed causes with evidence rather than assume that every listed factor contributes to the problem.

### 2.3 Pareto Analysis

Pareto analysis identifies the categories responsible for a large proportion of observed problems.

Suppose a company records 200 customer complaints:

| Complaint Category | Count |
| ------------------ | ----: |
| Delivery delays    |    90 |
| Damaged products   |    50 |
| Billing errors     |    30 |
| Website issues     |    20 |
| Other              |    10 |

Delivery delays and damaged products account for 140 of 200 complaints, or 70%.

Addressing these categories first may produce substantial improvement. However, low-frequency issues involving safety, compliance, or severe financial exposure may still require immediate attention.

## 3. Business Process Analysis

Business process analysis examines how activities, decisions, information, and resources combine to produce business outcomes.

### 3.1 Current-State Analysis

Investigate:

* Process inputs and outputs.
* Activity sequence.
* Decision points.
* Roles and responsibilities.
* Handoffs.
* Bottlenecks.
* Rework.
* Waiting time.
* Control points.
* Performance indicators.

### 3.2 Process Mapping

A process map represents the activities and decisions involved in a workflow.

Example:

Receive order → Validate information → Check payment → Confirm order → Fulfill order → Notify customer.

Exception paths should be included for invalid orders, payment failures, and unavailable inventory.

### 3.3 Value-Added Analysis

Classify activities as:

* Value-adding.
* Business-required but not directly value-adding.
* Non-value-adding or avoidable.

This classification helps identify unnecessary approvals, duplicated data entry, excessive waiting, and avoidable rework.

An activity should not be eliminated solely because it does not directly create customer value. Regulatory controls and essential risk-management activities may remain necessary.

## 4. Decision Analysis

Decision analysis provides a structured method for comparing alternatives.

### 4.1 Decision Criteria

Possible criteria include:

* Financial value.
* Strategic alignment.
* Implementation time.
* Technical feasibility.
* Operational impact.
* Risk.
* Regulatory compliance.
* Stakeholder acceptance.

Mandatory constraints should be separated from criteria that permit trade-offs.

### 4.2 Weighted Decision Matrix

Suppose three software alternatives are scored on a five-point scale.

| Criterion       | Weight |  A |  B |  C |
| --------------- | -----: | -: | -: | -: |
| Business fit    |    35% |  5 |  4 |  3 |
| Cost            |    25% |  3 |  4 |  5 |
| Delivery speed  |    20% |  3 |  5 |  4 |
| Maintainability |    20% |  4 |  4 |  3 |

Scores:

* A: 3.90
* B: 4.20
* C: 3.80

Alternative B ranks highest under the selected weights. The result should be tested for sensitivity to changes in assumptions and scoring.

### 4.3 Decision Trees

Decision trees represent choices, uncertain events, and possible outcomes.

They are useful when a decision depends on future conditions, such as market adoption or pilot results.

Expected monetary value can be calculated as:

$$
EMV=\sum_{i=1}^{n}P_iV_i
$$

Where \(P_i\) is the probability of an outcome and \(V_i\) is its monetary value.

For example, a project has:

* 60% probability of generating a benefit of 200,000.
* 40% probability of generating a benefit of 50,000.

Expected benefit:

\(0.60(200,000)+0.40(50,000)=140,000\).

If the project costs 100,000, the expected net monetary value is 40,000, assuming the probabilities and benefits are valid and all relevant costs are included.

Expected value alone does not capture risk tolerance, liquidity constraints, or the consequences of severe adverse outcomes.

## 5. Quantitative Analysis

Quantitative techniques help analysts evaluate measurable business conditions.

### 5.1 Descriptive Statistics

Common measures include:

* Mean.
* Median.
* Mode.
* Range.
* Variance.
* Standard deviation.
* Percentiles.

The mean can be affected by extreme values, while the median often better represents a typical observation in a skewed distribution.

### 5.2 Trend Analysis

Trend analysis examines how a metric changes over time.

Applications include:

* Sales performance.
* Customer churn.
* Production defects.
* Service demand.
* Operational costs.
* Employee turnover.

Analysts should distinguish long-term trends from seasonality, random variation, and one-time events.

### 5.3 Forecasting

Forecasting estimates future values using historical data, causal factors, expert judgment, or combinations of methods.

Methods include:

* Moving averages.
* Exponential smoothing.
* Regression.
* Time-series models.
* Scenario-based forecasting.

Forecasts should include assumptions and uncertainty rather than presenting estimates as guaranteed outcomes.

### 5.4 Correlation and Causation

Correlation describes an association between variables. It does not, by itself, prove that one variable causes another.

For example, increased advertising expenditure and increased sales may occur together, but other factors such as seasonality or market growth may explain part of the relationship.

Causal conclusions require stronger evidence and appropriate analytical designs.

## 6. Sensitivity and Scenario Analysis

Sensitivity analysis examines how changes in individual assumptions affect an outcome.

Scenario analysis examines combinations of assumptions representing plausible futures.

Example scenarios for a software investment:

* Optimistic: High adoption, low implementation cost.
* Expected: Moderate adoption and costs near the estimate.
* Pessimistic: Delayed implementation, lower adoption, and higher operating costs.

The analyst can identify which assumptions have the greatest influence on project value and prioritize their validation.

## 7. Requirements and Information Analysis

Advanced analysis frequently involves large volumes of stakeholder information.

### 7.1 Classification

Group information by:

* Business objective.
* Stakeholder.
* Process.
* Capability.
* Risk.
* Priority.
* Requirement type.
* Solution component.

### 7.2 Gap and Completeness Analysis

Check whether all relevant business objectives, stakeholders, processes, data entities, and exception conditions are represented.

A requirements checklist can help, but completeness ultimately depends on the business context.

### 7.3 Dependency Analysis

Identify requirements that depend on other requirements, capabilities, systems, or decisions.

Dependency analysis supports:

* Sequencing.
* Release planning.
* Impact assessment.
* Risk reduction.
* Resource allocation.

## 8. Benchmarking

Benchmarking compares performance with a relevant reference.

Types include:

* Internal benchmarking between departments.
* Competitive benchmarking against comparable organizations.
* Functional benchmarking against organizations performing similar activities.
* Industry benchmarking using established sector measures.

A meaningful benchmark requires comparable definitions, operating conditions, and data quality.

## 9. Cost-Benefit and Financial Analysis

### 9.1 Return on Investment

A commonly used simplified formula is:

$$
ROI=\frac{\text{Benefits}-\text{Costs}}{\text{Costs}}\times100\%
$$

If benefits are 150,000 and costs are 100,000:

ROI = 50%.

The time horizon and treatment of recurring costs must be clearly defined.

### 9.2 Net Present Value

Net present value accounts for the time value of money.

$$
NPV=\sum_{t=1}^{n}\frac{CF_t}{(1+r)^t}-I_0
$$

Where:

* \(CF_t\) is the net cash flow in period \(t\).
* \(r\) is the discount rate.
* \(I_0\) is the initial investment.
* \(n\) is the number of periods.

A positive NPV indicates that projected cash flows exceed the initial investment on a discounted basis under the model's assumptions.

### 9.3 Intangible Benefits

Some benefits are difficult to express in monetary terms, including:

* Better customer experience.
* Increased trust.
* Improved employee morale.
* Better decision quality.
* Reduced compliance exposure.

These benefits can be assessed through suitable indicators and documented alongside financial estimates.

## 10. Advanced Case Study: Supply Chain Optimization

### Scenario

A distributor experiences stockouts, excess inventory, and inconsistent supplier performance.

### Analysis

**Root cause:** Investigations identify fragmented demand data, inconsistent replenishment rules, and delayed supplier updates.

**Process analysis:** Mapping reveals duplicate approvals and delayed purchase-order release.

**Quantitative analysis:** Historical data shows seasonal demand variation and a small number of suppliers account for most late deliveries.

**Decision analysis:** Alternatives include improving existing procedures, implementing demand forecasting, and introducing supplier-performance monitoring.

**Sensitivity analysis:** Benefits are tested against different adoption rates, inventory holding costs, and forecast accuracy levels.

**Recommendation:** Standardize data and replenishment policies first, pilot forecasting for selected product categories, and expand after measuring results.

### Key Lesson

Advanced business analysis combines qualitative investigation, quantitative evidence, and structured decision-making to address underlying business problems.

## 11. Knowledge Check

1. What is the purpose of root-cause analysis?
2. How does Pareto analysis support prioritization?
3. What is the difference between process mapping and value-added analysis?
4. How is expected monetary value calculated?
5. Why does correlation not establish causation?
6. How do sensitivity and scenario analysis differ?
7. Why should benchmarking use comparable measures?
8. What does NPV account for that a simple total-benefit calculation may not?
9. Why should mandatory constraints be separated from weighted criteria?
10. How does dependency analysis improve planning?

### Answers

1. To identify underlying causes rather than treat symptoms.
2. It identifies categories contributing disproportionately to observed problems.
3. Process mapping represents workflow structure; value-added analysis assesses the contribution or necessity of activities.
4. Multiply each outcome's value by its probability and sum the results.
5. Other variables or coincidence may explain the observed association.
6. Sensitivity analysis varies selected assumptions; scenario analysis evaluates combinations of assumptions.
7. Incomparable definitions or conditions can produce misleading conclusions.
8. It accounts for the time value of money through discounting.
9. A high score cannot legitimately compensate for failure to satisfy a mandatory requirement.
10. It identifies prerequisite relationships and helps sequence work.

## 12. Practical Exercises

1. Use the Five Whys and a fishbone diagram to investigate a business problem.
2. Build a Pareto chart from a set of defect or complaint counts.
3. Compare three strategic alternatives using a weighted decision matrix.
4. Forecast monthly demand using a moving average and evaluate forecast errors.
5. Build optimistic, expected, and pessimistic scenarios for a proposed investment.
6. Calculate ROI and NPV using explicitly stated assumptions.
7. Map a business process and identify unnecessary handoffs and control requirements.

## 13. Recommended References

* IIBA, *A Guide to the Business Analysis Body of Knowledge (BABOK® Guide)*, Version 3.
* IIBA official CBAP certification resources.
* ISO 31000, Risk Management — Guidelines.
* *Business Analysis Techniques: 99 Essential Tools for Success*, by James Cadle, Debra Paul, and Paul Turner.

## 14. Module Summary

Advanced Business Analysis Techniques combine root-cause analysis, process modeling, decision analysis, quantitative methods, forecasting, benchmarking, and financial evaluation. Effective analysts select methods appropriate to the business question, validate their assumptions, interpret evidence critically, and communicate recommendations in terms of risk, feasibility, and business value.
