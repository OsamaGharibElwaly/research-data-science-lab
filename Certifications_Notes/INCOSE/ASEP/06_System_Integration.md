# Module 06: System Integration

## 1. Learning Objectives

After completing this module, you should be able to:

* Explain the purpose of system integration.
* Distinguish integration from verification and validation.
* Develop an integration strategy and integration sequence.
* Understand interface compatibility and integration dependencies.
* Explain bottom-up, top-down, and hybrid integration.
* Identify integration risks and failure modes.
* Understand integration testing, regression testing, and defect management.
* Apply integration planning to a realistic engineering project.

---

## 2. What Is System Integration?

**System integration** is the process of combining system elements and ensuring that they interact to form the intended system.

Elements may include hardware, software, subsystems, people, procedures, facilities, and external services.

Integration addresses questions such as:

* Do the elements connect correctly?
* Are their interfaces compatible?
* Can they exchange information as intended?
* Do their timing and performance characteristics work together?
* Does the integrated system behave correctly under normal and abnormal conditions?
* Are the required capabilities achieved when the elements operate together?

### Why Integration Is Necessary

A component can pass its individual tests and still fail when connected to another component.

Examples include:

* Two services interpret timestamps differently.
* A sensor reports measurements in unexpected units.
* A software component assumes that another service is always available.
* A controller issues commands faster than an actuator can respond.
* A user interface displays stale information as current.
* A security mechanism prevents legitimate communication between services.

Integration helps identify these problems at the boundaries between elements and at the system level.

---

## 3. Integration vs. Verification vs. Validation

These activities are related but have different purposes.

| Activity     | Main purpose                                                             |
| ------------ | ------------------------------------------------------------------------ |
| Integration  | Combine elements and establish correct interactions                      |
| Verification | Demonstrate that specified requirements are satisfied                    |
| Validation   | Evaluate whether the system satisfies stakeholder needs and intended use |

### Example: Smart Parking System

**Integration:** Connect occupancy sensors, gateways, backend services, and the mobile application.

**Verification:** Test that the system processes occupancy messages and displays the required status under defined conditions.

**Validation:** Determine whether drivers and parking operators can use the complete system to achieve the intended operational objectives.

Integration may include verification activities, but simply connecting components does not prove that all requirements are satisfied.

Similarly, a system can pass technical tests but still fail to support the intended operational workflow.

---

## 4. Integration Planning

Integration should be planned during system definition and design rather than postponed until all components are complete.

An integration plan may define:

* Elements to be integrated
* Integration sequence
* Interface requirements
* Required test environments
* Equipment and tools
* Test data
* Entry and exit criteria
* Responsibilities
* Defect-handling procedures
* Configuration identification
* Required verification evidence
* Risks and fallback arrangements

### Why Early Planning Matters

Early planning can reveal:

* Missing interface specifications
* Incompatible assumptions
* Unavailable test equipment
* External dependencies
* Unclear component ownership
* Difficult-to-reproduce failures
* Inadequate test data
* Integration work that exceeds the schedule

For example, a backend team should not discover at the end of development that the gateway uses an undocumented message format.

---

## 5. Integration Strategies

Integration strategies describe how elements are combined and evaluated.

### 5.1 Bottom-Up Integration

Bottom-up integration starts with lower-level elements and progressively integrates them into higher-level structures.

A simplified sequence is:

```text
Component A + Component B
            |
            v
       Subsystem 1

Component C + Component D
            |
            v
       Subsystem 2

Subsystem 1 + Subsystem 2
            |
            v
        Complete System
```

**Advantages:**

* Lower-level interfaces can be tested early.
* Foundational components can be stabilized before higher-level integration.
* Useful infrastructure and reusable components can be validated early.

**Limitations:**

* System-level behavior may not be visible until later.
* Higher-level functions may need temporary test drivers or simulated components.
* Problems in overall architecture may remain hidden if only lower-level tests are performed.

### 5.2 Top-Down Integration

Top-down integration begins with higher-level structures and progressively introduces lower-level implementations.

