# 05 — Requirements Life Cycle Management

## 1. Introduction

Requirements Life Cycle Management describes the tasks involved in managing and maintaining requirements and designs from their initial development through their subsequent changes and eventual retirement.

The purpose is to ensure that requirements and designs remain aligned with business needs, that changes are controlled appropriately, and that relationships among requirements and other business analysis information are maintained.

The BABOK Guide identifies five tasks in this knowledge area:

1. Trace Requirements.
2. Maintain Requirements.
3. Prioritize Requirements.
4. Assess Requirements Changes.
5. Approve Requirements.

Requirements management continues throughout the change lifecycle. It is not limited to the period before development begins.

## 2. Trace Requirements

Traceability establishes and maintains relationships between requirements, designs, business objectives, stakeholders, solution components, and other relevant information.

### 2.1 Why Traceability Matters

Traceability supports:

* Understanding why a requirement exists.
* Identifying the source of a requirement.
* Assessing the impact of a proposed change.
* Checking test coverage.
* Identifying requirements that are no longer needed.
* Demonstrating compliance.
* Identifying missing or unsupported requirements.
* Connecting delivered capabilities to business outcomes.

### 2.2 Types of Traceability

**Backward traceability:** Traces a requirement to its source, such as a stakeholder need, business objective, regulation, or business rule.

**Forward traceability:** Traces a requirement to downstream elements, such as solution components, implementation tasks, or test cases.

**Horizontal traceability:** Establishes relationships among requirements or elements at comparable levels, including dependencies and interactions.

Terminology may vary across organizations, so the traceability approach should define the relationships being maintained.

### 2.3 Example

Business objective: Reduce order-processing costs by 15%.

Business requirement: Automate repetitive order-processing activities.

Stakeholder requirement: Customer service employees need to identify incomplete orders quickly.

Solution requirement: The system shall flag orders with missing mandatory information.

Design: An order-validation component.

Test case: Submit an order without a required delivery address and verify that the system identifies the missing information.

Outcome measure: Reduction in manual correction time per order.

Traceability allows the analyst to determine whether the requirement contributes to the business objective and whether it is covered by testing.

### 2.4 Traceability Records

A traceability record may include:

| Field                   | Purpose                             |
| ----------------------- | ----------------------------------- |
| Requirement ID          | Unique identification               |
| Requirement description | Statement of the need               |
| Source                  | Origin of the requirement           |
| Parent requirement      | Higher-level justification          |
| Related requirements    | Dependencies and relationships      |
| Design reference        | Related solution design             |
| Test reference          | Verification or validation evidence |
| Status                  | Current lifecycle state             |
| Owner                   | Responsible person or role          |

Not every project needs every field. The information should support actual management needs.

## 3. Maintain Requirements

Requirements maintenance ensures that requirements and designs remain accurate, usable, consistent, and relevant over time.

Maintenance may involve:

* Updating requirement descriptions.
* Correcting errors.
* Maintaining status and ownership.
* Preserving traceability.
* Managing versions.
* Updating models.
* Recording approved changes.
* Retiring obsolete information.
* Ensuring that stakeholders can access the correct version.

### 3.1 Requirements Repositories

A repository may be a requirements management platform, an issue tracker, a document management system, or a controlled collection of files.

A good repository supports:

* Unique identification.
* Version history.
* Access control.
* Search and retrieval.
* Status tracking.
* Relationships among information.
* Change history.
* Review and approval records.

### 3.2 Version Control

Version control records changes to requirements or designs.

Example:

* Version 1.0: Customers can cancel orders before dispatch.
* Version 1.1: Cancellation is allowed until warehouse processing begins.
* Version 1.2: Cancellation is blocked after a shipping label is generated.

Each change should have an explanation, author, date, and appropriate review or approval status.

### 3.3 Requirement Status

Common lifecycle statuses include:

* Draft.
* Under review.
* Approved.
* In development.
* Implemented.
* Verified.
* Validated.
* Deferred.
* Rejected.
* Retired.

Organizations may use different status models. A status must have a clear definition so stakeholders understand what it means.

## 4. Prioritize Requirements

Prioritization establishes the relative importance of requirements and designs.

Priorities help determine:

* What must be delivered first.
* Which requirements create the most value.
* What can be deferred.
* Which requirements reduce significant risks.
* How limited resources should be allocated.

