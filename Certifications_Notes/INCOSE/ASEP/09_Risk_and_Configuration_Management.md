# Module 09 — Technical Management Processes

**Course:** INCOSE ASEP Preparation
**File:** `09_Technical_Management_Processes.md`
**Purpose:** Understand the technical management processes that help systems-engineering teams plan, monitor, control, and improve system development throughout the life cycle.

---

## 1. Learning Objectives

By the end of this module, you should be able to:

* Explain the purpose of technical management processes.
* Understand project planning and assessment.
* Apply decision management and trade-off analysis.
* Identify, assess, and manage technical risks.
* Explain configuration management and change control.
* Understand information management and measurement.
* Distinguish risk, issue, assumption, and opportunity.
* Apply technical management processes to a practical engineering project.
* Recognize common technical management concepts in ASEP-style questions.

## 2. What Are Technical Management Processes?

Technical management processes coordinate and control the technical work required to develop, operate, maintain, and retire a system.

They help answer questions such as:

* What work must be completed?
* Who is responsible for each activity?
* Are technical activities progressing as planned?
* What uncertainties could prevent success?
* Which technical alternative should be selected?
* How are changes approved and tracked?
* Are the data and measurements reliable enough to support decisions?

Technical management does not replace technical work. It provides the planning, monitoring, decision-making, and control needed to perform that work effectively.

### 2.1 Core Processes

The principal technical management processes commonly addressed in systems engineering include:

1. Project planning.
2. Project assessment and control.
3. Decision management.
4. Risk management.
5. Configuration management.
6. Information management.
7. Measurement.
8. Quality assurance, where applicable within the organization's process framework.

The precise process names and boundaries depend on the applicable edition of the systems-engineering standard and the organization's life-cycle model.

## 3. Project Planning

Project planning establishes how the technical work will be performed, coordinated, resourced, and evaluated.

### 3.1 Planning Objectives

A project plan should establish:

* Scope and objectives.
* Work breakdown and activities.
* Deliverables.
* Responsibilities.
* Required resources.
* Schedule and milestones.
* Technical methods and tools.
* Dependencies.
* Risks and assumptions.
* Verification and validation activities.
* Communication and reporting arrangements.
* Configuration and information management arrangements.
* Criteria for assessing progress and completion.

### 3.2 Work Breakdown Structure

A **work breakdown structure (WBS)** decomposes project scope into manageable elements.

For example, an enterprise monitoring system might use the following simplified structure:

```text
1. Enterprise Monitoring System
   1.1 Requirements
       1.1.1 Stakeholder needs
       1.1.2 System requirements
   1.2 Architecture and Design
       1.2.1 Sensor architecture
       1.2.2 Communication architecture
       1.2.3 Dashboard architecture
   1.3 Implementation
       1.3.1 Device firmware
       1.3.2 Backend services
       1.3.3 User interface
   1.4 Integration and V&V
       1.4.1 Component integration
       1.4.2 System verification
       1.4.3 Operational validation
   1.5 Transition
       1.5.1 Deployment
       1.5.2 Training and handover
```

The WBS helps organize work and clarify the scope. It does not, by itself, establish the chronological sequence of activities.

### 3.3 Work Packages

A work package is a manageable unit of work that can be assigned, scheduled, resourced, and monitored.

A well-defined work package may specify:

* Objective.
* Scope.
* Deliverable.
* Responsible person or team.
* Start and finish dates.
* Required resources.
* Dependencies.
* Acceptance criteria.
* Reporting requirements.

Weak work package: “Improve the monitoring system.”

Improved work package: “Implement and verify the alert-delivery API against requirements REQ-API-001 through REQ-API-006, with automated tests and a documented verification report.”

### 3.4 Schedule and Dependencies

A project schedule establishes the order and timing of activities.

Dependencies may include:

* **Finish-to-start:** Activity B cannot begin until Activity A finishes.
* **Start-to-start:** Activity B cannot start until Activity A starts.
* **Finish-to-finish:** Activity B cannot finish until Activity A finishes.
* **Start-to-finish:** Activity B cannot finish until Activity A starts; this is less common.

