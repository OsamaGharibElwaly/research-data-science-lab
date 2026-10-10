# 04 — Life Cycle Technical Processes

## 1. Learning Objectives

By the end of this module, you should be able to:

* Explain the purpose of the life-cycle technical processes used in systems engineering.
* Distinguish business or mission analysis, stakeholder needs definition, system requirements definition, architecture definition, and design definition.
* Explain system analysis, implementation, integration, verification, validation, transition, operation, maintenance, and disposal.
* Understand the relationships between requirements, architecture, design, implementation, and evidence.
* Explain how traceability, interface management, risk analysis, and configuration management support technical work.
* Distinguish verification from validation and explain why both are necessary.
* Apply technical-process concepts to a realistic system.
* Recognize that life-cycle technical processes are iterative, interconnected, and tailored to the system context.

**Terminology note:** ISO/IEC/IEEE 15288 defines a system life-cycle process framework. Process names and arrangements can vary by edition, adoption, and organizational implementation. Consult the edition and terminology specified by the current INCOSE certification guidance.

---

## 2. Understanding Life-Cycle Technical Processes

### 2.1 What Is a Process?

A process is a set of related activities used to achieve a defined purpose and produce intended outcomes.

A systems-engineering process may specify:

* Its purpose.
* Activities to perform.
* Inputs and information to consider.
* Outputs and work products.
* Responsibilities and decision authority.
* Criteria for evaluating results.
* Relationships with other processes.

A process is not simply a checklist. It should help the team produce a technically adequate system and credible evidence that the system satisfies its intended needs.

### 2.2 What Are Life-Cycle Technical Processes?

Life-cycle technical processes support the technical definition, realization, evaluation, operation, and retirement of a system.

They help answer questions such as:

* What problem must the system solve?
* Who are its stakeholders?
* What capabilities and constraints are required?
* What architecture can satisfy those requirements?
* How should the architecture be realized?
* Does the implemented system conform to its requirements?
* Does the integrated system satisfy stakeholder needs?
* How will the system be operated, supported, modified, and retired?

These processes are related. Requirements definition influences architecture; architecture influences design; design guides implementation; implementation enables integration and testing; operational experience can generate new needs and requirements.

### 2.3 Technical Processes Are Not Strictly Linear

Although the processes can be shown in an ordered diagram, actual engineering frequently involves iteration.

For example:

1. Requirements analysis reveals an infeasible performance target.
2. System analysis identifies a design trade-off.
3. Architecture definition is revised.
4. Requirements are negotiated or clarified.
5. The design is updated.
6. Verification plans are revised to reflect the approved change.

Iteration is expected when it is controlled and supported by evidence.

### 2.4 Processes, Activities, and Work Products

These terms should not be confused.

* **Process:** A coordinated set of activities serving a purpose.
* **Activity:** A particular type of work performed within a process.
* **Work product:** Information or an artifact produced by work.
* **Deliverable:** A work product or other result formally provided to a customer or stakeholder.
* **Evidence:** Information used to substantiate a claim, decision, or conclusion.

Examples of work products include a stakeholder-needs specification, requirements specification, architecture description, interface definition, analysis report, test procedure, test result, and operational procedure.

A document's existence does not automatically prove technical adequacy. The content must be correct, complete enough for its purpose, consistent, and supported by appropriate review or evidence.

---

## 3. Business or Mission Analysis

### 3.1 Purpose

Business or mission analysis investigates a stakeholder problem, operational opportunity, or mission need and evaluates possible ways to address it.

The objective is to understand the problem before committing prematurely to a particular solution.

The word *business* does not restrict this process to commercial organizations. The same concepts can apply to government, healthcare, infrastructure, research, defense, and other mission-oriented systems.

### 3.2 Typical Activities

Activities may include:

1. Identifying the problem or opportunity.
2. Understanding the operational environment.
3. Identifying relevant stakeholders and affected organizations.
4. Establishing objectives and desired outcomes.
5. Defining operational scenarios and constraints.
6. Developing alternative solution concepts.
7. Evaluating feasibility, risks, benefits, costs, and trade-offs.
8. Recommending a preferred direction or identifying what additional evidence is required.

### 3.3 Problem Definition Versus Solution Definition

A common mistake is to confuse a requested product with the underlying need.

Example:

A hospital requests a mobile application to monitor equipment.

The underlying problem may be that staff cannot reliably identify equipment location and availability. A mobile application is one possible solution, but alternatives could include equipment tags, workflow changes, centralized inventory, or a combination.

Systems engineering first clarifies the need and then evaluates solution alternatives.

### 3.4 Outputs

Potential work products include:

* Problem or opportunity statement.
* Mission analysis.
* Operational concept.
* Stakeholder identification.
* High-level objectives.
* Feasibility and trade-study results.
* Candidate solution concepts.
* Initial risk assessment.
* Recommendation for further development.

The exact artifacts depend on project scope and organizational practice.

### 3.5 Common Failure Modes

* Starting with a preferred solution instead of understanding the problem.
* Ignoring affected stakeholders.
* Treating assumptions as established facts.
* Failing to consider the operational environment.
* Comparing alternatives using inconsistent criteria.
* Selecting a concept without considering life-cycle cost or supportability.

---

## 4. Stakeholder Needs and Requirements Definition

### 4.1 Purpose

Stakeholder needs and requirements definition establishes what relevant stakeholders need from the system and expresses those needs in a form that can guide system development and evaluation.

Stakeholders may include users, operators, maintainers, owners, customers, regulators, support organizations, and members of the public affected by system operation.

### 4.2 Identify Stakeholders and Their Contexts

Different stakeholders can have different goals.

For a transportation ticketing system:

* Passengers need accessible and reliable ticket purchase.
* Operators need service monitoring.
* Finance teams need accurate transaction records.
* Maintenance teams need diagnostics.
* Security teams need controlled access and fraud prevention.
* Regulators may impose accessibility, privacy, or financial requirements.

