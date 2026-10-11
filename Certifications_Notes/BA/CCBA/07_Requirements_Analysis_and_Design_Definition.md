# 07 — Requirements Analysis and Design Definition

## 1. Introduction

Requirements Analysis and Design Definition focuses on structuring, specifying, verifying, validating, and maintaining requirements and designs that provide a usable basis for solution development and implementation.

The BABOK Guide identifies six tasks in this knowledge area:

1. Specify and Model Requirements.
2. Verify Requirements.
3. Validate Requirements.
4. Define Requirements Architecture.
5. Define Design Options.
6. Analyze Potential Value and Recommend Solution.

This knowledge area connects business needs to clear requirements, solution structures, design alternatives, and value-based recommendations.

## 2. Specify and Model Requirements

Specification represents requirements in a form that stakeholders can understand, evaluate, and use.

Modeling provides a structured representation of business information, behavior, processes, rules, or solution interactions.

Different representations are appropriate for different needs.

### 2.1 Requirement Specifications

A requirement statement may include:

* Unique ID.
* Description.
* Rationale.
* Source.
* Priority.
* Acceptance criteria.
* Dependencies.
* Assumptions.
* Status.
* Related design and test references.

Example:

**ID:** ORD-014

**Requirement:** The system shall prevent an order from being submitted when a mandatory delivery address is missing.

**Rationale:** Incomplete addresses cause delivery failures and manual correction.

**Acceptance criteria:**

* An order without a delivery address cannot be submitted.
* The system identifies the missing field.
* A valid address allows submission, subject to other validation rules.

The statement should be refined to match the system's actual scope and agreed business rules.

## 3. Requirements Modeling Techniques

### 3.1 Process Models

A process model describes the sequence of activities, decisions, and interactions involved in work.

Common notations include flowcharts and Business Process Model and Notation (BPMN).

Example order process:

1. Receive order.
2. Validate customer details.
3. Confirm inventory.
4. Process payment.
5. Create shipment.
6. Notify customer.

Decision branches represent situations such as insufficient inventory or payment failure.

Process models help identify:

* Rework.
* Bottlenecks.
* Handoffs.
* Missing activities.
* Exceptions.
* Opportunities for automation.

### 3.2 Use Cases

A use case describes how an actor interacts with a solution to achieve a goal.

Example: Place an Order.

**Primary actor:** Customer.

**Preconditions:**

* The customer has selected at least one item.
* The items are available for ordering.

**Main flow:**

1. Customer reviews the cart.
2. Customer enters delivery details.
3. System calculates the total.
4. Customer submits payment.
5. System confirms the order.
6. Customer receives confirmation.

**Alternative flow:** Payment fails, and the system requests another payment method.

Use cases help define interactions, success conditions, and exceptions.

### 3.3 User Stories

A common agile format is:

"As a [user], I want [capability], so that [benefit]."

Example:

"As a warehouse supervisor, I want to view stock levels across locations so that I can transfer inventory before stockouts occur."

A user story is a starting point, not necessarily a complete specification. It may need acceptance criteria, business rules, and supporting models.

### 3.4 Data Models

Data models describe information entities and their relationships.

Example e-commerce entities:

* Customer.
* Order.
* Order Item.
* Product.
* Payment.
* Shipment.

An order may contain multiple order items, while each order item references a product.

Data models support:

* Shared terminology.
* Data integrity.
* Integration design.
* Reporting.
* Identification of duplicate or missing information.

### 3.5 State Models

A state model describes the possible states of an entity and the transitions between them.

Example order states:

* Created.
* Awaiting Payment.
* Confirmed.
* Processing.
* Shipped.
* Delivered.
* Cancelled.

A transition model identifies which events allow movement between states.

For example, an order should not move from "Created" directly to "Delivered" without satisfying the required intermediate conditions.

### 3.6 Decision Models

Decision models represent business decisions, the information used to make them, and the resulting outcomes.

Example: Determine a discount.

Inputs:

* Customer category.
* Order amount.
* Promotional eligibility.

Output:

* Applicable discount percentage.

Decision tables can help ensure that rules cover expected combinations and avoid conflicting outcomes.

## 4. Verify Requirements

Verification evaluates whether requirements and models meet defined quality standards and are suitable for their intended purpose.

### Verification Questions

* Is the requirement clear?
* Is it unambiguous?
* Is it complete?
* Is it consistent?
* Is it feasible?
* Is it testable?
* Is it traceable?
* Does it comply with applicable standards?
* Does it contain unnecessary implementation detail?

### Example

Weak requirement: "The application must respond quickly."

Verification identifies ambiguity and the absence of measurable criteria.

Improved requirement: "Under the agreed load profile, 95% of search requests shall complete within two seconds."

