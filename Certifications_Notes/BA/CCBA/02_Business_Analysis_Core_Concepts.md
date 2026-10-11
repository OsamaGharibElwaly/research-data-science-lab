# 02 — Business Analysis Core Concepts

## 1. Introduction

This module develops the concepts that underpin business analysis and explains how they connect to requirements, designs, stakeholders, value, and business change.

For CCBA preparation, distinguish between:

* Business needs and stakeholder requests.
* Requirements and designs.
* Requirements at different levels.
* Requirements and solution performance.
* Validation and verification.
* Assumptions, constraints, risks, and dependencies.

## 2. Requirements and Designs

A **requirement** is a usable representation of a need. It may describe a capability, condition, or characteristic required to achieve an objective.

A **design** is a representation of a solution.

The distinction depends on perspective and context. A design created at one level may become a requirement for a lower-level solution.

Example:

* Business requirement: Reduce order processing time.
* Stakeholder requirement: Customer service agents need to retrieve order information quickly.
* Solution requirement: The application must display order status within two seconds under defined load conditions.
* Design: A proposed interface, database structure, API, and caching approach.

The first three statements express desired capabilities or conditions. The design describes one way of realizing the solution.

### Important principle

Requirements describe what is needed; designs describe how a solution may satisfy that need. In practice, requirements and designs evolve iteratively.

## 3. Requirement Classification

The BABOK Guide distinguishes four major requirement types.

### 3.1 Business Requirements

High-level statements describing organizational goals, objectives, or outcomes.

Examples:

* Increase online sales by 15% within twelve months.
* Reduce order fulfillment costs by 10%.
* Improve customer retention.

Business requirements establish why a change is needed.

### 3.2 Stakeholder Requirements

Statements describing the needs of a particular stakeholder or stakeholder group.

Examples:

* Sales representatives need a consolidated customer history.
* Warehouse supervisors need visibility into delayed shipments.
* Customers need to track orders without contacting support.

Stakeholder requirements connect business objectives to stakeholder expectations.

### 3.3 Solution Requirements

Requirements describing the capabilities and qualities of a solution.

They are divided into:

**Functional requirements:** Describe behavior or capabilities.

Examples:

* The system shall allow customers to reset passwords.
* The application shall calculate the total order price.
* The platform shall send shipment notifications.

**Non-functional requirements:** Describe quality attributes or conditions under which the solution must operate.

Examples:

* The application shall support 5,000 concurrent users.
* The service shall achieve 99.9% monthly availability.
* Sensitive information shall be encrypted in transit.
* Standard reports shall load within three seconds under specified conditions.

Non-functional requirements must be measurable whenever practical.

### 3.4 Transition Requirements

Temporary capabilities needed to move from the current state to the future state.

Examples:

* Migrate existing customer records.
* Train employees on the new platform.
* Convert legacy data.
* Run old and new systems in parallel.
* Establish a temporary reconciliation process.

Transition requirements may no longer be needed once the change is complete.

## 4. The Requirements Classification Structure

Consider a retail organization introducing an inventory management platform.

| Type                    | Example                                          | Main Question                 |
| ----------------------- | ------------------------------------------------ | ----------------------------- |
| Business                | Reduce stockout losses by 20%                    | Why is change needed?         |
| Stakeholder             | Warehouse managers need current stock visibility | Who needs what?               |
| Functional solution     | System records stock movements                   | What must the solution do?    |
| Non-functional solution | Inventory updates appear within two seconds      | How well must it operate?     |
| Transition              | Import current stock balances                    | What is needed during change? |

A single business need can generate many stakeholder, solution, and transition requirements.

## 5. Requirements Quality

High-quality requirements should be clear, useful, and capable of supporting implementation and evaluation.

Common quality characteristics include:

* **Atomic:** Expresses one primary requirement.
* **Complete:** Contains sufficient information for its intended use.
* **Consistent:** Does not conflict with other requirements.
* **Feasible:** Can reasonably be implemented within known constraints.
* **Unambiguous:** Has one intended interpretation.
* **Testable:** Can be evaluated against defined criteria.
* **Traceable:** Can be connected to its source and related requirements.
* **Prioritized:** Has an understood relative importance.
* **Understandable:** Can be interpreted by its intended audience.