For example, system-level integration may depend on component interfaces being defined and the required components being available.

Poor dependency planning can cause idle resources, late integration, and schedule compression.

### 3.5 Critical Path

The **critical path** is the longest-duration path through a network of schedule activities, given the defined dependencies and durations.

Activities on the critical path generally have zero total float under the schedule assumptions. A delay to one of these activities can delay the project's completion unless the schedule is changed or the delay is recovered.

Example:

| Activity            | Duration | Dependency     |
| ------------------- | -------: | -------------- |
| Requirements        |   5 days | None           |
| Architecture        |   4 days | Requirements   |
| Implementation      |  10 days | Architecture   |
| Integration         |   4 days | Implementation |
| System verification |   5 days | Integration    |

If all activities are sequential, the total duration is:

$$
5+4+10+4+5=28\text{ days}
$$

The actual critical path in a real project requires considering all activities, dependencies, calendars, and available float—not simply adding every listed duration.

## 4. Project Assessment and Control

Planning establishes the intended approach. Assessment determines actual status, while control helps the project respond to deviations.

### 4.1 Assessment

Assessment compares actual performance with planned objectives.

Questions include:

* Are milestones being achieved?
* Are requirements stable and traceable?
* Is integration progressing?
* Are verification activities passing?
* Are risks increasing?
* Are resources sufficient?
* Are technical deliverables acceptable?
* Are changes affecting the schedule or cost?

### 4.2 Control

Control involves taking appropriate action when actual conditions differ from the plan.

Possible responses include:

* Reallocating resources.
* Revising the schedule.
* Reducing scope through an authorized process.
* Addressing a technical dependency.
* Adding verification activities.
* Escalating a risk.
* Revising a plan after approval.
* Correcting inaccurate progress reports.

Control should be based on evidence and authorized decisions, not simply on pressure to meet a deadline.

### 4.3 Leading and Lagging Indicators

A **leading indicator** provides an early signal of a potential future outcome.

Examples:

* Increasing numbers of unresolved high-risk defects.
* Requirements with no verification method.
* Growing interface-change frequency.
* Shortages of integration-ready components.

A **lagging indicator** records an outcome that has already occurred.

Examples:

* Actual cost overrun.
* Missed milestone.
* Production failure rate.
* Number of defects discovered after release.

Using both types can help teams respond before technical problems become major project failures.

## 5. Decision Management

Decision management provides a structured method for choosing among alternatives.

Systems-engineering decisions may affect performance, safety, cost, schedule, maintainability, scalability, and operational suitability.

### 5.1 Decision-Making Process

A typical process includes:

1. Define the decision problem.
2. Identify constraints and required outcomes.
3. Establish evaluation criteria.
4. Identify feasible alternatives.
5. Gather relevant evidence.
6. Evaluate alternatives consistently.
7. Assess uncertainty and sensitivity.
8. Select and authorize an alternative.
9. Record the rationale and assumptions.
10. Review the decision when relevant conditions change.

### 5.2 Example: Selecting a Communication Technology

A monitoring system must communicate sensor readings to a backend service.

Possible alternatives include Wi-Fi, Bluetooth Low Energy, and a cellular connection.

Evaluation criteria may include:

* Power consumption.
* Range.
* Data rate.
* Coverage.
* Infrastructure availability.
* Security.
* Cost.
* Reliability.
* Ease of integration.

The best choice depends on the operational context. Cellular connectivity may offer wider geographic coverage but higher power consumption or recurring costs. Bluetooth Low Energy may suit short-range wearable communication but require a gateway or nearby device.

There is rarely a universally best alternative independent of requirements and constraints.

### 5.3 Weighted Decision Matrix

A weighted decision matrix can compare alternatives against agreed criteria.

Suppose a team evaluates two hypothetical deployment architectures.

| Criterion       | Weight | Architecture A | Architecture B |
| --------------- | -----: | -------------: | -------------: |
| Reliability     |   0.35 |              4 |              5 |
| Cost            |   0.25 |              5 |              3 |
| Maintainability |   0.25 |              4 |              4 |
| Scalability     |   0.15 |              3 |              5 |

