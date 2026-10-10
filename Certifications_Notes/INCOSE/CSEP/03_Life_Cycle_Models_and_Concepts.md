# 03 — Life Cycle Models and Concepts

## 1. Learning Objectives

By the end of this module, you should be able to:

* Explain the system life cycle and distinguish life-cycle stages from life-cycle models.
* Compare sequential, Vee, incremental, iterative, evolutionary, spiral, concurrent, and agile approaches.
* Select a suitable life-cycle model based on risk, uncertainty, complexity, stakeholder involvement, and regulatory constraints.
* Explain milestones, decision gates, baselines, reviews, and stage transitions.
* Understand how systems engineering activities continue throughout the life cycle.
* Explain the relationship between technical maturity, risk reduction, verification, validation, operation, maintenance, and retirement.
* Apply life-cycle concepts to practical systems-engineering scenarios.

---

## 2. Core Concepts

### 2.1 What Is a System Life Cycle?

A system life cycle is the evolution of a system from its initial identification or conception through development, use, support, and eventual retirement or disposal.

A system does not exist only during design and development. It may spend decades in operation and maintenance, and decisions made during early concept development can determine much of its long-term cost, performance, safety, and supportability.

Typical life-cycle activities include:

1. Identifying a stakeholder problem, opportunity, or mission need.
2. Exploring alternative concepts and feasible solutions.
3. Defining stakeholder needs and system requirements.
4. Defining the architecture and designing the system.
5. Implementing, integrating, verifying, and validating the solution.
6. Transitioning the system into its operational environment.
7. Operating, monitoring, supporting, and maintaining it.
8. Upgrading, replacing, retiring, or disposing of the system.

These activities are not necessarily performed only once or in a strictly linear sequence. Modern systems engineering frequently revisits earlier activities when new evidence, risks, requirements, or operational feedback emerge.

### 2.2 Life-Cycle Stages Versus Life-Cycle Models

These terms are related but different.

**Life-cycle stages** describe meaningful portions of a system's life, such as concept development, development, production, utilization, support, and retirement.

**A life-cycle model** describes how activities, stages, iterations, and decision points are organized and related.

For example, two projects may both contain requirements definition, design, implementation, verification, and validation. One may organize these activities sequentially, while the other performs them in repeated increments.

A stage is therefore not the same thing as a model. A model organizes how work proceeds through the life cycle.

### 2.3 Life Cycle Versus Project Life Cycle

A project is a temporary organizational effort. A system can outlive the project that developed it.

For example, a railway signaling system may require a four-year development project but operate for thirty years. Its system life cycle includes the years of operation, maintenance, upgrades, and eventual decommissioning.

This distinction matters because a project may meet its delivery deadline while producing a system that is expensive to operate or difficult to maintain.

Systems engineering must consider the complete system life cycle, not merely the development project.

### 2.4 Life-Cycle Thinking

Life-cycle thinking evaluates decisions in the context of the system's full existence.

Examples include:

* Selecting a component that costs more initially but lasts longer.
* Designing for maintainability to reduce future repair time.
* Planning software updates before deployment.
* Considering energy consumption during operation.
* Designing interfaces that allow future upgrades.
* Planning safe decommissioning before the system enters service.

The cheapest development option is not automatically the least expensive life-cycle option.

**Life-cycle cost (LCC)** is the total cost associated with a system over a defined life-cycle scope. Depending on the organization and project, it may include acquisition, development, production, deployment, operation, maintenance, upgrades, training, support, and disposal.

A simplified model is:

LCC = Development + Acquisition + Operation + Maintenance + Disposal

This is a conceptual equation, not a universal accounting formula. The cost categories and boundaries must be defined for the particular analysis.

---

## 3. Common Life-Cycle Models

### 3.1 Sequential or Waterfall Model

The sequential model organizes work into largely ordered phases. A phase typically produces defined outputs that support the next phase.

A simplified sequence is:

Requirements → Design → Implementation → Integration → Testing → Deployment

**Advantages**

* Clear phase boundaries and deliverables.
* Straightforward planning and progress reporting.
* Useful when requirements are stable and the solution is well understood.
* Can support formal reviews and contractual milestones.

**Limitations**

