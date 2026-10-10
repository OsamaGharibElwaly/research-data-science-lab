# 13. Tailoring and Complex System Applications

## 1. Purpose

This module explains how to tailor systems engineering processes to the context, risk, scale, complexity, and lifecycle of a system. Expert systems engineers do not apply every process identically to every project. They preserve necessary engineering rigor while adapting the approach to project-specific needs.

## 2. Learning Objectives

By the end of this module, you should be able to:

* Explain systems engineering tailoring and why it is necessary.
* Select processes appropriate to project complexity and risk.
* Balance agility, governance, documentation, and technical rigor.
* Apply systems engineering to complex, regulated, distributed, and rapidly changing environments.
* Document tailoring decisions and justify them to stakeholders.
* Recognize when tailoring has gone too far and creates unacceptable risk.

## 3. Core Concepts

### 3.1 What Is Systems Engineering Tailoring?

Tailoring is the deliberate adaptation of systems engineering processes, methods, reviews, documentation, tools, and governance to the characteristics of a specific project or organization.

Tailoring is not simply removing activities to save money. Each change should have a technical and managerial justification.

A sound tailoring decision considers:

* System complexity and novelty.
* Safety, security, and mission criticality.
* Regulatory and contractual obligations.
* Stakeholder diversity and geographic distribution.
* Lifecycle stage and project maturity.
* Cost, schedule, resources, and uncertainty.
* Supplier and integration dependencies.
* Consequences of failure.

### 3.2 Tailoring Versus Process Compliance

**Process compliance** means following a defined process or standard.

**Tailoring** means adapting how that process is applied within the permitted rules of the governing standard, contract, or organizational policy.

A project may tailor the depth and frequency of reviews while still retaining required approval gates, evidence, and traceability.

Mandatory legal, regulatory, contractual, and organizational requirements must not be removed merely because the project team considers them inconvenient.

### 3.3 Tailoring Dimensions

| Dimension                | Possible tailoring decision                      | Main consideration                   |
| ------------------------ | ------------------------------------------------ | ------------------------------------ |
| Requirements             | Scale the depth of decomposition                 | Complexity and verification needs    |
| Architecture             | Use lightweight or formal architecture models    | System interfaces and risk           |
| Reviews                  | Adjust frequency and depth                       | Risk, maturity, and change rate      |
| Documentation            | Use concise or comprehensive artifacts           | Stakeholder and compliance needs     |
| Verification             | Select appropriate test and analysis methods     | Consequences of failure              |
| Configuration management | Scale controls and approval workflows            | Change impact and baseline stability |
| Risk management          | Adjust analysis depth and review cadence         | Uncertainty and exposure             |
| Lifecycle                | Use sequential, iterative, or hybrid development | Technical and business constraints   |

### 3.4 Risk-Based Tailoring

Risk-based tailoring gives more attention to processes that control the most significant threats.

For example, a small internal dashboard may need lightweight architecture documentation and automated testing. A medical monitoring device may require stronger requirements traceability, hazard analysis, verification evidence, configuration control, and formal approval.

The principle is proportional rigor: the process should be strong enough to manage the consequences of failure.

### 3.5 Tailoring Process

A practical tailoring workflow is:

1. Understand the mission, objectives, constraints, and operating environment.
2. Identify applicable standards, contracts, policies, and mandatory activities.
3. Assess system complexity, novelty, interfaces, uncertainty, and risk.
4. Identify candidate engineering processes and lifecycle activities.
5. Decide which activities need full, reduced, combined, or specialized implementation.
6. Record the rationale, assumptions, risks, owners, and approvals.
7. Validate the tailored approach with stakeholders.
8. Monitor results and revise the tailoring when conditions change.

### 3.6 Tailoring Authority and Accountability

Tailoring decisions should have clear ownership.

Typical responsibilities include:

* **Systems engineering leadership:** evaluates technical adequacy.
* **Project management:** evaluates schedule, budget, and resource effects.
* **Quality assurance:** checks compliance with required processes.
* **Safety, security, and regulatory specialists:** identify mandatory controls.
* **Customer or designated authority:** approves deviations where required.

The person proposing a reduction in process rigor should not assume that the reduction is automatically acceptable.

## 4. Complex System Applications

### 4.1 Characteristics of Complex Systems

Complex systems may contain:

* Many interacting components and subsystems.
* Emergent behavior that cannot be understood from individual components alone.
* Multiple organizations, suppliers, and stakeholder groups.
* Dynamic operating environments.
* Technical, organizational, and regulatory dependencies.
* High uncertainty and difficult-to-predict failure modes.

Complexity is not determined only by system size. A relatively small system with high uncertainty or safety consequences can require substantial engineering rigor.

### 4.2 Engineering in Regulated Environments

Regulated systems often require formal evidence that requirements were satisfied and risks were controlled.

Typical practices include:

* Controlled requirements baselines.
* Bidirectional traceability.
* Documented verification and validation.
* Formal review records.
* Approved changes and configuration identification.
* Safety or security assurance evidence.
* Auditable decisions and release authorization.

Tailoring should simplify the implementation where allowed, not eliminate required evidence.

### 4.3 Engineering in Agile Environments

Agile development can be combined with systems engineering by using iterative development, frequent feedback, continuous integration, and incremental verification.

Useful practices include:

* Maintain system-level requirements and architecture.
* Allocate work into manageable increments.
* Define acceptance criteria before implementation.
* Use automated tests where appropriate.
* Review interface changes across teams.
* Maintain traceability proportional to risk.
* Integrate frequently instead of postponing integration until the end.

Agility does not remove the need for system-level thinking. Local team success can still produce system-level failure if interfaces, safety constraints, or operational needs are ignored.

### 4.4 Distributed and Multi-Supplier Projects

Distributed projects introduce communication, ownership, and interface risks.

Effective practices include:

* Clearly defined subsystem boundaries.
* Interface control documents or equivalent specifications.
* Agreed data formats and naming conventions.
* Shared configuration and change-control procedures.
* Explicit responsibility assignments.
* Integration plans and test environments.
* Regular cross-organizational technical reviews.

### 4.5 Legacy-System Modernization

Legacy modernization must account for existing operational behavior, undocumented interfaces, historical data, and compatibility requirements.

A suitable approach may include:

1. Identify the current system and its dependencies.
2. Capture essential existing behavior.
3. Define what must be retained, replaced, or retired.
4. Assess migration and coexistence risks.
5. Validate interfaces and data migration.
6. Plan rollback and continuity arrangements.
7. Verify the new system in realistic operational conditions.

## 5. Practical Example: Tailoring a Monitoring Platform

An organization develops an internal monitoring platform used by ten employees. The platform gathers application logs and displays operational metrics.

A suitable tailored approach could include:

* Lightweight stakeholder and requirements documentation.
* A simple architecture diagram.
* Automated unit and integration tests.
* Version control and code review.
* Basic access control and logging.
* A small risk register.
* A controlled deployment and rollback procedure.

If the same platform begins controlling safety-critical industrial equipment, the engineering approach must be reassessed. Stronger hazard analysis, timing and reliability requirements, formal verification, cybersecurity assurance, interface control, and operational approval may become necessary.

The correct process depends on the system's actual role and consequences of failure.

## 6. Common Tailoring Mistakes

* Removing activities without analyzing risk.
* Treating every project as if it had the same complexity.
* Confusing minimal documentation with no documentation.
* Ignoring mandatory contractual or regulatory requirements.
* Tailoring processes at the project level without considering enterprise interfaces.
* Failing to revisit tailoring after major changes.
* Reducing verification because the schedule is late.
* Allowing each team to use incompatible methods without coordination.

## 7. Exercises

### Exercise 1: Process Selection

A low-risk prototype is expected to be replaced after three months. Identify five engineering activities that should remain, even if the process is lightweight.

### Exercise 2: High-Risk System

A system includes safety-critical control software, multiple suppliers, and strict regulatory obligations. Explain why reduced documentation and informal approvals may be inappropriate.

### Exercise 3: Tailoring Review

A project removes integration testing to save two weeks. List the information required before approving or rejecting this decision.

## 8. Suggested Answers

**Exercise 1:** Clear objectives and acceptance criteria, basic requirements, architecture and interface understanding, version control, appropriate automated tests, and a documented deployment or rollback plan. The exact set depends on the prototype's intended use and risks.

**Exercise 2:** The project needs credible evidence of requirement satisfaction, interface compatibility, safety, and regulatory compliance. Informal approvals may not establish accountability or provide an auditable decision record.

**Exercise 3:** Consider the affected interfaces, integration risks, previous test results, change history, consequences of failure, alternative test methods, downstream dependencies, acceptance criteria, and authorized approval requirements. Schedule pressure alone is not sufficient justification.

## 9. Professional Application Evidence

When documenting experience for professional review, capture:

* A process-tailoring decision you helped evaluate.
* The constraints and risks considered.
* The alternatives discussed.
* The rationale for the chosen approach.
* Required approvals and stakeholders involved.
* Evidence that the approach was effective.
* Lessons learned and subsequent adjustments.

## 10. Key Takeaways

* Tailoring is a reasoned engineering decision, not arbitrary process removal.
* Rigor should be proportional to complexity, uncertainty, and consequences of failure.
* Mandatory requirements remain binding.
* Agile, regulated, legacy, and distributed projects need different implementations of systems engineering.
* Tailoring must be documented, approved where necessary, and reviewed as the system evolves.

## 11. Suggested References

* ISO/IEC/IEEE 15288, Systems and software engineering — System life cycle processes.
* ISO/IEC/IEEE 15289, Content of life-cycle information items.
* INCOSE Systems Engineering Handbook.
* Applicable organizational process standards, contracts, and regulatory requirements.
