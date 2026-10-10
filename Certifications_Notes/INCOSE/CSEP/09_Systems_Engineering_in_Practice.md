# 09 — Systems Engineering in Practice

**Certification Track:** INCOSE CSEP Preparation
**Filename:** `09_Systems_Engineering_in_Practice.md`
**Purpose:** Apply systems-engineering principles, processes, and technical management practices to real projects across the system life cycle.

> **Study note:** This is an independent study resource. Practice questions are original and are not official INCOSE examination questions. Use the edition of the INCOSE Systems Engineering Handbook and ISO/IEC/IEEE 15288 specified in your CSEP preparation materials.

---

## 1. Learning Objectives

By the end of this module, you should be able to:

1. Explain how systems engineering is applied in real projects.
2. Integrate stakeholder needs, requirements, architecture, design, implementation, verification, validation, and transition.
3. Understand the systems engineer's role within a multidisciplinary team.
4. Apply systems thinking to complex interactions and emergent behavior.
5. Coordinate technical decisions with project management.
6. Manage requirements, interfaces, risks, configuration, and technical evidence.
7. Recognize common systems-engineering failure patterns.
8. Apply systems engineering to software-intensive and physical systems.
9. Explain how technical decisions affect the complete system life cycle.
10. Evaluate a project scenario and recommend appropriate engineering actions.

## 2. Systems Engineering in the Real World

Systems engineering is an interdisciplinary approach used to develop, operate, maintain, and retire systems that satisfy stakeholder needs within technical, economic, schedule, regulatory, and operational constraints.

In practice, systems engineering is not a single document, software tool, job title, or design phase. It coordinates multiple disciplines so that the complete system achieves its intended purpose.

A project may involve:

* Mechanical engineering.
* Electrical and electronic engineering.
* Software engineering.
* Data engineering.
* Human factors.
* Cybersecurity.
* Manufacturing.
* Operations and maintenance.
* Safety and reliability.
* Procurement and supplier management.
* Test and evaluation.
* Project and program management.

Each discipline may produce a locally correct solution that still causes problems when integrated into the whole system.

**The central practical responsibility of systems engineering is to ensure that the parts work together to meet the system's overall objectives.**

### 2.1 Example: Warehouse automation

A warehouse automation system includes autonomous robots, charging stations, sensors, warehouse-management software, communication networks, operators, and maintenance processes.

Optimizing robot speed alone may increase collision risk or congestion. Increasing the number of robots may overload the network or warehouse-management system. Improving battery capacity may increase vehicle mass and affect payload.

Systems engineering evaluates these interactions and balances competing requirements across the complete operational environment.

## 3. The Systems Engineering Life Cycle in Practice

The exact life-cycle model depends on the project, but practical systems engineering commonly includes the following activities.

### 3.1 Understand the need

Determine the problem to solve before committing to a solution.

Questions include:

* What operational problem exists?
* Who experiences the problem?
* What outcomes are required?
* What happens if the system is not developed?
* What constraints already exist?
* Which stakeholders can approve or reject the solution?
* How will success be measured?

A poorly understood need can lead to a technically impressive but operationally irrelevant product.

### 3.2 Define the system boundary

Identify what is inside the system and what remains external.

The system boundary should identify:

* Included components.
* External systems.
* Users and operators.
* Environmental conditions.
* Interfaces.
* Organizational processes.
* Assumptions and dependencies.

Boundary definition prevents teams from overlooking responsibilities at the edges of the system.

For example, a cloud application may depend on identity services, network connectivity, data sources, and human procedures. These dependencies should be considered even when the project does not own them.

### 3.3 Develop stakeholder needs and requirements

Stakeholder needs express desired outcomes. Requirements translate those needs into clear, assessable statements.

Good requirements are generally:

* Necessary.
* Clear.
* Feasible.
* Consistent.
* Verifiable.
* Traceable.
* Appropriately allocated to system elements.

A requirement such as "the system should be easy to use" is difficult to verify without additional criteria.

A better approach may define task-completion rates, error rates, training time, or usability-test conditions, based on the stakeholders' actual needs.

### 3.4 Develop and evaluate architecture

Architecture describes the system's major elements, their relationships, interfaces, and governing design decisions.

In practice, architects and systems engineers consider:

* Functional allocation.
* Performance.
* Reliability and availability.
* Safety and security.
* Interfaces.
* Modularity.
* Maintainability.
* Scalability.
* Cost.
* Technology constraints.
* Future upgrades.

