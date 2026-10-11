# 08 — Solution Evaluation

## 1. Introduction

Solution Evaluation assesses the performance and value of a solution after or during implementation. It examines how well a solution satisfies business needs, delivers expected outcomes, operates within its environment, and creates value for stakeholders.

For advanced business analysts, evaluation does not end when a project is delivered. A solution may meet its technical specifications but still fail to achieve its business objectives because of adoption problems, process weaknesses, external changes, or unrealistic assumptions.

This module follows the Solution Evaluation knowledge area of the BABOK® Guide.

## 2. Purpose of Solution Evaluation

Solution Evaluation determines whether a solution is delivering the intended results and identifies opportunities to improve value.

Key activities include:

* Measuring solution performance.
* Analyzing actual versus expected outcomes.
* Identifying performance limitations.
* Assessing organizational constraints.
* Recommending actions to increase value.
* Evaluating changes to the solution or operating environment.

Evaluation can occur before full deployment, during implementation, and after the solution has been in operation.

## 3. Measuring Solution Performance

Solution performance describes how effectively a solution operates against established criteria.

### 3.1 Performance Dimensions

Depending on the solution, assess:

* Functional completeness.
* Reliability.
* Availability.
* Response time.
* Security.
* Usability.
* Accessibility.
* Accuracy.
* Maintainability.
* Scalability.
* Operational cost.
* Stakeholder satisfaction.

### 3.2 Performance Indicators

Indicators should connect to the purpose of the solution.

For a customer support platform, possible indicators include:

* Average resolution time.
* First-contact resolution.
* Repeat-contact rate.
* Customer satisfaction.
* System availability.
* Cost per resolved case.

For a manufacturing system, possible indicators include:

* Equipment downtime.
* Defect rate.
* Production throughput.
* Maintenance cost.
* Schedule adherence.

A metric should be defined clearly enough that different teams interpret and calculate it consistently.

## 4. Baselines and Targets

A baseline establishes performance before the change. A target defines the intended future performance.

Example:

* Baseline average processing time: 50 minutes.
* Target processing time: 35 minutes.
* Actual processing time after implementation: 40 minutes.

Absolute improvement:

50 − 40 = 10 minutes.

Relative improvement:

$$
\frac{50-40}{50}\times100=20\%.
$$

The solution improved processing time by 20% relative to the baseline but did not achieve the target reduction of 30%.

This distinction is important because a solution can produce measurable improvement without meeting its original objectives.

### 4.1 Establishing Comparable Measurements

Comparisons should account for:

* Differences in workload.
* Seasonal demand.
* Changes in staffing.
* Process changes.
* Data collection methods.
* External market conditions.
* Changes in measurement definitions.

Without consistent measurement conditions, apparent improvement may not reflect the solution's actual contribution.

## 5. Evaluating Business Value

Business value concerns the benefits and outcomes delivered to stakeholders.

### 5.1 Financial Measures

Possible measures include:

* Revenue growth.
* Operating cost reduction.
* Gross margin.
* Net present value.
* Return on investment.
* Payback period.
* Cost avoidance.

### 5.2 Non-Financial Measures

Possible measures include:

* Customer satisfaction.
* Service quality.
* Employee experience.
* Regulatory compliance.
* Risk reduction.
* Faster decisions.
* Improved accessibility.
* Organizational resilience.

Both financial and non-financial value should be considered when relevant to the business case.

### 5.3 Benefit Realization

Benefit realization examines whether expected benefits actually occur.

A benefit may require:

* A technically functional solution.
* Process redesign.
* Staff training.
* Changed stakeholder behavior.
* Data quality improvements.
* Updated policies.
* Ongoing operational support.

Consequently, a solution's value may depend on organizational changes beyond the technology itself.

## 6. Identifying Solution Limitations

A solution limitation is a condition that prevents a solution from achieving its intended performance or value.

### 6.1 Common Limitations

Examples include:

* Insufficient infrastructure capacity.
* Poor data quality.
* Integration failures.
* Inadequate user training.
* Complex workflows.
* Missing functionality.
* High operating costs.
* Security constraints.
* Inconsistent business rules.
* Limited scalability.

