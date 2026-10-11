# Requirements Life Cycle Management

## 1. Learning Objectives

By the end of this module, you should be able to:

* Explain requirements life cycle management.
* Trace requirements from their origin through implementation and evaluation.
* Maintain requirements and design relationships.
* Prioritize requirements and support approval decisions.
* Assess and manage requirement changes.
* Conduct impact analysis.
* Explain requirements status, versioning, and configuration management.
* Understand how requirements are maintained and reused.
* Apply life cycle management in a realistic project.

## 2. Introduction

Requirements Life Cycle Management ensures that requirements and designs remain useful, consistent, and aligned with business needs throughout their life cycle.

Requirements are not simply written once and handed to developers. They may change because of:

* New business priorities.
* Stakeholder feedback.
* Regulatory changes.
* Technical discoveries.
* Budget constraints.
* Market developments.
* Defects or misunderstandings.
* Changes in solution architecture.

Life cycle management provides a controlled way to handle these changes while maintaining traceability and business alignment.

## 3. Requirements Life Cycle

A simplified life cycle includes:

1. Identify a business or stakeholder need.
2. Elicit and analyze requirements.
3. Specify and model requirements.
4. Verify and validate requirements.
5. Prioritize and obtain appropriate decisions.
6. Maintain relationships and traceability.
7. Implement and test the solution.
8. Evaluate outcomes and manage further change.

This is a conceptual sequence, not necessarily a rigid waterfall process. Agile teams may repeat these activities continuously within iterations.

### Example

A retailer initially requires online order tracking.

During development, stakeholders discover that customers also need delivery notifications.

The analyst assesses the new need, identifies affected requirements and designs, estimates impact, supports prioritization, and ensures that the agreed change is communicated to the delivery team.

Without life cycle management, the additional feature might be implemented inconsistently or without considering cost, privacy, and release timing.

## 4. Requirements Traceability

Traceability maintains relationships among requirements, their sources, and related work products.

### Forward Traceability

Forward traceability follows a requirement toward its implementation and verification.

Example:

Business objective → Requirement → Design → Development task → Test case → Outcome measure.

It helps answer:

"How will this business need be implemented and tested?"

### Backward Traceability

Backward traceability follows an implemented feature or requirement back to its justification.

It helps answer:

"Why are we implementing this feature?"

Backward traceability can reveal unnecessary functionality, missing justification, and scope expansion.

### Bidirectional Traceability

Bidirectional traceability supports movement in both directions.

It helps identify:

* Requirements without tests.
* Tests without legitimate requirements.
* Features without business justification.
* Objectives without supporting requirements.
* Requirements affected by a change.

### Example Traceability Matrix

| Requirement ID | Business objective         | Design component       | Test case | Status       |
| -------------- | -------------------------- | ---------------------- | --------- | ------------ |
| REQ-001        | Reduce order inquiries     | Order-status page      | TC-001    | Approved     |
| REQ-002        | Improve service efficiency | Agent search           | TC-002    | In progress  |
| REQ-003        | Improve auditability       | Audit log              | TC-003    | Approved     |
| REQ-004        | Protect customer data      | Access-control service | TC-004    | Under review |

A traceability matrix is one possible technique. Other tools include requirements-management systems, backlog links, model relationships, and automated test-management integrations.

## 5. Maintaining Requirements

Requirements maintenance keeps requirements accurate, accessible, consistent, and relevant as the solution and business environment evolve.

Maintenance activities may include:

* Updating requirement wording.
* Recording decisions.
* Revising priorities.
* Updating dependencies.
* Correcting outdated assumptions.
* Updating traceability links.
* Recording approval and status.
* Communicating changes to affected stakeholders.
* Archiving obsolete versions where appropriate.

Maintenance is particularly important when a project spans multiple releases or when regulations and operational procedures change frequently.

### Example

A business requirement states that customers can cancel an order before shipment.

A new operational policy introduces a cutoff after warehouse picking begins.

The requirement and associated business rules must be updated, and the analyst should assess impacts on customer interfaces, order processing, refunds, and testing.

## 6. Requirement Attributes and Status

Requirement attributes help teams manage requirements consistently.

Typical attributes include:

* Unique identifier.
* Name.
* Description.
* Source.
* Owner.
* Type.
* Priority.
* Status.
* Version.
* Rationale.
* Dependencies.
* Risks.
* Acceptance criteria.
* Related designs.
* Related tests.