Architecture decisions should be assessed against multiple stakeholder concerns rather than a single preferred technical attribute.

### 3.5 Implement and integrate

Implementation produces the system elements, which may include hardware, software, data, procedures, facilities, and trained personnel.

Integration combines these elements and checks that they work together as intended.

Integration planning should identify:

* Integration order.
* Interface readiness.
* Test environments.
* Dependencies.
* Configuration baselines.
* Entry and exit criteria.
* Required test evidence.
* Defect ownership.
* Rollback and recovery options.

Early integration can expose interface problems before they become expensive to fix.

### 3.6 Verify and validate

Verification evaluates whether the system or element satisfies specified requirements.

Validation evaluates whether the resulting system meets stakeholder needs and intended use.

These activities may involve analysis, inspection, demonstration, simulation, testing, or other appropriate methods.

A system may pass its component tests but still fail to achieve the desired operational outcome. For this reason, system-level validation should be planned rather than treated as an afterthought.

### 3.7 Transition, operate, maintain, and retire

Systems engineering continues after development.

The project may need to plan:

* Installation and deployment.
* Site readiness.
* Migration from existing systems.
* User training.
* Operational monitoring.
* Maintenance procedures.
* Spare parts and supplier support.
* Updates and upgrades.
* Incident handling.
* Data retention.
* Decommissioning and disposal.

Life-cycle costs and operational constraints should influence early architecture decisions.

## 4. The Systems Engineer's Role

The systems engineer coordinates technical reasoning across disciplines and life-cycle activities.

Typical responsibilities include:

* Eliciting and analyzing stakeholder needs.
* Developing and managing requirements.
* Supporting architecture and trade studies.
* Defining interfaces and boundaries.
* Coordinating technical reviews.
* Planning verification and validation.
* Managing technical risks.
* Supporting configuration and change control.
* Evaluating system-level performance.
* Maintaining traceability.
* Communicating technical decisions and trade-offs.
* Helping resolve cross-disciplinary conflicts.

The systems engineer does not necessarily perform every specialized task. Instead, the role ensures that the appropriate expertise is involved and that discipline-level decisions remain consistent with system objectives.

### 4.1 Technical authority and decision ownership

Projects should clarify who is responsible for recommending, reviewing, approving, and implementing technical decisions.

For example:

* A subsystem engineer proposes an alternative component.
* The systems engineer assesses system-level impacts.
* The safety specialist evaluates hazard implications.
* The cybersecurity specialist assesses security consequences.
* The project manager evaluates schedule and resource effects.
* The designated authority approves the change.

The actual allocation depends on governance arrangements.

## 5. Systems Thinking and Emergent Behavior

Systems thinking considers the relationships, feedback loops, constraints, and interactions that influence overall system behavior.

An emergent property is a characteristic of the system that results from the interaction of its elements and cannot be fully assessed by examining each element in isolation.

Examples include:

* End-to-end response time.
* Overall availability.
* Operational safety.
* Network congestion.
* Human-machine usability.
* Resilience under degraded conditions.
* Data consistency across distributed services.

### 5.1 Example: Availability

Suppose a service depends on three components connected in series. If all three must work for the service to operate, and their failures are independent, the service availability can be approximated by multiplying their individual availabilities.

If each component has availability of 0.99:

$$
A_{\text{system}} = 0.99 \times 0.99 \times 0.99
$$

$$
A_{\text{system}} \approx 0.9703
$$

The system availability is approximately 97.03%, not 99%.

This simplified calculation assumes a series architecture, independent component behavior, and consistent availability definitions. Real systems may require more detailed reliability modeling.

### 5.2 Feedback and unintended consequences

A change can cause secondary effects.

For example, adding more frequent monitoring messages may improve visibility but increase network load. Increased load may introduce latency, which then reduces the timeliness of monitoring.

Systems engineers look beyond the immediate effect of a change and consider the broader feedback mechanisms.

## 6. Requirements Traceability in Practice

Traceability connects needs, requirements, design decisions, implementation, verification evidence, and acceptance.

A typical chain is:

**Stakeholder need → system requirement → allocated requirement → design element → implementation → verification evidence → validation and acceptance**

Traceability helps answer:

* Why does this requirement exist?
* Which system elements satisfy it?
* Which tests verify it?
* What is affected by a proposed change?
* Which requirements remain unverified?
* Which stakeholder needs lack supporting requirements?

### 6.1 Bidirectional traceability