A system that satisfies one group while ignoring another may fail in operation.

### 4.3 Elicit Needs

Needs can be discovered through:

* Interviews.
* Workshops.
* Observation.
* Surveys.
* Existing-system analysis.
* Operational data.
* Document review.
* Prototypes and demonstrations.
* Scenario analysis.

No single technique is sufficient for every stakeholder or context.

### 4.4 Define Operational Scenarios

Scenarios describe how the system is expected to be used in context.

A scenario can include:

* The initiating event.
* Relevant actors.
* Preconditions.
* Main interactions.
* Alternative paths.
* Failures or abnormal conditions.
* Expected outcomes.

Scenarios help uncover needs that might be missed when stakeholders provide only feature lists.

### 4.5 Transform Needs into Requirements

A stakeholder need may be expressed informally:

> Staff need to locate available equipment quickly.

A derived system requirement might state:

> Under the defined operating conditions, the system shall display the reported location and availability status of registered equipment within five seconds of a valid query.

This is an illustrative requirement. Its timing, operating conditions, data freshness, and measurement method would need stakeholder agreement and technical justification.

A useful requirement should generally be:

* Necessary.
* Clear and unambiguous.
* Feasible.
* Consistent with other requirements.
* Verifiable.
* Traceable to a source or rationale.
* Appropriately bounded.

Avoid vague words such as *fast*, *user-friendly*, *robust*, or *secure* unless they are defined by measurable or otherwise assessable criteria.

### 4.6 Requirements Versus Preferences

Not every stakeholder statement should immediately become a binding requirement.

A statement may represent:

* A mandatory need.
* A desirable feature.
* A constraint.
* An assumption.
* A proposed solution.
* A preference requiring clarification.

The team should record the source, priority, rationale, and disposition of significant statements.

### 4.7 Outputs

Possible work products include:

* Stakeholder needs and requirements.
* Operational scenarios.
* Use cases.
* Stakeholder priorities.
* Constraints and assumptions.
* Acceptance expectations.
* Initial traceability records.
* Requirements validation findings.

### 4.8 Common Failure Modes

* Writing requirements before understanding stakeholder needs.
* Treating a stakeholder's preferred solution as the only possible solution.
* Using unverifiable adjectives.
* Ignoring accessibility, maintenance, safety, security, or abnormal conditions.
* Failing to reconcile conflicting stakeholder expectations.
* Failing to distinguish confirmed requirements from assumptions.

---

## 5. System Requirements Definition

### 5.1 Purpose

System requirements definition translates stakeholder needs and higher-level constraints into a structured set of requirements that define the capabilities, behavior, performance, interfaces, and constraints of the system.

Stakeholder requirements and system requirements are related but are not interchangeable.

Stakeholder requirements describe what stakeholders need from the system in their context. System requirements provide a more precise technical basis for architecture, design, implementation, and evaluation.

### 5.2 Functional Requirements

Functional requirements specify what the system must do.

Examples:

* The system shall authenticate authorized users.
* The system shall record each completed transaction.
* The monitoring system shall generate an alert when a defined threshold condition is met.

Functional requirements should describe required behavior, not unnecessarily dictate the internal design.

### 5.3 Performance Requirements

Performance requirements specify measurable levels of service or capability.

Examples include:

* Response time.
* Throughput.
* Accuracy.
* Availability.
* Capacity.
* Range.
* Latency.
* Power consumption.

A performance requirement needs defined conditions and measurement criteria.

For example, a statement that a server must be "fast" is not sufficiently precise. A requirement specifying a response-time threshold under a defined workload and measurement method is more useful.

### 5.4 Interface Requirements

Interface requirements define interactions between the system and external entities or between its components.

Interfaces may involve:

* Data.
* Mechanical connections.
* Electrical signals.
* Communication protocols.
* Human interaction.
* Environmental conditions.
* Timing and synchronization.

An interface should be defined consistently on both sides. A mismatch in units, protocols, assumptions, or timing can cause integration failure even when individual components work correctly.

### 5.5 Constraint Requirements

Constraints limit the acceptable solution space.

Examples include:

* Required standards or regulations.
* Physical dimensions.
* Available power.
* Budget limits.
* Required technologies.
* Compatibility with existing systems.
* Operating-environment limitations.

Constraints should be recorded with their sources and applicability.

### 5.6 Requirements Analysis

Requirements analysis examines requirements for completeness, consistency, feasibility, allocation, and verifiability.

Questions include:

* Does each requirement have a clear meaning?
* Can it be traced to a legitimate source or rationale?
* Is it achievable within the system's constraints?
* Does it conflict with another requirement?
* Can compliance be demonstrated?
* Is the requirement allocated to the appropriate system element?
* Does it specify a need or unnecessarily impose a design choice?

### 5.7 Requirements Allocation

System-level requirements are allocated to system elements or lower-level subsystems when appropriate.

For example, an overall system requirement for measurement accuracy may lead to allocated requirements for sensor performance, signal processing, calibration, and environmental compensation.

Allocation must consider the behavior of the integrated system. Meeting every component's allocated requirement does not automatically guarantee that the overall system requirement is satisfied.

### 5.8 Requirements Traceability

Traceability links requirements to their sources, related requirements, design elements, and verification evidence.

A simplified relationship is:

Stakeholder Need → System Requirement → Architecture Element → Design or Implementation → Verification Evidence

Traceability helps engineers:

* Understand why a requirement exists.
* Identify affected components when a requirement changes.
* Find requirements with no supporting rationale.
* Identify design elements with no justified purpose.
* Plan verification.
* Evaluate change impacts.

Traceability alone does not prove correctness. A requirement can be fully traced and still be unnecessary, ambiguous, infeasible, or incorrect.

### 5.9 Outputs

Potential work products include:

* System requirements specification.
* Requirements hierarchy.
* Requirement attributes and rationale.
* Allocation records.
* Traceability records.
* Requirements analysis findings.
* Verification strategy or preliminary verification mapping.