* Late discoveries can cause expensive rework.
* Stakeholders may wait a long time before seeing a working solution.
* Uncertain requirements are difficult to manage if they are treated as fixed too early.
* Integration problems may appear late if integration is postponed.

**Suitable contexts**

A relatively stable, well-understood system with clear requirements and a contractual or regulatory need for formal documentation may benefit from a sequential approach.

The model should not be interpreted as a rule that all analysis and testing occur only once. Good sequential projects still perform reviews, risk management, and early technical checks.

### 3.2 The Vee Model

The Vee model emphasizes the relationship between system definition and decomposition on one side, and integration, verification, and validation on the other.

A simplified representation is:

```text
Concept and stakeholder needs       Validation
          \                         /
     System requirements       System verification
            \                   /
       Architecture definition
              \             /
          Detailed design
                \         /
             Implementation
```

The left side progressively defines the problem and solution structure. The bottom represents implementation at an appropriate level. The right side progressively integrates and evaluates the implemented solution.

The exact diagram and activity mapping vary by organization and reference. The important principle is that definition and decomposition activities should be linked to corresponding integration and evaluation activities.

**Key relationships**

* Stakeholder needs inform system requirements.
* System requirements inform architecture and design.
* Architecture and design guide implementation.
* Implementation is followed by integration and verification at appropriate levels.
* The complete system is validated against stakeholder needs and intended use.

Verification planning should begin while requirements and design decisions are being made, rather than waiting until the system is complete.

For example, when defining a temperature-monitoring device, engineers should establish how they will demonstrate measurement accuracy before the device is built.

**Advantages**

* Strong traceability between requirements, design, and testing.
* Encourages early test planning.
* Supports complex systems requiring evidence and formal reviews.
* Helps identify missing requirements and untestable statements.

**Limitations**

* Can be misunderstood as strictly sequential.
* May become documentation-heavy if applied without tailoring.
* Late changes can still cause rework.
* Does not eliminate the need for iteration.

The Vee model is especially useful for organizing engineering relationships, but it should not be treated as a prohibition against iterative development.

### 3.3 Incremental Development

Incremental development delivers a system in multiple usable or evaluable portions.

Each increment adds capability to an existing or evolving solution.

Example: a hospital information system might be delivered as follows:

* Increment 1: patient registration.
* Increment 2: appointment management.
* Increment 3: laboratory integration.
* Increment 4: reporting and analytics.

**Advantages**

* Stakeholders receive useful capability earlier.
* Feedback can influence later increments.
* Technical and delivery risks can be exposed progressively.
* Funding and deployment can sometimes be distributed over time.

**Limitations**

* Architecture must support planned growth.
* Interfaces between increments require careful management.
* Early increments may not provide the full intended capability.
* Poorly planned increments can produce integration debt or inconsistent behavior.

An increment is a portion of capability delivered over time. It is not necessarily the same as an iteration.

### 3.4 Iterative Development

Iterative development repeatedly revisits a solution to improve its maturity, correctness, performance, or suitability.

For example, a monitoring algorithm may be developed through repeated cycles of modeling, testing, error analysis, and refinement.

Each cycle uses new information to improve the existing solution.

**Advantages**

* Supports learning and refinement.
* Allows assumptions to be tested.
* Helps address uncertainty and complex technical problems.
* Encourages feedback from analysis, simulation, prototypes, and users.

**Limitations**

* Requires disciplined configuration and change management.
* May continue indefinitely without acceptance criteria.
* Can increase cost if iteration goals are unclear.
* Requires stakeholders to evaluate evolving outputs.

### 3.5 Incremental Versus Iterative Development

The two approaches are often combined, but they describe different ideas.

| Aspect           | Incremental                                   | Iterative                                            |
| ---------------- | --------------------------------------------- | ---------------------------------------------------- |
| Main idea        | Add capability in portions                    | Refine or improve a solution through repeated cycles |
| Typical question | What capability should be delivered next?     | What needs to be learned or improved?                |
| Output           | Additional functionality or system capability | A more mature or improved version                    |
| Example          | Add remote alerts to a monitoring platform    | Improve alert accuracy over several test cycles      |

A project can be both incremental and iterative. For example, each release can add a new feature while existing features are repeatedly improved.

### 3.6 Evolutionary Development

Evolutionary development allows the system solution to emerge progressively as understanding improves.

