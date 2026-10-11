# Requirements Analysis and Design Definition

## 1. Learning Objectives

By the end of this module, you should be able to:

* Distinguish requirements from designs.
* Classify business, stakeholder, solution, and transition requirements.
* Specify and model requirements.
* Verify, validate, prioritize, and organize requirements.
* Explain requirements traceability and reuse.
* Understand solution design alternatives.
* Assess requirement quality and resolve ambiguity.
* Apply requirements analysis to a practical case.

## 2. Introduction

Requirements Analysis and Design Definition focuses on specifying and modeling requirements and designs, checking their quality, and ensuring that they support stakeholder needs and business objectives.

A requirement describes a need or condition that must be satisfied.

A design describes a possible representation or approach for satisfying a need.

For example:

* Requirement: Customers must be able to track the status of their orders.
* Design: A dashboard displays order status, expected delivery date, and tracking history.

The requirement expresses the need. The design proposes how the solution may satisfy it.

A requirement should not unnecessarily prescribe a specific implementation unless that implementation is itself a genuine constraint.

## 3. Requirements Classification

### 3.1 Business Requirements

Business requirements describe organizational goals, objectives, and outcomes.

Example:

"The organization must reduce order-processing costs by 15% within twelve months."

### 3.2 Stakeholder Requirements

Stakeholder requirements describe what particular stakeholders need to do or achieve.

Example:

"Customer service representatives need to identify the latest status of a customer order without contacting the warehouse."

### 3.3 Solution Requirements

Solution requirements describe the capabilities and qualities a solution must provide.

They are commonly divided into functional and non-functional requirements.

**Functional requirements** describe behavior or functionality.

Example:

"The system shall allow authorized users to approve or reject a purchase request."

**Non-functional requirements** describe quality attributes or conditions under which the solution operates.

Examples:

* Performance.
* Availability.
* Usability.
* Security.
* Reliability.
* Accessibility.
* Maintainability.
* Scalability.

Example:

"The system shall display search results within two seconds for 95% of requests under the agreed normal operating load."

A non-functional requirement should be measurable wherever practical.

### 3.4 Transition Requirements

Transition requirements support the movement from the current state to the future state.

Examples:

* Migrating existing customer records.
* Training employees.
* Converting legacy data.
* Running old and new systems in parallel.
* Establishing temporary support procedures.

These requirements are often temporary and may no longer be needed after the transition is complete.

## 4. Characteristics of High-Quality Requirements

A high-quality requirement should be:

* **Atomic:** It expresses one main requirement rather than several unrelated requirements.
* **Clear:** Its meaning is understandable.
* **Unambiguous:** Reasonable readers interpret it consistently.
* **Complete:** It includes sufficient information for its intended purpose.
* **Consistent:** It does not conflict with other accepted requirements.
* **Feasible:** It can reasonably be implemented within constraints.
* **Necessary:** It supports a genuine business or stakeholder need.
* **Testable:** Compliance can be evaluated using an agreed method.
* **Traceable:** It can be linked to its source and related requirements.
* **Prioritized:** Its relative importance is understood.

### Weak Requirement

"The application should be fast and user-friendly."

Problems:

* "Fast" is undefined.
* "User-friendly" is subjective.
* No operating conditions are specified.
* Acceptance criteria are missing.

### Improved Requirement

"The application shall display the customer search results within two seconds for at least 95% of searches under normal operating conditions."

Usability can be specified separately, for example:

"At least 90% of representative first-time users shall complete the defined registration task without assistance during the agreed usability test."

The test population, task, environment, and measurement method should be agreed with stakeholders.

## 5. Requirement Specification

Requirements may be represented in several forms.

### 5.1 Natural Language

A textual statement written in ordinary language.

Advantages:

* Familiar to business stakeholders.
* Easy to distribute.
* Suitable for many business rules and functional requirements.

Disadvantages:

* Can be ambiguous.
* Can hide multiple conditions.
* May use inconsistent terminology.

### 5.2 Structured Templates

A template can include:

* Requirement ID.
* Requirement statement.
* Type.
* Rationale.
* Source.
* Priority.
* Dependencies.
* Acceptance criteria.
* Validation status.
* Related requirements.

Example:

| Field               | Value                                                                         |
| ------------------- | ----------------------------------------------------------------------------- |
| ID                  | REQ-015                                                                       |
| Name                | Search orders                                                                 |
| Type                | Functional                                                                    |
| Requirement         | The system shall allow authorized service agents to search orders by order ID |
| Rationale           | Reduce time spent locating customer orders                                    |
| Priority            | High                                                                          |
| Source              | Customer service manager                                                      |
| Acceptance criteria | A valid order ID returns the matching order when the user is authorized       |
| Dependency          | Order records must be available to the system                                 |

