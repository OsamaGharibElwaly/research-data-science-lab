# Module 07: Verification, Validation, and Test

## 1. Learning Objectives

By the end of this module, you should be able to:

* Distinguish verification, validation, testing, inspection, and analysis.
* Develop a lifecycle-wide verification and validation strategy.
* Select appropriate methods and define objective acceptance criteria.
* Establish requirements traceability and evidence management.
* Assess test coverage, uncertainty, and residual risk.
* Lead technical readiness and acceptance decisions.

## 2. Verification and Validation Fundamentals

Verification and validation (V&V) provide evidence that a system has been developed correctly and is suitable for its intended purpose.

### Verification

Verification asks:

**Does the system or element satisfy its specified requirements?**

Verification compares objective evidence against defined requirements, specifications, and applicable acceptance criteria.

### Validation

Validation asks:

**Does the resulting system satisfy stakeholder needs and intended use?**

Validation considers the actual operational context, users, mission outcomes, and constraints.

A system may pass verification while failing validation if its requirements do not adequately represent stakeholder needs.

Both activities should be planned from early lifecycle stages through delivery and operation.

## 3. Testing Is Not the Same as V&V

Testing is one method for collecting evidence.

Other methods include:

* Inspection.
* Analysis.
* Demonstration.
* Simulation.
* Formal proof or specialized analytical techniques where appropriate.

Verification and validation are broader engineering activities that establish whether the right questions have been answered and whether the collected evidence supports the required conclusions.

Testing alone cannot always demonstrate properties such as long-term reliability, safety under all conditions, or suitability across every operational scenario.

## 4. The Four Common Verification Methods

### 4.1 Inspection

Examine a system element, artifact, or record.

Examples:

* Confirming that a connector matches a drawing.
* Reviewing configuration records.
* Inspecting a manufactured component.
* Checking required labels and documentation.

### 4.2 Analysis

Use calculations, models, simulations, or other analytical techniques.

Examples:

* Calculating structural loading.
* Analyzing network capacity.
* Estimating reliability.
* Evaluating thermal performance.
* Analyzing timing budgets.

The analysis must use appropriate assumptions, inputs, methods, and uncertainty bounds.

### 4.3 Demonstration

Show that a function or capability operates as expected without necessarily requiring detailed quantitative instrumentation.

Examples:

* Demonstrating a standard user workflow.
* Showing that an operator can complete a prescribed procedure.
* Demonstrating installation or configuration steps.

Demonstration is suitable only when the required evidence does not demand more precise measurement.

### 4.4 Test

Operate an element under specified conditions and measure the resulting behavior.

Examples:

* Measuring response time.
* Testing recovery after power interruption.
* Testing network throughput.
* Measuring sensor accuracy.
* Checking access-control behavior.

A test procedure should define setup, inputs, conditions, instrumentation, steps, expected results, tolerances, and evidence records.

## 5. V&V Planning Across the Lifecycle

A robust strategy identifies V&V activities before implementation makes them difficult or expensive.

A representative sequence includes:

1. Analyze stakeholder needs and intended use.
2. Define verification and validation objectives.
3. Identify applicable requirements and scenarios.
4. Select methods and acceptance criteria.
5. Plan facilities, instrumentation, data, and personnel.
6. Define the required independence of assessment.
7. Execute reviews, analyses, inspections, demonstrations, and tests.
8. Record deviations and investigate failures.
9. Perform corrections and regression testing.
10. Evaluate evidence completeness and residual risk.
11. Support acceptance and release decisions.
12. Capture lessons learned and operational feedback.

V&V plans should be updated when requirements, architecture, configurations, or operating assumptions change.

## 6. Requirements Traceability and Verification Matrices

A verification cross-reference matrix connects each applicable requirement to its verification method, procedure, acceptance criteria, and result.

A useful record contains:

* Requirement identifier.
* Requirement version.
* Verification method.
* Verification procedure.
* Test or analysis configuration.
* Acceptance criteria.
* Execution status.
* Result and evidence location.
* Defects or deviations.
* Approval and disposition.

A separate validation matrix can link stakeholder needs and operational scenarios to validation activities and acceptance evidence.

Traceability supports coverage analysis, but a completed matrix does not independently establish that the requirement is correct or that the evidence is adequate.

## 7. Verification Levels

Verification may occur at different levels, depending on the architecture and lifecycle.

Typical levels include:

* Component or unit verification.
* Subsystem verification.
* Interface verification.
* Integrated system verification.
* System qualification or acceptance verification.

Lower-level verification can establish local correctness, while higher-level verification evaluates integrated behavior and interactions.

The required levels should be derived from system risk, architecture, requirements, and applicable standards rather than applied mechanically.

## 8. Validation in Operational Context

Validation should examine whether the system supports actual stakeholder objectives.

Methods may include:

* Operational trials.
* User acceptance activities.
* Scenario-based evaluations.
* Field demonstrations.
* Simulated mission exercises.
* Human factors studies.
* Performance evaluations using representative workloads.

Validation scenarios should cover important variations in operating conditions, users, environment, workload, and failure recovery.

For safety-critical or regulated systems, validation may require specialized evidence, independent review, or formal approval.

## 9. Test Design and Coverage

A comprehensive test strategy considers more than nominal functional behavior.

Relevant test categories include:

* Functional testing.
* Performance and load testing.
* Stress and endurance testing.
* Reliability and recovery testing.
* Interface and interoperability testing.
* Security testing.
* Usability and accessibility testing.
* Environmental testing.
* Compatibility testing.
* Regression testing.
* Fault injection.
* Acceptance testing.

Test coverage may be measured by requirements, functions, interfaces, scenarios, code, risk items, or operating conditions.

The appropriate coverage model depends on the system. No single coverage measure proves that all important risks have been addressed.

