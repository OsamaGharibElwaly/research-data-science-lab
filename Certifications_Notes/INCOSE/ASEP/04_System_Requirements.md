# Module 04: System Requirements Engineering

## 1. Learning Objectives

After completing this module, you should be able to:

* Explain the purpose of system requirements.
* Distinguish stakeholder requirements from system requirements and design specifications.
* Identify functional, performance, interface, constraint, and quality requirements.
* Write clear and verifiable requirements.
* Decompose and allocate requirements to system elements.
* Identify requirement dependencies and conflicts.
* Develop a requirements traceability matrix.
* Select appropriate requirement verification methods.
* Manage requirement changes and maintain baselines.

---

## 2. What Is a System Requirement?

A **system requirement** specifies a capability, characteristic, condition, or constraint that a system must satisfy.

Requirements provide a basis for architecture, design, implementation, integration, verification, and acceptance.

Without a clear set of requirements, teams may develop components that work individually but fail to meet the intended system purpose.

### Example: Industrial Monitoring Platform

Stakeholder need:

"Maintenance personnel need timely information about abnormal machine conditions."

Possible system requirements include:

* The system shall identify defined abnormal operating conditions.
* The system shall associate each detected condition with the relevant equipment identifier.
* The system shall record the timestamp of each accepted measurement.
* The system shall notify the designated operator role when a specified critical condition is detected.
* The system shall indicate when required input data is unavailable or stale.

These requirements describe capabilities without prematurely specifying every implementation detail.

Additional measurable limits—such as alert delivery time or data-freshness thresholds—must be established using operational analysis and stakeholder agreement.

---

## 3. Requirement Levels

Requirements are often organized into levels so that high-level needs can be translated into implementable and verifiable obligations.

A simplified hierarchy is:

1. Stakeholder needs and expectations
2. Stakeholder requirements
3. System requirements
4. Subsystem requirements
5. Component requirements

The number and naming of levels depend on the system and the engineering process.

### Example: Smart Parking

**Stakeholder need**

Drivers need useful information about available parking spaces.

**Stakeholder requirement**

The parking service shall provide drivers with current reported occupancy information for monitored spaces.

**System requirement**

The system shall display the latest accepted occupancy state associated with each monitored parking-space identifier.

**Subsystem requirement**

The backend service shall associate each accepted occupancy message with the corresponding parking-space identifier and receipt timestamp.

**Component requirement**

A particular component may be required to parse an approved message format and reject messages that do not meet its defined validation rules.

The final component requirement depends on the selected architecture and design.

### Why Requirements Are Decomposed

Decomposition helps:

* Break complex behavior into manageable obligations.
* Allocate responsibilities to system elements.
* Identify interfaces and dependencies.
* Support detailed design.
* Establish appropriate verification activities.
* Track requirement coverage.

However, decomposition must preserve the original intent. A lower-level requirement that is easy to implement but no longer satisfies the higher-level need is not a successful decomposition.

---

## 4. Types of Requirements

The categories below are useful for analysis and organization. Projects may use different taxonomies, and a single requirement may belong to more than one category.

### 4.1 Functional Requirements

Functional requirements specify what the system must do.

Examples:

* The system shall authenticate users before granting access to protected functions.
* The platform shall record each accepted equipment measurement.
* The system shall generate an alert when an approved fault condition is detected.
* The application shall allow an authorized operator to acknowledge an alert.

Functional requirements describe behavior or capability.

### 4.2 Performance Requirements

Performance requirements specify how well a function must be performed.

Examples include:

* Response time
* Throughput
* Accuracy
* Capacity
* Availability
* Update frequency
* Recovery time

Illustrative requirement:

"The service shall process at least 500 valid measurement messages per second under the specified workload and test configuration."

The number is an example, not a universal target. It must be justified for the actual system.

### 4.3 Interface Requirements

Interface requirements specify interactions between system elements or between the system and external entities.

They may concern:

* Message formats
* Electrical characteristics
* Mechanical dimensions
* Protocols
* Data types and units
* Timing
* Error handling
* External service contracts

Example:

"The gateway shall transmit accepted measurements using the approved message schema and shall include the equipment identifier, measurement value, unit, and timestamp."

A complete interface specification may need further detail about data types, allowed values, transport protocol, versioning, and error handling.

### 4.4 Constraint Requirements

Constraints restrict the acceptable solution space.

Examples:

* The system must operate within an existing facility's physical dimensions.
* The design must comply with applicable regulatory obligations.
* The solution must interface with a specified legacy system.
* The system must use an approved communication protocol.
* The project must meet a contractual delivery deadline.

A constraint should be justified and documented. An unnecessary constraint may prevent better alternatives from being considered.

### 4.5 Quality Requirements

Quality requirements describe important characteristics of the system.

Examples include:

* Reliability
* Maintainability
* Usability
* Security
* Safety
* Portability
* Interoperability
* Resilience

These qualities often need measurable criteria and operating conditions.

For example, "The system shall be secure" is not sufficient by itself. Relevant requirements might address authentication, authorization, audit logging, encryption, recovery, and handling of security events.

### 4.6 Operational and Support Requirements

These requirements address the conditions necessary to operate and support the system.

Examples:

* The system shall provide authorized maintenance personnel with diagnostic information.
* The device shall support the specified calibration procedure.
* The service shall retain operational records for the approved retention period.
* The system shall support recovery from defined failure conditions.

Operational and support requirements should be considered early, not only after development.

---

## 5. Anatomy of a Good Requirement

A good requirement states a clear obligation that can be assessed objectively.

A useful writing structure is:

**Subject + mandatory action or condition + object + applicable conditions + measurable criterion, where needed.**

Example:

"The monitoring service shall generate an alert within 5 seconds after detecting a qualifying critical condition under the specified operating conditions."

This sentence identifies:

* Subject: monitoring service
* Obligation: shall generate
* Output: alert
* Trigger: detection of a qualifying critical condition
* Timing criterion: within 5 seconds
* Conditions: specified operating conditions

The timing value is illustrative and requires justification in a real project.

### Requirement Quality Checklist

Check whether the requirement is:

1. **Clear:** It has a consistent interpretation.
2. **Necessary:** It supports an identified need or valid constraint.
3. **Feasible:** The system can satisfy it within applicable limits.
4. **Consistent:** It does not conflict with other requirements.
5. **Verifiable:** Compliance can be demonstrated.
6. **Traceable:** Its source and relationships are identifiable.
7. **Singular:** It does not combine unrelated obligations unnecessarily.
8. **Bounded:** Relevant conditions, limits, and assumptions are defined.
9. **Appropriately allocated:** It is assigned to a suitable system level.
10. **Controlled:** Its status and approved changes can be tracked.

### Common Weak Requirements

**Weak:** "The system should be fast."

**Problem:** The expected performance is undefined.

**Improvement:** Specify the operation, performance limit, workload, operating conditions, and measurement method.

---

**Weak:** "The system shall support secure and efficient processing."

**Problem:** It combines broad quality claims without objective criteria.

**Improvement:** Define separate security and performance requirements based on identified threats and operational needs.

---

**Weak:** "The system shall use Python."

**Problem:** This may prescribe an implementation unnecessarily.

**Improvement:** State the required behavior or capability unless Python is a justified project constraint.

---

**Weak:** "The system shall process all data correctly."

**Problem:** "All data" and "correctly" are undefined.

**Improvement:** Define valid input classes, expected outputs, error behavior, and the applicable test conditions.

---

## 6. Shall, Should, and May

Requirement documents often use modal verbs to distinguish obligations from preferences or permissions.

A common convention is:

* **Shall:** A mandatory requirement.
* **Should:** A recommendation or preferred behavior.
* **May:** A permitted option.

These meanings must be defined by the governing project standard or document convention. They should not be assumed if the document has not established them.