### 5.3 User Stories

User stories are commonly used in Agile environments.

A common format is:

"As a [role], I want [capability], so that [benefit]."

Example:

"As a customer, I want to track my order so that I can estimate when it will arrive."

A user story is not a complete specification by itself. It should be supported by discussion, acceptance criteria, and any necessary models or constraints.

### 5.4 Use Cases

A use case describes interactions between an actor and a system to achieve a goal.

Typical elements include:

* Use-case name.
* Primary actor.
* Preconditions.
* Trigger.
* Main success scenario.
* Alternative flows.
* Exception flows.
* Postconditions.

Example: Withdraw cash from an ATM.

**Precondition:** The customer has inserted a valid card and authenticated.

**Main flow:**

1. Customer selects withdrawal.
2. Customer enters an amount.
3. System validates the amount and available balance.
4. System authorizes the transaction.
5. ATM dispenses cash.
6. System records the transaction.

**Alternative flow:** The requested amount exceeds the available balance. The system informs the customer and requests a different amount.

### 5.5 Models and Diagrams

Models can clarify complex requirements by representing information visually.

Examples:

* Process flowcharts.
* Business process models.
* Use-case diagrams.
* Data models.
* State diagrams.
* Decision tables.
* Context diagrams.
* Wireframes.
* Prototypes.

Models supplement textual requirements; they do not automatically replace necessary rules, constraints, or acceptance criteria.

## 6. Modeling Requirements

### 6.1 Process Models

Process models represent activities, decisions, events, and handoffs.

They help identify:

* Redundant steps.
* Delays.
* Unclear responsibilities.
* Rework.
* Missing decision paths.
* Automation opportunities.

Example purchase process:

Request submitted → Budget check → Approval decision → Purchase order → Supplier fulfillment.

The model should also show what happens when the budget check fails or an approval is rejected.

### 6.2 Data Models

Data models describe entities, attributes, relationships, and constraints.

Example entities:

* Customer.
* Order.
* Product.
* Payment.
* Shipment.

An order may relate to one customer and contain multiple order items. Each order item references a product.

A data model can reveal missing information, duplicated records, and unclear ownership.

### 6.3 State Models

A state model represents the states an entity can occupy and the events that cause transitions.

Example order states:

Draft → Submitted → Confirmed → Shipped → Delivered.

Alternative states may include Cancelled, Rejected, or Returned.

State models help define which transitions are permitted and which actions are available in each state.

### 6.4 Decision Tables

Decision tables organize combinations of conditions and corresponding actions.

Example:

| Payment valid? | Stock available? | Action                                        |
| -------------- | ---------------- | --------------------------------------------- |
| Yes            | Yes              | Confirm order                                 |
| Yes            | No               | Notify customer of unavailability             |
| No             | Yes              | Request valid payment                         |
| No             | No               | Request valid payment and report stock status |

Decision tables are particularly useful when business rules contain multiple conditions.

## 7. Verification Versus Validation

These concepts are related but distinct.

**Verification:** Are the requirements and specifications sufficiently well-formed and consistent?

Verification examines quality characteristics such as clarity, completeness, consistency, and testability.

**Validation:** Do the requirements represent what stakeholders and the business actually need?

Validation checks alignment with the business need, stakeholder expectations, and desired outcomes.

### Example

A requirement states that a report must be generated within two seconds.

* Verification checks whether the statement defines measurable performance conditions.
* Validation checks whether the report solves the users' actual reporting problem.

A requirement can be well-written but still describe the wrong need.

## 8. Requirement Validation Techniques

Useful techniques include:

**Reviews and walkthroughs:** Stakeholders examine requirements and discuss issues.

**Prototyping:** Users interact with a preliminary representation of a solution.

**Model validation:** Stakeholders check whether diagrams represent the intended processes or behavior.

**Acceptance criteria review:** Stakeholders agree on conditions that demonstrate satisfactory implementation.

**Traceability review:** Analysts verify that requirements connect to legitimate needs and objectives.

Validation should occur throughout analysis rather than only at the end of a project.

## 9. Prioritization

Prioritization helps determine which requirements should receive attention first.

Common factors include:

* Business value.
* Regulatory necessity.
* Risk reduction.
* Cost.
* Dependencies.
* Implementation effort.
* Urgency.
* Stakeholder impact.

### MoSCoW

MoSCoW classifies requirements as:

* **Must have:** Essential for the agreed delivery or outcome.
* **Should have:** Important but not absolutely essential.
* **Could have:** Desirable if resources allow.
* **Won't have this time:** Explicitly excluded from the current scope.

The final category does not necessarily mean the requirement will never be implemented. It means it is excluded from the current delivery scope.

### Example

For an online banking application:

* Must: Secure authentication and balance visibility.
* Should: Transaction search by date.
* Could: Custom dashboard themes.
* Won't have this release: Personalized financial coaching.

Security and regulatory requirements should not be deprioritized simply because implementation is difficult.

## 10. Requirements Traceability

Traceability connects requirements to their sources and related project artifacts.

A requirement may trace to:

* A business objective.
* A stakeholder need.
* A policy or regulation.
* A design component.
* A development task.
* A test case.
* A release.
* A measured business outcome.

### Example Traceability Chain

Business objective: Reduce order-processing time.

→ Stakeholder requirement: Staff must locate orders quickly.

→ Solution requirement: Authorized users can search orders by ID.

→ Design: Search interface and order-query service.

→ Test: Confirm valid order IDs return the correct records within the performance target.

Traceability helps identify the impact of change and detect requirements that lack a clear business justification.

It also supports compliance and testing, particularly in regulated environments.

## 11. Requirements Reuse

Requirements reuse involves applying an existing requirement or requirement component in another context.

Examples:

* Reusing authentication requirements across applications.
* Reusing accessibility standards.
* Reusing common payment rules.
* Reusing standard data-retention requirements.

Before reuse, verify that the requirement remains appropriate for the new context.

Differences in stakeholders, regulations, technology, business processes, and risk can make an apparently reusable requirement unsuitable.

## 12. Design Definition

Design definition describes how a solution may satisfy requirements.

Design representations may include:

* Wireframes.
* Interface prototypes.
* Architecture diagrams.
* Data structures.
* Process designs.
* Interaction flows.
* Business rules.
* Integration diagrams.

### Requirements Versus Design Example

Requirement:

"An authorized employee must be able to retrieve a customer's recent transactions."

Possible designs:

* A web dashboard.
* A desktop application.
* A secured API used by an existing application.
* A report generated from a data warehouse.

Several designs may satisfy the same requirement. The analyst helps stakeholders compare the alternatives against business needs, usability, cost, constraints, and risk.

### Avoiding Premature Design

A common mistake is selecting a technical implementation before the business need is understood.

For example, requiring a particular database product may be unnecessary if the real need is simply to maintain reliable customer records.

However, existing architecture, contractual commitments, legal restrictions, or organizational standards may create legitimate design constraints. Such constraints should be documented and justified.

## 13. Design Options and Trade-Offs

Design decisions often involve competing priorities.

Examples:

* Security versus convenience.
* Customization versus implementation speed.
* Performance versus cost.
* Centralized control versus local flexibility.
* Automation versus human oversight.

A decision should consider:

1. Business objectives.
2. Functional coverage.
3. Quality attributes.
4. Technical constraints.
5. Operational support.
6. Implementation and maintenance costs.
7. Risks and dependencies.
8. Stakeholder feedback.

A prototype can help stakeholders understand these trade-offs before expensive implementation begins.

## 14. Handling Ambiguity and Conflicts

Requirements may conflict because stakeholders have different objectives.

Example:

* Finance wants strict approval controls.
* Operations wants faster purchasing.
* Compliance requires auditable decisions.

The analyst should identify the underlying interests and applicable constraints rather than simply selecting the loudest stakeholder's preference.

Possible approaches include:

* Clarifying business rules.
* Documenting decision criteria.
* Analyzing risks and impacts.
* Comparing options.
* Facilitating stakeholder discussions.
* Escalating unresolved decisions to the appropriate authority.

Ambiguous wording should be clarified before it causes inconsistent implementation.

Words such as "fast," "simple," "secure," "user-friendly," and "appropriate" should be replaced or supported with explicit conditions where possible.

## 15. Case Study: Online Order Management

### Background

A retailer wants to improve its order-management process. Customers cannot reliably track orders, and service agents frequently contact warehouse staff to obtain updates.

### Business Objective

Reduce order-status inquiries by 40% within six months while maintaining accurate customer information and access controls.

### Stakeholder Requirements

* Customers need to view order status.
* Service agents need to locate orders quickly.
* Warehouse staff need to update fulfillment progress.
* Managers need performance reports.
* Compliance staff need access to audit records.

### Solution Requirements

**REQ-001:** The system shall allow authenticated customers to view the status of their own orders.

**REQ-002:** The system shall allow authorized service agents to search orders by order ID.

**REQ-003:** The system shall record the time and identity associated with each status update.

