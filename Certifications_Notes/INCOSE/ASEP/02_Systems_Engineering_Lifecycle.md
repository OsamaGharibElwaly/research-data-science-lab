# Module 02: System Life Cycle and Life-Cycle Processes

## 1. Learning Objectives

After completing this module, you should be able to:

* Explain the concept of a system life cycle.
* Distinguish life-cycle stages from life-cycle models.
* Compare sequential, iterative, incremental, and evolutionary approaches.
* Understand the purpose of ISO/IEC/IEEE 15288.
* Explain the relationships between technical processes and technical management.
* Understand reviews, decision gates, baselines, and life-cycle transitions.
* Apply life-cycle concepts to a realistic engineering project.

---

## 2. What Is a System Life Cycle?

The **system life cycle** describes the stages and activities associated with a system from its initial conception through development, operation, maintenance, and eventual retirement.

A system life cycle is broader than software development. It considers the complete system, which may include hardware, software, people, facilities, operating procedures, and supporting services.

A typical system life cycle includes:

1. Concept and need identification
2. Concept development and feasibility assessment
3. Requirements and architecture definition
4. Design and implementation
5. Integration and verification
6. Validation and transition into operation
7. Operation and maintenance
8. Retirement and disposal

These stages are a useful simplified representation, not a universal mandatory sequence. Different life-cycle models organize activities differently, and real projects may combine or repeat stages.

### Why the Life Cycle Matters

A design that works during development may be difficult to manufacture, maintain, update, or safely retire.

For example, an industrial monitoring device may require:

* A reliable manufacturing process
* Installation instructions
* Operator training
* Spare parts
* Software updates
* Cybersecurity patches
* Calibration procedures
* End-of-life disposal

Considering these needs early can prevent expensive redesigns later.

### Life-Cycle Thinking

A systems engineer should consider not only whether a system can be built, but also whether it can be:

* Produced or acquired
* Integrated with existing systems
* Operated effectively
* Maintained affordably
* Upgraded when necessary
* Replaced or retired responsibly

These considerations are often described through life-cycle properties and stakeholder concerns.

---

## 3. Life-Cycle Stages

### 3.1 Concept and Need Identification

The effort begins by understanding the problem, opportunity, mission, or capability gap.

Typical activities include:

* Identifying stakeholders
* Understanding the operational environment
* Defining the problem or opportunity
* Identifying constraints
* Developing initial objectives
* Assessing whether a new system is needed

**Output examples:**

* Problem statement
* Initial concept of operations
* Stakeholder list
* Preliminary feasibility assessment
* Initial risk register

**Example:** A factory experiences unexpected machine downtime. The initial need is not necessarily "buy an AI model." It is to reduce unplanned downtime to an acceptable level.

Possible solutions may include predictive maintenance, improved preventive maintenance, better operator training, or replacing unreliable equipment.

### 3.2 Concept Development and Feasibility

The team explores alternative ways to meet the need.

Activities may include:

* Evaluating candidate solutions
* Assessing technical feasibility
* Estimating life-cycle costs
* Evaluating operational implications
* Identifying major risks
* Comparing benefits and limitations

A concept should be assessed against stakeholder needs and constraints rather than selected because it uses a fashionable technology.

**Example:** A factory compares three alternatives:

* Improve existing maintenance procedures
* Add condition-monitoring sensors
* Introduce a predictive-maintenance platform

The best choice depends on downtime patterns, data availability, budget, maintainability, and expected operational benefit.

### 3.3 Requirements and Architecture Definition

Once the preferred concept is sufficiently understood, the team defines what the system must do and develops a suitable structure.

Activities include:

* Eliciting stakeholder needs
* Developing system requirements
* Defining system functions
* Identifying system elements
* Defining interfaces
* Allocating requirements
* Evaluating architectural alternatives
* Planning verification and validation

**Example:** A monitoring platform may require that it detect defined machine conditions, record relevant measurements, issue alerts within an agreed interval, and support maintenance personnel during investigations.

The specific thresholds and conditions should be justified by stakeholder needs and engineering analysis.

### 3.4 Design and Implementation

System elements are designed, developed, configured, or procured.

Activities may include:

* Detailed hardware and software design
* Mechanical and electrical engineering
* Software implementation
* Data-model development
* Supplier coordination
* Component testing
* Design reviews
* Configuration management

Implementation is not restricted to writing code. It can include manufacturing hardware, configuring infrastructure, procuring equipment, developing procedures, and preparing facilities.

### 3.5 Integration and Verification

The developed elements are combined into a functioning system.

**Integration** focuses on combining elements and ensuring that their interactions work as intended.

**Verification** establishes whether specified requirements have been satisfied.

Activities may include:

* Interface testing
* Subsystem integration
* System-level testing
* Performance measurements
* Environmental testing
* Requirements traceability review
* Defect investigation

Integration and verification planning should start early enough to influence architecture and design.

### 3.6 Validation and Transition

Validation evaluates whether the complete system satisfies stakeholder needs and intended use.

Transition prepares the system and its operating environment for actual use.

Activities may include:

* Acceptance testing
* Operational trials
* User training
* Data migration
* Installation
* Operating procedure preparation
* Support readiness
* Handover to the responsible organization

**Example:** A predictive-maintenance platform may pass all API tests but still fail validation if maintenance staff cannot interpret its alerts or use them to plan work.

### 3.7 Operation and Maintenance

During operation, the system performs its intended mission or service.

Maintenance may involve:

* Corrective maintenance
* Preventive maintenance
* Software updates
* Security patching
* Performance monitoring
* Calibration
* Repair and replacement
* Operational support

Systems engineering remains relevant because operating experience can reveal new needs, changed environmental conditions, or design limitations.

### 3.8 Retirement and Disposal

Eventually, a system is withdrawn from service.

Activities may include:

* Planning replacement
* Migrating data
* Removing equipment
* Decommissioning interfaces
* Revoking credentials
* Disposing of hazardous materials
* Protecting or securely deleting data
* Preserving required records

Retirement is especially important for systems involving safety, security, regulated information, critical infrastructure, or hazardous materials.

---

## 4. Life-Cycle Models

A **life-cycle model** describes how life-cycle activities are organized and performed.

No single model is ideal for every project. The choice depends on uncertainty, complexity, risk, regulation, stakeholder availability, technical maturity, and the cost of changing a design.

### 4.1 Sequential or Waterfall-Oriented Model

A sequential model organizes major activities into ordered stages, with substantial completion of one stage before the next.

Simplified example:

```text
Requirements
     |
     v
Architecture and Design
     |
     v
Implementation
     |
     v
Integration and Testing
     |
     v
Deployment
     |
     v
Operation and Maintenance
```

**Advantages:**

* Clear stage structure
* Easier planning when requirements are stable
* Formal review and approval opportunities
* Useful for work requiring controlled documentation

**Limitations:**

* Late discoveries may cause expensive rework.
* Stakeholders may not see a working system until late.
* Assumptions can remain untested for too long.
* Changes may be costly once designs are established.

**Suitable situations:** Projects with relatively stable requirements, well-understood technologies, and formal approval requirements.

Sequential does not mean that feedback is impossible. Well-managed sequential projects still review evidence and revisit decisions when necessary.

### 4.2 Iterative Model

An iterative approach repeatedly revises a solution to improve its completeness, correctness, or performance.

A team may produce an initial architecture, evaluate it, discover a weakness, and revise the architecture before proceeding further.

**Example:** An engineering team develops a first version of an industrial sensor enclosure, tests heat dissipation, changes the ventilation design, and repeats the test.

**Advantages:**

* Supports learning and refinement
* Reveals design weaknesses earlier
* Allows alternatives to be explored
* Can reduce uncertainty

**Limitations:**

* Repeated work may increase cost.
* Uncontrolled iteration can cause scope drift.
* Decision criteria and configuration records must be maintained.

### 4.3 Incremental Model

An incremental approach delivers system capability in portions.

Each increment adds useful functionality to an existing or developing system.

**Example:** A monitoring platform is delivered in stages:

* Increment 1: Collect and display sensor data
* Increment 2: Add alerts
* Increment 3: Add historical analysis
* Increment 4: Add predictive analytics

Each increment should have an explicit scope, acceptance criteria, integration strategy, and relationship to the complete system.

**Advantages:**

* Earlier delivery of useful capability
* Feedback from actual users
* Phased investment
* Reduced need to implement every feature before initial deployment

