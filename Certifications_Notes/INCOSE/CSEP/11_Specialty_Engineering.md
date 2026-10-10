# 11 — Specialty Engineering

## 1. Learning Objectives

By the end of this module, you should be able to:

* Explain the role of specialty engineering in systems engineering.
* Distinguish safety, reliability, availability, maintainability, supportability, human factors, security, and resilience.
* Identify when specialty engineering activities should begin during the life cycle.
* Select suitable analysis methods for a system's risks and performance needs.
* Integrate specialty requirements into architecture, design, verification, validation, and operations.
* Apply specialty engineering concepts to a realistic system.

## 2. What Is Specialty Engineering?

**Specialty engineering** covers technical disciplines that influence system-wide properties and constraints but may not be captured adequately by considering individual components alone.

Examples include:

* Safety engineering
* Reliability engineering
* Availability and maintainability engineering
* Human factors and ergonomics
* Security engineering
* Environmental engineering
* Electromagnetic compatibility
* Survivability and resilience
* Quality engineering
* Logistics and supportability engineering

These disciplines are sometimes called *specialty* or *system-wide engineering disciplines*. Their precise grouping varies among organizations and standards.

### Why it matters

A system can meet its functional requirements and still fail operationally.

For example, a hospital monitoring system might correctly measure a patient's vital signs but still be unsuitable if:

* An alarm is frequently missed by staff.
* A network failure causes readings to disappear.
* A sensor produces unreliable measurements.
* Unauthorized users can access patient data.
* Replacement sensors take weeks to obtain.

Specialty engineering helps address these concerns throughout the system life cycle rather than treating them as final-stage checks.

## 3. Integration with Systems Engineering

Specialty engineering is not a separate activity performed only after the design is complete. It should influence stakeholder needs, requirements, architecture, design, implementation, integration, verification, validation, operation, and retirement.

A typical integration sequence is:

1. Identify stakeholder concerns, hazards, operating environments, and applicable obligations.
2. Define measurable specialty requirements.
3. Allocate requirements to system elements, interfaces, people, and operational procedures.
4. Analyze candidate architectures and design alternatives.
5. Identify risks, failure modes, and design constraints.
6. Define verification methods and acceptance criteria.
7. Evaluate evidence from tests, analysis, inspection, and operational monitoring.
8. Maintain traceability and reassess impacts when the system changes.

**Key principle:** Specialty requirements must be designed into the system and verified with evidence.

## 4. Safety Engineering

Safety engineering aims to prevent unacceptable harm to people, property, and the environment.

### Important concepts

* **Hazard:** A condition or situation that can contribute to harm.
* **Accident or mishap:** An event resulting in harm or other defined undesirable consequences.
* **Risk:** A combination of the likelihood of an adverse event and the severity of its consequences, interpreted according to the chosen assessment method.
* **Safety constraint:** A condition that must be satisfied to control a hazard.
* **Mitigation:** A measure that eliminates a hazard or reduces its likelihood or consequences.

A hazard is not necessarily the same as a component failure. A hazardous condition can arise from incorrect operation, unsafe interactions, environmental conditions, software behavior, or combinations of otherwise functioning components.

### Common safety analysis methods

| Method                                    | Main purpose                                                              |
| ----------------------------------------- | ------------------------------------------------------------------------- |
| Preliminary Hazard Analysis (PHA)         | Identify hazards early                                                    |
| Failure Modes and Effects Analysis (FMEA) | Examine individual failure modes and their effects                        |
| Fault Tree Analysis (FTA)                 | Analyze combinations of events that can cause a top-level undesired event |
| Hazard and Operability Study (HAZOP)      | Systematically identify deviations from intended operation                |
| System-Theoretic Process Analysis (STPA)  | Analyze unsafe control actions and inadequate control in complex systems  |

### Example

An industrial conveyor may injure a worker if it continues moving while a maintenance technician accesses a dangerous area.

