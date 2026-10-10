# Module 05: System Architecture and Design

## 1. Learning Objectives

After completing this module, you should be able to:

* Explain the difference between architecture and detailed design.
* Describe functional and physical decomposition.
* Understand logical and physical architectures.
* Identify system elements, interfaces, and dependencies.
* Explain architecture views and viewpoints.
* Compare design alternatives using trade studies.
* Understand requirement allocation and interface management.
* Apply architecture and design principles to a practical system.

---

## 2. What Is System Architecture?

System architecture describes the fundamental organization of a system, including its elements, relationships, interfaces, and the principles that guide its design and evolution.

Architecture helps answer questions such as:

* What major elements make up the system?
* What responsibilities does each element have?
* How do the elements interact?
* Where are requirements allocated?
* How are information, energy, or materials exchanged?
* How does the architecture address performance, safety, reliability, security, and maintainability?

Architecture is not simply a diagram. It is a structured representation of the system that supports analysis and engineering decisions.

### Example: Predictive-Maintenance Platform

A high-level architecture might include:

1. Sensors
2. Edge gateway
3. Data ingestion service
4. Data storage
5. Analytics service
6. Alerting service
7. Operator dashboard
8. Monitoring and administration services

The architecture defines how these elements interact and where responsibilities are assigned.

For example, the edge gateway may validate incoming measurements, while the backend performs long-term storage and analytics.

The exact responsibilities depend on operational needs, network conditions, reliability targets, cost, and other constraints.

---

## 3. Architecture vs. Design

Architecture and design are closely related, but they emphasize different levels of detail.

**Architecture** focuses on the major structure, relationships, interfaces, and significant technical decisions.

**Design** develops the detailed characteristics needed to implement or realize the system elements.

| Architecture concerns           | Detailed design concerns                  |
| ------------------------------- | ----------------------------------------- |
| Major system elements           | Internal component implementation         |
| Allocation of responsibilities  | Detailed algorithms and logic             |
| System-wide interfaces          | Exact field layouts and interface details |
| Deployment structure            | Specific infrastructure configurations    |
| Major technology choices        | Detailed component specifications         |
| System-level quality attributes | Detailed implementation measures          |

The distinction is not absolute. Projects differ in how they define architecture and design, and architecture decisions may continue throughout development.

### Example: Online Banking

Architecture decisions may include:

* Whether transaction processing is centralized or distributed
* How authentication is separated from transaction services
* How external payment networks are accessed
* How data is replicated and recovered
* How security boundaries are established

Detailed design decisions may include:

* Database indexes
* Internal class structures
* Exact API request validation logic
* Retry algorithms
* Specific deployment configuration parameters

Architecture decisions can have broad consequences, so they should be evaluated early enough to avoid unnecessary rework.

---

## 4. Functional Architecture

Functional architecture describes the functions the system must perform and how those functions relate to one another.

A **function** describes an activity or transformation performed by the system, independent of the particular element that implements it.

### Example: Smart Parking

The system may need to:

1. Detect parking-space occupancy.
2. Identify the relevant space.
3. Transmit occupancy data.
4. Validate incoming measurements.
5. Determine the reported occupancy state.
6. Publish availability information.
7. Notify operators about faults.
8. Record operational events.

These functions describe required behavior without yet assigning every function to a particular device or software service.

### Functional Decomposition

A high-level function can be decomposed into more detailed functions.

For example:

**Function: Process occupancy data**

* Receive occupancy message
* Validate message structure
* Check space identifier
* Assess data freshness
* Determine the accepted occupancy state
* Record processing status
* Publish the updated state

Decomposition should be detailed enough to support requirements, architecture, allocation, and verification without introducing unnecessary complexity.

### Functional Flow

A functional flow shows how functions exchange information, material, energy, or control.

Example:

```text
Detect Occupancy
       |
       v
Transmit Measurement
       |
       v
Validate Data
       |
       v
Determine Occupancy State
       |
       v
Publish Availability
       |
       v
Display Information
```