### Example

* "The service shall authenticate users before granting access to protected functions." — mandatory obligation.
* "The design should minimize unnecessary operator steps." — preferred objective requiring further clarification if compliance must be assessed.
* "The operator may export an approved report format." — permitted capability or option, depending on context.

For a formal requirements baseline, mandatory obligations should be clearly distinguished from guidance and optional features.

---

## 7. Requirement Decomposition and Allocation

**Decomposition** breaks higher-level requirements into more detailed requirements.

**Allocation** assigns requirements or portions of required behavior to appropriate system elements.

### Example: Automated Gate

High-level requirement:

"The gate system shall prevent unauthorized vehicle entry."

Possible lower-level requirements may concern:

* Identity or credential validation
* Authorization decision logic
* Gate actuator control
* Safety sensing
* Event recording
* Failure handling

The allocation depends on the selected architecture and the specific meaning of unauthorized entry.

### Allocation Rules

When allocating a requirement, consider:

* Which element can satisfy the obligation?
* Does the element have the required interfaces?
* Are supporting requirements needed?
* Does the allocation create a safety or security concern?
* How will the element be verified?
* Does the parent requirement remain fully covered?

### Avoid Artificial Decomposition

A higher-level requirement should not be split into arbitrary pieces merely to create more rows in a requirements document.

Every lower-level requirement should have a clear purpose and preserve the parent requirement's intent.

Some system-level requirements may apply to the system as a whole and cannot be assigned to a single component. For example, end-to-end availability may depend on several components, redundancy mechanisms, operating procedures, and external services.

---

## 8. Requirements Allocation Matrix

A requirements allocation matrix maps requirements to system elements.

Illustrative example:

| Requirement ID | Requirement                                                | Backend    | Gateway    | User Interface |
| -------------- | ---------------------------------------------------------- | ---------- | ---------- | -------------- |
| SYS-001        | Associate accepted measurements with equipment identifiers | Primary    | Supporting | —              |
| SYS-002        | Detect specified abnormal conditions                       | Primary    | Supporting | —              |
| SYS-003        | Display alerts to authorized operators                     | Supporting | —          | Primary        |
| SYS-004        | Indicate when data is stale                                | Primary    | Supporting | Supporting     |
| SYS-005        | Record defined alert events                                | Primary    | Supporting | Supporting     |

"Primary" indicates the main responsibility in this illustrative allocation. "Supporting" indicates a contribution. The actual allocation must reflect the system architecture.

The matrix can reveal:

* Requirements with no responsible element
* Elements with unclear responsibilities
* Duplicate implementations
* Requirements that cross multiple elements
* Interfaces requiring additional definition

An allocation matrix is not a replacement for detailed requirement statements, architecture models, or interface specifications.

---

## 9. Interface Requirements and Interface Control

Interfaces are a frequent source of system-level failures.

A component may operate correctly but fail to interoperate with another component because of incompatible assumptions.

### Example: Measurement Pipeline

The gateway sends:

```json
{
  "equipment_id": "MOTOR-17",
  "temperature": 84.5,
  "unit": "C",
  "timestamp": "2026-10-10T10:30:00Z"
}
```

The backend expects the temperature field to be named `temperature_celsius` and the timestamp to use a different format.

Both components may pass their own unit tests, yet the integrated system fails.

### Interface Definition Should Consider

* Interface purpose
* Sender and receiver
* Message or signal structure
* Data types
* Units
* Allowed values
* Timing requirements
* Error conditions
* Version compatibility
* Security and authorization
* Ownership and change responsibilities

An **Interface Control Document (ICD)** or equivalent controlled interface specification may document these details.

The specific artifact and level of formality depend on project needs.

### Interface Verification

Possible tests include:

* Schema conformance
* Data type and unit checks
* Timing tests
* Invalid-message handling
* Version compatibility
* Communication-loss behavior
* Security checks
* End-to-end data integrity

Interface tests should include abnormal conditions, not just successful exchanges.

