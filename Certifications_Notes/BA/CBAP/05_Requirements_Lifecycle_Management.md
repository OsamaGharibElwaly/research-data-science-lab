# 05 — Requirements Lifecycle Management

## 1. Introduction

Requirements Lifecycle Management covers the activities required to maintain requirements and design information from their initial development through changes, implementation, and eventual retirement.

For advanced business analysts, requirements management is not simply storing documents. It involves maintaining traceability, ensuring stakeholder agreement, prioritizing requirements, evaluating changes, resolving conflicts, and keeping requirements aligned with business objectives.

This module follows the BABOK® Guide's Requirements Life Cycle Management knowledge area, with additional advanced applications for CBAP preparation.

## 2. The Requirements Life Cycle

A requirement can evolve throughout an initiative. Its lifecycle may include:

1. Identification.
2. Elicitation and analysis.
3. Specification and modeling.
4. Verification and validation.
5. Approval.
6. Implementation and verification of the solution.
7. Change assessment and maintenance.
8. Retirement when the requirement is no longer relevant.

These activities are not always sequential. Adaptive delivery may revisit requirements repeatedly, while predictive environments may introduce more formal approval and baseline controls.

### 2.1 Requirements Versus Designs

Requirements express needs, expectations, and required capabilities. Designs describe how a solution may satisfy them.

Both requirements and designs can be managed throughout their lifecycles. A design decision may affect requirements, and a change to a requirement may affect multiple designs.

### 2.2 Lifecycle States

An organization may define states such as:

* Draft.
* Under review.
* Approved.
* In progress.
* Implemented.
* Verified.
* Rejected.
* Deferred.
* Superseded.
* Retired.

The exact states depend on the organization's governance model. State definitions should clarify what actions are permitted and what evidence is required for transitions.

## 3. Maintaining Requirements

Maintenance ensures that requirements remain accurate, usable, consistent, and relevant.

Maintenance activities include:

* Updating requirements when approved changes occur.
* Correcting errors and ambiguities.
* Recording decisions and rationale.
* Preserving historical versions.
* Updating relationships and dependencies.
* Reviewing requirements that may have become obsolete.
* Communicating changes to affected stakeholders.

Requirements should not be modified informally when the change could affect approved scope, cost, schedule, risk, or business value.

## 4. Requirements Traceability

Traceability establishes relationships between requirements and other elements of business analysis.

A traceability chain may connect:

Business objective → Business requirement → Stakeholder requirement → Solution requirement → Design → Test case → Business outcome.

### 4.1 Benefits of Traceability

Traceability supports:

* Impact analysis.
* Requirements coverage.
* Change assessment.
* Verification and validation.
* Compliance and auditability.
* Defect investigation.
* Scope management.
* Benefits realization.

### 4.2 Forward and Backward Traceability

**Forward traceability** follows a requirement toward its implementation, verification, or intended outcome.

**Backward traceability** traces a requirement back to its source, business objective, or underlying need.

Both directions are important.

Forward traceability helps identify requirements that have not been implemented or tested. Backward traceability helps identify requirements that lack a defensible business justification.

### 4.3 Traceability Matrix

| Requirement ID | Business Objective        | Design Reference | Test Reference | Status       |
| -------------- | ------------------------- | ---------------- | -------------- | ------------ |
| BR-01          | Reduce processing time    | DES-01           | TC-01          | Approved     |
| SR-02          | Improve order visibility  | DES-04           | TC-08          | In progress  |
| NFR-03         | Protect confidential data | DES-07           | TC-12          | Under review |

This is an illustrative matrix. Real repositories should also capture owners, versions, dependencies, and approval details when necessary.

### 4.4 Traceability Quality

Traceability should be meaningful rather than mechanical. A link should represent a genuine relationship.

Poor traceability can result from:

* Missing source references.
* Outdated links.
* Incorrect requirement identifiers.
* Requirements without business justification.
* Tests that do not verify the intended behavior.
* Designs that no longer satisfy the approved requirements.

## 5. Maintaining Requirements Reuse

Requirements reuse means applying existing requirements or requirement components in another context when appropriate.

Potential sources include:

* Organizational standards.
* Previous projects.
* Product families.
* Regulatory requirements.
* Shared services.
* Enterprise architecture.
* Existing business rules.

### 5.1 Benefits

Reuse can reduce:

* Analysis effort.
* Documentation duplication.
* Inconsistency.
* Review time.
* Repeated discovery of known constraints.

### 5.2 Risks

A reused requirement may be inappropriate when:

* The business context differs.
* Regulations have changed.
* Stakeholder needs are different.
* Technology constraints have changed.
* The original requirement was poorly validated.
* Assumptions no longer hold.