Real systems also require alternate paths for invalid data, communication failures, stale measurements, and recovery.

---

## 5. Logical Architecture

A logical architecture organizes functions and responsibilities into logical elements without necessarily committing to physical hardware or deployment locations.

It answers:

* Which logical elements are needed?
* What responsibilities do they have?
* What information do they exchange?
* What dependencies exist between them?

### Example

A predictive-maintenance platform may have these logical elements:

* Measurement Acquisition
* Data Validation
* Asset Management
* Analytics
* Alert Management
* User Interaction
* Audit and Monitoring

These are logical responsibilities. They do not necessarily correspond one-to-one with physical servers, containers, applications, or teams.

A logical element could later be implemented as a microservice, a module in a larger application, an embedded function, or a combination of components.

### Benefits

Logical architecture helps separate the problem of **what responsibilities are required** from the question of **where and how those responsibilities will be implemented**.

This separation can make it easier to compare alternative physical solutions.

---

## 6. Physical Architecture

Physical architecture identifies the actual or proposed system elements and their physical or implementation relationships.

Depending on the domain, these elements may include:

* Hardware units
* Software components
* Network devices
* Servers
* Sensors
* Mechanical assemblies
* Human operators
* Facilities
* External services

### Example: Smart Factory

A possible physical architecture includes:

* Vibration sensors mounted on machines
* Industrial gateways on the factory network
* An on-premises data-processing server
* A cloud analytics platform
* A web dashboard
* A maintenance workstation

The physical architecture must address practical constraints such as network connectivity, environmental conditions, latency, installation space, power, security, and maintenance access.

### Logical-to-Physical Mapping

A mapping connects logical responsibilities to physical elements.

| Logical responsibility  | Possible physical realization         |
| ----------------------- | ------------------------------------- |
| Measurement acquisition | Sensor firmware and sensor hardware   |
| Data validation         | Gateway software                      |
| Long-term storage       | Database service                      |
| Analytics               | Processing service or deployed model  |
| Alert management        | Backend notification component        |
| User interaction        | Web application                       |
| Audit and monitoring    | Logging and monitoring infrastructure |

One logical element may be distributed across several physical components. Conversely, one physical component may implement multiple logical responsibilities.

---

## 7. Interfaces and Dependencies

An interface describes an interaction across a boundary between elements.

Architecture must define important interfaces early enough to support coordinated development and integration.

### Common Interface Types

* Mechanical
* Electrical
* Software
* Data
* Communication
* Human-machine
* Organizational or procedural

### Example: Industrial Sensor Interface

The sensor and gateway interface may need to specify:

* Electrical connection
* Communication protocol
* Measurement units
* Sampling behavior
* Data representation
* Timestamp source
* Error reporting
* Calibration information

A mismatch in any of these characteristics can cause system-level problems even if both components work individually.

### Dependency Analysis

A dependency exists when the behavior or availability of one element affects another.

For example, an analytics service may depend on:

* Valid sensor data
* A functioning data-ingestion service
* Access to asset metadata
* Available computing resources
* Correct system time

Dependency analysis helps identify single points of failure, integration risks, and important design constraints.

### Interface Control

Interfaces should be documented and changes coordinated across affected elements.

Possible artifacts include interface specifications, interface control documents, API schemas, communication protocols, and controlled architecture models.

The appropriate level of documentation depends on complexity, risk, contractual requirements, and development practices.

---

## 8. Architecture Views and Viewpoints

A complex architecture cannot always be understood through one diagram.

Different stakeholders need different representations of the same system.

A **viewpoint** establishes conventions for constructing and interpreting a particular kind of view.

An **architecture view** is a representation of the architecture developed according to a viewpoint.

### Common Architecture Views

**Functional view:** Shows functions and their relationships.

**Logical view:** Shows logical elements and responsibilities.

