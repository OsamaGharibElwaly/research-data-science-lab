# Module 03: Strategic Stakeholder Needs and Requirements

## 1. Learning Objectives

By the end of this module, you should be able to:

* Identify stakeholders across organizational and operational boundaries.
* Elicit and analyze strategic stakeholder needs.
* Translate needs into measurable, verifiable requirements.
* Resolve conflicting stakeholder objectives.
* Establish bidirectional traceability and manage requirement changes.
* Evaluate requirements quality and stakeholder satisfaction.

## 2. Stakeholders in Complex Systems

A stakeholder is an individual, group, organization, or other entity with an interest in a system, its outcomes, or its lifecycle.

Stakeholders may include:

* Customers and sponsors.
* System users and operators.
* Maintenance and support personnel.
* Regulators and certification bodies.
* Safety and security authorities.
* Suppliers and subcontractors.
* Business owners.
* Neighboring system owners.
* The public and affected communities.
* Future operators and decommissioning organizations.

Stakeholder identification should account for both direct and indirect effects. An organization purchasing a system may not represent every person who will operate, maintain, or be affected by it.

## 3. Strategic Needs Versus Technical Requirements

A stakeholder need expresses a desired outcome, capability, or condition.

A system requirement specifies a necessary, sufficiently precise condition or capability that the system must satisfy.

Example:

**Stakeholder need:** Hospital staff need to identify potentially dangerous changes in a patient's condition promptly.

**Candidate system requirement:** When specified sensor data meet the approved alarm criteria, the system shall generate and communicate an alarm within the defined response-time limit under the specified operating conditions.

The requirement must be completed with justified thresholds, measurement definitions, operating assumptions, and acceptance criteria. Numerical limits must come from stakeholder agreement, engineering analysis, clinical expertise, or applicable standards—not arbitrary invention.

Needs describe value and intent; requirements provide controlled, assessable obligations.

## 4. Strategic Stakeholder Analysis

A stakeholder analysis should identify:

1. Stakeholder identity and responsibilities.
2. Desired outcomes and concerns.
3. Decision authority.
4. Influence over system success.
5. Operational environment.
6. Conflicting objectives.
7. Communication and engagement needs.
8. Acceptance criteria.
9. Relevant legal, regulatory, and contractual constraints.

Useful artifacts include stakeholder registers, influence-interest maps, responsibility matrices, context diagrams, use cases, and operational scenarios.

Influence-interest classifications help prioritize engagement but should not be used to ignore stakeholders with limited organizational power and substantial exposure to system consequences.

## 5. Needs Elicitation Techniques

### Interviews

Useful for detailed understanding of individual experiences, concerns, and expectations.

### Workshops

Useful for surfacing conflicting needs and building shared understanding across disciplines.

### Observation and contextual inquiry

Useful when actual workflows differ from documented procedures or stakeholder descriptions.

### Surveys

Useful for collecting structured feedback from large stakeholder populations.

### Document and policy analysis

Useful for identifying contractual commitments, regulations, existing processes, and organizational constraints.

### Prototyping

Useful for clarifying interactions and testing assumptions before committing to a design.

### Operational scenarios and use cases

Useful for understanding how the system will be used under normal, exceptional, and degraded conditions.

No single technique is sufficient for every project. An expert combines methods and checks whether the resulting evidence represents the intended stakeholder population.

## 6. From Needs to Requirements

A structured transformation process is:

1. Identify stakeholders and their operating context.
2. Gather needs and supporting evidence.
3. Classify needs by mission, function, performance, safety, security, usability, support, and other relevant concerns.
4. Identify conflicts, ambiguities, assumptions, and missing scenarios.
5. Establish system-level objectives.
6. Develop measurable system requirements.
7. Analyze feasibility, risk, cost, and testability.
8. Allocate requirements to system elements where appropriate.
9. Define verification methods and acceptance criteria.
10. Review and baseline the approved requirements.
11. Maintain traceability and change control.