Scores range from 1 (poor) to 5 (excellent).

The weighted score is:

$$
S=\sum_{i=1}^{n}w_i s_i
$$

Architecture A:

$$
S_A=(0.35)(4)+(0.25)(5)+(0.25)(4)+(0.15)(3)=4.05
$$

Architecture B:

$$
S_B=(0.35)(5)+(0.25)(3)+(0.25)(4)+(0.15)(5)=4.20
$$

Under these illustrative assumptions, Architecture B scores higher.

However, weighted scores are not objective truth. Results depend on criterion selection, weighting, scoring quality, and uncertainty. A high score must not override mandatory safety, security, legal, or interface constraints.

### 5.4 Decision Records

A decision record should capture:

* The decision question.
* Alternatives considered.
* Evaluation criteria.
* Evidence and analysis.
* Key assumptions.
* Risks and trade-offs.
* The selected alternative.
* Rationale.
* Approval authority.
* Date and conditions for review.

This record helps future engineers understand why a decision was made and whether its original assumptions remain valid.

## 6. Risk Management

Risk management identifies and addresses uncertain events or conditions that could affect project or system objectives.

A risk is not the same as a problem that has already happened.

### 6.1 Risk vs. Issue vs. Assumption vs. Opportunity

| Concept     | Meaning                                                      | Example                                         |
| ----------- | ------------------------------------------------------------ | ----------------------------------------------- |
| Risk        | An uncertain event or condition that could affect objectives | A supplier may deliver a sensor late            |
| Issue       | A current problem requiring action                           | The supplier has missed the delivery date       |
| Assumption  | A proposition treated as true for planning until confirmed   | The deployment site will provide stable power   |
| Opportunity | An uncertain possibility that could improve outcomes         | A reusable module may reduce development effort |

An issue may create new risks, and an assumption may need to be tracked as a source of risk.

### 6.2 Risk Management Process

A common process includes:

1. Identify risks.
2. Analyze causes and consequences.
3. Estimate likelihood and impact.
4. Prioritize risks.
5. Select response strategies.
6. Assign owners.
7. Implement responses.
8. Monitor indicators and triggers.
9. Update risk records.
10. Close risks when appropriate.

### 6.3 Risk Categories

Technical risks may concern:

* Requirements ambiguity.
* Architecture limitations.
* Interface incompatibility.
* Technology maturity.
* Performance shortfalls.
* Reliability.
* Safety.
* Cybersecurity.
* Data quality.
* Integration complexity.
* Verification feasibility.
* Supply-chain availability.
* Obsolescence.

Project risks may concern schedule, budget, staffing, resources, or stakeholder availability.

### 6.4 Likelihood and Impact

A qualitative risk matrix categorizes risk according to likelihood and consequence.

| Likelihood | Impact | Typical interpretation                           |
| ---------- | ------ | ------------------------------------------------ |
| Low        | Low    | Monitor as appropriate                           |
| High       | Low    | Evaluate frequency and cumulative cost           |
| Low        | High   | Prepare contingency measures                     |
| High       | High   | Prioritize mitigation or other approved response |

Organizations may use numerical scales, but the definitions should be clear and consistently applied.

Multiplying ordinal scores does not automatically produce a scientifically precise measure of risk. The underlying definitions and consequences still matter.

### 6.5 Risk Response Strategies

Common strategies for threats include:

* **Avoid:** Change the approach to eliminate the threat or exposure.
* **Mitigate:** Reduce likelihood, consequence, or both.
* **Transfer or share:** Allocate some responsibility or impact through an appropriate arrangement, while recognizing that ultimate accountability may remain.
* **Accept:** Acknowledge the risk and proceed under defined conditions.

For opportunities, teams may use strategies such as exploit, enhance, share, or accept, depending on the framework.

### 6.6 Risk Register

Example:

| ID   | Risk                                                          | Likelihood | Impact    | Response                                                          | Owner            |
| ---- | ------------------------------------------------------------- | ---------- | --------- | ----------------------------------------------------------------- | ---------------- |
| R-01 | Wireless communication may fail in the deployment environment | Medium     | High      | Test representative environments and define recovery behavior     | Systems engineer |
| R-02 | Required sensor delivery may be delayed                       | High       | Medium    | Identify an approved alternative supplier                         | Procurement lead |
| R-03 | Alert latency may exceed the requirement                      | Medium     | High      | Prototype early and measure end-to-end latency                    | Software lead    |
| R-04 | Sensitive data may be exposed through weak access controls    | Low        | Very high | Apply threat analysis, access controls, and security verification | Security lead    |

Risk owners should have the authority and resources needed to monitor and respond to their assigned risks.

### 6.7 Residual Risk

**Residual risk** is the risk remaining after a response has been implemented.

A mitigation does not necessarily eliminate a risk.

For example, adding communication retries may reduce the chance of losing an alert, but residual risk may remain during prolonged outages. The team must determine whether that remaining risk is acceptable under applicable stakeholder, safety, and regulatory requirements.

## 7. Configuration Management

Configuration management establishes and maintains the integrity of system configurations throughout the life cycle.

It ensures the team knows what constitutes the system, what has changed, and which version is approved.

### 7.1 Configuration Items

Configuration items may include:

* Requirements documents.
* Architecture models.
* Interface specifications.
* Source code.
* Executable software.
* Hardware assemblies.
* Firmware.
* Test procedures and results.
* Network configuration files.
* Operational manuals.

The selection of configuration items should be appropriate to system complexity, risk, and organizational requirements.

### 7.2 Configuration Management Activities

Common activities include:

1. Configuration identification.
2. Configuration baseline establishment.
3. Change control.
4. Configuration status accounting.
5. Configuration audits or verification.

### 7.3 Baselines

A baseline is an approved reference configuration.

Examples include:

* Requirements baseline.
* Functional baseline.
* Allocated baseline.
* Product baseline.

These terms are commonly used in configuration management, but their exact definitions and applicability depend on the adopted framework and project practices.

A baseline does not mean that changes are forbidden. It means that changes are controlled, authorized, recorded, and assessed.

### 7.4 Change Control

A proposed change should be evaluated for its effects on:

* Requirements.
* Interfaces.
* Architecture.
* Safety and security.
* Cost and schedule.
* Verification and validation.
* Training and operational procedures.
* Maintenance and support.

A change-control board or another authorized decision-maker may review significant changes, depending on the organization's governance.

### 7.5 Configuration Audits

A configuration audit checks whether the documented configuration corresponds to the actual system and whether required records are complete.

For example, a deployed server may be documented as running one software version but actually run another. That discrepancy can undermine test evidence, security assumptions, and support procedures.

## 8. Information Management

Information management ensures that the right information is created, stored, protected, maintained, and made available to authorized users.

Systems engineering produces many artifacts, including:

* Requirements.
* Models and diagrams.
* Interface definitions.
* Test results.
* Decision records.
* Risk registers.
* Configuration records.
* Operational procedures.
* Maintenance history.

### 8.1 Information Management Objectives

Information should be:

* Accurate.
* Traceable.
* Accessible to authorized users.
* Protected from unauthorized access or modification.
* Available when needed.
* Retained according to applicable policy.
* Organized and version-controlled.
* Understandable to its intended audience.

### 8.2 Information Security

Information management should consider confidentiality, integrity, and availability.

* **Confidentiality:** Prevent unauthorized disclosure.
* **Integrity:** Protect against unauthorized or inappropriate modification.
* **Availability:** Ensure authorized users can access information when required.

Access controls, version history, backups, retention policies, and audit logs can support these objectives.

### 8.3 Knowledge Transfer

Engineering knowledge should not remain only in individual employees' memories.

Useful knowledge-transfer artifacts include:

* Architecture decisions and rationale.
* Known limitations.
* Troubleshooting procedures.
* Interface assumptions.
* Operational lessons learned.
* Maintenance instructions.
* Risk history.
* Unresolved technical questions.

