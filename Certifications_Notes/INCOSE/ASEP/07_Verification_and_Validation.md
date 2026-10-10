# Module 07 — Verification and Validation (V&V)

**Course:** INCOSE ASEP Preparation
**File:** `07_Verification_and_Validation.md`
**Purpose:** Understand how systems are verified against requirements and validated for their intended operational use.

---

## 1. Learning Objectives

By the end of this module, you should be able to:

* Distinguish verification from validation.
* Select appropriate verification methods.
* Develop a V&V plan, test procedures, and acceptance criteria.
* Trace requirements to verification evidence.
* Understand verification at different system levels.
* Evaluate test results and manage defects.
* Explain risk-based verification and independence.
* Apply V&V principles to a real systems-engineering case study.

## 2. Core Concepts

### 2.1 Verification

**Verification asks: “Did we build the system right?”**

It determines whether a system element satisfies its specified requirements.

Examples:

* Does a temperature sensor meet its specified accuracy?
* Does an API return the required response format?
* Does a network switch support the required throughput?
* Does a monitoring system generate an alarm within five seconds?

Verification evaluates conformance to defined requirements, specifications, and design constraints.

### 2.2 Validation

**Validation asks: “Did we build the right system?”**

It determines whether the system meets stakeholder needs and intended operational objectives.

Examples:

* Can a doctor use the monitoring system effectively during a real consultation?
* Does the system provide useful information for clinical decisions?
* Can technicians operate and maintain the equipment in its intended environment?
* Does the deployed system solve the original operational problem?

A system can pass verification but fail validation. Every component might meet its specification, yet the complete system may be inconvenient, impractical, or unsuitable for users.

### 2.3 Verification vs. Validation

| Aspect              | Verification                                      | Validation                                                       |
| ------------------- | ------------------------------------------------- | ---------------------------------------------------------------- |
| Main question       | Did we build it right?                            | Did we build the right thing?                                    |
| Primary focus       | Requirements and specifications                   | Stakeholder needs and intended use                               |
| Typical evidence    | Test results, inspections, analyses               | Operational demonstrations, user evaluations, acceptance results |
| Typical environment | Laboratory, test facility, simulated environment  | Representative or actual operational environment                 |
| Example             | Confirming an alarm activates within five seconds | Confirming the alarm helps a nurse respond appropriately         |
| Common failure      | Requirement not satisfied                         | User need not satisfied                                          |

**Exam reminder:** Do not classify an activity only by its name. A test can support verification or validation depending on what is being evaluated and against which criteria.

## 3. Verification and Validation Planning

V&V should be planned early in the system life cycle—not postponed until development is complete.

A V&V plan defines how evidence will be collected to establish that the system satisfies its requirements and stakeholder needs.

### 3.1 Contents of a V&V Plan

A typical plan includes:

1. **Scope:** Which systems, subsystems, components, and interfaces are covered?
2. **Objectives:** What must verification and validation establish?
3. **Requirements:** Which requirements must be evaluated?
4. **Methods:** Will each requirement be tested, analyzed, inspected, or demonstrated?
5. **Resources:** What personnel, facilities, tools, simulators, and equipment are needed?
6. **Environment:** Where will each activity take place?
7. **Responsibilities:** Who prepares, performs, reviews, and approves the activities?
8. **Schedule:** When will each activity occur?
9. **Entry criteria:** What must be true before an activity starts?
10. **Exit criteria:** What conditions must be met before it is considered complete?
11. **Evidence:** What records will prove the result?
12. **Defect management:** How will failures be recorded, investigated, corrected, and retested?
13. **Configuration control:** Which version of the system and test artifacts will be evaluated?
14. **Risks:** What could prevent reliable or safe verification and validation?

### 3.2 Why Early Planning Matters

Consider a requirement:

> The monitoring device shall detect a critical physiological threshold and notify the caregiver within five seconds.

