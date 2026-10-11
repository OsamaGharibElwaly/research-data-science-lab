# 05 — Requirements Life Cycle Management

## 1. Module Objectives

By the end of this module, you should be able to:

* Explain requirements life cycle management.
* Understand requirements traceability and maintenance.
* Explain how requirements are prioritized.
* Assess proposed requirement changes.
* Understand requirements approval.
* Distinguish requirements verification from validation.
* Apply requirements management concepts to practical business scenarios.

## 2. Introduction

Requirements Life Cycle Management focuses on managing requirements and designs from their initial development through changes, implementation, and eventual retirement.

Requirements do not remain static throughout an initiative. Stakeholder needs may change, new regulations may appear, and solution designs may evolve.

Effective requirements management helps ensure that requirements remain understandable, relevant, consistent, and aligned with business objectives.

The BABOK Guide identifies five tasks within this knowledge area:

1. Trace Requirements.
2. Maintain Requirements.
3. Prioritize Requirements.
4. Assess Requirements Changes.
5. Approve Requirements.

These tasks are related and may be performed iteratively.

## 3. Trace Requirements

### 3.1 Definition

Requirements traceability establishes and maintains relationships between requirements, designs, business objectives, stakeholders, and other relevant information.

Traceability helps explain why a requirement exists and what other elements may be affected by a change.

### 3.2 Types of Traceability

**Backward traceability:** Links a requirement to its origin, such as a business objective or stakeholder need.

**Forward traceability:** Links a requirement to downstream elements, such as designs, test cases, and implemented functionality.

**Bidirectional traceability:** Supports movement in both directions, from the requirement to its source and from the source to the requirement.

### 3.3 Benefits

Traceability supports:

* Impact analysis.
* Change management.
* Verification and validation.
* Compliance.
* Test coverage.
* Identification of unnecessary requirements.
* Understanding dependencies.
* Demonstrating alignment with business objectives.

### 3.4 Example

A retailer has the business objective of reducing fraudulent transactions.

A stakeholder requirement states that suspicious transactions must be reviewed.

A solution requirement specifies that transactions exceeding defined risk thresholds must be flagged.

A test case verifies that qualifying transactions are flagged correctly.

Traceability connects these elements and demonstrates how the solution requirement supports the business objective.

### 3.5 Traceability Matrix

A traceability matrix is one way to represent relationships between requirements and other artifacts.

| ID    | Requirement                  | Source             | Related Test | Status    |
| ----- | ---------------------------- | ------------------ | ------------ | --------- |
| BR-01 | Reduce order errors          | Business objective | KPI-01       | Approved  |
| SR-01 | Validate product identifiers | BR-01              | TC-01        | Approved  |
| SR-02 | Display validation errors    | SR-01              | TC-02        | In review |

A matrix is not the only way to manage traceability. A requirements management tool or repository may provide the same capability.

## 4. Maintain Requirements

### 4.1 Purpose

Requirements maintenance ensures that requirements and designs remain accurate, consistent, usable, and relevant throughout their life cycles.

Maintenance may involve:

* Updating requirement status.
* Correcting inconsistencies.
* Managing versions.
* Preserving relationships.
* Recording approved changes.
* Removing obsolete information according to governance rules.
* Keeping requirements accessible to authorized stakeholders.

### 4.2 Requirements Status

Common status labels include:

* Proposed.
* Under review.
* Approved.
* Implemented.
* Verified.
* Rejected.
* Deferred.
* Retired.

The precise status model depends on the organization's process.

A requirement's status should not be confused with its priority. A high-priority requirement can still be under review.

### 4.3 Version Management

Version management records changes to requirements and helps users identify the current approved version.

For example, a payment requirement may change from requiring one-time passwords to supporting an additional authentication method.

A controlled repository should preserve the history of the change, its approval, and its impact on related artifacts.

## 5. Prioritize Requirements

### 5.1 Purpose

Prioritization determines the relative importance of requirements so that stakeholders can allocate limited time, money, and resources effectively.

Not every requirement can necessarily be delivered immediately.

