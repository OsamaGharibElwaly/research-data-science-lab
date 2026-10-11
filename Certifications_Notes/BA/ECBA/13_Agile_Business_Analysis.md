# 13 — ECBA Requirements Quality and Traceability

## 1. Module Objectives

By the end of this module, you should be able to:

* Explain the characteristics of quality requirements.
* Identify ambiguity, inconsistency, and incompleteness.
* Understand requirements verification and validation.
* Explain requirements traceability and relationships.
* Understand requirement versioning and status management.
* Apply quality and traceability concepts to practical scenarios.

## 2. Introduction

Requirements provide a shared understanding of what stakeholders need from a change. Poor requirements can cause rework, delays, incorrect implementations, and failure to deliver expected business value.

Requirements quality concerns whether requirements are expressed in a way that supports understanding, analysis, implementation, and evaluation.

Traceability concerns the relationships between requirements and other relevant information.

Together, quality management and traceability help teams understand what must be delivered, why it is needed, how it relates to other elements, and whether the intended outcomes have been achieved.

## 3. Characteristics of Quality Requirements

Requirements should be suitable for their intended purpose and audience.

Important characteristics include:

### 3.1 Clear

A requirement should have an understandable meaning.

Poor: "The system should process requests quickly."

Improved: "The system shall display the request confirmation within two seconds for at least 95% of eligible requests under the agreed normal operating load."

The improved requirement provides a measurable expectation. The actual threshold should be agreed with stakeholders.

### 3.2 Complete

A requirement should contain the information necessary for its intended use.

Poor: "The system shall notify customers."

Questions remain: Which customers? Under what conditions? Through which channel? What information must be included?

Completeness is assessed in context. A requirement need not contain every implementation detail, but missing information must not prevent correct interpretation or use.

### 3.3 Consistent

Requirements should not contradict one another.

Example:

* Requirement A: Customers can cancel orders until shipment dispatch.
* Requirement B: Customers cannot cancel orders after payment.

If payment normally occurs before dispatch, these statements may conflict. The analyst must clarify the intended business rules.

### 3.4 Testable

A requirement should support a method for determining whether it has been satisfied.

Poor: "The application shall be user-friendly."

Improved: "At least 90% of representative first-time users shall complete the defined checkout task without assistance during the agreed usability test."

Testability depends on an agreed measurement method and acceptance criteria.

### 3.5 Feasible

A requirement should be achievable within applicable technical, financial, legal, operational, and time constraints.

A requirement that exceeds available infrastructure or budget may require negotiation, alternative designs, or a change in scope.

### 3.6 Necessary

A requirement should contribute to a genuine need, objective, obligation, or justified constraint.

Unnecessary requirements can increase costs and complexity without delivering meaningful value.

### 3.7 Traceable

A requirement should be capable of being linked to relevant sources, objectives, designs, tests, and other artifacts when appropriate.

Traceability supports change assessment and demonstrates why a requirement exists.

### 3.8 Unambiguous

A requirement should not reasonably support multiple conflicting interpretations.

Words such as "fast," "simple," "appropriate," and "efficient" may need clarification.

## 4. Requirements Verification

Verification examines whether requirements and designs are expressed appropriately and meet relevant quality standards.

Verification questions include:

* Is the requirement clear?
* Is it consistent with related requirements?
* Is it sufficiently complete?
* Can it be tested or otherwise assessed?
* Is the terminology used consistently?
* Does it follow applicable documentation standards?

### Example

Requirement: "The system must respond quickly."

A reviewer identifies that "quickly" is subjective.

The requirement is revised to specify a response-time threshold, workload conditions, and measurement method.

This improves its quality and testability.

## 5. Requirements Validation

Validation examines whether requirements and designs address the actual business need and contribute to desired outcomes.

Validation questions include:

* Does this requirement support a business objective?
* Does it address the stakeholder's actual need?
* Is the proposed capability appropriate?
* Does it create unnecessary complexity?
* Will satisfying it contribute to the desired future state?

### Example

A company asks for a sophisticated dashboard.

Investigation reveals that managers primarily need a daily exception report to identify delayed orders.

A simpler reporting capability may satisfy the business need more effectively.

The distinction is important: a requirement can be written perfectly yet still be the wrong requirement.

## 6. Verification Versus Validation

| Aspect           | Verification                        | Validation                                               |
| ---------------- | ----------------------------------- | -------------------------------------------------------- |
| Main concern     | Quality of requirements and designs | Relevance to business needs                              |
| Typical question | Is it expressed correctly?          | Is it the right thing to address the need?               |
| Example          | Clarifying an ambiguous threshold   | Confirming the threshold supports the business objective |
| Potential result | Improved requirement quality        | Revised scope or requirements                            |

Both activities are important and may occur iteratively throughout an initiative.

## 7. Requirements Traceability

### 7.1 Definition

Traceability establishes and maintains relationships between requirements and relevant elements.

Depending on the initiative, these relationships may connect requirements to:

* Business objectives.
* Stakeholder needs.
* Sources.
* Other requirements.
* Designs.
* Development work items.
* Test cases.
* Solution components.
* Business rules.
* Delivered capabilities.

### 7.2 Forward Traceability

Forward traceability follows a requirement toward related downstream elements.

Example:

Business requirement → Detailed requirement → Design element → Test case.

It can help determine whether requirements have been addressed during delivery.

### 7.3 Backward Traceability

Backward traceability follows an element back to its source or justification.

Example:

Test case → Requirement → Stakeholder need → Business objective.