Potential controls include:

* Physical guarding
* Interlocked access panels
* Emergency-stop mechanisms
* Lockout/tagout procedures
* Safe maintenance instructions
* Periodic inspection and testing

No single control should automatically be assumed sufficient. The complete design and operating context determine whether risks are acceptably controlled.

### Safety engineering workflow

1. Define the system boundary and operational context.
2. Identify hazards and hazardous scenarios.
3. Estimate and evaluate risk using the applicable method.
4. Develop safety requirements and constraints.
5. Select controls and allocate them to hardware, software, interfaces, and procedures.
6. Verify that controls are correctly implemented.
7. Validate their effectiveness under representative conditions.
8. Monitor incidents, changes, and residual risk throughout operation.

## 5. Reliability Engineering

Reliability is the probability that a system performs its required function without failure for a specified time under specified conditions.

Reliability must therefore be associated with:

* A defined function
* A time interval
* Operating and environmental conditions
* A defined failure criterion

A statement such as “the system is highly reliable” is incomplete without these details.

### Basic reliability models

For a constant failure rate under an exponential model:

$$
R(t)=e^{-\lambda t}
$$

Where:

* \(R(t)\) is the probability of surviving without failure through time \(t\).
* \(\lambda\) is the constant failure rate.
* \(t\) is the elapsed operating time.

The mean time to failure under this model is:

$$
MTTF=\frac{1}{\lambda}
$$

For two independent components arranged in a simple series configuration, where both must work for the system to work:

$$
R_{\text{series}}=R_1R_2
$$

For two independent components in a simple parallel configuration, where either component can provide the required function:

$$
R_{\text{parallel}}=1-(1-R_1)(1-R_2)
$$

These equations rely on assumptions such as independence and the stated architecture. Real systems may have common-cause failures, dependencies, standby switching failures, and repair effects that require more detailed models.

### Example

Two independent components each have reliability \(0.95\) over a specified mission.

For a series system:

$$
R_{\text{series}}=0.95\times0.95=0.9025
$$

For a simple parallel system:

$$
R_{\text{parallel}}=1-(0.05\times0.05)=0.9975
$$

The parallel result applies only if either component can provide the required function and the assumptions hold. Redundancy does not automatically protect against shared power, shared software, common environmental exposure, or other common-cause failures.

### Reliability engineering techniques

* Reliability Block Diagrams (RBDs)
* FMEA and FMECA
* Fault Tree Analysis
* Reliability prediction and allocation
* Accelerated life testing, where justified
* Failure data analysis
* Reliability growth tracking
* Root-cause analysis

## 6. Availability Engineering

Availability concerns whether a system is ready to perform its required function when needed.

A commonly used steady-state approximation for a repairable system is:

$$
A=\frac{MTBF}{MTBF+MTTR}
$$

Where:

* \(MTBF\) is mean time between failures.
* \(MTTR\) is mean time to repair or restore service under the organization's defined measurement convention.

For example, if MTBF is 200 hours and MTTR is 2 hours:

$$
A=\frac{200}{200+2}\approx0.9901
$$

This is approximately 99.01% availability under the simplified model.

Be careful: operational availability may also include preventive maintenance, logistics delays, administrative delays, and other downtime. The metric definition must state what is counted.

### Availability improvement strategies

* Improve component reliability.
* Reduce diagnostic time.
* Reduce repair time.
* Maintain spare parts.
* Use redundancy where justified.
* Improve monitoring and fault detection.
* Design for rapid replacement.
* Establish effective maintenance procedures.

**Important distinction:** Reliability concerns failure-free operation over a specified interval. Availability concerns readiness to perform the function when required.

## 7. Maintainability Engineering

Maintainability addresses how effectively and efficiently a system can be inspected, diagnosed, repaired, restored, or maintained.

Relevant design characteristics include:

* Accessibility of components
* Modular construction
* Standardized interfaces and parts
* Built-in test and diagnostics
* Clear maintenance instructions
* Safe isolation of energy sources
* Availability of tools and spare parts
* Ease of software updates and rollback

A system can be reliable but difficult to repair. Conversely, a system may experience frequent failures but achieve high availability if faults can be repaired rapidly.

### Example

Compare two network switches:

* Switch A is inexpensive but requires several hours of service interruption to diagnose and replace.
* Switch B costs more but supports monitoring, rapid configuration restoration, and hot-swappable components where appropriate.

The correct choice depends on the mission, downtime consequences, maintenance model, and life-cycle cost—not purchase price alone.

## 8. Supportability and Logistics Engineering

Supportability concerns the resources and arrangements needed to keep a system operational throughout its service life.

It includes:

* Spare-parts planning
* Maintenance personnel and training
* Technical manuals
* Diagnostic tools
* Supply-chain arrangements
* Software and firmware support
* Repair facilities
* Obsolescence management
* End-of-life planning

Supportability should be addressed during design. A technically excellent system can become unusable if its critical components are unavailable or its maintenance requires capabilities the operator does not possess.

### Life-cycle cost

Life-cycle cost can include acquisition, integration, operation, energy, maintenance, training, downtime, upgrades, and disposal.

A simplified conceptual expression is:

$$
LCC=C_{\text{acquisition}}+C_{\text{operation}}+C_{\text{maintenance}}+C_{\text{disposal}}
$$

Actual models may include many more cost categories, timing effects, inflation assumptions, and discounting.

## 9. Human Factors and Ergonomics

Human factors engineering considers the interactions among people, technology, tasks, environments, and organizational processes.

It addresses:

* Cognitive workload
* Situational awareness
* Interface readability
* Alarm design
* Error prevention and recovery
* Accessibility
* Training requirements
* Physical ergonomics
* Human-machine interaction
* Operational procedures

### Example: Monitoring dashboard

A dashboard may display every available metric but still be unsafe if the operator cannot quickly identify a critical alarm.

A human-factors review may recommend:

* Prioritizing alarms by urgency.
* Using clear labels rather than ambiguous codes.
* Reducing unnecessary alerts.
* Providing context and recommended actions.
* Avoiding reliance on color alone.
* Testing the interface with representative users.
* Evaluating workload under realistic conditions.

Human factors is not simply “making the interface attractive.” It is about making the system usable, understandable, and appropriate for the tasks and operating conditions.

## 10. Security Engineering

Security engineering protects system assets and functions against unauthorized access, misuse, disruption, alteration, or disclosure.

Common concerns include:

* Confidentiality
* Integrity
* Availability
* Authentication and authorization
* Secure communications
* Secure configuration
* Vulnerability management
* Logging and monitoring
* Recovery from security incidents
* Supply-chain security

### Security engineering activities

1. Identify assets and security objectives.
2. Define the system boundary, trust boundaries, and interfaces.
3. Identify threats, vulnerabilities, and attack paths.
4. Assess risk and establish security requirements.
5. Apply appropriate controls.
6. Verify and test the implementation.
7. Monitor, maintain, and update controls during operation.
8. Plan incident response and recovery.

Security requirements may influence architecture, component selection, data flows, user privileges, update mechanisms, and operational procedures.

**Safety and security are related but distinct.** A security incident may create a safety hazard, and a safety mechanism may be vulnerable to malicious interference. Their analyses should be coordinated where their risks interact.

## 11. Resilience Engineering

Resilience concerns the ability of a system to withstand disruptions, adapt, recover, and continue providing required services at an acceptable level.

Resilience strategies can include:

* Redundancy and diversity
* Fault containment
* Graceful degradation
* Backup and recovery
* Disaster recovery plans
* Isolation of compromised components
* Recovery-time objectives
* Monitoring and early warning
* Tested continuity procedures

### Example