**Limitations:**

* Interfaces and architecture must accommodate future increments.
* Integration across increments can become complex.
* Early versions may have limited functionality.
* Temporary workarounds can become long-term technical debt.

### 4.4 Evolutionary Model

An evolutionary approach develops and refines a system as understanding and evidence improve.

It is particularly useful when important requirements or technical characteristics cannot be fully established at the beginning.

**Example:** A robotics team develops a navigation capability through repeated field trials because real-world obstacle behavior is difficult to characterize completely in advance.

Evolutionary development requires control. Requirements, interfaces, decisions, and changes still need to be managed.

### 4.5 Spiral or Risk-Driven Model

A spiral-style approach organizes development around repeated cycles that emphasize objectives, alternatives, risk analysis, development, and evaluation.

A simplified cycle is:

1. Define objectives and constraints.
2. Identify and analyze risks.
3. Develop or evaluate a solution.
4. Review the results and plan the next cycle.

**Advantages:**

* Explicit attention to high-impact risks
* Useful for technically uncertain or complex projects
* Encourages evidence-based decisions before major commitments

**Limitations:**

* Risk analysis requires skilled people and reliable evidence.
* The approach may require more planning and management effort.
* It can be excessive for simple, low-risk work.

### 4.6 Agile and Hybrid Approaches

Agile approaches emphasize short feedback cycles, collaboration, and delivery of useful increments. Hybrid approaches combine elements of multiple life-cycle models.

A project might use:

* Formal system-level architecture and safety reviews
* Incremental software development
* Continuous integration and automated testing
* Controlled releases
* Periodic operational validation

Agile development does not remove the need for systems engineering. Complex products still require system-level requirements, interfaces, risk management, integration, and life-cycle consideration.

### Model Comparison

| Model        | Primary characteristic               | Useful when                                        |
| ------------ | ------------------------------------ | -------------------------------------------------- |
| Sequential   | Ordered stages                       | Requirements and technology are relatively stable  |
| Iterative    | Repeated refinement                  | Design needs to improve through evaluation         |
| Incremental  | Capability delivered in portions     | Early useful delivery is valuable                  |
| Evolutionary | Solution develops as knowledge grows | Requirements or technical details are uncertain    |
| Spiral-style | Repeated risk-focused cycles         | Major risks require deliberate analysis            |
| Agile        | Short feedback and delivery cycles   | Stakeholders can collaborate frequently            |
| Hybrid       | Combination of approaches            | Different parts of the system have different needs |

These approaches can overlap. For example, a project can be iterative, incremental, risk-driven, and agile at the same time.

---

## 5. ISO/IEC/IEEE 15288 and Life-Cycle Processes

ISO/IEC/IEEE 15288 is a key international standard for system life-cycle processes.

It provides a framework for describing processes used across a system's life cycle. It is not a single prescribed project schedule or a requirement to use one specific development model.

The standard groups processes into broad categories, including:

* Agreement processes
* Organizational project-enabling processes
* Technical management processes
* Technical processes

The exact terminology and organization should be checked against the applicable edition of the standard.

### 5.1 Agreement Processes

These processes address agreements between parties, such as acquisition and supply.

Examples include:

* Defining acquisition needs
* Establishing supplier responsibilities
* Agreeing on deliverables and acceptance criteria
* Managing contractual obligations

**Example:** A company procuring industrial sensors specifies performance requirements, environmental conditions, interface expectations, and acceptance tests.

### 5.2 Organizational Project-Enabling Processes

These establish capabilities and conditions that support projects.

Examples may include:

* Life-cycle model management
* Infrastructure management
* Portfolio or resource management
* Human-resource and competency management
* Quality-management support
* Knowledge and information management

**Example:** An organization establishes a shared test laboratory and common configuration-control procedures for multiple engineering teams.

### 5.3 Technical Management Processes

These processes help plan, assess, control, and coordinate technical work.

Examples include:

* Project planning
* Project assessment and control
* Decision management
* Risk management
* Configuration management
* Information management
* Measurement
* Quality assurance

**Example:** A technical manager monitors requirement volatility, integration defects, and unresolved high-priority risks to determine whether a design review can proceed.

### 5.4 Technical Processes