**Physical view:** Shows physical or implementation elements.

**Interface view:** Shows interactions and interface definitions.

**Deployment view:** Shows where components execute or are installed.

**Information view:** Shows important data entities, relationships, and flows.

**Operational view:** Shows how the system is used in its intended environment.

**Security view:** Shows trust boundaries, security responsibilities, and relevant controls.

Not every project requires every view. Views should be selected according to stakeholder concerns and the decisions they need to support.

### Example: Hospital Monitoring System

* Clinicians need an operational view of how alerts reach staff.
* Developers need a logical view of processing responsibilities.
* Infrastructure administrators need a deployment view.
* Integration engineers need interface definitions.
* Security specialists need a view of trust boundaries and access control.
* Maintenance personnel need a view of replaceable components and support responsibilities.

The architecture should communicate the information needed by each audience without creating unnecessary documentation.

---

## 9. Architecture Drivers and Quality Attributes

Architecture is shaped by requirements and constraints that strongly influence the solution.

These are often called architecture drivers.

Examples include:

* Performance
* Reliability
* Availability
* Safety
* Security
* Scalability
* Maintainability
* Interoperability
* Cost
* Environmental constraints

### Example: Remote Monitoring

Suppose a remote monitoring system operates where internet connectivity is unreliable.

The architecture may need to support:

* Local data buffering
* Edge processing
* Delayed synchronization
* Clear indication of stale information
* Recovery after communication loss

If the architecture assumes continuous cloud connectivity, it may fail under the intended operating conditions.

### Quality Attributes Can Conflict

Examples:

* More redundancy may improve availability but increase cost.
* Stronger encryption may increase processing overhead.
* Smaller hardware may reduce installation space but constrain cooling.
* More frequent sensor reporting may improve freshness but consume more power.
* Greater flexibility may increase implementation and testing complexity.

Architecture decisions should account for these trade-offs explicitly.

---

## 10. Design Alternatives and Trade Studies

A **trade study** compares alternative solutions against defined criteria.

It helps engineers make transparent, evidence-based decisions when no alternative is best in every respect.

### Trade Study Process

1. Define the decision to be made.
2. Identify constraints and mandatory requirements.
3. Develop viable alternatives.
4. Establish evaluation criteria.
5. Assign justified weights if using weighted scoring.
6. Collect evidence for each alternative.
7. Evaluate performance, risk, cost, and uncertainty.
8. Compare results and perform sensitivity analysis when useful.
9. Select or recommend an alternative.
10. Record the decision, assumptions, and rationale.

### Example: Data Processing Location

A factory must decide whether to process sensor data at the edge, in the cloud, or using a hybrid architecture.

Potential criteria include:

* Response time
* Network dependence
* Data volume
* Availability
* Security
* Operational complexity
* Scalability
* Cost
* Maintainability

The team should first identify mandatory constraints. A weighted score should not allow a low cost score to compensate for failing a mandatory safety requirement.

### Weighted Scoring Example

Suppose three alternatives are scored from 1 to 5, where 5 is best.

| Criterion                  | Weight | Edge | Cloud | Hybrid |
| -------------------------- | -----: | ---: | ----: | -----: |
| Low latency                |   0.30 |    5 |     2 |      4 |
| Limited network dependence |   0.25 |    5 |     1 |      4 |
| Scalability                |   0.20 |    3 |     5 |      5 |
| Operational simplicity     |   0.10 |    3 |     4 |      2 |
| Cost suitability           |   0.15 |    3 |     4 |      3 |

The weighted score is calculated as:

$$
S_j = \sum_{i=1}^{n} w_i r_{ij}
$$

where:

* \(S_j\) is the score for alternative \(j\).
* \(w_i\) is the weight of criterion \(i\).
* \(r_{ij}\) is the rating of alternative \(j\) against criterion \(i\).

Using the illustrative values above:

* Edge: \(4.10\)
* Cloud: \(2.95\)
* Hybrid: \(3.85\)