A cloud service may lose access to one region. A resilient design could redirect traffic, restore critical data, and provide reduced functionality while recovery continues.

The architecture should be evaluated against realistic failure scenarios. Replication alone is insufficient if corrupted data or a compromised credential propagates to every replica.

## 12. Environmental and Electromagnetic Compatibility Engineering

Environmental engineering evaluates the effects of conditions such as temperature, humidity, vibration, dust, corrosion, shock, and radiation on system performance.

Electromagnetic compatibility (EMC) addresses whether equipment can operate satisfactorily in its electromagnetic environment without causing unacceptable interference to other equipment.

Potential design measures include:

* Environmental protection and suitable enclosures
* Component derating
* Thermal management
* Vibration isolation
* Grounding and bonding
* Shielding and filtering
* Cable routing and separation
* Testing under representative conditions

Requirements should reflect the actual deployment environment, not only laboratory conditions.

## 13. Quality Engineering

Quality engineering establishes confidence that processes and products meet defined requirements and are suitable for their intended use.

Activities can include:

* Quality planning
* Reviews and inspections
* Process monitoring
* Defect prevention
* Root-cause analysis
* Nonconformance management
* Corrective and preventive actions
* Audit and improvement activities

Quality assurance and verification overlap in practice but are not identical. Verification asks whether specified requirements have been met; quality assurance focuses on confidence in the processes and practices used to achieve the required quality.

## 14. Trade-Offs Among Specialty Disciplines

Specialty requirements can conflict or compete for resources.

Examples:

* More redundancy may improve availability but increase cost and complexity.
* Stronger security controls may increase authentication time or operational workload.
* A sealed enclosure may improve environmental protection but complicate maintenance.
* Additional alarms may improve detection but increase operator fatigue.
* Lightweight construction may conflict with durability or thermal management.

A disciplined trade study should:

1. Define the decision and stakeholders.
2. Establish mandatory constraints.
3. Select measurable evaluation criteria.
4. Assign justified weights where weighted scoring is appropriate.
5. Evaluate alternatives using evidence.
6. Test sensitivity to assumptions and weights.
7. Document the rationale and residual risks.

A weighted score does not justify violating a mandatory safety or legal constraint.

## 15. Case Study: Industrial Predictive-Maintenance System

### Scenario

A factory introduces a system that collects vibration and temperature measurements from production machinery. An analytics service predicts possible equipment failures and alerts maintenance staff.

### Specialty concerns

**Reliability:** Sensor readings and analytics must be sufficiently dependable for the intended decision.

**Availability:** Monitoring should remain useful during network or server disruptions.

**Maintainability:** Sensors and gateways should be replaceable without excessive downtime.

**Safety:** Maintenance actions must not expose personnel to moving machinery or hazardous energy.

**Security:** Unauthorized parties must not be able to alter predictions, disable alerts, or access sensitive operational data.

**Human factors:** Alerts should communicate urgency, supporting evidence, and appropriate next steps.

**Resilience:** The system should have a defined degraded mode if the analytics service becomes unavailable.

**Supportability:** Replacement sensors, trained technicians, firmware updates, and documentation must be available.

### Example requirements

* The system shall timestamp and store measurements with defined accuracy and retention requirements.
* The monitoring service shall generate a specified notification when a validated fault condition is detected.
* The system shall indicate when sensor data is stale or unavailable.
* Maintenance access shall follow approved isolation procedures.
* Administrative access shall require authenticated, authorized users.
* The system shall recover from a defined service interruption within a specified time.
* The dashboard shall be evaluated by representative maintenance personnel against defined usability criteria.

These requirements require project-specific thresholds, verification methods, and acceptance criteria before they can be baselined.

## 16. Exercises with Suggested Answers

### Exercise 1 — Reliability versus availability

A system rarely fails but takes a long time to repair. Which property is likely to be strong, and which may be weak?

