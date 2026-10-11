# 03 — Business Analysis Planning and Monitoring

## 1. Introduction

Business Analysis Planning and Monitoring establishes how business analysis work will be organized, governed, monitored, and improved.

At the advanced level, planning is not merely scheduling interviews or producing documentation. It involves selecting an appropriate approach, defining stakeholder engagement, establishing governance, managing information, coordinating decisions, and evaluating the effectiveness of business analysis activities.

This module follows the relevant knowledge area in the BABOK® Guide, supplemented with advanced practical applications.

## 2. Purpose of Business Analysis Planning

Business analysis planning determines the activities required to achieve analysis objectives and how those activities will be performed.

Planning should address:

* Scope of business analysis work.
* Analysis approach and methods.
* Stakeholder roles and responsibilities.
* Communication and engagement.
* Information management.
* Governance and decision-making.
* Deliverables and quality expectations.
* Risks, dependencies, and constraints.
* Performance measurement.

A business analysis plan should be appropriate to the size, complexity, risk, and delivery environment of the initiative.

## 3. Planning the Business Analysis Approach

The business analysis approach describes the overall strategy for performing analysis.

### 3.1 Predictive Approach

A predictive approach generally defines significant analysis activities and deliverables in advance.

Typical characteristics:

* Structured planning.
* Formal documentation.
* Defined approval points.
* Baseline management.
* Change control.
* Detailed requirements before major implementation stages.

It is often appropriate when regulatory obligations, contractual requirements, or costly dependencies demand extensive planning.

### 3.2 Adaptive Approach

An adaptive approach evolves through feedback and incremental discovery.

Typical characteristics:

* Iterative planning.
* Frequent stakeholder feedback.
* Progressive elaboration of requirements.
* Short delivery cycles.
* Continuous reprioritization.
* Early validation of assumptions.

It is useful when the solution space is uncertain or business priorities change frequently.

### 3.3 Hybrid Approach

Hybrid approaches combine structured governance with iterative analysis and delivery.

Example:

A healthcare organization maintains formal privacy, security, and approval controls while using short iterations to refine a patient-facing application.

### 3.4 Selecting an Approach

Evaluate:

* Requirement uncertainty.
* Business volatility.
* Stakeholder availability.
* Regulatory requirements.
* Cost of change.
* Delivery deadlines.
* Organizational maturity.
* Team experience.
* Integration dependencies.
* Risk exposure.

The approach should be justified by the circumstances, not chosen simply because a method is fashionable.

## 4. Planning Business Analysis Activities

Business analysis activities may include:

* Reviewing existing documentation.
* Conducting stakeholder interviews.
* Facilitating workshops.
* Observing business processes.
* Modeling current and future states.
* Defining requirements.
* Evaluating solution alternatives.
* Validating information.
* Supporting prioritization.
* Assessing changes.
* Evaluating solution performance.

### 4.1 Activity Sequencing

Some activities depend on earlier results.

Example:

1. Identify the business need.
2. Analyze stakeholders and context.
3. Investigate the current state.
4. Define desired outcomes.
5. Develop and assess requirements.
6. Evaluate solution options.
7. Support implementation and verification.
8. Assess realized value.

Real initiatives may revisit earlier steps as new evidence emerges.

### 4.2 Effort Estimation

Estimate effort by considering:

* Number and complexity of stakeholders.
* Availability and quality of existing information.
* Technical and organizational complexity.
* Degree of uncertainty.
* Required documentation.
* Approval processes.
* Geographic or cultural distribution.
* Dependencies and competing priorities.

Possible estimation techniques include expert judgment, analogous estimation, decomposition, and three-point estimation.

Three-point estimation can use:

* Optimistic estimate (O).
* Most likely estimate (M).
* Pessimistic estimate (P).

A commonly used PERT-style estimate is:

Expected effort = (O + 4M + P) / 6.

This is a planning approximation, not a guarantee of actual effort.

## 5. Stakeholder Engagement Planning

Stakeholder engagement planning identifies the stakeholders who must contribute to, review, approve, or be informed about business analysis work.

### 5.1 Identify Stakeholders

Consider:

* Executive sponsors.
* Business owners.
* Customers.
* End users.
* Subject-matter experts.
* Technical specialists.
* Operations teams.
* Compliance and legal teams.
* Vendors and partners.
* Governance bodies.

Some stakeholders may be indirectly affected and should not be overlooked simply because they are not part of the project team.

### 5.2 Assess Stakeholder Characteristics

Examine:

* Authority and influence.
* Knowledge and expertise.
* Interests and expectations.
* Availability.
* Attitude toward change.
* Preferred communication methods.
* Potential conflicts.
* Impact of the proposed change.

### 5.3 Stakeholder Engagement Techniques

Useful techniques include:

* Stakeholder maps.
* Power-interest grids.
* Interviews.
* Workshops.
* Surveys.
* Focus groups.
* Observation.
* Reviews and demonstrations.

Engagement should be proportionate to stakeholder impact and the decisions requiring input.

### 5.4 Managing Resistance

Resistance may result from:

* Fear of job displacement.
* Lack of trust.
* Poor communication.
* Previous failed initiatives.
* Increased workload.
* Conflicting incentives.
* Concerns about privacy or control.

A business analyst should investigate the underlying concern rather than label every disagreement as unreasonable resistance.

## 6. Business Analysis Governance

Governance defines how decisions are made, who has authority, how approvals occur, and how conflicts are resolved.

Governance may cover:

* Requirement approval.
* Prioritization.
* Change requests.
* Escalation.
* Quality reviews.
* Decision records.
* Exception handling.
* Regulatory compliance.
* Acceptance criteria.

### 6.1 Roles and Responsibilities

Possible roles include:

* Business analyst.
* Business sponsor.
* Product owner.
* Subject-matter expert.
* Project manager.
* Solution architect.
* Development lead.
* Test lead.
* Change manager.

Responsibilities vary across organizations. A business analyst may facilitate a decision without having final approval authority.

### 6.2 RACI Matrix

A RACI matrix clarifies participation:

* **Responsible:** Performs the work.
* **Accountable:** Ultimately owns the outcome or decision.
* **Consulted:** Provides input.
* **Informed:** Receives updates.

Example:

| Activity                       | Business Analyst | Sponsor | Technical Lead | Operations |
| ------------------------------ | ---------------- | ------- | -------------- | ---------- |
| Elicit business needs          | R                | C       | C              | C          |
| Approve business objectives    | C                | A       | I              | C          |
| Assess technical feasibility   | C                | I       | A/R            | C          |
| Validate operational readiness | C                | I       | C              | A/R        |

This example is illustrative. Actual accountability should follow the organization's governance structure.

## 7. Information Management Planning

Business analysis produces and uses information that must be organized, maintained, protected, and made accessible.

### 7.1 Information Management Considerations

Define:

* Repository and storage location.
* Naming and versioning conventions.
* Access permissions.
* Confidentiality classifications.
* Retention periods.
* Approval status.
* Traceability rules.
* Review and update responsibilities.
* Archiving and disposal processes.

### 7.2 Requirements Repositories

A repository may contain:

* Business requirements.
* Stakeholder requirements.
* Solution requirements.
* Models and diagrams.
* Decision records.
* Assumptions and constraints.
* Change requests.
* Approval history.
* Test traceability.
* Solution evaluation results.

A spreadsheet may be sufficient for a small initiative. Larger or regulated initiatives may require dedicated requirements management or lifecycle management tools.

### 7.3 Version Control

Version control helps teams identify:

* What changed.
* Who changed it.
* When the change occurred.
* Why the change was made.
* Whether approval was required.
* Which downstream artifacts are affected.

Changes should not silently overwrite approved requirements where historical traceability is important.

### 7.4 Information Security

Business analysis information may include sensitive customer, employee, commercial, or technical data.

Controls should include appropriate access restrictions, secure storage, data minimization, and compliance with applicable privacy and retention requirements.

## 8. Business Analysis Performance Management

Performance management evaluates whether business analysis work is effective and whether its processes need improvement.

### 8.1 Possible Performance Measures

Examples include:

* Requirements rework rate.
* Time required to obtain decisions.
* Stakeholder review participation.
* Defect rates attributable to requirement ambiguity.
* Percentage of requirements with traceability.
* Time taken to assess change requests.
* Stakeholder satisfaction with analysis outputs.
* Percentage of identified assumptions validated.

Measures should support decisions rather than create activity for its own sake.

### 8.2 Leading and Lagging Indicators

Leading indicators help anticipate future performance.

Examples:

* Percentage of high-risk assumptions still unvalidated.
* Number of unresolved requirement conflicts.
* Stakeholder review backlog.

Lagging indicators reflect results that have already occurred.

Examples:

* Defects discovered after release.
* Actual requirement rework.
* Final stakeholder satisfaction.
* Realized business benefits.

A balanced set of indicators helps identify problems early while still measuring outcomes.

### 8.3 Avoiding Misleading Metrics

A high number of requirements completed does not necessarily indicate high business value.

Likewise, a low change-request count may indicate stable requirements or ineffective stakeholder engagement.

Interpret metrics in context and combine quantitative results with qualitative evidence.

## 9. Planning for Risks and Uncertainty

Business analysis plans should identify uncertainties that could affect analysis quality or delivery.

Common risks include:

* Key stakeholders are unavailable.
* Existing documentation is outdated.
* Business objectives conflict.
* Requirements depend on unverified assumptions.
* Decisions are delayed.
* Data quality is inadequate.
* Regulatory interpretation is uncertain.
* Solution dependencies are not understood.

For each significant risk, record:

* Description.
* Probability.
* Impact.
* Owner.
* Mitigation or response.
* Trigger or warning indicator.
* Review date.

Risk prioritization should reflect organizational criteria and the potential consequences of failure.

## 10. Monitoring Business Analysis Work

Monitoring compares actual performance against the plan and identifies required adjustments.

Activities may include:

* Reviewing progress against milestones.
* Monitoring stakeholder participation.
* Tracking unresolved decisions.
* Reviewing requirements quality.
* Assessing effort and schedule.
* Monitoring assumptions and dependencies.
* Evaluating changes to scope.
* Updating the analysis approach when necessary.

A plan is a management tool, not an immutable document. Material changes in context may justify revising the approach.

## 11. Evaluating Business Analysis Effectiveness

Business analysis effectiveness concerns whether the selected approach and activities are producing useful results.

Evaluation questions include:

* Are stakeholders receiving the information they need?
* Are requirements clear and usable?
* Are decisions being made promptly?
* Is rework decreasing?
* Are analysis outputs supporting implementation?
* Are business objectives remaining clear?
* Are emerging risks being identified?
* Are stakeholders satisfied with the process?

Findings should lead to practical improvements.

For example, if repeated misunderstandings arise from long documents, the team might introduce process diagrams, prototypes, structured reviews, or clearer examples.

## 12. Advanced Case Study: Enterprise Reporting Transformation

### Scenario

A multinational company plans to replace separate departmental reports with a shared analytics platform.

Challenges include:

* Different definitions of revenue.
* Conflicting departmental priorities.
* Poor source-data quality.
* Regulatory restrictions.
* Limited stakeholder availability.

### Planning Decisions

**Approach:** Use formal governance for data definitions, security, and executive approvals, combined with iterative delivery of dashboards.

**Stakeholders:** Finance, sales, operations, data engineering, compliance, and executive leadership.

**Governance:** Establish a decision owner for metric definitions and a documented escalation process.

**Information management:** Use a controlled repository for requirements, metric definitions, approvals, and data lineage.

**Performance indicators:**

* Decision turnaround time.
* Percentage of agreed metrics with documented definitions.
* Data-quality defect rate.
* Requirement rework.
* Stakeholder acceptance.
* Reporting preparation time.

**Risks:** Inconsistent definitions, poor data quality, delayed approvals, and unauthorized data access.

### Lessons

Effective planning aligns the analysis approach with business risk, decision complexity, stakeholder availability, and the organization's ability to implement change.

## 13. Knowledge Check

### Questions

1. What is the purpose of planning the business analysis approach?
2. What factors influence the choice between predictive and adaptive approaches?
3. How does stakeholder engagement planning improve analysis quality?
4. What is the difference between responsible and accountable in a RACI matrix?
5. Why is information management important?
6. How do leading indicators differ from lagging indicators?
7. Why can a low change-request count be misleading?
8. What should happen when assumptions or business conditions change?
9. What is the purpose of governance?
10. How can business analysis performance measures support continuous improvement?

### Answers and Explanations

1. It defines how analysis activities will be performed, coordinated, governed, and evaluated.
2. Uncertainty, regulatory needs, cost of change, stakeholder availability, complexity, and delivery conditions.
3. It ensures the right people contribute at appropriate times and that their needs and concerns are understood.
4. Responsible performs the work; accountable owns the decision or outcome.
5. It supports consistency, traceability, collaboration, confidentiality, and reliable decision-making.
6. Leading indicators warn about potential future issues; lagging indicators measure outcomes that have already occurred.
7. It may reflect stable requirements, but it may also indicate that stakeholders are not identifying or reporting changes.
8. Reassess the plan, validate the assumptions, and revise activities or decisions where justified.
9. It establishes decision authority, approvals, accountability, and escalation.
10. They reveal inefficiencies and quality problems that can be addressed through targeted changes to the analysis process.

## 14. Practical Exercises

### Exercise 1: Approach Selection

Choose a project with uncertain requirements and significant regulatory constraints. Recommend a predictive, adaptive, or hybrid approach and justify your choice.

### Exercise 2: Stakeholder Engagement Plan

Identify at least eight stakeholders for a business transformation. Document their interests, influence, engagement method, communication frequency, and required decisions.

### Exercise 3: RACI Matrix

Create a RACI matrix for requirements elicitation, approval, change control, solution verification, and business acceptance.

### Exercise 4: Performance Dashboard

Design a small business analysis performance dashboard containing at least three leading indicators, three lagging indicators, and an explanation of how each measure supports decisions.

### Exercise 5: Risk Register

Create a risk register for an initiative involving inconsistent data, competing stakeholders, and strict delivery deadlines. Include owners, impacts, responses, and warning indicators.

## 15. Recommended References

* IIBA, *A Guide to the Business Analysis Body of Knowledge (BABOK® Guide)*, Version 3.
* IIBA, official CBAP certification resources.
* Project Management Institute, *A Guide to the Project Management Body of Knowledge (PMBOK® Guide)*.
* ISO 31000, Risk Management — Guidelines.
* ISO 27001, Information Security Management Systems.

## 16. Module Summary

Business Analysis Planning and Monitoring establishes how analysis work is approached, coordinated, governed, measured, and improved. Strong planning aligns the approach with context, clarifies stakeholder responsibilities, protects business information, anticipates uncertainty, and uses meaningful performance measures. Effective monitoring enables the analyst to adapt plans when evidence or circumstances change.
