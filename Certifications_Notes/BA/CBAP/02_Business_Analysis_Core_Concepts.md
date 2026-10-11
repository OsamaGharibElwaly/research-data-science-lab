# 02 — Business Analysis Core Concepts

## 1. Introduction

Advanced business analysis requires a consistent understanding of needs, requirements, designs, value, context, stakeholders, and change. These concepts support clear communication, sound decisions, effective governance, and traceability across complex initiatives.

This module expands on the foundational concepts introduced in Module 01 and emphasizes their application to advanced business analysis scenarios.

## 2. Business Needs

A business need describes a problem to be solved or an opportunity to be realized.

### 2.1 Problem-Oriented Needs

Problem-oriented needs arise when actual performance falls short of expectations.

Examples:

* Customer complaints exceed the acceptable threshold.
* Inventory accuracy is below the required level.
* Operating costs exceed the approved budget.
* A manual process creates excessive delays.

### 2.2 Opportunity-Oriented Needs

Opportunity-oriented needs arise when an organization identifies potential improvements or new sources of value.

Examples:

* Entering a new market.
* Introducing a new service.
* Automating repetitive administrative work.
* Using analytics to improve demand forecasting.

### 2.3 Need Validation

A business analyst should determine whether the need is:

* Clearly defined.
* Supported by credible evidence.
* Consistent with organizational objectives.
* Important enough to justify action.
* Feasible to address within relevant constraints.
* Understood by the stakeholders who will be affected.

A stakeholder's request is evidence of a possible need, not proof that the proposed solution is necessary.

## 3. Requirements

A requirement is a usable representation of a need. Requirements provide a basis for designing, implementing, evaluating, and accepting changes.

### 3.1 Business Requirements

Business requirements describe organizational goals, objectives, and desired outcomes.

Example:

"Reduce the average time required to resolve customer complaints by 25% within six months."

A good business requirement explains the outcome the organization seeks rather than prescribing a particular technology.

### 3.2 Stakeholder Requirements

Stakeholder requirements describe the needs of an individual stakeholder or group.

Example:

"Customer service supervisors need to identify unresolved complaints approaching their service-level deadlines."

Stakeholder requirements connect organizational objectives with the needs of people affected by a change.

### 3.3 Solution Requirements

Solution requirements describe capabilities or characteristics a solution must provide.

They include functional and non-functional requirements.

**Functional requirements** describe behavior or capabilities.

Example:

"The system shall notify a supervisor when a complaint remains unresolved for 24 hours."

**Non-functional requirements** describe quality attributes or conditions under which the solution must operate.

Examples:

* Performance.
* Security.
* Availability.
* Accessibility.
* Reliability.
* Usability.
* Maintainability.
* Scalability.

Non-functional requirements should be sufficiently precise to support verification.

Example:

"The system shall support 500 concurrent users while maintaining a 95th-percentile response time below two seconds under the defined load test."

The threshold and test conditions must be validated with stakeholders.

### 3.4 Transition Requirements

Transition requirements describe temporary capabilities needed to move from the current state to the future state.

Examples:

* Data migration.
* User training.
* Temporary parallel operations.
* Initial data cleansing.
* Legacy-system decommissioning.
* Transitional reporting.

These requirements are generally no longer needed once the transition is complete.

## 4. Requirements Versus Designs

Requirements describe what is needed or what must be true. Designs describe how a solution may satisfy those needs.

Example:

* Requirement: Users must authenticate before accessing confidential records.
* Design: Use a specific identity provider with multifactor authentication and role-based access controls.

A requirement can have multiple possible designs. Separating requirements from designs helps prevent unnecessary constraints and encourages meaningful comparison of alternatives.

However, the distinction depends on the level of abstraction. A design decision at one level may become a requirement at another level when it establishes a binding architectural or regulatory constraint.

## 5. The Business Analysis Core Concept Model

The BACCM contains six concepts that are always relevant to business analysis.

### 5.1 Change

Change is the act of transformation in response to a need.

It may involve:

* People.
* Processes.
* Technology.
* Organizational structures.
* Policies.
* Business models.

Change may be incremental or transformational.

### 5.2 Need

A need is a problem or opportunity requiring attention. It provides the rationale for change.

A clearly established need prevents organizations from investing in solutions without sufficient justification.

### 5.3 Solution

A solution satisfies one or more needs in a specific context.

Solutions should be evaluated against expected benefits, risks, constraints, and stakeholder expectations.

### 5.4 Stakeholder

A stakeholder has an interest in, influence over, or relationship with the change, need, or solution.

Stakeholders may be internal or external, direct or indirect, supportive or resistant.

### 5.5 Value

Value is the worth, importance, or usefulness of an outcome to a stakeholder in context.

Value may include financial benefits, improved service quality, reduced exposure to risk, or better decision-making.

### 5.6 Context

Context includes the conditions and circumstances surrounding the change.

It can include market conditions, organizational culture, regulations, existing systems, resource limitations, and stakeholder relationships.

### 5.7 Applying the Model to a Requirement

Consider a hospital introducing an electronic appointment system.