Forward traceability helps show that requirements have corresponding implementation and verification activities.

Backward traceability helps show that design elements and tests have a justified origin.

Untraceable design features may indicate unnecessary complexity, while requirements without implementation or verification evidence may indicate incomplete engineering.

### 6.2 Traceability is not merely a spreadsheet

A spreadsheet can support traceability, but the value comes from the relationships, accuracy, maintenance, and use of the information.

For larger systems, a managed requirements tool or model-based approach may improve consistency and change-impact analysis.

The project should select tools appropriate to its scale and risks.

## 7. Technical Trade Studies

A trade study compares alternatives against criteria derived from stakeholder needs, requirements, constraints, and project objectives.

### 7.1 Typical trade-study steps

1. Define the decision to be made.
2. Identify feasible alternatives.
3. Establish evaluation criteria.
4. Define constraints and mandatory requirements.
5. Gather evidence and assumptions.
6. Evaluate alternatives.
7. Analyze sensitivities and uncertainties.
8. Recommend an alternative.
9. Document the rationale.
10. Revisit the decision if important assumptions change.

### 7.2 Weighted decision matrix

Consider three candidate platforms.

| Criterion        | Weight | Platform A | Platform B | Platform C |
| ---------------- | -----: | ---------: | ---------: | ---------: |
| Performance      |   0.35 |          5 |          4 |          3 |
| Life-cycle cost  |   0.25 |          3 |          4 |          5 |
| Maintainability  |   0.20 |          4 |          4 |          3 |
| Integration risk |   0.20 |          2 |          4 |          5 |

Assume ratings range from 1 (poor) to 5 (excellent).

The weighted score is:

$$
S_j = \sum_{i=1}^{n} w_i r_{ij}
$$

where \(w_i\) is the weight of criterion \(i\), and \(r_{ij}\) is the rating of alternative \(j\) for that criterion.

For Platform A:

$$
S_A = (0.35 \times 5)+(0.25 \times 3)+(0.20 \times 4)+(0.20 \times 2)
$$

$$
S_A = 3.65
$$

For Platform B:

$$
S_B = (0.35 \times 4)+(0.25 \times 4)+(0.20 \times 4)+(0.20 \times 4)=4.00
$$

For Platform C:

$$
S_C = (0.35 \times 3)+(0.25 \times 5)+(0.20 \times 3)+(0.20 \times 5)=3.90
$$

Platform B has the highest illustrative weighted score.

However, the result is not automatically decisive. The team should examine rating quality, uncertainty, sensitivity to weights, and any mandatory constraints. A high score cannot compensate for failure to meet a non-negotiable safety or regulatory requirement.

## 8. Technical Reviews and Evidence

Technical reviews evaluate whether a system, design, plan, or work product is sufficiently mature for its intended purpose.

Depending on the project, reviews may address:

* Requirements completeness.
* Architecture feasibility.
* Interface consistency.
* Design readiness.
* Test readiness.
* Integration readiness.
* Operational readiness.
* Safety and security.
* Configuration status.
* Residual risks.

A review should have a defined purpose, appropriate participants, clear entry and exit criteria, recorded findings, and assigned actions.

A meeting is not an effective review merely because stakeholders attended it.

### 8.1 Evidence-based decisions

Engineering decisions should be based on appropriate evidence, including:

* Measurements.
* Test results.
* Analyses.
* Simulations.
* Inspection findings.
* Supplier documentation.
* Demonstrations.
* Operational data.
* Expert judgment with explicit assumptions.

The type and quality of evidence should be proportionate to the decision's importance and risk.

## 9. Managing Technical Risk

Technical risk concerns uncertainty that may affect system performance, safety, cost, schedule, integration, or other project objectives.

Examples include:

* Unproven technology.
* Unstable requirements.
* Unknown interface behavior.
* Inadequate performance margins.
* Limited supplier availability.
* Security vulnerabilities.
* Incomplete test environments.
* Uncertain operating conditions.

A risk register should normally identify the risk, its causes and consequences, likelihood or probability, impact, owner, response, and status according to the organization's method.

### 9.1 Risk response

Possible responses include:

* **Avoid:** Change the approach to eliminate the exposure.
* **Mitigate:** Reduce the probability or consequence.
* **Transfer or share:** Allocate specified exposure through an agreement or other arrangement, recognizing that some consequences cannot truly be transferred.
* **Accept:** Retain the risk under an authorized decision, with suitable monitoring or contingency planning.