---

## 10. Requirements Traceability

Traceability links requirements to their sources, derived requirements, architecture elements, verification activities, and relevant evidence.

A traceability matrix may contain:

* Requirement ID
* Requirement text
* Source or parent requirement
* Allocated system element
* Verification method
* Verification procedure or test case
* Status
* Change history

### Example Traceability Matrix

| ID      | Requirement                                                                | Source                         | Element           | Verification           |
| ------- | -------------------------------------------------------------------------- | ------------------------------ | ----------------- | ---------------------- |
| SYS-001 | Each accepted measurement shall include an equipment identifier.           | Stakeholder need SN-001        | Gateway/backend   | Test                   |
| SYS-002 | The system shall record a receipt timestamp for each accepted measurement. | SYS-001 and operational need   | Backend           | Test                   |
| SYS-003 | The operator interface shall indicate stale measurements.                  | Stakeholder need SN-002        | Backend/UI        | Test and demonstration |
| SYS-004 | Critical alerts shall be delivered within the approved time limit.         | Stakeholder requirement SR-003 | End-to-end system | Test                   |

This is an illustrative table. Real traceability may include several parent and child relationships for a single requirement.

### Forward and Backward Traceability

**Forward traceability** follows a need or requirement toward its derived requirements, design elements, and verification evidence.

**Backward traceability** follows a lower-level requirement or implementation element back to its justification.

Forward traceability helps establish coverage. Backward traceability helps identify unjustified requirements or unnecessary implementation.

### What Traceability Does Not Guarantee

Traceability does not automatically prove that:

* A requirement is correct.
* The architecture is optimal.
* A test is adequate.
* Stakeholders are satisfied.
* The system is safe.

It provides relationships that support analysis and evidence-based engineering decisions.

---

## 11. Requirement Verification Methods

Requirement verification demonstrates whether a requirement has been satisfied.

Common methods include:

### 11.1 Test

The system is operated under defined conditions, and observed results are compared with acceptance criteria.

Example:

Send a specified number of valid measurement messages and verify that the service processes them within the required performance limits.

### 11.2 Analysis

Calculations, models, simulations, or analytical evaluations are used to demonstrate compliance.

Example:

Calculate power consumption using component specifications and an approved operating profile.

The analysis method must be appropriate to the requirement and supported by adequate evidence.

### 11.3 Inspection

An item is examined to determine whether it meets specified characteristics.

Example:

Inspect an enclosure to confirm that its dimensions match the approved drawing.

### 11.4 Demonstration

The system's behavior is observed to establish that a capability exists, often without requiring highly instrumented quantitative measurements.

Example:

Demonstrate that an authorized operator can acknowledge an alert using the approved interface.

Some projects use different definitions or combine methods. Follow the applicable verification procedure.

### Selecting a Method

| Requirement type       | Possible verification method                                           |
| ---------------------- | ---------------------------------------------------------------------- |
| Dimensional constraint | Inspection or measurement                                              |
| Throughput             | Test and measurement                                                   |
| Structural performance | Analysis and/or test                                                   |
| Required user function | Test or demonstration                                                  |
| Data format            | Inspection and test                                                    |
| Reliability target     | Statistical analysis, test, or a justified combination                 |
| Safety behavior        | Analysis, inspection, test, and other approved evidence as appropriate |

The selected method should produce sufficient evidence for the importance and risk of the requirement.

---

## 12. Verification vs. Validation

These concepts are related but distinct.

**Verification:** Does the system or element satisfy its specified requirements?

**Validation:** Does the system satisfy stakeholder needs and intended use?

### Example: Medical Alert System

Verification may establish that:

* The system generates an alert under specified test conditions.
* The alert contains the correct equipment or patient identifier.
* The alert is delivered within the required interval.

Validation may evaluate whether:

* Medical staff can interpret the alert.
* The alert supports the intended clinical workflow.
* The complete system performs adequately in its operational environment.