---

## 6. Architecture Definition

### 6.1 Purpose

Architecture definition establishes the fundamental organization of a system, including its elements, responsibilities, relationships, interfaces, and relevant views.

Architecture connects requirements to a feasible solution structure.

It is not simply a diagram. A useful architecture description communicates how the system is organized and why that organization can satisfy the required capabilities and constraints.

### 6.2 Architectural Decisions

Architecture definition may address:

* Major system elements.
* Functional responsibilities.
* Allocation of behavior.
* Interfaces and dependencies.
* Data flows.
* Control flows.
* Deployment and physical organization.
* External-system interactions.
* Performance and resilience.
* Security boundaries.
* Growth and upgrade strategies.

Architecture should be developed with the operational environment and life-cycle constraints in mind.

### 6.3 Logical and Physical Views

A logical architecture describes functions, behaviors, or responsibilities without necessarily committing to specific physical components.

A physical architecture describes the elements that realize those responsibilities, such as devices, servers, software services, networks, or mechanical assemblies.

The distinction is useful but not absolute: architecture descriptions may contain multiple complementary views.

Example:

A logical architecture for a monitoring platform may contain sensing, data processing, alerting, storage, and visualization functions. A physical architecture may allocate these functions to wearable devices, an edge gateway, cloud services, and operator dashboards.

### 6.4 Architecture Alternatives and Trade Studies

There may be several viable architectures.

A trade study compares alternatives against defined criteria, such as:

* Performance.
* Cost.
* Reliability.
* Safety.
* Security.
* Maintainability.
* Scalability.
* Complexity.
* Technical risk.
* Schedule.
* Life-cycle cost.

Criteria should be relevant to the mission, and assumptions should be explicit. A weighted score is useful only if the criteria, weights, and evidence are credible.

### 6.5 Architecture Evaluation

Architecture evaluation asks whether the proposed organization can plausibly satisfy the requirements and constraints.

Methods may include:

* Analysis.
* Modeling and simulation.
* Prototyping.
* Interface analysis.
* Performance budgets.
* Reliability analysis.
* Security analysis.
* Hazard analysis.
* Technical reviews.

Important architectural risks should be investigated before they become expensive to correct.

### 6.6 Outputs

Potential work products include:

* Architecture description.
* System-element definitions.
* Functional and physical views.
* Interface definitions.
* Architecture decision records.
* Trade-study results.
* Allocation of requirements.
* Architectural risk and feasibility findings.

---

## 7. Design Definition

### 7.1 Purpose

Design definition develops sufficiently detailed descriptions of system elements and interfaces to support implementation, integration, and evaluation.

Architecture establishes the overall organization; design definition elaborates how selected elements will be realized.

The boundary between architecture and design varies by system and organization. They should nevertheless remain consistent with each other.

### 7.2 Design Decisions

Design work may define:

* Component behavior.
* Software modules.
* Database structures.
* Mechanical and electrical details.
* Network configuration.
* Data schemas.
* Algorithms.
* Interface specifications.
* Manufacturing information.
* Installation and configuration procedures.

### 7.3 Design for the Whole Life Cycle

Design decisions should consider more than immediate functionality.

Important concerns include:

* Reliability.
* Availability.
* Maintainability.
* Testability.
* Safety.
* Cybersecurity.
* Usability.
* Accessibility.
* Manufacturability.
* Environmental impact.
* Energy efficiency.
* Upgradeability.
* Supportability.
* Disposal.

For example, a modular power supply may increase initial cost but simplify replacement and reduce future downtime.

### 7.4 Design Reviews

Design reviews assess whether the design is sufficiently mature and consistent for the next activity.

A review may consider:

* Requirement coverage.
* Interface completeness.
* Technical feasibility.
* Risk status.
* Analysis results.
* Verification plans.
* Manufacturing or deployment readiness.
* Open issues and assumptions.

Review completion should be based on agreed criteria, not simply on the existence of a presentation.

### 7.5 Outputs

Potential work products include:

* Detailed design descriptions.
* Component specifications.
* Interface control information.
* Software and hardware design artifacts.
* Manufacturing or deployment instructions.
* Updated requirements allocation.
* Design analyses and review findings.
* Updated verification information.

---

## 8. System Analysis

### 8.1 Purpose

System analysis provides evidence to support technical decisions and evaluate system properties.

It may be used throughout the life cycle, from concept selection to operational problem investigation.

### 8.2 Types of Analysis

Examples include:

* Performance analysis.
* Reliability and availability analysis.
* Safety and hazard analysis.
* Security analysis.
* Cost and life-cycle cost analysis.
* Capacity and throughput analysis.
* Trade-off analysis.
* Sensitivity analysis.
* Failure analysis.
* Modeling and simulation.
* Human-factors analysis.
* Environmental impact analysis.

### 8.3 Trade-Off Analysis

A trade-off analysis compares alternatives that offer different benefits and limitations.

Example:

A network architecture might trade initial cost against resilience, operational complexity, and recovery time.

A sound analysis should:

1. Define the decision to be made.
2. Establish feasible alternatives.
3. Identify relevant criteria.
4. Record assumptions and constraints.
5. Collect or estimate evidence.
6. Evaluate alternatives consistently.
7. Assess uncertainty and sensitivity.
8. Document the recommendation and rationale.

The highest score in a numerical model does not automatically identify the best solution if important criteria are missing or the inputs are unreliable.

### 8.4 Sensitivity and Uncertainty

Sensitivity analysis examines how changes in inputs affect results.

Uncertainty analysis considers how uncertain assumptions, measurements, or models affect conclusions.

For example, if a data center's future workload is uncertain, the team can assess how different demand scenarios affect capacity and cost.

### 8.5 Outputs

Potential work products include:

* Analysis reports.
* Model and simulation results.
* Trade-study recommendations.
* Performance predictions.
* Reliability or safety analyses.
* Cost estimates.
* Risk findings.
* Decision rationale.

---

## 9. Implementation

