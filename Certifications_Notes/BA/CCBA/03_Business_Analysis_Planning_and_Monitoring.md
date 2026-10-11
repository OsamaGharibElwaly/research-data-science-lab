# 03 — Business Analysis Planning and Monitoring

## 1. Purpose

Business Analysis Planning and Monitoring determines how business analysis work will be approached, governed, coordinated, and assessed.

The analyst establishes suitable methods for:

* Planning business analysis activities.
* Engaging stakeholders.
* Managing business analysis governance.
* Coordinating information and requirements.
* Monitoring analysis performance.
* Improving the analysis process.

Planning is not a one-time exercise. Plans may change as risks, stakeholder needs, and business conditions evolve.

## 2. Planning the Business Analysis Approach

The business analysis approach describes the general method used to perform analysis.

The approach should fit the change, organizational environment, risk, complexity, stakeholder availability, and delivery method.

### Predictive approach

Often used when:

* Requirements are relatively stable.
* Regulatory or contractual documentation is extensive.
* Formal approvals are necessary.
* Change is expensive or difficult.

Planning and requirements definition often occur early, with controlled changes later.

### Adaptive approach

Often used when:

* Requirements evolve through learning.
* Stakeholders can provide frequent feedback.
* Incremental delivery is practical.
* Uncertainty is high.

Analysis and delivery may proceed iteratively, with priorities refined over time.

### Hybrid approach

Combines predictive and adaptive practices.

Example: A regulated organization uses formal governance and security approval but delivers user-facing functionality in short iterations.

### Selecting an approach

Consider:

* Business complexity.
* Scope uncertainty.
* Regulatory requirements.
* Stakeholder availability.
* Organizational culture.
* Delivery team capabilities.
* Technology constraints.
* Risk tolerance.
* Expected frequency of change.

No approach is universally best.

## 3. Business Analysis Plan Components

A business analysis plan may include:

1. Scope of business analysis work.
2. Activities and deliverables.
3. Roles and responsibilities.
4. Stakeholder engagement strategy.
5. Elicitation techniques.
6. Requirements management approach.
7. Modeling and documentation standards.
8. Communication methods.
9. Governance and approval procedures.
10. Tools and repositories.
11. Performance measures.
12. Risks, assumptions, and dependencies.
13. Schedule and resource estimates.
14. Change control arrangements.

The level of detail should be proportionate to the complexity and risk of the work.

## 4. Planning Stakeholder Engagement

Stakeholder engagement planning identifies stakeholders and determines how to work effectively with them.

### Stakeholder identification

Potential stakeholders include:

* Sponsor.
* Business owner.
* End users.
* Customers.
* Subject matter experts.
* Operations personnel.
* Developers and architects.
* Testers.
* Security and compliance teams.
* Vendors.
* Regulators.

Stakeholders may be affected directly or indirectly by a change.

### Stakeholder analysis

Consider:

* Authority and decision-making power.
* Influence over outcomes.
* Interest in the change.
* Impact of the change.
* Knowledge and expertise.
* Attitude toward the change.
* Availability and communication needs.

A stakeholder map should not be treated as static. Influence, interest, and support can change over time.

### Engagement strategy

Examples:

* Executive sponsor: concise decision-oriented reports.
* End users: workshops, interviews, and usability sessions.
* Compliance team: structured reviews and documented evidence.
* Technical team: architecture discussions and interface specifications.
* Customers: surveys, interviews, and feedback analysis.

The analyst selects techniques that help each stakeholder contribute effectively.

## 5. Roles and Responsibilities

Clearly defined responsibilities reduce duplication and unresolved decisions.

Example responsibility matrix:

| Activity                     | Sponsor        | Business Analyst | Product Owner | Technical Lead |
| ---------------------------- | -------------- | ---------------- | ------------- | -------------- |
| Confirm business objectives  | Accountable    | Supports         | Consulted     | Consulted      |
| Elicit requirements          | Consulted      | Leads            | Participates  | Participates   |
| Prioritize product backlog   | Consulted      | Supports         | Leads         | Consulted      |
| Assess technical feasibility | Consulted      | Supports         | Consulted     | Leads          |
| Approve funding              | Leads/approves | Advises          | Consulted     | Consulted      |

