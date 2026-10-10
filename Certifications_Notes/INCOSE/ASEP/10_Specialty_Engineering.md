# Module 10 — Agreement and Acquisition Processes

**Course:** INCOSE ASEP Preparation
**File:** `10_Agreement_and_Acquisition_Processes.md`
**Purpose:** Understand how organizations acquire systems and services, select suppliers, establish agreements, and manage technical responsibilities across organizational boundaries.

---

## 1. Learning Objectives

By the end of this module, you should be able to:

* Explain acquisition and supply processes in systems engineering.
* Distinguish the acquirer, supplier, customer, and end user.
* Understand needs definition and acquisition planning.
* Explain supplier selection and proposal evaluation.
* Identify essential elements of technical agreements.
* Understand requirements allocation and flow-down to suppliers.
* Explain supplier monitoring, acceptance, and change control.
* Recognize acquisition risks and contract-related trade-offs.
* Apply agreement and acquisition concepts to an engineering case study.

## 2. Introduction to Agreement and Acquisition Processes

Many systems are developed using components, software, equipment, or services supplied by external organizations.

Examples include:

* Purchasing sensors for a monitoring system.
* Contracting a company to develop a software subsystem.
* Acquiring cloud infrastructure.
* Buying network switches and routers.
* Obtaining specialist engineering or testing services.
* Integrating a third-party communication module into a larger system.

These relationships create technical and organizational dependencies. The acquirer must communicate its needs clearly, assess supplier capability, define responsibilities, and establish a way to determine whether the delivered products or services meet the agreed requirements.

### 2.1 Acquisition

**Acquisition** is the process through which an organization obtains a system, product, or service from another organization.

The acquirer may purchase an existing product, commission a new development, license software, or contract for a service.

### 2.2 Supply

**Supply** concerns the activities performed by the organization providing the system, product, or service.

The supplier must understand the agreed requirements, develop or provide the deliverable, manage its work, and demonstrate conformity with the applicable agreement.

### 2.3 Agreement

An **agreement** establishes the shared understanding and obligations between the relevant parties.

Depending on the context, it may be a formal contract, purchase order, statement of work, service-level agreement, or another authorized arrangement.

A commercial agreement can include technical requirements, deliverables, schedules, acceptance conditions, payment terms, responsibilities, and change procedures.

**Important:** Exact legal obligations depend on the agreement and applicable law. Systems engineers help define and manage technical content but should not assume that an informal technical understanding overrides a binding contract.

## 3. Key Stakeholders and Roles

### 3.1 Acquirer

The acquirer obtains the product or service.

Typical responsibilities include:

* Defining the need.
* Establishing acquisition objectives.
* Preparing requirements and evaluation criteria.
* Selecting a supplier.
* Establishing and managing the agreement.
* Monitoring performance.
* Evaluating deliverables.
* Accepting or rejecting deliverables according to agreed criteria.

### 3.2 Supplier

The supplier provides the agreed product or service.

Typical responsibilities include:

* Understanding and clarifying requirements.
* Developing a delivery or implementation plan.
* Allocating resources.
* Managing technical risks.
* Controlling its configuration and changes.
* Providing deliverables and required evidence.
* Reporting progress and problems.
* Correcting nonconformances under the applicable agreement.

### 3.3 Customer and End User

The customer is the party purchasing or receiving a system or service. The end user operates or interacts with it.

These roles may belong to the same organization or different organizations.

For example, a hospital may contract for a monitoring system, while doctors and nurses use it operationally.

The acquirer should ensure that end-user needs are represented in the requirements and acceptance criteria.

### 3.4 Other Stakeholders

Other parties may include:

* Regulators.
* Subcontractors.
* Integration partners.
* Independent assessors.
* Maintenance providers.
* Cloud service providers.
* Security and safety specialists.

A supplier's subcontractor can introduce additional risks even when the acquirer has no direct agreement with that subcontractor.

## 4. Acquisition Planning

Acquisition planning defines how the organization will obtain the system or service and manage the associated technical, commercial, and operational risks.