If testing is planned only at the end, the team may discover that it cannot reproduce the physiological input reliably, synchronize timestamps, or capture notification latency.

Early planning identifies these needs before they become expensive schedule problems.

### 3.3 Verification Cross-Reference Matrix

A **verification cross-reference matrix (VCRM)** connects requirements to planned verification activities and results.

| Requirement ID | Requirement                                                                     | Method          | Test ID | Status  |
| -------------- | ------------------------------------------------------------------------------- | --------------- | ------- | ------- |
| REQ-001        | Device battery life shall be at least 12 hours                                  | Test            | BAT-001 | Pass    |
| REQ-002        | Alarm shall activate within 5 seconds                                           | Test            | ALM-001 | Fail    |
| REQ-003        | Enclosure shall meet specified dimensions                                       | Inspection      | MEC-001 | Pass    |
| REQ-004        | Predicted battery life shall meet the target under defined operating conditions | Analysis + test | BAT-002 | Planned |

The matrix helps identify:

* Requirements with no verification method.
* Tests that do not map to requirements.
* Requirements with failed or incomplete evidence.
* Verification activities that must be repeated after a change.

A requirement marked “tested” is not necessarily verified. The test must have valid evidence showing that the acceptance criteria were met.

## 4. Verification Methods

Four commonly used methods are **test, analysis, inspection, and demonstration**.

### 4.1 Test

A test uses controlled inputs and observes measured outputs to determine whether specified criteria are satisfied.

Examples:

* Measure battery endurance under a defined workload.
* Send requests to an API and measure response time.
* Inject a simulated sensor value and observe alarm activation.
* Measure network throughput under a defined traffic profile.

**Strength:** Produces empirical evidence under specified conditions.

**Limitations:** Can require expensive facilities, specialized equipment, representative inputs, and considerable time.

A sound test specifies the input conditions, configuration, measurement method, expected results, and acceptance criteria.

### 4.2 Analysis

Analysis uses calculations, models, simulations, or analytical reasoning to establish whether a requirement is satisfied.

Examples:

* Calculate whether a power budget supports the required operating duration.
* Estimate network capacity from expected traffic.
* Analyze thermal performance using a validated model.
* Evaluate reliability using an appropriate statistical model.

**Strength:** Can assess many conditions that are expensive, dangerous, or impractical to test directly.

**Limitations:** Conclusions depend on assumptions, model validity, input quality, and uncertainty.

Where appropriate, analytical predictions should be supported by test data or other independent evidence.

### 4.3 Inspection

Inspection examines a system element, document, or physical characteristic to determine whether it conforms to specified criteria.

Examples:

* Inspect a device for required dimensions.
* Review a configuration file for required settings.
* Check a connector's labeling and orientation.
* Examine a requirements document for mandatory fields and traceability.

**Strength:** Effective for visible, measurable, or document-based characteristics.

**Limitations:** Inspection alone cannot reliably establish dynamic performance such as end-to-end response time.

### 4.4 Demonstration

Demonstration shows that a system can perform a required function, usually through observable operation with limited instrumentation.

Examples:

* Demonstrate that a technician can start and shut down a system.
* Show that a dashboard displays the required measurements.
* Demonstrate a user workflow using representative scenarios.

**Strength:** Useful for operational functions and user-facing behavior.

**Limitations:** May not provide sufficiently precise quantitative evidence for strict timing, accuracy, or reliability requirements.

### 4.5 Selecting the Method

| Requirement                                       | Suitable method                       | Reason                                                             |
| ------------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------ |
| Battery lasts at least 12 hours                   | Test                                  | Direct measurement of endurance                                    |
| Enclosure length is 100 mm ± 2 mm                 | Inspection or test                    | Direct dimensional measurement                                     |
| Thermal model predicts safe operating temperature | Analysis, supported by testing        | Model-based prediction needs credible assumptions                  |
| User can complete a workflow                      | Demonstration or usability evaluation | Observes task completion                                           |
| API responds within 200 ms at a specified load    | Test                                  | Requires measured response time under defined conditions           |
| Software design follows required coding rules     | Inspection or automated analysis      | Static conformance can be evaluated without executing the software |