Prioritization considers business value, risk, cost, dependencies, urgency, and stakeholder needs.

### 5.2 Common Prioritization Factors

* Business benefit.
* Regulatory necessity.
* Customer impact.
* Implementation cost.
* Technical risk.
* Dependencies.
* Urgency.
* Operational impact.
* Availability of resources.
* Consequences of not implementing the requirement.

### 5.3 MoSCoW Technique

MoSCoW categorizes requirements into four groups:

**Must have:** Essential for the agreed scope or minimum acceptable outcome.

**Should have:** Important but not absolutely essential for the immediate release.

**Could have:** Desirable if resources and time permit.

**Won't have this time:** Explicitly excluded from the current scope or release.

The final category does not necessarily mean the requirement will never be implemented.

### 5.4 Example

An online store is launching a new checkout process.

| Requirement                 | Priority             | Reason                                    |
| --------------------------- | -------------------- | ----------------------------------------- |
| Secure payment processing   | Must have            | Essential to safe transactions            |
| Order confirmation          | Must have            | Required for basic customer communication |
| Saved shopping lists        | Could have           | Useful but not essential to launch        |
| Custom animated transitions | Won't have this time | Excluded from the initial release         |

Priorities should be agreed with the appropriate stakeholders rather than assigned solely according to the analyst's personal preferences.

### 5.5 Priority Conflicts

Two stakeholders may assign different priorities to the same requirement.

The analyst should clarify the business outcomes, constraints, dependencies, and consequences of delay, then support a decision through the agreed governance process.

## 6. Assess Requirements Changes

### 6.1 Purpose

This task evaluates proposed changes to requirements or designs before decisions are made about whether and how to implement them.

A change may affect cost, schedule, scope, risk, quality, dependencies, and business value.

### 6.2 Change Assessment Process

A practical process includes:

1. Record the proposed change.
2. Understand the reason for the change.
3. Identify affected requirements and designs.
4. Assess business benefits and risks.
5. Evaluate cost, effort, and schedule implications.
6. Identify dependencies and downstream impacts.
7. Obtain the required decision.
8. Update affected information if approved.
9. Communicate the outcome.

The exact process depends on the initiative's governance and delivery approach.

### 6.3 Example

A stakeholder requests an additional identity-verification feature shortly before a release.

The analyst assesses:

* Whether the feature is required by a new regulation.
* Which existing requirements are affected.
* The implementation effort.
* Security and privacy implications.
* Testing requirements.
* Delivery risks.
* Whether the release should be adjusted.

The analyst provides the assessment to the authorized decision-makers.

A request should not automatically be accepted or rejected without considering its implications.

## 7. Approve Requirements

### 7.1 Purpose

Approval establishes that the appropriate stakeholders or authorized decision-makers accept requirements or designs for the next stage of work.

Approval may confirm agreement on scope, expectations, priorities, or readiness for implementation.

### 7.2 Approval Considerations

Before approval, stakeholders may need to determine whether requirements are:

* Understandable.
* Consistent.
* Feasible.
* Aligned with business needs.
* Sufficiently detailed for their intended use.
* Within the agreed scope.
* Acceptable in terms of risk and cost.

Different requirements may require approval from different authorities.

For example, business requirements may need sponsor approval, while security requirements may require review by an authorized security or compliance representative.

### 7.3 Approval Is Not the Same as Validation

Approval is a decision by an authorized person or group.

Validation evaluates whether requirements or designs support the business needs and desired outcomes.

A requirement can be formally approved and still be based on an incorrect assumption. Approval does not eliminate the need for continued analysis and validation.

## 8. Verification and Validation

These concepts are related but answer different questions.

**Verification:** Are the requirements or designs expressed appropriately and with sufficient quality?

Verification may examine clarity, consistency, completeness, feasibility, and testability.

**Validation:** Do the requirements or designs address the business need and deliver the intended value?

Validation focuses on alignment with the underlying need and desired outcomes.

### Example

Requirement: "The system should process orders quickly."

Verification identifies that "quickly" is ambiguous and not objectively testable.