Requirements must remain connected to the original need or justified constraint so that the organization can explain why each important obligation exists.

## 7. Characteristics of High-Quality Requirements

A well-formed requirement should be:

* **Necessary:** Supports a legitimate need, constraint, or obligation.
* **Unambiguous:** Has one defensible interpretation.
* **Singular:** Expresses a coherent requirement rather than unrelated obligations.
* **Feasible:** Can reasonably be achieved within known constraints.
* **Verifiable:** Can be evaluated using a defined method.
* **Consistent:** Does not contradict other applicable requirements.
* **Traceable:** Has identifiable origins and downstream relationships.
* **Complete:** Contains sufficient information for its intended purpose.
* **Implementation-independent when appropriate:** Specifies what is required without unnecessarily prescribing how to build it.
* **Controlled:** Has an identifier, status, owner or authority, and applicable baseline information.

Not every requirement can remain fully implementation-independent; design constraints may be legitimate when supported by architecture, interfaces, standards, or contractual commitments.

## 8. Requirement Writing Pattern

A useful starting pattern is:

**The system shall + required behavior or condition + measurable threshold or defined reference + applicable operating conditions.**

Weak example:

"The system should be fast and user-friendly."

Improved example:

"The system shall display the requested patient record within the approved response-time limit under the defined workload and network conditions."

The actual response-time threshold, workload, and test conditions must be established and documented before the requirement is baselined.

Avoid vague terms such as:

* Fast.
* Easy.
* Adequate.
* Reliable.
* Flexible.
* User-friendly.
* As soon as possible.
* Sufficiently secure.

These terms require measurable definitions or supporting constraints.

## 9. Requirements Hierarchy and Allocation

A typical hierarchy may include:

1. Mission and business objectives.
2. Stakeholder needs.
3. System requirements.
4. Subsystem requirements.
5. Component requirements.
6. Software and hardware requirements.
7. Interface requirements and implementation constraints.

The hierarchy is not necessarily a simple tree. Requirements can have many-to-many relationships, cross-cutting effects, and dependencies across several system elements.

Allocation must preserve system-level intent and avoid creating inconsistent or unnecessary lower-level requirements.

## 10. Requirements Traceability

Bidirectional traceability links needs, requirements, architecture, implementation, verification, validation, and approved changes.

Forward traceability helps establish that each need is addressed by requirements and realized capabilities.

Backward traceability helps establish that each requirement and implementation obligation has a valid justification.

Traceability supports:

* Impact analysis.
* Change control.
* Verification coverage.
* Validation planning.
* Auditability.
* Defect investigation.
* Acceptance decisions.
* Regulatory evidence.

Traceability is not proof of correctness by itself. A complete traceability matrix can still contain poorly written or technically invalid requirements.

## 11. Conflicting Stakeholder Needs

Stakeholders may disagree about cost, performance, usability, security, availability, maintainability, and delivery dates.

An expert practitioner should:

1. Identify the underlying objectives rather than treating stated preferences as fixed facts.
2. Separate mandatory constraints from negotiable objectives.
3. Clarify assumptions and operating scenarios.
4. Quantify trade-offs where possible.
5. Develop and evaluate alternatives.
6. Record impacts and residual risks.
7. Facilitate a transparent decision.
8. Obtain approval from the appropriate authority.
9. Revisit the decision when assumptions change.

Safety, legal, and regulatory obligations cannot simply be traded away because a stakeholder prefers a cheaper solution.

## 12. Managing Requirements Volatility

Requirements volatility describes the rate and extent of requirements changes during development.

Some changes are legitimate responses to new evidence. Others result from inadequate elicitation, unclear ownership, poor communication, or uncontrolled design decisions.

Useful controls include:

* Establishing a baseline at an appropriate maturity point.
* Assigning requirement ownership.
* Defining change-request procedures.
* Performing impact analysis.
* Tracking reasons for change.
* Updating affected architecture, tests, and documentation.
* Monitoring volatility by requirement category and lifecycle stage.

