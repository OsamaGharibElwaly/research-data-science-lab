# Module 08 — System Transition, Operation, Maintenance, and Disposal

**Course:** INCOSE ASEP Preparation
**File:** `08_System_Transition_and_Operation.md`
**Purpose:** Understand how a system moves from development into operational use, how it is operated and maintained, and how it is eventually retired or disposed of.

---

## 1. Learning Objectives

By the end of this module, you should be able to:

* Explain system transition, operation, maintenance, and disposal.
* Identify operational readiness requirements.
* Develop a transition and deployment strategy.
* Understand installation, configuration, training, and acceptance.
* Explain maintenance strategies and logistics support.
* Apply configuration management throughout operations.
* Understand incident management, upgrades, and operational feedback.
* Plan system retirement and environmentally responsible disposal.
* Apply these concepts to practical systems-engineering scenarios.

## 2. System Life-Cycle Overview

A system is not complete merely because its development and verification activities have finished. It must be transitioned into its intended environment, operated effectively, maintained throughout its service life, and eventually retired.

A simplified life-cycle sequence is:

1. Concept and stakeholder needs.
2. Requirements definition.
3. Architecture and design.
4. Implementation.
5. Integration.
6. Verification and validation.
7. Transition.
8. Operation.
9. Maintenance.
10. Disposal.

These activities may overlap or repeat. Operational feedback can lead to new requirements, design changes, upgrades, or another verification cycle.

### 2.1 Transition

**Transition** prepares and transfers a system from its development or acquisition environment into its intended operational environment.

Typical activities include:

* Installation and deployment.
* Configuration and data migration.
* Operational acceptance.
* User and maintenance training.
* Documentation delivery.
* Readiness assessment.
* Handover to the operational organization.

### 2.2 Operation

**Operation** is the use of the system to deliver its intended capabilities within its operational environment.

Typical activities include:

* Monitoring system status.
* Executing operational procedures.
* Managing users and access.
* Responding to alarms and incidents.
* Tracking performance and availability.
* Recording operational data and feedback.

### 2.3 Maintenance

**Maintenance** preserves or restores a system's ability to perform its required functions.

Examples include:

* Replacing failed components.
* Applying software patches.
* Calibrating sensors.
* Updating configurations.
* Repairing hardware.
* Replacing aging equipment.
* Improving reliability and maintainability.

### 2.4 Disposal

**Disposal** removes a system from service and manages its retirement safely, securely, and responsibly.

Typical activities include:

* Decommissioning.
* Data preservation or secure destruction.
* Removing access credentials.
* Disconnecting interfaces.
* Recovering reusable components.
* Recycling or disposing of materials.
* Updating asset and configuration records.

**Key principle:** Systems engineering considers the entire life cycle, not only the design and development phases.

## 3. System Transition Planning

Transition should be planned early because deployment constraints can influence architecture, interfaces, training, cost, and system design.

For example, a monitoring system that requires uninterrupted service cannot be deployed safely without a migration strategy, rollback plan, and agreed outage limits.

### 3.1 Transition Plan Contents

A transition plan commonly defines:

1. Scope and objectives.
2. Transition strategy.
3. Required facilities and infrastructure.
4. Hardware and software prerequisites.
5. Data and configuration migration.
6. Roles and responsibilities.
7. Training and documentation.
8. Schedule and milestones.
9. Operational acceptance criteria.
10. Risks and mitigations.
11. Backup and rollback arrangements.
12. Support arrangements.
13. Communication and stakeholder coordination.
14. Final handover requirements.

### 3.2 Transition Strategies

| Strategy           | Description                                              | Advantages                                      | Risks                                                 |
| ------------------ | -------------------------------------------------------- | ----------------------------------------------- | ----------------------------------------------------- |
| Direct cutover     | Replace the old system at a planned point                | Fast transition; avoids long parallel operation | High impact if the new system fails                   |
| Phased transition  | Introduce the new system in stages                       | Limits the size of each change                  | More complex coordination                             |
| Pilot deployment   | Introduce the system to a limited user group or location | Reveals practical problems before wider rollout | Pilot conditions may not represent all environments   |
| Parallel operation | Run old and new systems simultaneously for a period      | Allows comparison and fallback                  | Higher operating cost and possible data inconsistency |

The best strategy depends on risk, service continuity, resources, compatibility, and the ability to reverse the change.