Good information management improves continuity when team members change or systems are transferred between organizations.

## 9. Measurement

Measurement provides quantitative information about system or project characteristics.

Measurement helps answer questions such as:

* Is the system meeting its performance requirements?
* Is reliability improving?
* Is the defect backlog increasing?
* Are planned milestones being achieved?
* Is the system using resources efficiently?

### 9.1 Measurement Process

A typical measurement process includes:

1. Define the information need.
2. Identify the characteristic to measure.
3. Define the measurement method.
4. Establish units and operational definitions.
5. Select tools and data sources.
6. Collect and validate data.
7. Analyze and interpret results.
8. Report findings.
9. Use the results to support decisions.

### 9.2 Useful Engineering Measures

| Area            | Example measure                                    |
| --------------- | -------------------------------------------------- |
| Performance     | Response time                                      |
| Reliability     | Failures per operating hour, under a defined model |
| Availability    | Percentage of required operating time available    |
| Maintainability | Mean time to repair or restore                     |
| Requirements    | Percentage with approved verification evidence     |
| Testing         | Pass rate and unresolved failure count             |
| Project         | Schedule variance                                  |
| Cost            | Actual cost compared with planned cost             |
| Security        | Time to remediate prioritized vulnerabilities      |
| Operations      | Incident rate per defined period                   |

A metric is useful only when its definition, data source, and interpretation are understood.

### 9.3 Leading and Lagging Measures

Examples of leading measures:

* Number of unresolved high-risk interfaces.
* Percentage of requirements with verification methods.
* Number of critical design decisions awaiting approval.
* Trend in high-severity defects during integration.

Examples of lagging measures:

* Actual cost overrun.
* Production outage duration.
* Post-release defect rate.
* Missed contractual milestone.

Leading measures may help anticipate problems, but they do not guarantee a particular outcome.

### 9.4 Measurement Pitfalls

Common mistakes include:

* Measuring activity rather than results.
* Comparing data collected using different definitions.
* Ignoring uncertainty.
* Using a single metric to represent a complex objective.
* Optimizing a metric at the expense of overall system effectiveness.
* Treating correlation as proof of causation.
* Reporting averages without considering important variation.

For example, reducing average response time may conceal a small number of extremely slow responses. Percentiles and distribution analysis may be more informative for latency-sensitive systems.

## 10. Technical Reviews and Quality Assurance

Technical reviews examine whether technical artifacts, designs, or results satisfy their intended objectives and applicable criteria.

Examples include:

* Requirements reviews.
* Architecture reviews.
* Design reviews.
* Test-readiness reviews.
* Verification-result reviews.
* Operational-readiness reviews.

A review should have a defined purpose, appropriate participants, relevant inputs, documented findings, assigned actions, and closure criteria.

**Quality assurance (QA)** focuses on confidence that appropriate processes and standards are being followed. It can include process audits, adherence checks, and examination of quality records.

Quality control activities, in contrast, typically evaluate whether a particular product or output meets specified criteria.

These activities are complementary; neither replaces verification, validation, or effective risk management.

## 11. Integrating Technical Management Processes

Technical management processes reinforce each other.

Consider a change to a monitoring-system alert threshold:

1. **Risk management** assesses the consequences of an incorrect threshold.
2. **Decision management** evaluates proposed threshold alternatives.
3. **Configuration management** controls the approved change.
4. **Information management** preserves the rationale and associated evidence.
5. **Measurement** evaluates the resulting alert performance.
6. **Project assessment and control** monitors the schedule, implementation, and verification status.
7. **Project planning** ensures resources and test activities are available.

The processes work together to maintain technical integrity throughout the life cycle.

## 12. Practical Case Study — SmartBrace Monitoring System

### 12.1 Scenario

A team is developing a wearable monitoring system that collects sensor data, transmits measurements to a backend, and presents alerts through a user interface.

The project has a limited schedule, multiple software components, and requirements related to measurement accuracy, alert latency, battery endurance, and user workflows.