### 9.1 Purpose

Implementation realizes a system element in accordance with its approved requirements and design information.

Depending on the system, implementation may involve:

* Software development.
* Hardware fabrication.
* Component procurement.
* Manufacturing.
* Configuration.
* Data preparation.
* Model training.
* Service deployment.
* Installation of equipment.

### 9.2 Implementation Is More Than Coding

For a software-intensive system, implementation includes coding, configuration, dependency management, build processes, and appropriate developer testing.

For a hardware system, it may include manufacturing, assembly, calibration, and inspection.

For a data-intensive or AI-enabled system, implementation may also involve data pipelines, model artifacts, inference services, monitoring, and controlled deployment.

The activities depend on the system and its architecture.

### 9.3 Implementation Controls

Useful controls may include:

* Approved design information.
* Coding or manufacturing standards.
* Version control.
* Build reproducibility.
* Supplier quality controls.
* Unit-level checks.
* Configuration identification.
* Defect tracking.
* Security practices.
* Implementation reviews.

### 9.4 Outputs

Potential work products include:

* Implemented system elements.
* Source code or compiled software.
* Manufactured components.
* Configured infrastructure.
* Build and deployment records.
* Unit-level test results.
* Implementation verification records.
* Updated configuration information.

Implementation alone does not demonstrate that the complete system satisfies its requirements.

---

## 10. Integration

### 10.1 Purpose

Integration combines system elements into a larger system or subsystem while ensuring that their interactions are consistent with the architecture and interface definitions.

Integration may occur at multiple levels, from components to subsystems to the complete system.

### 10.2 Why Integration Fails

Elements can work individually and still fail when combined.

Common causes include:

* Incompatible interfaces.
* Different assumptions about units or data formats.
* Protocol mismatches.
* Incorrect timing.
* Version incompatibility.
* Capacity limitations.
* Unexpected dependencies.
* Resource contention.
* Inconsistent configuration.
* Fault propagation between components.

### 10.3 Integration Strategy

A project should define an integration strategy appropriate to its architecture and risk.

It may specify:

* Integration sequence.
* Required equipment and environments.
* Interface test procedures.
* Dependencies and prerequisites.
* Configuration requirements.
* Test data.
* Expected results.
* Defect handling.
* Entry and exit criteria.

Incremental integration can reveal interface defects earlier than a single late integration event.

### 10.4 Example

A patient-monitoring device, gateway, backend API, database, and dashboard are tested individually.

During integration, the team discovers that the device sends timestamps in one format while the backend interprets them differently. The resulting alert sequence is incorrect even though each component passes its individual tests.

The defect illustrates why interface definitions and end-to-end integration are essential.

### 10.5 Outputs

Potential work products include:

* Integrated system or subsystem.
* Integration procedures and results.
* Interface test results.
* Defect reports.
* Updated configuration records.
* Integration readiness or completion findings.

---

## 11. Verification

### 11.1 Purpose

Verification determines whether a system element or system satisfies its specified requirements.

The central question is:

**Did we build the system correctly against its requirements?**

Verification is requirements-focused. It evaluates compliance with the applicable specification or defined acceptance criteria.

### 11.2 Verification Methods

Common methods include:

**Test:** Execute the item under specified conditions and observe results.

**Analysis:** Use calculations, models, or other analytical methods to determine whether a requirement is satisfied.

**Inspection:** Examine the item or its characteristics to assess conformance.

**Demonstration:** Operate or exercise the item to show that a capability is present, often without the detailed instrumentation associated with a formal test.

The exact method names and classifications can vary by standard or organization. The method selected must be suitable for the requirement and the strength of evidence needed.

### 11.3 Examples

| Requirement                                                                 | Possible verification method |
| --------------------------------------------------------------------------- | ---------------------------- |
| Enclosure dimensions are within specified limits                            | Inspection or measurement    |
| API response time remains below a defined threshold under a stated workload | Test                         |
| Structural load capability satisfies a specified limit                      | Test and/or analysis         |
| A backup process produces a recoverable backup                              | Test                         |
| A connector uses a specified pin arrangement                                | Inspection                   |
| A system supports a specified calculation under defined conditions          | Test or analysis             |

### 11.4 Verification Planning

Verification planning should begin while requirements and design are being defined.

For each requirement, establish:

* The requirement identifier.
* The intended verification method.
* The conditions and equipment needed.
* The acceptance criteria.
* The required evidence.
* The responsible organization or role.
* Dependencies and prerequisites.

A requirement that cannot be verified may be ambiguous, poorly formulated, or in need of a different evaluation approach.

### 11.5 Verification Is Not Only Final Testing

Verification can be applied to requirements, designs, components, software modules, subsystems, and the integrated system.

Reviews and analyses may identify defects long before final system testing.

### 11.6 Outputs

Potential work products include:

* Verification plans.
* Procedures and test cases.
* Analysis and inspection records.
* Test results.
* Nonconformance reports.
* Verification status and closure evidence.

---

## 12. Validation

### 12.1 Purpose

Validation determines whether the system, when used in its intended environment, satisfies stakeholder needs and supports its intended use.

The central question is:

**Did we build the right system for the intended need?**

Validation considers operational context, stakeholders, mission outcomes, and intended use. It is not limited to checking individual technical requirements.

### 12.2 Validation Examples

For a hospital monitoring system, validation may assess whether:

* Clinicians can interpret the displayed information.
* Alerts support the intended workflow.
* The system can be used under realistic operating conditions.
* The solution addresses the original monitoring problem.
* Operational limitations are understood and acceptable to authorized stakeholders.

A system might pass all component-level verification tests yet fail validation because it creates excessive workload or does not fit the real operational process.

### 12.3 Validation Methods

Depending on the system, validation may use:

* Operational trials.
* Representative user evaluations.
* Simulations.
* Scenario-based assessments.
* End-to-end demonstrations.
* Stakeholder acceptance activities.
* Evaluation against mission or business outcomes.

