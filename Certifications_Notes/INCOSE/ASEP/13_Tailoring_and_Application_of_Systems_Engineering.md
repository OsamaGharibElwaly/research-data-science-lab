# Module 13: Tailoring and Application of Systems Engineering

## INCOSE ASEP Preparation Course

**Suggested filename:** `13_Tailoring_and_Application_of_Systems_Engineering.md`

**Purpose:** Understand how to apply systems engineering appropriately to different projects, considering complexity, risk, life-cycle stage, resources, stakeholder needs, and organizational constraints.

**Exam note:** This is original study material aligned with established systems-engineering concepts. The practice questions are not official INCOSE exam questions.

---

# 1. Learning Objectives

By the end of this module, you should be able to:

1. Define tailoring in systems engineering.
2. Explain why systems-engineering processes must be adapted to context.
3. Identify factors that influence the selection and application of processes.
4. Distinguish legitimate tailoring from unjustified omission of necessary activities.
5. Apply risk-based thinking to process selection.
6. Understand how complexity, uncertainty, and system criticality affect engineering rigor.
7. Explain the role of organizational policies, contracts, and standards.
8. Apply tailoring to projects involving software, hardware, cloud infrastructure, and integrated systems.
9. Evaluate tailoring decisions using practical scenarios.
10. Prepare for ASEP-style questions about tailoring and process application.

# 2. What Is Tailoring?

## 2.1 Definition

Tailoring is the deliberate adaptation of a systems-engineering process, method, procedure, or set of activities to suit the characteristics and constraints of a particular project, system, or organization.

A systems-engineering approach that is appropriate for a complex aircraft-control system may be unnecessarily burdensome for a small internal application. Conversely, a lightweight process that works for a low-risk application may be inadequate for a safety-critical medical device.

Tailoring seeks an appropriate level of rigor rather than maximum formality or minimum effort.

The goal is to retain the activities, controls, evidence, and decisions necessary to achieve the system's objectives while avoiding unnecessary process overhead.

## 2.2 Why Tailoring Is Necessary

Projects differ in:

* System complexity.
* Technical novelty.
* Safety consequences.
* Security and privacy exposure.
* Stakeholder expectations.
* Regulatory obligations.
* Contractual commitments.
* Budget and schedule.
* Team size and experience.
* Supplier involvement.
* Environmental conditions.
* Operational life span.
* Maintenance requirements.

Applying exactly the same process depth to every project may waste resources in some cases and leave important risks uncontrolled in others.

Tailoring helps the organization align engineering effort with actual needs.

## 2.3 Tailoring Is Not Arbitrary Process Removal

Tailoring does not mean that a project manager can remove any activity considered inconvenient.

A tailoring decision must respect:

* Applicable laws and regulations.
* Contractual obligations.
* Organizational policies.
* Mandatory standards or approved procedures.
* Stakeholder commitments.
* Safety and security obligations.
* Required approvals.
* The risks associated with the proposed change.

For example, a project cannot simply omit a mandatory acceptance test because the schedule is late. The appropriate response is to evaluate options through the authorized process and preserve applicable obligations.

**Core principle:** Tailoring is justified adaptation within applicable constraints, not an excuse to ignore requirements.

# 3. Tailoring Versus Standardization

These concepts are complementary rather than contradictory.

## 3.1 Standardization

Standardization establishes common processes, methods, terminology, templates, interfaces, and expectations.

Benefits include:

* Consistency across teams.
* Reuse of proven practices.
* Easier training.
* More predictable reviews.
* Better communication.
* Improved interoperability.
* Reduced duplication.

## 3.2 Tailoring

Tailoring adapts those common practices to the specific needs of a project.

Benefits include:

* Proportional engineering effort.
* Better alignment with project risk.
* Flexibility for unusual technical problems.
* More efficient resource use.
* Better handling of uncertainty.
* Reduced unnecessary documentation.

## 3.3 How They Work Together

An organization may define a standard engineering process and identify which activities are mandatory, conditional, or optional.

Projects then select and tailor activities according to defined criteria and approval rules.

For example, an organization might require every project to maintain configuration control but permit different levels of formality depending on the project's scale and risk.

A small application may use a controlled repository, versioned releases, and documented change reviews. A safety-critical system may additionally require formal baselines, independent assessments, detailed change-impact analysis, and extensive configuration audits.

