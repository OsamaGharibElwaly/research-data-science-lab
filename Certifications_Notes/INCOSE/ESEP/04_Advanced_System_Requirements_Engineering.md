# Module 04: Advanced System Requirements Engineering

## 1. Learning Objectives

By the end of this module, you should be able to:

* Establish and maintain a coherent system requirements baseline.
* Analyze functional, performance, interface, constraint, and quality requirements.
* Apply requirements analysis and decomposition appropriately.
* Assess feasibility, consistency, completeness, and verifiability.
* Manage requirement allocation, dependencies, and change impact.
* Integrate requirements with architecture, risk management, verification, and validation.

## 2. Advanced Requirements Engineering

Requirements engineering is the disciplined process of eliciting, analyzing, specifying, validating, verifying, managing, and maintaining requirements throughout the lifecycle.

At an advanced level, the objective is not merely to produce a requirements document. It is to ensure that requirements form a technically coherent, feasible, traceable, and testable basis for system development and acceptance.

Requirements engineering connects:

* Stakeholder intent.
* System behavior.
* Architecture and design.
* Operational constraints.
* Safety and security.
* Verification and validation.
* Configuration and change control.
* Acceptance and lifecycle support.

## 3. Requirements Categories

### 3.1 Functional Requirements

Define the behavior or services the system must provide.

Example:

"The system shall record each accepted shipment event with its shipment identifier and event timestamp."

### 3.2 Performance Requirements

Define measurable levels of system behavior.

Examples include response time, throughput, accuracy, capacity, availability, and recovery time.

A performance requirement needs a defined operating context and measurement method.

### 3.3 Interface Requirements

Specify interactions between system elements, external systems, users, networks, and physical interfaces.

They may address:

* Data formats.
* Communication protocols.
* Physical connectors.
* Timing and synchronization.
* Units and coordinate systems.
* Error handling.
* Authentication and authorization.
* Interface capacity and failure behavior.

### 3.4 Constraint Requirements

Specify boundaries within which the solution must be developed or operated.

Examples include mandated standards, physical limits, approved technologies, contractual conditions, and regulatory obligations.

Constraints should be justified and controlled because they can limit future design alternatives.

### 3.5 Quality Requirements

Address characteristics such as reliability, maintainability, usability, security, safety, portability, resilience, and interoperability.

These qualities should be expressed using measurable criteria and defined conditions wherever possible.

### 3.6 Operational and Support Requirements

Address installation, training, maintenance, diagnostics, logistics, supportability, upgrades, monitoring, and decommissioning.

### 3.7 Derived Requirements

Derived requirements emerge from architecture decisions, engineering analysis, interface needs, safety analysis, or lower-level design.

They must be justified, traceable, assessed for impact, and managed under appropriate change control.

## 4. Requirements Analysis

Requirements analysis determines whether proposed requirements adequately define the system's necessary behavior and constraints.

Typical activities include:

1. Clarify terminology and assumptions.
2. Identify missing operating scenarios.
3. Check requirement completeness and consistency.
4. Analyze interactions and dependencies.
5. Evaluate technical feasibility.
6. Assess performance budgets and resource constraints.
7. Identify safety, security, and reliability implications.
8. Establish verification methods.
9. Identify unresolved decisions and risks.
10. Review the complete set for system-level coherence.

Analysis should examine the requirements set as a whole, not just individual statements.

## 5. Decomposition and Allocation

Decomposition breaks a system-level problem into manageable elements and obligations.

Allocation assigns functions, performance budgets, interfaces, or requirements to appropriate system elements.

A disciplined approach is:

1. Establish system-level functions and requirements.
2. Develop candidate architectures.
3. Identify logical and physical system elements.
4. Allocate requirements and responsibilities.
5. Evaluate feasibility at each level.
6. Check that allocated elements can collectively satisfy the parent requirements.
7. Maintain traceability across levels.
8. Reassess allocations when architecture or requirements change.

Over-decomposition can create unnecessary complexity. Under-decomposition can leave critical behavior and interfaces insufficiently specified.

## 6. Requirements Baselines and Maturity

A baseline is an agreed, controlled set of requirements used as a reference for subsequent engineering and change management.

Baselines may be established at different levels and lifecycle points, such as:

* Stakeholder needs baseline.
* System requirements baseline.
* Allocated requirements baseline.
* Product or configuration baseline.