The selected method must be appropriate to the requirement and provide evidence of sufficient quality.

## 5. Verification Levels

Verification occurs throughout system decomposition and integration.

### 5.1 Component Verification

Checks an individual component against its allocated requirements.

Examples:

* Verify a sensor's measurement range.
* Unit-test a software function.
* Inspect a power regulator.

### 5.2 Subsystem Verification

Checks integrated groups of components.

Examples:

* Verify a sensor subsystem's accuracy and sampling rate.
* Check communication between an embedded controller and its wireless module.
* Verify a network segment's VLAN and routing behavior.

### 5.3 System Verification

Checks the integrated system against system-level requirements.

Examples:

* Measure end-to-end alert latency.
* Verify overall operating duration.
* Check system performance with multiple components operating simultaneously.

### 5.4 Acceptance Verification

Confirms that the delivered system meets defined acceptance requirements and contractual or organizational criteria.

Acceptance may involve the customer, operator, independent assessor, or another authorized party, depending on the agreement.

**Important:** Acceptance testing and validation are closely related but are not identical. Acceptance is a decision or process governed by agreed criteria; validation is the broader determination that the system fulfills its intended use and stakeholder needs.

## 6. Validation in the Operational Context

Validation should represent the real conditions in which the system is intended to be used.

Relevant factors may include:

* User skills and training.
* Environmental conditions.
* Workload and usage patterns.
* External interfaces and connected systems.
* Maintenance and recovery procedures.
* Safety constraints.
* Operational disruptions and exceptional scenarios.

### 6.1 Operational Scenarios

A good validation scenario describes:

* **Actor:** Who uses or interacts with the system?
* **Starting conditions:** What must already be true?
* **Trigger:** What event initiates the scenario?
* **Actions:** What happens during the scenario?
* **Expected outcome:** What operational result should occur?
* **Success criteria:** How will the outcome be evaluated?

For example, a caregiver receives an alert during a simulated clinical workflow. Validation evaluates not only whether the alert appears, but also whether the caregiver can understand it, identify the affected patient, and take the intended action.

### 6.2 Representative Conditions

Testing only ideal conditions can hide important problems.

A monitoring system may function correctly on a laboratory bench but fail when:

* Wireless connectivity becomes unstable.
* Battery capacity is low.
* The user wears the device incorrectly.
* Multiple devices operate in the same area.
* The system restarts after a power interruption.

Representative scenarios help establish whether the system is suitable for actual use.

For safety-critical applications, operational validation must follow appropriate clinical, regulatory, ethical, and safety requirements. Simulated results must not be represented as evidence of real-world clinical effectiveness unless the applicable evaluation supports that conclusion.

## 7. Test Cases, Procedures, and Acceptance Criteria

A test case defines a particular situation and the expected result. A test procedure provides the detailed instructions for performing the activity.

### 7.1 Essential Test Case Fields

A test case commonly includes:

* Test ID and title.
* Linked requirement IDs.
* Objective.
* Preconditions.
* System configuration and version.
* Equipment and tools.
* Input data.
* Test steps.
* Expected results.
* Acceptance criteria.
* Actual results.
* Pass/fail status.
* Evidence references.
* Tester, date, and environment.
* Defect references, where applicable.

### 7.2 Example Test Case

**Test ID:** ALM-001

**Objective:** Verify that the critical alert activates within five seconds.

**Requirement:** REQ-ALM-001

**Preconditions:**

* The device is running an identified software version.
* The sensor simulator is calibrated or otherwise qualified for the test.
* The system clock and measurement method are configured.
* The notification channel is available.

**Procedure:**