The environment and evidence should be representative enough for the conclusion being made.

### 12.4 Verification Versus Validation

| Aspect           | Verification                                       | Validation                                                               |
| ---------------- | -------------------------------------------------- | ------------------------------------------------------------------------ |
| Main question    | Does it satisfy specified requirements?            | Does it satisfy stakeholder needs and intended use?                      |
| Main reference   | Requirements and specifications                    | Stakeholder needs, mission, and operational context                      |
| Typical emphasis | Conformance                                        | Suitability and effectiveness in context                                 |
| Example          | Confirming that a display meets specified accuracy | Confirming that operators can use the display effectively for their task |

The two activities complement each other. Neither replaces the other.

### 12.5 Outputs

Potential work products include:

* Validation plans and scenarios.
* Operational evaluation results.
* Stakeholder feedback.
* Validation findings.
* Acceptance recommendations.
* Identified limitations or unmet needs.

---

## 13. Transition

### 13.1 Purpose

Transition moves a system or system element into its intended operational environment or to the receiving organization.

A technically complete system may not be ready for operational use if users, infrastructure, procedures, support, or authorization are not ready.

### 13.2 Transition Activities

Depending on the system, transition may involve:

* Installation and deployment.
* Data migration.
* System configuration.
* User training.
* Operator and maintainer training.
* Operational documentation.
* Support arrangements.
* Acceptance activities.
* Cutover planning.
* Rollback planning.
* Confirmation of operational readiness.

### 13.3 Example: Replacing a Business System

A company is replacing its legacy inventory platform.

Transition planning must address:

* Migrating and validating inventory data.
* Training staff.
* Establishing user permissions.
* Integrating with warehouse equipment.
* Planning downtime.
* Defining rollback conditions.
* Confirming support coverage.

A successful software deployment is not sufficient if inventory records are inaccurate or warehouse staff cannot perform their jobs.

### 13.4 Outputs

Potential work products include:

* Deployment records.
* Installation and configuration records.
* Training records.
* Operational procedures.
* Acceptance evidence.
* Readiness findings.
* Data migration and reconciliation results.

---

## 14. Operation

### 14.1 Purpose

Operation uses the system to provide its intended services or mission outcomes.

Operations also generate evidence about real-world performance, reliability, user behavior, and emerging needs.

### 14.2 Operational Activities

Activities may include:

* Operating the system.
* Monitoring performance and availability.
* Managing access.
* Handling incidents.
* Applying operational procedures.
* Recording usage and service outcomes.
* Monitoring safety and security conditions.
* Reporting defects and improvement opportunities.
* Coordinating operational support.

### 14.3 Operational Feedback

Actual operating conditions may differ from design assumptions.

For example, a network may experience more peak traffic than anticipated. Operational monitoring can identify capacity problems and provide evidence for architectural changes.

Feedback should be analyzed and routed through appropriate processes rather than converted directly into uncontrolled modifications.

### 14.4 Outputs

Potential work products include:

* Operational records.
* Performance and availability data.
* Incident reports.
* User feedback.
* Maintenance requests.
* Operational risk findings.
* Proposed improvements and change requests.

---

## 15. Maintenance

### 15.1 Purpose

Maintenance sustains or restores the system's ability to perform its required functions throughout its service life.

Maintenance includes more than replacing broken hardware. It can involve software corrections, security updates, calibration, configuration changes, component replacement, and other controlled activities.

### 15.2 Maintenance Categories

**Corrective maintenance:** Addresses a detected fault or deficiency.

**Preventive maintenance:** Reduces the likelihood of future failures through planned activities.

**Condition-based maintenance:** Uses observed condition or measurements to determine when maintenance is needed.

**Adaptive maintenance:** Changes a system to accommodate changes in its environment, interfaces, or supporting technology.

**Perfective maintenance:** Improves performance, maintainability, or other qualities. Exact classification terminology can vary by discipline.

These categories are useful for understanding maintenance objectives; an organization's formal taxonomy may differ.

### 15.3 Maintenance Planning

A maintainable system may require:

* Diagnostic capability.
* Replaceable modules.
* Access to components.
* Spare parts.
* Repair documentation.
* Software update mechanisms.
* Configuration records.
* Trained personnel.
* Test equipment.
* Defined restoration and acceptance criteria.

### 15.4 Changes During Maintenance

A maintenance change may affect safety, performance, cybersecurity, interfaces, or compliance.

Changes should be evaluated and controlled. Appropriate regression verification and, when necessary, validation should be performed before returning the system to service.

### 15.5 Outputs

Potential work products include:

* Maintenance plans and procedures.
* Repair records.
* Updated configurations.
* Corrective-action records.
* Replacement and calibration records.
* Regression test results.
* Updated support documentation.

---

## 16. Disposal

### 16.1 Purpose

Disposal removes a system or system element from service and manages its final disposition in accordance with applicable obligations.

Disposal is not simply switching off the system. It includes the technical, operational, information-security, environmental, and organizational tasks required to conclude its use responsibly.

### 16.2 Disposal Considerations

Relevant considerations may include:

* Safe removal from service.
* Continuity of essential services.
* Data backup and retention.
* Secure data sanitization.
* Removal of credentials and access.
* Environmental handling of components.
* Recycling and material recovery.
* Hazardous-substance management.
* Transfer or termination of support contracts.
* Preservation of required technical records.
* Verification that disposal actions are complete.

### 16.3 Example: Retiring a Server

A server is replaced by a new platform.

The disposal process may require the team to:

1. Confirm that dependent services have migrated.
2. Validate the migrated data.
3. Obtain authorization to decommission the server.
4. Remove it from production and monitoring systems.
5. Revoke credentials and certificates.
6. Sanitize storage media according to policy.
7. Update asset and configuration records.
8. Reuse, recycle, or dispose of hardware through approved channels.
9. Retain the records required by policy or law.

### 16.4 Outputs

Potential work products include:

* Decommissioning plans and records.
* Data sanitization evidence.
* Asset disposition records.
* Service termination records.
* Environmental handling records.
* Final configuration updates.
* Closure of remaining obligations.

---

## 17. Cross-Process Relationships

Technical processes should work together as a coordinated system of engineering activities.

### 17.1 From Need to Evidence

A simplified chain is:

```text
Business or Mission Need
          |
          v
Stakeholder Needs Definition
          |
          v
System Requirements Definition
          |
          v
Architecture Definition
          |
          v
Design Definition
          |
          v
Implementation
          |
          v
Integration
          |
          v
Verification
          |
          v
Validation
          |
          v
Transition and Operation
          |
          v
Maintenance and Disposal
```

This diagram is a learning aid, not a mandatory one-way sequence. Analysis, verification planning, stakeholder feedback, and other activities may occur throughout development. Iteration can return the team to earlier processes.

### 17.2 Traceability Across Processes

Consider a requirement that the system must retain operational data for a specified period.

The team should be able to identify:

* The stakeholder need or regulation behind the requirement.
* The system requirement that defines retention.
* The architecture elements responsible for storage and retrieval.
* The design and configuration implementing the capability.
* The verification evidence demonstrating compliance.
* The operational procedures controlling retention.
* The disposal procedures handling data at the end of its required life.

This is an example of end-to-end engineering traceability.

### 17.3 Interface Management

Interfaces connect system elements and external systems.

Interface management should define and control relevant characteristics, including:

* Physical or logical connections.
* Data formats and units.
* Protocols.
* Timing.
* Error handling.
* Performance constraints.
* Security requirements.
* Ownership and responsibilities.

Interfaces should be coordinated across architecture, design, implementation, integration, verification, and maintenance.

### 17.4 Risk Management

Risk analysis supports technical decisions throughout the life cycle.

Examples:

* Mission analysis identifies uncertainty in operational demand.
* Requirements analysis identifies an unachievable performance target.
* Architecture analysis reveals a single point of failure.
* Design analysis identifies overheating.
* Integration exposes protocol incompatibility.
* Verification reveals an unmet requirement.
* Operation reveals unexpected failure patterns.
* Maintenance identifies obsolete components.

Risk information should be updated as evidence changes.

### 17.5 Configuration and Change Management

Configuration management supports consistency between approved requirements, architecture, design, implementation, and test evidence.

A change to one system element may affect several other artifacts. Impact analysis should identify affected requirements, interfaces, components, procedures, and verification results.

For example, changing a communication protocol can require updates to architecture, interface definitions, software, integration tests, operational procedures, and support documentation.

### 17.6 Information and Evidence Management

Engineering decisions depend on trustworthy information.

Important practices include:

* Identifying authoritative artifacts.
* Recording assumptions and rationale.
* Preserving test conditions and results.
* Linking evidence to requirements.
* Controlling versions.
* Recording unresolved issues.
* Maintaining records needed for operation and support.

The amount of documentation should be tailored to system complexity, risk, contractual obligations, and the consequences of failure.

---

## 18. Practical Case Study: Enterprise Network Upgrade

### Scenario

An organization must replace an aging network supporting offices, servers, voice services, and business applications. The system includes routers, switches, wireless access points, firewalls, servers, cabling, monitoring tools, and operational procedures.

### Step 1: Business or Mission Analysis

The team investigates outages, bandwidth limitations, business continuity needs, future growth, and operating costs.

It compares alternatives such as upgrading the existing topology, introducing redundant network paths, or segmenting the network into separate security and operational zones.

**Output:** An agreed problem statement, objectives, constraints, candidate concepts, and a recommended direction.

### Step 2: Stakeholder Needs Definition

Users need reliable access to applications. Administrators need manageable configurations and monitoring. Security teams need controlled access and segmentation. Management needs a solution that fits budget and business continuity constraints.

**Output:** Prioritized stakeholder needs and operational scenarios.

### Step 3: System Requirements Definition

The team defines measurable requirements for availability, throughput, segmentation, authentication, monitoring, recoverability, and compatibility.

An illustrative requirement might state:

> The network shall restore connectivity for designated critical services within the approved recovery-time objective after the defined single-link failure.

The recovery-time objective and applicable failure conditions must be established and agreed before verification.

**Output:** A reviewed system requirements specification and initial verification mapping.

### Step 4: Architecture Definition

The team defines network zones, routing boundaries, redundancy, management access, external connections, and relationships between network elements.

Architecture alternatives are evaluated against cost, availability, security, complexity, and maintainability.

**Output:** Architecture views, interface definitions, allocation decisions, and trade-study results.

### Step 5: Design Definition

The team develops VLAN plans, IP addressing, routing configurations, firewall policies, hardware specifications, cable plans, monitoring configuration, and migration procedures.

**Output:** Detailed designs, configuration specifications, and test plans.

### Step 6: System Analysis

Capacity analysis estimates expected and peak traffic. Resilience analysis identifies single points of failure. Security analysis evaluates segmentation and management access. Cost analysis compares initial and long-term operating costs.

**Output:** Analysis reports, risk findings, and justified design decisions.

### Step 7: Implementation

Hardware is procured, configurations are prepared, monitoring systems are configured, and the deployment environment is established.

**Output:** Configured and identified network elements with implementation records.

### Step 8: Integration

Switches, routers, firewalls, servers, wireless services, and monitoring tools are connected in a controlled test environment or staged deployment.

The team checks routing, VLAN connectivity, interface compatibility, authentication, and monitoring behavior.

**Output:** An integrated network with recorded integration results.

### Step 9: Verification

The team checks approved requirements through inspection, analysis, demonstration, and testing.

Examples include testing segmentation rules, measuring throughput under specified conditions, and demonstrating failover behavior.

**Output:** Requirement-linked verification evidence and records of unresolved nonconformances.

### Step 10: Validation

Representative users and service owners evaluate whether the network supports actual operational needs. Critical applications and workflows are tested under representative conditions.