### Weak vs. Strong Requirements

Weak: "The system should be fast."

Strong: "Under a load of 1,000 concurrent users, 95% of product-search requests shall complete within two seconds."

The stronger statement defines a measurable threshold and operating condition.

Weak: "The platform should be user-friendly."

Stronger: "At least 90% of representative first-time users shall complete the checkout task without assistance during usability testing."

The second statement provides a testable measure.

## 6. Requirements vs. Business Rules

A **business rule** is a policy, obligation, or constraint that guides or governs business behavior.

Examples:

* Orders above a specified amount require managerial approval.
* Customers may return eligible products within 14 days.
* Employees cannot approve their own expense claims.

A **requirement** specifies what a solution must provide to satisfy a need.

Example business rule: Orders above EGP 50,000 require managerial approval.

Possible solution requirement: The system shall route orders exceeding EGP 50,000 to an authorized manager for approval.

The business rule may exist independently of any software system. A solution requirement describes how a solution supports that rule.

## 7. Assumptions, Constraints, Risks, and Dependencies

### Assumptions

Statements accepted as true for planning or analysis purposes without complete confirmation.

Example: All branches have reliable internet access.

An incorrect assumption may cause rework or failure.

### Constraints

Restrictions that limit available choices.

Examples:

* The budget cannot exceed EGP 2 million.
* The solution must launch by a contractual deadline.
* The application must comply with applicable data protection rules.
* The organization must retain its existing ERP system.

### Risks

Uncertain events or conditions that may affect objectives.

Examples:

* A supplier may delay integration work.
* Data migration may reveal duplicate records.
* Adoption may be lower than expected.

Risk analysis considers likelihood, impact, and potential responses.

### Dependencies

Relationships in which an activity, requirement, component, or outcome relies on another.

Examples:

* Reporting depends on data migration.
* User acceptance testing depends on a stable test environment.
* A new checkout process depends on payment gateway integration.

Dependencies can exist between teams, requirements, systems, and external parties.

## 8. Traceability and Relationships

Traceability establishes relationships among requirements, designs, sources, components, tests, and business objectives.

Example:

Business objective: Reduce stockout losses.

↓ Business requirement: Improve inventory availability.

↓ Stakeholder requirement: Warehouse managers need accurate stock levels.

↓ Solution requirement: Record every confirmed stock movement.

↓ Design: Inventory event service and database structure.

↓ Test: Verify that a confirmed receipt increases available stock correctly.

↓ Outcome measure: Reduction in stockout frequency.

Traceability supports:

* Impact analysis.
* Change assessment.
* Coverage analysis.
* Verification.
* Validation.
* Compliance evidence.
* Identification of orphaned requirements.

**Orphan requirement:** A requirement with no clear relationship to a business need or other justified source.

## 9. Verification vs. Validation

These terms are related but different.

**Verification:** Determines whether a requirement or specification is defined appropriately according to its quality criteria.

Questions include:

* Is the requirement clear?
* Is it consistent with other requirements?
* Is it feasible?
* Is it testable?

**Validation:** Determines whether a requirement or solution supports the business need and provides stakeholder value.

Questions include:

* Does this requirement address the actual problem?
* Will the solution meet the stakeholder's need?
* Does the proposed capability support the desired outcome?

Example:

A requirement states that a report must calculate monthly revenue. Verification checks that the requirement is clear and testable. Validation checks whether that report helps management make the intended business decisions.

Do not confuse requirement verification with solution testing or business validation. The specific activity depends on what is being evaluated.

## 10. Prioritization

Prioritization helps determine which requirements should be addressed first, considering value, risk, urgency, cost, dependencies, and stakeholder needs.

### MoSCoW

* **Must have:** Essential for the defined scope or outcome.
* **Should have:** Important but not absolutely essential.
* **Could have:** Desirable if resources permit.
* **Won't have this time:** Explicitly excluded from the current delivery.

"W on't have this time" does not necessarily mean the requirement will never be implemented.