### 3.3 Rollback Planning

A rollback plan defines how to return to a known acceptable state if deployment fails.

It should address:

* Conditions that trigger rollback.
* Authorized decision-makers.
* Backup and restoration procedures.
* Data consistency.
* Configuration recovery.
* Service restoration targets.
* Communication responsibilities.
* Verification after rollback.

Rollback is not always as simple as reinstalling the previous version. A database migration, hardware replacement, or irreversible data transformation may make complete reversal difficult.

Therefore, reversibility should be assessed before deployment.

## 4. Operational Readiness

Operational readiness means the system and the organization are prepared to use and support the system safely and effectively.

A technically functional system may still be operationally unready if the required staff, procedures, facilities, or support arrangements are unavailable.

### 4.1 Operational Readiness Checklist

| Area           | Questions                                                                 |
| -------------- | ------------------------------------------------------------------------- |
| Technical      | Has the required configuration been installed and checked?                |
| Infrastructure | Are power, network, cooling, storage, and other dependencies available?   |
| People         | Are operators and support personnel trained?                              |
| Procedures     | Are operating, recovery, and escalation procedures approved?              |
| Security       | Are accounts, permissions, monitoring, and security controls configured?  |
| Data           | Has required data been migrated, validated, and backed up?                |
| Support        | Are support contacts, spare parts, and escalation paths available?        |
| Documentation  | Are manuals, diagrams, configuration records, and known issues available? |
| Performance    | Does the deployed system meet required operational performance criteria?  |
| Continuity     | Are backup, recovery, and business-continuity arrangements ready?         |

### 4.2 Readiness Review

A readiness review evaluates whether the required conditions have been satisfied before the system enters service.

It may review:

* Outstanding defects.
* Open risks and mitigations.
* Training completion.
* Acceptance evidence.
* Maintenance readiness.
* Safety and security requirements.
* Contingency plans.
* Approval from authorized stakeholders.

A readiness review should not automatically approve deployment just because a date has been reached. The decision should be based on predefined criteria and documented risks.

## 5. Installation, Deployment, and Configuration

Deployment transfers the system into the environment where it will be used.

### 5.1 Installation

Installation may include:

* Mounting and connecting equipment.
* Installing software.
* Establishing network connectivity.
* Connecting external interfaces.
* Configuring power and environmental controls.
* Applying initial security settings.

### 5.2 Configuration

Configuration establishes the system settings required for its intended operation.

Examples include:

* IP addresses and VLANs.
* User roles and permissions.
* Application settings.
* Sensor thresholds.
* Database connections.
* Firewall rules.
* Logging and monitoring parameters.

The deployed configuration should be checked against an approved baseline.

### 5.3 Deployment Verification

After installation, perform appropriate checks such as:

* Hardware inventory and identification.
* Software version confirmation.
* Connectivity tests.
* Interface checks.
* Security configuration review.
* Basic functional tests.
* Performance and monitoring checks.
* Backup and recovery checks.

A successful laboratory test does not automatically prove that a system has been deployed correctly in its operational environment.

## 6. System Operation

Operational processes ensure the system continues delivering its intended capability.

### 6.1 Operational Responsibilities

Operators may be responsible for:

* Starting and stopping the system.
* Monitoring health and performance.
* Managing routine workflows.
* Responding to alarms.
* Following approved operating procedures.
* Recording incidents and abnormal conditions.
* Escalating issues to support teams.

### 6.2 Operational Procedures

A procedure should explain:

* Purpose and scope.
* Required roles and permissions.
* Preconditions.
* Step-by-step actions.
* Expected system responses.
* Warnings and safety constraints.
* Failure handling.
* Escalation contacts.
* Required records.

Procedures should be tested or reviewed for usability, especially when errors could interrupt service or create safety risks.

### 6.3 Monitoring and Operational Metrics

Metrics help determine whether a system continues to satisfy operational requirements.

Examples:

* Availability.
* Response time.
* Throughput.
* Error rate.
* Resource utilization.
* Failure frequency.
* Recovery time.
* Energy consumption.
* User-reported issues.

Metrics must have clear definitions. For example, availability calculations should specify the measurement period, what counts as downtime, and whether planned maintenance is included.

## 7. Reliability, Availability, and Maintainability

These concepts are related but distinct.