### 6.2 Distinguishing Symptoms from Causes

Suppose users complain that a reporting platform is slow.

Possible causes include:

* Inefficient queries.
* Poorly designed data models.
* Network latency.
* Infrastructure constraints.
* Excessive concurrent usage.
* Unnecessary data processing.

Increasing server capacity may reduce the symptom temporarily without addressing the underlying cause.

Solution evaluation should investigate evidence before recommending corrective action.

## 7. Organizational Constraints

A solution may perform as designed but still deliver limited value because of organizational conditions.

Examples include:

* Employees continue using legacy processes.
* Managers do not use available reports.
* Responsibilities remain unclear.
* Incentives discourage adoption.
* Training is insufficient.
* Data ownership is unresolved.
* Business policies conflict with the new workflow.

The analyst should distinguish solution defects from organizational adoption problems because the corrective actions differ.

## 8. Solution Evaluation Techniques

### 8.1 KPI Analysis

Compare actual performance against baselines, targets, and agreed service levels.

### 8.2 User Feedback

Collect information through interviews, surveys, focus groups, and support records.

User feedback can reveal usability problems and unmet needs, but subjective reports should be combined with operational evidence where possible.

### 8.3 Process Analysis

Examine whether the solution improves process flow, reduces bottlenecks, or introduces new work.

### 8.4 Root-Cause Analysis

Use techniques such as the Five Whys, fishbone diagrams, and structured incident analysis to investigate performance gaps.

### 8.5 Benchmarking

Compare performance with relevant internal units, previous periods, or credible external benchmarks.

Comparisons must account for differences in scale, operating context, and measurement definitions.

### 8.6 Cost-Benefit Analysis

Compare actual implementation and operating costs with realized financial and non-financial benefits.

### 8.7 Controlled Pilots and Experiments

Where practical, compare outcomes between a pilot group and an appropriate comparison group.

A controlled design can help distinguish solution effects from broader changes, although ethical, operational, and statistical limitations must be considered.

## 9. Root-Cause Analysis of Performance Gaps

A performance gap is the difference between expected and actual performance.

A structured investigation may follow these steps:

1. Define the performance gap.
2. Confirm the quality of the measurement data.
3. Identify possible causes.
4. Collect additional evidence.
5. Test competing explanations.
6. Identify root causes and contributing factors.
7. Evaluate corrective actions.
8. Measure the results after intervention.

### Example

Expected outcome: Reduce customer complaint resolution time by 30%.

Actual outcome: Resolution time improves by only 10%.

Investigation reveals:

* The system automatically categorizes common complaints.
* Complex complaints still require manual routing.
* Some categories are incorrectly assigned.
* Supervisors do not consistently review escalation alerts.

Potential corrective actions include improving categorization, redesigning escalation procedures, and providing targeted training.

## 10. Recommending Solution Improvements

Recommendations should address identified causes and support measurable business outcomes.

Possible actions include:

* Correcting defects.
* Improving system configuration.
* Optimizing performance.
* Redesigning processes.
* Improving data quality.
* Introducing additional functionality.
* Updating business rules.
* Improving training.
* Changing operating procedures.
* Replacing or retiring a solution.

### 10.1 Recommendation Evaluation

Compare proposed improvements by:

* Expected value.
* Cost.
* Implementation effort.
* Risk.
* Urgency.
* Dependencies.
* Stakeholder impact.
* Strategic alignment.

A technically possible improvement may not be justified if the costs exceed its expected benefits or if it creates unacceptable risks.

## 11. Solution Retirement

A solution may need to be retired when it no longer provides sufficient value or is no longer viable.

Potential reasons include:

* Business needs have changed.
* Technology is no longer supported.
* Maintenance costs are excessive.
* Security risks are unacceptable.
* A replacement provides greater value.
* Regulatory requirements have changed.
* The solution duplicates other capabilities.

Retirement planning should address data retention, migration, contractual obligations, operational continuity, access removal, and stakeholder communication.

## 12. Advanced Case Study: Business Intelligence Platform

### Scenario

A company invests in a business intelligence platform intended to reduce reporting time and improve decision-making.