**Output:** Validation findings and acceptance recommendations.

### Step 11: Transition

The team executes a staged migration with approved maintenance windows, communication plans, rollback criteria, configuration backups, and post-change checks.

**Output:** Deployment records, readiness confirmation, and updated operational documentation.

### Step 12: Operation and Maintenance

Monitoring, incident response, configuration backup, patching, capacity management, and change control become part of normal operations.

Operational trends inform future improvements.

**Output:** Operational evidence, maintenance records, and approved change requests.

### Step 13: Disposal

Legacy equipment is removed from service after dependencies are resolved. Configurations and sensitive information are handled according to organizational policy, and asset records are updated.

**Output:** Decommissioning records and final asset disposition evidence.

### Case Study Lessons

* Each process has a distinct purpose, but its outputs support other processes.
* Requirements should be measurable and linked to verification evidence.
* Integration defects often arise at interfaces.
* Verification does not replace validation with actual users and workflows.
* Transition readiness includes people, procedures, and infrastructure.
* Operational and maintenance processes are part of the system life cycle.
* Disposal requires planning and controlled execution.

---

## 19. Exercises

### Exercise 1: Distinguish the Processes

A customer reports that staff cannot locate available equipment quickly. The engineering team immediately starts designing a mobile application.

**Question:** Which process should be strengthened before committing to the application design?

**Suggested answer:** Business or mission analysis should clarify the underlying problem, operational environment, desired outcomes, and alternative concepts. Stakeholder needs definition should then establish what affected users and organizations require.

### Exercise 2: Improve a Requirement

Consider this requirement:

> The system shall be highly reliable and easy to use.

**Question:** Identify two problems and propose a way to improve it.

**Suggested answer:** "Highly reliable" and "easy to use" are ambiguous and lack defined evaluation criteria. The team should establish measurable reliability targets and usability criteria appropriate to the operating context. The exact targets must be justified and agreed with stakeholders.

### Exercise 3: Identify the Correct Process

The team has completed component testing but has not connected the components to one another.

**Question:** Which process remains particularly important before evaluating the complete system?

**Suggested answer:** Integration is required to combine the components and assess their interactions. System-level verification and validation may follow or overlap according to the test strategy.

### Exercise 4: Verification or Validation?

A system meets its specified response-time and capacity requirements, but operators cannot complete the intended workflow efficiently.

**Question:** What does this suggest?

**Suggested answer:** The system may satisfy selected requirements through verification but fail to meet stakeholder needs in actual use. Validation should evaluate the workflow and intended operational outcomes. The findings may require changes to requirements, architecture, design, or procedures.

### Exercise 5: Architecture or Design?

The team decides that a monitoring system will separate sensing, data processing, alerting, and storage responsibilities. Later, it defines the database schema and specific API payload fields.

**Question:** Which work is primarily architecture definition, and which is primarily design definition?

**Suggested answer:** Defining major responsibilities and their relationships is primarily architecture definition. Specifying the database schema and detailed API payloads is primarily design definition. In practice, the boundary depends on system scale and organizational conventions.

### Exercise 6: Requirements Traceability

A system requirement has no identified source, rationale, or stakeholder need.

**Question:** What should the team do?

**Suggested answer:** Investigate the requirement's origin and justification. Determine whether it is a legitimate constraint or derived technical requirement, document the rationale, or revise or remove it through the approved process if it is unnecessary. Missing traceability does not automatically prove the requirement is invalid, but it needs resolution.

### Exercise 7: Integration Failure

Two components pass their individual tests but exchange data incorrectly because they interpret a measurement in different units.

**Question:** What is the main engineering lesson?

**Suggested answer:** Component-level success does not guarantee system-level success. Interface definitions, unit conventions, integration testing, and configuration control are essential.

### Exercise 8: Transition Readiness

A replacement system has passed its technical tests, but users are untrained and the support team has no approved operating procedures.

**Question:** Is the system necessarily ready for operational transition?

**Suggested answer:** No. Transition readiness also includes user training, operational procedures, support arrangements, configuration, and acceptance conditions. The team should address these gaps before authorizing the transition.

### Exercise 9: Maintenance Change

A security patch modifies a service that communicates with three other subsystems.

**Question:** What should happen before the patched service is returned to operation?

**Suggested answer:** Assess the change's impact, control the configuration, perform appropriate testing including regression and interface tests, evaluate security and operational effects, and obtain required approval. Validation may also be necessary if intended use or stakeholder outcomes are affected.

### Exercise 10: Disposal

An organization is retiring a server that stores confidential records.

**Question:** Name four important disposal actions.

**Suggested answer:** Confirm service migration, revoke credentials, sanitize storage media according to policy, update asset and configuration records, retain required records, and arrange authorized reuse or disposal.

---

## 20. CSEP-Style Practice Questions

These are original study questions, not official INCOSE examination questions.

### Question 1

What is the principal purpose of business or mission analysis?

A. To write source code before defining the problem.
B. To understand a problem or opportunity and evaluate potential solution concepts.
C. To perform final acceptance testing only.
D. To dispose of the system.

**Correct answer: B.**

**Explanation:** Business or mission analysis clarifies the need, context, objectives, constraints, and alternatives before excessive commitment to a solution.

### Question 2

What is the primary purpose of stakeholder needs and requirements definition?

A. To select all hardware models before understanding users.
B. To establish what relevant stakeholders need from the system and express those needs appropriately.
C. To replace system requirements with informal preferences.
D. To verify the finished system without requirements.

**Correct answer: B.**

**Explanation:** This process identifies and analyzes stakeholder needs and establishes a suitable basis for system development and evaluation.

### Question 3

Which statement best describes a good system requirement?

A. It is intentionally vague so every implementation can claim compliance.
B. It includes as much detailed design as possible regardless of need.
C. It is sufficiently clear, feasible, necessary, and verifiable for its intended purpose.
D. It does not need a source or rationale.

**Correct answer: C.**