### 7.1 Reliability

**Reliability** is the ability of a system to perform its required function without failure for a specified period under stated conditions.

A system may be highly reliable over short periods but still require substantial maintenance over its entire life.

### 7.2 Availability

**Availability** is the degree to which a system is operational and accessible when required.

A commonly used simplified steady-state relationship is:

$$
A=\frac{MTBF}{MTBF+MTTR}
$$

Where:

* \(A\) = availability.
* \(MTBF\) = mean time between failures, under the assumptions of the model.
* \(MTTR\) = mean time to repair or restore service, according to the metric definition.

This simplified equation assumes a repairable system and consistent definitions. Real operational availability may also account for logistics delays, preventive maintenance, administrative delays, and other downtime.

**Example:** If MTBF is 990 hours and MTTR is 10 hours:

$$
A=\frac{990}{990+10}=0.99=99\%
$$

### 7.3 Maintainability

**Maintainability** describes how effectively and efficiently a system can be maintained or restored.

Factors include:

* Accessibility of components.
* Diagnostic capability.
* Availability of maintenance instructions.
* Modularity and replaceability.
* Required tools and skills.
* Spare-part availability.
* Repair time.

A maintainable design can reduce downtime and life-cycle cost.

### 7.4 Operational Availability vs. Reliability

A system can experience frequent failures yet recover quickly, producing relatively high availability. Another system may fail rarely but require long repairs, reducing availability.

Therefore, improving reliability and improving maintainability are different engineering activities.

## 8. Maintenance Strategies

### 8.1 Corrective Maintenance

Performed after a fault or failure is identified.

Example: Replacing a failed network power supply.

**Advantages:** Maintenance effort is directed toward identified problems.

**Limitations:** Unexpected failures may cause downtime, service disruption, or secondary damage.

### 8.2 Preventive Maintenance

Performed at scheduled intervals or according to defined usage thresholds.

Examples:

* Periodic inspection.
* Sensor calibration.
* Battery replacement.
* Scheduled patching.
* Cleaning and lubrication where applicable.

**Advantages:** Can reduce the likelihood of some failures.

**Limitations:** Excessive maintenance can increase cost and may introduce maintenance-related faults.

### 8.3 Predictive Maintenance

Uses condition data and analysis to estimate when maintenance may be needed.

Examples:

* Monitoring equipment temperature.
* Detecting unusual vibration patterns.
* Tracking battery degradation.
* Using logs and telemetry to identify early warning signs.

**Advantages:** Can reduce unnecessary maintenance and help prevent unexpected downtime.

**Limitations:** Depends on data quality, model accuracy, sensor availability, and appropriate decision thresholds.

### 8.4 Reliability-Centered Maintenance

Reliability-centered maintenance selects maintenance tasks according to system functions, failure modes, consequences, and appropriate mitigation strategies.

It asks which failures matter, what causes them, and which maintenance or design action best manages their consequences.

### 8.5 Comparison

| Strategy             | Timing                                             | Typical trigger                          |
| -------------------- | -------------------------------------------------- | ---------------------------------------- |
| Corrective           | After a fault is identified                        | Failure or defect                        |
| Preventive           | Before expected failure                            | Calendar schedule or usage threshold     |
| Predictive           | Based on condition or predicted degradation        | Sensor data or analytical warning        |
| Reliability-centered | Based on failure consequences and system functions | Structured reliability and risk analysis |

These approaches can be combined within one maintenance program.

## 9. Logistics and Supportability

A system may be technically maintainable but operationally difficult to support.

Supportability considers whether the organization can sustain the system throughout its service life.

### 9.1 Support Resources

Typical resources include:

* Spare parts.
* Tools and diagnostic equipment.
* Trained personnel.
* Technical documentation.
* Repair facilities.
* Software licenses and update access.
* Vendor support.
* Backup equipment.
* Secure access to system logs.

### 9.2 Supportability Planning

Support planning should consider:

* Expected failure rates.
* Repair time.
* Geographic distribution of users.
* Supply-chain lead times.
* Availability of qualified technicians.
* Obsolescence.
* Warranty and service agreements.
* Security updates.
* End-of-support dates.

Supportability decisions should be made early enough to influence architecture and procurement.

For example, a system that uses a proprietary component with a long replacement lead time may need a spare-part strategy or a redesign.