1. Place the system in its specified normal operating state.
2. Apply a representative input that crosses the defined critical threshold.
3. Record the threshold-crossing time.
4. Record the alert activation time.
5. Calculate the elapsed time.
6. Repeat for the required number of trials and specified conditions.

**Acceptance criterion:** Every required trial satisfies the requirement's defined latency criterion, subject to any approved measurement uncertainty and test protocol.

**Evidence:** Time-stamped input and output logs, test configuration, measurement records, and the signed test report.

The number of trials, treatment of boundary values, and allowable uncertainty should be defined before execution—not chosen afterward to obtain a pass.

### 7.3 Good Acceptance Criteria

Acceptance criteria should be:

* Objective.
* Measurable or otherwise clearly observable.
* Traceable to requirements.
* Defined before testing.
* Appropriate to the operational risk.
* Clear about boundary values and uncertainty.

Weak criterion: “The system should be fast.”

Improved criterion: “Under the specified workload and configuration, the 95th-percentile response time shall not exceed 200 ms.”

The percentile, workload, measurement window, and relevant exclusions must be defined so the result is reproducible.

## 8. Evidence, Results, and Reporting

Verification and validation are evidence-based engineering activities.

### 8.1 Evidence Quality

Useful evidence should be:

* **Traceable:** Linked to requirements, test cases, and system versions.
* **Objective:** Based on observable facts and recorded results.
* **Reproducible:** Another qualified person can repeat the activity.
* **Relevant:** Directly supports the claim being made.
* **Reliable:** Produced using suitable equipment and methods.
* **Complete:** Includes relevant conditions, exceptions, and failures.

### 8.2 Typical Evidence

* Raw measurements and instrument logs.
* Test execution records.
* Inspection checklists.
* Analysis reports and model assumptions.
* Simulation results.
* Demonstration records.
* Photographs or video where appropriate.
* Configuration identifiers.
* Defect reports.
* Review approvals and acceptance records.

A screenshot showing that a dashboard opened does not prove that the system meets an end-to-end response-time requirement.

### 8.3 Test Report

A test report should summarize:

1. Objective and scope.
2. Requirement and test-case references.
3. System version and configuration.
4. Environment and equipment.
5. Procedure and deviations.
6. Expected and actual results.
7. Pass/fail status.
8. Evidence locations.
9. Defects and unresolved issues.
10. Conclusions and limitations.
11. Approvals, where required.

Report failures honestly. A failed test is valuable evidence because it exposes a gap that must be understood and addressed.

## 9. Independence and Objectivity

V&V independence refers to the degree of separation between the people developing the system and those evaluating it.

Independence may help reduce bias, particularly where the consequences of failure are serious.

Possible arrangements include:

* Developer performs unit tests.
* A separate integration team verifies interfaces.
* An independent test team evaluates system-level behavior.
* An authorized customer or assessor participates in acceptance.

The appropriate degree of independence depends on risk, contractual obligations, organizational policy, and applicable standards.

**Exam reminder:** Independence does not automatically guarantee correctness. Independent teams still need competent personnel, sound procedures, suitable tools, and adequate evidence.

## 10. Risk-Based Verification

Not every requirement requires the same testing effort.

Risk-based verification prioritizes effort according to the likelihood and consequences of failure, while respecting all mandatory requirements and applicable obligations.

Consider:

| Function                     | Potential consequence                      | Verification priority                                            |
| ---------------------------- | ------------------------------------------ | ---------------------------------------------------------------- |
| Critical physiological alarm | Delayed response to a dangerous condition  | Very high                                                        |
| Battery status display       | User may misjudge remaining operating time | High                                                             |
| Dashboard color preference   | Reduced usability or satisfaction          | Lower, unless accessibility requirements make it safety-relevant |
| Noncritical help text        | User confusion                             | Depends on operational context                                   |

Risk assessment should consider severity, likelihood, detectability, exposure, and the consequences of incorrect system behavior as appropriate to the chosen risk method.