**Suggested answer:** Reliability may be strong, while availability may be weak because repair duration creates substantial downtime.

### Exercise 2 — Identify hazards

An automated door closes when its sensor fails to detect a person.

**Suggested answer:** Consider the hazard of the door closing on a person. Analyze sensor failure, control logic, environmental conditions, and human interaction. Define suitable detection, force limitation, fail-safe behavior, testing, and maintenance controls according to the applicable safety requirements.

### Exercise 3 — Human factors

A dashboard has dozens of alarms, and operators routinely ignore them.

**Suggested answer:** Investigate alarm relevance, prioritization, workload, terminology, and response procedures. Test redesigned alarm behavior with representative users and measure whether critical conditions are recognized and handled correctly.

### Exercise 4 — Security and safety

A malicious actor disables a machine's safety monitoring.

**Suggested answer:** Treat this as a security threat that can create a safety hazard. Coordinate threat analysis and hazard analysis, define prevention and detection controls, and verify safe behavior when monitoring is unavailable or compromised.

### Exercise 5 — Supportability

A critical component is proprietary and has a six-month delivery time.

**Suggested answer:** Assess spare-parts needs, supplier risk, alternative components, redesign options, inventory cost, and the operational consequences of a prolonged outage.

### Exercise 6 — Environmental requirements

A device designed for an office is deployed in a hot, dusty factory.

**Suggested answer:** Reassess environmental assumptions and requirements. Evaluate temperature limits, dust ingress, cooling, component derating, and representative environmental testing.

### Exercise 7 — Redundancy

Two redundant servers share one power supply.

**Suggested answer:** The shared power supply is a potential common-cause failure. Analyze the full system architecture and consider independent power paths or another justified mitigation.

### Exercise 8 — Maintainability

A sensor can only be replaced after removing several unrelated components.

**Suggested answer:** Evaluate modularity, access, isolation, connector design, and replacement procedures. Measure expected maintenance time and assess whether the redesign improves life-cycle performance.

### Exercise 9 — Trade study

A more secure login mechanism is slower for emergency users.

**Suggested answer:** Define security and response-time requirements, identify operational scenarios, evaluate alternatives, assess human factors, and verify that the selected design satisfies mandatory constraints.

### Exercise 10 — Specialty integration

When should safety and reliability analyses begin?

**Suggested answer:** Early in concept development and requirements definition, then continue iteratively as architecture, design, implementation, and operational evidence evolve.

## 17. Original Exam-Style Practice Questions

*These questions are independently written for study practice and are not official INCOSE examination questions.*

### Question 1

Which statement best describes specialty engineering?

A. It is performed only after system integration.
B. It addresses system-wide properties and constraints throughout the life cycle.
C. It replaces system requirements engineering.
D. It applies only to safety-critical systems.

**Answer: B.** Specialty engineering influences requirements, architecture, design, verification, and operation. It is not restricted to the end of development or to safety-critical systems.

### Question 2

Which method is particularly suitable for identifying combinations of events that can lead to a defined top-level undesired event?

A. Fault Tree Analysis
B. Interface Control Documentation
C. Configuration auditing
D. Usability testing alone

**Answer: A.** Fault Tree Analysis models how contributing events and combinations can cause the selected top-level event.

### Question 3

Under a simple exponential reliability model, what happens to reliability as the mission duration increases, assuming a positive constant failure rate?

A. It always increases.
B. It remains constant.
C. It decreases.
D. It becomes equal to availability.

**Answer: C.** Under \(R(t)=e^{-\lambda t}\) with \(\lambda>0\), reliability decreases as \(t\) increases.

### Question 4

A system has high reliability but poor availability. Which explanation is most plausible?

A. Its repairs take a long time.
B. It never performs its required function.
C. Reliability and availability are identical.
D. It has no maintenance needs.

**Answer: A.** Long repair and restoration times can reduce availability even when failures are infrequent.