Both projects use configuration management, but the depth of implementation differs.

# 4. Factors That Influence Tailoring

## 4.1 System Complexity

Complexity may arise from:

* The number of system elements.
* The number of interfaces.
* Interdependencies among components.
* The number of stakeholders.
* Emergent system behavior.
* Multiple operating environments.
* Technical novelty.
* Distributed development teams.
* External system dependencies.

A system with many interacting components may require stronger architecture definition, interface control, integration planning, and verification than a system with few independent elements.

However, component count alone does not determine complexity. A small system with highly coupled or safety-critical behavior can require substantial engineering rigor.

## 4.2 Risk and Criticality

The consequences of failure strongly influence process rigor.

Consider three systems:

1. A personal task-tracking application.
2. A company's production database.
3. A flight-control system.

A defect in the task-tracking application may cause inconvenience. A production-database failure may interrupt business operations and cause data loss. A flight-control failure may create catastrophic consequences.

The engineering effort should reflect these differences.

Higher-risk systems may require:

* More extensive hazard analysis.
* Stronger requirements traceability.
* Greater verification independence.
* More rigorous configuration control.
* Formal technical reviews.
* More detailed failure analysis.
* Additional redundancy or fault tolerance.
* Stronger evidence of compliance.

Risk-based tailoring should consider both likelihood and consequences, along with uncertainty and applicable obligations.

## 4.3 Technical Novelty

A project using established technology may have fewer unknowns than a project developing a novel algorithm, material, or control mechanism.

Higher novelty can justify:

* Feasibility studies.
* Prototypes.
* Technology demonstrations.
* Simulations.
* Early experiments.
* More frequent technical reviews.
* Additional contingency planning.

The purpose is to reduce uncertainty before committing to expensive implementation or deployment decisions.

## 4.4 Requirements Stability

Stable requirements can support a more predictable development approach.

Frequently changing requirements may justify more iterative development, frequent stakeholder feedback, stronger change-impact analysis, and short feedback cycles.

Requirements volatility does not remove the need for control. It changes how the team manages and incorporates change.

## 4.5 Life-Cycle Stage

The appropriate activities depend partly on the system's current stage.

During early concept development, emphasis may be placed on stakeholder needs, feasibility, alternatives, and risk reduction.

During architecture and design, emphasis may shift toward requirements allocation, interfaces, technical analysis, and design evaluation.

During integration and verification, the emphasis may be on controlled configurations, test environments, defect resolution, and evidence of compliance.

During operation, maintenance, and disposal, emphasis may shift toward reliability, supportability, operational risk, upgrades, data handling, and retirement obligations.

Tailoring should account for the current stage without ignoring obligations established earlier.

## 4.6 Team Capability

A team with experienced systems engineers and established tools may execute some activities efficiently.

A less experienced team may require additional:

* Templates.
* Guidance.
* Mentoring.
* Peer reviews.
* Training.
* Checklists.
* Independent support.

A small team is not automatically entitled to less rigor. If the team lacks a critical competency, the appropriate response may be to acquire that competency rather than omit the associated engineering activity.

## 4.7 Supplier and Interface Complexity

Projects involving multiple suppliers, contractors, or external systems may need more formal agreements and interface controls.

Relevant considerations include:

* Allocation of responsibilities.
* Interface specifications.
* Data ownership.
* Version compatibility.
* Acceptance criteria.
* Change notification.
* Verification evidence.
* Supplier qualification.
* Delivery schedules.
* Support obligations.

The greater the number of independent organizations, the more important clear responsibilities and controlled interfaces may become.

# 5. A Practical Tailoring Method

The following method provides a structured way to tailor systems-engineering processes.

## Step 1: Understand the System and Its Context

Identify:

* The intended purpose.
* Stakeholder needs.
* System boundaries.
* Operating environments.
* Major interfaces.
* Relevant life-cycle stages.
* Constraints and assumptions.

Tailoring cannot be justified until the engineering team understands what the project is trying to achieve.

## Step 2: Identify Applicable Obligations

Review:

* Laws and regulations.
* Contracts.
* Organizational policies.
* Customer requirements.
* Applicable standards.
* Safety and security obligations.
* Required approval authorities.

Separate mandatory requirements from practices that may be adapted.

## Step 3: Assess Risk and Uncertainty

Identify major risks related to:

* Safety.
* Security.
* Performance.
* Reliability.
* Technical feasibility.
* Integration.
* Schedule.
* Cost.
* Operations.
* Maintenance.
* Disposal.

Determine which risks require additional analysis, control, or evidence.

## Step 4: Identify the Candidate Processes

Start with the organization's standard processes or another justified process baseline.

Consider activities for:

* Stakeholder needs and requirements.
* System requirements.
* Architecture.
* Design.
* Analysis.
* Implementation.
* Integration.
* Verification.
* Validation.
* Transition.
* Operation.
* Maintenance.
* Disposal.
* Technical and project management.

The exact set and terminology depend on the applicable life-cycle model and project context.

## Step 5: Determine the Required Rigor

For each activity, determine the appropriate depth, frequency, formality, independence, documentation, and evidence.

For example:

* A low-risk change may require a brief review and regression test.
* A change affecting a critical interface may require impact analysis, formal review, and broader regression testing.
* A safety-significant change may require additional independent assessment and documented authorization.

## Step 6: Document the Tailoring Rationale

Record important decisions, including:

* The process or activity being tailored.
* The reason for the decision.
* Relevant risks and constraints.
* Alternative approaches considered.
* Expected consequences.
* Compensating controls.
* Approval authority.
* Conditions that would trigger reconsideration.

Documentation should be proportionate to the significance of the decision.

## Step 7: Obtain Required Approval

Submit the proposed tailoring to the designated authority when organizational procedures, contracts, or applicable obligations require approval.

A project manager should not assume that schedule ownership automatically grants authority to waive technical or compliance obligations.

## Step 8: Implement and Monitor

Apply the approved approach and monitor whether it remains suitable.

New evidence may reveal that:

* The risk was underestimated.
* The system is more complex than expected.
* Requirements are changing.
* Additional verification is needed.
* A planned simplification is causing defects.
* A different life-cycle approach would be more effective.

Tailoring should be revisited when the project's context changes materially.

# 6. Tailoring Documentation and Decision Records

## 6.1 Why Document Decisions?

A documented tailoring rationale helps future team members understand why the project uses a particular process.

It also supports:

* Reviews and audits.
* Consistency across teams.
* Risk management.
* Change-impact analysis.
* Accountability.
* Transfer of knowledge.
* Reassessment when conditions change.

The purpose is not to create paperwork for its own sake. It is to preserve the reasoning needed to make and review engineering decisions.

## 6.2 Example Tailoring Record

**Project:** Internal business analytics dashboard.

**Activity:** Formal system architecture review.

**Proposed approach:** Conduct a documented peer review rather than a separate multi-department review board.

**Rationale:** The system has a limited number of interfaces, uses established technology, and has no safety-critical control functions.

**Constraints:** Security, privacy, access control, backup, and deployment requirements remain applicable.

**Risks considered:** Data-access errors, integration defects, and service interruption.

**Controls:** Peer review, requirements traceability, automated testing, controlled releases, and a documented rollback procedure.

**Approval:** Obtain approval from the authority designated by organizational procedures.

**Reassessment trigger:** Significant changes in data sensitivity, integration scope, user population, or operational criticality.

This example is illustrative. Whether the proposed approach is acceptable depends on the organization's actual policies and obligations.

# 7. Tailoring Across Different Project Types

## 7.1 Small Internal Software Application

A small internal application may have:

* A limited user population.
* A narrow set of interfaces.
* Established technology.
* Relatively low consequences of failure.

Potential tailoring choices include lightweight requirements documentation, automated tests, peer reviews, version control, and a simple release process.

However, sensitive data, production dependencies, or business-critical functions can increase the required rigor.

## 7.2 Enterprise IT Infrastructure

An enterprise network or infrastructure modernization project may involve:

* Many users and locations.
* Legacy systems.
* Security and availability requirements.
* Complex migration activities.
* Supplier dependencies.
* Operational continuity constraints.

This project may require detailed interface and configuration documentation, migration planning, staged deployment, rollback procedures, change authorization, and operational readiness reviews.

## 7.3 Safety-Critical Medical Device

A medical device may have significant safety, regulatory, reliability, and traceability obligations.

Appropriate rigor may include:

* Detailed hazard analysis.
* Controlled requirements and design records.
* Formal verification.
* Risk-based independence.
* Configuration control.
* Validation with representative use conditions.
* Documented change assessment.
* Formal release and post-deployment monitoring.