Every reused requirement should be checked for relevance, correctness, applicability, and ownership.

## 6. Requirements Prioritization

Prioritization determines the relative importance of requirements when time, budget, resources, or implementation capacity are limited.

### 6.1 Prioritization Factors

Consider:

* Business value.
* Strategic alignment.
* Risk reduction.
* Regulatory necessity.
* Stakeholder urgency.
* Dependencies.
* Implementation cost.
* Technical feasibility.
* Time sensitivity.
* Operational impact.

A requirement may be important because it enables other requirements, even if its direct business value is limited.

### 6.2 MoSCoW Technique

MoSCoW categorizes requirements into four groups:

* **Must have:** Essential for the agreed outcome or minimum viable solution.
* **Should have:** Important but not absolutely essential for the immediate release.
* **Could have:** Desirable if resources permit.
* **Won't have this time:** Explicitly excluded from the current scope or release.

"Won't have this time" does not necessarily mean the requirement will never be implemented.

### 6.3 Weighted Scoring

A weighted scoring model compares alternatives against defined criteria.

Example:

| Criterion           | Weight | Requirement A Score | Requirement B Score |
| ------------------- | -----: | ------------------: | ------------------: |
| Business value      |    40% |                   5 |                   3 |
| Risk reduction      |    30% |                   4 |                   5 |
| Implementation ease |    20% |                   3 |                   4 |
| Strategic alignment |    10% |                   5 |                   3 |

Using a five-point scale:

* Requirement A: \(0.4(5)+0.3(4)+0.2(3)+0.1(5)=4.3\)
* Requirement B: \(0.4(3)+0.3(5)+0.2(4)+0.1(3)=3.9\)

Requirement A ranks higher under these assumptions. The result depends on the selected weights and scores, so the model should support rather than replace informed judgment.

### 6.4 Prioritization Challenges

Common problems include:

* Every stakeholder claims their requirement is essential.
* Short-term benefits conflict with strategic objectives.
* Dependencies are overlooked.
* Estimates of value are uncertain.
* Technical risks are underestimated.
* Political influence replaces objective criteria.

A transparent prioritization process makes trade-offs explicit and documents the rationale.

## 7. Assessing Requirement Changes

A change request proposes modifying an existing requirement, design, or related business analysis element.

Change assessment determines whether the change should be accepted, rejected, deferred, or investigated further.

### 7.1 Change Assessment Process

1. Record the change request.
2. Clarify the requested change and its rationale.
3. Identify affected requirements and designs.
4. Assess dependencies and traceability.
5. Evaluate business value and strategic alignment.
6. Estimate costs, effort, and schedule effects.
7. Assess technical, operational, and regulatory risks.
8. Identify stakeholder impacts.
9. Present options and recommendations.
10. Obtain the required decision.
11. Update approved artifacts and communicate the result.

### 7.2 Impact Analysis

Impact analysis identifies the consequences of a proposed change.

It should consider:

* Related requirements.
* Designs and architecture.
* Data structures and integrations.
* Test cases.
* Documentation.
* Training.
* Operational procedures.
* Security and compliance.
* Cost and schedule.
* Expected benefits.

A seemingly small requirement change can create extensive downstream consequences.

### 7.3 Example

A retailer requests an additional payment method.

Potential impacts include:

* Payment-provider integration.
* Fraud detection.
* Financial reconciliation.
* Refund processing.
* Security controls.
* User-interface changes.
* Regression testing.
* Support procedures.

The analyst should evaluate these impacts before recommending approval.

## 8. Approval and Governance

Approval establishes that the authorized stakeholders have accepted a requirement or related decision according to the organization's governance rules.

Approval does not automatically prove that a requirement is correct, feasible, or valuable. Those concerns should be addressed through appropriate analysis and review.

### 8.1 Baselines

A requirements baseline is an agreed reference version used for control and comparison.

A baseline supports:

* Change control.
* Scope management.
* Auditability.
* Progress assessment.
* Impact analysis.

Baselining should not prevent legitimate changes. It establishes a controlled reference against which changes can be assessed.

### 8.2 Adaptive Environments

In adaptive environments, requirements may be refined continuously. Governance may rely on product backlogs, acceptance criteria, prioritization policies, and release decisions instead of a single comprehensive requirements baseline.

The objective remains the same: maintain control appropriate to the risk and delivery context.

## 9. Resolving Requirement Conflicts

Conflicting requirements arise when different stakeholders, policies, or system constraints impose incompatible expectations.

Example:

* Finance wants all transactions to require manual approval.
* Operations wants low-value transactions approved automatically.

### Resolution Approach