### Question 5

Which is the best example of a human-factors concern?

A. Whether the operator can correctly identify and respond to a critical alarm
B. Whether a source-code repository has a branch policy
C. Whether a purchase order has a reference number
D. Whether a file has been compressed

**Answer: A.** Human factors addresses the interaction between people, tasks, interfaces, and operating conditions.

### Question 6

What is a key limitation of adding redundant components?

A. Redundancy can never improve reliability.
B. Redundant components may share common-cause failure modes.
C. Redundancy always reduces maintainability.
D. Redundancy eliminates the need for testing.

**Answer: B.** Shared power, environmental exposure, software defects, and common dependencies can defeat redundancy.

### Question 7

Which activity most directly supports maintainability?

A. Making components accessible and easy to replace
B. Increasing the number of dashboard colors
C. Removing all maintenance documentation
D. Avoiding diagnostic functions

**Answer: A.** Accessibility and replaceability can reduce diagnostic and repair effort.

### Question 8

A system's security control makes a safety-critical action too slow. What is the best systems-engineering response?

A. Ignore the safety requirement.
B. Remove every security control.
C. Evaluate the conflict using coordinated security, safety, operational, and human-factors analyses.
D. Decide solely by selecting the lowest-cost alternative.

**Answer: C.** The interaction requires evidence-based analysis of mandatory constraints and operational consequences.

### Question 9

Why should supportability be considered during architecture development?

A. It only affects procurement paperwork.
B. It can influence modularity, component choices, maintenance strategy, and life-cycle cost.
C. It is unrelated to system availability.
D. It matters only after the system is retired.

**Answer: B.** Supportability decisions affect both design and the resources needed to sustain the system.

### Question 10

Which statement about verification is most accurate?

A. Verification proves that the system will never fail.
B. Verification checks conformance to specified requirements using defined methods and evidence.
C. Verification is identical to stakeholder validation.
D. Verification eliminates the need for operational monitoring.

**Answer: B.** Verification evaluates whether specified requirements have been satisfied; it does not guarantee zero failures or replace validation and monitoring.

## 18. Revision Notes

* Specialty engineering addresses system-wide properties and constraints.
* Integrate specialty concerns from the beginning of the life cycle.
* Safety engineering identifies hazards, assesses risk, and develops controls.
* Reliability concerns failure-free performance over a specified interval and conditions.
* Availability concerns readiness to perform a function when required.
* Maintainability concerns the effort and time required to maintain or restore a system.
* Supportability includes parts, tools, training, facilities, and logistics.
* Human factors addresses people, tasks, interfaces, and operational context.
* Security protects assets and functions against threats; security events can create safety hazards.
* Resilience concerns withstanding disruptions, adapting, and recovering.
* Redundancy requires analysis of common-cause failures and dependencies.
* Specialty trade studies must respect mandatory constraints and document their rationale.

## 19. References and Further Study

Use the latest applicable editions and confirm licensing, scope, and organizational applicability before relying on a standard.

* INCOSE, *Systems Engineering Handbook* — systems engineering processes and specialty engineering context.
* ISO/IEC/IEEE 15288, *Systems and software engineering — System life cycle processes*.
* ISO 31000, *Risk management — Guidelines*.
* IEC 61508, *Functional safety of electrical/electronic/programmable electronic safety-related systems*.
* ISO 26262, *Road vehicles — Functional safety*, when relevant to automotive systems.
* IEC 60812, *Failure modes and effects analysis (FMEA and FMECA)*.
* ISO 9241 series, *Ergonomics of human-system interaction*.
* ISO/IEC 27001, *Information security management systems — Requirements*.
* ISO 22301, *Security and resilience — Business continuity management systems — Requirements*.

**Study reminder:** Knowing a method's name is not enough. Be prepared to explain the question it answers, the evidence it produces, its assumptions, its limitations, and how its results affect system requirements and design.