The improved requirement is more measurable and testable, although the load profile and measurement method must also be defined.

### Verification Techniques

* Reviews.
* Walkthroughs.
* Checklists.
* Model inspections.
* Peer review.
* Automated consistency checks.
* Comparison against standards.
* Validation rules for requirement repositories.

Verification can occur iteratively as requirements and designs evolve.

## 5. Validate Requirements

Validation determines whether requirements support the business need and whether the proposed solution will create the intended value.

A technically clear requirement may still be unnecessary or misaligned with the actual problem.

### Validation Questions

* Does the requirement address the underlying need?
* Does it support the desired outcome?
* Is it relevant to the stakeholder?
* Is it consistent with the business strategy?
* Does it introduce unacceptable risk?
* Is the proposed capability worth its cost?
* Can the expected value be measured?

### Example

A stakeholder requests a dashboard showing hundreds of operational metrics.

Verification checks that each requirement is clear and testable.

Validation investigates which decisions the dashboard must support. The result may be a smaller set of meaningful indicators rather than hundreds of low-value metrics.

### Verification vs. Validation

| Verification                          | Validation                                                 |
| ------------------------------------- | ---------------------------------------------------------- |
| Assesses requirement quality          | Assesses alignment with needs                              |
| Checks clarity and consistency        | Checks relevance and value                                 |
| Examines testability and completeness | Examines whether the right problem is being addressed      |
| May use reviews and checklists        | May use stakeholder feedback and business outcome analysis |

Both activities are important and may overlap in practice.

## 6. Define Requirements Architecture

Requirements architecture describes how requirements and designs are organized and related.

It helps stakeholders understand how individual requirements fit into a larger structure.

### 6.1 Architectural Relationships

Requirements may be related through:

* Decomposition.
* Dependencies.
* Shared capabilities.
* Common business rules.
* Interfaces.
* Data relationships.
* Traceability.
* Constraints.

### 6.2 Example

Business objective: Improve online sales.

Business requirements:

* Improve checkout completion.
* Reduce payment failures.
* Increase product availability visibility.

Solution requirements:

* Support approved payment methods.
* Validate order details.
* Display current availability.
* Record transaction outcomes.
* Provide checkout performance monitoring.

These requirements interact. Payment processing depends on transaction validation, while accurate availability depends on reliable inventory data.

### 6.3 Benefits

Requirements architecture helps:

* Identify gaps and duplication.
* Understand dependencies.
* Manage complexity.
* Support impact analysis.
* Organize delivery increments.
* Identify shared solution capabilities.
* Maintain alignment with business objectives.

A well-structured requirements set is easier to review and maintain than an unorganized list of statements.

## 7. Define Design Options

Design options represent alternative ways to satisfy requirements and achieve business outcomes.

A design option may involve:

* Buying a commercial product.
* Developing custom software.
* Improving an existing process.
* Outsourcing a service.
* Automating selected activities.
* Changing organizational roles.
* Combining several approaches.

### 7.1 Evaluate Design Options

Consider:

* Functional fit.
* Non-functional requirements.
* Cost.
* Time to implement.
* Technical feasibility.
* Security.
* Compliance.
* Maintainability.
* Scalability.
* Stakeholder experience.
* Operational impact.
* Vendor dependency.
* Implementation risks.

### 7.2 Example: Customer Support Improvement

Option A: Hire more agents.

Advantages:

* Additional human capacity.
* Potentially better handling of complex cases.

Disadvantages:

* Recurring labor costs.
* Recruitment and training time.

Option B: Improve knowledge management.

Advantages:

* May reduce repetitive inquiries.
* Helps agents locate accurate answers.

Disadvantages:

* Requires content ownership and maintenance.
* Does not necessarily reduce every inquiry type.

Option C: Introduce AI-assisted support.

Advantages:

* May help classify inquiries and draft responses.
* Can improve agent productivity.

Disadvantages:

* Requires evaluation, governance, integration, and monitoring.
* Incorrect responses and privacy risks must be managed.

Option D: Combine workflow redesign, better knowledge management, and targeted automation.

This option may address multiple root causes but may require more coordination.

The best choice depends on evidence, constraints, and expected value.

## 8. Analyze Potential Value and Recommend Solution

The analyst evaluates whether a proposed solution is likely to deliver sufficient value and recommends an appropriate option.

### 8.1 Value Analysis

Consider:

* Expected benefits.
* Initial investment.
* Operating costs.
* Implementation effort.
* Risk exposure.
* Strategic alignment.
* Stakeholder impact.
* Time to realize benefits.
* Measurement feasibility.

### 8.2 Cost-Benefit Analysis