### 12.2 Planning

The team creates a WBS for:

* Requirements and stakeholder analysis.
* Sensor and device implementation.
* Communication and backend development.
* User-interface development.
* Integration and testing.
* Deployment and training.

Dependencies are identified. For example, end-to-end integration requires agreed interface contracts and functioning component builds.

### 12.3 Risk Management

The team identifies several risks:

* Sensor measurements may be inaccurate.
* Wireless communication may introduce latency.
* Backend integration may be delayed.
* Battery endurance may be insufficient.
* Alert behavior may confuse users.

Each risk receives an owner, response strategy, and monitoring approach.

### 12.4 Decision Management

The team compares alternative communication architectures using agreed criteria such as power consumption, latency, reliability, cost, and security.

The selected architecture and rationale are documented so future changes can be evaluated against the original assumptions.

### 12.5 Configuration Management

The team controls:

* Requirements versions.
* Firmware builds.
* API specifications.
* Model versions.
* Deployment configuration.
* Test procedures and reports.

When an alert-processing change is approved, affected requirements and tests are identified before implementation.

### 12.6 Measurement

The team tracks:

* Alert latency.
* Sensor accuracy.
* Battery endurance.
* Integration defect count.
* Requirement verification status.
* Open high-risk items.

Measurements are collected under defined conditions so that results can be compared meaningfully.

### 12.7 Assessment and Control

Suppose alert latency begins to exceed the target during integration.

The team investigates the cause, evaluates schedule impact, updates the risk register, and determines whether the implementation plan or architecture requires adjustment.

The team does not simply report that development is 90% complete. It uses technical evidence to assess whether the system can meet its requirements.

## 13. Exercises

### Exercise 1 — Planning

A project has three subsystems, but their interface definitions have not been approved. The team schedules full-system integration to begin tomorrow.

Identify the planning weakness and recommend two corrective actions.

### Exercise 2 — Decision Matrix

A team evaluates two architectures using the following scores:

| Criterion       | Weight |  A |  B |
| --------------- | -----: | -: | -: |
| Reliability     |   0.40 |  5 |  4 |
| Cost            |   0.30 |  3 |  5 |
| Maintainability |   0.20 |  4 |  4 |
| Scalability     |   0.10 |  4 |  3 |

Calculate both weighted scores. Which alternative scores higher? State one limitation of the result.

### Exercise 3 — Risk or Issue?

Classify each item as a risk, issue, assumption, or opportunity.

1. A required component may become unavailable next quarter.
2. The component supplier has already announced that the delivery is late.
3. The project plan assumes the customer will provide a test environment next week.
4. A reusable software component may shorten implementation time.

### Exercise 4 — Risk Response

A critical requirement may not be met because a new sensor technology has not been sufficiently tested.

Suggest a mitigation strategy and identify evidence that could help determine whether the risk is decreasing.

### Exercise 5 — Configuration Management

A technician modifies a production configuration directly to restore service but does not document the change.

Explain why this is a configuration-management problem and propose a suitable response.

### Exercise 6 — Measurement

A team reports that the average API response time is 120 ms. The requirement specifies that the 95th-percentile response time must not exceed 200 ms.

Can the team claim that the requirement has been satisfied? Explain what information is still needed.

### Exercise 7 — Integrated Scenario

During development, the team discovers that the current architecture cannot satisfy a required battery-life target.

Describe how project planning, risk management, decision management, configuration management, and measurement should work together to address the problem.

---

## 14. Exercise Answer Key

### Exercise 1

The schedule assumes integration can begin before interface definitions and dependencies are sufficiently established.

Corrective actions include:

* Agree on and baseline the interface specifications.
* Verify component compatibility before integration.
* Reassess schedule dependencies and resource availability.
* Plan interface tests and integration entry criteria.

### Exercise 2

Architecture A:

$$
S_A=(0.40)(5)+(0.30)(3)+(0.20)(4)+(0.10)(4)
$$

$$
S_A=2.0+0.9+0.8+0.4=4.10
$$

Architecture B:

$$
S_B=(0.40)(4)+(0.30)(5)+(0.20)(4)+(0.10)(3)
$$

$$
S_B=1.6+1.5+0.8+0.3=4.20
$$

Architecture B scores higher: 4.20 versus 4.10.

Limitation: The result depends on the chosen criteria, weights, scores, and assumptions. A weighted score must not override mandatory constraints.

### Exercise 3

1. Risk.
2. Issue.
3. Assumption.
4. Opportunity.

### Exercise 4

Possible mitigation: Build and test an early prototype, compare its performance against the requirement, evaluate alternative sensors, and define a fallback architecture.

Useful evidence includes controlled test results, accuracy measurements, power-consumption measurements, supplier data, and a documented comparison against the acceptance criteria.

### Exercise 5

The unrecorded change creates uncertainty about the actual approved configuration. It can undermine troubleshooting, security, repeatability, and future verification.

The team should document the change, assess its impact, verify the restored service, review security implications, update configuration records, and determine whether formal approval or further corrective action is needed.

Emergency changes should follow an appropriate emergency change process rather than bypassing accountability.

### Exercise 6

No. An average of 120 ms does not establish that the 95th percentile is at or below 200 ms.

The team needs representative test data, the defined workload and measurement window, a valid percentile calculation, the correct software configuration, and evidence that the test conditions match the requirement.

### Exercise 7

* **Project planning:** Replan activities, dependencies, resources, and schedule.
* **Risk management:** Assess the likelihood and consequences of missing the target and assign mitigation actions.
* **Decision management:** Compare alternatives such as reducing power consumption, changing components, or revising the architecture.
* **Configuration management:** Control approved design changes and update affected baselines.
* **Measurement:** Collect power-consumption data under representative operating conditions and verify the revised design.

The team should not relax the requirement without appropriate stakeholder authorization and an assessment of its consequences.

---

## 15. ASEP-Style Practice Questions

These are original practice questions for study and revision, not official INCOSE examination questions.

### Question 1

What is the primary purpose of project planning?

A. To guarantee that no risks occur
B. To define how project work, resources, activities, and deliverables will be organized
C. To eliminate the need for monitoring
D. To replace system requirements

### Question 2

Which statement best describes a critical path?

A. The path with the least technical complexity
B. The path with the most expensive equipment
C. The longest-duration path through the scheduled activities and their dependencies
D. The list of all project risks

### Question 3

What is the primary purpose of decision management?

A. To ensure every stakeholder gets their preferred alternative
B. To provide a structured and traceable process for evaluating alternatives and selecting an option
C. To prevent changes to the system
D. To avoid documenting assumptions

### Question 4

A supplier may fail to deliver a component next month. How should this initially be classified?

A. An issue that has already occurred
B. A risk
C. A verified defect
D. A completed change request

### Question 5

What is a baseline in configuration management?

A. A guarantee that a system can never change
B. An approved reference configuration against which changes can be controlled
C. A list of employee responsibilities only
D. An informal collection of unapproved files

### Question 6

Which statement about residual risk is correct?

A. It is the risk remaining after risk responses have been applied
B. It is always zero after mitigation
C. It applies only to financial risks
D. It is identical to an issue

### Question 7

What is the principal purpose of information management?

A. To ensure that relevant information is controlled, maintained, protected, and available to authorized users
B. To prevent engineers from documenting decisions
C. To eliminate all project communication
D. To replace configuration management entirely

### Question 8

Which is the best example of a leading indicator?

A. A production outage that has already occurred
B. Final project cost at completion
C. A growing backlog of unresolved high-risk defects before release
D. The number of failures recorded last year

### Question 9

A system meets its average response-time target but fails the specified 95th-percentile limit. What should the team conclude?

A. The system passes because the average is acceptable
B. The system satisfies the requirement if the schedule is at risk
C. The specified performance requirement has not been demonstrated as satisfied
D. The percentile requirement can be ignored without approval

### Question 10

Why should technical decisions be documented?