A system can pass its defined tests and still be unsuitable for its intended purpose if the requirements were incomplete or the operational assumptions were wrong.

---

## 13. Requirement Dependencies and Conflicts

Requirements may depend on one another or impose competing constraints.

Examples:

* Higher sampling rates may increase communications load.
* Stronger encryption may increase processing overhead.
* A smaller enclosure may limit heat dissipation.
* Longer data retention may increase storage cost and privacy exposure.
* Higher availability targets may require redundancy and additional maintenance.

### Detecting Conflicts

The engineering team should examine:

* Requirements with overlapping scope
* Conflicting numerical limits
* Incompatible assumptions
* Shared resources
* Timing dependencies
* Safety and security constraints
* Conflicting stakeholder priorities

### Resolving Conflicts

A structured approach includes:

1. Identify the conflict.
2. Determine the underlying needs.
3. Check mandatory constraints.
4. Develop alternative solutions.
5. Analyze technical and operational consequences.
6. Compare alternatives against agreed criteria.
7. Document the decision and rationale.
8. Update affected requirements and verification plans.

A conflict should not be resolved by silently weakening one requirement.

---

## 14. Requirements Change Control

Requirements evolve as stakeholders learn, technology changes, regulations change, and operational evidence becomes available.

A controlled change process helps the team assess the consequences before modifying an approved baseline.

A typical process is:

1. Submit a change request.
2. Record the reason for the change.
3. Identify affected requirements and system elements.
4. Analyze technical, schedule, cost, safety, and operational impacts.
5. Identify affected interfaces and verification activities.
6. Obtain approval from the authorized decision-maker.
7. Update controlled documents and models.
8. Implement the change.
9. Perform the required verification and regression testing.
10. Record the final status and evidence.

The process should be proportionate to the risk and complexity of the change.

### Example

A stakeholder requests that a monitoring platform retain historical measurements for five years rather than one year.

The impact analysis should consider:

* Storage capacity
* Infrastructure costs
* Data-retention obligations
* Privacy and access controls
* Backup and recovery
* Data deletion at end of retention
* Performance of historical queries
* Migration of existing records
* Verification and operational procedures

A seemingly simple requirement change can affect several system elements.

---

## 15. Practical Case Study: SmartBrace Healthcare Monitoring System

### Scenario

A wearable device collects patient measurements and sends them to a backend platform. The platform processes the measurements and presents results to authorized users.

This case is educational. Actual clinical requirements, thresholds, and safety decisions must be established by qualified domain experts and applicable regulatory processes.

### Step 1: Identify the Need

Care teams need useful patient-monitoring information and timely notification of defined conditions.

### Step 2: Develop System Requirements

Candidate requirements include:

* The system shall associate each accepted measurement with the correct patient and measurement type.
* The system shall record the measurement timestamp and the time of receipt.
* The system shall indicate when required measurements are missing or stale.
* The system shall restrict access to patient information according to the approved access-control policy.
* The system shall record specified alert-generation and acknowledgement events.
* The system shall handle communication loss according to the approved failure-handling requirements.

These requirements need detailed acceptance criteria before implementation and verification.

### Step 3: Allocate Requirements

| Requirement area         | Candidate system element                  |
| ------------------------ | ----------------------------------------- |
| Measurement acquisition  | Wearable device                           |
| Measurement transmission | Device and communication interface        |
| Data validation          | Backend ingestion service                 |
| Patient association      | Backend identity/data services            |
| Alert generation         | Analytics and alerting services           |
| User access              | Authentication and authorization services |
| Alert presentation       | User interface                            |
| Audit records            | Backend audit service                     |

Some requirements apply across multiple elements and require end-to-end verification.

### Step 4: Define Interfaces

The engineering team defines:

* Measurement formats and units
* Patient and device identifiers
* Timestamp semantics
* Data-quality indicators
* Communication failure behavior
* Alert payloads
* Authorization rules
* Error reporting

### Step 5: Plan Verification

