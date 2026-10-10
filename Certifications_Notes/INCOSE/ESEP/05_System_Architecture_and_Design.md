# Module 05: System Architecture and Design

## 1. Learning Objectives

By the end of this module, you should be able to:

* Develop and evaluate system architectures against stakeholder needs and system requirements.
* Compare logical, functional, and physical architectures.
* Allocate system functions and requirements to architectural elements.
* Define interfaces, architectural constraints, and design decisions.
* Conduct architecture trade studies and assess system-level consequences.
* Manage architecture evolution, technical debt, and architectural risk.

## 2. Introduction to System Architecture

System architecture defines the fundamental organization of a system, including its elements, relationships, interfaces, constraints, and guiding design principles.

Architecture establishes how the system will achieve its intended capabilities while satisfying technical, operational, business, safety, and lifecycle requirements.

Architecture is not simply a component diagram. It includes the rationale behind structural decisions and the constraints that govern implementation and evolution.

A good architecture should provide a defensible relationship between:

* Stakeholder needs.
* System requirements.
* System functions.
* Physical and logical elements.
* Interfaces and dependencies.
* Operational scenarios.
* Verification and validation.
* Lifecycle cost and risk.

## 3. Functional, Logical, and Physical Architecture

### 3.1 Functional Architecture

Functional architecture describes what the system must do, independently of the specific physical elements that implement the functions.

Typical activities include:

* Identifying system functions.
* Decomposing high-level functions.
* Defining inputs and outputs.
* Establishing functional sequences.
* Identifying control and data flows.
* Defining functional interfaces.

Example: A shipment monitoring system may need to acquire location data, validate observations, estimate arrival time, detect delays, notify users, and record events.

### 3.2 Logical Architecture

Logical architecture organizes functions into logical elements and defines their relationships without necessarily committing to particular physical implementations.

For example, shipment monitoring may be organized into tracking, analytics, notification, and data management services.

Logical architecture helps manage complexity before making detailed technology decisions.

### 3.3 Physical Architecture

Physical architecture maps system responsibilities to actual or proposed implementation elements.

These may include:

* Hardware components.
* Software services.
* Embedded controllers.
* Networks and communication equipment.
* Databases and storage.
* Human operators.
* External platforms.

A physical architecture must account for resource constraints, interfaces, deployment environments, reliability, security, maintainability, and cost.

## 4. Architecture Development Process

A structured architecture development process includes:

1. Establish the system context and boundary.
2. Review stakeholder needs and system requirements.
3. Identify operational scenarios and critical use cases.
4. Identify system functions and their dependencies.
5. Develop candidate architectural alternatives.
6. Define interfaces and allocate requirements.
7. Analyze quality attributes and constraints.
8. Evaluate alternatives through trade studies.
9. Select and document the preferred architecture.
10. Verify architectural consistency and feasibility.
11. Validate the architecture against stakeholder needs.
12. Maintain architectural traceability and change control.

Architecture development is iterative. New analysis, prototypes, integration results, or stakeholder feedback may require earlier decisions to be revisited.

## 5. Architecture Drivers

Architecture drivers are the needs, constraints, and technical characteristics that significantly influence architectural decisions.

Common drivers include:

* Performance and latency.
* Availability and reliability.
* Safety and security.
* Scalability.
* Interoperability.
* Maintainability.
* Modifiability.
* Environmental conditions.
* Regulatory compliance.
* Cost and schedule.
* Supplier capabilities.
* Operational constraints.

Architecture drivers should be prioritized because not all attributes can be optimized simultaneously.

For example, distributing a system across multiple services may improve independent scalability but introduce network latency, operational complexity, and additional failure modes.

## 6. Quality Attribute Scenarios

Quality attributes should be expressed in terms of observable, assessable behavior.

A quality attribute scenario commonly identifies:

* **Stimulus:** The event that occurs.
* **Source:** The origin of the event.
* **Environment:** The conditions under which it occurs.
* **Response:** The system's expected behavior.
* **Response measure:** The criterion used to evaluate the response.

Example:

During a specified peak workload, when a tracking update arrives, the platform shall process and publish the update within an agreed response-time limit.

The numerical threshold and workload must be established through stakeholder agreement, operational evidence, and technical analysis.

Quality attribute scenarios help turn vague goals such as "high performance" or "easy maintenance" into assessable architecture drivers.

## 7. Architecture Patterns and Styles

Architecture patterns provide reusable approaches to recurring design problems.

Examples include:

* Layered architecture.
* Client-server architecture.
* Event-driven architecture.
* Service-oriented architecture.
* Microservices architecture.
* Distributed control architecture.
* Redundant fault-tolerant architecture.
* Centralized data processing architecture.
* Edge-cloud architecture.

No pattern is universally superior.

A microservices architecture, for example, may support independent deployment and scaling but also introduce distributed tracing, service discovery, network failure, data consistency, and deployment management challenges.

The architect should select patterns based on requirements, system boundaries, team capabilities, operational maturity, and lifecycle constraints.

## 8. Interface Architecture

Interfaces define how system elements interact.

Interface specifications may cover:

* Physical and mechanical connections.
* Electrical characteristics.
* Communication protocols.
* Data structures and semantics.
* Timing and synchronization.
* Units of measurement.
* Authentication and authorization.
* Error handling and recovery.
* Capacity and resource limits.
* Version compatibility.

Poorly defined interfaces frequently produce integration delays and defects.

An interface control document or equivalent controlled specification should identify interface ownership, assumptions, constraints, versioning, and verification expectations.

Interfaces must be reviewed when changes occur in connected elements or their operating environments.

## 9. Architecture Trade Studies

Trade studies compare alternatives against explicit criteria.

A typical process is:

1. Define the decision and required outcome.
2. Identify feasible alternatives.
3. Establish mandatory constraints.
4. Select evaluation criteria.
5. Define criteria weights where appropriate.
6. Collect evidence and estimates.
7. Assess uncertainty and sensitivity.
8. Compare alternatives.
9. Document the recommendation and rationale.
10. Obtain the required decision approval.

Potential criteria include performance, cost, risk, reliability, scalability, maintainability, safety, security, and time to deploy.

A weighted scoring model can help structure the comparison, but it does not eliminate judgment. Scores, weights, and assumptions must be justified.

Mandatory safety or regulatory requirements should not be treated as ordinary criteria that can be offset by a high score elsewhere.

## 10. Architecture Risk Analysis

Architecture risk arises when structural decisions may prevent the system from meeting its requirements or operating effectively.

Examples include:

* An unproven technology on a critical path.
* A single point of failure.
* Unbounded network latency.
* A supplier-controlled interface.
* Inadequate fault isolation.
* A data model that cannot support future needs.
* Excessive coupling between components.
* An architecture that cannot be tested adequately.

Useful methods include:

* Prototyping.
* Simulation.
* Interface experiments.
* Sensitivity analysis.
* Failure mode and effects analysis.
* Fault-tree analysis.
* Reliability analysis.
* Architecture reviews.
* Early integration tests.

Risk reduction should prioritize assumptions that are both uncertain and consequential.

## 11. Architecture Documentation and Governance

Architecture documentation should communicate the system's structure, behavior, constraints, decisions, and rationale.

Typical artifacts include:

* System context diagrams.
* Functional decomposition.
* Logical and physical architecture views.
* Interface specifications.
* Deployment diagrams.
* Data-flow diagrams.
* Architecture decision records.
* Trade-study reports.
* Requirements allocation matrices.
* Risk and assumption registers.
* Architecture verification evidence.

Architecture decision records should document the problem, alternatives considered, decision, rationale, consequences, assumptions, and conditions that might require reconsideration.

The depth of documentation should match the system's complexity, risk, regulatory environment, and stakeholder needs.

## 12. Architecture Evolution and Technical Debt

Architecture evolves as new requirements, operating conditions, technologies, and lessons emerge.

Technical debt occurs when a design compromise creates future costs or constraints.

Examples include excessive coupling, undocumented interfaces, duplicated logic, outdated dependencies, and insufficient observability.

Technical debt is not automatically unacceptable. A deliberate compromise may be appropriate when its cost, risk, and repayment strategy are understood.

An expert architect monitors whether accumulated compromises are undermining system performance, security, reliability, maintainability, or future change.

## 13. Common Failure Patterns

1. Selecting a technology before defining the architecture drivers.
2. Confusing architecture diagrams with a complete architecture description.
3. Optimizing one quality attribute while ignoring others.
4. Ignoring interfaces until integration.
5. Failing to document architectural decisions.
6. Choosing fashionable patterns without assessing operational complexity.
7. Neglecting fault containment and recovery.
8. Allowing architectural changes without impact analysis.
9. Treating weighted scoring as a substitute for engineering judgment.

## 14. Practical Exercise

**Scenario:** A logistics organization is building a shipment-monitoring platform with GPS devices, mobile applications, a cloud backend, analytics, and a customer portal.

Develop:

1. A system context and boundary description.
2. A functional architecture with at least eight functions.
3. A logical architecture identifying major elements.
4. A physical architecture proposal.
5. Five architecture drivers with measurable scenarios.
6. Three candidate architecture alternatives.
7. A trade-study matrix.
8. An interface specification outline.
9. A risk assessment covering availability, scalability, security, and maintainability.
10. Three architecture decision records.

Identify the evidence needed before committing to each major architectural decision.

## 15. Knowledge Check

**Q1.** What is the difference between functional and physical architecture?

**Answer:** Functional architecture describes what the system does; physical architecture describes the elements that implement the required behavior.

**Q2.** Why should architecture drivers be prioritized?

**Answer:** Because architectural decisions involve trade-offs, and the most consequential requirements and constraints must guide the design.

**Q3.** Why is an interface specification important?

**Answer:** It establishes controlled expectations for interactions and reduces ambiguity, incompatibility, and integration risk.

**Q4.** What is the danger of selecting an architecture pattern solely because it is popular?

**Answer:** The pattern may introduce complexity or fail to satisfy the system's actual requirements and operating constraints.

**Q5.** What should an architecture decision record contain?

**Answer:** The decision context, alternatives, selected option, rationale, consequences, assumptions, and conditions that may require reconsideration.

## 16. Professional Application Evidence

Maintain evidence of your ability to:

* Develop or significantly influence a system architecture.
* Resolve a difficult architectural trade-off.
* Establish or improve interface governance.
* Reduce a major architectural risk.
* Improve reliability, scalability, or maintainability.
* Guide architecture decisions across multidisciplinary teams.
* Improve organizational architecture practices.

For each example, document the context, your responsibility, alternatives evaluated, evidence, decision rationale, measurable outcomes, and lessons learned.

## 17. Key Takeaways

* Architecture connects requirements to system structure and behavior.
* Functional, logical, and physical views serve different purposes.
* Quality attributes must be measurable and evaluated together.
* Interfaces are critical architectural elements.
* Trade studies require transparent criteria and justified assumptions.
* Architecture risk should be reduced early.
* Architecture decisions need traceability, governance, and controlled evolution.

## 18. Suggested References

* INCOSE, *Systems Engineering Handbook*, applicable edition.
* ISO/IEC/IEEE 42010, *Systems and software engineering — Architecture description*.
* ISO/IEC/IEEE 15288, *Systems and software engineering — System life cycle processes*.
* Relevant organizational architecture and interface management standards.