### 4.1 Acquisition Plan Contents

An acquisition plan may include:

1. Purpose and scope.
2. Operational needs and expected outcomes.
3. Technical and performance requirements.
4. Acquisition strategy.
5. Supplier selection criteria.
6. Required deliverables.
7. Schedule and milestones.
8. Budget and cost assumptions.
9. Contract or agreement structure.
10. Verification and acceptance strategy.
11. Risk management approach.
12. Quality and configuration requirements.
13. Security and intellectual-property considerations.
14. Maintenance and support requirements.
15. Training and documentation requirements.
16. Change management and dispute procedures.

The level of detail should reflect system complexity, criticality, uncertainty, and contractual obligations.

### 4.2 Build, Buy, or Reuse

A common acquisition decision is whether to develop a capability internally, buy it, or reuse an existing component.

| Option | Advantages                                              | Potential disadvantages                            |
| ------ | ------------------------------------------------------- | -------------------------------------------------- |
| Build  | Greater control over design and tailoring               | Development cost, schedule, and technical risk     |
| Buy    | Faster access to an existing capability                 | Limited customization and supplier dependence      |
| Reuse  | May reduce cost and implementation time                 | Compatibility, maintenance, and legacy constraints |
| Hybrid | Combines internal development with purchased components | Integration and interface complexity               |

The choice should be based on stakeholder needs, life-cycle cost, capability, risk, schedule, supportability, and constraints.

A low purchase price does not necessarily mean a low total cost of ownership.

### 4.3 Total Cost of Ownership

Total cost of ownership (TCO) considers costs over a defined period rather than only the initial purchase price.

Possible costs include:

* Purchase or licensing.
* Integration.
* Installation.
* Training.
* Operations.
* Maintenance.
* Security updates.
* Spare parts.
* Data migration.
* Vendor support.
* Upgrades.
* Retirement and disposal.

For example, a low-cost sensor may require a proprietary gateway and expensive replacement parts. A more expensive sensor with standard interfaces and better support may have a lower life-cycle cost.

## 5. Defining Acquisition Requirements

The acquirer must communicate what the system or service needs to accomplish.

Requirements should be clear, measurable where appropriate, feasible, traceable, and verifiable.

### 5.1 Types of Requirements

Acquisition requirements may include:

* Functional requirements.
* Performance requirements.
* Interface requirements.
* Environmental requirements.
* Safety requirements.
* Security requirements.
* Reliability and availability requirements.
* Maintainability requirements.
* Compatibility requirements.
* Documentation requirements.
* Training requirements.
* Support and warranty requirements.
* Data ownership and portability requirements.

### 5.2 Avoiding Ambiguous Requirements

Weak requirement:

> The supplier shall provide a reliable monitoring service.

Improved requirement:

> The supplier shall provide a monitoring service with monthly availability of at least 99.9%, calculated according to the agreed measurement method and exclusions.

The agreement should define:

* The measurement period.
* What constitutes an outage.
* Whether planned maintenance is excluded.
* How partial service degradation is handled.
* How results are reported.
* What remedies or corrective actions apply if the target is missed.

A numerical target is not sufficient unless its interpretation and measurement method are clear.

### 5.3 Requirements Flow-Down

Requirements flow-down allocates applicable higher-level requirements to lower-level system elements, suppliers, or subcontractors.

For example:

* System requirement: A critical alert shall reach the authorized caregiver within five seconds.
* Communication subsystem requirement: The communication subsystem shall deliver alert messages within its allocated latency budget under defined conditions.
* Supplier requirement: The supplied communication module shall meet its specified transmission performance under the agreed test conditions.

The allocated requirements must collectively support the parent requirement. The system engineer should assess timing budgets, interface assumptions, and interactions between components.

**Key principle:** A supplier's component may meet its own requirements while the complete system fails its system-level requirement.

## 6. Supplier Selection

Supplier selection evaluates which supplier is best positioned to deliver the required capability under the agreed constraints.

### 6.1 Selection Criteria

Criteria may include:

* Technical capability.
* Compliance with requirements.
* Relevant experience.
* Quality-management practices.
* Delivery schedule.
* Cost.
* Financial stability.
* Security practices.
* Support capability.
* Supply-chain resilience.
* Maintenance and upgrade plans.
* Regulatory compliance.
* Intellectual-property arrangements.

The criteria should be defined before proposals are evaluated to support consistency and fairness.

### 6.2 Request for Proposal

A **request for proposal (RFP)** invites suppliers to propose how they would meet the acquirer's needs.

An RFP may contain:

* Scope and background.
* Requirements.
* Deliverables.
* Constraints.
* Required technical approach.
* Schedule.
* Evaluation criteria.
* Proposal format.
* Assumptions and exclusions to identify.
* Required evidence.
* Commercial terms.

A **request for quotation (RFQ)** often focuses more directly on pricing for a sufficiently specified product or service, although terminology varies by organization and industry.

### 6.3 Proposal Evaluation

Proposal evaluation should consider both compliance and overall suitability.

A structured process may involve:

1. Confirming eligibility.
2. Checking mandatory requirements.
3. Evaluating technical proposals.
4. Reviewing cost and schedule.
5. Assessing risks and assumptions.
6. Evaluating support and life-cycle costs.
7. Conducting demonstrations or technical assessments where appropriate.
8. Documenting the selection rationale.

A supplier should not automatically win because it offers the lowest initial price.

### 6.4 Example Weighted Evaluation

Suppose two suppliers are assessed using illustrative scores from 1 to 5.

| Criterion            | Weight | Supplier A | Supplier B |
| -------------------- | -----: | ---------: | ---------: |
| Technical compliance |   0.35 |          5 |          4 |
| Life-cycle cost      |   0.25 |          3 |          5 |
| Delivery capability  |   0.20 |          4 |          4 |
| Support quality      |   0.20 |          4 |          3 |

Supplier A:

$$
S_A=(0.35)(5)+(0.25)(3)+(0.20)(4)+(0.20)(4)=4.10
$$

Supplier B:

$$
S_B=(0.35)(4)+(0.25)(5)+(0.20)(4)+(0.20)(3)=4.05
$$

Supplier A has the higher weighted score under these assumptions.

However, a weighted score should not compensate for a failure to meet a mandatory requirement. Mandatory compliance should be checked separately.

## 7. Statements of Work and Deliverables

A **statement of work (SOW)** describes the work to be performed and the expected outputs.

Depending on the agreement, it may define:

* Tasks and responsibilities.
* Deliverables.
* Technical requirements.
* Milestones.
* Required reviews.
* Test activities.
* Documentation.
* Reporting.
* Support.
* Acceptance conditions.

### 7.1 Deliverables

Deliverables may include physical products, software, services, documentation, and evidence.

Examples:

* Hardware units.
* Source code or executable software.
* Interface specifications.
* Architecture documents.
* Test plans and reports.
* Installation procedures.
* Training materials.
* Configuration records.
* Maintenance manuals.
* Security documentation.

Each deliverable should have a clear description, due date, required format, applicable version, and acceptance criteria.

### 7.2 Milestones

Milestones mark significant events or decision points.

Examples include:

* Requirements approval.
* Design review.
* Prototype delivery.
* Integration completion.
* Verification completion.
* Operational acceptance.
* Final handover.

Milestones should be linked to meaningful evidence rather than merely to the passage of time.

## 8. Contract Types and Incentives

Commercial arrangements allocate cost, schedule, and performance risks differently.

The precise names and legal meanings vary by jurisdiction and agreement.

### 8.1 Fixed-Price Arrangements

Under a fixed-price arrangement, the supplier generally agrees to deliver defined scope for an agreed price, subject to the contract's terms.

Potential advantages:

* Greater price predictability for the acquirer.
* Clear cost expectations for defined scope.

Potential limitations:

* Changes may require formal renegotiation.
* Ambiguous requirements can generate disputes.
* The supplier may face significant cost risk if the work is poorly estimated.

### 8.2 Cost-Reimbursement Arrangements