Baseline maturity should reflect the project's risk, contractual commitments, and lifecycle approach.

A baseline does not mean that change is forbidden. It means that changes are evaluated, authorized, and incorporated through controlled processes.

## 7. Requirements Verification Methods

Requirements verification establishes whether a requirement has been correctly specified and whether the realized system or element satisfies it, as applicable.

Common methods include:

* **Inspection:** Examination of an item or record for compliance.
* **Analysis:** Use of calculations, models, simulations, or other analytical evidence.
* **Demonstration:** Showing that a function or behavior occurs under specified conditions.
* **Test:** Operating the system or element under controlled conditions and measuring results.

The appropriate method depends on the requirement and required confidence. Multiple methods may be necessary for complex requirements.

Verification methods should be planned early enough to influence requirement wording, instrumentation, test environments, and architecture.

## 8. Verification Versus Validation

Verification asks whether the system or element meets its specified requirements.

Validation asks whether the resulting system satisfies stakeholder needs and intended use.

For example, a shipment tracking application may pass every response-time and interface test but still fail validation if the workflow does not help dispatchers make operational decisions.

Both activities are necessary because requirements can be satisfied while still representing an incomplete or incorrect understanding of stakeholder needs.

## 9. Requirements Traceability and Coverage

A requirements management system should support relationships among:

* Stakeholder needs.
* System requirements.
* Architecture elements.
* Derived requirements.
* Interfaces.
* Verification cases.
* Validation scenarios.
* Defects and change requests.

Coverage analysis can identify requirements with no verification evidence, tests with no requirement justification, and architectural elements with unclear responsibility.

Useful measures include:

* Percentage of approved requirements with verification methods.
* Percentage of requirements with completed verification.
* Number of unresolved requirement conflicts.
* Number of orphan requirements.
* Number of unverified derived requirements.
* Requirements change impact completion rate.

Coverage metrics must be interpreted alongside quality and risk. High test coverage alone does not prove the system is safe, correct, or fit for use.

## 10. Interface and Dependency Management

Interface requirements often expose integration problems that are difficult to detect through isolated component analysis.

An interface specification may define:

* Data structure and semantics.
* Units and acceptable ranges.
* Protocols and message sequencing.
* Timing and latency.
* Error and timeout behavior.
* Authentication and access control.
* Resource limits.
* Version compatibility.
* Recovery and degraded operation.

Dependency analysis should also identify external services, infrastructure, suppliers, datasets, and operational processes required for the system to function.

Changes to one interface can affect multiple requirements, test procedures, architecture elements, and operational assumptions.

## 11. Performance Budgets and Feasibility

Performance budgets allocate system-level limits to subsystems and components.

Examples include:

* Latency budgets across processing stages.
* Power budgets across hardware elements.
* Memory and compute budgets.
* Weight and volume budgets.
* Bandwidth and storage budgets.
* Reliability allocations.

Allocations should include justified margins where uncertainty and variation require them.

For example, an end-to-end latency requirement cannot be allocated independently to each component without accounting for communication overhead, scheduling, queuing, and measurement uncertainty.

A system-level performance budget should therefore be checked against realistic operating scenarios and integration effects.

## 12. Requirements Risk and Uncertainty

Requirements risk may arise from ambiguity, technical novelty, uncertain operating conditions, stakeholder disagreement, unavailable technology, or unproven assumptions.

Useful techniques include:

* Requirement risk classification.
* Feasibility demonstrations.
* Sensitivity analysis.
* Prototyping.
* Scenario testing.
* Interface experiments.
* Assumption tracking.
* Independent technical review.

High-risk requirements should receive appropriate attention early enough to influence design decisions.

An expert distinguishes between uncertainty that can be reduced through analysis and uncertainty that must be managed through contingency planning or operational controls.

## 13. Change Impact Analysis

A proposed requirement change should be evaluated for its effects on:

1. Parent and child requirements.
2. Stakeholder needs and acceptance criteria.
3. System architecture.
4. Interfaces and external dependencies.
5. Safety and security analyses.
6. Cost and schedule.
7. Supplier commitments.
8. Verification and validation plans.
9. Existing test evidence.
10. Operational documentation and training.
11. Configuration and release compatibility.

The impact analysis should identify affected owners, necessary approvals, implementation actions, and regression testing.

