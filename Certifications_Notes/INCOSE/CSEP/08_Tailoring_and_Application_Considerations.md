# 08 — Tailoring and Application Considerations

**Certification Track:** INCOSE CSEP Preparation
**Suggested Filename:** `08_Tailoring_and_Application_Considerations.md`
**Purpose:** Understand how systems-engineering life-cycle processes and practices are adapted to the context, risks, constraints, and characteristics of a specific system or project.

> **Study note:** This is an independent study resource. The practice questions are original and are not official INCOSE examination questions. Check the edition of ISO/IEC/IEEE 15288 and the INCOSE Systems Engineering Handbook specified in your certification study materials.

---

## 1. Learning Objectives

By the end of this module, you should be able to:

1. Explain the purpose and value of tailoring.
2. Distinguish organizational-level tailoring from project-level tailoring.
3. Identify the factors that influence tailoring decisions.
4. Explain how system complexity, criticality, uncertainty, and project constraints affect engineering rigor.
5. Describe a systematic tailoring process.
6. Document and justify tailoring decisions.
7. Recognize under-tailoring and over-tailoring.
8. Apply tailoring to traditional, iterative, agile, and hybrid life-cycle approaches.
9. Explain how compliance, governance, and assurance constrain tailoring.
10. Evaluate tailoring decisions through realistic project scenarios.

## 2. What Is Tailoring?

**Tailoring** is the deliberate adaptation of a systems-engineering process, activity, method, technique, or set of work products to suit a particular organizational or project context.

A systems-engineering framework provides processes and practices that can be applied across many kinds of systems. However, not every project needs the same level of documentation, review, analysis, testing, or approval.

For example:

* A small internal reporting tool may need lightweight requirements, automated tests, and a short release review.
* An industrial monitoring platform may need formal interface specifications, controlled configurations, integration testing, and documented acceptance.
* A safety-critical medical or aerospace system may require extensive traceability, independent assurance, formal reviews, and evidence that applicable regulations have been satisfied.

The objective is not to minimize systems engineering. It is to apply the **appropriate level of systems engineering for the situation**.

### 2.1 Why tailoring is necessary

Without tailoring, organizations may apply the same process to every project regardless of risk or complexity.

This can create two problems:

1. **Over-processing:** Unnecessary documentation, approvals, and reviews consume resources without producing proportionate value.
2. **Under-processing:** Insufficient analysis, verification, validation, or control allows significant defects and risks to escape.

Effective tailoring balances engineering effectiveness, risk reduction, cost, schedule, and organizational obligations.

### 2.2 Tailoring is not arbitrary omission

Tailoring should be a reasoned and documented decision, not an excuse to ignore difficult work.

A process may be simplified, combined with another activity, performed at a different time, automated, or replaced by an alternative method that achieves the required outcome.

However, applicable legal obligations, contractual commitments, safety constraints, and mandatory organizational controls cannot be dismissed merely because a project finds them inconvenient.

## 3. Levels of Tailoring

Tailoring can occur at several levels.

### 3.1 Organizational-level tailoring

Organizational tailoring establishes the common systems-engineering framework that projects use.

An organization may define:

* Standard life-cycle models.
* Approved engineering processes.
* Mandatory reviews and approval gates.
* Standard document templates.
* Requirements-management rules.
* Configuration-management procedures.
* Risk classification methods.
* Verification and validation policies.
* Quality and assurance expectations.
* Rules for requesting and approving exceptions.

The purpose is to create consistency and avoid every project inventing its own process from the beginning.

Organizational standards may allow different process profiles for different classes of projects.

**Example:** An organization defines three engineering profiles: low-risk internal applications, ordinary commercial systems, and safety-critical systems. Each profile specifies an appropriate baseline of process activities and evidence.

### 3.2 Project-level tailoring

Project-level tailoring adapts the organizational framework to the particular project.

A project team may determine:

* Which approved life-cycle model is appropriate.
* Which technical reviews are required.
* How often stakeholders review increments.
* How much requirements formality is necessary.
* Which analyses and simulations are justified.
* Which configuration items require formal control.
* How verification and validation are organized.
* How risks are monitored.
* Which deliverables must be produced.
* Which activities can be automated or combined.