* Change: Replace manual appointment scheduling.
* Need: Reduce booking errors and waiting times.
* Solution: Introduce an electronic scheduling system.
* Stakeholders: Patients, receptionists, clinicians, administrators, and IT staff.
* Value: Reduced administrative workload and improved patient access.
* Context: Patient privacy, existing medical systems, staff capabilities, and clinical workflows.

The model helps ensure that requirements remain connected to the broader business problem.

## 6. Business Value and Value Measurement

Value should be defined in measurable or otherwise assessable terms whenever possible.

### 6.1 Financial Value

Financial measures include:

* Revenue growth.
* Cost reduction.
* Profit margin.
* Return on investment.
* Net present value.
* Payback period.

### 6.2 Non-Financial Value

Non-financial measures include:

* Customer satisfaction.
* Employee experience.
* Compliance.
* Reputation.
* Service quality.
* Accessibility.
* Organizational resilience.

Non-financial benefits may still have significant financial implications, but they should not be assigned arbitrary monetary values without a defensible method.

### 6.3 Baselines and Targets

A baseline represents current performance. A target represents desired performance.

Example:

* Baseline average resolution time: 10 hours.
* Target average resolution time: 7 hours.
* Absolute improvement: 3 hours.
* Relative reduction: 30%.

Relative reduction is calculated as:

Reduction percentage = (Baseline − New value) / Baseline × 100%.

A reliable value assessment requires consistent definitions and comparable measurement conditions.

## 7. Stakeholders and Stakeholder Perspectives

Stakeholders may interpret the same change differently.

For example, automating invoice processing may:

* Reduce administrative workload for finance.
* Require training for existing staff.
* Increase integration work for IT.
* Improve payment visibility for suppliers.
* Introduce new control requirements for auditors.

Business analysts should identify stakeholders early, understand their interests, and evaluate both benefits and negative impacts.

### 7.1 Stakeholder Analysis

A stakeholder analysis can document:

* Stakeholder identity and role.
* Business interests.
* Expectations.
* Influence and decision authority.
* Required information.
* Potential impacts.
* Conflicts or dependencies.
* Engagement needs.

Power-interest grids, stakeholder maps, interviews, and responsibility matrices may support this analysis.

### 7.2 Conflicting Interests

Conflicts may concern:

* Scope.
* Cost.
* Schedule.
* Quality.
* Risk tolerance.
* Privacy.
* Operational disruption.
* Distribution of benefits.

The business analyst should make trade-offs explicit and help decision-makers evaluate them against agreed objectives and governance rules.

## 8. Context and Constraints

A solution must operate within its actual environment.

### 8.1 Business Context

Relevant factors include:

* Strategic objectives.
* Existing processes.
* Organizational culture.
* Workforce capabilities.
* Customer expectations.
* Supplier relationships.

### 8.2 Technical Context

Technical factors include:

* Legacy systems.
* APIs and integration patterns.
* Data quality.
* Infrastructure capacity.
* Security architecture.
* Vendor dependencies.

### 8.3 Regulatory and External Context

External factors may include:

* Privacy regulations.
* Industry standards.
* Contractual obligations.
* Economic conditions.
* Competitive pressures.
* Market demand.

### 8.4 Assumptions, Constraints, and Dependencies

An **assumption** is something treated as true for planning or analysis purposes but not yet fully confirmed.

A **constraint** restricts available choices.

A **dependency** describes a relationship in which one activity, requirement, or outcome depends on another.

Example:

* Assumption: Most customers have internet access.
* Constraint: The project must comply with applicable privacy laws.
* Dependency: The new reporting platform depends on the availability of a cleaned customer database.

Assumptions should be validated, constraints documented, and dependencies monitored.

## 9. Current State and Future State

Current-state analysis establishes how an organization operates today.

It may include:

* Process maps.
* System inventories.
* Performance metrics.
* Organizational responsibilities.
* Pain points.
* Existing controls.
* Known risks.

Future-state analysis describes the intended operating model after change.

It may include:

* Target processes.
* Required capabilities.
* New roles.
* System behavior.
* Performance targets.
* Governance changes.

### 9.1 Gap Analysis

Gap analysis compares the current state with the desired future state.

Example:

| Capability      | Current State                  | Future State               | Gap                         |
| --------------- | ------------------------------ | -------------------------- | --------------------------- |
| Reporting       | Manual monthly reports         | Automated daily reports    | Reporting automation        |
| Data quality    | Frequent duplicate records     | Validated customer records | Data cleansing and controls |
| Decision-making | Delayed performance visibility | Near-real-time monitoring  | Improved data integration   |

Gap analysis helps identify the work needed to achieve the target state.

## 10. Requirements Quality

High-quality requirements should be appropriate for their intended purpose and sufficiently clear to support design, implementation, and evaluation.

Useful quality characteristics include:

* Clear and understandable.
* Necessary.
* Feasible.
* Consistent with other requirements.
* Testable or verifiable.
* Traceable.
* Unambiguous.
* Appropriately detailed.
* Aligned with the business need.

The level of detail depends on the delivery approach and the decision being supported.

### 10.1 Common Requirement Defects

Examples include:

* Vague language: "The system should be fast."
* Unverifiable claims: "The interface must be excellent."
* Hidden design assumptions: "The company must purchase Vendor X."
* Conflicting expectations: Two requirements specify incompatible processing rules.
* Missing conditions: A requirement does not identify when a behavior should occur.
* Unnecessary requirements: A feature has no demonstrated relationship to an approved need.

### 10.2 Improving Requirement Quality

Weak requirement:

"The system should generate reports quickly."

Improved requirement:

"The system shall generate the standard monthly operations report within 10 seconds for datasets containing up to one million records under the approved test environment."

The improved version defines the operation, time limit, data volume, and testing context.

## 11. Traceability and Relationships

Traceability establishes relationships between requirements and other elements of business analysis.

A traceability chain may connect:

Business objective → Business requirement → Stakeholder requirement → Solution requirement → Design element → Test case → Outcome measure.

Traceability supports:

* Impact analysis.
* Change assessment.
* Coverage analysis.
* Verification.
* Auditability.
* Benefit realization.

Traceability should be proportionate to the complexity, risk, and governance needs of the initiative.

## 12. Advanced Case Study: Customer Service Transformation

### Scenario

An online retailer experiences rising complaint volumes. Executives request a chatbot to reduce support costs.

### Analysis

**Need:** Determine why support demand and resolution times are increasing.

**Evidence:** Complaint categories, contact volume, resolution times, repeat contacts, customer feedback, and staffing patterns.

**Stakeholders:** Customers, support agents, team leaders, IT, legal, and senior management.

**Possible solutions:**

1. Improve self-service knowledge articles.
2. Redesign the complaint-resolution workflow.
3. Introduce chatbot-assisted support.
4. Improve product information and order tracking.
5. Combine selected interventions.

**Requirements:**

* Customers must be able to find accurate order information.
* The service must protect personal information.
* Complex cases must be transferred to human agents.
* Performance must be monitored through agreed service indicators.

**Value measures:**

* Average resolution time.
* First-contact resolution.
* Repeat-contact rate.
* Customer satisfaction.
* Cost per resolved case.
* Escalation rate.

The analyst should avoid assuming that a chatbot is the best solution until the evidence establishes where the main problems originate.

## 13. Knowledge Check

### Questions

1. What distinguishes a business requirement from a solution requirement?
2. What is the difference between a requirement and a design?
3. Why are transition requirements temporary?
4. How does the BACCM improve business analysis?
5. What is the difference between an assumption and a constraint?
6. Why are baseline measurements important?
7. What is the purpose of gap analysis?
8. How does traceability support change management?
9. Why should non-functional requirements be measurable where possible?
10. How should a business analyst address conflicting stakeholder expectations?

### Answers

1. Business requirements describe organizational goals and outcomes; solution requirements describe capabilities or characteristics needed from a solution.
2. Requirements express what is needed or expected, while designs describe how a solution may satisfy the need.
3. They support migration or transition and are no longer needed after the transition is complete.
4. It provides an interconnected framework for examining change, needs, solutions, stakeholders, value, and context.
5. An assumption is treated as true for planning; a constraint restricts available choices.
6. Baselines provide a reference for evaluating whether performance has improved.
7. Gap analysis identifies differences between current capabilities and the desired future state.
8. Traceability reveals which requirements, designs, tests, and outcomes may be affected by a proposed change.
9. Measurable requirements support objective verification and reduce interpretation disputes.
10. Identify interests, establish decision criteria, document trade-offs, and follow appropriate governance and approval processes.

## 14. Practical Exercises

### Exercise 1: Requirement Classification

Classify each statement as a business, stakeholder, solution-functional, solution-non-functional, or transition requirement:

1. Reduce customer complaints by 20%.
2. Supervisors need a view of unresolved complaints.
3. The system shall notify supervisors about overdue cases.
4. The application shall maintain 99.9% monthly availability.
5. Staff must complete training before launch.

Explain any ambiguity in the statements.

### Exercise 2: Current-State and Future-State Analysis

Choose an administrative or operational process. Document its current workflow, problems, desired outcomes, capability gaps, and measurable future-state objectives.

### Exercise 3: Traceability

Develop a traceability matrix linking at least three business objectives to stakeholder requirements, solution requirements, verification activities, and outcome measures.

### Exercise 4: Stakeholder Conflict

Imagine that management wants to reduce service costs while customers demand faster human support. Propose decision criteria that balance cost, service quality, risk, and stakeholder value.

## 15. Recommended References

* IIBA, *A Guide to the Business Analysis Body of Knowledge (BABOK® Guide)*, Version 3.
* IIBA, Business Analysis Core Concept Model resources.
* ISO 9001, Quality Management Systems — Requirements.
* ISO/IEC/IEEE 29148, Requirements Engineering.
* ISO 31000, Risk Management — Guidelines.

## 16. Module Summary

Business analysis core concepts provide the vocabulary and structure required to investigate needs, define requirements, evaluate designs, understand stakeholders, and measure value. Strong analysis connects every important requirement to a legitimate need and evaluates proposed changes within their organizational, technical, and regulatory context.