**REQ-004:** The system shall display an agreed set of order statuses.

**REQ-005:** The system shall prevent customers from viewing orders belonging to other customers.

**REQ-006:** The system shall produce a monthly report of order-status inquiries.

### Quality Requirement

"The system shall display order-status information within two seconds for at least 95% of requests under the agreed normal operating load."

### Acceptance Criteria for REQ-001

* Given an authenticated customer with an order, when the customer opens the order page, then the system displays the correct order status.
* Given a customer who does not own an order, when the customer attempts to access it, then the system denies access.
* Given an order-status update, when the customer refreshes the order page, then the current authorized status is displayed within the agreed update interval.

### Model

A simple order lifecycle is:

Submitted → Confirmed → Processing → Shipped → Delivered.

Exception paths include Cancelled, Rejected, and Returned.

The team must define which roles can perform each transition and what happens when an invalid transition is attempted.

### Traceability

The requirement to display status supports the customer transparency objective.

The requirement to record status changes supports auditability and helps investigate incorrect updates.

The monthly inquiry report measures whether the solution is reducing avoidable customer-service workload.

### Lessons

* Separate business outcomes from solution functionality.
* Write requirements so they can be evaluated.
* Model complex behavior and exceptions.
* Validate requirements with the people who will use the solution.
* Maintain links between objectives, requirements, designs, and tests.

## 16. Knowledge Check

### Questions

**1. Which statement is a business requirement?**

A. The system shall display a blue button.
B. Reduce order-processing costs by 15%.
C. The database shall contain an Order table.
D. The login screen shall use a specific font.

**2. Which is a transition requirement?**

A. Migrate existing customer records before the new system becomes operational.
B. Increase customer satisfaction.
C. Search for an order by ID.
D. Maintain system availability.

**3. What does verification primarily assess?**

A. Whether the solution is profitable.
B. Whether requirements are sufficiently well-formed and consistent.
C. Whether every stakeholder agrees with every design detail.
D. Whether the project is completed early.

**4. What does validation primarily assess?**

A. Whether requirements reflect genuine needs.
B. Whether every requirement has an ID.
C. Whether the database is normalized.
D. Whether all developers use the same editor.

**5. Which requirement is most testable?**

A. The system must be fast.
B. The interface must be beautiful.
C. The system shall return search results within two seconds for 95% of requests under agreed conditions.
D. Users should be satisfied.

**6. What is the main benefit of traceability?**

A. It eliminates the need for testing.
B. It connects requirements to their sources, related artifacts, and outcomes.
C. It guarantees zero defects.
D. It prevents all requirement changes.

**7. What is the purpose of a use case?**

A. Describe interactions between an actor and a system to achieve a goal.
B. Define only project cost.
C. Replace all business rules.
D. List employee salaries.

**8. Which statement about design is correct?**

A. Every requirement has exactly one possible design.
B. Design should always precede business analysis.
C. Multiple design alternatives may satisfy the same requirement.
D. Design is unrelated to stakeholder needs.

### Answer Key

1. B — Business requirements express organizational outcomes.
2. A — Data migration supports the transition to the future state.
3. B — Verification checks requirement quality and consistency.
4. A — Validation checks whether requirements represent actual needs.
5. C — It defines measurable performance conditions.
6. B — Traceability supports impact analysis, testing, and justification.
7. A — Use cases describe actor-system interactions and goal achievement.
8. C — Several designs may satisfy the same requirement.

## 17. Revision Summary

* Requirements describe needs or conditions; designs describe possible ways to satisfy them.
* Business requirements express organizational outcomes.
* Stakeholder requirements describe stakeholder needs.
* Solution requirements include functional and non-functional requirements.
* Transition requirements support movement to the future state.
* Good requirements should be clear, necessary, feasible, testable, and traceable.
* Natural-language specifications can be strengthened with templates, models, and acceptance criteria.
* Verification checks requirement quality; validation checks alignment with genuine needs.
* Prioritization supports decisions about scope and sequencing.
* Traceability connects objectives, requirements, designs, and tests.
* Reuse requires checking whether the original requirement fits the new context.
* Design alternatives should be assessed against business value, constraints, risks, and stakeholder needs.

## 18. Further Study

Review the IIBA BABOK Guide sections covering Requirements Analysis and Design Definition, including:

* Specify and Model Requirements.
* Verify Requirements.
* Validate Requirements.
* Define Requirements Architecture.
* Define Design Options.
* Analyze Potential Value and Recommend Solution.

Practice by taking a business problem and creating five requirements, two process or data models, acceptance criteria, a prioritization scheme, and a simple traceability matrix.