Applicable medical-device standards and regulations must be considered. Tailoring cannot override binding obligations.

## 7.4 Experimental AI System

An experimental AI system may involve uncertainty about model behavior, data quality, and performance under new conditions.

Useful practices may include:

* Early prototypes.
* Data-quality analysis.
* Experiment tracking.
* Evaluation datasets.
* Reproducible environments.
* Model-version control.
* Performance and robustness evaluation.
* Human oversight appropriate to the use case.
* Monitoring for behavior changes.

An experimental system used only for internal exploration may justify different deployment controls from a model used to make consequential decisions about people.

The intended use and impact matter more than the label "AI."

# 8. Tailoring and Life-Cycle Models

Tailoring may influence the selection and application of a life-cycle model.

## 8.1 Sequential Development

A sequential approach may be suitable when requirements and interfaces are sufficiently stable and the system can be developed through well-defined stages.

It may emphasize formal stage reviews, documented baselines, and planned verification activities.

Its suitability depends on the project context; sequential development is not inherently superior or inferior to iterative development.

## 8.2 Iterative Development

An iterative approach develops and evaluates the solution through repeated cycles.

It may be appropriate when requirements, feasibility, or stakeholder preferences are uncertain.

Useful controls include:

* Iteration objectives.
* Defined acceptance criteria.
* Configuration management.
* Stakeholder feedback.
* Risk assessment.
* Regression testing.
* Controlled incorporation of changes.

Iteration should generate evidence and learning rather than repeat development without clear objectives.

## 8.3 Incremental Development

An incremental approach delivers capabilities in stages.

It may allow early delivery of useful functionality and feedback from real use.

The project must still manage dependencies, system-level requirements, integration, and the consequences of partial deployment.

## 8.4 Hybrid Approaches

A project may combine approaches.

For example, a hardware platform may follow relatively fixed manufacturing and qualification stages, while its supporting software is developed iteratively.

The system-level approach should ensure that the different development streams remain compatible and that their integration and verification needs are addressed.

# 9. Common Tailoring Mistakes

## Mistake 1: Reducing Rigor Only to Save Time

Schedule pressure is not sufficient justification for removing important engineering controls.

**Better approach:** Identify the actual bottleneck, evaluate alternatives, and preserve necessary risk controls.

## Mistake 2: Treating Every Project as Equally Risky

Applying the same depth of documentation and review to every system can waste resources.

**Better approach:** Use project context, risk, complexity, and obligations to determine proportional rigor.

## Mistake 3: Confusing Small Size With Low Risk

A small software component can control a critical process or expose sensitive information.

**Better approach:** Assess consequences and dependencies rather than relying on project size alone.

## Mistake 4: Assuming Agile Means No Documentation

Iterative development still needs sufficient requirements, design information, test evidence, configuration control, and decision records for its context.

**Better approach:** Create useful documentation that supports communication, operation, maintenance, and change—not documentation merely for appearance.

## Mistake 5: Ignoring External Obligations

A project may follow its internal process while still violating a contract or applicable regulation.

**Better approach:** Identify obligations before approving tailoring decisions.

## Mistake 6: Failing to Reassess Tailoring

An approach suitable during a prototype phase may be insufficient when the system enters production.

**Better approach:** Reassess process rigor when scope, users, risk, interfaces, or life-cycle stage changes materially.

## Mistake 7: Removing an Activity Without Replacing Its Function

Removing a formal review may also remove an important opportunity to identify interface or safety problems.

**Better approach:** Determine what risk the activity controls. If the activity is changed, ensure that its necessary purpose remains covered by an appropriate method.

# 10. Risk-Based Tailoring

## 10.1 Basic Principle

Risk-based tailoring directs engineering effort toward the areas where failure, uncertainty, or inadequate evidence could have the greatest consequences.

Risk is often considered in terms of likelihood and consequence, but a practical assessment should also consider uncertainty, detectability, exposure, and the effectiveness of existing controls where relevant.

A simple qualitative matrix can help organize discussion, but it should not replace a required formal risk-assessment method.

## 10.2 Example Risk Matrix