Under a cost-reimbursement arrangement, eligible costs are reimbursed according to agreed rules, potentially with an additional fee.

Potential advantages:

* Can suit work with substantial uncertainty.
* May accommodate exploratory development.

Potential limitations:

* The acquirer may bear more cost risk.
* Cost monitoring and oversight can be more demanding.

### 8.3 Incentive-Based Arrangements

Incentives may be linked to defined performance, cost, schedule, or other outcomes.

They should be designed carefully. An incentive focused only on delivery speed may encourage shortcuts that damage reliability, security, or maintainability.

Technical acceptance criteria and quality constraints remain important regardless of the commercial arrangement.

**Exam reminder:** Contract terminology alone does not determine whether a project will succeed. Clear scope, sound requirements, appropriate risk allocation, and effective oversight are also necessary.

## 9. Supplier Monitoring and Technical Oversight

Supplier oversight checks whether the supplier's work is progressing toward the agreed outcomes.

### 9.1 Monitoring Activities

Activities may include:

* Progress reviews.
* Technical meetings.
* Deliverable reviews.
* Schedule and cost reporting.
* Risk reviews.
* Interface coordination.
* Configuration audits.
* Quality assessments.
* Witnessed tests.
* Nonconformance tracking.
* Corrective-action reviews.

The level of oversight should be proportionate to technical risk, system criticality, and contractual obligations.

### 9.2 Early Warning Indicators

Potential warning signs include:

* Repeated missed milestones.
* Frequent staff turnover.
* Unresolved high-severity defects.
* Incomplete documentation.
* Increasing numbers of unexplained changes.
* Inconsistent test evidence.
* Unclear subcontractor responsibilities.
* Failure to report risks promptly.

Early intervention is generally easier than resolving serious technical problems near delivery.

### 9.3 Supplier Nonconformance

If a deliverable fails an agreed requirement, the acquirer should follow the applicable nonconformance and acceptance process.

Possible steps include:

1. Record the failure.
2. Identify the affected requirement and deliverable.
3. Preserve evidence.
4. Assess technical and operational consequences.
5. Request root-cause analysis and corrective action where appropriate.
6. Evaluate the proposed correction.
7. Retest or reinspect the deliverable.
8. Make an acceptance decision under the agreement.
9. Update relevant records.

Acceptance of a nonconforming deliverable, if permitted at all, should be handled through the authorized process and assessed for downstream consequences.

## 10. Interface and Integration Management Across Suppliers

When different suppliers provide subsystems, interface incompatibility becomes a major risk.

### 10.1 Interface Definition

An interface specification may define:

* Mechanical dimensions.
* Electrical characteristics.
* Communication protocols.
* Data formats.
* Timing constraints.
* Units and precision.
* Error handling.
* Security expectations.
* Version compatibility.
* Operating assumptions.

### 10.2 Supplier Interface Responsibilities

The agreement should establish who is responsible for:

* Defining interface specifications.
* Approving changes.
* Providing interface documentation.
* Supplying simulators or test tools.
* Supporting integration testing.
* Resolving incompatibilities.
* Maintaining backward compatibility, if required.

Without clear ownership, each supplier may claim that its own product is correct while the combined system fails.

### 10.3 Example

Supplier A delivers a sensor module using degrees Celsius. Supplier B develops a backend that assumes the input is Fahrenheit.

Both components may function according to their internal implementations, yet the integrated system produces incorrect results.

The problem demonstrates why data semantics, units, interface specifications, and end-to-end verification must be explicitly managed.

## 11. Agreement Changes and Claims

Changes may be needed when requirements evolve, technical assumptions prove incorrect, or operational conditions change.

### 11.1 Change Process

A controlled agreement-change process may include:

1. Submit a change request.
2. Describe the proposed change and rationale.
3. Assess technical impact.
4. Assess cost and schedule impact.
5. Evaluate risks and dependencies.
6. Identify affected deliverables and requirements.
7. Obtain authorization from the designated parties.
8. Update the agreement and relevant technical baselines.
9. Implement and verify the change.
10. Maintain an auditable record.

