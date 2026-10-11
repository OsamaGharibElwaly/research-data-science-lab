# 07 — Requirements Analysis and Design Definition

## 1. Introduction

Requirements Analysis and Design Definition (RADD) focuses on structuring, specifying, verifying, validating, and modeling requirements and designs so that stakeholders can understand the needs and evaluate potential solutions.

At the CBAP level, the analyst must move beyond writing individual requirement statements. The analyst needs to establish coherent models, evaluate solution alternatives, identify requirement relationships, assess feasibility, and ensure that requirements and designs collectively support business objectives.

This module follows the corresponding BABOK® Guide knowledge area.

## 2. Requirements Analysis Fundamentals

Requirements analysis transforms elicited information into structured, usable representations of business needs and solution expectations.

Activities include:

* Specifying and modeling requirements.
* Verifying requirements.
* Validating requirements.
* Defining architecture and design options.
* Analyzing potential value.
* Comparing alternatives.
* Maintaining consistency and traceability.

Requirements analysis is iterative. Modeling may expose missing information, while feasibility analysis may reveal that a requirement needs refinement.

## 3. Specifying Requirements

A requirement specification describes a need or expected capability in a form suitable for communication, review, and implementation.

### 3.1 Requirement Quality Characteristics

Requirements should be:

* Clear.
* Necessary.
* Feasible.
* Consistent.
* Traceable.
* Verifiable.
* Unambiguous.
* Appropriately detailed.
* Understandable to the intended audience.

### 3.2 Writing Requirement Statements

A useful format is:

"The system shall [required behavior] when [condition], subject to [relevant constraints]."

Example:

"The system shall notify the assigned supervisor when a service request remains unresolved for more than 24 business hours."

The analyst should clarify the definition of business hours, notification delivery, recipient assignment, and exceptional conditions where relevant.

### 3.3 Avoiding Ambiguity

Weak requirement:

"The system shall process orders efficiently."

Improved requirement:

"The system shall process at least 200 order submissions per minute while maintaining a 95th-percentile response time below two seconds under the approved load-test conditions."

The threshold must be validated against business needs, architecture, and operational constraints.

## 4. Functional and Non-Functional Requirements

### 4.1 Functional Requirements

Functional requirements describe behavior or capabilities.

Examples:

* The system shall calculate an invoice total.
* The application shall allow authorized users to approve orders.
* The platform shall generate a monthly performance report.
* The system shall notify users when a transaction fails.

### 4.2 Non-Functional Requirements

Non-functional requirements describe qualities or conditions of operation.

Common categories include:

* Performance.
* Reliability.
* Availability.
* Security.
* Usability.
* Accessibility.
* Scalability.
* Maintainability.
* Interoperability.
* Compliance.

Example:

"The service shall maintain 99.9% monthly availability, excluding the explicitly defined and approved maintenance window."

A non-functional requirement should define the scope, measurement conditions, and acceptable threshold.

### 4.3 Conflicting Quality Attributes

Quality attributes may compete.

For example:

* Stronger security controls may introduce additional authentication steps.
* Higher availability may increase infrastructure costs.
* Greater customization may reduce maintainability.
* More detailed logging may increase storage and privacy risks.

The analyst should help stakeholders evaluate trade-offs rather than assume every quality attribute can be maximized simultaneously.

## 5. Business Rules

Business rules define or constrain business behavior.

Examples:

* Orders above a specified amount require additional approval.
* Customers must meet defined eligibility criteria.
* Discounts cannot exceed an authorized threshold.
* Transactions must comply with applicable financial controls.

Business rules should be distinguished from requirements describing how a particular system implements them.

A business rule may exist independently of the system and apply across multiple processes or applications.

### 5.1 Decision Tables

Decision tables represent combinations of conditions and their corresponding actions.

Example:

| Order Value  | Credit Status | Required Action               |
| ------------ | ------------- | ----------------------------- |
| Within limit | Approved      | Process order                 |
| Within limit | On hold       | Request review                |
| Above limit  | Approved      | Request manager approval      |
| Above limit  | On hold       | Hold order and request review |