Under these assumptions, edge processing receives the highest score.

This result is not an engineering conclusion by itself. The weights and ratings are illustrative, subjective, and potentially uncertain. The team should verify that the alternatives are feasible, that the criteria reflect stakeholder priorities, and that the decision remains reasonable when assumptions change.

---

## 11. Modeling and Architecture Analysis

Architecture models help engineers reason about the system before all components are built.

Models can represent:

* System context
* Functional decomposition
* Interfaces
* Data flows
* State transitions
* Physical structure
* Timing
* Resource consumption
* Failure behavior

Modeling techniques include block diagrams, activity diagrams, state machines, sequence diagrams, interface models, and formal or executable models.

### Example: Communication Loss

A system state model might include:

* Normal
* Degraded
* Communication Lost
* Recovering

Transitions depend on events such as missed heartbeats, restored connectivity, or successful synchronization.

The model helps identify requirements such as:

* How long before communication is declared lost?
* What functions remain available?
* How is data buffered?
* How are stale values identified?
* What happens when connectivity returns?
* How is duplicate data handled?

Modeling is useful only when the model's assumptions, scope, and relationship to the real system are understood.

---

## 12. Architecture Risk and Robustness

Architecture decisions can create risks that are difficult or expensive to remove later.

Examples include:

* A single critical component with no recovery strategy
* Excessive coupling between software services
* An undocumented external dependency
* An interface that cannot support required future changes
* A design that cannot be tested under realistic conditions
* Insufficient separation between safety-critical and noncritical functions
* An assumption that an external service is always available

### Robust Architecture

A robust architecture accommodates expected variation and failure conditions within defined limits.

Useful strategies may include:

* Clear separation of responsibilities
* Well-defined interfaces
* Appropriate redundancy
* Fault detection and recovery
* Graceful degradation
* Controlled configuration
* Security boundaries
* Monitoring and diagnostics
* Support for maintainability and replacement

Redundancy alone does not guarantee resilience. Shared power, common software defects, common data sources, or common network dependencies may still cause simultaneous failures.

---

## 13. Practical Case Study: Predictive-Maintenance Architecture

### Scenario

A manufacturer wants to monitor critical rotating machinery.

The system must collect measurements, identify abnormal conditions, notify maintenance personnel, and support long-term analysis.

### Step 1: Identify Architecture Drivers

* Timely detection
* Reliable measurement collection
* Operation during temporary network interruptions
* Secure access
* Manageable operating costs
* Maintainable hardware and software
* Traceable alerts

### Step 2: Define Functional Responsibilities

* Acquire measurements
* Validate measurements
* Buffer data
* Transmit data
* Store historical records
* Analyze conditions
* Generate alerts
* Display information
* Record audit events

### Step 3: Develop Alternatives

**Alternative A: Cloud-centered**

Most processing occurs in the cloud.

Benefits may include centralized management and scalable computing. Limitations may include dependence on connectivity and additional data transmission.

**Alternative B: Edge-centered**

Most time-sensitive processing occurs locally.

Benefits may include reduced dependence on connectivity and rapid local responses. Limitations may include constrained computing resources and more complex distributed maintenance.

**Alternative C: Hybrid**

Time-sensitive processing occurs locally, while the cloud supports historical analytics and fleet-wide analysis.

Benefits may include balancing local responsiveness with centralized capabilities. Limitations may include more complex synchronization and system integration.

### Step 4: Evaluate the Alternatives

The team should evaluate the alternatives against defined requirements, cost assumptions, network conditions, data volumes, failure scenarios, security needs, and maintenance capabilities.

### Step 5: Define Interfaces

Specify:

* Sensor-to-gateway communication
* Gateway-to-backend message format
* Time and unit conventions
* Buffering and synchronization behavior
* Alert interfaces
* Identity and access-control interfaces
* Monitoring and audit interfaces

### Step 6: Analyze Failure Conditions