This is illustrative, not a universal allocation of responsibilities.

A RACI matrix may classify participants as:

* **Responsible:** Performs the work.
* **Accountable:** Owns the final result or decision.
* **Consulted:** Provides input.
* **Informed:** Receives updates.

Each activity should have clear accountability, subject to organizational governance.

## 6. Planning Business Analysis Governance

Governance defines how decisions are made, reviewed, approved, and escalated.

It may cover:

* Requirement approval.
* Scope decisions.
* Change requests.
* Prioritization authority.
* Risk escalation.
* Documentation standards.
* Decision records.
* Compliance reviews.
* Conflict resolution.

### Example

A banking application has requirements affecting customer data privacy.

The governance plan may require:

1. Business review.
2. Privacy assessment.
3. Security review.
4. Technical feasibility assessment.
5. Authorized approval.
6. Traceable documentation.

The analyst identifies the required process and supports it, but does not automatically replace the designated decision-makers.

## 7. Planning Business Analysis Information Management

Business analysis information includes:

* Requirements.
* Designs.
* Business rules.
* Models.
* Decisions.
* Assumptions.
* Risks.
* Stakeholder feedback.
* Traceability relationships.
* Approval records.

An information management approach establishes how this information is created, stored, accessed, updated, shared, and retained.

### Important considerations

**Repository:** Where information is stored.

**Version control:** How changes to information are tracked.

**Access control:** Who may view or modify information.

**Traceability:** How related information is connected.

**Retention:** How long information must be retained.

**Confidentiality:** How sensitive information is protected.

**Naming conventions:** How information is identified consistently.

For example, a requirements repository may store each requirement with an ID, description, source, priority, status, owner, acceptance criteria, and related test cases.

## 8. Requirements Management and Communication Planning

The analyst establishes how requirements and related information will be communicated and maintained.

A communication plan should consider:

* Audience.
* Purpose.
* Content.
* Frequency.
* Format.
* Delivery channel.
* Owner.
* Feedback method.
* Required confidentiality.

### Example

| Audience          | Information                          | Method                | Frequency            |
| ----------------- | ------------------------------------ | --------------------- | -------------------- |
| Executive sponsor | Key decisions, risks, progress       | Summary report        | Weekly               |
| Business users    | Requirements and process changes     | Workshop              | Biweekly             |
| Technical team    | Detailed requirements and interfaces | Repository and review | Each iteration       |
| Compliance        | Controls and evidence                | Formal review         | At agreed milestones |

Communication should be two-way. Sending information does not prove that it was understood.

## 9. Planning Business Analysis Performance Improvements

The analyst identifies how to assess the effectiveness of business analysis work.

Possible performance measures:

* Requirements review turnaround time.
* Number of unresolved requirement defects.
* Percentage of requirements with traceability.
* Stakeholder review participation.
* Rework caused by unclear requirements.
* Frequency of requirement changes.
* Time taken to resolve analysis issues.
* Stakeholder satisfaction with analysis deliverables.

Metrics require context. A high change rate, for example, may indicate poor analysis, but it may also reflect legitimate learning in an adaptive environment.

Avoid optimizing one metric at the expense of business outcomes.

## 10. Monitoring Business Analysis Work

Monitoring compares actual analysis performance with the plan.

The analyst may track:

* Planned vs. completed activities.
* Deliverable quality.
* Stakeholder availability.
* Open issues.
* Requirement approval status.
* Risks and dependencies.
* Resource utilization.
* Change requests.
* Analysis performance measures.

When a deviation occurs, determine its cause and assess the effect on scope, schedule, quality, and value.

### Example

Planned: Requirements for three business units will be reviewed by Friday.

Actual: One unit has not provided feedback.

Possible response:

1. Identify the missing stakeholder input.
2. Assess its impact on dependent requirements.
3. Contact the responsible stakeholder.
4. Re-plan affected work.
5. Escalate if a decision deadline is threatened.
6. Update the plan and communicate changes.

Monitoring should result in informed corrective action, not just status reporting.

## 11. Planning Techniques

### Document analysis

Review existing policies, procedures, reports, contracts, and system documentation to understand the current state.

### Interviews

Gather detailed information from individuals or small groups.

### Workshops

Facilitate collaborative discussions to discover needs, resolve conflicts, or reach agreement.