Project tailoring should remain consistent with organizational policies and higher-level obligations.

### 3.3 Product or system-level tailoring

Within a project, different system elements may warrant different levels of rigor.

For example, an industrial control system might contain:

* A safety-related controller requiring formal requirements and strict verification.
* A noncritical administrative dashboard requiring lighter controls.
* A commercial networking component requiring supplier evidence and interface testing.
* A custom analytics module requiring data-quality checks and model-performance evaluation.

The project may tailor engineering practices by component, provided that integration and system-level assurance remain adequate.

### 3.4 Tailoring hierarchy

A useful conceptual hierarchy is:

**Organizational framework → Project process profile → System-element practices → Work-package execution**

Decisions made at a lower level must respect applicable constraints imposed at higher levels.

## 4. Factors That Influence Tailoring

Tailoring should be based on the actual context rather than a single factor such as project size.

### 4.1 System complexity

Complexity may arise from:

* The number of components.
* Interdependencies among components.
* Distributed interfaces.
* Software and hardware interactions.
* Operational environments.
* Multiple stakeholder groups.
* External systems and suppliers.
* Emergent behavior.
* Uncertainty about how the system will behave when integrated.

As complexity increases, teams may need stronger architecture analysis, interface management, integration planning, and system-level testing.

A small system can still be complex if it has many dependencies or unpredictable interactions.

### 4.2 Criticality and consequences of failure

Criticality concerns the consequences of system failure or incorrect behavior.

Consider:

* Potential injury or loss of life.
* Environmental damage.
* Financial loss.
* Mission failure.
* Security compromise.
* Regulatory noncompliance.
* Loss of essential services.
* Damage to public trust.

Higher consequences generally justify stronger assurance, verification, validation, traceability, independent review, and risk controls.

The level of rigor should be based on the consequences and applicable assurance requirements, not merely the number of developers.

### 4.3 Uncertainty and novelty

Projects involving unfamiliar technology, uncertain requirements, or novel operating conditions may require more experimentation and learning.

Useful practices can include:

* Prototypes.
* Proofs of concept.
* Simulations.
* Technical demonstrations.
* Early integration.
* Incremental delivery.
* Feasibility studies.
* Targeted experiments.
* Frequent stakeholder feedback.

High uncertainty does not automatically mean less process. It may mean using more iterative learning while maintaining appropriate controls.

### 4.4 Project size and duration

A small project may need fewer formal coordination mechanisms than a large multi-organization program.

However, project size alone is not sufficient to determine rigor.

A small medical device or embedded controller may have substantial safety obligations. A large internal information system may have lower safety criticality but significant security and privacy obligations.

### 4.5 Stakeholder diversity

A project serving multiple departments, customers, countries, or regulatory authorities may need more formal requirements agreement and decision traceability.

Tailoring should account for:

* Different operational priorities.
* Conflicting requirements.
* Different approval authorities.
* Language and cultural differences.
* Distributed teams.
* External dependencies.
* Acceptance responsibilities.

### 4.6 Technology maturity

Mature, well-understood technology may reduce some technical uncertainties.

New technology may require:

* Feasibility assessments.
* Technology-readiness evaluations.
* Additional prototyping.
* Performance characterization.
* Compatibility studies.
* Expanded verification.
* Contingency planning.

Using mature components does not remove the need to verify system-level behavior.

### 4.7 Contractual and regulatory obligations

Some practices and evidence are mandatory because of law, regulation, contract, customer policy, or organizational governance.

Examples include:

* Required safety analyses.
* Regulatory submissions.
* Specific quality records.
* Contractually required reviews.
* Security assessments.
* Data-protection controls.
* Traceability records.
* Formal acceptance tests.

These obligations constrain tailoring. A project cannot unilaterally remove a contractual deliverable simply because it prefers a lighter process.

### 4.8 Team capability and organizational maturity

A team with strong automated testing, configuration management, experienced systems engineers, and mature tooling may execute certain activities more efficiently.

A less experienced team may need more guidance, structured reviews, or explicit documentation.

Automation can reduce manual effort, but the project must still establish that the automated process is suitable and produces reliable evidence.