When a lower-level component is unavailable, a temporary substitute may be used.

**Advantages:**

* High-level behavior can be demonstrated early.
* Important workflows and interfaces can be evaluated.
* Stakeholders may provide feedback before every component is complete.

**Limitations:**

* Temporary substitutes may not reproduce actual component behavior.
* Detailed lower-level issues may remain hidden.
* The team may need to replace simulated components repeatedly.

### 5.3 Hybrid Integration

Hybrid integration combines bottom-up and top-down approaches.

For example, a team may integrate critical data-processing components bottom-up while developing the user-facing workflow top-down.

Hybrid integration can balance early system-level feedback with early verification of foundational components.

### 5.4 Big-Bang Integration

Big-bang integration combines many or all components at approximately the same time.

It may appear straightforward for very small systems, but it carries significant risk.

When numerous components are integrated simultaneously, failures may be difficult to isolate because many interfaces and assumptions are involved.

For complex systems, incremental integration generally provides better opportunities to identify and resolve defects systematically.

---

## 6. Integration Order and Dependencies

The order of integration should reflect technical dependencies, risk, and the value of early feedback.

Suppose a system contains:

* Sensors
* Gateway
* Data-ingestion service
* Database
* Analytics service
* Alert service
* User interface

A possible sequence is:

1. Verify sensor and gateway interfaces.
2. Integrate the gateway with the ingestion service.
3. Integrate ingestion with data storage.
4. Integrate analytics with validated data.
5. Integrate alert generation with analytics.
6. Connect the user interface to the relevant APIs.
7. Test the complete end-to-end workflow.
8. Introduce representative failure scenarios.

This is only one possible sequence. If user workflow uncertainty is the largest risk, an early interface prototype may be more valuable.

### Dependency Graph

An integration dependency graph identifies which elements must be available or stable before other integrations can proceed.

```text
Sensor
   |
   v
Gateway
   |
   v
Ingestion Service
   |
   +--------> Database
   |             |
   v             v
Analytics Service
   |
   v
Alert Service
   |
   v
User Interface
```

The actual architecture may contain parallel paths, feedback, shared services, and alternative data flows.

Integration planning should identify these dependencies and determine which can be developed and tested in parallel.

---

## 7. Interface Compatibility

Interfaces must be compatible in both structure and behavior.

### Structural Compatibility

Elements agree on:

* Message formats
* Data types
* Units
* Identifiers
* Protocols
* Electrical or mechanical connections
* Version definitions

### Behavioral Compatibility

Elements agree on:

* Timing
* Ordering
* Error handling
* Retry behavior
* State transitions
* Initialization
* Recovery
* Ownership of shared resources

### Example: API Integration

A service returns:

```json
{
  "status": "critical",
  "timestamp": "2026-10-10T10:30:00Z"
}
```

The receiving application expects the field `severity` instead of `status`.

The response may be valid JSON, but the interface contract is incompatible with the receiver's expectations.

A different problem occurs if both sides use the same field names but disagree about whether timestamps represent event time or receipt time.

Integration testing should check both the structure and the meaning of exchanged information.

---

## 8. Stubs, Drivers, Simulators, and Test Harnesses

Integration may begin before all real components are available.

Temporary test support can help exercise interfaces and behavior.

### Stub

A stub is a simplified replacement for a component or service, often used to provide predetermined responses.

Example: A temporary authentication service returns an approved test result so that the user interface can be exercised before the real identity service is ready.

### Driver

A driver is a test component that invokes or stimulates another component.

Example: A test script sends predefined messages to a data-ingestion service.

### Simulator

A simulator models relevant behavior of a real system or component.

Example: A simulated sensor generates temperature readings and fault conditions.

### Test Harness

A test harness is a collection of tools, scripts, configuration, and supporting components used to execute tests and collect results.

### Important Limitation

A component passing tests with a stub does not establish that it will integrate successfully with the real component.

Temporary test components should be identified and their limitations understood. They should be replaced or supplemented by tests using representative implementations before the system is accepted.