## 10. Negative, Boundary, and Failure Testing

Systems must be assessed under conditions in which inputs, resources, interfaces, or dependencies behave unexpectedly.

Useful approaches include:

* Boundary-value testing.
* Invalid-input testing.
* Timeout and retry testing.
* Resource exhaustion.
* Network interruption.
* Power interruption.
* Sensor or data failure.
* Authentication failure.
* Recovery and restart testing.
* Concurrent activity.
* Degraded operating modes.

Failure testing should be planned carefully so that it does not introduce unacceptable risk into operational systems.

## 11. Test Environment and Measurement Quality

Test results are only as trustworthy as the configuration, instrumentation, procedure, and assumptions supporting them.

Key concerns include:

* Configuration identification.
* Calibration and measurement uncertainty.
* Representative workloads.
* Environment fidelity.
* Data quality.
* Test repeatability.
* Instrumentation limitations.
* Tool qualification where required.
* Independence and competence of evaluators.
* Reproducibility of results.

A result close to an acceptance threshold requires careful treatment of measurement uncertainty and tolerances.

## 12. Defect Management and Regression Testing

When a V&V activity fails:

1. Record the observed deviation.
2. Preserve the relevant configuration and evidence.
3. Assess severity and system impact.
4. Determine whether the issue originates in requirements, design, implementation, integration, or the test itself.
5. Identify root cause.
6. Approve and implement the correction.
7. Repeat the relevant verification activity.
8. Perform regression testing on affected areas.
9. Update traceability and evidence records.
10. Assess whether residual risk is acceptable.

Regression scope should be based on change impact and risk rather than automatically repeating only the failed test.

## 13. Independence and Objective Evidence

The required level of independence depends on the system's criticality, contractual conditions, regulatory obligations, and organizational governance.

Independent assessment can reduce confirmation bias and provide additional confidence in important decisions.

Objective evidence may include:

* Signed test reports.
* Measurement records.
* Analysis reports.
* Inspection records.
* Simulation outputs.
* Approved configuration records.
* Validation findings.
* Defect and corrective-action records.

Evidence should be sufficient, relevant, reproducible where practical, and traceable to the item and configuration assessed.

## 14. Acceptance and Residual Risk

A system should not be declared acceptable merely because most tests pass.

Acceptance decisions should consider:

* Applicable requirements.
* Critical unresolved defects.
* Deviations and waivers.
* Validation results.
* Safety and security findings.
* Operational readiness.
* Support and maintenance capability.
* Configuration completeness.
* Residual risks.
* Decision authority.

Any acceptance of deviations should follow the relevant authorization process and account for mandatory requirements and safety obligations.

## 15. Common Failure Patterns

1. Treating testing as the entire V&V process.
2. Defining acceptance criteria after tests have been executed.
3. Testing requirements without validating the underlying needs.
4. Ignoring configuration differences between environments.
5. Failing to test interfaces and failure conditions.
6. Accepting results without accounting for measurement uncertainty.
7. Repeating a failed test without understanding the cause.
8. Omitting regression tests after changes.
9. Treating a high pass rate as proof of operational suitability.
10. Allowing schedule pressure to override mandatory safety or compliance evidence.

## 16. Practical Exercise

**Scenario:** A remote patient-monitoring platform collects sensor data, evaluates configured conditions, and notifies caregivers.

Develop:

1. A V&V strategy covering the full lifecycle.
2. Five functional verification cases.
3. Five performance or quality verification cases.
4. Three operational validation scenarios.
5. A verification cross-reference matrix.
6. A plan for handling measurement uncertainty.
7. A failure-injection strategy covering communication loss and invalid sensor readings.
8. A regression testing plan for a model or software update.
9. An acceptance review checklist.

Identify which results require specialist clinical, safety, security, or regulatory input. Do not invent clinical thresholds.

## 17. Knowledge Check

**Q1.** How do verification and validation differ?

**Answer:** Verification establishes conformance to specified requirements; validation establishes suitability for stakeholder needs and intended use.

**Q2.** Is testing the only acceptable verification method?

**Answer:** No. Inspection, analysis, demonstration, and other suitable methods may provide the required evidence.

**Q3.** Why should test configurations be recorded?

**Answer:** Results depend on the system version, environment, data, tools, and conditions; configuration records support reproducibility and change impact analysis.

**Q4.** Why is regression testing necessary?

**Answer:** A correction or change may unintentionally affect previously working functionality, interfaces, or system properties.

**Q5.** Can a system pass verification but fail validation?

**Answer:** Yes. It can satisfy its written requirements while those requirements fail to represent real stakeholder needs or intended use.

## 18. Professional Application Evidence

Maintain examples of your ability to:

* Develop a system-level V&V strategy.
* Improve verification coverage or testability.
* Resolve disputed test results.
* Establish objective acceptance criteria.
* Manage deviations and waivers.
* Improve evidence quality and reproducibility.
* Lead acceptance decisions.
* Improve the organization's V&V practices.

Document your role, technical rationale, methods, evidence, results, and lessons learned.

## 19. Key Takeaways

* Verification and validation answer different questions.
* Testing is one method within a broader evidence-based process.
* V&V planning begins early and evolves with the system.
* Traceability and configuration control support reliable conclusions.
* Negative, boundary, and failure scenarios are essential where relevant.
* Acceptance requires consideration of unresolved defects and residual risk.

## 20. Suggested References

* INCOSE, *Systems Engineering Handbook*, applicable edition.
* ISO/IEC/IEEE 15288, *Systems and software engineering — System life cycle processes*.
* ISO/IEC/IEEE 29148, requirements engineering guidance.
* Applicable industry-specific verification, validation, test, safety, and acceptance standards.