Engineers should not assume that a technical discussion or informal email necessarily authorizes a contractual change.

### 11.2 Claims and Disputes

A claim may arise when a party seeks a contractual remedy or asserts an entitlement under the agreement.

Potential causes include:

* Scope ambiguity.
* Late delivery.
* Unapproved changes.
* Acceptance disagreements.
* Missing documentation.
* Unclear responsibility for interface failures.
* Differing interpretations of performance criteria.

Clear requirements, decision records, change control, and objective evidence help reduce disputes.

Legal interpretation and formal dispute resolution should be handled by the authorized commercial and legal functions.

## 12. Supplier Security, Intellectual Property, and Data

Acquisition creates security and ownership questions that must be addressed explicitly.

### 12.1 Security

Evaluate:

* Supplier access to sensitive systems.
* Secure development practices.
* Vulnerability disclosure.
* Patch availability.
* Software dependencies.
* Supply-chain risks.
* Incident notification.
* Access control.
* Data handling and storage.
* End-of-support arrangements.

A supplier's security assurance should be evaluated against the system's actual requirements and threat context.

### 12.2 Intellectual Property

Agreements may need to clarify ownership and permitted use of:

* Source code.
* Designs.
* Documentation.
* Models and training data.
* Algorithms.
* Technical inventions.
* Configuration scripts.
* Test tools.

Ownership and licensing are distinct. An organization may have permission to use software without owning the source code.

### 12.3 Data Rights and Portability

For data-intensive or cloud-based systems, clarify:

* Who owns or controls the data.
* Who can access it.
* Where it is stored and processed.
* How it can be exported.
* What happens at contract termination.
* How data is retained or deleted.
* Whether proprietary formats create lock-in.

These decisions affect future system evolution and disposal.

## 13. Acceptance and Handover

Acceptance determines whether a deliverable meets the agreed acceptance conditions and whether the authorized party accepts it.

### 13.1 Acceptance Criteria

Criteria may cover:

* Required functionality.
* Performance.
* Reliability.
* Security.
* Interface compatibility.
* Documentation.
* Training.
* Configuration records.
* Test evidence.
* Outstanding defects.

The agreement should define the acceptance process, including how failures, corrective actions, and retesting are handled.

### 13.2 Acceptance vs. Verification and Validation

* **Verification:** Determines whether specified requirements are satisfied.
* **Validation:** Determines whether the system meets stakeholder needs and intended use.
* **Acceptance:** Determines whether the agreed conditions for accepting a deliverable or system have been met.

These processes overlap but are not interchangeable.

A customer may formally accept a deliverable after the contractual criteria are satisfied, while broader operational validation continues according to the project plan.

### 13.3 Handover

Handover may require:

* Approved technical documentation.
* As-built configuration records.
* Operating and maintenance procedures.
* Training completion.
* Support contacts.
* Warranty information.
* Known limitations and unresolved issues.
* Licenses and credentials transferred through secure procedures.
* Backup and recovery instructions.
* Final verification and acceptance records.

A physical product is not necessarily ready for operational handover if the support and documentation package is incomplete.

## 14. Practical Case Study — Acquiring a Monitoring Subsystem

### 14.1 Scenario

A company developing a wearable monitoring system needs to acquire a wireless communication module from an external supplier.

The module must satisfy power, latency, reliability, security, and interface requirements.

### 14.2 Acquisition Planning

The acquirer defines:

* Functional and performance requirements.
* Environmental conditions.
* Power and communication constraints.
* Required interface documentation.
* Security obligations.
* Delivery schedule.
* Required test evidence.
* Acceptance criteria.
* Maintenance and support expectations.

### 14.3 Supplier Selection

The team compares candidate suppliers using technical compliance, cost, delivery capability, security, support, and life-cycle cost.

Mandatory requirements are checked separately from weighted evaluation scores.

### 14.4 Agreement Definition

The agreement specifies:

* Module specifications.
* Firmware and hardware deliverables.
* Interface documentation.
* Test reports.
* Required versions and configuration records.
* Delivery milestones.
* Defect-correction process.
* Change-control requirements.
* Security updates and support.
* Acceptance procedures.

### 14.5 Supplier Monitoring

During development, the supplier reports that its current firmware may exceed the agreed latency budget.

The acquirer records the risk, evaluates the impact on the end-to-end requirement, requests a corrective plan, and assesses the evidence.

The team avoids assuming that the supplier's component-level timing result guarantees that the integrated monitoring system will meet its end-to-end latency requirement.

### 14.6 Acceptance

The module is evaluated against its acceptance criteria, including interface compatibility and required evidence.

After delivery, the integration team verifies the combined system under representative conditions.

If a required criterion is not satisfied, the issue is managed through the agreed nonconformance and acceptance process.

### 14.7 Systems-Engineering Lesson

Successful acquisition requires more than purchasing a component. The acquirer must translate stakeholder needs into clear technical requirements, select a suitable supplier, manage the agreement, verify deliverables, control changes, and ensure the delivered subsystem integrates into the larger system.

## 15. Exercises

### Exercise 1 — Build, Buy, or Reuse

An organization needs a standard database capability for a new monitoring application. Three options are available:

* Develop a custom database engine.
* Purchase a commercial database product.
* Reuse an existing approved database platform.

Identify at least five factors that should influence the decision. Explain why purchase price alone is insufficient.

### Exercise 2 — Supplier Selection

Two suppliers offer the same component. Supplier A is cheaper but has limited maintenance support. Supplier B costs more but offers stronger technical documentation, security updates, and long-term availability.

Develop an evaluation framework that reflects both technical and life-cycle considerations.

### Exercise 3 — Requirements Flow-Down

A system must deliver an alert within five seconds of a critical event.

Explain why it is insufficient to allocate the entire five-second allowance to the wireless communication module. Identify at least three other sources of latency.

### Exercise 4 — Nonconforming Deliverable

A supplier delivers a device that meets its physical dimensions but fails the required battery-endurance test.

Describe the appropriate technical and agreement-management actions.

### Exercise 5 — Change Control

An engineer asks a supplier to add a new API feature through an informal message. The supplier implements it, but the change causes compatibility problems.

Explain the process weaknesses and how they could have been prevented.

### Exercise 6 — Total Cost of Ownership

Supplier A offers equipment for $8,000 with estimated annual support costs of $3,000. Supplier B offers equipment for $10,000 with estimated annual support costs of $1,500.

Calculate the total estimated cost over three years, excluding discounting and other costs. Which option is cheaper under these assumptions? Identify two limitations of the comparison.

### Exercise 7 — Case Study

A cloud provider meets its advertised service availability, but the monitoring application still experiences unacceptable outages due to integration problems and poor recovery procedures.

Explain the difference between supplier compliance and overall system success. Recommend actions for the acquirer and systems-engineering team.

---

## 16. Exercise Answer Key

### Exercise 1

Relevant factors include:

* Functional and performance requirements.
* Development time.
* Initial and life-cycle costs.
* Integration effort.
* Security and compliance.
* Vendor support.
* Skills and maintainability.
* Licensing.
* Data portability.
* Scalability.
* Existing compatibility.
* Obsolescence risk.

Purchase price alone ignores integration, training, maintenance, licensing, operational, and retirement costs.

### Exercise 2

A suitable framework might assign weights to mandatory technical compliance, performance, support, security, delivery capability, compatibility, and life-cycle cost.

First, eliminate any supplier that fails mandatory requirements. Then evaluate the remaining candidates using consistent criteria and document the rationale, assumptions, and risks.

Supplier B may be preferable if stronger support and security significantly reduce life-cycle risk, but the decision depends on evidence and stakeholder priorities.

### Exercise 3

The complete latency budget includes sensor detection and processing, operating-system scheduling, network transmission, backend processing, notification delivery, and user-interface presentation.

The team must allocate the five-second budget across the complete end-to-end path and verify the integrated system under defined conditions.