### 4.9 Resource and schedule constraints

Limited resources can influence how activities are sequenced and performed.

Appropriate responses may include:

* Automating repetitive verification.
* Combining compatible reviews.
* Using risk-based sampling where justified.
* Prioritizing high-risk interfaces.
* Reusing qualified components.
* Delivering increments.
* Removing genuinely unnecessary work products.

Insufficient resources do not make essential risk controls unnecessary. If required rigor cannot be supported within the available budget or schedule, the project should address feasibility, scope, resources, or risk acceptance through the proper authority.

## 5. A Systematic Tailoring Process

A disciplined tailoring process helps ensure that decisions are justified, traceable, and consistent.

### Step 1: Establish the baseline

Identify the governing framework:

* Applicable standards.
* Organizational processes.
* Contractual requirements.
* Regulatory obligations.
* Customer requirements.
* Approved life-cycle model.
* Required reviews and deliverables.

The team must understand what is mandatory before deciding what can be adapted.

### Step 2: Understand the project context

Assess:

* Mission and intended use.
* Stakeholders.
* System boundaries.
* Complexity.
* Criticality.
* Technical novelty.
* Requirements stability.
* Team capability.
* Supplier dependencies.
* Operating environment.
* Cost and schedule constraints.

This assessment establishes why a standard process may need adaptation.

### Step 3: Identify candidate processes and practices

Review the processes, activities, methods, and work products in the baseline.

For each candidate, ask:

* Is this activity needed?
* What objective does it achieve?
* What risks does it control?
* Is it mandatory?
* Can it be combined with another activity?
* Can it be automated?
* Is an alternative method equally or more effective?
* What evidence will demonstrate that the objective has been achieved?

### Step 4: Assess risks and consequences

Evaluate the impact of modifying each process.

Potential consequences include:

* Increased technical uncertainty.
* Missed requirements.
* Reduced traceability.
* Weak integration assurance.
* Security exposure.
* Delayed defect discovery.
* Loss of decision evidence.
* Contractual noncompliance.
* Reduced maintainability.

A process should not be removed solely because it consumes time. Its purpose and risk contribution must be considered.

### Step 5: Define the tailored process

Document the selected approach.

Specify:

* Activities to be performed.
* Activities to be combined or adapted.
* Methods and tools to be used.
* Responsible roles.
* Required inputs and outputs.
* Review and approval points.
* Verification and validation evidence.
* Configuration and records requirements.
* Monitoring indicators.
* Escalation criteria.

The tailored process should be clear enough for team members and assessors to understand what will actually happen.

### Step 6: Justify and approve the tailoring

For each significant deviation, record:

* The baseline practice.
* The proposed modification.
* The rationale.
* The expected benefit.
* The associated risk.
* Compensating controls.
* The decision authority.
* Approval status.
* Conditions for reconsideration.

Approval should follow the organization's governance rules. A project manager should not approve an exception that is reserved for a safety authority, customer, regulator, or contract owner.

### Step 7: Implement and monitor

Apply the approved process and monitor whether it achieves its intended objectives.

Possible indicators include:

* Defect discovery trends.
* Rework levels.
* Requirements volatility.
* Integration failures.
* Review findings.
* Test coverage and results.
* Risk exposure.
* Change-request frequency.
* Delivery performance.

If the tailored approach produces unexpected problems, revise it through the authorized process.

### Step 8: Review and improve

At suitable milestones or after major changes, reconsider whether the tailoring remains appropriate.

Reassessment may be needed when:

* Scope changes substantially.
* New hazards are identified.
* A supplier changes.
* Technology proves less mature than expected.
* The operating environment changes.
* A regulatory obligation is introduced.
* Defect trends reveal inadequate controls.
* The project moves into a more critical life-cycle phase.

Tailoring is a managed decision, not necessarily a one-time activity.

## 6. Tailoring Rationale and Records

A good tailoring record explains why the chosen process is appropriate.

A useful structure is:

| Field                 | Purpose                                           |
| --------------------- | ------------------------------------------------- |
| Process or practice   | Identifies the baseline activity                  |
| Baseline expectation  | Describes the standard or organizational approach |
| Tailored approach     | States what will actually be done                 |
| Rationale             | Explains why the change fits the project          |
| Risk assessment       | Describes possible adverse effects                |
| Compensating controls | Shows how essential objectives remain protected   |
| Responsible owner     | Identifies who implements the decision            |
| Approval authority    | Identifies who authorizes the deviation           |
| Evidence              | Defines how effectiveness will be demonstrated    |
| Review trigger        | Specifies when the decision must be reconsidered  |

### Example: Tailoring a design review

**Baseline:** A formal multidisciplinary design review is required at a defined project milestone.

**Proposed tailoring:** For a low-risk internal dashboard, combine the architecture review with an existing technical review.

**Rationale:** The same qualified reviewers can assess the architecture, interfaces, security concerns, and deployment design in one session.

**Risk:** Combining reviews could cause an important topic to be overlooked.

**Compensating control:** Use a review checklist, record findings and decisions, assign actions, and require approval by the designated technical authority.

**Evidence:** Completed checklist, review record, action closure, and approved design baseline.

This is a stronger tailoring argument than simply stating, "The project is small, so the review is unnecessary."

## 7. Under-Tailoring and Over-Tailoring

### 7.1 Under-tailoring

Under-tailoring occurs when a project does not adapt the process sufficiently to its context.

Potential symptoms:

* Every project must produce the same large set of documents.
* Review schedules do not reflect technical risk.
* Teams repeat analyses that add no useful information.
* Low-risk changes require unnecessarily elaborate approval.
* Process overhead reduces time available for meaningful engineering.
* Team members focus on document completion instead of actual system outcomes.

Consequences may include increased cost, slower delivery, and lower productivity.

### 7.2 Over-tailoring

Over-tailoring occurs when a project removes or weakens too many controls or fails to preserve essential process objectives.

Potential symptoms:

* Requirements have no reliable baseline.
* Interfaces are undocumented.
* Test evidence is incomplete.
* Safety or security concerns are not analyzed.
* Changes are implemented without impact assessment.
* Acceptance criteria are vague.
* Decisions cannot be traced.
* Mandatory obligations are ignored.
* No one owns system-level integration.

Consequences may include expensive rework, defects, incidents, noncompliance, and loss of stakeholder confidence.

### 7.3 The right balance

The aim is not to find the shortest process or the most elaborate process.

The aim is to select a process that achieves the required outcomes with a level of effort and rigor proportionate to the system's context and risk.

## 8. Tailoring Life-Cycle Models

The choice of life-cycle model is related to tailoring but is not identical to it.

A life-cycle model organizes the stages and activities through which a system is conceived, developed, produced, operated, maintained, and retired.

Tailoring determines how the chosen framework and its activities are adapted to the project's circumstances.

### 8.1 Sequential or plan-driven approaches

A plan-driven approach may be appropriate when:

* Requirements are relatively stable.
* External approval gates are important.
* Physical manufacturing has long lead times.
* Changes are costly.
* Formal evidence is required.
* Multiple organizations need a controlled baseline.

Potential tailoring choices include the frequency of reviews, depth of analysis, and level of documentation.

### 8.2 Iterative and incremental approaches

An iterative approach allows the solution to evolve through repeated cycles. An incremental approach delivers capability in manageable portions.

These approaches can be useful when:

* Stakeholders need early demonstrations.
* Requirements are expected to evolve.
* Technical uncertainty is significant.
* Feedback can improve the design.
* Software can be delivered in controlled increments.

Tailoring may involve:

* Shorter feedback cycles.
* Incremental requirements elaboration.
* Continuous integration.
* Automated regression testing.
* Frequent risk reviews.
* Progressive architecture refinement.

Iterative delivery does not eliminate the need for architecture, traceability, configuration control, safety assurance, or acceptance evidence where those are necessary.

### 8.3 Agile and hybrid approaches

Agile practices emphasize frequent feedback, collaboration, and adaptation. Hybrid approaches combine practices from different life-cycle models.

A hybrid system project might use:

* Formal system-level requirements and architecture.
* Iterative software development.
* Controlled hardware design baselines.
* Automated continuous integration.
* Formal system acceptance testing.
* Structured release and change authorization.