## 10. Change and Configuration Management During Operation

Operational systems continue to change.

Common changes include:

* Security patches.
* Hardware replacement.
* Software upgrades.
* Network redesign.
* Threshold adjustments.
* Database migrations.
* Changes to user roles.

Each change should be evaluated for its effects on system requirements, interfaces, safety, security, performance, and existing evidence.

### 10.1 Change-Control Process

A typical process is:

1. Submit and document the change request.
2. Analyze technical and operational impact.
3. Assess risks, dependencies, and affected stakeholders.
4. Obtain the required authorization.
5. Plan implementation and rollback.
6. Implement the approved change.
7. Verify the changed configuration.
8. Perform appropriate regression testing.
9. Update documentation and configuration records.
10. Close the change after reviewing evidence.

### 10.2 Configuration Baseline

A configuration baseline identifies an approved system configuration at a particular point in time.

It may include:

* Hardware models and serial identifiers.
* Software and firmware versions.
* Configuration files.
* Network diagrams.
* Database schemas.
* Requirements and interface specifications.
* Operational procedures.

A baseline provides a reference for determining what changed and whether the current configuration is approved.

## 11. Incident and Problem Management

Operational support often distinguishes incidents from underlying problems.

* **Incident:** An unplanned interruption, degradation, or operational event requiring response.
* **Problem:** The underlying cause, or potential cause, of one or more incidents.

Example:

A network connection drops repeatedly.

* Incident management restores connectivity and communicates service status.
* Problem management investigates the recurring root cause, such as a failing switch or configuration defect.

### 11.1 Operational Response

A structured response may involve:

1. Detecting the event.
2. Recording relevant evidence.
3. Assessing severity and impact.
4. Restoring service or applying containment.
5. Communicating with affected users.
6. Investigating root cause.
7. Implementing corrective action.
8. Verifying recovery.
9. Updating operational knowledge and documentation.

Safety- or security-related incidents may require specialized escalation and reporting procedures.

### 11.2 Lessons Learned

Operational data can reveal issues that were not apparent during development.

Examples include:

* Frequently misunderstood alerts.
* Unexpected workloads.
* High repair times.
* Poorly documented interfaces.
* Repeated security misconfigurations.
* Excessive false alarms.

These observations can drive design improvements and future system versions.

## 12. System Upgrades and Evolution

Systems often remain in service for years, while technology, stakeholder needs, regulations, and operating environments change.

An upgrade may affect:

* Interfaces.
* Performance.
* Security.
* Data compatibility.
* User workflows.
* Maintenance procedures.
* Training requirements.
* Verification evidence.

Before an upgrade, assess whether it introduces new requirements or invalidates previous assumptions.

After implementation, perform appropriate verification and validation to establish that the updated system remains fit for purpose.

### 12.1 Technical Debt and Obsolescence

**Technical debt** describes future costs created by design or implementation compromises.

**Obsolescence** occurs when components, technologies, skills, or support services become outdated or unavailable.

Examples:

* Unsupported operating systems.
* End-of-life hardware.
* Deprecated APIs.
* Unavailable replacement components.
* Loss of vendor support.

Obsolescence management may involve planned upgrades, alternative suppliers, component redesign, extended support, or system replacement.

## 13. System Disposal and Retirement

Disposal is an engineered life-cycle activity, not merely the removal of equipment.

### 13.1 Reasons for Retirement

* The system no longer meets stakeholder needs.
* Maintenance becomes too expensive.
* Required components become unavailable.
* Security or regulatory requirements cannot be satisfied.
* A replacement system is introduced.
* The system reaches the end of its intended service life.

### 13.2 Disposal Planning

A disposal plan may address:

1. Retirement authorization.
2. Operational shutdown.
3. Dependency identification.
4. Data retention and migration.
5. Secure data destruction where required.
6. Removal of credentials and access permissions.
7. Disconnection of interfaces.
8. Asset and inventory updates.
9. Recovery of reusable components.
10. Recycling and environmental requirements.
11. Contract and license closure.
12. Documentation and lessons learned.

### 13.3 Data Security

Before retiring computers, servers, storage devices, or embedded systems, determine whether they contain sensitive information.

Appropriate actions may include:

* Preserving records required by policy or law.
* Transferring data to an authorized repository.
* Revoking certificates, keys, and credentials.
* Securely sanitizing or destroying storage media.
* Verifying that backups and replicas are handled correctly.