Consider:

* Sensor failure
* Gateway power loss
* Network interruption
* Invalid measurements
* Cloud service unavailability
* Analytics failure
* Alert delivery failure
* Incorrect system time

Each scenario may require a defined response, status indication, recovery behavior, or operational procedure.

### Step 7: Verify and Validate the Architecture

Verification-oriented activities include interface tests, performance tests, failure injection, and resource measurements.

Validation-oriented activities evaluate whether the architecture supports the intended maintenance workflow and the required operational outcome.

### Lessons

* Architecture should be driven by requirements and operating conditions.
* Logical responsibilities should be clear before detailed implementation.
* Interface assumptions must be documented.
* Trade studies should use explicit criteria.
* Failure conditions should influence architecture early.
* The architecture should support integration, verification, maintenance, and evolution.

---

## 14. Exercises

### Exercise 1: Architecture vs. Design

Classify the following decisions as primarily architectural or detailed design decisions. Explain any ambiguity.

1. Choosing between edge, cloud, and hybrid processing.
2. Defining the internal variable names of a software function.
3. Separating authentication from transaction processing.
4. Selecting the exact database index for a particular query.
5. Defining the interface between a sensor gateway and a backend service.

### Exercise 2: Functional Decomposition

A smart irrigation system must water plants when soil moisture falls below an approved threshold.

Decompose the high-level function into at least five lower-level functions.

Include one function related to abnormal conditions.

### Exercise 3: Logical and Physical Architecture

For an automated warehouse robot, identify:

* Four logical elements
* Four physical elements
* Two possible mappings between logical and physical elements
* One reason the logical and physical structures might not correspond one-to-one

### Exercise 4: Trade Study

A remote industrial system needs fast responses but also requires centralized historical reporting.

Compare edge, cloud, and hybrid architectures using at least four criteria. Identify any mandatory constraints that should be evaluated before weighted scoring.

### Exercise 5: Interface Failure

A sensor reports temperatures in Fahrenheit, while the analytics service interprets values as Celsius.

Explain:

* Why this is an architecture or interface problem.
* Which specifications should define the interface.
* How the problem should be verified after correction.

### Exercise 6: Architecture Views

A hospital monitoring project involves clinicians, software developers, infrastructure administrators, and cybersecurity specialists.

Propose a useful architecture view for each group and explain why one diagram may not be sufficient.

### Exercise 7: Architecture Risk

A system depends on one cloud service for all critical functions. Identify at least four failure scenarios or architectural risks and propose possible mitigations.

### Exercise 8: Trade Study Calculation

Two alternatives receive ratings from 1 to 5.

| Criterion        | Weight | Alternative A | Alternative B |
| ---------------- | -----: | ------------: | ------------: |
| Performance      |   0.40 |             4 |             3 |
| Reliability      |   0.35 |             3 |             5 |
| Cost suitability |   0.25 |             5 |             2 |

Calculate both weighted scores. Explain why the result does not automatically determine the final design.

---

## 15. Exercise Answers

### Answer 1

1. Primarily architectural.
2. Primarily detailed design or implementation.
3. Primarily architectural.
4. Primarily detailed design.
5. Architectural at the interface-definition level, with detailed design needed for the complete schema and protocol behavior.

Some decisions span both levels. Their classification depends on the consequences and the project's architecture conventions.

### Answer 2

Possible decomposition:

1. Acquire soil-moisture measurements.
2. Validate measurement values.
3. Determine whether a watering condition is satisfied.
4. Check water availability and system readiness.
5. Command the appropriate irrigation valve.
6. Monitor watering status.
7. Stop watering when the defined condition is met.
8. Detect sensor or valve faults and enter the approved fault-handling mode.

The threshold, duration, and safety limits must be established for the actual system.

### Answer 3

Logical elements might include localization, route planning, obstacle avoidance, and motion control.

Physical elements might include a localization sensor, onboard computer, motor controller, and drive motors.