A risk-based strategy may allocate:

* More boundary-condition testing to high-risk requirements.
* More failure-mode testing to critical interfaces.
* Independent review of safety-related evidence.
* Additional regression tests for high-impact changes.
* Greater scrutiny of assumptions in critical analyses.

**Key distinction:** Risk prioritization does not authorize skipping required verification. It helps determine depth, sequence, and resources within applicable constraints.

## 11. Defect and Nonconformance Management

A **defect** is a flaw or problem identified in a system element, artifact, or implementation. A **nonconformance** is a failure to meet a specified requirement or criterion.

Not every defect necessarily causes a demonstrated requirement failure, and not every failure has an immediately known root cause.

### 11.1 Defect Workflow

1. Detect and record the issue.
2. Identify the affected requirement and configuration.
3. Assess severity, operational impact, and safety implications.
4. Investigate the root cause.
5. Approve and implement a correction.
6. Repeat the failed test.
7. Perform regression testing as appropriate.
8. Review evidence and update traceability.
9. Close the issue only when closure criteria are met.

### 11.2 Retesting vs. Regression Testing

* **Retesting:** Repeats the failed activity to determine whether the defect has been corrected.
* **Regression testing:** Checks that a change has not adversely affected previously working functionality.

A corrected alert-timing defect should be retested. Related sensor processing, notification delivery, logging, and other affected functions may also need regression testing.

### 11.3 Configuration Management

Test results apply to a particular configuration.

If firmware, hardware, a model, a network setting, or a test procedure changes, the team must determine whether the existing evidence remains valid.

A report without reliable version information may be impossible to use as defensible verification evidence.

## 12. Common V&V Mistakes

Avoid these frequent mistakes:

1. Treating verification and validation as interchangeable.
2. Defining pass/fail criteria after seeing results.
3. Testing only normal operating conditions.
4. Assuming successful component tests prove system-level correctness.
5. Using a demonstration to prove a quantitative requirement without sufficient measurement.
6. Accepting analysis results without reviewing assumptions.
7. Failing to trace test evidence to requirements.
8. Closing defects without appropriate retesting.
9. Ignoring configuration changes.
10. Reporting only successful tests.
11. Assuming customer acceptance automatically proves every stakeholder need has been satisfied.
12. Treating test coverage as proof that all possible failures have been eliminated.

Passing tests provides evidence against defined criteria; it does not establish that a system can never fail.

## 13. Practical Case Study — SmartBrace Monitoring System

### 13.1 Scenario

A wearable monitoring system collects physiological measurements and notifies a caregiver when a configured critical threshold is crossed.

The team must verify system requirements and validate the system's suitability for its intended workflow.

### 13.2 Example Requirements

| ID         | Requirement                                                                                                         |
| ---------- | ------------------------------------------------------------------------------------------------------------------- |
| SB-REQ-001 | The sensor subsystem shall provide measurements within its specified accuracy limits under defined test conditions. |
| SB-REQ-002 | A critical threshold event shall result in an alert within five seconds under specified operating conditions.       |
| SB-REQ-003 | The device shall operate for at least 12 hours under the defined usage profile.                                     |
| SB-REQ-004 | The system shall record the event time and alert outcome.                                                           |
| SB-REQ-005 | An intended caregiver shall be able to identify the alert and its associated patient in a representative workflow.  |

### 13.3 Verification Strategy

| Requirement | Method                                 | Evidence                                                   |
| ----------- | -------------------------------------- | ---------------------------------------------------------- |
| SB-REQ-001  | Test                                   | Sensor measurements compared with an appropriate reference |
| SB-REQ-002  | Test                                   | Time-stamped threshold input and alert output              |
| SB-REQ-003  | Test                                   | Battery endurance measurements under the specified profile |
| SB-REQ-004  | Test and inspection                    | Event logs and records checked against defined criteria    |
| SB-REQ-005  | Demonstration and usability evaluation | Observed workflow performance and documented evaluation    |