---

## 9. Integration Test Levels

Integration can be evaluated at different levels.

### Component Integration

Checks interactions between closely related components.

Example: A parser correctly passes validated measurements to a processing function.

### Subsystem Integration

Checks interactions among components forming a subsystem.

Example: A gateway combines sensor acquisition, buffering, and communication functions.

### System Integration

Checks interactions across major system elements.

Example: A sensor reading travels through the gateway and backend and appears correctly in the operator dashboard.

### External-System Integration

Checks interaction with systems outside the defined system boundary.

Example: A monitoring platform sends notifications through an external messaging provider.

### End-to-End Integration

Exercises a complete operational path from an initiating event to the resulting output or action.

Example:

1. A simulated sensor detects a defined condition.
2. The gateway transmits the measurement.
3. The backend validates and processes it.
4. The alert service generates a notification.
5. The operator receives and acknowledges the alert.
6. The system records the relevant events.

End-to-end tests are valuable, but they do not replace focused tests that help isolate failures.

---

## 10. Integration Entry and Exit Criteria

Integration should be governed by defined readiness and completion conditions.

### Entry Criteria

Examples include:

* The component version is identified.
* Required interface specifications are available.
* Component-level checks are complete where required.
* The test environment is ready.
* Dependencies are available or represented by approved substitutes.
* Test data and procedures are prepared.
* Known limitations are documented.

### Exit Criteria

Examples include:

* Required interface tests have passed.
* Critical defects have been resolved or handled under approved criteria.
* Required end-to-end scenarios have passed.
* Results and test configurations are recorded.
* Remaining issues have owners and dispositions.
* The next integration stage is authorized.

Entry and exit criteria should be proportionate to the risk and importance of the integration.

A team should not declare integration complete merely because all components are connected.

---

## 11. Integration Defects and Fault Isolation

When integration fails, the team needs to determine where the failure originates and why it occurs.

Possible causes include:

* Incorrect implementation
* Incompatible interfaces
* Incorrect assumptions
* Configuration differences
* Missing dependencies
* Timing problems
* Resource exhaustion
* Environmental differences
* Invalid test data
* Inadequate requirements

### Fault-Isolation Process

1. Reproduce the failure.
2. Record the configuration and conditions.
3. Identify the earliest observable point of deviation.
4. Inspect relevant logs and measurements.
5. Compare expected and actual interface behavior.
6. Isolate components or replace dependencies with controlled test doubles when useful.
7. Identify the root cause.
8. Correct the problem.
9. Repeat the relevant test.
10. Run regression tests for affected functions and interfaces.

### Example

The dashboard shows an incorrect machine temperature.

Possible causes include:

* Sensor calibration error
* Incorrect unit conversion
* Corrupted message
* Incorrect database mapping
* Stale data
* Incorrect dashboard formatting

The team should trace the measurement through the system rather than immediately assuming that the dashboard is responsible.

---

## 12. Regression Testing

**Regression testing** checks whether a change has caused previously working functionality to fail.

It is particularly important after:

* Fixing integration defects
* Changing interfaces
* Updating libraries
* Modifying configuration
* Replacing hardware
* Changing data models
* Deploying software updates

### Example

A developer fixes an API field-name mismatch.

The original interface test now passes, but the change also affects a reporting service that consumes the same API.

Regression testing checks both the corrected interface and the dependent reporting functionality.

The extent of regression testing should be determined by impact analysis, system risk, and the project's verification strategy.

---

## 13. Integration and Configuration Management

Integration results depend on knowing exactly which components and configurations were tested.

The test record should identify relevant items such as:

* Hardware revision
* Software version
* API or interface version
* Configuration parameters
* Test data
* Environment
* External dependencies
* Test procedure
* Results and defects

Without this information, a passing test may not be reproducible.

### Example

An integration test passes on a developer's machine but fails in the production environment.

Possible differences include:

* Dependency versions
* Network rules
* Credentials
* Environment variables
* Operating-system configuration
* Database schema
* Resource limits