The table should define how boundary values, missing data, and exceptional cases are handled.

## 6. Requirements Modeling

Models provide structured representations of requirements, processes, data, interactions, and system behavior.

They help stakeholders identify gaps, contradictions, dependencies, and alternative interpretations.

### 6.1 Process Models

Process models describe activities, decisions, handoffs, and outcomes.

A basic order-processing workflow may be:

1. Receive order.
2. Validate order data.
3. Check inventory.
4. Check payment.
5. Confirm order.
6. Arrange fulfillment.
7. Notify customer.

The analyst should model exception paths such as insufficient inventory, failed payment, or incomplete customer information.

### 6.2 Use Cases

A use case describes how an actor interacts with a system to achieve a goal.

A use case typically includes:

* Name and objective.
* Primary actor.
* Preconditions.
* Trigger.
* Main success scenario.
* Alternative flows.
* Exception flows.
* Postconditions.

Example: **Approve Purchase Order**

Actor: Purchasing manager.

Precondition: A purchase order is submitted and requires approval.

Main flow:

1. Manager opens the order.
2. System displays order details and supporting information.
3. Manager reviews the request.
4. Manager approves the order.
5. System records the decision and notifies relevant stakeholders.

Alternative flow: The manager rejects the order and provides a reason.

### 6.3 Data Models

Data models describe entities, attributes, and relationships.

For an order-management system, entities may include:

* Customer.
* Order.
* Order Item.
* Product.
* Payment.
* Shipment.

Example relationships:

* One customer may place many orders.
* One order may contain many order items.
* Each order item refers to a product.
* An order may have one or more associated payments or shipment records, depending on the business model.

Data models help identify duplication, missing relationships, and data ownership requirements.

### 6.4 State Models

State models represent the states an entity can occupy and the events that cause transitions.

Example order lifecycle:

Draft → Submitted → Approved → Fulfilled → Delivered.

Alternative states may include Rejected, Cancelled, On Hold, or Returned.

The analyst should define valid transitions, transition conditions, and authorized actors.

### 6.5 Context Diagrams

Context diagrams show a system boundary and its interactions with external actors or systems.

They help clarify:

* What is inside the solution boundary.
* Which external systems exchange information.
* Who initiates interactions.
* Which responsibilities remain outside the solution.

They are especially useful for integration-heavy initiatives.

## 7. Data and Information Requirements

Data requirements define the information needed for business operations, reporting, decisions, and solution behavior.

Consider:

* Data entities and attributes.
* Definitions and formats.
* Data sources.
* Ownership.
* Quality expectations.
* Validation rules.
* Retention.
* Access controls.
* Privacy.
* Lineage.
* Integration requirements.

### 7.1 Data Quality Dimensions

Common dimensions include:

* Accuracy.
* Completeness.
* Consistency.
* Timeliness.
* Validity.
* Uniqueness.

Example:

If a customer record lacks a valid delivery address, the system may be unable to fulfill an order even if other fields are accurate.

### 7.2 Data Dictionaries

A data dictionary documents data elements and their meanings.

Example:

| Field        | Definition                   | Type             | Validation                                  |
| ------------ | ---------------------------- | ---------------- | ------------------------------------------- |
| Order_ID     | Unique order identifier      | String           | Must be unique                              |
| Order_Date   | Date the order was submitted | Date/time        | Cannot be after the defined processing date |
| Order_Status | Current order state          | Controlled value | Must match an approved status               |
| Total_Amount | Total monetary amount        | Decimal          | Must follow currency and calculation rules  |

Clear definitions reduce inconsistent interpretations across teams.

## 8. Requirements Verification

Verification evaluates whether requirements and models are sufficiently well-formed and of appropriate quality for their intended use.

Questions include:

* Is the requirement clear?
* Is it internally consistent?
* Is it feasible?
* Is it testable?
* Is it traceable?
* Is it appropriately detailed?
* Does it conflict with other requirements?