Possible status values include:

* Proposed.
* Under analysis.
* Reviewed.
* Approved.
* In progress.
* Implemented.
* Verified.
* Rejected.
* Deferred.
* Retired.

Status values should be defined by the organization or project. A team should not assume that every requirement follows an identical status sequence.

A unique identifier helps preserve relationships when a requirement's name or wording changes.

## 7. Approval and Authorization

Requirements approval establishes an authorized decision that a requirement or set of requirements may proceed under the applicable governance process.

Approval can occur through:

* Formal sign-off.
* A product owner decision.
* A governance board.
* A documented stakeholder review.
* An agreed backlog-prioritization process.

The appropriate method depends on organizational governance, project risk, and delivery approach.

Approval does not mean that a requirement can never change. It means that changes should follow the agreed decision process.

### Example

A regulated financial institution may require formal approval for changes affecting financial calculations or customer-data handling.

A small internal software team may use product-owner approval and version-controlled backlog updates.

Both approaches can be appropriate in their respective contexts.

## 8. Prioritization Across the Life Cycle

Priorities can change as new information becomes available.

A requirement may become more important because:

* A regulation changes.
* A key dependency is completed.
* A major customer need is identified.
* A security risk becomes more significant.
* A budget reduction forces scope changes.
* A planned benefit becomes less valuable.

Prioritization should consider both business value and delivery constraints.

### Common Methods

**MoSCoW:** Must, Should, Could, Won't have this time.

**Value versus effort:** Compare expected benefit with implementation effort.

**Risk-based prioritization:** Address high-risk requirements early where doing so reduces uncertainty or exposure.

**Dependency-based sequencing:** Implement prerequisites before dependent features.

**Weighted scoring:** Compare requirements using agreed criteria.

No prioritization technique removes the need for stakeholder judgment and transparent decision-making.

## 9. Change Requests

A change request proposes an addition, modification, or removal affecting requirements, designs, scope, or related work products.

Examples:

* Add a new report.
* Change an approval threshold.
* Modify a security requirement.
* Remove an obsolete feature.
* Introduce a new integration.
* Change a regulatory retention period.

A change request should be documented sufficiently for the relevant people to understand what is changing and why.

Typical information includes:

* Change ID.
* Requester.
* Date.
* Description.
* Business rationale.
* Affected requirements.
* Expected benefits.
* Cost and schedule implications.
* Risks.
* Dependencies.
* Decision.
* Decision rationale.
* Implementation status.

## 10. Change Impact Analysis

Impact analysis determines the likely consequences of a proposed change.

It may examine:

**Business impact:** Does the change support or undermine business objectives?

**Requirement impact:** Which existing requirements need modification?

**Design impact:** Which solution components are affected?

**Data impact:** Are data structures, mappings, retention, or migration processes affected?

**Integration impact:** Will connected systems or external interfaces change?

**Testing impact:** Which test cases must be created or repeated?

**Schedule impact:** Will delivery dates or sequencing change?

**Cost impact:** What additional resources are required?

**Risk impact:** Does the change create or reduce exposure?

**Stakeholder impact:** Who needs to be consulted or trained?

### Example

A customer portal must support a new phone number field.

The apparent change is small, but the analyst should consider:

* Data validation.
* Database changes.
* Privacy rules.
* Existing APIs.
* Import and export formats.
* User-interface behavior.
* Regression testing.
* Existing customer records.
* Consent and communication policies.

Impact analysis prevents teams from treating apparently minor changes as isolated tasks.

## 11. Change Control Process

A general change-control process can be represented as:

1. **Submit:** Record the requested change.
2. **Clarify:** Understand the need and desired outcome.
3. **Analyze:** Identify impacts, costs, risks, and dependencies.
4. **Evaluate:** Compare the change with priorities and constraints.
5. **Decide:** Approve, reject, defer, or request further analysis.
6. **Update:** Revise affected requirements, designs, and plans.
7. **Communicate:** Inform affected stakeholders.
8. **Implement:** Deliver the authorized change.
9. **Verify:** Confirm that the change meets the agreed criteria.
10. **Close:** Record the outcome and update relevant records.

Not every change requires the same degree of formality. The process should be proportional to risk, complexity, and governance requirements.