Simply deleting visible files may not adequately remove recoverable data.

### 13.4 Environmental Considerations

Disposal should consider:

* Electronic waste.
* Batteries and hazardous materials.
* Reuse and recycling.
* Energy consumption.
* Supplier take-back arrangements.
* Local environmental requirements.

Where practical, reuse and recycling can reduce waste, provided that security, safety, and regulatory obligations are satisfied.

## 14. Practical Case Study — Enterprise Network Modernization

### 14.1 Scenario

An organization replaces aging network switches and deploys a new monitoring platform. Existing services must remain available, and several departments depend on the network.

### 14.2 Transition Plan

The engineering team should:

* Inventory existing switches, VLANs, routing, and connected systems.
* Define the approved target configuration.
* Verify compatibility with existing interfaces.
* Test the proposed configuration in a lab or pilot environment.
* Schedule the migration and communicate planned impacts.
* Back up configurations.
* Define rollback triggers and responsibilities.
* Prepare operational procedures.
* Train the support team.
* Perform post-deployment verification.

### 14.3 Operational Readiness

Before cutover, confirm:

* Switch configurations are reviewed.
* Required ports and VLANs are mapped.
* Routing and access controls are checked.
* Monitoring and alerting are functional.
* Backups are available.
* Support personnel are available.
* Recovery procedures are documented.
* Stakeholders understand the maintenance window.

### 14.4 Operation and Maintenance

After deployment, monitor:

* Link availability.
* Packet loss.
* Latency.
* Interface errors.
* CPU and memory utilization.
* Security events.
* Configuration changes.

Preventive maintenance may include approved firmware updates and periodic configuration reviews. Predictive approaches may use telemetry to identify deteriorating components.

### 14.5 Retirement

Once the old switches are no longer required:

* Confirm that no live service depends on them.
* Remove old configurations and credentials.
* Update diagrams and inventory.
* Retain records according to policy.
* Sanitize storage where applicable.
* Reuse, recycle, or dispose of hardware responsibly.

### 14.6 Systems-Engineering Lesson

Successful deployment requires more than installing functioning equipment. The engineering team must preserve required services, verify the actual deployed configuration, prepare the operational organization, maintain the system, and retire the old system safely.

## 15. Exercises

### Exercise 1 — Transition Strategy

An organization is replacing an important service that cannot tolerate a long outage. The new system can run alongside the old one for two weeks.

1. Which transition strategy would you consider?
2. What risks would you assess?
3. What criteria would trigger rollback?
4. What must be verified before retiring the old system?

### Exercise 2 — Operational Readiness

A newly installed server passes its basic functional tests. However, no one has tested backup restoration, and the support team has not received recovery instructions.

Is the server fully operationally ready? Explain what remains to be done.

### Exercise 3 — Availability Calculation

A repairable system has an MTBF of 1,980 hours and an MTTR of 20 hours.

Calculate its simplified steady-state availability using:

$$
A=\frac{MTBF}{MTBF+MTTR}
$$

Explain one reason actual operational availability might be lower.

### Exercise 4 — Maintenance Strategy

Choose a suitable primary maintenance approach for each scenario and justify your choice.

1. A component fails unexpectedly and must be replaced.
2. A battery must be replaced every 24 months according to an approved maintenance schedule.
3. Sensor telemetry indicates progressive degradation before failure.
4. A complex system has multiple failure modes with different operational consequences.

### Exercise 5 — Change Management

A team updates a firewall rule to resolve a connectivity problem. The change restores the required connection but unintentionally exposes an internal service.

Identify the failure in the change process and propose corrective actions.

### Exercise 6 — Disposal

An organization retires a server containing confidential customer records.

Develop a disposal checklist that addresses data security, service continuity, access control, asset records, and environmental considerations.

### Exercise 7 — Case Study

During a network migration, the new equipment passes laboratory tests but several production applications lose connectivity.

Explain why laboratory verification was insufficient and describe how the transition plan, interface requirements, operational readiness, and rollback strategy should address the problem.

---

## 16. Exercise Answer Key

### Exercise 1