| Likelihood | Consequence | Illustrative interpretation                                             |
| ---------- | ----------- | ----------------------------------------------------------------------- |
| Low        | Low         | Limited additional controls may be appropriate                          |
| High       | Low         | Frequent issues may require efficient preventive measures               |
| Low        | High        | Strong controls may still be justified because consequences are serious |
| High       | High        | Urgent risk treatment and close oversight are likely necessary          |

A low likelihood does not automatically justify low rigor when consequences are severe.

For example, a rare failure in a safety-critical system may still require extensive prevention and evidence.

## 10.3 Compensating Controls

If a process is simplified, the team should consider whether alternative controls can preserve the necessary risk reduction.

Examples include:

* Automated checks replacing some manual checks.
* A targeted independent review replacing a broader review when permitted.
* Risk-focused testing in addition to standard regression testing.
* Reusable approved components reducing repeated design effort.
* Continuous integration and automated test pipelines supporting frequent verification.

A compensating control is acceptable only if it is effective for the risk being managed and permitted by the applicable obligations.

## 10.4 Tailoring and Uncertainty

When uncertainty is high, teams may initially choose more investigation, experimentation, and review rather than committing to a fixed detailed solution.

As evidence accumulates, the approach can become more focused.

For example, an engineering team may initially prototype two alternative communication architectures. After testing demonstrates that one alternative meets the required latency and reliability, the team may reduce further exploration and concentrate on implementation and integration.

Tailoring is therefore dynamic: process decisions can change as knowledge improves.

# 11. Integrated Case Study: Network Modernization Project

## 11.1 Scenario

A company plans to modernize its enterprise network across several buildings.

The project includes new switches, routing changes, VLAN segmentation, wireless access, centralized monitoring, and migration of production services.

The organization has limited budget and wants to minimize downtime.

The team proposes eliminating detailed interface documentation and formal migration reviews to accelerate deployment.

## 11.2 Assessing the Proposal

### Step 1: Understand the context

The project affects multiple locations, users, applications, and network segments. A failure could interrupt business operations.

### Step 2: Identify obligations

Review organizational change-control requirements, cybersecurity policies, service commitments, and contractual obligations.

### Step 3: Identify risks

Potential risks include routing failures, incorrect VLAN assignments, security exposure, configuration incompatibility, and unsuccessful rollback.

### Step 4: Evaluate tailoring options

Some documentation and review activities may be simplified if equivalent controls remain effective and the change is authorized. However, removing all interface documentation or migration checks may leave major risks uncontrolled.

### Step 5: Define proportionate controls

Possible controls include:

* Controlled network diagrams.
* Versioned configurations.
* Addressing and VLAN documentation.
* Staged migration.
* Predeployment testing.
* Peer review.
* Backup configurations.
* Rollback procedures.
* Post-change connectivity and security checks.
* Defined change approval.

### Step 6: Monitor and reassess

If a pilot migration reveals unexpected dependencies, the project should update its plan and process rigor accordingly.

## 11.3 Key Lesson

Tailoring should reduce unnecessary overhead while preserving the engineering functions needed to manage system risk. A faster process is not better if it increases the probability or consequences of failure beyond acceptable limits.

# 12. Practical Exercises

## Exercise 1: Identify Tailoring Factors

A team is developing a low-cost sensor for a noncritical environmental-monitoring application.

Identify at least six factors that should influence its systems-engineering approach.

### Suggested answer

Factors include intended use, consequences of failure, environmental conditions, stakeholder needs, interface complexity, technical novelty, applicable standards, team capability, maintenance requirements, and budget.

The system's low criticality may support a lightweight process, but that conclusion should follow from assessment rather than assumption.

## Exercise 2: Mandatory Versus Adaptable Activities

A project manager proposes removing an acceptance test required by the customer because the schedule is delayed.

1. Is this automatically acceptable?
2. What should the project do?
3. Why is this not simply a question of process efficiency?

### Suggested answer

1. No.
2. Assess the situation, review the contract and applicable obligations, evaluate alternatives, and use the authorized change process if a change is permissible.
3. The test may be part of a binding acceptance obligation or a critical risk control. Efficiency cannot justify unauthorized noncompliance.

## Exercise 3: Tailoring for Risk

Compare these systems:

* A personal note-taking application.
* A production payroll system.
* An industrial emergency-shutdown controller.

Describe how risk could affect verification, configuration management, and review rigor.

### Suggested answer