Configuration control and reproducible environments help distinguish implementation defects from environmental differences.

---

## 14. Integration Risk Management

Integration risks should be identified early and monitored throughout development.

Typical risks include:

* Undefined interfaces
* Late availability of critical components
* Unstable requirements
* Poorly understood dependencies
* Incompatible supplier products
* Inadequate test infrastructure
* Unrepresentative test data
* Insufficient system-level testing
* Limited fault-isolation capability

### Risk Reduction Strategies

Possible strategies include:

* Define interfaces early.
* Integrate high-risk elements early.
* Use representative prototypes.
* Automate repeatable tests.
* Establish clear component ownership.
* Maintain controlled interface specifications.
* Use representative environments.
* Monitor integration defects and unresolved dependencies.
* Plan fault-injection and recovery testing where appropriate.

Integration order should not be based only on convenience. It should also consider risk and the consequences of late discovery.

---

## 15. Practical Case Study: SmartBrace Monitoring System

### Scenario

A wearable device collects patient measurements and transmits them to a backend service. The backend stores data, processes approved rules, and presents alerts to authorized users.

### Step 1: Identify Elements

* Wearable sensor hardware
* Embedded software
* Communication service
* Backend ingestion service
* Data storage
* Analytics and alerting
* User interface
* Identity and access-control services
* Monitoring and audit services

### Step 2: Identify Critical Interfaces

* Sensor-to-embedded software
* Device-to-backend communication
* Backend-to-database
* Analytics-to-alert service
* Backend-to-user interface
* Application-to-identity service

### Step 3: Define the Integration Sequence

A possible sequence is:

1. Verify measurement acquisition and representation.
2. Integrate acquisition with device communication.
3. Integrate device communication with backend ingestion.
4. Integrate ingestion with data storage.
5. Integrate validated data with approved processing rules.
6. Integrate alert generation and delivery.
7. Integrate the user interface and access control.
8. Test end-to-end scenarios.
9. Test defined communication-loss and recovery conditions.

### Step 4: Define Test Scenarios

Include:

* Valid measurements
* Missing measurements
* Delayed messages
* Duplicate messages
* Incorrect units
* Invalid identifiers
* Communication loss
* Backend unavailability
* Unauthorized access attempts
* Recovery and synchronization

### Step 5: Record Evidence

For each integration test, record:

* Test identifier
* Requirement or interface reference
* Component versions
* Test environment
* Input data
* Expected behavior
* Actual behavior
* Pass/fail result
* Defect reference
* Retest result

### Step 6: Validate the Complete Workflow

The complete system should be evaluated against its intended operational use by representative users and qualified stakeholders.

Passing individual interface tests is not enough to establish that the workflow is suitable.

This case is educational; actual healthcare deployment requires appropriate clinical, safety, security, and regulatory evaluation.

---

## 16. Exercises

### Exercise 1: Select an Integration Strategy

A system includes an established sensor subsystem, a new analytics service, and a user interface that stakeholders want to evaluate early.

Recommend an integration strategy and explain the trade-offs.

### Exercise 2: Identify Interface Problems

A gateway sends a timestamp representing event time. The backend interprets it as receipt time.

Explain the problem, identify possible consequences, and propose a corrective action.

### Exercise 3: Build an Integration Sequence

A system contains:

* Sensor
* Gateway
* Data-ingestion service
* Database
* Analytics service
* Alert service
* User interface

Propose an integration sequence. Identify two dependencies that could prevent progress.

### Exercise 4: Stubs and Simulators

The real sensor hardware will not be available for six weeks.

Explain how the team can continue integration work and what limitations must be addressed before final acceptance.

### Exercise 5: Fault Isolation

A dashboard displays an incorrect value, but the system's individual components have passed their unit tests.

Describe a systematic fault-isolation approach.

### Exercise 6: Integration Readiness

Develop five entry criteria and five exit criteria for integrating a backend service with a user interface.

### Exercise 7: Regression Testing

A change to an API schema fixes one service but may affect three other services.

Explain how to determine the appropriate regression-test scope.