After six months:

* Reporting preparation time decreases by 25%.
* Only 45% of managers use the platform regularly.
* Several departments report inconsistent metrics.
* Licensing and support costs exceed the initial forecast.

### Evaluation

**Performance:** Reporting is faster, but adoption is limited.

**Business value:** Some efficiency benefits have materialized, but decision-making improvements remain uncertain.

**Solution limitations:** Inconsistent metric definitions and usability concerns reduce confidence in reports.

**Organizational constraints:** Some managers lack training, and several decisions still rely on familiar spreadsheets.

**Financial assessment:** Additional licensing and support costs reduce the net benefit.

### Recommended Actions

1. Standardize metric definitions and ownership.
2. Investigate usability and access barriers.
3. Provide targeted training.
4. Integrate key reporting workflows into management routines.
5. Review licensing and usage levels.
6. Reassess benefits after an agreed monitoring period.

### Key Lesson

A solution can function technically while delivering less value than expected. Effective evaluation examines technology, processes, adoption, costs, and outcomes together.

## 13. Knowledge Check

### Questions

1. What is the purpose of Solution Evaluation?
2. How does solution performance differ from business value?
3. Why are baselines important?
4. Why might a technically successful solution fail to deliver expected benefits?
5. How can an analyst distinguish a solution limitation from an organizational constraint?
6. What is a performance gap?
7. Why should evaluation combine multiple evidence sources?
8. When can benchmarking be misleading?
9. What should guide recommendations for solution improvement?
10. What factors should be considered when retiring a solution?

### Answers

1. To assess solution performance, determine whether expected value is being delivered, and identify improvement opportunities.
2. Performance describes how the solution operates; business value describes the benefits and outcomes achieved for stakeholders.
3. They establish a reference for evaluating change and measuring improvement.
4. Adoption, processes, training, data quality, governance, or external conditions may prevent benefits from being realized.
5. Examine technical behavior and operational evidence alongside process, training, policy, and stakeholder factors.
6. The difference between expected and actual performance.
7. Multiple sources reduce reliance on incomplete measurements or individual perceptions.
8. When compared solutions differ substantially in scale, context, definitions, or operating conditions.
9. Evidence about root causes, expected value, cost, risk, feasibility, and strategic alignment.
10. Data migration, continuity, security, legal obligations, costs, contracts, and stakeholder impacts.

## 14. Practical Exercises

### Exercise 1: KPI Evaluation

Select a digital or operational solution. Define its baseline, target, actual performance, and at least five indicators that measure both operational performance and business value.

### Exercise 2: Root-Cause Analysis

Develop a Five Whys analysis for a solution that failed to meet its performance targets. Identify evidence required to validate each proposed cause.

### Exercise 3: Benefit Realization

Create a benefits realization plan that assigns an owner to each expected benefit, defines measurement methods, and specifies when results will be reviewed.

### Exercise 4: Organizational Constraints

Analyze a situation in which a new system is technically successful but user adoption remains low. Propose interventions and measures to evaluate their effectiveness.

### Exercise 5: Solution Improvement Business Case

Compare three corrective actions for an underperforming solution. Evaluate their expected benefits, costs, risks, implementation effort, and dependencies.

### Exercise 6: Retirement Assessment

Develop a retirement checklist for a legacy business application. Include data retention, migration, access control, contracts, continuity, and stakeholder communication.

## 15. Recommended References

* IIBA, *A Guide to the Business Analysis Body of Knowledge (BABOK® Guide)*, Version 3.
* IIBA, official CBAP certification resources.
* ISO 9001, Quality Management Systems — Requirements.
* ISO 31000, Risk Management — Guidelines.
* ISO/IEC 25010, Systems and Software Quality Models.
* Kaplan and Norton, *The Balanced Scorecard*.

## 16. Module Summary

Solution Evaluation determines whether a solution performs as intended and delivers meaningful value. It combines baseline comparisons, KPI analysis, stakeholder feedback, root-cause investigation, financial assessment, and organizational readiness analysis. The strongest recommendations address the causes of performance gaps and establish measurable ways to confirm whether improvements succeed.