This can be suitable for systems combining software, hardware, suppliers, and regulated operations.

The key is to preserve the required systems-engineering outcomes across all teams and increments.

### 8.4 Life-cycle selection and tailoring example

Consider an autonomous warehouse robot.

Its project may use:

* Early prototypes to evaluate navigation algorithms.
* Iterative software development for user-facing features.
* Formal interfaces for sensors, actuators, and fleet-management systems.
* Hazard analysis for unsafe movement.
* Controlled hardware configuration.
* System-level verification in a representative warehouse.
* Formal operational acceptance.

This is a tailored hybrid approach: different activities use methods appropriate to their uncertainty, interfaces, and consequences of failure.

## 9. Risk-Based Rigor

Risk-based tailoring allocates effort according to uncertainty, likelihood, consequence, and the importance of the activity.

A common conceptual model is:

**Tailoring rigor should increase when the potential consequence of failure, uncertainty, or complexity increases.**

This is a principle, not a universal mathematical formula. Organizations should use their approved risk-assessment methods.

### 9.1 Example risk classification

| Project characteristic                    | Possible engineering response                                                                      |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Low complexity, low consequence           | Lightweight documentation, automated tests, focused reviews                                        |
| Moderate complexity, business-critical    | Controlled requirements, interface reviews, integration testing, formal change management          |
| High complexity, safety-critical          | Extensive traceability, hazard analysis, independent reviews, rigorous verification and validation |
| High uncertainty, low initial criticality | Prototyping, experiments, iterative development, explicit learning objectives                      |
| High security sensitivity                 | Threat analysis, access control, secure development practices, security testing and evidence       |

These are illustrative profiles. Actual controls depend on applicable standards, regulations, contracts, and project risks.

### 9.2 Compensating controls

If a particular activity is simplified, another control may help preserve its purpose.

Examples:

* Replace a manually compiled status report with a validated automated dashboard.
* Combine two compatible review meetings but retain both review objectives and records.
* Reduce duplicate documentation while preserving requirements traceability in a managed tool.
* Replace some repetitive manual regression tests with validated automation.
* Use a prototype to reduce uncertainty before committing to a detailed design.

A compensating control must actually address the risk. It should not be added merely to make an unjustified exception appear acceptable.

## 10. Common Tailoring Mistakes

### Mistake 1: Tailoring only to schedule

A deadline does not establish that a process is unnecessary.

**Better approach:** Identify the required outcome, assess the risk of reducing effort, and explore automation, sequencing, resource changes, or scope adjustments.

### Mistake 2: Assuming small systems are simple

A compact system may still have dangerous failure modes or strict legal obligations.

**Better approach:** Assess complexity and consequences separately from size.

### Mistake 3: Removing documentation without preserving information

A project may reduce the number of documents but accidentally lose design rationale, configuration history, or acceptance evidence.

**Better approach:** Preserve required information in an appropriate controlled form, which may be a document, repository, tool record, or another auditable artifact.

### Mistake 4: Treating agile as permission to omit engineering

Agile methods do not automatically make architecture, risk management, interface definition, or verification unnecessary.

**Better approach:** Adapt the timing and methods while preserving the necessary engineering outcomes.

### Mistake 5: Tailoring without approval

A team may unintentionally violate organizational policy or contractual obligations.

**Better approach:** Identify the appropriate decision authority and document approvals before implementing significant deviations.

### Mistake 6: Never revisiting tailoring decisions

A process suitable during early exploration may be inadequate before production or deployment.

**Better approach:** Define review triggers and reassess tailoring as risk, scope, and maturity change.

### Mistake 7: Confusing a tool with a process

Purchasing a requirements-management or project-management tool does not establish that requirements or risks are managed effectively.

**Better approach:** Define responsibilities, workflow, decision rules, and evidence. Use tools to support that process.

## 11. Case Study: Tailoring a Smart Industrial Monitoring Platform

### 11.1 Scenario

A company develops a platform that collects sensor data from industrial machines and alerts maintenance teams.

The project includes:

* Sensor hardware from a supplier.
* Gateway software.
* A cloud data-processing service.
* A dashboard for operators.
* Integration with an existing maintenance system.

The first release is intended for a non-safety-critical pilot. Future releases may support more operationally critical machinery.

The team has limited resources and wants to use an iterative delivery approach.

### 11.2 Initial proposal

The project proposes to:

1. Use lightweight requirements for the dashboard.
2. Automate software unit and regression testing.
3. Perform formal interface reviews for the sensors and gateway.
4. Conduct a security review of the cloud service.
5. Perform end-to-end testing before pilot deployment.
6. Maintain configuration control for deployed versions.
7. Use short stakeholder feedback cycles.
8. Defer some formal production-readiness activities until the pilot is evaluated.

This approach may be reasonable, but it needs documented rationale and approval. Deferring production-readiness activities is not the same as waiving mandatory pilot safety, security, or operational controls.

### 11.3 Tailoring assessment

**Dashboard requirements:** Lightweight user stories may be appropriate if acceptance criteria remain clear and the dashboard's functions are adequately tested.

**Software testing:** Automated unit and regression tests can reduce repeated manual effort, provided the tests are reliable and sufficiently cover relevant behavior.

**Interfaces:** Formal interface specifications are justified because multiple components and suppliers must exchange data consistently.

**Security:** The cloud service requires security controls appropriate to the data, access, deployment model, and threat environment.

**System integration:** End-to-end tests are necessary to verify that the complete monitoring chain behaves as intended.

**Configuration management:** Deployed versions and critical configuration data must be controlled so that defects can be traced and rollbacks can be performed.

**Future critical use:** If the platform later influences safety-related decisions, the project must reassess its process profile. The pilot's lightweight approach should not automatically become the production baseline.

### 11.4 Tailoring record example

| Item                 | Decision                                                                               |
| -------------------- | -------------------------------------------------------------------------------------- |
| Process area         | Software regression testing                                                            |
| Baseline             | Manual regression suite executed for each release                                      |
| Tailored approach    | Automate repeatable regression tests and retain focused manual exploratory testing     |
| Rationale            | Reduce repetitive effort and obtain faster feedback                                    |
| Risk                 | Automated tests may miss usability or unanticipated behavior                           |
| Compensating control | Retain exploratory testing and end-to-end acceptance tests                             |
| Evidence             | Test results, defect records, release review, and acceptance evidence                  |
| Reassessment trigger | Major architecture change, critical defect trend, or expansion into safety-related use |

### 11.5 Outcomes

The project can use fewer repetitive manual activities while preserving interface control, security assurance, system-level testing, and release evidence.

The key is that process changes are based on risk and purpose, not on convenience alone.

## 12. Practical Exercises with Suggested Answers

### Exercise 1: Small but safety-critical

A small embedded device controls a heating element. The team argues that its small size justifies minimal testing.

**Question:** Is this sufficient justification?

**Suggested answer:** No. Physical size does not determine the consequences of failure. The team should assess hazards, applicable obligations, and operating conditions before selecting verification, validation, and assurance activities.

### Exercise 2: Reduce documentation overhead

A project produces three separate reports containing nearly identical status information.

**Question:** How could this be tailored?

**Suggested answer:** Consolidate the reports or generate them from a controlled source, provided that each report's required purpose, audience, approval, and retained information are preserved. Document the change if organizational policy requires it.

### Exercise 3: New technology

A project uses an unfamiliar machine-learning model for predictive maintenance.

**Question:** Should the project reduce process rigor because the requirements are uncertain?

**Suggested answer:** Not automatically. It may use prototypes, experiments, iterative evaluation, and explicit model-performance criteria to manage uncertainty. It should also define data quality, validation conditions, limitations, monitoring, and the consequences of incorrect predictions.

### Exercise 4: Missing organizational approval

A project manager removes a mandatory architecture review to meet a deadline.

**Question:** What is the primary problem?

**Suggested answer:** The project has bypassed the required governance process. The team should assess the schedule and risk impacts and seek authorization from the designated authority before changing the mandatory review.

### Exercise 5: Agile system project

A software team works in two-week sprints, but its hardware supplier delivers components only every three months.