Potential verification activities include:

* Test correct measurement parsing and unit handling.
* Test patient and device association.
* Simulate missing and delayed data.
* Test access-control enforcement.
* Verify alert generation under approved test conditions.
* Test recovery after communication interruption.
* Verify audit-event creation.

### Step 6: Plan Validation

Representative users evaluate whether the complete system provides the intended monitoring capability, whether information is understandable, and whether alert handling fits the approved operational workflow.

### Step 7: Maintain Traceability

Each stakeholder need should connect to relevant requirements, system elements, verification activities, and validation evidence.

This helps identify missing coverage when requirements or the design change.

---

## 16. Exercises

### Exercise 1: Requirement Classification

Classify each statement as functional, performance, interface, constraint, or quality-related. More than one category may apply.

1. The service shall process 200 messages per second under the specified workload.
2. The application shall allow authorized users to export an approved report.
3. The gateway shall use the approved message schema.
4. The enclosure shall fit within the specified installation space.
5. The system shall recover from a defined failure within the approved recovery time.

### Exercise 2: Improve Requirements

Rewrite these statements as clearer candidate requirements:

1. "The platform should be secure."
2. "The system shall be fast."
3. "The application shall process all data correctly."
4. "The device shall be easy to maintain."

For each, identify information that must be agreed upon before the requirement is finalized.

### Exercise 3: Decomposition and Allocation

A warehouse monitoring system must notify operators when a critical monitored area becomes inaccessible.

Develop:

* One high-level system requirement.
* Three lower-level candidate requirements.
* A possible allocation of those requirements to system elements.
* One integration test.

### Exercise 4: Traceability

Create a traceability chain for the need:

"Authorized operators must be able to identify the source of every critical alert."

Include a stakeholder need, system requirement, design element, and verification activity.

### Exercise 5: Verification Method

Choose an appropriate primary verification method for each requirement and justify your choice.

1. The mounting bracket shall have specified dimensions.
2. The platform shall process a defined workload within a maximum response time.
3. The system's power consumption shall remain below a specified limit under a defined operating profile.
4. An authorized operator shall be able to acknowledge an alert.
5. A component shall withstand a specified environmental stress.

More than one method may be needed for some requirements.

### Exercise 6: Change Impact Analysis

A sensor's output unit changes from Fahrenheit to Celsius.

Identify at least six affected areas and explain which verification activities may need to be repeated.

### Exercise 7: Requirement Conflict

One requirement calls for a small battery-powered device. Another requires continuous high-frequency sensing and wireless transmission.

Explain the potential conflict and outline a systematic method for resolving it.

### Exercise 8: Baseline and Change Control

A developer changes an API response field without updating the approved interface specification.

Explain:

* Why this is a configuration-management problem.
* How the change should have been handled.
* What evidence is needed before the revised interface is accepted.

---

## 17. Exercise Answers

### Answer 1

1. Performance.
2. Functional.
3. Interface and potentially constraint-related.
4. Physical constraint.
5. Performance and reliability-related.

The categories are not mutually exclusive; classification depends on the project's taxonomy and the exact wording.

### Answer 2

Possible improvements:

1. "The system shall enforce the approved authorization rules for all protected functions." Detailed roles, permissions, threat assumptions, and test conditions must be defined.
2. "The service shall complete the specified operation within [agreed limit] under [defined workload and environment]." The operation, limit, workload, and measurement method are needed.
3. "The service shall validate each input against the approved schema and shall reject invalid messages with the specified error response." The schema and error behavior must be defined.
4. "An authorized technician shall be able to replace the specified field-replaceable component using the approved tools and procedure within [agreed time limit]." The technician profile, tools, procedure, and time limit must be agreed upon.

These are examples of candidate wording, not finalized requirements.

### Answer 3

High-level requirement:

"The system shall notify the designated operator when a monitored area meets the approved criteria for critical inaccessibility."

Possible lower-level requirements:

* The sensing subsystem shall report the defined status of each monitored area.
* The backend shall determine the critical-inaccessibility state according to the approved decision rules.
* The notification service shall deliver the resulting alert to the designated operator role.

Possible allocation: sensing subsystem, backend decision service, and notification service.

Integration test: Simulate the defined critical condition, verify that the backend detects it, and confirm that the correct operator receives an alert within the agreed interval.

### Answer 4

* **Need:** Authorized operators need to identify the source of critical alerts.
* **Requirement:** Each critical alert shall include the unique identifier of the originating monitored asset.
* **Design element:** Alert-generation service and asset registry.
* **Verification:** Generate alerts for several known assets and confirm that every alert contains the correct originating identifier.

### Answer 5

1. **Inspection or measurement:** Compare bracket dimensions against the approved drawing and tolerances.
2. **Test:** Measure response time under the defined workload.
3. **Analysis and/or test:** Estimate consumption from a justified model and confirm it through measurement where required.
4. **Demonstration or test:** Execute the acknowledgement workflow using an authorized account.
5. **Test and possibly analysis:** Apply the specified environmental stress and evaluate the acceptance criteria.

The primary method depends on the requirement, risk, available evidence, and governing procedure.

### Answer 6

Potentially affected areas include:

* Sensor interface specification
* Unit conversion logic
* Stored measurement values
* Historical records and their metadata
* Analytics and threshold logic
* Dashboard labels
* API schemas
* Alert calculations
* Reports
* Verification procedures
* User documentation

Tests should confirm correct conversion and unit interpretation, verify thresholds, inspect displayed values, and assess historical-data handling. Regression tests should cover affected interfaces and functions.

### Answer 7

Continuous sensing and transmission may increase energy consumption, while the battery requirement limits available power.

The team should quantify the sensing and communication workload, define the required battery life, analyze duty cycles and transmission strategies, evaluate local processing and event-driven reporting, compare alternatives, and verify the selected design against agreed performance and endurance criteria.

### Answer 8

The unapproved API change can break dependent components and make the implementation inconsistent with the controlled specification.

The team should submit and assess the change, identify affected components, update the interface specification after authorization, notify dependent teams, and execute compatibility and integration tests.

Acceptance evidence may include schema-conformance results, successful integration tests, error-handling tests, regression-test results, and an approved change record.

---

## 18. Exam-Style Practice Questions

These are original study questions, not official INCOSE examination questions.

### Question 1

What is the primary purpose of system requirements?

A. To describe only the final source code.
B. To define conditions and capabilities the system must satisfy.
C. To replace stakeholder analysis.
D. To eliminate all design decisions.

### Question 2

Which statement is most clearly a functional requirement?

A. The system shall support the defined number of concurrent users.
B. The system shall allow an authorized operator to acknowledge an alert.
C. The system shall fit within a specified physical envelope.
D. The system shall achieve a specified availability target.

### Question 3

Which is the strongest reason to decompose a high-level requirement?

A. To create as many requirements as possible.
B. To establish manageable obligations that can be allocated and verified while preserving the original intent.
C. To eliminate system-level analysis.
D. To avoid documenting interfaces.

### Question 4

What is the purpose of a requirements traceability matrix?

A. To guarantee that every requirement is correct.
B. To record relationships between requirements and relevant sources, elements, and evidence.
C. To replace all design documents.
D. To prevent changes to the baseline.

### Question 5

Which verification method primarily uses calculations or models to demonstrate compliance?

A. Analysis.
B. Demonstration.
C. Inspection only.
D. Informal discussion.

### Question 6

A system meets every documented requirement but fails to satisfy the operational need. What is the most important lesson?

A. Requirements are unnecessary.
B. Verification alone does not establish that stakeholder needs and intended use are satisfied.
C. Testing must always be removed.
D. The system is automatically compliant with every operational objective.

### Question 7

A developer modifies an approved interface without updating the specification. Which concern is most relevant?