These processes define, realize, evaluate, and sustain the system.

Examples include:

* Business or mission analysis
* Stakeholder needs and requirements definition
* System requirements definition
* Architecture definition
* Design definition
* System analysis
* Implementation
* Integration
* Verification
* Transition
* Validation
* Operation
* Maintenance
* Disposal

The exact process names and groupings can vary by standard edition and related guidance.

### Important Exam Concept

A process framework describes **what outcomes and activities need to be addressed**. It does not necessarily prescribe one universal sequence for performing every activity.

Projects tailor processes to their size, complexity, risk, domain, and contractual or regulatory constraints.

---

## 6. Technical Processes Are Connected

The technical processes should not be understood as isolated tasks.

For example:

* Stakeholder needs influence system requirements.
* System requirements influence architecture.
* Architecture influences design and interfaces.
* Design affects implementation and integration.
* Verification evaluates conformance to requirements.
* Validation evaluates satisfaction of stakeholder needs.
* Operational results may trigger changes to requirements or architecture.

A change to one part of the system may require updates to several other parts.

### Example: Changing a Sensor

Suppose a temperature sensor is replaced by a lower-cost model.

The change may affect:

* Measurement accuracy
* Sampling frequency
* Electrical interfaces
* Software drivers
* Calibration procedures
* Power consumption
* Environmental tolerance
* Verification procedures
* Safety margins

The change should be assessed at system level, not approved solely because the new sensor is cheaper.

---

## 7. Reviews and Decision Gates

A **technical review** examines evidence to determine whether a product, process, or technical state is sufficiently mature for its intended purpose.

A **decision gate** is a point at which authorized decision-makers evaluate evidence and decide whether to proceed, revise, pause, or terminate work.

Examples of review objectives include:

* Confirming that stakeholder needs are understood
* Evaluating requirements quality
* Assessing architectural feasibility
* Confirming readiness for integration
* Evaluating verification results
* Assessing operational readiness

### Example: Architecture Review

A review team may examine:

* Requirement coverage
* Interface definitions
* Alternative architectures
* Performance estimates
* Safety and security concerns
* Reliability considerations
* Life-cycle cost
* Major technical risks
* Verification and validation plans

Possible outcomes include:

1. Approve progression to the next stage.
2. Approve with specified actions.
3. Request additional analysis.
4. Require redesign.
5. Stop the project if the concept is no longer viable.

A review is only useful when its purpose, entry criteria, evidence, decision authority, and exit criteria are understood.

### Entry and Exit Criteria

**Entry criteria** specify what must be ready before a review begins.

Examples:

* Required documents are available.
* Relevant stakeholders are invited.
* Key analyses are complete.
* Major unresolved issues are identified.

**Exit criteria** specify what must be achieved before the review is considered complete.

Examples:

* Critical issues have been resolved or formally accepted.
* Required actions have owners and due dates.
* The decision is documented.
* The next stage has defined conditions for proceeding.

---

## 8. Baselines and Controlled Progression

A **baseline** is an agreed reference configuration or set of information used as a basis for managing changes.

Examples include:

* Requirements baseline
* Architecture baseline
* Design baseline
* Product baseline

The exact meaning and timing of a baseline depend on the organization's processes.

A baseline does not mean the system can never change. It means changes are assessed and controlled rather than made without understanding their effects.

### Example

An approved interface specification defines the message format between a sensor gateway and a backend service.

A developer changes the format to improve performance but does not update the specification or notify the backend team.

The backend rejects incoming messages. This is a configuration and interface-management failure.

A controlled change process would identify the change, assess its impacts, authorize it when appropriate, update relevant records, and verify the result.

---

## 9. Life-Cycle Cost and Total Ownership

The cost of a system includes more than its initial purchase or development.

Potential cost categories include:

* Research and development
* Hardware and software acquisition
* Manufacturing
* Installation
* Training
* Infrastructure
* Operation
* Energy consumption
* Maintenance
* Upgrades
* Technical support
* Downtime
* Retirement and disposal

A solution with a lower initial cost may have a higher total life-cycle cost.

### Example

Two industrial monitoring solutions are being compared.

* Solution A has a lower purchase price but requires frequent manual calibration.
* Solution B costs more initially but supports remote diagnostics and requires less maintenance.