The note-taking application may need proportionate testing and release controls based on its actual data and availability risks. The payroll system may need stronger data-integrity, privacy, access-control, backup, and recovery evidence. The emergency-shutdown controller may require extensive safety analysis, rigorous verification, formal change control, and appropriate independence.

Exact obligations depend on the system, domain, and applicable standards.

## Exercise 4: Compensating Controls

An organization wants to replace a lengthy manual regression-testing procedure with automated tests.

Identify four conditions that should be evaluated before approving the change.

### Suggested answer

Evaluate whether the automated tests cover the required behavior, whether test results are reliable, whether the environment and configurations are controlled, whether failures are reported and investigated, and whether any mandatory independent or manual checks must remain.

The organization should also validate the new approach and retain the required evidence.

## Exercise 5: Dynamic Tailoring

A prototype project begins with high technical uncertainty. After several experiments, the main design risks are resolved.

Explain how the engineering approach might change.

### Suggested answer

The team may reduce exploratory prototyping and concentrate on detailed design, implementation, integration, and planned verification. Requirements, configuration control, and necessary risk controls remain applicable. The change in approach should be based on evidence and documented where required.

## Exercise 6: Tailoring Review

A small team says that because it has only three engineers, it cannot perform an independent review.

Identify possible responses.

### Suggested answer

Possible responses include arranging a review by another qualified team, using an approved external reviewer, obtaining appropriate organizational support, or selecting another permitted control that achieves the required independence. The team should not assume that small size automatically waives a mandatory independence requirement.

## Exercise 7: Find the Process Gap

A project reduces documentation to save time. During maintenance, a new engineer cannot determine why a critical interface was designed in a particular way.

1. What information may have been lost?
2. What organizational or technical practices could have prevented the problem?
3. How could the organization improve future projects?

### Suggested answer

1. Design rationale, assumptions, trade studies, interface decisions, and change history may have been lost.
2. Maintain proportionate decision records, interface documentation, requirements traceability, and configuration control.
3. Capture the lesson, improve templates or guidance, communicate the change, and evaluate whether it reduces similar problems.

# 13. ASEP-Style Practice Questions

**These are original practice questions for study, not official INCOSE exam questions.** Select the single best answer.

## Question 1

What is the primary purpose of tailoring in systems engineering?

A. Eliminate every process that consumes time.

B. Apply an appropriate level of engineering rigor based on the project context and applicable constraints.

C. Ensure all projects use identical documentation.

D. Transfer all technical decisions to the project manager.

**Answer: B**

**Explanation:** Tailoring adapts processes to project needs while retaining necessary controls and respecting applicable obligations.

## Question 2

Which factor should most directly influence the rigor of safety-related engineering activities?

A. The number of pages in the project plan.

B. The color of the engineering team's diagram templates.

C. The consequences of failure, applicable obligations, and the relevant risk.

D. The preference of the newest team member.

**Answer: C**

**Explanation:** Engineering rigor should reflect risk, consequences, and mandatory requirements.

## Question 3

A project manager removes a required verification activity because the project is behind schedule. What is the best assessment?

A. This is acceptable whenever the project budget is limited.

B. This is always acceptable for iterative projects.

C. The decision must be assessed against applicable obligations, risks, and authorized change procedures; schedule pressure alone is insufficient.

D. Verification is unnecessary if the design review passed.

**Answer: C**

**Explanation:** Tailoring cannot automatically override mandatory requirements or necessary risk controls.

## Question 4

What is the relationship between standardization and tailoring?

A. They are mutually exclusive.

B. Standardization provides common practices, while tailoring adapts them to project context within applicable constraints.

C. Tailoring requires eliminating organizational policies.

D. Standardization means every project must use identical levels of formality.

**Answer: B**

**Explanation:** Organizations can standardize a common baseline and provide controlled options for adapting its application.

## Question 5

A small system controls a potentially hazardous industrial process. Which conclusion is most appropriate?

A. Small system size guarantees low engineering risk.

B. The project can omit safety analysis because it has few components.

C. Process rigor should reflect the system's hazards and consequences, not just its size.

D. Tailoring is prohibited for every industrial system.

**Answer: C**

**Explanation:** A small system may have severe consequences of failure and require extensive controls.

## Question 6

A team is uncertain whether a new communication architecture can satisfy latency requirements. Which action is most appropriate?

A. Assume the architecture will work and postpone all analysis until deployment.