A technically small change can have a large system-level impact if it affects a shared interface or a critical operating assumption.

## 14. Requirements Quality Review Checklist

For each requirement, ask:

* Is its origin or justification known?
* Is it necessary?
* Is the wording unambiguous?
* Is it sufficiently singular?
* Is it feasible?
* Are its conditions and units defined?
* Is there a suitable verification method?
* Are dependencies and interfaces identified?
* Does it conflict with another requirement?
* Is its allocation appropriate?
* Are safety, security, and operational consequences understood?
* Is the current version controlled?

For the full set, also assess completeness across normal operation, abnormal conditions, degraded modes, maintenance, recovery, and retirement.

## 15. Common Failure Patterns

1. Treating the requirements baseline as a static document.
2. Writing requirements before understanding the operational context.
3. Decomposing requirements without checking system-level feasibility.
4. Failing to allocate performance budgets with realistic margins.
5. Ignoring interface timing and error handling.
6. Using a verification method that cannot demonstrate the stated requirement.
7. Confusing verification coverage with system validation.
8. Failing to analyze the effects of a change on existing evidence.
9. Accepting derived requirements without traceable justification.
10. Treating tool usage as a substitute for sound requirements engineering.

## 16. Practical Exercise

**Scenario:** A distribution center is introducing an automated package-sorting system with barcode scanners, conveyor controls, a warehouse management interface, and operational dashboards.

Produce:

1. A set of ten functional requirements.
2. Five performance requirements with defined measurement conditions.
3. Five interface requirements.
4. Three quality or operational requirements.
5. A requirements hierarchy showing parent-child relationships.
6. A traceability matrix connecting requirements to verification cases.
7. A verification strategy covering inspection, analysis, demonstration, and test.
8. A change-impact analysis for replacing the barcode scanner interface.
9. Three high-risk requirements and a plan to reduce their uncertainty.

Do not invent arbitrary performance thresholds. State which values require stakeholder agreement, operational measurement, supplier evidence, or engineering analysis.

## 17. Knowledge Check

**Q1.** What is the purpose of requirements decomposition?

**Answer:** To allocate system-level obligations into manageable, coherent requirements for lower-level elements while preserving traceability and system-level feasibility.

**Q2.** Why should verification methods be identified early?

**Answer:** Early identification helps ensure requirements are testable and that design, instrumentation, test environments, and evidence collection are planned appropriately.

**Q3.** What is the difference between a baseline and an immutable specification?

**Answer:** A baseline is controlled and changes require appropriate evaluation and authorization; it is not permanently frozen.

**Q4.** Why can a small interface change create major system risk?

**Answer:** Interfaces connect multiple components and processes, so a change may affect dependencies, timing, compatibility, safety, and existing verification evidence.

**Q5.** Why is requirements coverage insufficient as the only quality measure?

**Answer:** Coverage shows whether requirements are addressed by evidence, but it does not establish that the requirements are correct, complete, feasible, or aligned with stakeholder needs.

## 18. Professional Application Evidence

Collect evidence of your ability to:

* Improve a requirements baseline.
* Resolve a requirements conflict.
* Establish or correct requirements traceability.
* Identify an untestable or infeasible requirement.
* Evaluate a derived requirement.
* Improve interface specifications.
* Conduct change impact analysis.
* Improve verification efficiency without reducing necessary confidence.

For each case, describe the problem, your role, analysis, decision rationale, supporting evidence, measurable outcome, and lessons learned.

## 19. Key Takeaways

* Requirements engineering connects stakeholder intent to realizable system behavior.
* Requirements must be analyzed as a coherent set.
* Decomposition and allocation must preserve feasibility and traceability.
* Verification planning influences requirements quality and system design.
* Interfaces and dependencies are major sources of system-level risk.
* Controlled baselines support change without preventing justified improvement.
* Verification establishes conformance; validation establishes suitability for intended use.

## 20. Suggested References

* INCOSE, *Systems Engineering Handbook*, applicable edition.
* ISO/IEC/IEEE 29148, *Systems and software engineering — Life cycle processes — Requirements engineering*.
* ISO/IEC/IEEE 15288, *Systems and software engineering — System life cycle processes*.
* Applicable requirements management, verification, validation, and configuration management procedures.

Consult the latest official publications and the current INCOSE ESEP application guidance for authoritative requirements.
