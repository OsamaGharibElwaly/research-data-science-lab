# 06 — Strategy Analysis

## 1. Introduction

Strategy Analysis describes the work required to identify a business need, understand the current state, define a desired future state, assess risks, and develop a change strategy that enables the organization to move toward that future state.

The BABOK Guide identifies four tasks in this knowledge area:

1. Analyze Current State.
2. Define Future State.
3. Assess Risks.
4. Define Change Strategy.

Strategy Analysis connects business analysis to organizational direction, business capability, and long-term value.

## 2. Analyze Current State

The current state describes the organization's existing capabilities, processes, systems, policies, performance, and operating environment relevant to the business need.

The purpose is to understand why change may be necessary and what conditions must be considered.

### 2.1 Current-State Analysis Objectives

* Understand the business problem or opportunity.
* Identify root causes.
* Establish performance baselines.
* Identify organizational strengths and weaknesses.
* Understand existing capabilities.
* Identify constraints and dependencies.
* Examine stakeholder concerns.
* Identify risks associated with maintaining the status quo.

### 2.2 Current-State Elements

A current-state assessment may examine:

**Business processes:** How work is performed.

**People and organization:** Roles, responsibilities, knowledge, and capacity.

**Technology:** Existing systems, integrations, infrastructure, and limitations.

**Information:** Data quality, ownership, availability, and reporting.

**Policies and rules:** Internal policies and external obligations.

**Performance:** Cost, quality, speed, reliability, and customer outcomes.

**Culture:** Attitudes, behaviors, and readiness for change.

**External environment:** Competition, regulations, suppliers, and market conditions.

### 2.3 Root-Cause Analysis

A visible problem may be a symptom rather than the underlying cause.

Example: A company experiences frequent late deliveries.

Possible causes:

* Inaccurate inventory data.
* Poor demand forecasting.
* Inefficient warehouse layouts.
* Unreliable suppliers.
* Manual scheduling.
* Inadequate staffing.

Purchasing route optimization software may not solve delays caused by incorrect inventory records.

### 2.4 Five Whys

The Five Whys technique repeatedly asks why a problem occurs.

Example:

Problem: Customer orders are shipped late.

1. Why? Orders are released to the warehouse late.
2. Why? Payment confirmation arrives late.
3. Why? Payment status is checked manually.
4. Why? The payment system is not integrated with the order system.
5. Why? The integration was excluded from the original design.

The final explanation is a hypothesis to investigate, not proof that the fifth answer is the only root cause.

### 2.5 SWOT Analysis

SWOT examines:

* **Strengths:** Internal advantages.
* **Weaknesses:** Internal limitations.
* **Opportunities:** External or emerging possibilities.
* **Threats:** External conditions that could cause harm.

Example for a small retailer:

| Category    | Example                                 |
| ----------- | --------------------------------------- |
| Strength    | Loyal local customer base               |
| Weakness    | Manual inventory tracking               |
| Opportunity | Growing online demand                   |
| Threat      | Larger competitors with faster delivery |

SWOT organizes strategic observations but does not replace detailed evidence or financial analysis.

### 2.6 Baseline Performance

A baseline provides a reference against which future performance can be evaluated.

Suppose the current order fulfillment rate is 88%.

The organization may set a future target of 97%.

Without reliable baseline measurement, it becomes difficult to determine whether the change improved performance.

Baseline metrics should have clear definitions, measurement periods, data sources, and ownership.

## 3. Define Future State

The future state describes the conditions the organization wants to achieve.

It should address the business need and establish how success will be evaluated.

### 3.1 Future-State Elements

* Business objectives.
* Desired outcomes.
* Target capabilities.
* Performance measures.
* Organizational changes.
* Required technology.
* Business rules.
* Stakeholder impacts.
* Constraints.
* Risks.
* Value expectations.

### 3.2 SMART Objectives

Objectives are often improved by making them:

* Specific.
* Measurable.
* Achievable.
* Relevant.
* Time-bound.

Example:

Weak: Improve customer service.

Stronger: Reduce average customer support resolution time from 18 hours to eight hours within six months, while maintaining customer satisfaction at or above 90%.

The stronger objective defines the metric, baseline, target, timeframe, and quality condition.

### 3.3 Business Outcomes and Capabilities

A capability is the ability of an organization to achieve a particular result.

Examples:

* Demand forecasting.
* Inventory management.
* Customer relationship management.
* Regulatory reporting.
* Supplier management.
* Digital service delivery.

A future-state analysis asks which capabilities must exist or improve to achieve the desired outcomes.

For example, reducing stockouts may require better forecasting, reliable inventory records, supplier visibility, and replenishment controls.