The objective is not to eliminate every change. It is to make changes deliberate, understood, and affordable.

## 13. Strategic Needs Under Uncertainty

Stakeholder needs can be difficult to define when the operational context or technology is changing.

In such situations, use:

* Explicit assumptions and confidence levels.
* Alternative operational scenarios.
* Prototypes and experiments.
* Sensitivity analysis.
* Progressive refinement.
* Risk-based prioritization.
* Defined decision points for unresolved issues.

Do not convert uncertain assumptions into apparently precise requirements without acknowledging their evidence and limitations.

## 14. Common Failure Patterns

1. Treating the sponsor as the only stakeholder.
2. Confusing proposed solutions with underlying needs.
3. Writing requirements using subjective adjectives.
4. Creating requirements that cannot be verified.
5. Allowing unapproved changes into the baseline.
6. Losing traceability between stakeholder needs and system behavior.
7. Ignoring maintenance, accessibility, security, and retirement needs.
8. Treating stakeholder agreement as proof of technical feasibility.
9. Assuming a traceability matrix guarantees requirements quality.

## 15. Practical Exercise

**Scenario:** A logistics company wants a system to monitor shipments, estimate arrival times, and notify customers about delays.

Develop:

1. A stakeholder register with at least eight stakeholder groups.
2. Five stakeholder needs.
3. Ten candidate system requirements.
4. Verification methods for each requirement.
5. A traceability matrix connecting needs and requirements.
6. Two conflicting stakeholder objectives.
7. A change request and its impact-analysis checklist.
8. A plan for validating the needs with actual users.

For every requirement, identify any missing threshold, operating condition, or acceptance criterion.

## 16. Knowledge Check

**Q1.** How does a stakeholder need differ from a system requirement?

**Answer:** A need expresses a desired outcome or capability; a requirement defines a specific, assessable obligation or condition that supports that outcome.

**Q2.** Why is bidirectional traceability important?

**Answer:** It demonstrates how needs are addressed and why requirements exist, while supporting change impact analysis and verification coverage.

**Q3.** Can a requirement be measurable but still be poor quality?

**Answer:** Yes. It may be unnecessary, infeasible, inconsistent, ambiguous in other respects, or unrelated to a legitimate need.

**Q4.** How should an expert handle conflicting stakeholder priorities?

**Answer:** Identify underlying objectives, establish mandatory constraints, evaluate alternatives, document trade-offs, and secure an authorized decision.

**Q5.** Is requirements volatility always evidence of poor engineering?

**Answer:** No. Some changes are justified by new information or changing conditions. The concern is unmanaged, poorly justified, or unnecessarily costly change.

## 17. Professional Application Evidence

Maintain evidence of your ability to:

* Elicit needs from multiple stakeholder groups.
* Resolve ambiguous or conflicting requirements.
* Improve requirement quality and testability.
* Establish or improve traceability.
* Evaluate the impact of proposed changes.
* Facilitate a decision between competing objectives.
* Improve stakeholder acceptance or reduce rework.

Document your personal contribution, decision authority, methods, evidence, measurable results, and lessons learned.

## 18. Key Takeaways

* Stakeholder needs establish the intended value of a system.
* Requirements translate needs into controlled, assessable obligations.
* High-quality requirements are necessary, clear, feasible, verifiable, and traceable.
* Traceability supports change analysis but does not guarantee correctness.
* Stakeholder conflicts require transparent, evidence-based decisions.
* Requirements changes should be controlled without preventing justified learning.

## 19. Suggested References

* INCOSE, *Systems Engineering Handbook*, applicable edition.
* ISO/IEC/IEEE 15288, *Systems and software engineering — System life cycle processes*.
* ISO/IEC/IEEE 29148, *Systems and software engineering — Life cycle processes — Requirements engineering*.
* Relevant organizational requirements management and stakeholder engagement procedures.