The exact test protocol and acceptable limits must be defined by the system requirements and applicable safety or regulatory constraints.

### 13.4 Validation Strategy

Use a representative simulated-care scenario:

1. Configure the system for a simulated patient.
2. Begin a representative monitoring session.
3. Introduce a simulated critical event.
4. Observe alert presentation and event recording.
5. Ask an intended caregiver to interpret the alert and follow the defined workflow.
6. Record task completion, misunderstandings, delays, and feedback.
7. Compare the outcome with predefined stakeholder acceptance criteria.

This validation evaluates whether the system supports the intended workflow, rather than only whether individual technical requirements pass.

### 13.5 Example Failure Investigation

Suppose the alert activates in 6.2 seconds, while the maximum permitted time is five seconds.

The test fails. The team should:

* Preserve the original test result.
* Confirm the system version and measurement method.
* Check whether the input and output timestamps were recorded correctly.
* Investigate sensor processing, network latency, queueing, and notification handling.
* Determine the root cause.
* Implement an approved correction.
* Repeat the failed test.
* Conduct appropriate regression tests.
* Update the VCRM and defect record.

The original failure must remain part of the test history; it should not be overwritten by the successful retest.

## 14. Exercises

### Exercise 1 — Verification or Validation?

Classify each activity and briefly explain your choice.

1. Measuring whether a sensor meets its specified accuracy.
2. Evaluating whether a caregiver understands and responds appropriately to an alert.
3. Inspecting a housing component against a dimensional drawing.
4. Evaluating whether the overall system solves the stakeholder's operational problem.
5. Measuring API latency against a defined response-time requirement.

### Exercise 2 — Select a Method

Choose the most suitable primary method: test, analysis, inspection, or demonstration.

1. Determine whether the battery supports 12 hours of operation.
2. Check whether a document contains all mandatory approval fields.
3. Calculate expected heat dissipation using a validated engineering model.
4. Show that an operator can complete a specified shutdown procedure.
5. Measure packet loss under a defined network traffic profile.

Some activities may legitimately combine multiple methods. State any assumptions.

### Exercise 3 — Improve the Requirement

Rewrite the following as a measurable requirement:

> The monitoring application should notify the caregiver quickly when a dangerous condition occurs.

Identify at least four details that must be clarified with stakeholders or the system design team.

### Exercise 4 — Test Coverage

A project has 100 approved system requirements. The team has mapped 85 to verification procedures. Of those 85, 70 have passed, 10 have failed, and 5 have not yet been executed.

Calculate:

1. Requirement mapping coverage.
2. The proportion of all requirements with passed verification results.
3. The number of requirements without a mapped verification procedure.

Explain why mapping coverage and successful verification are different measures.

### Exercise 5 — Defect Management

A developer fixes a failed API response-time test. The new test passes, but the software version is not recorded and no regression testing is performed.

Identify at least three weaknesses and recommend corrective actions.

### Exercise 6 — Case Study

A monitoring system passes all component tests but repeatedly loses alerts when wireless connectivity is interrupted.

Explain why component-level success is insufficient and propose an appropriate verification and validation strategy.

---

## 15. Exercise Answer Key

### Exercise 1

1. **Verification:** Compares sensor performance against a specified accuracy requirement.
2. **Validation:** Evaluates whether the system supports the intended user response.
3. **Verification:** Checks physical conformance to a specification.
4. **Validation:** Evaluates whether stakeholder needs are fulfilled.
5. **Verification:** Measures performance against a specified requirement.

### Exercise 2

1. Test.
2. Inspection.
3. Analysis, with model assumptions documented and appropriate supporting evidence.
4. Demonstration.
5. Test.

### Exercise 3

One possible rewrite:

> Under the specified operating conditions, when the measured input crosses the configured critical threshold, the system shall activate the designated caregiver alert within five seconds of the threshold-crossing event.