### Exercise 4

The acquirer should record the failed battery test, link it to the applicable requirement, preserve the evidence, assess operational consequences, and follow the agreement's nonconformance procedure.

The supplier may be required to investigate the root cause, propose a correction, and provide a corrected unit or other agreed remedy. The corrected deliverable should be retested before acceptance according to the applicable criteria.

### Exercise 5

The team bypassed authorized change control and failed to assess interface compatibility.

Prevention includes formal change requests, impact analysis, authorization, updated interface specifications, version management, and regression testing before the modified API is accepted.

### Exercise 6

Supplier A:

$$
8000+(3\times3000)=\$17{,}000
$$

Supplier B:

$$
10000+(3\times1500)=\$14{,}500
$$

Supplier B is cheaper by $2,500 under the stated assumptions.

Limitations include omitted installation or integration costs, uncertain future support charges, discounting, taxes, downtime, and differences in capability or reliability.

### Exercise 7

A supplier may satisfy its own service-level agreement while the integrated application still fails its system-level needs. The overall system includes the provider, application, interfaces, data paths, monitoring, and recovery procedures.

The acquirer should define end-to-end requirements, test integrated failure and recovery scenarios, clarify responsibility boundaries, monitor application-level metrics, and improve operational readiness and recovery procedures.

---

## 17. ASEP-Style Practice Questions

These are original practice questions for study, not official INCOSE examination questions.

### Question 1

What is the primary purpose of acquisition planning?

A. To eliminate the need for technical requirements
B. To define how a system or service will be obtained and managed
C. To guarantee that the cheapest supplier is selected
D. To replace verification and validation

### Question 2

Which statement best describes the supplier's role?

A. The supplier provides the agreed product or service and fulfills its contractual responsibilities
B. The supplier automatically owns all system requirements
C. The supplier has no responsibility for documentation
D. The supplier can unilaterally change the agreement

### Question 3

Why should mandatory technical requirements be evaluated separately from weighted supplier scores?

A. To prevent cost from compensating for failure to meet an essential constraint
B. To guarantee that every supplier receives the same score
C. To eliminate the need for evidence
D. To make technical compliance optional

### Question 4

Which factor is most relevant to total cost of ownership?

A. Purchase price alone
B. Purchase, integration, operation, maintenance, and retirement costs over a defined period
C. Supplier advertising
D. The number of pages in the proposal

### Question 5

What is the purpose of requirements flow-down?

A. To remove system-level requirements
B. To allocate applicable higher-level requirements to lower-level elements or suppliers
C. To guarantee that every component independently satisfies every system requirement
D. To eliminate interface specifications

### Question 6

A supplier's component passes its individual tests, but the integrated system fails. What is the best conclusion?

A. The supplier's component test proves that the complete system is correct
B. Integration and system-level requirements may not have been adequately satisfied
C. The failure must be ignored if the contract is fixed-price
D. No further verification is necessary

### Question 7

What should normally happen before a significant contractual scope change is implemented?

A. The change should be implemented immediately without records
B. The authorized parties should evaluate and approve the change under the agreement's process
C. The technical requirements should be deleted
D. The supplier should decide unilaterally

### Question 8

What is a key purpose of supplier monitoring?

A. To replace the supplier's responsibilities
B. To assess progress, technical performance, risks, and compliance with agreed obligations
C. To guarantee that no technical issues will occur
D. To avoid reviewing deliverables

### Question 9

Which statement best distinguishes acceptance from validation?

A. Acceptance and validation are always identical
B. Acceptance evaluates agreed acceptance conditions; validation evaluates suitability for intended use and stakeholder needs
C. Validation is only a financial activity
D. Acceptance never involves technical evidence

### Question 10

A supplier delivers a component with incomplete interface documentation. The component appears to function in a demonstration.

What is the most appropriate response?

A. Accept it automatically because the demonstration succeeded
B. Ignore the documentation requirement
C. Evaluate the deliverable against the agreed acceptance criteria and manage any nonconformance through the authorized process
D. Modify the system without recording the change