The terminology and available response categories depend on the organization's risk-management framework.

### 9.2 Risk retirement

Risk retirement means gathering sufficient evidence or implementing effective controls so that a previously identified risk no longer requires the same level of attention.

A risk should not be marked closed merely because an action was performed. The team should verify that the action changed the risk as intended.

## 10. Configuration and Change Management

Configuration management maintains control over identified system items and their versions, status, and changes.

It helps ensure that teams know exactly what has been designed, tested, approved, delivered, and deployed.

Configuration items may include:

* Requirements baselines.
* Architecture models.
* Interface specifications.
* Source code.
* Firmware.
* Hardware drawings.
* Test procedures.
* Test results.
* Deployment scripts.
* System configuration data.
* Operational documentation.

### 10.1 Change impact analysis

Before approving a change, evaluate its potential effects on:

* Requirements.
* Architecture.
* Interfaces.
* Safety.
* Security.
* Performance.
* Cost and schedule.
* Verification and validation.
* Supplier agreements.
* Maintenance.
* Training.
* Existing deployments.

After approval, update affected artifacts, implement the change, and collect required evidence.

A change that is technically simple may have a broad system-level impact.

## 11. System Integration and End-to-End Thinking

Integration combines system elements and evaluates their interactions.

A useful strategy is to plan integration progressively, beginning with manageable combinations and expanding toward the complete system.

The exact sequence depends on architecture and risk.

Important practices include:

* Define interface contracts.
* Verify component readiness.
* Establish controlled integration environments.
* Use representative test data.
* Track versions and configurations.
* Automate repeatable integration tests.
* Test failure and recovery behavior.
* Monitor end-to-end performance.
* Maintain clear defect ownership.

### 11.1 Why component success is insufficient

A component may satisfy its own specification while the integrated system fails because of:

* Incompatible assumptions.
* Timing mismatches.
* Incorrect data formats.
* Unexpected network latency.
* Resource contention.
* Fault propagation.
* Inadequate recovery behavior.

System-level evidence is required to establish that the integrated solution meets its objectives.

## 12. Case Study: Enterprise Data Center Migration

### 12.1 Scenario

An organization plans to migrate several applications from aging physical servers to a virtualized infrastructure.

The system includes:

* Physical hosts.
* Virtual machines.
* Storage.
* Switching and routing.
* Identity and access management.
* Backup services.
* Monitoring.
* Application dependencies.
* Users and operational support staff.

The project initially focuses on copying virtual machines and meeting a weekend migration deadline.

### 12.2 Problems

During testing, the team discovers:

1. An application depends on an undocumented legacy server.
2. A firewall rule blocks communication between two services.
3. A backup job completes but cannot restore the application correctly.
4. DNS changes cause intermittent access failures.
5. The monitoring platform does not recognize the new virtual machines.
6. The rollback procedure has never been rehearsed.

Each technical team completed its own assigned task, but the integrated service is not ready.

### 12.3 Systems-engineering analysis

The primary problem is not simply a failed migration script. The project lacked a complete system view.

Missing or inadequate practices included:

* System-boundary and dependency analysis.
* Interface and network-flow documentation.
* Requirements traceability.
* End-to-end verification.
* Recovery testing.
* Operational-readiness assessment.
* Configuration control.
* Validation against user needs.

### 12.4 Corrective actions

The team should:

1. Build a dependency map for the affected applications.
2. Establish baseline requirements for availability, performance, access, backup, and recovery.
3. Document network flows and required interfaces.
4. Create a representative test environment.
5. Test application functions and integration.
6. Perform restore and recovery tests.
7. Validate monitoring and alerting.
8. Rehearse rollback with defined decision criteria.
9. Freeze and record the migration configuration.
10. Obtain formal readiness approval before the production cutover.

### 12.5 Lessons learned

* Infrastructure migration is a system transition, not just a server-copy exercise.
* Backups are useful only if recovery objectives can be demonstrated.
* Network, identity, monitoring, and application dependencies must be considered together.
* A schedule milestone is not evidence of readiness.
* Operational validation and rollback planning are part of good systems engineering.

## 13. Practical Exercises with Suggested Answers

### Exercise 1: Define a system boundary

A company develops a cloud inventory application that uses a third-party identity provider and an external warehouse database.

**Question:** What should the system boundary include or identify?