**Question:** What tailoring approach may be suitable?

**Suggested answer:** A hybrid approach may align iterative software development with hardware milestones, formal interface control, integration planning, and system-level verification. The team should coordinate baselines and dependencies across both cadences.

### Exercise 6: Automated testing

A project replaces all manual testing with an automated suite.

**Question:** What should be evaluated?

**Suggested answer:** Determine whether the automated tests cover the required behaviors, interfaces, failure conditions, performance, security, and relevant user interactions. Automation may be effective for repeatable checks, but it does not automatically replace exploratory testing or other evidence.

### Exercise 7: Changed system criticality

A pilot monitoring tool is later proposed for use in a process where missed alarms could cause serious injury.

**Question:** What should happen to the existing tailoring decisions?

**Suggested answer:** Reassess them against the new operating context and consequences. Additional hazard analysis, requirements rigor, verification, validation, independent assessment, and formal approval may be required. The pilot process should not be assumed adequate.

### Exercise 8: Supplier integration

Three suppliers use different data formats and have unclear interface responsibilities.

**Question:** Which tailoring decision would be inappropriate?

**Suggested answer:** Removing interface management to save time would be inappropriate because the integration risk is high. The project should establish clear interface agreements, ownership, and integration tests.

### Exercise 9: Review consolidation

A project wants to combine its architecture review and design review into one meeting.

**Question:** Under what conditions could this be acceptable?

**Suggested answer:** If policy permits it, the combined review can adequately address both sets of objectives, the required participants and authorities are present, findings and actions are recorded, and the change is approved where required.

### Exercise 10: Evaluate a tailoring proposal

A team proposes eliminating requirements traceability because the requirements are stored in a spreadsheet.

**Question:** Is the spreadsheet sufficient justification?

**Suggested answer:** No. The tool format does not determine whether traceability is necessary. The team must consider risk, change impact, verification coverage, and applicable obligations. If traceability remains necessary, it can be maintained in a spreadsheet or another suitable controlled system.

## 13. Original CSEP-Style Practice Questions

**These are original practice questions, not official INCOSE examination items.**

### Question 1

What is the primary purpose of tailoring?

A. Eliminate all systems-engineering processes.
B. Adapt processes and practices to the project's context while preserving necessary outcomes and obligations.
C. Ensure that every project uses identical documentation.
D. Remove all approval requirements.

**Correct answer: B.**

**Explanation:** Tailoring adapts the process to the context and risk. It is not arbitrary process removal.

### Question 2

Which factor should most directly influence the rigor of assurance activities?

A. The number of pages in the project plan.
B. The personal preference of the project manager.
C. The consequences of failure, relevant uncertainty, and applicable obligations.
D. The color scheme used by the engineering team.

**Correct answer: C.**

**Explanation:** Engineering rigor should reflect risk and mandatory constraints, among other contextual factors.

### Question 3

Which statement best describes organizational-level tailoring?

A. Each developer chooses a different process without coordination.
B. The organization establishes common process frameworks and approved profiles for projects.
C. The supplier unilaterally changes customer requirements.
D. The organization eliminates all project-specific decisions.

**Correct answer: B.**

**Explanation:** Organizational tailoring provides common rules and options that projects can apply consistently.

### Question 4

A project wants to simplify a review process. What is the strongest justification?

A. The review takes too long.
B. The team dislikes documentation.
C. The revised approach preserves the review objectives and required evidence while reducing unnecessary effort.
D. Another project once skipped the review.

**Correct answer: C.**

**Explanation:** Effective tailoring is justified by objectives, risk, and evidence—not convenience alone.

### Question 5

Which is an example of over-tailoring?

A. Automating repetitive regression tests while retaining necessary system tests.
B. Combining compatible reviews with approved procedures.
C. Removing interface controls from a multi-supplier system despite significant integration risk.
D. Using prototypes to investigate technical uncertainty.

**Correct answer: C.**

**Explanation:** Removing a necessary control without addressing the underlying risk weakens the engineering process.

### Question 6

A project uses agile software development within a larger regulated system. Which statement is most accurate?