Possible mappings include route planning to software on the onboard computer and motion control to software running on the motor controller.

A logical element may be distributed across several devices, or one physical device may perform several logical functions.

### Answer 4

Possible criteria include response time, network dependence, scalability, operating cost, data volume, availability, and maintainability.

Mandatory constraints might include a maximum response time, operation during network loss, safety requirements, and required data-protection controls.

A hybrid architecture may be worth evaluating, but the decision should depend on evidence and the actual constraints.

### Answer 5

The components use inconsistent unit assumptions, so individually functional components produce incorrect system-level results.

The interface specification should define units, data types, allowed ranges, conversion responsibility, and error handling.

Verification should include known values in both units, boundary cases, interface integration tests, and regression tests for analytics and displays.

### Answer 6

* Clinicians: operational view showing alert generation, interpretation, and response.
* Developers: logical view showing services and responsibilities.
* Infrastructure administrators: deployment view showing servers, networks, dependencies, and recovery arrangements.
* Cybersecurity specialists: security view showing trust boundaries, identities, permissions, and protected interfaces.

Different views expose different concerns. A single diagram may become too crowded or omit information needed by particular stakeholders.

### Answer 7

Possible risks include cloud outage, network loss, credential compromise, service misconfiguration, data corruption, and provider dependency.

Mitigations may include local fallback functions, redundancy, tested recovery procedures, secure access controls, backups, monitoring, and documented provider-exit plans. Each mitigation should be assessed for its effectiveness, cost, and new risks.

### Answer 8

Alternative A:

$$
S_A = (0.40 \times 4)+(0.35 \times 3)+(0.25 \times 5)=3.85
$$

Alternative B:

$$
S_B = (0.40 \times 3)+(0.35 \times 5)+(0.25 \times 2)=3.45
$$

Alternative A has the higher illustrative weighted score. However, the weights and ratings require justification, uncertainty should be considered, and mandatory constraints must be satisfied regardless of the score.

---

## 16. Exam-Style Practice Questions

These are original study questions, not official INCOSE examination questions.

### Question 1

What is the primary purpose of system architecture?

A. To specify every source-code statement.
B. To describe fundamental system organization, relationships, interfaces, and significant design decisions.
C. To replace stakeholder requirements.
D. To eliminate detailed design.

### Question 2

Which decision is most clearly architectural?

A. Selecting a local variable name.
B. Choosing how major system responsibilities are separated and allocated.
C. Formatting a source-code comment.
D. Selecting the order of fields in an internal debugging message with no interface implications.

### Question 3

What does functional decomposition primarily accomplish?

A. It breaks required behavior into manageable functions.
B. It automatically determines the final hardware.
C. It removes the need for stakeholder needs.
D. It guarantees that integration will succeed.

### Question 4

What is the distinction between logical and physical architecture?

A. Logical architecture describes responsibilities and relationships; physical architecture identifies implementation or physical elements.
B. Logical architecture applies only to hardware.
C. Physical architecture never includes software.
D. The two terms always mean exactly the same thing.

### Question 5

Why are architecture views useful?

A. They eliminate the need for a consistent architecture.
B. They communicate relevant architectural concerns to different stakeholders.
C. They guarantee every design is correct.
D. They replace requirements verification.

### Question 6

What is the purpose of a trade study?

A. To select the newest technology automatically.
B. To compare alternatives against defined criteria and constraints.
C. To avoid documenting design decisions.
D. To ensure that the cheapest alternative always wins.

### Question 7

An architecture has excellent average performance but cannot operate during a required network interruption. What is the main issue?

A. The architecture may fail an important operational requirement despite performing well under normal conditions.
B. Average performance is always the only relevant metric.
C. Network availability is never an architectural concern.
D. The issue can only be solved by changing the user interface.

### Question 8

Why should interface definitions include units and data representations?