## 12. Scope Creep

Scope creep occurs when project scope expands without appropriate evaluation and authorization.

Common causes include:

* Informal promises.
* Uncontrolled stakeholder requests.
* Unclear scope boundaries.
* Poor change-impact analysis.
* Weak prioritization.
* Missing acceptance criteria.
* Unrecorded decisions.

Scope creep does not mean that every new requirement is bad. Valuable changes should be considered, but their implications must be understood.

### Prevention Techniques

* Define scope and objectives clearly.
* Maintain a visible backlog or requirements register.
* Record change requests.
* Analyze impact before committing.
* Establish decision authority.
* Communicate approved changes.
* Reassess schedule and budget when scope changes.
* Preserve traceability.

## 13. Versioning and Configuration Management

Versioning records changes to requirements and associated artifacts over time.

Configuration management identifies and controls the versions of work products that form an agreed baseline or configuration.

These practices support reproducibility, coordination, and impact analysis.

### Example

A requirement evolves through three versions:

* v1.0: Users can search orders by order ID.
* v1.1: Users can also search by customer reference.
* v2.0: Search permissions are revised to reflect new access-control rules.

A record of the changes should identify what changed, why it changed, who authorized the change, and which related components require updates.

A baseline is an agreed reference point. It is not necessarily immutable; it is changed through the applicable control process.

## 14. Requirements Reuse

Requirements reuse allows suitable requirements to be applied across projects or solution components.

Examples:

* Standard authentication requirements.
* Accessibility requirements.
* Audit logging requirements.
* Common financial validation rules.
* Standard error-handling behavior.

Reuse can reduce duplication and improve consistency.

However, reused requirements must be checked for:

* Applicability.
* Current regulatory relevance.
* Context.
* Dependencies.
* Stakeholder expectations.
* Technology constraints.
* Version compatibility.

Copying a requirement without checking its assumptions can create incorrect or unnecessary obligations.

## 15. Agile Requirements Life Cycle Management

Agile delivery commonly manages requirements through a backlog.

A product backlog may contain:

* Epics.
* Features.
* User stories.
* Defects.
* Technical work.
* Research tasks.

Items are refined, prioritized, estimated, selected for delivery, implemented, tested, and reviewed.

### Product Backlog Example

| Item                    | Business value | Priority | Status      |
| ----------------------- | -------------- | -------- | ----------- |
| Customer order tracking | High           | 1        | Done        |
| Agent order search      | High           | 2        | In progress |
| Custom dashboard theme  | Low            | 5        | Backlog     |
| Delivery notifications  | Medium         | 3        | Refined     |

Backlog management does not eliminate requirements analysis. It changes how requirements are organized, refined, prioritized, and delivered.

An Agile team should still maintain adequate clarity, traceability, acceptance criteria, and stakeholder alignment for its context.

## 16. Metrics for Requirements Management

Metrics can help assess requirements quality and management effectiveness.

Examples include:

* Number of unresolved requirement questions.
* Number of changes after approval.
* Percentage of requirements with acceptance criteria.
* Percentage of requirements linked to tests.
* Number of requirements without clear business justification.
* Change-request turnaround time.
* Requirement-related defects.
* Number of conflicting requirements.
* Percentage of completed requirements accepted by stakeholders.

Metrics should be interpreted carefully.

A high change count does not automatically indicate poor performance. It may reflect learning, changing business conditions, or improved stakeholder engagement.

The objective is to understand patterns and improve outcomes, not merely to minimize numbers.

## 17. Case Study: Banking Application Enhancement

### Background

A bank is upgrading its mobile banking application. The approved scope includes balance checking, transaction history, and secure authentication.

During development, stakeholders request biometric authentication, downloadable statements, and additional transaction filters.

### Existing Objectives

* Improve customer experience.
* Maintain appropriate security.
* Deliver the planned release within budget.
* Meet applicable regulatory obligations.

### Change Requests

**CR-001: Biometric authentication**

Potential impacts:

* Supported devices.
* Authentication design.
* Security assessment.
* Recovery procedures.
* Testing across devices.

**CR-002: Downloadable statements**

Potential impacts:

* File formats.
* Customer privacy.
* Data access controls.
* Storage and generation costs.
* Accessibility.
* Testing.

**CR-003: Additional transaction filters**

Potential impacts:

* Search behavior.
* Query performance.
* User interface.
* Test cases.
* Delivery effort.

### Recommended Management Approach

1. Record each request separately.
2. Clarify the business need behind each request.
3. Trace each request to relevant objectives.
4. Identify affected requirements and designs.
5. Estimate cost, risk, dependencies, and schedule impact.
6. Compare the changes with the release priorities.
7. Obtain the appropriate decision.
8. Update the backlog and relevant artifacts.
9. Communicate the decision.
10. Verify the approved implementation.

### Possible Decision

The bank may include biometric authentication in the current release if security and device support are ready, defer downloadable statements to a later release, and include basic transaction filters if the effort is low.

This is only an illustrative decision. The actual decision depends on business value, risk, feasibility, and governance.

### Lessons

* Changes should be evaluated rather than automatically accepted or rejected.
* Traceability reveals which objectives and artifacts are affected.
* Approval and versioning help teams work from consistent information.
* Scope changes require transparent trade-off decisions.
* Requirements management continues after implementation.

## 18. Knowledge Check

### Questions

**1. What is the main purpose of requirements life cycle management?**

A. Prevent every change.
B. Maintain requirements and their relationships throughout the life cycle.
C. Replace solution testing.
D. Eliminate stakeholder involvement.

**2. What does forward traceability help establish?**

A. How a business need connects to implementation and verification.
B. Whether the project has a large budget.
C. Whether stakeholders have identical preferences.
D. Whether a system uses cloud hosting.

**3. What is scope creep?**

A. A planned, approved reduction in scope.
B. Uncontrolled scope expansion without appropriate evaluation and authorization.
C. A test failure.
D. A formal requirements review.

**4. What should happen before a significant change is authorized?**

A. Implement it immediately.
B. Assess its rationale, impacts, risks, and implications.
C. Remove all existing requirements.
D. Stop all stakeholder communication.

**5. What is a baseline?**

A. An agreed reference point for controlled work products.
B. A guarantee that requirements never change.
C. A list of unresolved defects only.
D. A project budget.

**6. Which is a benefit of traceability?**

A. It makes testing unnecessary.
B. It supports impact analysis and identification of missing relationships.
C. It eliminates all project risks.
D. It prevents stakeholder disagreement.

**7. What is a suitable response to an additional stakeholder request?**

A. Always reject it.
B. Always accept it.
C. Clarify, analyze, prioritize, and decide using the applicable process.
D. Implement it without documenting the decision.

**8. Which statement about Agile requirements management is correct?**

A. Agile teams do not analyze requirements.
B. Backlog prioritization and refinement help manage requirements iteratively.
C. Traceability is always prohibited.
D. Acceptance criteria are unnecessary.

### Answer Key

1. B — Requirements and designs must remain aligned and manageable over time.
2. A — Forward traceability connects needs to implementation and verification.
3. B — Scope creep is uncontrolled expansion, not all change.
4. B — Impact analysis enables informed decisions.
5. A — A baseline provides an agreed reference point subject to change control.
6. B — Traceability supports impact analysis, coverage, and justification.
7. C — A structured evaluation helps balance value, risk, cost, and constraints.
8. B — Agile teams manage requirements through iterative refinement and delivery.

## 19. Revision Summary

* Requirements life cycle management continues from initial identification through implementation and later change.
* Forward traceability connects needs to implementation and tests.
* Backward traceability connects artifacts to their justification.
* Maintenance keeps requirements accurate and relevant.
* Requirement attributes support identification, prioritization, ownership, and status tracking.
* Approval establishes an authorized decision under the applicable governance process.
* Priorities can change as business conditions evolve.
* Change impact analysis considers requirements, designs, cost, schedule, data, testing, risk, and stakeholders.
* Scope creep is uncontrolled expansion without appropriate evaluation and authorization.
* Versioning and configuration management help preserve consistency and decision history.
* Reuse can improve consistency but requires contextual review.
* Agile backlog management supports iterative requirements refinement and prioritization.

## 20. Further Study

Review the IIBA BABOK Guide section on Requirements Life Cycle Management, including:

* Trace Requirements.
* Maintain Requirements.
* Prioritize Requirements.
* Assess Requirements Changes.
* Approve Requirements.

Practice by creating a change-request register, a traceability matrix, and an impact analysis for a hypothetical system enhancement.