A. To ensure the original choice can never be reconsidered
B. To preserve the rationale, assumptions, evidence, and conditions relevant to future decisions
C. To remove the need for risk management
D. To avoid communicating with stakeholders

## 16. Practice Question Answer Key

| Question | Answer | Explanation                                                                                   |
| -------- | ------ | --------------------------------------------------------------------------------------------- |
| 1        | B      | Planning defines the approach, resources, activities, and deliverables.                       |
| 2        | C      | The critical path determines the minimum scheduled duration under the model's assumptions.    |
| 3        | B      | Decision management supports structured, evidence-based selection.                            |
| 4        | B      | The future delivery failure is uncertain and therefore a risk.                                |
| 5        | B      | A baseline provides an approved reference for change control.                                 |
| 6        | A      | Risk responses may reduce but not eliminate risk.                                             |
| 7        | A      | Information management supports controlled access, integrity, availability, and traceability. |
| 8        | C      | A growing high-risk defect backlog can indicate future problems.                              |
| 9        | C      | The system must satisfy the stated percentile criterion, not merely an average target.        |
| 10       | B      | Decision records preserve reasoning and assumptions for future evaluation.                    |

## 17. Revision Notes

Remember these principles:

* **Project planning:** Defines the work, schedule, resources, responsibilities, and deliverables.
* **Assessment:** Compares actual technical status with planned objectives.
* **Control:** Takes authorized action to address deviations.
* **WBS:** Decomposes project scope into manageable work elements.
* **Critical path:** Longest-duration path through scheduled dependencies.
* **Decision management:** Structures the evaluation and selection of alternatives.
* **Risk:** An uncertain event or condition that may affect objectives.
* **Issue:** A current problem requiring action.
* **Assumption:** A proposition treated as true for planning but not yet confirmed.
* **Opportunity:** An uncertain possibility for a beneficial outcome.
* **Residual risk:** Risk remaining after responses.
* **Configuration management:** Maintains the integrity and traceability of system configurations.
* **Baseline:** Approved reference configuration.
* **Information management:** Controls and maintains engineering information.
* **Measurement:** Produces defined data to support technical and management decisions.
* **Leading indicator:** Provides an early signal of a possible future outcome.
* **Lagging indicator:** Records an outcome that has already occurred.
* **Weighted decision matrix:** Supports comparison but depends on the quality of criteria, weights, and scores.

### Quick Self-Check

Before moving to the next module, make sure you can:

1. Explain how a WBS supports project planning.
2. Distinguish assessment from control.
3. Calculate a weighted decision score.
4. Differentiate risks, issues, assumptions, and opportunities.
5. Describe the major configuration-management activities.
6. Explain why baselines do not prohibit authorized changes.
7. Identify suitable engineering metrics.
8. Explain why metrics must have consistent definitions.
9. Describe how technical management processes reinforce each other.

## 18. Official References and Further Reading

Consult current editions and applicable revisions.

1. **INCOSE Systems Engineering Handbook** — Technical management processes and their application across the system life cycle.
2. **ISO/IEC/IEEE 15288, Systems and software engineering — System life cycle processes** — Systems life-cycle process framework, including technical management processes.
3. **ISO 31000, Risk management — Guidelines** — Risk-management principles and guidance.
4. **ISO 10007, Quality management — Guidelines for configuration management** — Configuration-management guidance.
5. **ISO/IEC/IEEE 15939, Systems and software engineering — Measurement process** — Measurement concepts and process guidance.
6. **INCOSE Certification Program** — Current ASEP examination and reference guidance.

Official starting points:

* INCOSE: https://www.incose.org/
* INCOSE Certification: https://www.incose.org/certification
* ISO Standards: https://www.iso.org/standards.html
* IEEE Standards Association: https://standards.ieee.org/

Verify the applicable editions and the official examination reference list before using any standard as an exam-specific source. This module is a study aid, not a substitute for official publications.

---

**End of Module 09 — Technical Management Processes**

**Next module:** `10_Agreement_and_Acquisition_Processes.md` — acquisition, supply, agreements, supplier selection, contract requirements, and managing technical responsibilities across organizational boundaries.