**Suggested answer:** Identify the application, its internal services and data, the identity provider, the warehouse database, users, network dependencies, external interfaces, operational responsibilities, and assumptions. External components need not be owned by the project to be relevant to the system boundary.

### Exercise 2: Improve a requirement

A requirement states: "The platform must be highly reliable."

**Question:** What should the systems engineer do?

**Suggested answer:** Work with stakeholders to define the operational meaning of reliability, relevant failure conditions, time horizon, operating environment, measurable thresholds, and acceptable recovery behavior. Trace the resulting requirement and define appropriate verification evidence.

### Exercise 3: Select an alternative

A high-performance design costs more to operate, while a lower-cost design has less capacity.

**Question:** How should the decision be made?

**Suggested answer:** Establish mandatory constraints and evaluation criteria, compare life-cycle cost and performance, assess uncertainty and sensitivity, and document the rationale. The lowest cost or highest performance alone does not determine the best system.

### Exercise 4: Handle an interface defect

Two services work independently, but their integration fails because one uses seconds and the other uses milliseconds.

**Question:** Which systems-engineering practices could prevent recurrence?

**Suggested answer:** Define interface data types and units, maintain controlled interface specifications, verify assumptions, use integration tests, and conduct change-impact analysis when interfaces change.

### Exercise 5: Evaluate a risk response

A team identifies an unproven component and assigns an engineer to investigate it. The risk register is immediately marked closed.

**Question:** Is this appropriate?

**Suggested answer:** No. Assigning an investigation is an action, not evidence that the risk has been reduced. The team should evaluate the findings, determine residual risk, and close or revise the risk based on evidence.

### Exercise 6: Verify or validate?

A system passes all specified response-time tests, but users cannot complete the intended workflow efficiently.

**Question:** Which activity has exposed the problem?

**Suggested answer:** Validation has exposed a mismatch between system behavior and intended use. The team may also need to refine requirements and conduct additional verification after changes.

### Exercise 7: Manage a configuration change

A developer changes a production configuration to fix an incident but does not record the change.

**Question:** Why is this dangerous?

**Suggested answer:** The deployed state may differ from the controlled baseline. Future troubleshooting, reproduction, rollback, security review, and verification may become unreliable. Emergency changes should still be recorded and reconciled with configuration control.

### Exercise 8: Assess a migration

A server migration succeeds, but users cannot access the application through the normal identity system.

**Question:** What does this reveal?

**Suggested answer:** Infrastructure-level success did not establish end-to-end system success. Identity, network, application, and user workflows should have been included in integration and validation activities.

### Exercise 9: Review a trade study

A weighted matrix selects an option that violates a mandatory security requirement.

**Question:** Should the option be selected because it has the highest score?

**Suggested answer:** No. Mandatory constraints should be evaluated separately. An alternative that violates a non-negotiable requirement should be rejected or redesigned unless the governing requirement is formally and lawfully changed by the authorized authority.

### Exercise 10: Plan integration

A project has five components and a deadline that leaves little time for end-to-end testing.

**Question:** What should the systems engineer recommend?

**Suggested answer:** Plan integration early, prioritize high-risk interfaces, use incremental integration and automated tests where appropriate, ensure test environments are ready, and communicate residual risks. The team should not assume that individual component tests replace end-to-end evidence.

## 14. Original CSEP-Style Practice Questions

**These are original study questions, not official INCOSE examination items.**

### Question 1

What is the central purpose of systems engineering in a multidisciplinary project?

A. Optimize every component independently.
B. Coordinate the system's elements and disciplines so the complete system meets stakeholder needs.
C. Replace the project manager.
D. Eliminate the need for testing.

**Correct answer: B.**

**Explanation:** Systems engineering considers the complete system and its interactions, not only individual components.

### Question 2

A component meets its local requirements, but the complete system fails to achieve the intended operational outcome. What is the most relevant concern?

A. Emergent system behavior and system-level validation.
B. The color of the project documentation.
C. The number of meetings attended.
D. The absence of a marketing campaign.

**Correct answer: A.**

**Explanation:** System behavior can emerge from interactions that are not evident during component-level evaluation.

### Question 3

Which is the strongest purpose of bidirectional requirements traceability?

A. Increase the number of requirements without justification.
B. Connect stakeholder needs, requirements, implementation, and verification evidence.
C. Prevent all requirements changes.
D. Replace stakeholder engagement.

**Correct answer: B.**

**Explanation:** Traceability supports completeness analysis, change-impact assessment, and verification coverage.

### Question 4

Which statement best describes a trade study?