### 3.4 Value Proposition

A value proposition explains why a change is worthwhile for relevant stakeholders.

It may include:

* Expected benefits.
* Costs.
* Risks.
* Strategic alignment.
* Operational improvements.
* Customer impact.
* Compliance benefits.

Value may be financial or nonfinancial.

A solution that reduces costs but creates unacceptable safety or compliance risks may not be a viable option.

### 3.5 Future-State Measures

Examples include:

| Objective                    | Measure                                     |
| ---------------------------- | ------------------------------------------- |
| Improve delivery reliability | Percentage of orders delivered on time      |
| Reduce operating cost        | Cost per order                              |
| Improve data quality         | Percentage of records meeting quality rules |
| Improve customer experience  | Customer satisfaction score                 |
| Reduce processing delays     | Average processing time                     |
| Improve availability         | Service uptime percentage                   |

Measures should be relevant to the objective and sufficiently reliable to support decisions.

## 4. Identify and Analyze Potential Risks

A risk is an uncertain event or condition that may affect the achievement of objectives.

Strategy Analysis considers risks associated with:

* The current state.
* The desired future state.
* The change strategy.
* The proposed solution.
* Organizational readiness.
* External conditions.

### 4.1 Risk Categories

**Business risks:** The change may not deliver expected benefits.

**Technical risks:** Integration, performance, or reliability may be inadequate.

**Operational risks:** Daily operations may be disrupted.

**Financial risks:** Costs may exceed estimates.

**People risks:** Employees may resist the change or lack necessary skills.

**Regulatory risks:** The change may fail to satisfy applicable obligations.

**Supplier risks:** External providers may not deliver as expected.

**Data risks:** Data quality, privacy, or migration may cause problems.

### 4.2 Risk Assessment

A common qualitative model scores likelihood and impact.

Example scale: 1 to 5.

$$
Risk\ Score = Likelihood \times Impact
$$

A risk with likelihood 4 and impact 5 receives a score of 20.

A risk with likelihood 2 and impact 3 receives a score of 6.

This multiplication is a prioritization aid, not a universally valid probability model. Organizations should define their own scales and response thresholds.

### 4.3 Risk Responses

Common responses include:

* **Avoid:** Change the plan to eliminate the threat.
* **Mitigate:** Reduce its likelihood or impact.
* **Transfer or share:** Allocate part of the exposure to another party through suitable arrangements.
* **Accept:** Recognize the risk and proceed under defined conditions.

Opportunities may be exploited, enhanced, shared, or accepted depending on the risk management framework.

### 4.4 Risk Register

A risk register may include:

| Field       | Purpose                                  |
| ----------- | ---------------------------------------- |
| Risk ID     | Unique identifier                        |
| Description | Uncertain event or condition             |
| Cause       | Source of the risk                       |
| Likelihood  | Estimated probability or rating          |
| Impact      | Potential consequences                   |
| Owner       | Responsible person                       |
| Response    | Planned action                           |
| Status      | Current state                            |
| Trigger     | Condition that signals increased concern |

### 4.5 Risk Appetite and Tolerance

Risk appetite describes the general amount and type of risk an organization is willing to pursue or retain.

Risk tolerance describes acceptable variation around objectives or specific exposure limits.

For example, a company may tolerate limited downtime in an internal reporting system but have almost no tolerance for unauthorized financial transactions.

## 5. Define Change Strategy

A change strategy describes how the organization will transition from the current state to the future state.

It considers alternative approaches and recommends a feasible way to achieve the desired outcomes.

### 5.1 Change Strategy Elements

* Scope of change.
* Solution approach.
* Required capabilities.
* Transition stages.
* Resource requirements.
* Implementation timing.
* Stakeholder engagement.
* Training and communication.
* Data migration.
* Risk responses.
* Dependencies.
* Measures of success.

### 5.2 Solution Alternatives

A business analyst should compare plausible alternatives rather than assume that a single proposed solution is correct.

Possible alternatives include:

* Maintain the current state.
* Improve the existing process.
* Purchase a commercial product.
* Build a custom solution.
* Outsource selected activities.
* Introduce a phased transformation.
* Combine process redesign with technology.

### 5.3 Build vs. Buy

Consider:

* Total cost of ownership.
* Time to implementation.
* Fit with business needs.
* Customization requirements.
* Integration complexity.
* Security and compliance.
* Vendor dependence.
* Maintenance.
* Scalability.
* Internal capabilities.

The lowest purchase price does not necessarily represent the lowest long-term cost.

### 5.4 Gap Analysis

Gap analysis compares current capabilities with the desired future state.

Example:

| Capability           | Current State             | Future State                      | Gap                             |
| -------------------- | ------------------------- | --------------------------------- | ------------------------------- |
| Inventory visibility | Daily spreadsheet updates | Near-real-time visibility         | Integrated inventory records    |
| Demand forecasting   | Manual estimates          | Forecast-supported planning       | Data and forecasting capability |
| Reporting            | Weekly manual reports     | Daily automated reports           | Reporting automation            |
| Staff skills         | Basic spreadsheet use     | System-based inventory management | Training and support            |

The identified gaps help define requirements, solution options, and transition activities.

### 5.5 Transition Strategy

A transition strategy explains how the organization will move from current operations to future operations.

Options include:

**Big-bang implementation:** Switch to the new solution at one point in time.

**Phased implementation:** Introduce capabilities, locations, or user groups in stages.

**Pilot implementation:** Test the solution in a limited environment before wider deployment.

**Parallel operation:** Run old and new systems simultaneously for a defined period.

Each option has trade-offs involving cost, complexity, disruption, and risk.

## 6. Practical Case Study: Warehouse Transformation

A distributor has a 12% stockout rate, frequent manual adjustments, and high fulfillment costs.

### Current state

* Inventory data is updated manually.
* Warehouses use different spreadsheets.
* Forecasts are prepared monthly.
* Managers lack consolidated reporting.
* Employees have limited experience with integrated systems.

### Future state

* Stockout rate reduced from 12% to 4% within twelve months.
* Inventory records updated through controlled transactions.
* Managers can view stock across warehouses.
* Forecasts are reviewed using current demand data.
* Fulfillment cost per order is reduced by 10%.

### Risks

1. Poor legacy data may produce inaccurate opening balances.
2. Staff may resist new procedures.
3. System integration may be delayed.
4. Implementation may disrupt warehouse operations.
5. Forecasting models may perform poorly during demand shocks.

### Change strategy

1. Establish baseline metrics.
2. Clean and standardize product data.
3. Select an appropriate inventory solution.
4. Pilot the system at one warehouse.
5. Train users and refine procedures.
6. Migrate the remaining warehouses in phases.
7. Monitor stockouts, accuracy, cost, and fulfillment.
8. Adjust the implementation based on evidence.

### Evaluation

Compare actual outcomes with the baseline and targets. If stockouts decline but fulfillment costs rise, investigate the trade-off rather than declaring success based on a single measure.

## 7. Knowledge Check

**Question 1:** What is the primary purpose of current-state analysis?

A. To select a vendor immediately
B. To understand existing conditions and the business need
C. To approve all requirements
D. To eliminate all business risks

**Question 2:** Which technique repeatedly asks why a problem occurs?

A. SWOT
B. Five Whys
C. MoSCoW
D. RACI

**Question 3:** A target states, "Reduce average processing time from 10 minutes to six minutes within six months." This is primarily:

A. A measurable future-state objective
B. An assumption
C. A stakeholder map
D. A risk response

**Question 4:** What does gap analysis compare?

A. Two employees' performance only
B. Current capabilities and desired future capabilities
C. Two unrelated financial reports
D. Requirements and meeting schedules

**Question 5:** A project may fail because employees cannot use the new system. Which response is most directly relevant?

A. Ignore the risk
B. Provide appropriate training and adoption support
C. Remove all performance measures
D. Stop stakeholder communication

**Question 6:** Which statement about change strategies is correct?

A. Big-bang implementation is always cheapest and safest.
B. The analyst should evaluate alternatives and their trade-offs.
C. A pilot removes every implementation risk.
D. A change strategy does not need to consider stakeholders.

### Answers and Explanations

1. **B.** Current-state analysis establishes the facts and conditions surrounding the business need.
2. **B.** Five Whys explores possible underlying causes.
3. **A.** The statement defines a metric, baseline, target, and timeframe.
4. **B.** Gap analysis identifies differences between current and desired capabilities.
5. **B.** Training and adoption support address a skills-related risk.
6. **B.** The appropriate strategy depends on context, risk, cost, and organizational needs.

## 7. Revision Summary

* Current-state analysis explains the existing environment and the business need.
* Future-state definition describes desired outcomes, capabilities, and measures.
* Root-cause analysis distinguishes symptoms from underlying problems.
* Risks must be assessed and managed.
* Gap analysis identifies capabilities that must be created or improved.
* Change strategies compare alternatives and define a practical transition.
* Implementation choices involve trade-offs among risk, cost, speed, and disruption.

## 8. Further Study

Review the BABOK Guide's Strategy Analysis knowledge area. Practice current-state analysis, future-state definition, risk assessment, gap analysis, and comparison of change strategies using realistic organizational scenarios.