The engineering team should compare the alternatives over an agreed analysis period, using justified assumptions about installation, maintenance, downtime, replacement, and other relevant costs.

### Life-Cycle Cost Concept

A simplified representation is:

$$
C_{\text{life cycle}} =
C_{\text{development}} +
C_{\text{acquisition}} +
C_{\text{operation}} +
C_{\text{maintenance}} +
C_{\text{retirement}}
$$

This is a conceptual equation. Real cost models may account for timing, inflation, discount rates, uncertainty, residual value, and different cost categories.

### Trade-Off

The lowest-cost option is not necessarily the best option. Reliability, safety, maintainability, performance, schedule, and stakeholder priorities must also be considered.

---

## 10. Practical Case Study: Industrial Predictive-Maintenance Platform

### Scenario

A manufacturing company wants to reduce unexpected failures in production equipment.

The proposed system includes sensors, an edge gateway, a cloud platform, an analytics model, a maintenance dashboard, and maintenance procedures.

### Stage 1: Need Identification

The company identifies frequent unplanned downtime.

The initial need is to improve equipment availability, not necessarily to implement a particular AI technique.

### Stage 2: Concept Evaluation

Alternatives include:

* Improve existing maintenance scheduling
* Add basic condition monitoring
* Develop a predictive-maintenance system
* Replace the most unreliable machines

The team compares expected benefits, costs, data availability, feasibility, and operational risks.

### Stage 3: Requirements and Architecture

The team defines:

* Which equipment is in scope
* Which measurements are required
* How frequently data must be collected
* How missing or stale data will be handled
* What constitutes a meaningful warning
* Who receives alerts
* What response is expected
* How model performance will be assessed
* What availability and security requirements apply

### Stage 4: Implementation

The team installs sensors, configures gateways, develops data pipelines, implements analytics, and builds the dashboard.

### Stage 5: Integration and Verification

The team tests whether:

* Sensors provide measurements in the expected format.
* The gateway transmits data correctly.
* The platform handles missing messages.
* The analytics service processes valid input.
* Alerts are delivered within the required time.
* Access controls operate as specified.

### Stage 6: Validation and Transition

Maintenance personnel use the system during a controlled operational trial.

The team evaluates whether alerts are understandable, whether they support useful maintenance decisions, and whether the system contributes to the intended operational improvement.

Training, support, procedures, and fallback arrangements are established before broader deployment.

### Stage 7: Operation and Improvement

The team monitors:

* Data quality
* System availability
* Alert delivery
* False alarms
* Missed failures
* Model degradation
* User feedback
* Maintenance outcomes

If the operating environment changes, the team reassesses the system's requirements and suitability.

### Stage 8: Retirement

When the system is replaced, the organization plans data migration, sensor removal, credential revocation, retention of required records, and decommissioning of external interfaces.

### Lessons

* Start with the operational need.
* Compare alternatives before committing to a technology.
* Define interfaces and requirements before integration.
* Plan verification and validation early.
* Include people and procedures in the system.
* Manage changes throughout the life cycle.
* Consider operation, maintenance, and retirement during initial design.

---

## 11. Exercises

### Exercise 1: Choose a Life-Cycle Model

A company is developing a small, well-understood mechanical fixture using established manufacturing methods. Requirements are stable, and formal approval is required before production.

Which life-cycle approach might be suitable? Explain the reasons and identify one limitation.

### Exercise 2: Uncertain Technology

A research team is developing an autonomous robot for an environment it has never encountered. Navigation performance is uncertain.

Which development approach or combination of approaches could be suitable? Explain why.

### Exercise 3: Incremental Delivery

A city wants to deploy a smart parking platform in three phases.

Propose three increments and identify one integration risk that must be managed across them.

### Exercise 4: Process Categories

Classify the following activities into their most appropriate broad process category: agreement, organizational project-enabling, technical management, or technical.

1. Managing the technical risks of a development project.
2. Defining system requirements.
3. Establishing an organization-wide engineering infrastructure.
4. Agreeing on supplier deliverables and acceptance conditions.

### Exercise 5: Change Impact

An approved system design uses a communication module that is no longer available. A replacement has a different message format and power requirement.

Identify at least five areas that should be assessed before the change is approved.