It is especially relevant when the problem is understood better than the final solution.

An early prototype may reveal new user needs, technical limitations, or unexpected interactions. The design evolves using that evidence.

Evolutionary development does not mean uncontrolled change. It still requires:

* A defined mission and intended outcomes.
* Appropriate architectural direction.
* Risk and configuration management.
* Acceptance criteria for increments or releases.
* Controlled evaluation of stakeholder feedback.

It is useful when uncertainty is high and learning is necessary before a final solution can be fully defined.

### 3.7 Spiral and Risk-Driven Development

A spiral model organizes development around repeated cycles that emphasize identifying and reducing important risks.

A simplified cycle may include:

1. Establish objectives, alternatives, and constraints.
2. Identify and analyze major risks.
3. Develop or evaluate a prototype, model, or solution.
4. Review results and plan the next cycle.

The key feature is not simply repetition. It is the deliberate use of risk analysis to determine what should be addressed next.

Example: before committing to mass production of a new autonomous inspection robot, a team might test obstacle detection, battery performance, and safe-stop behavior because these uncertainties could threaten feasibility or safety.

**Advantages**

* Focuses attention on the most consequential uncertainties.
* Supports prototyping and experimentation.
* Helps prevent premature commitment to an infeasible solution.

**Limitations**

* Requires credible risk analysis and experienced decision-makers.
* Can be expensive if cycles are poorly controlled.
* May be difficult to manage when risk evaluation is informal.
* Requires clear decisions at the end of each cycle.

### 3.8 Concurrent Engineering

Concurrent engineering allows related activities to overlap rather than waiting for one activity to finish completely before another begins.

For example, manufacturing engineers may evaluate producibility while system architects are still refining the design.

**Advantages**

* Shortens schedules.
* Identifies downstream constraints earlier.
* Improves communication between engineering disciplines.
* Helps expose integration and support issues before design completion.

**Limitations**

* Changes can affect several teams at once.
* Requires coordinated information, interface, and configuration management.
* Incomplete information may create rework.

Concurrent engineering does not mean every task can proceed independently. Dependencies and decision authority must remain clear.

### 3.9 Agile and Adaptive Approaches

Agile approaches emphasize short feedback cycles, collaboration, adaptive planning, and delivery of value. They are often applied to software-intensive parts of a system.

Common practices include:

* Short development iterations.
* Prioritized work backlogs.
* Frequent demonstrations.
* Automated testing and integration.
* Regular stakeholder feedback.
* Retrospectives and continuous improvement.

Agile methods can support systems engineering, but system-level constraints remain important. Hardware lead times, safety approvals, interfaces, cybersecurity, and regulatory evidence may not fit entirely within short software iterations.

For complex cyber-physical systems, a hybrid approach may combine agile software development with formal system architecture, interface control, safety engineering, and verification planning.

### 3.10 Hybrid Life-Cycle Models

Many real projects combine models.

Example: an aircraft subsystem may use:

* A staged, review-driven system-level process.
* Iterative simulation and design optimization.
* Incremental software releases.
* Concurrent manufacturing planning.
* Formal verification and validation.

A hybrid model is appropriate when it deliberately addresses different parts of the problem. It becomes harmful when teams use incompatible assumptions about requirements, baselines, change control, and acceptance.

---

## 4. Selecting a Life-Cycle Model

No single life-cycle model is universally best.

Model selection should consider the characteristics of the system, stakeholders, environment, and organization.

### 4.1 Requirements Stability

* Stable requirements may support more sequential planning.
* Uncertain requirements often benefit from iterative or evolutionary development.
* Safety-critical requirements may require formal baselines and rigorous change assessment even when development is iterative.

### 4.2 Technical and Operational Risk

High technical uncertainty may justify prototypes, simulations, experiments, or risk-driven cycles before major investment.

High operational risk may require formal hazard analysis, staged integration, independent review, and strong verification evidence.

### 4.3 System Complexity and Interfaces

Systems with many subsystems and organizations need clear interface definitions, integration planning, configuration management, and cross-team coordination.

A purely informal process is unlikely to be adequate for a complex system with tightly coupled components.

### 4.4 Stakeholder Availability

Frequent stakeholder participation supports iterative and incremental approaches.