**Explanation:** Requirements should be meaningful and capable of supporting implementation and objective evaluation.

### Question 4

What is the primary purpose of architecture definition?

A. To establish the system's fundamental organization, elements, relationships, and interfaces.
B. To replace all detailed design.
C. To produce only a user manual.
D. To close all operational incidents.

**Correct answer: A.**

**Explanation:** Architecture provides the organizing structure that connects requirements with a feasible system solution.

### Question 5

A design team compares two architectures using performance, maintainability, cost, and resilience criteria. Which activity does this most directly represent?

A. Disposal
B. Trade-off analysis supporting architecture definition
C. User training
D. Final decommissioning

**Correct answer: B.**

**Explanation:** Trade-off analysis compares alternatives against relevant criteria to support a justified technical decision.

### Question 6

Why is integration required when individual components have already passed their tests?

A. Individual testing always proves complete-system compliance.
B. Integration is unnecessary if components come from approved suppliers.
C. Component interactions can introduce failures that are not observable in isolated testing.
D. Integration replaces requirements definition.

**Correct answer: C.**

**Explanation:** Interface mismatches, timing problems, configuration differences, and resource interactions can emerge only when elements are combined.

### Question 7

Which statement most accurately distinguishes verification from validation?

A. Verification concerns requirements conformance; validation concerns stakeholder needs and intended use.
B. Verification is only for software, while validation is only for hardware.
C. Validation always occurs before any system requirements are written.
D. The terms describe exactly the same activity in every context.

**Correct answer: A.**

**Explanation:** Verification and validation have complementary purposes. Both are important to establishing system suitability.

### Question 8

A new system passes technical testing, but data migration and user training are incomplete. What is the most relevant concern?

A. The architecture must automatically be discarded.
B. Transition readiness is incomplete.
C. Disposal must begin immediately.
D. Requirements no longer apply.

**Correct answer: B.**

**Explanation:** Transition includes the arrangements needed to move the system into its intended operational environment, not just technical testing.

### Question 9

A maintenance change affects an interface that has already been verified. What should the engineering team do?

A. Assume the previous test evidence remains sufficient regardless of the change.
B. Delete the original requirement.
C. Assess the impact, control the change, and determine the necessary regression and interface verification.
D. Stop maintaining the system permanently.

**Correct answer: C.**

**Explanation:** Changes can invalidate previous evidence. The team should assess affected requirements and interfaces and perform appropriate evaluation.

### Question 10

Why should disposal include information-security and configuration activities?

A. Retired systems never contain sensitive information.
B. Asset records are irrelevant once a system is switched off.
C. Retirement can leave data, credentials, dependencies, and assets that require controlled handling.
D. Disposal is only a purchasing activity.

**Correct answer: C.**

**Explanation:** Responsible disposal addresses information, security, operational, environmental, and asset-management obligations.

---

## 21. Revision Notes

### Process Purpose

* **Business or mission analysis:** Understand the problem or opportunity and evaluate possible solution concepts.
* **Stakeholder needs and requirements definition:** Establish stakeholder needs and appropriate stakeholder-level requirements.
* **System requirements definition:** Specify the system's required capabilities, behavior, performance, interfaces, and constraints.
* **Architecture definition:** Establish the system's fundamental organization and relationships.
* **Design definition:** Develop detailed descriptions sufficient to implement and evaluate system elements.
* **System analysis:** Produce evidence to support technical decisions and evaluate system properties.
* **Implementation:** Realize system elements according to approved requirements and design information.
* **Integration:** Combine elements and evaluate their interactions.
* **Verification:** Determine whether the system or element satisfies its specified requirements.
* **Validation:** Determine whether the system satisfies stakeholder needs and intended use.
* **Transition:** Move the system into its intended operational environment.
* **Operation:** Use the system to deliver its intended service or mission.
* **Maintenance:** Sustain or restore required capability throughout the service life.
* **Disposal:** Remove the system from service and manage its final disposition.

### Key Relationships

* Requirements should be connected to stakeholder needs, rationale, design decisions, and evaluation evidence.
* Architecture connects system requirements with the organization of the solution.
* Design elaborates the selected architecture into implementation-level information.
* System analysis supports decisions across multiple technical processes.
* Integration addresses interactions between elements.
* Verification addresses conformance to specified requirements.
* Validation addresses stakeholder needs and intended use.
* Transition readiness includes operational procedures, people, infrastructure, and support.
* Maintenance changes should be controlled and evaluated.
* Disposal includes technical, security, environmental, and asset-management concerns.
* Processes can overlap and iterate; a process diagram should not be mistaken for a mandatory one-way sequence.
* Traceability is valuable, but traceability alone does not prove that a requirement is correct or necessary.
* The exact process terminology and expected examination scope should be checked against the current standard and certification guidance.

---

## 22. References and Further Reading

Use the editions and resources specified by the current INCOSE certification guidance.

1. **INCOSE Systems Engineering Handbook** — technical processes, process relationships, requirements, architecture, design, integration, verification, validation, and life-cycle application.
2. **ISO/IEC/IEEE 15288, Systems and software engineering — System life cycle processes** — reference framework for system life-cycle processes and their application.
3. **INCOSE Certification Program** — current certification requirements, application instructions, and exam guidance: https://www.incose.org/certification
4. **NASA Systems Engineering Handbook (NASA/SP-2016-6105 Rev 2)** — practical guidance on requirements, architecture, design, technical management, integration, verification, validation, and reviews: https://www.nasa.gov/reference/systems-engineering-handbook/
5. **NASA Systems Engineering resources** — additional systems-engineering guidance and technical references: https://www.nasa.gov/

### Study Guidance

For certification preparation, compare the definitions and process relationships in this document with the current INCOSE Handbook and the applicable edition of ISO/IEC/IEEE 15288. Pay particular attention to the distinctions between stakeholder needs and system requirements, architecture and design, integration and verification, and verification and validation. Treat the examples as learning aids rather than authoritative definitions of the certification examination scope.