A. A decision based exclusively on the most experienced engineer's preference.
B. A structured comparison of feasible alternatives using relevant criteria and evidence.
C. A test performed only after system retirement.
D. A method for avoiding documentation of decisions.

**Correct answer: B.**

**Explanation:** Trade studies make alternatives and trade-offs explicit and support defensible decisions.

### Question 5

A team performs a mitigation action for a technical risk. When should the risk be considered resolved?

A. Immediately after the action is assigned.
B. When the project manager requests closure.
C. When evidence supports the conclusion that the risk has been sufficiently reduced or otherwise addressed under the risk process.
D. When the risk has been copied into a report.

**Correct answer: C.**

**Explanation:** Risk closure should reflect the effectiveness of the response and the residual exposure.

### Question 6

What is a primary purpose of configuration management?

A. Allow undocumented changes to be made more quickly.
B. Maintain control and visibility over system configurations, versions, and changes.
C. Replace all testing with document reviews.
D. Prevent all system evolution.

**Correct answer: B.**

**Explanation:** Configuration management establishes a reliable record of what exists, what changed, and which baseline is authoritative.

### Question 7

A system passes verification but fails during realistic user operations. What is the most direct lesson?

A. Verification is always unnecessary.
B. Validation and operational context must be considered in addition to requirements verification.
C. Component tests guarantee system success.
D. Requirements cannot be changed.

**Correct answer: B.**

**Explanation:** Verification and validation address related but distinct questions.

### Question 8

A weighted trade-study score favors an alternative that fails a mandatory regulatory requirement. What should the team do?

A. Select it because the score is highest.
B. Ignore the regulatory requirement.
C. Treat the mandatory requirement as a constraint and reject or redesign the noncompliant alternative.
D. Increase the weight of cost until the result changes.

**Correct answer: C.**

**Explanation:** Mandatory constraints cannot normally be traded away through a weighted preference score.

### Question 9

Which activity is most useful for preventing late integration problems?

A. Postponing interface definition until the final delivery.
B. Incremental integration, controlled interfaces, and early integration testing.
C. Testing each component only in isolation.
D. Avoiding shared configuration information.

**Correct answer: B.**

**Explanation:** Early integration exposes mismatches while corrective action is generally less expensive.

### Question 10

Why should systems engineering continue through operation and retirement?

A. System performance, maintenance, upgrades, and disposal remain part of the system life cycle.
B. Engineering is complete as soon as the first component is built.
C. Operational data cannot improve future decisions.
D. Retirement has no technical consequences.

**Correct answer: A.**

**Explanation:** Life-cycle thinking includes operational effectiveness, supportability, changes, and responsible retirement.

## 15. Revision Notes

* Systems engineering coordinates disciplines and life-cycle activities to meet stakeholder needs.
* System boundaries identify included elements, external dependencies, and interfaces.
* Requirements should be clear, traceable, feasible, and verifiable.
* Architecture decisions require consideration of system-wide trade-offs.
* Emergent behavior results from interactions among elements.
* Verification assesses requirements conformity; validation assesses intended use and stakeholder needs.
* Traceability supports completeness, change-impact analysis, and verification planning.
* Trade studies compare alternatives against criteria, constraints, and evidence.
* Technical reviews require defined objectives and documented findings.
* Risk responses should be evaluated for effectiveness.
* Configuration management maintains reliable baselines and change records.
* Integration tests are essential because component-level success does not guarantee system-level success.
* Operation, maintenance, and retirement should be considered throughout the life cycle.

## 16. References and Further Study

1. **INCOSE Systems Engineering Handbook.** Consult the edition aligned with your CSEP preparation for systems-engineering practice, technical processes, technical management, and life-cycle application.
2. **ISO/IEC/IEEE 15288, Systems and software engineering — System life cycle processes.** Use the edition specified in your study materials.
3. **INCOSE Certification Program.** Review current official certification requirements and the applicable reference list.
4. **NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev. 2.** Supplementary reference for requirements, architecture, technical reviews, integration, verification, validation, and risk management.
5. **ISO 31000, Risk management — Guidelines.** Supplementary background on structured risk assessment and treatment.
6. **ISO 10007, Quality management — Guidelines for configuration management.** Useful supplementary material on configuration-management concepts.

**Study approach:** For each project scenario, identify the system boundary, stakeholder need, technical constraints, interfaces, risks, decision criteria, and evidence required to establish that the complete system works as intended.