If stakeholder access is limited, teams may need stronger upfront discovery, documented decisions, representative user research, and planned review points.

### 4.5 Regulatory and Contractual Constraints

The life-cycle model must support required evidence, approvals, safety obligations, contractual deliverables, and acceptance criteria.

Agile or evolutionary development does not remove legal or regulatory obligations.

### 4.6 Schedule, Cost, and Supply-Chain Constraints

Long-lead hardware, scarce components, external approvals, or manufacturing constraints can limit how quickly increments are delivered.

The model must reflect actual technical dependencies, not merely the desired release schedule.

### 4.7 Model Selection Matrix

| Project characteristic                   | Potentially useful approach              | Important caution                               |
| ---------------------------------------- | ---------------------------------------- | ----------------------------------------------- |
| Stable requirements and known technology | Sequential or Vee-oriented planning      | Still plan for change and test early            |
| High requirement uncertainty             | Iterative or evolutionary                | Define boundaries and acceptance criteria       |
| Capability can be delivered in portions  | Incremental                              | Preserve architecture and interface integrity   |
| Major technical uncertainties            | Spiral or risk-driven cycles             | Prioritize risks using credible evidence        |
| Software features need rapid feedback    | Agile/adaptive                           | Maintain system-level controls                  |
| Many parallel engineering disciplines    | Concurrent or hybrid                     | Coordinate baselines and dependencies           |
| High assurance or regulatory burden      | Vee-oriented and formal review structure | Tailor documentation without weakening evidence |

These are decision aids, not absolute rules. A Vee-oriented project can be iterative; an agile project can contain formal gates; and a sequential project can use risk-driven prototypes.

---

## 5. Milestones, Reviews, Gates, and Baselines

### 5.1 Milestones

A milestone is a significant point used to assess progress, make a decision, or coordinate work.

Examples include:

* Concept selected.
* Requirements baseline approved.
* Architecture review completed.
* Prototype evaluated.
* Integration completed.
* System accepted for operation.

A milestone is not necessarily a deliverable. It may mark a decision or achievement.

### 5.2 Decision Gates

A decision gate is a formal point at which authorized decision-makers determine whether the project should proceed, pause, redirect, or stop.

A gate should use defined criteria and evidence.

Possible questions include:

* Is the concept technically feasible?
* Are major risks understood and acceptably controlled?
* Are stakeholder needs sufficiently understood?
* Is the architecture mature enough for the next investment?
* Are safety, cost, schedule, and resource assumptions credible?

A gate is not valuable merely because a meeting occurred. It should support a real decision.

### 5.3 Technical Reviews

Reviews evaluate the adequacy, maturity, or consistency of engineering outputs.

Examples include requirements reviews, architecture reviews, preliminary design reviews, critical design reviews, test readiness reviews, and operational readiness reviews. Exact review names and their placement vary by organization and contract.

Reviews should identify issues, record decisions, assign actions, and verify closure of important findings.

### 5.4 Baselines

A baseline is an approved reference configuration or set of information used to control and evaluate changes.

Examples include:

* Requirements baseline.
* Architecture baseline.
* Design baseline.
* Product or system configuration baseline.
* Schedule or performance baseline.

A baseline does not mean that change is forbidden. It means changes are evaluated, authorized, documented, and reflected in controlled information.

### 5.5 Configuration Management

Configuration management maintains consistency between approved information and the actual system as it evolves.

It commonly includes:

* Configuration identification.
* Change control.
* Configuration status accounting.
* Configuration verification or audit activities.

It helps ensure that engineers, testers, suppliers, and operators are working with the correct versions of requirements, designs, software, and hardware definitions.

---

## 6. Technical Maturity, Prototypes, and Evidence

### 6.1 Prototypes

A prototype is a model or implementation created to explore, evaluate, or demonstrate selected characteristics of a proposed solution.

Prototypes can investigate:

* Technical feasibility.
* User interaction.
* Performance.
* Interfaces.
* Manufacturability.
* Safety concepts.
* Maintainability.

A prototype does not automatically demonstrate that the final system is fit for operation. Its representativeness, limitations, test conditions, and intended use must be understood.

### 6.2 Simulation and Modeling

Modeling and simulation can reduce uncertainty before physical implementation.

Examples include:

* Network simulations to test topology and capacity.
* Thermal models to evaluate component cooling.
* Discrete-event simulations for warehouse throughput.
* Digital models to evaluate system behavior.
* Software simulations to test fault scenarios.

Models depend on assumptions. Their credibility should be appropriate to the decision being made.

### 6.3 Technology Maturity

A technically promising component may still be unsuitable for production if it has not been sufficiently demonstrated under representative conditions.

Technology maturity assessments consider evidence such as laboratory results, prototype tests, environmental tests, integration evidence, and operational demonstrations.

A project should not treat a successful isolated experiment as proof that a technology will work reliably in the complete system.

### 6.4 Risk Reduction Before Commitment

A useful principle is to reduce the most consequential uncertainties before making expensive or difficult-to-reverse commitments.

For example, before building a large data center, the team may validate power capacity, cooling, network architecture, resilience, physical space, and service-provider assumptions.

The appropriate level of evidence depends on risk and the consequences of failure.

---

## 7. Operation, Maintenance, Upgrades, and Retirement

### 7.1 Operation

Operation includes using the system to deliver its intended services or mission outcomes.

Engineering concerns may include:

* Performance monitoring.
* Availability and reliability.
* User feedback.
* Operational procedures.
* Incident response.
* Environmental and safety constraints.

Operational evidence should inform future engineering decisions.

### 7.2 Maintenance

Maintenance preserves or restores the system's ability to perform its intended functions.

It may include preventive maintenance, corrective maintenance, condition-based maintenance, software updates, component replacement, and recalibration.

Maintainability is influenced by design choices such as access to components, diagnostics, modularity, spare-part availability, and repair procedures.

### 7.3 Upgrades and Modernization

Upgrades introduce new capability or improve existing performance.

They may trigger renewed requirements analysis, impact assessment, design changes, verification, validation, training, and transition planning.

Even a small software change can affect safety, cybersecurity, interfaces, or operational procedures.

### 7.4 Retirement and Disposal

Retirement is a planned transition out of service. Disposal addresses the final handling of the system and its components according to applicable technical, environmental, legal, and security requirements.

Considerations may include:

* Data sanitization and privacy.
* Hazardous materials.
* Asset recovery and recycling.
* Safe removal from service.
* Transfer of remaining responsibilities.
* Archiving required records.
* Replacement or continuity of service.

Retirement should be planned early enough to avoid creating avoidable cost, safety, or environmental problems.

---

## 8. Practical Case Study: Smart Hospital Monitoring System

### Scenario

A hospital wants a monitoring system that collects patient measurements, alerts clinicians to concerning values, and stores data for review. The system includes wearable sensors, mobile devices, a backend service, a dashboard, and interfaces to hospital systems.

### Step 1: Identify Uncertainty

The team identifies uncertainties involving sensor accuracy, connectivity, alert thresholds, usability, battery life, privacy, integration, and operational workflow.

### Step 2: Select an Approach

A hybrid life-cycle model is selected:

* System-level requirements and architecture receive formal review.
* Sensor performance is evaluated through prototypes and experiments.
* Software capabilities are delivered incrementally.
* Usability is refined iteratively with representative users.
* Safety-related behavior is verified using predefined test evidence.
* Deployment proceeds through controlled stages.

### Step 3: Define Increments

* Increment 1: collect and display measurements.
* Increment 2: provide alerts and acknowledgment.
* Increment 3: add hospital-system integration.
* Increment 4: provide operational analytics and maintenance diagnostics.

Each increment has acceptance criteria and integration plans.

### Step 4: Manage Baselines

The team controls approved requirements, interface definitions, software versions, and test records. A proposed alert-rule change receives impact analysis before approval.

### Step 5: Validate the Complete System

The team evaluates whether the integrated solution supports the intended clinical workflow, not merely whether individual components pass their technical tests.

### Step 6: Plan Support and Retirement

The design includes battery replacement, sensor calibration, software patching, access control, data retention, and secure decommissioning.

### Lessons

* The complete life cycle matters more than the development phase alone.
* Incremental delivery and iterative refinement can coexist.
* Risk reduction should precede high-cost commitments.
* Verification and validation address different questions.
* Hybrid models need disciplined interfaces and configuration management.

---

## 9. Exercises

### Exercise 1: Select a Model