1. Identify the conflicting requirements.
2. Determine their sources and authority.
3. Clarify the business objectives behind each.
4. Evaluate risks and constraints.
5. Develop alternative options.
6. Compare alternatives against agreed criteria.
7. Escalate decisions beyond the analyst's authority.
8. Document the final decision and rationale.
9. Update affected requirements and traceability.

The analyst should distinguish a genuine contradiction from requirements that apply under different conditions.

## 10. Requirement Lifecycle Metrics

Useful measures include:

* Percentage of requirements with valid traceability.
* Number of unresolved conflicts.
* Average change-assessment time.
* Requirements defect rate.
* Percentage of approved requirements verified.
* Number of requirements without an identified source.
* Rework attributable to misunderstood requirements.

Metrics should be interpreted carefully. For example, a high number of change requests may reflect unstable scope, but it may also reflect effective discovery of previously unknown needs.

## 11. Advanced Case Study: Banking Application Enhancement

### Scenario

A bank plans to introduce biometric login to its mobile application.

### Lifecycle Management

**Need:** Improve authentication usability while maintaining appropriate security.

**Requirements:** Define authentication behavior, supported devices, accessibility needs, fallback procedures, and security expectations.

**Traceability:** Link the business objective to stakeholder needs, solution requirements, designs, test cases, and security controls.

**Prioritization:** Essential security and fallback requirements take precedence over optional interface enhancements.

**Change request:** A stakeholder proposes supporting additional biometric methods. Assess device compatibility, security implications, testing effort, and operational support.

**Governance:** Obtain approval from the appropriate business and security authorities.

**Evaluation:** Measure authentication success, failed login rates, support requests, and security outcomes.

### Key Lesson

Requirements lifecycle management keeps requirements controlled, connected to their objectives, and responsive to change without losing accountability.

## 12. Knowledge Check

### Questions

1. What is requirements lifecycle management?
2. How do forward and backward traceability differ?
3. Why should requirements be evaluated before reuse?
4. What does "Won't have this time" mean in MoSCoW?
5. Why is impact analysis important before approving a change?
6. How does a requirements baseline support governance?
7. Why is approval different from verification?
8. How should an analyst resolve conflicting requirements?
9. Why might a high change-request count not always indicate failure?
10. What makes traceability useful rather than merely administrative?

### Answers

1. It maintains requirements and related designs through development, change, implementation, and retirement.
2. Forward traceability follows a requirement toward implementation and outcomes; backward traceability follows it toward its source and justification.
3. Reused requirements may be inaccurate or inappropriate in a different context.
4. It is excluded from the current scope or release, not necessarily permanently rejected.
5. It reveals downstream consequences, dependencies, costs, risks, and stakeholder impacts.
6. It provides an agreed reference for assessing and controlling changes.
7. Approval is a governance decision; verification assesses whether requirements or solutions satisfy specified criteria.
8. Clarify the conflict, evaluate evidence and objectives, develop options, and follow the appropriate decision process.
9. It may indicate effective discovery of previously unknown needs, although it can also reveal instability.
10. It provides accurate relationships that support impact analysis, verification, scope control, and value realization.

## 13. Practical Exercises

### Exercise 1: Build a Traceability Matrix

Create a matrix connecting five business objectives to stakeholder requirements, solution requirements, designs, test cases, and outcome measures.

### Exercise 2: Prioritization

Use MoSCoW and weighted scoring to prioritize ten requirements for an e-commerce platform. Explain differences between the results.

### Exercise 3: Change Impact Assessment

Evaluate a request to introduce a new payment method into an existing system. Document technical, operational, financial, security, and stakeholder impacts.

### Exercise 4: Requirements Reuse

Select three requirements from a previous project and determine whether they can be reused in a different business context. Identify the assumptions requiring validation.

### Exercise 5: Conflict Resolution

Resolve conflicting requirements between finance, operations, and customer service. Document the decision criteria, trade-offs, approval authority, and rationale.

## 14. Recommended References

* IIBA, *A Guide to the Business Analysis Body of Knowledge (BABOK® Guide)*, Version 3.
* IIBA, official CBAP certification resources.
* ISO/IEC/IEEE 29148, Requirements Engineering.
* ISO 9001, Quality Management Systems — Requirements.
* ISO 31000, Risk Management — Guidelines.

## 15. Module Summary

Requirements Lifecycle Management maintains the integrity and usefulness of requirements throughout change. Traceability connects requirements to their origins and outcomes; prioritization supports resource allocation; change assessment reveals downstream impacts; and governance ensures that decisions are made by the appropriate stakeholders. Together, these practices preserve alignment between business needs, implementation, and realized value.