1. **Parallel operation** is a strong candidate because the systems can run simultaneously and support comparison or fallback.
2. Assess data consistency, interface compatibility, duplicate processing, user confusion, cybersecurity, migration defects, and additional operating cost.
3. Define measurable triggers in advance, such as unacceptable service disruption, data-integrity failures, or critical acceptance criteria not being met.
4. Verify dependencies have been migrated, data is complete, required services work, backups and recovery are established, and stakeholders approve retirement.

### Exercise 2

No. Basic functionality is insufficient to establish full operational readiness. The team should test backup restoration, document recovery procedures, train support personnel, verify permissions and monitoring, and confirm the required operational acceptance criteria.

### Exercise 3

$$
A=\frac{1980}{1980+20}
=\frac{1980}{2000}=0.99
$$

Simplified availability is **99%**.

Actual operational availability may be lower because the calculation may exclude spare-part delays, administrative delays, preventive maintenance, logistics, or other downtime.

### Exercise 4

1. **Corrective maintenance:** Responds to an identified failure.
2. **Preventive maintenance:** Follows an established interval or usage threshold.
3. **Predictive maintenance:** Uses condition data to anticipate maintenance needs.
4. **Reliability-centered maintenance:** Selects tasks based on functions, failure modes, and consequences.

### Exercise 5

The team failed to evaluate the full security impact of the change. Corrective actions include containing the exposure, restoring an approved secure configuration, assessing impact, reviewing the change authorization process, updating tests to include security and connectivity requirements, and documenting the incident.

### Exercise 6

A good checklist includes:

* Identify all dependent services and migrate them safely.
* Confirm data retention obligations and authorized transfers.
* Verify backups and restoration before shutdown.
* Revoke accounts, keys, certificates, and credentials.
* Sanitize or physically destroy storage using an appropriate approved method.
* Verify completion and preserve required evidence.
* Update asset and configuration records.
* Remove network connections and monitoring entries.
* Arrange approved reuse, recycling, or disposal.
* Document approvals and closure.

### Exercise 7

Laboratory testing did not fully represent production interfaces, configuration, workloads, or dependencies. The team should investigate interface mappings and configuration differences, verify production-specific requirements, and assess whether the readiness review overlooked dependencies. The rollback plan should define how to restore the previous service configuration if the agreed failure thresholds are reached.

---

## 17. ASEP-Style Practice Questions

These are original practice questions, not official INCOSE examination questions.

### Question 1

What is the primary purpose of system transition?

A. To replace requirements analysis
B. To move a system into its intended operational environment and prepare it for use
C. To eliminate the need for maintenance
D. To perform only final software testing

### Question 2

Which situation best demonstrates operational unreadiness?

A. The system has a complete approved configuration
B. Operators are trained and recovery procedures are tested
C. The system works in basic tests, but required recovery procedures are unavailable
D. The support team has access to approved documentation

### Question 3

Which strategy allows the old and new systems to operate simultaneously for a period?

A. Direct cutover
B. Parallel operation
C. Immediate disposal
D. Uncontrolled migration

### Question 4

What does maintainability primarily concern?

A. How easily and efficiently a system can be maintained or restored
B. Whether stakeholders initially approved the concept
C. The number of requirements in the specification
D. The system's purchase price alone

### Question 5

A system has frequent failures but is repaired very quickly. Which statement is most accurate?

A. Its reliability must be high
B. Its availability may still be relatively high
C. Its maintainability must be poor
D. It cannot be operated safely

### Question 6

What is a principal benefit of a configuration baseline?

A. It eliminates every configuration error
B. It provides an approved reference for identifying and assessing changes
C. It replaces all operational procedures
D. It guarantees that every upgrade is successful

### Question 7

Which activity best represents predictive maintenance?

A. Replacing a component only after failure
B. Replacing every component daily regardless of condition
C. Using condition data to identify developing degradation
D. Retiring equipment without reviewing its condition

### Question 8

What is the main purpose of rollback planning?

A. To ensure that no deployment will ever fail
B. To define how to restore an acceptable state if deployment fails
C. To remove the need for deployment verification
D. To avoid recording configuration changes

### Question 9

Which activity is essential when retiring a server containing confidential data?

A. Remove the server from the inventory without further action
B. Delete desktop shortcuts
C. Apply an appropriate approved data-sanitization or destruction process and verify completion
D. Disconnect the network cable only

### Question 10

What is the main distinction between incident management and problem management?