B. Use suitable analysis, prototypes, or experiments to reduce uncertainty before committing to major implementation decisions.

C. Remove the latency requirement.

D. Select the architecture with the most documentation.

**Answer: B**

**Explanation:** Technical investigation can reduce uncertainty and support evidence-based decisions.

## Question 7

Why should a tailoring decision be documented?

A. To guarantee that the project cannot change.

B. To preserve the rationale, risks, approvals, and assumptions supporting the decision.

C. To replace technical verification.

D. To ensure every project uses the same implementation.

**Answer: B**

**Explanation:** Decision records support review, accountability, knowledge transfer, and reassessment.

## Question 8

An organization wants to simplify a review process. What should it consider first?

A. Whether the review's name can be removed from the project plan.

B. What purpose and risk controls the review provides, and whether an alternative preserves necessary functions.

C. Whether other projects have fewer documents.

D. Whether the team can avoid reporting defects.

**Answer: B**

**Explanation:** A process should not be simplified in a way that unintentionally removes a necessary control.

## Question 9

A project initially uses prototypes because of high uncertainty. After testing resolves the major unknowns, the team shifts toward detailed design and controlled implementation. This is an example of:

A. Uncontrolled process failure.

B. Dynamic, evidence-based tailoring.

C. Elimination of systems engineering.

D. Portfolio disposal.

**Answer: B**

**Explanation:** The engineering approach can evolve as evidence and project conditions change.

## Question 10

Which situation most clearly requires reassessing an existing tailoring decision?

A. The project changes the font in an internal presentation.

B. The project expands from an internal prototype to a safety-relevant operational deployment.

C. A team member changes their desk location.

D. A meeting ends five minutes early.

**Answer: B**

**Explanation:** A material change in intended use, risk, or operational context may make the original process approach inadequate.

# 14. Revision Notes

Review these core principles before proceeding:

* Tailoring adapts engineering processes to the system and project context.
* The goal is appropriate rigor, not maximum formality or minimum effort.
* Mandatory legal, contractual, regulatory, and organizational obligations must be respected.
* Complexity includes interfaces, dependencies, stakeholder diversity, and emergent behavior.
* System size alone does not determine risk.
* Higher consequences of failure may justify stronger verification, analysis, configuration control, and independence.
* Technical novelty and uncertainty can justify prototypes and additional analysis.
* Requirements volatility may justify iterative development and more frequent feedback.
* Standardization and tailoring are complementary.
* A tailoring decision should have a rationale and appropriate authorization.
* Compensating controls must preserve the necessary function of the activity being changed.
* Tailoring should be revisited when system scope, risk, intended use, or life-cycle stage changes materially.
* Process simplification is successful only when it improves efficiency without leaving important risks uncontrolled.

## Quick Self-Assessment

1. What is tailoring, and why is it necessary?
2. Why is removing a mandatory activity not automatically acceptable?
3. How should risk influence verification rigor?
4. How can standardization and tailoring coexist?
5. Why does a small system sometimes require extensive engineering controls?
6. What should a tailoring record contain?
7. How can prototypes support tailoring?
8. What is a compensating control?
9. When should a tailoring decision be reconsidered?
10. How can an organization determine whether a simplified process remains effective?

# 15. Further Reading and Official References

Consult current official publications and the editions applicable to your organization and project.

1. **INCOSE Systems Engineering Handbook** — guidance on systems-engineering processes and their application throughout the system life cycle. Official website: https://www.incose.org/

2. **ISO/IEC/IEEE 15288, Systems and software engineering — System life cycle processes** — a key reference for system life-cycle processes and their organizational and project context. Consult the ISO or IEEE catalog for the applicable edition.

3. **ISO 31000, Risk management — Guidelines** — useful guidance for integrating risk considerations into organizational decisions and activities. Official ISO catalog: https://www.iso.org/

4. **ISO 9001, Quality management systems — Requirements** — relevant background on process control, documented information, evaluation, and improvement. Official ISO catalog: https://www.iso.org/

5. **INCOSE Certification Program** — official information about certification routes and examination requirements: https://www.incose.org/certification/

## Final Study Principle

Tailoring is a disciplined engineering decision. Select and adapt processes based on system purpose, complexity, uncertainty, risk, and applicable obligations. Preserve the controls needed to deliver a system that is fit for purpose, while avoiding unnecessary process overhead.