It can help determine why a particular feature or test exists.

### 7.4 Bidirectional Traceability

Bidirectional traceability supports tracing in both directions.

It helps analysts understand both the origins and downstream implications of requirements.

The precise terminology and implementation depend on the organization's traceability approach.

## 8. Traceability Matrix

A traceability matrix records relationships between relevant elements.

Example:

| Requirement ID | Business Objective | Design  | Test Case | Status       |
| -------------- | ------------------ | ------- | --------- | ------------ |
| REQ-001        | OBJ-01             | DES-001 | TC-001    | Approved     |
| REQ-002        | OBJ-01             | DES-002 | TC-002    | In progress  |
| REQ-003        | OBJ-02             | DES-003 | TC-003    | Under review |

The matrix can reveal missing relationships.

For example, an approved requirement without an associated test or evaluation method may require investigation, depending on the requirement type.

A matrix is only useful when its information is accurate and maintained.

## 9. Requirements Versioning

Versioning records changes to requirements over time.

It helps teams understand:

* What changed.
* When it changed.
* Why it changed.
* Who authorized or made the change.
* Which version is current.
* Which related elements may be affected.

Example:

* Version 1.0: Password must contain at least eight characters.
* Version 1.1: Password must contain at least twelve characters.
* Change reason: Updated security policy.

The team should identify affected designs, tests, user guidance, and other dependent elements.

## 10. Requirements Status Management

A requirement may have a status such as:

* Proposed.
* Under review.
* Approved.
* In progress.
* Implemented.
* Verified.
* Rejected.
* Deferred.

These labels are illustrative. Organizations may define different status models.

Status indicates the requirement's current management state; it does not automatically indicate its priority or business value.

A high-priority requirement may still be under review.

## 11. Impact Analysis

Impact analysis examines the consequences of a proposed change.

Traceability helps identify affected requirements, designs, tests, processes, stakeholders, and solution components.

### Example

A company changes the definition of an eligible customer.

The analyst investigates the effects on:

1. Customer eligibility rules.
2. Registration requirements.
3. Existing customer records.
4. Reports.
5. Automated tests.
6. Training materials.
7. Regulatory controls.

This reduces the likelihood of inconsistent changes.

## 12. Practical Case Study

### Scenario: Online Ordering Platform

A retailer wants to introduce order cancellation.

The analyst documents the business need, identifies stakeholder requirements, and creates relationships between requirements and business objectives.

A requirement states:

"Customers can cancel eligible orders before dispatch."

During verification, the team identifies ambiguity around the term "eligible."

During validation, stakeholders confirm that the cancellation capability must reduce customer support requests without creating unnecessary warehouse disruption.

The analyst clarifies the eligibility rules and links them to design elements and test cases.

Later, the business changes its cancellation policy.

Traceability helps identify affected requirements, application behavior, customer communications, and tests.

The team assesses the impact before implementing the change.

## 13. Practice Questions

### Question 1

What is the main purpose of requirements verification?

A. To ensure requirements address the business need regardless of their quality.

B. To assess whether requirements are expressed appropriately and meet quality standards.

C. To approve every requirement automatically.

D. To eliminate stakeholder participation.

**Correct answer: B**

Explanation: Verification examines the quality of requirements and designs.

### Question 2

A requirement is clear and testable but does not address the business problem. Which activity is most relevant?

A. Validation.

B. Version numbering only.

C. Status reporting only.

D. Document formatting.

**Correct answer: A**

Explanation: Validation assesses alignment with the underlying business need.

### Question 3

Which activity helps determine which tests may need modification when a requirement changes?

A. Traceability and impact analysis.

B. Branding.

C. Meeting scheduling.

D. Recruitment.

**Correct answer: A**

Explanation: Traceability helps identify dependent elements affected by a change.

### Question 4

What does a requirement's priority indicate?

A. Its current implementation status.

B. Its relative importance compared with other requirements.

C. Its version number.

D. Its author.

**Correct answer: B**

Explanation: Priority and status represent different dimensions of requirement management.

### Question 5

Which statement best describes backward traceability?

A. Following a requirement to its source or justification.

B. Assigning a developer to every requirement.

C. Automatically implementing a requirement.

D. Removing relationships between requirements.

**Correct answer: A**

Explanation: Backward traceability helps establish the origin and rationale of an element.

### Question 6

Why is version management useful?

A. It prevents all future changes.

B. It records changes and helps identify the current version and affected elements.

C. It removes the need for approval.

D. It guarantees that every requirement is correct.

**Correct answer: B**

Explanation: Version management supports controlled changes and reliable information.

## 14. Revision Checklist

* [ ] Explain quality characteristics of requirements.
* [ ] Identify ambiguous and incomplete requirements.
* [ ] Distinguish verification from validation.
* [ ] Explain forward, backward, and bidirectional traceability.
* [ ] Understand the purpose of a traceability matrix.
* [ ] Explain version and status management.
* [ ] Apply traceability to impact analysis.
* [ ] Identify missing relationships in a requirements scenario.

## 15. Further Study Resources

* IIBA: https://www.iiba.org/
* BABOK Guide: https://www.iiba.org/standards-and-resources/babok/
* ECBA certification: https://www.iiba.org/business-analysis-certifications/ecba/

## 16. Final Exam Reminder

Do not confuse requirement quality with business relevance. Verification examines whether a requirement is appropriately expressed; validation examines whether it addresses the need. Traceability connects requirements with their sources and related artifacts, supporting impact analysis and delivery control.