A. Agile development makes system-level verification unnecessary.
B. Agile development prohibits formal requirements.
C. Agile practices can be combined with system-level controls and assurance appropriate to the project.
D. Each sprint automatically constitutes final system acceptance.

**Correct answer: C.**

**Explanation:** Life-cycle practices can be combined when the tailored approach preserves required engineering outcomes.

### Question 7

What should be included in a significant tailoring record?

A. Only the project manager's name.
B. The change, rationale, risk, compensating controls, approval, and evidence.
C. Only the revised schedule.
D. Only a statement that the team agreed.

**Correct answer: B.**

**Explanation:** The record should make the decision understandable, reviewable, and traceable.

### Question 8

A team removes a mandatory contractual deliverable because it believes the deliverable provides little value. What is the correct response?

A. Proceed because tailoring always overrides contracts.
B. Remove the requirement from the project plan without notice.
C. Follow the applicable contractual change and approval process; do not unilaterally waive the obligation.
D. Assume that the supplier will resolve the issue.

**Correct answer: C.**

**Explanation:** Tailoring remains constrained by contractual, regulatory, and organizational obligations.

### Question 9

A project is initially low risk, but a later release will control a hazardous industrial process. What should the team do?

A. Retain the original process automatically.
B. Reassess the process profile and required controls against the changed context.
C. Reduce testing because the team already has experience.
D. Avoid documenting the change.

**Correct answer: B.**

**Explanation:** Tailoring should be revisited when system context, intended use, or consequences of failure change.

### Question 10

Which statement best describes a compensating control?

A. An unrelated activity added to make a plan longer.
B. A measure intended to address a risk introduced by a tailored process.
C. A reason to ignore mandatory regulation.
D. A replacement for all project governance.

**Correct answer: B.**

**Explanation:** A compensating control should preserve the necessary risk reduction or process objective affected by the change.

## 14. Revision Notes

Remember these core principles:

* **Tailoring:** Adapt engineering processes to the project's context while preserving necessary outcomes.
* **Organizational tailoring:** Establishes common processes, profiles, and rules.
* **Project tailoring:** Selects and adapts practices for a specific project.
* **Risk-based rigor:** Higher consequences, uncertainty, and complexity may justify stronger controls.
* **Mandatory obligations:** Laws, regulations, contracts, and required governance constrain tailoring.
* **Tailoring rationale:** Explains the change, benefit, risks, and reasons for selecting the approach.
* **Compensating controls:** Address risks created by simplifying or changing a practice.
* **Under-tailoring:** Applies excessive or unsuitable process overhead without adequate adaptation.
* **Over-tailoring:** Removes necessary controls or fails to preserve required engineering outcomes.
* **Life-cycle selection:** Chooses an overall development and operation approach; tailoring adapts how its practices are applied.
* **Continuous reassessment:** Revisits tailoring when project conditions, risks, or intended use change.

A useful decision test is:

1. What objective does the original practice achieve?
2. Is the practice mandatory?
3. What risk results if it is changed?
4. Can another approach achieve the same objective?
5. Who must approve the change?
6. What evidence will demonstrate that the tailored approach is effective?

## 15. References and Further Study

1. **ISO/IEC/IEEE 15288, Systems and software engineering — System life cycle processes.** Consult the edition specified for your study and review its framework for system life-cycle processes and their application.
2. **INCOSE Systems Engineering Handbook.** Use the edition aligned with your CSEP study materials for guidance on applying systems engineering in different project contexts.
3. **INCOSE Certification Program.** Check the current official certification guidance and applicable knowledge reference list.
4. **NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev. 2.** Supplementary guidance on life-cycle models, technical management, risk, reviews, verification, and validation.
5. **ISO 31000, Risk management — Guidelines.** Useful background on structured risk management and risk-informed decisions.
6. **ISO 9001, Quality management systems — Requirements.** Useful context for organizational processes, controlled records, and quality assurance.
7. **Applicable domain standards and regulations.** Safety-critical, medical, aerospace, automotive, industrial, and cybersecurity projects may have additional mandatory requirements that affect tailoring.

**Study approach:** Practice explaining not only which process you would tailor, but why, what risk the change creates, what controls remain necessary, and how you would demonstrate that the decision is acceptable.