Suppose a proposed system has:

* Initial implementation cost: EGP 500,000.
* Annual operating cost: EGP 80,000.
* Expected annual savings: EGP 250,000.

First-year net benefit before other costs:

$$
250{,}000 - 80{,}000 - 500{,}000 = -330{,}000
$$

Subsequent annual net benefit, assuming stable costs and savings:

$$
250{,}000 - 80{,}000 = 170{,}000
$$

A simple payback calculation based on the initial investment and annual net operating savings is:

$$
Payback = \frac{500{,}000}{170{,}000}
\approx 2.94\text{ years}
$$

This is a simplified estimate. A complete business case may include implementation timing, cash-flow timing, taxes, inflation, risk, discount rates, and nonfinancial benefits.

### 8.3 Net Present Value

Net Present Value (NPV) expresses the present value of future cash flows minus the initial investment.

$$
NPV = \sum_{t=1}^{n}\frac{CF_t}{(1+r)^t}-I_0
$$

Where:

* \(CF_t\) = net cash flow in period \(t\).
* \(r\) = discount rate.
* \(I_0\) = initial investment.
* \(n\) = number of periods.

A positive NPV indicates that projected discounted cash flows exceed the initial investment under the assumptions used.

Financial metrics support the decision but do not replace assessment of compliance, safety, strategy, and stakeholder value.

## 9. Practical Case Study: Automated Expense Claims

An organization processes employee expense claims manually.

### Current problems

* Average approval time is seven days.
* Employees frequently submit incomplete forms.
* Managers lack visibility into pending claims.
* Finance spends significant time correcting records.

### Proposed requirements

**Functional**

* Employees can submit expense claims.
* The system validates mandatory fields.
* Managers can approve or reject claims.
* Finance can export approved claims.

**Non-functional**

* Authorized users can access the system securely.
* The system records an auditable history of approvals.
* Common screens load within the agreed response-time threshold.

**Business rule**

* Claims exceeding the specified threshold require additional approval.

### Models

* Process model for submission and approval.
* Use case for submitting a claim.
* State model for claim statuses.
* Decision table for approval routing.
* Data model for employees, claims, receipts, and approvals.

### Validation

Confirm that automation addresses the causes of delay and that the target approval time is feasible.

### Design alternatives

* Improve the existing forms and process.
* Configure a commercial expense-management tool.
* Develop a custom application.
* Use an existing enterprise platform.

### Recommendation

Compare alternatives against cost, usability, integration, security, auditability, and expected reduction in processing time. Recommend the option best aligned with the organization's needs and constraints.

## 10. Knowledge Check

**Question 1:** What is the primary purpose of verification?

A. To determine whether the solution is profitable
B. To evaluate the quality of requirements and models
C. To authorize project funding
D. To select a vendor automatically

**Question 2:** Which question is most closely associated with validation?

A. Is the requirement grammatically correct?
B. Does the requirement address the actual business need?
C. Is the requirement ID unique?
D. Does the requirement have a version number?

**Question 3:** Which model is best suited to representing transitions between order statuses?

A. State model
B. Stakeholder map only
C. SWOT analysis
D. Cost-benefit analysis

**Question 4:** What is the primary purpose of requirements architecture?

A. To organize requirements and their relationships
B. To eliminate stakeholder consultation
C. To prevent all future changes
D. To replace business strategy

**Question 5:** Why should multiple design options be evaluated?

A. To ensure that the most expensive option is selected
B. To compare alternatives against needs, costs, risks, and value
C. To avoid defining requirements
D. To guarantee that all stakeholders agree

**Question 6:** A system meets every written requirement but does not solve the original business problem. Which activity may have been inadequate?

A. Validation
B. Version numbering
C. Requirements naming
D. Repository access control

### Answers and Explanations

1. **B.** Verification assesses requirement and model quality.
2. **B.** Validation checks alignment with the actual business need.
3. **A.** State models describe states and transitions.
4. **A.** Requirements architecture organizes elements and relationships.
5. **B.** Comparing alternatives supports an informed recommendation.
6. **A.** Requirements may be well specified but still fail to address the real need.

## 10. Revision Summary

* Specification makes requirements clear and usable.
* Models represent processes, interactions, data, states, and decisions.
* Verification assesses requirement quality.
* Validation assesses alignment with needs and expected value.
* Requirements architecture organizes relationships and dependencies.
* Design options represent alternative ways to meet business needs.
* Value analysis supports recommendations using benefits, costs, risks, and strategic alignment.

## 11. Further Study

Review the BABOK Guide's Requirements Analysis and Design Definition knowledge area. Practice writing measurable requirements, selecting suitable models, distinguishing verification from validation, and evaluating design alternatives.