A. Configuration and interface control.
B. Stakeholder identification only.
C. Retirement planning only.
D. Life-cycle cost accounting only.

### Question 8

Which statement best describes a constraint requirement?

A. It defines a restriction on the acceptable solution space.
B. It is always a user-interface requirement.
C. It cannot influence architecture.
D. It is always optional.

### Question 9

A new requirement increases data retention from one year to five years. What should happen first?

A. Implement it immediately without further analysis.
B. Assess its impact on storage, cost, privacy, security, performance, and related requirements before approval.
C. Delete the existing requirements baseline.
D. Assume that no other component is affected.

### Question 10

Why should requirements be verifiable?

A. So compliance can be demonstrated using appropriate evidence.
B. So requirements never change.
C. So stakeholders do not need to review them.
D. So system validation becomes unnecessary.

### Answer Key

| Question | Answer | Explanation                                                                 |
| -------- | ------ | --------------------------------------------------------------------------- |
| 1        | B      | Requirements define what the system must satisfy.                           |
| 2        | B      | It describes a specific system capability.                                  |
| 3        | B      | Decomposition supports allocation and verification while preserving intent. |
| 4        | B      | Traceability records relevant relationships and supports impact analysis.   |
| 5        | A      | Analysis uses calculations, models, or analytical evidence.                 |
| 6        | B      | Meeting specifications does not by itself prove operational suitability.    |
| 7        | A      | Approved interfaces and their changes require control.                      |
| 8        | A      | Constraints limit acceptable solutions.                                     |
| 9        | B      | The change may affect multiple requirements and system elements.            |
| 10       | A      | Verifiability allows objective compliance evidence to be established.       |

---

## 19. Revision Notes

* **System requirement:** A condition or capability that the system must satisfy.
* **Functional requirement:** Specifies what the system must do.
* **Performance requirement:** Specifies how well the system must perform.
* **Interface requirement:** Specifies how elements interact.
* **Constraint:** Restricts the acceptable solution space.
* **Quality requirement:** Specifies a quality characteristic such as reliability, usability, or security.
* **Decomposition:** Breaks a higher-level obligation into manageable requirements.
* **Allocation:** Assigns requirements to suitable system elements.
* **Traceability:** Connects requirements to their origins and related engineering artifacts.
* **Verification:** Demonstrates compliance with specified requirements.
* **Validation:** Evaluates satisfaction of stakeholder needs and intended use.
* **Baseline:** An approved reference configuration or information set.
* **Change control:** Assesses and governs modifications to controlled items.

### Final Self-Assessment

You are ready to move on when you can:

1. Classify common requirement types.
2. Rewrite vague requirements into testable candidate statements.
3. Explain decomposition and allocation.
4. Develop a basic requirements traceability matrix.
5. Select appropriate verification methods.
6. Explain interface control and change impact analysis.
7. Distinguish verification from validation.

---

## 20. References and Further Reading

1. **INCOSE Systems Engineering Handbook** — consult the current edition for system requirements definition, requirements management, allocation, verification, and validation.
2. **ISO/IEC/IEEE 15288, Systems and software engineering — System life cycle processes** — for the broader life-cycle framework.
3. **ISO/IEC/IEEE 29148, Systems and software engineering — Life cycle processes — Requirements engineering** — for requirements engineering concepts and requirements-related information items.
4. **INCOSE Certification Program:** https://www.incose.org/certification/
5. **ISO standards catalogue:** https://www.iso.org/standards.html

Check the current editions and the official ASEP examination reference requirements before relying on a specific publication.

## Completion Checklist

* [ ] I can distinguish requirement levels and types.
* [ ] I can write clear and verifiable candidate requirements.
* [ ] I can decompose and allocate requirements.
* [ ] I understand interface requirements and control.
* [ ] I can create a basic traceability matrix.
* [ ] I can select suitable verification methods.
* [ ] I understand requirement baselines and change control.
* [ ] I completed all eight exercises.
* [ ] I reviewed all ten exam-style questions.