### Surveys

Collect information from many participants using standardized questions.

### Process modeling

Represent workflows, decisions, handoffs, and exceptions.

### Estimation

Estimate analysis effort, duration, and resource needs using suitable techniques.

### Risk analysis

Identify uncertainty and determine how it could affect analysis activities or outcomes.

### Lessons learned

Use previous project experience to improve the current approach.

Technique selection should reflect the question being answered, the people involved, and the information available.

## 12. Practical Case Study: Digital Banking Upgrade

A bank plans to upgrade its online banking platform.

Stakeholders include customers, operations, compliance, security, IT, product management, and external payment providers.

### Planning approach

**Approach:** Hybrid. Formal compliance approvals are combined with iterative interface development.

**Scope:** Online transfers, transaction history, authentication, and customer notifications.

**Governance:** Security and compliance reviews are required before production release.

**Stakeholder engagement:** Customer interviews, operations workshops, technical reviews, and formal approval sessions.

**Information management:** Central repository with unique requirement IDs, version history, traceability, and controlled access.

**Communication:** Weekly progress updates, iteration demonstrations, and milestone approvals.

**Performance measures:**

* Percentage of requirements reviewed.
* Number of unresolved high-risk issues.
* Requirements linked to test cases.
* Stakeholder approval turnaround time.
* Rework due to ambiguous requirements.

### Monitoring example

The security review identifies a missing authentication requirement.

The analyst should:

1. Record the issue.
2. Assess affected requirements and designs.
3. Identify impacted tests and release activities.
4. Consult the relevant security and business stakeholders.
5. Update the plan if necessary.
6. Ensure the decision and requirement changes are traceable.

## 13. Knowledge Check

**Question 1:** What is the primary purpose of business analysis planning?

A. Guarantee that no changes occur
B. Determine how business analysis work will be performed and controlled
C. Replace stakeholder engagement
D. Eliminate all project risks

**Question 2:** Which approach is often suitable when requirements are uncertain and feedback is frequent?

A. Adaptive
B. Strictly predictive in every circumstance
C. No planning approach
D. Documentation-free delivery

**Question 3:** Which governance element clarifies who can approve requirement changes?

A. A naming convention
B. A decision and approval process
C. A survey
D. A process flowchart alone

**Question 4:** What should an analyst do when planned stakeholder input is delayed?

A. Ignore the delay
B. Automatically cancel the project
C. Assess impact, engage stakeholders, and adjust the plan as needed
D. Approve the missing requirements without review

**Question 5:** Which metric most directly measures traceability coverage?

A. Number of meetings held
B. Percentage of requirements linked to their relevant sources or related elements
C. Total number of employees
D. Total project budget

**Question 6:** What does RACI stand for?

A. Review, Analyze, Control, Implement
B. Responsible, Accountable, Consulted, Informed
C. Requirements, Assumptions, Constraints, Issues
D. Risk, Analysis, Communication, Integration

### Answers and Explanations

1. **B — Determine how work will be performed and controlled.** Planning establishes the approach, activities, roles, and governance.
2. **A — Adaptive.** Adaptive approaches support learning and iterative refinement.
3. **B — A decision and approval process.** Governance defines decision authority and escalation.
4. **C — Assess impact and adjust the plan.** The response should reflect the consequences and urgency.
5. **B — Percentage of requirements linked to relevant elements.** The exact denominator and expected links should be defined.
6. **B — Responsible, Accountable, Consulted, Informed.** RACI clarifies participation and accountability.

## 14. Revision Summary

* The analysis approach should fit uncertainty, complexity, risk, governance, and stakeholder needs.
* Business analysis planning covers activities, deliverables, roles, communication, governance, and information management.
* Stakeholder engagement should be tailored to influence, interest, impact, and availability.
* Governance clarifies decision-making and approval.
* Information management supports security, versioning, access, and traceability.
* Monitoring compares actual work with the plan and enables corrective action.
* Performance metrics must be interpreted in context.

## 15. Further Study

Review the BABOK Guide's Business Analysis Planning and Monitoring knowledge area, including planning the approach, stakeholder engagement, governance, information management, and performance improvement. Verify the current CCBA exam blueprint before finalizing revision priorities.