### Exercise 6: Life-Cycle Cost

A device costs less to purchase but requires more frequent maintenance and has higher downtime.

Explain why comparing purchase prices alone may lead to a poor decision. Identify at least four cost or performance factors to consider.

### Exercise 7: Decision Gate

An architecture review finds that the system meets most performance requirements but has an unresolved critical safety concern.

Should the team automatically proceed because the performance requirements are mostly met? Explain what evidence and decision criteria are needed.

---

## 12. Exercise Answers

### Answer 1

A sequential or stage-gated approach may be suitable because the requirements and technology are well understood, and formal approvals are required.

One limitation is that unrecognized problems discovered late may cause costly rework. The team should still perform appropriate tests and reassess assumptions when new evidence appears.

### Answer 2

An iterative, evolutionary, or risk-driven approach may be appropriate, potentially combined with incremental development.

The team can use prototypes and field trials to reduce uncertainty, analyze major risks, and refine the system as knowledge improves. Configuration and requirements management remain important.

### Answer 3

Possible increments:

1. Occupancy monitoring and an operator dashboard.
2. A driver-facing application showing reported availability.
3. Historical analysis and optional payment integration.

An integration risk is inconsistent space identifiers or occupancy states across the sensor, backend, application, and payment-related services. Shared interface definitions and end-to-end testing can reduce this risk.

### Answer 4

1. Technical management.
2. Technical.
3. Organizational project-enabling.
4. Agreement.

The exact process classification should be checked against the applicable edition of ISO/IEC/IEEE 15288.

### Answer 5

Potential impacts include:

* Interface and message-format definitions
* Electrical compatibility
* Power consumption
* Thermal behavior
* Software drivers
* Timing and performance
* Verification procedures
* Environmental requirements
* Safety and security assumptions
* Supplier documentation
* Manufacturing and maintenance procedures

The team should also update affected configuration items and traceability records.

### Answer 6

Purchase price excludes many costs incurred over the system's life.

Factors include maintenance labor, spare parts, energy consumption, downtime, expected service life, reliability, repair time, support costs, replacement frequency, and disposal costs.

The decision should compare alternatives over a consistent analysis period with explicit assumptions.

### Answer 7

No. Meeting most performance requirements does not automatically justify proceeding with an unresolved critical safety concern.

The team should review the hazard analysis, potential consequences, risk acceptance criteria, proposed mitigations, verification evidence, and authorized decision-maker's responsibilities. Progression should follow the project's safety and review rules.

---

## 13. Exam-Style Practice Questions

These are original study questions, not official INCOSE examination questions.

### Question 1

What does a system life cycle primarily describe?

A. Only the period during which a product is manufactured.
B. The stages and activities associated with a system from conception through operation and retirement.
C. Only the software testing process.
D. The sequence of tasks performed by one engineering discipline.

### Question 2

Which statement best describes ISO/IEC/IEEE 15288?

A. It mandates one universal project schedule.
B. It defines a system life-cycle process framework that organizations can apply and tailor.
C. It applies exclusively to software coding.
D. It eliminates the need for project-specific planning.

### Question 3

A team repeatedly builds, tests, and refines a prototype. Which approach does this most directly illustrate?

A. Iterative development.
B. Retirement planning.
C. Configuration identification only.
D. A purely sequential approach with no feedback.

### Question 4

A product is delivered in several planned releases, with each release adding useful functionality. This is most directly associated with:

A. Incremental development.
B. Disposal.
C. Requirements validation only.
D. A one-time procurement process.

### Question 5

Why is a risk-driven life-cycle approach useful for highly uncertain technology?

A. It guarantees that no technical risks remain.
B. It directs attention to significant risks before making major commitments.
C. It removes the need for verification.
D. It prevents stakeholders from changing their needs.

### Question 6

Which is the best description of a decision gate?

A. A routine software function.
B. A point at which authorized decision-makers evaluate evidence and decide how work should proceed.
C. A substitute for requirements management.
D. An activity that can only occur after retirement.

### Question 7

Why are baselines useful?

A. They prevent all changes.
B. They provide controlled reference configurations against which changes can be assessed.
C. They replace interface specifications.
D. They ensure that every design is optimal.

### Question 8