### Example

For an online store:

| Requirement                                          | Priority |
| ---------------------------------------------------- | -------- |
| Secure payment processing                            | Must     |
| Accurate order confirmation                          | Must     |
| Personalized recommendations                         | Could    |
| Animated product transitions                         | Could    |
| Multi-language support required by launch regulation | Must     |

Priorities depend on context. A feature considered optional for one business may be mandatory for another.

## 11. Practical Case Study: Inventory Management

A distributor experiences stock discrepancies and late deliveries.

### Findings

* Employees record stock movements manually.
* Several spreadsheets contain conflicting balances.
* Managers cannot see stock across all warehouses.
* Product identifiers are inconsistent.
* Staff have limited training on the proposed system.

### Analysis

**Business requirement:** Improve inventory accuracy and reduce stock-related losses.

**Stakeholder requirement:** Warehouse managers need access to reliable stock balances across locations.

**Functional requirement:** The solution shall record receipts, dispatches, returns, and approved adjustments.

**Non-functional requirement:** Authorized users shall retrieve a stock balance within two seconds under the agreed operating load.

**Transition requirement:** Existing stock records shall be cleansed and migrated before go-live.

**Business rule:** Only authorized personnel may approve stock adjustments above the defined threshold.

**Assumption:** Warehouse locations will provide network connectivity.

**Constraint:** The current ERP must remain in operation during the first release.

**Risk:** Poor-quality legacy data may cause inaccurate opening balances.

**Dependency:** Inventory reporting depends on successful data migration.

### Recommended actions

1. Establish baseline stock accuracy.
2. Define the target stock accuracy rate.
3. Identify data owners.
4. Cleanse and map legacy records.
5. Confirm access and approval rules.
6. Trace requirements to tests.
7. Validate results with warehouse managers.

## 12. Knowledge Check

**Question 1:** Which requirement type describes a business goal?

A. Transition
B. Business
C. Functional solution
D. Technical design

**Question 2:** "The system shall support 2,000 concurrent users" is primarily:

A. A business rule
B. A stakeholder requirement
C. A non-functional solution requirement
D. A transition requirement

**Question 3:** What is the main purpose of traceability?

A. To eliminate all stakeholder disagreements
B. To establish relationships among requirements and related elements
C. To replace testing
D. To guarantee project success

**Question 4:** "The new platform will integrate with the existing ERP" is a constraint when:

A. It limits the available solution choices
B. It measures customer satisfaction
C. It identifies a business outcome
D. It describes an unverified assumption

**Question 5:** Which statement best distinguishes validation from verification?

A. Validation checks alignment with needs; verification checks defined quality criteria.
B. Validation is only for software; verification is only for business processes.
C. They always mean the same thing.
D. Verification determines financial value exclusively.

**Question 6:** Migrating legacy customer data is most likely which requirement type?

A. Business
B. Transition
C. Stakeholder
D. Business rule

### Answers and Explanations

1. **B — Business.** Business requirements describe organizational goals and outcomes.
2. **C — Non-functional solution requirement.** It specifies a capacity or performance condition.
3. **B — Establish relationships.** Traceability enables impact analysis and coverage assessment.
4. **A — It limits available solution choices.** Constraints restrict the options available.
5. **A — Alignment with needs vs. quality criteria.** Validation and verification have distinct purposes.
6. **B — Transition.** Migration is often needed to move from the current state to the future state.

## 13. Revision Summary

* The four requirement types are business, stakeholder, solution, and transition.
* Solution requirements include functional and non-functional requirements.
* Business rules govern behavior; requirements specify needed capabilities or conditions.
* Assumptions are accepted provisionally; constraints restrict choices; risks involve uncertainty; dependencies link related elements.
* Traceability supports impact analysis and coverage.
* Verification assesses defined quality criteria; validation checks alignment with needs.
* Prioritization balances value, risk, urgency, and constraints.

## 14. Further Study

Review the BABOK Guide sections on requirements classification, requirements architecture, requirements life cycle management, and requirements analysis and design definition. Confirm the current CCBA exam blueprint for the applicable task coverage.