Clarify:

* The precise definition of a critical threshold.
* The conditions under which the requirement applies.
* Whether the five seconds ends at alert generation, delivery, or presentation to the caregiver.
* The required behavior when connectivity is unavailable.
* Measurement accuracy and timestamp resolution.
* Any required handling of false alarms, repeated alarms, or acknowledgment.

The final wording must reflect agreed stakeholder needs and system constraints.

### Exercise 4

1. Mapping coverage: \(85/100 \times 100 = 85\%\).
2. Passed verification as a proportion of all requirements: \(70/100 \times 100 = 70\%\).
3. Unmapped requirements: \(100 - 85 = 15\).

Mapping coverage shows whether verification has been planned and linked to requirements. It does not show whether the system passed. Failed and unexecuted requirements are mapped but not successfully verified.

### Exercise 5

Weaknesses include:

* The exact software configuration cannot be established.
* The passing result may not be reproducible.
* Related functions may have regressed.
* The correction may not address the actual root cause.
* The verification matrix and defect history may be incomplete.

Corrective actions: identify the tested build, preserve test logs, investigate and document the correction, repeat the failed test under controlled conditions, perform risk-appropriate regression testing, and update traceability records.

### Exercise 6

Component tests do not necessarily establish that integrated components behave correctly during network interruptions.

The team should test end-to-end behavior under normal, degraded, and restored connectivity; verify buffering, retry, alert persistence, and recovery requirements; evaluate timing and data integrity; and inspect event logs. Validation should assess whether the intended caregiver workflow remains effective during communication failures and recovery.

Any required safety behavior must be defined and assessed against applicable system requirements.

---

## 16. ASEP-Style Practice Questions

These are original practice questions designed to reinforce systems-engineering concepts; they are not official INCOSE exam questions.

### Question 1

What is the primary purpose of verification?

A. To determine whether stakeholders like the final system
B. To establish whether specified requirements are satisfied
C. To approve the project budget
D. To eliminate all possible system failures

### Question 2

A component meets every allocated requirement, but users cannot complete their intended workflow with the integrated system. What is the clearest conclusion?

A. Verification and validation must both have succeeded
B. Component verification is irrelevant
C. Validation has identified a possible failure despite component-level success
D. The requirements should automatically be waived

### Question 3

Which method is most appropriate for directly measuring whether an API meets a specified response-time limit?

A. Inspection only
B. Test
C. Demonstration without timing measurements
D. Informal stakeholder discussion

### Question 4

Why should acceptance criteria be defined before test execution?

A. To guarantee that every test passes
B. To avoid recording unexpected results
C. To provide objective, predetermined conditions for judging results
D. To eliminate the need for requirements traceability

### Question 5

What is the main purpose of a verification cross-reference matrix?

A. To replace all test procedures
B. To connect requirements with verification methods, activities, and results
C. To document only failed tests
D. To determine the project budget

### Question 6

A software defect is corrected and the original test passes. Which activity checks that related functions still work correctly?

A. Regression testing
B. Requirements elicitation
C. Stakeholder identification
D. Architecture definition only

### Question 7

Which statement about analysis is most accurate?

A. Analysis is always more reliable than testing
B. Analysis never depends on assumptions
C. Analysis can provide verification evidence when its models, assumptions, and methods are appropriate
D. Analysis is identical to demonstration

### Question 8

What is a key benefit of independent verification?

A. It removes the need for objective evidence
B. It can reduce bias and improve confidence in evaluation
C. It guarantees that no defects remain
D. It eliminates all project risks

### Question 9

A test passes, but the team cannot identify the software version used. What is the principal concern?

A. The requirement automatically becomes invalid
B. The test is necessarily a validation activity
C. The evidence may not be traceable to the delivered configuration
D. The system must be redesigned

### Question 10

Which statement best describes risk-based verification?