Verification focuses on the quality of the requirement or representation itself.

Techniques include structured reviews, checklists, peer review, and automated consistency checks where appropriate.

## 9. Requirements Validation

Validation determines whether the requirements represent the actual business need and support the desired outcomes.

Questions include:

* Does the requirement address a real need?
* Does it align with business objectives?
* Does it create value for relevant stakeholders?
* Does it reflect the intended future state?
* Are important stakeholder needs missing?
* Does it introduce unnecessary scope?

A requirement can be well written and still be wrong for the business.

### 9.1 Verification Versus Validation

| Verification                                | Validation                                            |
| ------------------------------------------- | ----------------------------------------------------- |
| Examines requirement quality                | Examines business relevance                           |
| Checks clarity and consistency              | Checks alignment with needs                           |
| Asks whether the requirement is well formed | Asks whether it is the right requirement              |
| May use structured requirement reviews      | May use stakeholder reviews, scenarios, or prototypes |

Both activities are necessary for reliable analysis.

## 10. Defining Solution Design Options

Design definition describes possible ways to satisfy the requirements and business needs.

Possible options include:

* Buying a commercial product.
* Developing a custom application.
* Configuring an existing platform.
* Integrating current systems.
* Outsourcing selected activities.
* Redesigning business processes.
* Combining technology and organizational changes.

### 10.1 Design Considerations

Evaluate:

* Functional fit.
* Non-functional requirements.
* Technical architecture.
* Data integration.
* Security.
* Usability.
* Maintainability.
* Scalability.
* Implementation effort.
* Operational costs.
* Vendor dependency.
* Organizational readiness.

The analyst should distinguish mandatory constraints from preferences that may be traded off.

## 11. Evaluating Solution Options

Solution options should be compared against consistent criteria.

### 11.1 Weighted Decision Matrix

Suppose an organization compares three options for a reporting platform.

| Criterion            | Weight | Build | Buy | Configure Existing Tool |
| -------------------- | -----: | ----: | --: | ----------------------: |
| Functional fit       |    30% |     5 |   4 |                       3 |
| Cost                 |    25% |     2 |   4 |                       5 |
| Implementation speed |    20% |     2 |   5 |                       4 |
| Maintainability      |    15% |     3 |   4 |                       4 |
| Flexibility          |    10% |     5 |   3 |                       3 |

Using a five-point scoring scale:

* Build: \(1.50+0.50+0.40+0.45+0.50=3.35\)
* Buy: \(1.20+1.00+1.00+0.60+0.30=4.10\)
* Configure existing tool: \(0.90+1.25+0.80+0.60+0.30=3.85\)

Under these illustrative assumptions, buying scores highest.

The result is not automatically a final decision. The analyst must validate the scores, check mandatory requirements, assess risks, and consider sensitivity to the selected weights.

### 11.2 Fit-Gap Analysis

Fit-gap analysis compares a proposed solution's capabilities with approved requirements.

* **Fit:** The solution satisfies the requirement.
* **Partial fit:** Additional configuration or process changes are needed.
* **Gap:** The solution cannot satisfy the requirement without additional work or a different approach.

This is particularly useful when evaluating commercial software.

## 12. Acceptance Criteria

Acceptance criteria define the conditions under which a requirement, feature, or deliverable will be considered acceptable.

Example:

Requirement: A customer can reset a forgotten password.

Acceptance criteria:

* A valid reset request initiates the approved verification process.
* The reset link expires according to the approved security policy.
* Invalid or expired links cannot reset the password.
* The user receives appropriate confirmation.
* The process does not reveal whether an arbitrary account exists.

Acceptance criteria should be clear, testable, and consistent with security and business rules.

## 13. Advanced Case Study: Inventory Management System

### Scenario

A retailer experiences frequent stock discrepancies and delayed replenishment.

Management requests a new inventory management application.

### Requirements Analysis

**Business need:** Improve inventory accuracy and product availability.