### Exercise 8: Configuration Control

An integration test passes, but the team cannot identify which software version was tested.

Explain why the evidence is insufficient and identify what information should have been recorded.

---

## 17. Exercise Answers

### Answer 1

A hybrid approach is reasonable.

The established sensor subsystem can be integrated bottom-up with the gateway, while the user interface can be developed and evaluated top-down using a stubbed analytics service. The real analytics service should then be integrated and tested.

The team must recognize that simulated behavior does not establish compatibility with the final service.

### Answer 2

The components interpret the same field differently. This may produce incorrect ordering, misleading latency measurements, or inaccurate decisions.

The interface specification should define the meaning, time basis, format, and synchronization assumptions for timestamps. Integration tests should verify event-time and receipt-time handling, including delayed messages.

### Answer 3

A possible sequence is:

1. Sensor and gateway
2. Gateway and ingestion service
3. Ingestion service and database
4. Database and analytics service
5. Analytics and alert service
6. Alert service and user interface
7. End-to-end testing

Potential dependencies include the approved message schema and the availability of the asset-identifier registry.

### Answer 4

The team can use a sensor simulator to generate representative measurements and faults, and a test harness to exercise the gateway and backend.

Before final acceptance, the team must integrate representative real hardware, verify physical and communication interfaces, and assess behavior that the simulator cannot adequately reproduce.

### Answer 5

Reproduce the issue and record the configuration. Trace the value from the original measurement through the gateway, backend, database, API, and user interface. Compare the value at each boundary, inspect logs, verify units and timestamps, isolate components if useful, correct the root cause, and perform regression testing.

### Answer 6

Possible entry criteria:

* The interface specification is approved.
* The service version is identified.
* Required APIs are available.
* The test environment is configured.
* Test cases and data are prepared.

Possible exit criteria:

* Required interface tests pass.
* Error handling has been tested.
* Relevant performance criteria are met.
* Critical defects are resolved or formally dispositioned.
* Results and configuration records are complete.

### Answer 7

Use impact analysis to identify dependent services, shared schemas, affected requirements, and high-risk workflows. Prioritize tests based on the change's scope and consequences. Run the affected interface tests and end-to-end regression tests, with broader regression testing where shared dependencies or high system risk justify it.

### Answer 8

The result cannot be reliably reproduced or associated with a specific configuration.

The record should identify software versions, interface versions, configuration parameters, environment, test data, procedures, dependencies, results, and defect references.

---

## 18. Exam-Style Practice Questions

These are original study questions, not official INCOSE examination questions.

### Question 1

What is the primary purpose of system integration?

A. To define stakeholder needs for the first time.
B. To combine system elements and establish their intended interactions.
C. To eliminate the need for verification.
D. To replace configuration management.

### Question 2

Which approach begins with lower-level elements and progressively combines them into higher-level structures?

A. Bottom-up integration.
B. Top-down integration.
C. Big-bang integration only.
D. Retirement planning.

### Question 3

Why might a team use a stub?

A. To prove that the final real component is fully verified.
B. To simulate a component's responses while other integration work proceeds.
C. To permanently replace all system testing.
D. To remove interface specifications.

### Question 4

What is a major risk of big-bang integration?

A. It guarantees that all defects are found early.
B. Failures may be difficult to isolate when many elements are combined simultaneously.
C. It prevents components from communicating.
D. It eliminates all schedule dependencies.

### Question 5

What is the main purpose of regression testing?

A. To check whether a change has broken previously working behavior.
B. To identify stakeholders for the first time.
C. To replace all acceptance testing.
D. To guarantee that no future defect will occur.

### Question 6

A system's individual components pass unit tests, but the integrated system fails. What is a likely area to investigate?

A. Interface compatibility, timing, configuration, or interactions.
B. Only the user-interface color scheme.
C. Only the project budget.
D. Whether component testing should be prohibited.

### Question 7

Which statement about integration and verification is correct?