A. Only high-risk requirements need verification
B. All requirements can be ignored if the schedule is tight
C. Verification depth and resources are prioritized according to risk while mandatory obligations remain in force
D. Low-risk requirements can never cause operational problems

## 17. Practice Question Answer Key

| Question | Answer | Explanation                                                             |
| -------- | ------ | ----------------------------------------------------------------------- |
| 1        | B      | Verification evaluates conformance to specified requirements.           |
| 2        | C      | Technical conformance does not guarantee suitability for intended use.  |
| 3        | B      | A controlled test directly measures response time.                      |
| 4        | C      | Predetermined criteria reduce ambiguity and result-driven judgment.     |
| 5        | B      | The matrix links requirements to methods, tests, and results.           |
| 6        | A      | Regression testing checks for unintended effects of changes.            |
| 7        | C      | Analysis is useful when its assumptions and models are credible.        |
| 8        | B      | Independence can reduce bias but cannot guarantee correctness.          |
| 9        | C      | Configuration traceability is necessary for reliable evidence.          |
| 10       | C      | Risk helps prioritize effort without automatically waiving obligations. |

## 18. Revision Notes

Memorize these principles:

* **Verification:** Did we build the system right?
* **Validation:** Did we build the right system?
* **Test:** Apply inputs and measure outputs.
* **Analysis:** Use calculations, models, or simulations.
* **Inspection:** Examine an item or artifact for conformance.
* **Demonstration:** Show that a function or procedure can be performed.
* **VCRM:** Links requirements to verification activities and evidence.
* **Retesting:** Checks whether a previously failed test now passes.
* **Regression testing:** Checks whether a change has affected other functions.
* **Acceptance:** Determines whether agreed acceptance conditions are met.
* **Risk-based verification:** Prioritizes effort according to risk without automatically removing mandatory verification.
* **Configuration management:** Establishes which version the evidence applies to.
* **Evidence quality:** Evidence should be relevant, objective, traceable, reproducible, and sufficiently complete.
* **Coverage is not success:** A mapped requirement may still fail or remain untested.

### Quick Self-Check

Before moving on, make sure you can explain:

1. Why verification and validation are different.
2. When to use each of the four verification methods.
3. How requirements traceability supports V&V.
4. What a complete test case contains.
5. Why failed tests must remain documented.
6. How regression testing differs from retesting.
7. Why operational scenarios matter during validation.
8. How configuration changes affect the validity of existing evidence.

## 19. Official References and Further Reading

Use the current editions and applicable revisions of these publications. Check INCOSE's official certification guidance for the references and handbook edition relevant to your exam.

1. **INCOSE Systems Engineering Handbook** — Review the life-cycle processes and material on verification, validation, integration, requirements, and technical assessment.
2. **ISO/IEC/IEEE 15288, Systems and software engineering — System life cycle processes** — Provides the systems life-cycle process framework, including verification and validation.
3. **ISO/IEC/IEEE 29148, Systems and software engineering — Life cycle processes — Requirements engineering** — Supports requirements quality, traceability, and the relationship between requirements and verification.
4. **ISO/IEC/IEEE 29119 series, Software testing** — Provides software-testing concepts and guidance for test processes, documentation, and techniques. Apply the relevant parts to the project's scope.
5. **INCOSE Certification Program official website** — Consult current ASEP eligibility, examination, and handbook guidance.

Official starting points:

* INCOSE: https://www.incose.org/
* INCOSE Certification: https://www.incose.org/certification
* ISO standards catalogue: https://www.iso.org/standards.html
* IEEE Standards Association: https://standards.ieee.org/

**Study recommendation:** Read the applicable handbook sections alongside this module, then practice explaining each concept in your own words and applying it to a system example. Treat this document as a study aid, not a replacement for the current official reference material.

---

**End of Module 07 — Verification and Validation**

**Next module:** `08_System_Transition_and_Operation.md` — system transition, deployment, operational readiness, maintenance, support, and system disposal across the life cycle.