### 4.1 Prioritization Factors

Consider:

* Business value.
* Strategic alignment.
* Regulatory obligations.
* Urgency.
* Risk reduction.
* Implementation cost.
* Technical feasibility.
* Dependencies.
* Stakeholder expectations.
* Operational impact.
* Time sensitivity.

A requirement's priority is contextual and may change when business conditions change.

### 4.2 MoSCoW Prioritization

**Must have:** Essential to the agreed scope or business outcome.

**Should have:** Important, but the solution can still meet its core objectives without it temporarily.

**Could have:** Desirable if resources and time permit.

**Won't have this time:** Explicitly excluded from the current delivery.

Example for an online store:

| Requirement                  | Example Priority     |
| ---------------------------- | -------------------- |
| Secure payment processing    | Must                 |
| Correct order totals         | Must                 |
| Shipment tracking            | Should               |
| Personalized recommendations | Could                |
| Animated page transitions    | Won't have this time |

The categories must be agreed within the relevant delivery context.

### 4.3 Ranking and Relative Prioritization

Requirements may be ranked from highest to lowest priority.

However, ranking becomes difficult when many requirements have similar importance. Grouping, weighted scoring, or pairwise comparison can help.

### 4.4 Weighted Scoring

Suppose a business evaluates requirements using value, risk reduction, and urgency.

Each factor is scored from 1 to 5.

| Requirement               | Value | Risk Reduction | Urgency |
| ------------------------- | ----: | -------------: | ------: |
| A: Fix payment failures   |     5 |              5 |       5 |
| B: Improve search filters |     4 |              2 |       3 |
| C: Add dark mode          |     2 |              1 |       1 |

If the weights are 50% for value, 30% for risk reduction, and 20% for urgency:

$$
Score = 0.5V + 0.3R + 0.2U
$$

Requirement A:

$$
0.5(5)+0.3(5)+0.2(5)=5.0
$$

Requirement B:

$$
0.5(4)+0.3(2)+0.2(3)=3.2
$$

Requirement C:

$$
0.5(2)+0.3(1)+0.2(1)=1.5
$$

Requirement A receives the highest score.

Weighted scoring supports decision-making but does not replace professional judgment. Mandatory legal or safety requirements cannot automatically be deprioritized because of a low numerical score.

## 5. Assess Requirements Changes

Requirements change because stakeholders learn more, regulations evolve, risks emerge, technology changes, or business priorities shift.

A change assessment determines the implications of a proposed change before an appropriate decision is made.

### 5.1 Change Assessment Process

1. Receive and record the change request.
2. Clarify the problem or opportunity.
3. Identify the affected requirements and designs.
4. Review traceability and dependencies.
5. Assess business value and risks.
6. Estimate effort, cost, and schedule impact.
7. Identify effects on stakeholders and operations.
8. Compare alternatives.
9. Provide a recommendation.
10. Submit the change to the appropriate decision-maker.
11. Record the decision and update relevant information.

### 5.2 Impact Analysis

Impact analysis investigates the consequences of changing an element.

Potential impacts include:

* Other requirements.
* Solution architecture.
* User interfaces.
* Data models.
* Security controls.
* Test cases.
* Training.
* Operational procedures.
* Costs.
* Delivery dates.
* Business benefits.
* Regulatory compliance.

A seemingly small requirement can have significant downstream consequences.

### 5.3 Example

A retailer requests that customers be allowed to cancel orders after dispatch.

The analyst identifies impacts on:

* Warehouse operations.
* Shipping providers.
* Refund rules.
* Inventory accounting.
* Customer notifications.
* Payment processing.
* Return policies.
* Fraud controls.

Possible alternatives include cancellation before dispatch, shipment interception where supported, and a post-delivery return process.

The analyst compares alternatives rather than treating the requested change as a simple interface modification.

## 6. Approve Requirements

Approval establishes that the authorized stakeholders accept requirements or designs for their intended purpose.

Approval may be formal or lightweight, depending on organizational governance.

### 6.1 Approval Considerations

Before approval, stakeholders may need to understand:

* The business need.
* Requirement quality.
* Priority.
* Feasibility.
* Risks.
* Dependencies.
* Scope implications.
* Acceptance criteria.
* Relevant assumptions.
* Outstanding issues.