## 18. Practice Question Answer Key

| Question | Answer | Explanation                                                                              |
| -------- | ------ | ---------------------------------------------------------------------------------------- |
| 1        | B      | Acquisition planning establishes the approach for obtaining and managing the capability. |
| 2        | A      | Supplier obligations are defined by the agreement and applicable requirements.           |
| 3        | A      | Mandatory constraints should not be offset by unrelated high scores.                     |
| 4        | B      | TCO includes relevant costs across a defined life-cycle period.                          |
| 5        | B      | Flow-down allocates appropriate requirements to lower-level elements.                    |
| 6        | B      | Component success does not prove end-to-end system success.                              |
| 7        | B      | Significant changes require the authorized change process.                               |
| 8        | B      | Monitoring evaluates progress, risks, and compliance.                                    |
| 9        | B      | Acceptance and validation have related but different purposes.                           |
| 10       | C      | The deliverable must be assessed against all applicable acceptance criteria.             |

## 19. Revision Notes

Remember these principles:

* **Acquisition:** Obtain a system, product, or service.
* **Supply:** Provide the agreed system, product, or service.
* **Agreement:** Establish responsibilities, deliverables, criteria, and obligations.
* **Acquirer:** Defines needs, selects suppliers, manages agreements, and evaluates deliverables.
* **Supplier:** Provides the agreed capability and evidence.
* **Build, buy, or reuse:** Compare capability, cost, schedule, risk, and supportability.
* **Total cost of ownership:** Considers costs over a defined period.
* **RFP:** Requests proposals for meeting defined needs.
* **SOW:** Defines the work and deliverables.
* **Requirements flow-down:** Allocates higher-level requirements to lower-level elements or suppliers.
* **Supplier monitoring:** Evaluates progress, technical quality, and contractual performance.
* **Acceptance:** Determines whether agreed acceptance conditions are satisfied.
* **Change control:** Ensures changes are evaluated, authorized, documented, and verified.
* **Interface management:** Coordinates technical compatibility across system elements and suppliers.
* **Supplier compliance does not guarantee system success:** The integrated system must still satisfy its end-to-end requirements.

### Quick Self-Check

Before moving to the next module, ensure you can:

1. Distinguish acquisition, supply, and agreement.
2. Compare build, buy, and reuse.
3. Explain how requirements are allocated to suppliers.
4. Evaluate supplier proposals using mandatory constraints and weighted criteria.
5. Identify the major contents of an SOW.
6. Explain why supplier monitoring is necessary.
7. Describe the management of nonconforming deliverables.
8. Explain the difference between acceptance and validation.
9. Identify security, intellectual-property, and data-portability concerns.
10. Explain how supplier-level success can differ from system-level success.

## 20. Official References and Further Reading

Consult the current editions and applicable revisions.

1. **INCOSE Systems Engineering Handbook** — Agreement and acquisition processes and their relationship to the wider system life cycle.
2. **ISO/IEC/IEEE 15288, Systems and software engineering — System life cycle processes** — Systems life-cycle processes, including acquisition and supply.
3. **ISO/IEC/IEEE 29148, Systems and software engineering — Requirements engineering** — Requirements definition, specification, and traceability relevant to acquisition.
4. **ISO 31000, Risk management — Guidelines** — Risk-management principles that can support supplier and acquisition risk assessment.
5. **INCOSE Certification Program** — Current ASEP examination requirements and official reference guidance.

Official starting points:

* INCOSE: https://www.incose.org/
* INCOSE Certification: https://www.incose.org/certification
* ISO Standards: https://www.iso.org/standards.html
* IEEE Standards Association: https://standards.ieee.org/

Use the editions and reference list specified by the current INCOSE certification guidance. This module is a study aid, not a substitute for the official handbook, standards, or legal advice.

---

**End of Module 10 — Agreement and Acquisition Processes**

**Next module:** `11_Organizational_Project_Enabling_Processes.md` — life-cycle model management, infrastructure, portfolio and human-resource considerations, quality management, and organizational support for systems engineering.