**Business requirements:** Reduce stock discrepancies and improve replenishment performance.

**Functional requirements:**

* Record inventory movements.
* Track stock by location.
* Generate low-stock alerts.
* Support approved stock adjustments.

**Non-functional requirements:**

* Protect inventory data.
* Maintain agreed availability.
* Process transactions within defined performance limits.
* Support the expected transaction volume.

**Data requirements:** Product identifiers, location identifiers, quantities, transaction timestamps, suppliers, and replenishment rules.

**Models:** Current-state and future-state process maps, inventory data models, and stock-status state models.

**Verification:** Review requirement clarity, consistency, feasibility, and testability.

**Validation:** Confirm that the requirements address the underlying inventory problems and expected business outcomes.

**Design alternatives:** Enhance the existing system, configure a commercial platform, or build a custom solution.

**Evaluation:** Compare alternatives based on cost, functional fit, integration risk, maintainability, and expected value.

### Key Lesson

A complete solution definition requires coherent requirements, models, data definitions, acceptance criteria, and a justified design choice.

## 14. Knowledge Check

### Questions

1. What is the purpose of Requirements Analysis and Design Definition?
2. How do functional and non-functional requirements differ?
3. Why should business rules be distinguished from system implementation requirements?
4. What does a state model represent?
5. What is the difference between verification and validation?
6. Why are data definitions important?
7. What is fit-gap analysis?
8. Why should solution alternatives be compared against common criteria?
9. What purpose do acceptance criteria serve?
10. How can models reveal requirement defects?

### Answers

1. It structures, specifies, verifies, validates, and models requirements and designs to support effective solution decisions.
2. Functional requirements describe behavior; non-functional requirements describe quality attributes or operating conditions.
3. Business rules may apply across multiple systems and processes, whereas implementation requirements describe how a particular solution satisfies needs.
4. The states of an entity and the events or conditions that cause transitions.
5. Verification checks the quality of requirements; validation checks whether they represent the actual business need.
6. They establish consistent meaning, improve data quality, and support integration and reporting.
7. It compares a solution's capabilities with approved requirements to identify fits and gaps.
8. Common criteria make trade-offs more transparent and reduce arbitrary decision-making.
9. They define the conditions for accepting a requirement, feature, or deliverable.
10. Models expose missing paths, contradictory rules, incomplete data relationships, and ambiguous behavior.

## 15. Practical Exercises

### Exercise 1: Requirements Specification

Write ten functional requirements and five non-functional requirements for an online ordering system. Ensure that the requirements are clear and verifiable.

### Exercise 2: Process and State Modeling

Model an order-fulfillment process, including normal flow, exceptions, and valid state transitions.

### Exercise 3: Data Dictionary

Create a data dictionary for a customer relationship management system. Define field meanings, types, validation rules, ownership, and privacy considerations.

### Exercise 4: Verification and Validation

Review a set of requirements and classify each defect as a verification problem, a validation problem, or both. Explain the appropriate corrective action.

### Exercise 5: Solution Evaluation

Compare a custom application, commercial product, and existing-platform configuration using a weighted decision matrix. Perform a sensitivity analysis on the most important weights.

### Exercise 6: Acceptance Criteria

Define testable acceptance criteria for user authentication, order submission, inventory updates, and management reporting.

## 16. Recommended References

* IIBA, *A Guide to the Business Analysis Body of Knowledge (BABOK® Guide)*, Version 3.
* IIBA, official CBAP certification resources.
* ISO/IEC/IEEE 29148, Requirements Engineering.
* ISO/IEC 25010, Systems and Software Quality Models.
* ISO 8000, Data Quality.
* ISO 31000, Risk Management — Guidelines.

## 17. Module Summary

Requirements Analysis and Design Definition transforms discovered needs into coherent requirements, models, and solution options. Strong practice combines clear specification, business rules, process and data modeling, verification, validation, acceptance criteria, and structured design evaluation. The goal is to establish that requirements are well formed, relevant to the business, and capable of guiding a feasible solution.