The requirement is revised to specify an agreed processing-time threshold.

Validation then examines whether that threshold is appropriate for the business objective and stakeholder needs.

## 9. Practical Case Study

### Scenario: Banking Application

A bank is developing a mobile application.

Initial requirements include:

* Customers can view account balances.
* Customers can transfer money.
* Customers receive transaction notifications.

Later, the compliance team identifies an additional authentication requirement.

### Applying Requirements Life Cycle Management

**Trace requirements:** Link authentication requirements to relevant security and regulatory objectives.

**Maintain requirements:** Update the repository and preserve version history.

**Prioritize requirements:** Assess whether the authentication change is mandatory before launch.

**Assess changes:** Evaluate implementation cost, testing effort, schedule, and risk.

**Approve requirements:** Obtain the required approval from authorized stakeholders.

After implementation, verify that the requirement is correctly expressed and tested, and validate that the authentication approach satisfies the underlying security and business needs.

## 10. Practice Questions

### Question 1

What is the primary purpose of requirements traceability?

A. To guarantee that requirements never change.

B. To establish relationships between requirements and related information.

C. To replace stakeholder communication.

D. To eliminate the need for testing.

**Correct answer: B**

Explanation: Traceability helps connect requirements to their sources, objectives, designs, and other relevant artifacts.

### Question 2

A requirement is essential for regulatory compliance. Which prioritization consideration is most relevant?

A. Personal preference of the analyst.

B. Regulatory necessity and consequences of non-compliance.

C. Visual appeal.

D. The number of words in the requirement.

**Correct answer: B**

Explanation: Regulatory obligations can strongly influence requirement priority.

### Question 3

A stakeholder proposes a change that may delay the release. What should the analyst do?

A. Implement it immediately.

B. Reject it automatically.

C. Assess its rationale, dependencies, costs, risks, and impacts before the appropriate decision.

D. Delete the original requirement.

**Correct answer: C**

Explanation: Change assessment supports informed decisions about the consequences of a proposed change.

### Question 4

Which statement best distinguishes verification from validation?

A. Verification examines requirement quality; validation examines alignment with business needs.

B. Verification means stakeholder approval; validation means project scheduling.

C. They are always identical.

D. Validation is only relevant after a system is retired.

**Correct answer: A**

Explanation: Verification focuses on whether requirements are appropriately expressed, while validation examines whether they address the underlying need.

### Question 5

Who should formally approve a requirement?

A. Always the Business Analyst alone.

B. Any person who attends a meeting.

C. The stakeholder or authority designated by the applicable governance arrangements.

D. Only the software developer.

**Correct answer: C**

Explanation: Approval authority depends on the organization's governance and decision-making structure.

### Question 6

A requirement has high business priority but is still being reviewed. What can be concluded?

A. High priority means it is automatically approved.

B. Priority and approval status are different attributes.

C. It must already be implemented.

D. It cannot be changed.

**Correct answer: B**

Explanation: Priority expresses relative importance; status expresses where the requirement is in its management process.

## 11. Revision Checklist

* [ ] Explain requirements life cycle management.
* [ ] Recall its five BABOK tasks.
* [ ] Distinguish backward, forward, and bidirectional traceability.
* [ ] Explain requirements maintenance and version management.
* [ ] Apply MoSCoW prioritization.
* [ ] Identify factors influencing requirement priority.
* [ ] Assess proposed requirement changes.
* [ ] Understand approval authority.
* [ ] Distinguish verification from validation.
* [ ] Apply requirements management concepts to a practical scenario.

## 12. Further Study Resources

* IIBA: https://www.iiba.org/
* BABOK Guide: https://www.iiba.org/standards-and-resources/babok/
* ECBA certification: https://www.iiba.org/business-analysis-certifications/ecba/

## 13. Final Exam Reminder

For requirement-management scenarios, identify whether the problem concerns relationships, ongoing accuracy, relative importance, a proposed change, or formal acceptance. These correspond respectively to traceability, maintenance, prioritization, change assessment, and approval.