A. They are identical activities.
B. Integration combines elements; verification demonstrates compliance with specified requirements.
C. Verification is unnecessary after integration.
D. Integration occurs only after retirement.

### Question 8

Why should integration results identify component versions?

A. To make test evidence reproducible and associated with a known configuration.
B. To eliminate the need for test procedures.
C. To guarantee that all interfaces are compatible.
D. To prevent authorized updates.

### Question 9

When should integration planning begin?

A. Only after all components have been completed.
B. During early engineering so interfaces, dependencies, and risks can influence design.
C. Only after the system has entered operation.
D. Only when an integration defect occurs.

### Question 10

A simulated component passes integration tests, but the final hardware is never tested. What is the strongest conclusion?

A. Final hardware compatibility is automatically proven.
B. The simulation provides useful evidence, but untested hardware-specific behavior remains uncertain.
C. Hardware integration is unnecessary.
D. All system requirements are automatically validated.

### Answer Key

| Question | Answer | Explanation                                                                 |
| -------- | ------ | --------------------------------------------------------------------------- |
| 1        | B      | Integration combines elements and establishes intended interactions.        |
| 2        | A      | Bottom-up integration progresses from lower-level elements.                 |
| 3        | B      | A stub enables testing before the real dependency is available.             |
| 4        | B      | Simultaneous integration can make failures harder to isolate.               |
| 5        | A      | Regression tests detect unintended effects of changes.                      |
| 6        | A      | System failures often arise from interactions or configuration differences. |
| 7        | B      | Integration and verification have distinct but related purposes.            |
| 8        | A      | Configuration identification supports reproducibility and traceability.     |
| 9        | B      | Early planning exposes dependencies and interface risks.                    |
| 10       | B      | Simulation cannot establish every property of the final hardware.           |

---

## 19. Revision Notes

* **Integration:** Combining elements and establishing intended interactions.
* **Bottom-up integration:** Integrating lower-level elements first.
* **Top-down integration:** Beginning with higher-level structures and progressively adding lower-level elements.
* **Hybrid integration:** Combining integration approaches.
* **Stub:** A simplified replacement that provides predefined responses.
* **Driver:** A test component that stimulates another component.
* **Simulator:** A model that reproduces selected behavior of a real system.
* **Test harness:** Tools and supporting components used to execute and record tests.
* **Integration test:** Test of interactions among components or system elements.
* **End-to-end test:** Test of a complete operational path.
* **Regression testing:** Testing to detect unintended effects of changes.
* **Fault isolation:** Systematic identification of the source of a failure.
* **Entry criteria:** Conditions required before integration begins.
* **Exit criteria:** Conditions required before integration is considered complete.

### Final Self-Assessment

You are ready to move on when you can:

1. Explain why individually tested components may fail during integration.
2. Compare bottom-up, top-down, and hybrid integration.
3. Plan an integration sequence based on dependencies.
4. Explain how stubs and simulators support development.
5. Distinguish integration, verification, and validation.
6. Describe fault isolation and regression testing.
7. Explain why configuration identification is essential to integration evidence.

---

## 20. References and Further Reading

1. **INCOSE Systems Engineering Handbook** — consult the current edition for implementation, integration, verification, and technical management.
2. **ISO/IEC/IEEE 15288, Systems and software engineering — System life cycle processes** — for system life-cycle process context.
3. **ISO/IEC/IEEE 29119 series** — for software testing concepts where software integration testing is relevant.
4. **INCOSE Certification Program:** https://www.incose.org/certification/
5. **ISO standards catalogue:** https://www.iso.org/standards.html

Confirm the applicable editions and the current official ASEP examination reference requirements.

## Completion Checklist

* [ ] I can explain the purpose of system integration.
* [ ] I can compare integration strategies.
* [ ] I can plan an integration sequence.
* [ ] I understand interface compatibility and dependency management.
* [ ] I can explain stubs, drivers, and simulators.
* [ ] I understand integration testing and regression testing.
* [ ] I can describe entry and exit criteria.
* [ ] I completed all eight exercises.
* [ ] I reviewed all ten exam-style questions.