A. Incident management restores or manages service impact; problem management investigates underlying causes
B. Incident management is only for hardware, while problem management is only for software
C. Both terms mean exactly the same thing
D. Problem management never requires technical investigation

## 18. Practice Question Answer Key

| Question | Answer | Explanation                                                                               |
| -------- | ------ | ----------------------------------------------------------------------------------------- |
| 1        | B      | Transition prepares and transfers the system into operational use.                        |
| 2        | C      | Recovery capability is part of operational readiness.                                     |
| 3        | B      | Parallel operation runs old and new systems together temporarily.                         |
| 4        | A      | Maintainability concerns the ease and efficiency of maintenance and restoration.          |
| 5        | B      | Fast restoration can support high availability despite frequent failures.                 |
| 6        | B      | A baseline provides a reference for controlled change.                                    |
| 7        | C      | Predictive maintenance uses condition information to anticipate needs.                    |
| 8        | B      | Rollback defines recovery from an unsuccessful deployment.                                |
| 9        | C      | Confidential data requires an appropriate, verified disposition process.                  |
| 10       | A      | Incident management addresses service impact; problem management seeks underlying causes. |

## 19. Revision Notes

Remember these distinctions:

* **Transition:** Prepare and transfer the system into operational use.
* **Operation:** Use the system to deliver its intended capabilities.
* **Maintenance:** Preserve or restore required performance.
* **Disposal:** Retire the system safely, securely, and responsibly.
* **Operational readiness:** The system, people, procedures, infrastructure, and support are ready.
* **Direct cutover:** Switch at a planned point.
* **Phased transition:** Introduce the system in stages.
* **Pilot deployment:** Trial the system with a limited group or environment.
* **Parallel operation:** Run old and new systems together temporarily.
* **Reliability:** Ability to perform without failure under stated conditions for a specified period.
* **Availability:** Degree to which the system is operational when required.
* **Maintainability:** Ease and efficiency of maintenance and restoration.
* **Corrective maintenance:** Respond to an identified fault.
* **Preventive maintenance:** Maintain according to an established schedule or usage threshold.
* **Predictive maintenance:** Use condition data to anticipate maintenance.
* **Configuration baseline:** Approved reference for controlled change.
* **Rollback:** Restore an acceptable state after unsuccessful deployment.
* **Incident management:** Address an operational event and its immediate impact.
* **Problem management:** Investigate underlying causes.
* **Disposal planning:** Includes data, security, dependencies, asset records, and environmental considerations.

### Quick Self-Check

Before continuing, ensure you can:

1. Compare direct, phased, pilot, and parallel transitions.
2. Explain why readiness requires more than a successful functional test.
3. Calculate simplified availability.
4. Distinguish reliability, availability, and maintainability.
5. Compare corrective, preventive, predictive, and reliability-centered maintenance.
6. Explain why operational changes require impact analysis and verification.
7. Describe the difference between incident and problem management.
8. Create a safe system-disposal plan.

## 20. Official References and Further Reading

Consult current editions and applicable revisions.

1. **INCOSE Systems Engineering Handbook** — Life-cycle processes, operation, maintenance, transition, and disposal.
2. **ISO/IEC/IEEE 15288, Systems and software engineering — System life cycle processes** — System life-cycle processes, including transition, operation, maintenance, and disposal.
3. **ISO/IEC/IEEE 14764, Software engineering — Software life cycle processes — Maintenance** — Software maintenance concepts and processes.
4. **ISO 55000 series, Asset management** — Asset-management principles and life-cycle value considerations.
5. **IEC 60300 series, Dependability management** — Dependability, reliability, maintainability, and related management practices where applicable.
6. **INCOSE Certification Program** — Current ASEP certification requirements and examination references.

Official starting points:

* INCOSE: https://www.incose.org/
* INCOSE Certification: https://www.incose.org/certification
* ISO Standards: https://www.iso.org/standards.html
* IEEE Standards Association: https://standards.ieee.org/
* IEC: https://www.iec.ch/

Check the applicable editions and standards for your system type and industry. This module is a study aid, not a replacement for official standards or the current INCOSE handbook.

---

**End of Module 08 — System Transition, Operation, Maintenance, and Disposal**

**Next module:** `09_Technical_Management_Processes.md` — project planning, assessment, decision management, risk management, configuration management, information management, and measurement.