A system is inexpensive to acquire but expensive to maintain. Which evaluation is most relevant?

A. Initial purchase price alone.
B. Total life-cycle cost and relevant performance trade-offs.
C. Number of developers involved.
D. Number of documents produced.

### Question 9

Which activity is most closely associated with validation?

A. Checking whether a component meets its specified voltage tolerance.
B. Confirming that intended users can accomplish the operational mission with the system.
C. Checking whether a drawing has a revision number.
D. Measuring the time required to compile source code when that time is not a system requirement.

### Question 10

Why should retirement be considered during early life-cycle planning?

A. Retirement always happens immediately after design.
B. End-of-life requirements can affect architecture, data handling, maintainability, safety, and cost.
C. Retirement replaces the need for operation.
D. It eliminates the need for configuration management.

### Answer Key

| Question | Answer | Explanation                                                                             |
| -------- | ------ | --------------------------------------------------------------------------------------- |
| 1        | B      | The system life cycle extends beyond development and includes operation and retirement. |
| 2        | B      | The standard provides a process framework rather than a universal project schedule.     |
| 3        | A      | Iteration involves repeated evaluation and refinement.                                  |
| 4        | A      | Incremental development adds capability in portions.                                    |
| 5        | B      | Risk-driven development helps reduce uncertainty before major commitments.              |
| 6        | B      | A gate is a formal decision point based on evidence and criteria.                       |
| 7        | B      | Baselines support controlled configuration and change management.                       |
| 8        | B      | Life-cycle cost includes acquisition, operation, maintenance, and retirement.           |
| 9        | B      | Validation evaluates suitability for stakeholder needs and intended use.                |
| 10       | B      | End-of-life needs can influence earlier engineering decisions.                          |

---

## 14. Revision Notes

* **Life cycle:** The full span of a system's existence and associated activities.
* **Life-cycle model:** The organization and execution approach used for life-cycle activities.
* **Sequential:** Major stages proceed in an ordered manner.
* **Iterative:** A solution is repeatedly refined.
* **Incremental:** Useful capabilities are delivered in portions.
* **Evolutionary:** The solution develops as understanding improves.
* **Risk-driven:** Development decisions are strongly influenced by risk analysis.
* **Hybrid:** Different approaches are combined to suit the system.
* **Technical processes:** Define, realize, evaluate, and sustain the system.
* **Technical management processes:** Plan, assess, control, and coordinate technical work.
* **Review:** An evaluation of evidence against defined objectives and criteria.
* **Decision gate:** A formal point for deciding whether and how to proceed.
* **Baseline:** An agreed reference configuration or information set.
* **Life-cycle cost:** Costs incurred across relevant stages of the system's existence.

### Final Self-Assessment

You are ready to move on when you can:

1. Explain the life cycle beyond development.
2. Compare sequential, iterative, and incremental approaches.
3. Describe how ISO/IEC/IEEE 15288 supports life-cycle process definition.
4. Explain why technical management and technical processes are connected.
5. Describe the purpose of reviews, decision gates, and baselines.
6. Explain why life-cycle cost is broader than purchase price.
7. Apply life-cycle thinking to an industrial or software-intensive system.

---

## 15. References and Further Reading

1. **INCOSE Systems Engineering Handbook** — consult the current edition identified by INCOSE for life-cycle models, life-cycle stages, technical processes, and technical management.
2. **ISO/IEC/IEEE 15288, Systems and software engineering — System life cycle processes** — the principal standards reference for system life-cycle processes.
3. **INCOSE Certification Program** — https://www.incose.org/certification/
4. **INCOSE official website** — https://www.incose.org/
5. **ISO official standards catalogue** — https://www.iso.org/standards.html

Check the current edition, availability, and ASEP examination reference requirements through official sources.

## Completion Checklist

* [ ] I can describe the major life-cycle stages.
* [ ] I can compare sequential, iterative, incremental, evolutionary, and risk-driven approaches.
* [ ] I understand the purpose of ISO/IEC/IEEE 15288.
* [ ] I can distinguish technical processes from technical management processes.
* [ ] I understand reviews, decision gates, and baselines.
* [ ] I can explain life-cycle cost.
* [ ] I completed all seven exercises.
* [ ] I reviewed all ten exam-style questions.