A. To prevent components from making incompatible assumptions about exchanged information.
B. To eliminate all component testing.
C. To avoid identifying system boundaries.
D. To guarantee that all requirements are feasible.

### Question 9

Which statement about weighted trade studies is correct?

A. A high score can override any mandatory safety constraint.
B. Scores and weights should be justified, and mandatory constraints must still be satisfied.
C. A numerical score removes all uncertainty.
D. The highest-cost option is always best.

### Question 10

Why should architecture account for failure scenarios?

A. Failure scenarios are relevant only after retirement.
B. They can expose dependencies, single points of failure, and missing recovery capabilities.
C. They eliminate the need for normal-operation requirements.
D. They guarantee that no failures will occur.

### Answer Key

| Question | Answer | Explanation                                                                             |
| -------- | ------ | --------------------------------------------------------------------------------------- |
| 1        | B      | Architecture captures the fundamental structure and significant decisions.              |
| 2        | B      | Responsibility allocation and major structural choices are architectural concerns.      |
| 3        | A      | Functional decomposition structures required behavior.                                  |
| 4        | A      | Logical and physical architecture emphasize different representations of the system.    |
| 5        | B      | Different stakeholders need different architectural information.                        |
| 6        | B      | Trade studies compare viable alternatives systematically.                               |
| 7        | A      | The architecture must satisfy operational conditions, not only normal-case performance. |
| 8        | A      | Explicit units and representations prevent interface misunderstandings.                 |
| 9        | B      | Weighted scoring supports decisions but does not override mandatory constraints.        |
| 10       | B      | Failure analysis reveals weaknesses in dependencies and recovery design.                |

---

## 17. Revision Notes

* **Architecture:** Fundamental system organization, relationships, interfaces, and guiding principles.
* **Design:** Detailed definition of how system elements are realized.
* **Functional architecture:** Organization of required functions and their interactions.
* **Logical architecture:** Organization of logical responsibilities and relationships.
* **Physical architecture:** Organization of physical or implementation elements.
* **Interface:** Boundary across which elements interact.
* **Architecture view:** Representation of architecture for particular concerns.
* **Viewpoint:** Conventions used to construct and interpret a view.
* **Architecture driver:** Requirement, constraint, or concern that significantly influences architectural decisions.
* **Trade study:** Structured comparison of alternatives.
* **Allocation:** Assignment of requirements or functions to system elements.
* **Robustness:** Ability to continue satisfying defined needs under expected variation or disturbance.

### Final Self-Assessment

You are ready to move on when you can:

1. Explain architecture versus detailed design.
2. Develop a functional decomposition.
3. Distinguish logical and physical architectures.
4. Identify important interfaces and dependencies.
5. Select useful architecture views for different stakeholders.
6. Conduct a simple trade study.
7. Explain how architecture decisions affect reliability, performance, and maintainability.

---

## 18. References and Further Reading

1. **INCOSE Systems Engineering Handbook** — consult the current edition for architecture definition, design definition, functional analysis, and technical decision-making.
2. **ISO/IEC/IEEE 15288, Systems and software engineering — System life cycle processes** — for the broader system life-cycle process framework.
3. **ISO/IEC/IEEE 42010, Systems and software engineering — Architecture description** — for architecture descriptions, stakeholders, concerns, views, and viewpoints.
4. **INCOSE Certification Program:** https://www.incose.org/certification/
5. **ISO standards catalogue:** https://www.iso.org/standards.html

Confirm the applicable editions and official ASEP examination reference requirements.

## Completion Checklist

* [ ] I understand architecture and detailed design.
* [ ] I can decompose system functions.
* [ ] I can distinguish logical and physical architecture.
* [ ] I can identify interface and dependency risks.
* [ ] I understand architecture views and viewpoints.
* [ ] I can compare alternatives using a trade study.
* [ ] I can explain architecture's relationship to quality attributes.
* [ ] I completed all eight exercises.
* [ ] I reviewed all ten exam-style questions.