### 6.2 Approval vs. Validation

Validation checks whether requirements or solutions address stakeholder needs and business objectives.

Approval is an authorization or acceptance decision made by the appropriate authority.

A requirement may be validated but still await formal approval. Conversely, approval does not guarantee that a requirement is correct or that the resulting solution will deliver value.

### 6.3 Approval Workflow Example

1. Analyst prepares the requirement.
2. Stakeholders review the requirement.
3. Technical specialists assess feasibility.
4. Compliance reviews applicable controls.
5. The designated authority approves or rejects it.
6. The analyst records the decision.
7. Approved requirements become part of the controlled baseline where applicable.

## 7. Requirements Baselines and Change Control

A requirements baseline is an agreed reference version of requirements used for subsequent work and change assessment.

Baselines are particularly useful in environments requiring formal scope control.

A baseline does not mean requirements can never change. It means changes are assessed and managed according to an agreed process.

In adaptive delivery, the baseline may be a product backlog or an agreed iteration scope rather than a fixed comprehensive requirements specification.

## 8. Practical Case Study: E-Commerce Checkout

An online retailer is developing a new checkout process.

Initial requirements:

* Customers can pay by card.
* Orders receive unique identifiers.
* Customers receive confirmation emails.
* The system calculates shipping costs.

A new regulation requires stronger customer authentication for certain transactions.

### Analysis

**Traceability:** Link the authentication requirement to the relevant regulatory source, affected payment requirements, design elements, and tests.

**Maintenance:** Update the requirement repository and version history.

**Prioritization:** Treat the applicable regulatory obligation as mandatory within the relevant scope.

**Change assessment:** Examine payment gateway compatibility, user experience, delivery schedule, security, and test coverage.

**Approval:** Obtain authorization from the appropriate business, security, and compliance authorities.

### Key lesson

Requirements life cycle management protects the relationship between business objectives and the changing requirements needed to achieve them.

## 9. Knowledge Check

**Question 1:** What is the main purpose of traceability?

A. To prevent every requirement change
B. To establish relationships among requirements and related elements
C. To replace stakeholder communication
D. To guarantee that the solution is profitable

**Question 2:** A requirement has no identifiable relationship to a business need. What should the analyst investigate?

A. Whether it is justified or an orphan requirement
B. Whether it should automatically become mandatory
C. Whether the project should be canceled
D. Whether all other requirements should be deleted

**Question 3:** Which activity assesses the consequences of a proposed requirement change?

A. Brainstorming only
B. Impact analysis
C. Requirements retirement only
D. Stakeholder identification only

**Question 4:** What is the primary purpose of a requirements baseline?

A. To make future changes impossible
B. To provide an agreed reference for managing scope and changes
C. To eliminate the need for testing
D. To replace business objectives

**Question 5:** Which statement about approval is correct?

A. Approval guarantees business value.
B. Approval and validation are identical.
C. Approval is an authorization decision, while validation evaluates alignment with needs.
D. Every stakeholder must approve every requirement.

**Question 6:** A requirement has high business value but depends on an unfinished integration. What should the analyst consider?

A. Business value alone
B. Dependencies, sequencing, risks, and business value
C. The requirement's description length
D. The number of meetings already held

### Answers and Explanations

1. **B.** Traceability connects requirements to sources, related requirements, designs, tests, and objectives.
2. **A.** An unsupported requirement may be unnecessary or may have an undocumented justification.
3. **B.** Impact analysis identifies the effects of a proposed change.
4. **B.** A baseline provides an agreed reference for assessing change.
5. **C.** Approval and validation serve different purposes.
6. **B.** Prioritization must account for dependencies as well as value.

## 10. Revision Summary

* Traceability establishes relationships between requirements and related business analysis information.
* Maintenance keeps requirements accurate, current, and accessible.
* Prioritization considers value, urgency, risk, cost, dependencies, and constraints.
* Impact analysis evaluates the consequences of proposed changes.
* Approval is an authorization decision.
* Validation evaluates alignment with business needs.
* A baseline provides a reference for change management.
* Requirements may evolve throughout the change lifecycle.

## 11. Further Study

Review the BABOK Guide's Requirements Life Cycle Management knowledge area, particularly traceability, maintenance, prioritization, change assessment, and approval. Practice identifying downstream impacts and distinguishing approval from validation.