A small team is developing a reporting application. User requirements are likely to change after demonstrations, and features can be released independently.

**Question:** Which approach is potentially suitable, and why?

**Suggested answer:** An iterative and incremental approach, potentially using agile practices, is suitable because the team can gather feedback frequently and release features in useful portions. The team must still manage interfaces, quality, security, and release acceptance.

### Exercise 2: Stable Requirements

A supplier is producing a well-understood component against a stable specification and a formal acceptance contract.

**Question:** Which model characteristics may be useful?

**Suggested answer:** A sequential or Vee-oriented approach may provide clear deliverables, traceability, review points, and acceptance evidence. Early verification planning remains valuable.

### Exercise 3: High Technical Uncertainty

A company proposes a new energy-storage technology, but its performance and safety under operating conditions are uncertain.

**Question:** What should the team do before making a major production commitment?

**Suggested answer:** Use risk-driven investigation, prototypes, modeling, and representative testing to address critical feasibility and safety uncertainties. Establish decision criteria before committing to expensive production infrastructure.

### Exercise 4: Increment Versus Iteration

A project releases a basic dashboard, adds export functionality in the next release, and repeatedly improves dashboard response time.

**Question:** Identify the incremental and iterative activities.

**Suggested answer:** Adding export functionality is incremental delivery. Repeatedly improving response time is iterative refinement. The project can do both.

### Exercise 5: Life-Cycle Cost

A component has a higher purchase price but requires fewer repairs and less energy over ten years.

**Question:** Why should the decision not be based on purchase price alone?

**Suggested answer:** Purchase price represents only one part of life-cycle cost. Energy use, maintenance, downtime, replacement, and disposal may change the total cost and operational value.

### Exercise 6: Change After Baseline

A stakeholder requests a new interface after the design baseline is approved.

**Question:** Should the team automatically reject the change?

**Suggested answer:** No. The team should record the change request, assess impacts on requirements, design, safety, cost, schedule, verification, and interfaces, and then obtain the required authorization.

### Exercise 7: Retirement Planning

A monitoring platform stores sensitive operational records and uses components that may become obsolete.

**Question:** Name four retirement considerations.

**Suggested answer:** Secure data sanitization, records retention, replacement or migration planning, component recycling or disposal, service continuity, and removal of obsolete access credentials are relevant considerations.

---

## 10. CSEP-Style Practice Questions

These are original practice questions for study. They are not official INCOSE exam questions.

### Question 1

What is the primary distinction between a life-cycle stage and a life-cycle model?

A. A stage is always shorter than a model.
B. A stage describes a portion of system life; a model organizes life-cycle activities and their relationships.
C. A model applies only to software.
D. A stage is the same as a project milestone.

**Correct answer: B.**

**Explanation:** Stages describe portions of the system's life, while a model describes how activities, stages, iterations, and decision points are organized.

### Question 2

A project has uncertain user needs and can release useful functionality in separate portions. Which approach is most directly aligned with these conditions?

A. Iterative and incremental development
B. A single irreversible design commitment
C. Deferring all user feedback until retirement
D. Avoiding prototypes

**Correct answer: A.**

**Explanation:** Iteration supports learning and refinement; increments provide capability in portions.

### Question 3

What is a central characteristic of a risk-driven spiral approach?

A. It prohibits prototyping.
B. It requires every activity to finish before risk analysis begins.
C. It organizes cycles around identifying and reducing important risks.
D. It eliminates the need for stakeholder decisions.

**Correct answer: C.**

**Explanation:** Risk analysis influences the focus of each cycle and helps determine what evidence is needed before proceeding.

### Question 4

Which statement about the Vee model is most accurate?

A. It requires all requirements to remain unchanged forever.
B. It connects system definition and decomposition with integration and evaluation activities.
C. It is exclusively a software coding method.
D. It removes the need for validation.

**Correct answer: B.**

**Explanation:** The Vee model emphasizes relationships between definition activities and corresponding verification, integration, and validation activities.

### Question 5

A team adds new functionality in each release and also repeatedly improves the reliability of existing features. This is best described as:

A. Only sequential development
B. Incremental development combined with iterative refinement
C. Retirement without maintenance
D. A process without a life cycle

**Correct answer: B.**

