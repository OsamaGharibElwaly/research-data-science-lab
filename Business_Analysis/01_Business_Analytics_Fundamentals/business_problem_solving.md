# Business Problem Solving Through Analytics

## 1. Introduction

Business problem-solving is the process of defining a business challenge, investigating its causes, evaluating potential solutions, and selecting actions that improve measurable outcomes.

Business Analytics strengthens this process by replacing unsupported assumptions with structured questions, reliable evidence, and transparent reasoning.

A business problem is not always the same as its visible symptom. A decline in sales is an observed outcome; the underlying explanation might involve customer demand, product availability, pricing, competition, or several interacting factors.

The objective is to solve the right problem rather than simply analyze the most visible metric.

## 2. The Business Problem-Solving Framework

This module uses an eight-stage framework.

### Stage 1: Understand the Business Context

Before analyzing data, determine:

* What does the organization want to achieve?
* Who owns the business decision?
* Who is affected by the problem?
* What constraints must be respected?
* What does success look like?
* When must a decision be made?

**Example:** An online retailer wants to improve profitability without significantly reducing customer retention.

This objective is more useful than simply stating that the company wants to increase sales because it identifies a broader business outcome and a constraint.

### Stage 2: Define the Problem

A strong problem statement identifies the observed gap between current and desired performance.

A useful structure is:

> Between [baseline period] and [comparison period], [measurable outcome] changed from [baseline value] to [current value], compared with [target or expectation]. The analysis will investigate [scope] to support [business decision].

Example:

"During the last quarter, the gross profit margin fell below the company's 30% target. The analysis will examine product categories, discounting, and unit costs to support decisions about pricing and product mix."

The example is illustrative rather than a statement about an actual company.

A good problem statement should be:

* Specific
* Measurable
* Relevant to a business objective
* Limited to a manageable scope
* Neutral about the cause until evidence is collected

### Stage 3: Translate the Problem into Analytical Questions

Broad concerns need to be converted into questions that data can help answer.

For a revenue decline, questions might include:

1. How much did revenue change?
2. Which regions and product categories contributed most to the change?
3. Did order volume, average order value, or both change?
4. Did prices, discounts, or product availability change?
5. Are the observed changes unusual compared with historical patterns?
6. Which factors can the organization realistically influence?

Organize these questions into descriptive, diagnostic, predictive, or prescriptive categories where appropriate.

### Stage 4: Identify the Data Requirements

For each analytical question, determine which data is required.

| Analytical Question                        | Required Data                                    | Potential Source         |
| ------------------------------------------ | ------------------------------------------------ | ------------------------ |
| Did revenue decrease?                      | Order dates, quantities, prices, returns         | Transaction database     |
| Which products contributed to the decline? | Product IDs, categories, sales values            | Sales system             |
| Did discounting change?                    | List prices, discount amounts, final prices      | Pricing or order records |
| Were products unavailable?                 | Inventory levels, stockout periods               | Inventory system         |
| Did customer behavior change?              | Customer IDs, order history, acquisition channel | CRM or customer database |

Before using a dataset, inspect its time coverage, missing values, definitions, duplication, and suitability for the intended analysis.

### Stage 5: Investigate Possible Causes

Use evidence to narrow down explanations.

Useful techniques include:

* Segmentation by region, product, customer, or channel
* Comparison with previous periods
* Trend analysis
* Descriptive statistics
* Correlation analysis
* Hypothesis testing
* Process mapping
* Root-cause analysis

#### The Five Whys

The Five Whys technique repeatedly asks why an observed problem occurred to identify potentially deeper causes.

Illustrative example:

1. **Problem:** Orders are frequently delivered late.
2. **Why?** Some orders leave the warehouse later than planned.
3. **Why?** Picking and packing take longer during peak periods.
4. **Why?** Staffing and workload are not aligned with demand.
5. **Why?** Staffing schedules are based on average demand rather than peak patterns.

This suggests investigating workload patterns and staffing schedules.

The chain is a hypothesis, not proof. Each proposed cause should be checked against operational evidence. Some problems have several independent or interacting causes.

### Stage 6: Generate and Evaluate Solutions

Potential solutions should be compared against explicit criteria.

For example, a retailer investigating low profitability might consider:

* Reviewing supplier costs
* Reducing unprofitable discounts
* Improving product assortment
* Revising inventory allocation
* Testing targeted promotions
* Improving demand forecasting

Evaluate each option using:

| Criterion       | Guiding Question                                   |
| --------------- | -------------------------------------------------- |
| Expected impact | How much improvement could the action deliver?     |
| Cost            | What resources and expenses are required?          |
| Feasibility     | Can the organization implement it?                 |
| Risk            | What could go wrong?                               |
| Time            | How quickly could results appear?                  |
| Customer impact | Could the action reduce satisfaction or retention? |
| Measurement     | How will success be evaluated?                     |

Do not assume that the option with the largest potential benefit is automatically the best choice. Cost, uncertainty, implementation risk, and constraints matter.

### Stage 7: Implement and Measure

Translate the selected action into an implementation plan.

A basic action plan identifies:

* The action to be taken
* The responsible owner
* The expected completion date
* Required resources
* Baseline performance
* Target performance
* Measurement frequency
* Conditions that would trigger reassessment

For example, if management tests a new discount policy, it should track profit, sales volume, customer response, and the possibility that purchases merely shift from full-price to discounted products.

Where possible, use a suitable comparison group or controlled experiment to distinguish the intervention's impact from other changes.

### Stage 8: Review and Learn

After implementation:

1. Compare actual results with the baseline and target.
2. Check whether the intended outcome improved.
3. Examine unintended consequences.
4. Document limitations and lessons learned.
5. Decide whether to expand, modify, or stop the intervention.

A completed analysis should lead to learning, not merely a presentation.

## 3. Hypothesis-Driven Analysis

A hypothesis is a testable statement about a possible explanation or relationship.

Example:

"An increase in discounting contributed to the decline in gross profit margin."

To investigate it:

1. Define the margin calculation.
2. Compare discount levels across relevant periods.
3. Examine product-level prices and costs.
4. Compare affected and unaffected product categories.
5. Consider other explanations, including supplier cost changes and product mix.
6. Assess whether the evidence supports the hypothesis.

A hypothesis should be open to rejection. Analysts should not select only the data that supports their initial opinion.

## 4. Distinguishing Correlation from Causation

Suppose advertising spending and revenue increase during the same period.

Possible explanations include:

* Advertising contributed to increased sales.
* Seasonal demand increased both spending and revenue.
* A price change affected revenue independently.
* Another marketing or operational change influenced both variables.

A correlation alone cannot establish which explanation is correct.

Depending on the business question, stronger evidence may come from controlled experiments, randomized A/B tests, natural experiments, longitudinal analysis, or appropriate causal inference methods.

The chosen method should match the question and available data.

## 5. Prioritizing Business Problems

Organizations usually face more problems than they can solve simultaneously.

A simple prioritization model can score each issue from 1 to 5 on:

* Business impact
* Urgency
* Confidence in the available evidence
* Feasibility of addressing the problem

One possible scoring formula is:

**Priority Score = Impact × Urgency × Evidence Confidence × Feasibility**

Each factor uses a scale from 1 to 5, producing a score from 1 to 625.

This is a practical heuristic, not a statistically validated measurement. The scores are subjective, and teams should agree on the definitions before comparing issues.

For high-impact decisions, a financial business case, explicit risk assessment, or optimization model may be more appropriate.

## 6. Decision-Making Under Uncertainty

Business decisions are rarely made with perfect information.

Analysts should distinguish:

* **Known facts:** Directly supported by the available evidence.
* **Assumptions:** Conditions temporarily accepted for analysis.
* **Estimates:** Quantities inferred from incomplete information.
* **Uncertainties:** Factors whose values or outcomes remain unknown.
* **Constraints:** Limits on budget, time, capacity, policy, or resources.

Scenario analysis can help decision-makers compare possible outcomes.

For example, a business might estimate the financial consequences of low, medium, and high demand. Each scenario should have clearly stated assumptions rather than being presented as a guaranteed forecast.

## 7. Communicating a Recommendation

A useful recommendation contains five elements:

1. **Business objective:** What outcome matters?
2. **Evidence:** What did the analysis find?
3. **Proposed action:** What should happen next?
4. **Expected impact:** What improvement is anticipated, and with what uncertainty?
5. **Measurement plan:** How will the result be evaluated?

Example:

"Test a revised discount policy in selected product categories. The analysis suggests that discounting and unit costs may be contributing to lower margins. Track gross profit per order, total sales volume, and customer retention against an appropriate baseline before expanding the policy."

This recommendation proposes a test rather than assuming the cause has already been proven.

## 8. Common Problem-Solving Failures

* Defining a solution before understanding the problem
* Confusing symptoms with causes
* Collecting data without a specific analytical question
* Ignoring alternative explanations
* Using inappropriate comparison periods
* Treating correlation as proof of causation
* Optimizing one KPI while damaging another
* Ignoring implementation costs
* Failing to assign responsibility for action
* Measuring outputs instead of business outcomes

## 9. Practical Exercise

### Scenario: Rising Customer Complaints

A delivery company reports an increase in customer complaints over the last two months.

Prepare a structured analysis plan answering:

1. What is the initial problem statement?
2. Which additional information is required?
3. Which three KPIs would you investigate?
4. How would you segment complaints?
5. List four possible causes.
6. Explain how you would test two of those causes.
7. Suggest three potential interventions.
8. Identify the risks of each intervention.
9. Propose a method to evaluate the intervention's effectiveness.
10. Explain what evidence would make you revise your initial hypothesis.

### Expected Deliverable

Produce a short business memo containing:

* Problem statement
* Analytical questions
* Data requirements
* Hypotheses
* Proposed methods
* Candidate actions
* Success metrics
* Limitations

## 10. Key Takeaway

Effective business problem-solving connects a clearly defined business objective to reliable evidence, testable explanations, realistic actions, and measurable outcomes.

The analyst's role is not merely to find patterns. It is to help the organization make better decisions while being transparent about uncertainty and limitations.