**Explanation:** Adding capabilities is incremental; repeated improvement is iterative.

### Question 6

What is the main purpose of a decision gate?

A. To ensure that no change can ever occur.
B. To create a meeting without requiring evidence.
C. To support an authorized decision based on defined criteria and evidence.
D. To replace all technical reviews.

**Correct answer: C.**

**Explanation:** A gate supports a proceed, pause, redirect, or stop decision.

### Question 7

Why is configuration management important after a baseline has been approved?

A. Because all change requests must be rejected.
B. Because it controls and records changes so approved information remains consistent with the evolving system.
C. Because it removes the need for testing.
D. Because it prevents operational feedback.

**Correct answer: B.**

**Explanation:** Baselines are controlled reference points, not permanent prohibitions against change.

### Question 8

A prototype performs well in a laboratory but has not been tested under representative environmental conditions. What is the best conclusion?

A. Production readiness is proven.
B. No additional evidence is needed.
C. The prototype provides some evidence, but its representativeness and limitations must be assessed.
D. The system has passed operational validation.

**Correct answer: C.**

**Explanation:** Evidence must be appropriate to the claim being made. A laboratory result does not automatically prove performance in the intended environment.

### Question 9

Why should retirement be considered during early system development?

A. Retirement always occurs immediately after implementation.
B. Early decisions can influence data removal, environmental impact, replacement, supportability, and disposal costs.
C. Retirement planning replaces operational planning.
D. It eliminates maintenance requirements.

**Correct answer: B.**

**Explanation:** Life-cycle decisions can create long-term obligations that are cheaper and safer to address early.

### Question 10

Which is the best approach for a complex system with hardware lead times, software uncertainty, formal safety requirements, and frequent stakeholder feedback?

A. Apply an unmodified software-only agile method to every activity.
B. Ignore the hardware schedule until software is complete.
C. Use a tailored hybrid approach with coordinated system-level controls and iterative development where appropriate.
D. Avoid all formal baselines.

**Correct answer: C.**

**Explanation:** Complex systems often need a hybrid model that accommodates different technical, operational, and assurance constraints.

---

## 11. Revision Notes

* The system life cycle extends beyond development into operation, support, and retirement.
* A life-cycle stage is a portion of system life; a life-cycle model organizes activities and relationships.
* Sequential approaches suit relatively stable, well-understood work but still need risk management and testing.
* The Vee model links definition and decomposition with integration, verification, and validation.
* Incremental development adds capability in portions.
* Iterative development improves or refines a solution through repeated cycles.
* Evolutionary development allows the solution to emerge as understanding improves.
* Spiral approaches organize cycles around risk reduction.
* Concurrent engineering overlaps related activities to improve coordination and schedule.
* Agile methods support frequent feedback and adaptive planning but do not remove system-level obligations.
* Hybrid models should be deliberately tailored and consistently managed.
* Milestones mark significant events; decision gates support authorized decisions.
* Baselines enable controlled change rather than forbidding change.
* Prototypes and simulations reduce uncertainty, but evidence must be appropriate to the intended claim.
* Life-cycle cost includes more than initial acquisition.
* Operation, maintenance, upgrades, and retirement should influence early engineering decisions.

---

## 12. References and Further Reading

Use the current edition and any syllabus-specific references identified by INCOSE for the certification you are pursuing.

1. **INCOSE Systems Engineering Handbook** — life-cycle concepts, life-cycle models, technical processes, and systems-engineering application.
2. **ISO/IEC/IEEE 15288, Systems and software engineering — System life cycle processes** — international reference for system life-cycle process frameworks.
3. **INCOSE Certification Program** — official certification requirements, application guidance, and current examination information: https://www.incose.org/certification
4. **NASA Systems Engineering Handbook (NASA/SP-2016-6105 Rev 2)** — practical systems-engineering guidance, reviews, technical planning, and life-cycle application: https://www.nasa.gov/reference/systems-engineering-handbook/
5. **NASA Systems Engineering resources** — supporting guidance and technical references: https://www.nasa.gov/

### Study Guidance

Read the relevant life-cycle sections of the current INCOSE Handbook and compare its terminology with ISO/IEC/IEEE 15288. Use the current certification exam guidance to establish scope; do not assume that every example or model in this document has equal examination emphasis.
