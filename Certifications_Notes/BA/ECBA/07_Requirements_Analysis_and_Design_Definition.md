# 07 — Requirements Analysis and Design Definition

## 1. Module Objectives

By the end of this module, you should be able to:

* Explain requirements analysis and design definition.
* Understand how requirements are specified and modeled.
* Distinguish requirements from designs.
* Identify useful requirements analysis techniques.
* Understand requirement verification and validation.
* Explain requirements architecture and design options.
* Evaluate solution alternatives.
* Define requirements and designs that support business needs.

## 2. Introduction

Requirements Analysis and Design Definition focuses on analyzing, specifying, modeling, verifying, and validating requirements and designs.

The objective is to transform discovered information into a clear, usable representation of what stakeholders need and how a potential solution could satisfy those needs.

The BABOK Guide identifies six tasks within this knowledge area:

1. Specify and Model Requirements.
2. Verify Requirements.
3. Validate Requirements.
4. Define Requirements Architecture.
5. Define Design Options.
6. Analyze Potential Value and Recommend Solution.

These tasks are interconnected and may be repeated as requirements and designs evolve.

## 3. Specify and Model Requirements

### 3.1 Purpose

Specifying requirements means expressing them in a form that stakeholders and delivery teams can understand and use.

Modeling requirements represents information visually or structurally to clarify relationships, behavior, data, or processes.

Requirements may be documented using:

* Natural-language statements.
* User stories.
* Use cases.
* Process diagrams.
* Data models.
* Decision tables.
* State diagrams.
* Interface specifications.
* Prototypes.

The representation should match the complexity of the need and the audience using it.

### 3.2 Characteristics of Effective Requirements

Good requirements should be:

**Clear:** The intended meaning is understandable.

**Complete:** Necessary information is included for the requirement's intended purpose.

**Consistent:** The requirement does not conflict with related requirements.

**Feasible:** It can reasonably be satisfied within the applicable constraints.

**Testable:** Evidence can be collected to determine whether it has been met.

**Necessary:** It supports a business need, stakeholder need, or relevant constraint.

**Traceable:** Its origin and relationships can be identified when required.

**Unambiguous:** It has one clear interpretation within the intended context.

### 3.3 Example of an Unclear Requirement

Weak requirement:

"The system should load quickly."

Improved requirement:

"Under the agreed normal operating load, the customer dashboard shall load within two seconds for at least 95% of requests."

The improved version defines a measurable performance expectation. The actual threshold and operating conditions should be agreed with stakeholders.

### 3.4 User Stories

A user story commonly follows this format:

"As a [user], I want [capability], so that [benefit]."

Example:

"As a warehouse supervisor, I want to view low-stock products so that I can replenish inventory before stockouts occur."

A user story communicates the user's need and its benefit. Acceptance criteria provide additional detail about the conditions that must be satisfied.

Example acceptance criteria:

* The supervisor can view products below their defined reorder thresholds.
* The list displays the current available quantity.
* The list can be filtered by warehouse location.

User stories are commonly used in adaptive delivery approaches, but their usefulness depends on the context.

## 4. Modeling Requirements

### 4.1 Process Models

Process models describe activities, decisions, and flows of work.

They help identify:

* Process steps.
* Responsibilities.
* Decision points.
* Delays.
* Exceptions.
* Opportunities for improvement.

Example: A loan approval process may include application submission, identity verification, credit assessment, approval, and notification.

### 4.2 Data Models

Data models represent information entities, attributes, and relationships.

For example, an e-commerce system may contain:

* Customer.
* Order.
* Product.
* Payment.
* Shipment.

An order may contain multiple products, and each order may have an associated payment and shipment record, depending on the business rules.

Data modeling helps identify information requirements and potential inconsistencies.

### 4.3 Use Cases

A use case describes interactions between an actor and a system to achieve a goal.

Example: A customer submits an online order.

A use case may describe:

1. The customer selects products.
2. The system displays the cart.
3. The customer provides delivery details.
4. The system validates the order.
5. The payment is processed.
6. The customer receives confirmation.

Alternative flows may cover insufficient stock, invalid addresses, or declined payments.

### 4.4 Decision Tables

Decision tables represent combinations of conditions and their corresponding outcomes.

They are useful when business rules depend on several conditions.

Example: A discount may depend on membership status and order value.

| Member? | Order Value   | Discount |
| ------- | ------------- | -------- |
| Yes     | At least $100 | 10%      |
| Yes     | Below $100    | 5%       |
| No      | At least $100 | 3%       |
| No      | Below $100    | 0%       |

This is an illustrative rule set. Real business rules should be approved by the appropriate stakeholders.

## 5. Verify Requirements

Verification examines whether requirements and designs are expressed appropriately and meet the relevant quality expectations.

Typical verification questions include:

* Is the requirement clear?
* Is it complete enough for its intended purpose?
* Is it consistent with related requirements?
* Is it feasible?
* Is it testable?
* Does it contain ambiguous terms?
* Does it conflict with another requirement?

### Example

Requirement: "The system shall send reports regularly."

Verification identifies ambiguity in "regularly."

The analyst clarifies the intended frequency, recipient, format, and delivery conditions.

Verification improves the quality of the requirement representation.

## 6. Validate Requirements

Validation evaluates whether requirements and designs support the business need and desired outcomes.

A requirement may be clearly written and technically feasible but still fail to address the actual business problem.

### Example

A company requests an automated report showing the number of calls handled by each employee.

The requirement is clear and testable.

However, the underlying business need is to reduce customer waiting time.

The analyst investigates whether call volume alone supports this objective or whether waiting time, abandonment rates, staffing, and resolution quality are also relevant.

Validation helps ensure that the requirements remain connected to the intended business outcomes.

### Verification vs. Validation

| Verification                                      | Validation                                                  |
| ------------------------------------------------- | ----------------------------------------------------------- |
| Examines the quality of requirements and designs  | Examines alignment with business needs                      |
| Focuses on clarity, consistency, and completeness | Focuses on relevance and expected value                     |
| Identifies ambiguous or contradictory statements  | Identifies requirements that do not solve the right problem |

Both activities are important and may occur repeatedly.

## 7. Define Requirements Architecture

Requirements architecture describes the structure and relationships among requirements and designs.

It helps organize complex requirements into meaningful groups and shows how different components relate to one another.

### Benefits

* Improves understanding of complex solutions.
* Supports traceability.
* Reveals dependencies.
* Identifies inconsistencies.
* Supports impact analysis.
* Helps stakeholders understand how capabilities fit together.

### Example

A banking application may contain requirements related to:

* Authentication.
* Account management.
* Payments.
* Notifications.
* Reporting.
* Audit logging.

Requirements architecture helps explain the relationships between these areas. For example, payment processing may depend on authentication, account validation, transaction limits, and audit logging.

## 8. Define Design Options

### 8.1 Purpose

Design options describe possible ways to satisfy requirements and achieve the desired future state.

A design option may involve changes to:

* Software.
* Business processes.
* Organizational structure.
* Technology infrastructure.
* Roles and responsibilities.
* Training.
* External service arrangements.

### 8.2 Solution Options

Common options include:

**Build:** Develop a custom solution.

**Buy:** Purchase an existing product.

**Configure:** Adapt an existing product to meet requirements.

**Outsource:** Obtain services from an external provider.

**Improve existing capabilities:** Modify existing processes or systems.

**Do nothing:** Retain the current state when the costs, risks, or lack of value justify that decision.

The do-nothing option should be evaluated realistically, including the consequences of leaving the existing problem unresolved.

### 8.3 Compare Design Options

Relevant criteria may include:

* Cost.
* Business value.
* Technical feasibility.
* Implementation time.
* Operational impact.
* Risk.
* Security.
* Maintainability.
* Scalability.
* User experience.
* Regulatory compliance.

No single criterion automatically determines the best option.

## 9. Analyze Potential Value and Recommend a Solution

This task evaluates the potential value of design options and supports the recommendation of a suitable solution.

The analyst considers how well each option addresses the business need and the trade-offs associated with it.

### Example

A company wants to reduce customer service response time.

Three alternatives are considered:

1. Hire additional agents.
2. Improve the existing customer service process.
3. Implement a chatbot for common questions.

The analyst compares costs, expected response-time improvements, customer experience, implementation effort, risks, and operational implications.

A chatbot may reduce repetitive inquiries but may not address complex cases. Additional agents may improve capacity but increase recurring costs.

The best recommendation depends on evidence and the organization's objectives.

### Cost-Benefit Analysis

A simple financial assessment compares expected benefits with expected costs.

Net benefit can be represented as:

Net Benefit = Total Expected Benefits − Total Expected Costs

For example:

* Expected benefits: $120,000.
* Expected costs: $80,000.
* Net benefit: $40,000.

This simple calculation does not capture every consideration. Time value of money, uncertainty, operational risks, and non-financial benefits may also matter.

## 10. Practical Case Study

### Scenario: Online Retail Returns

A retailer wants to reduce the cost and processing time associated with customer returns.

### Requirements

* Customers can initiate eligible returns online.
* The system displays return eligibility.
* Customers receive return instructions.
* Staff can monitor return status.

### Modeling

A process model represents return initiation, eligibility checking, authorization, shipping, inspection, and refund processing.

A decision table defines eligibility rules based on purchase date, product category, and item condition.

### Verification

The analyst checks whether requirements are clear, consistent, complete enough for implementation, and testable.

### Validation

The analyst checks whether the requirements address the business objectives of reducing processing costs and improving customer experience.

### Design Options

* Improve the existing manual process.
* Configure a returns module in the current platform.
* Purchase a specialized returns management system.
* Develop a custom returns application.

### Recommendation

The analyst compares cost, implementation time, integration complexity, expected savings, and customer impact before recommending an option.

## 11. Practice Questions

### Question 1

Which requirement is the most testable?

A. The application should be user-friendly.

B. The report should load quickly.

C. The system shall display the account balance within two seconds for at least 95% of requests under the agreed test conditions.

D. Customers should receive excellent service.

**Correct answer: C**

Explanation: It specifies a measurable performance threshold and test conditions.

### Question 2

What is the primary purpose of requirement verification?

A. To determine whether the organization should enter a new market.

B. To examine the quality and consistency of requirements.

C. To approve the final budget.

D. To guarantee that a solution generates revenue.

**Correct answer: B**

Explanation: Verification checks whether requirements are appropriately expressed and satisfy relevant quality criteria.

### Question 3

A requirement is clearly written but does not contribute to the business objective. Which activity is most relevant?

A. Validation.

B. Version numbering only.

C. Project scheduling.

D. Database backup.

**Correct answer: A**

Explanation: Validation examines whether requirements and designs address the underlying business need.

### Question 4

Which model is especially suitable for representing business rules involving multiple conditions and outcomes?

A. Decision table.

B. Organizational chart only.

C. Project calendar.

D. Contact list.

**Correct answer: A**

Explanation: Decision tables organize combinations of conditions and the corresponding outcomes.

### Question 5

An organization compares building a custom application with purchasing an existing product. Which activity is being performed?

A. Defining design options.

B. Retiring all requirements.

C. Conducting stakeholder identification only.

D. Confirming meeting attendance.

**Correct answer: A**

Explanation: Build-versus-buy analysis compares potential approaches to satisfying business needs.

### Question 6

What is the purpose of requirements architecture?

A. To organize requirements and explain their relationships.

B. To eliminate all stakeholder communication.

C. To replace business objectives.

D. To ensure that every requirement has equal priority.

**Correct answer: A**

Explanation: Requirements architecture helps stakeholders understand structure, dependencies, and relationships across complex requirements.

### Question 7

Which statement best describes a solution recommendation?

A. It should always favor the newest technology.

B. It should consider expected value, feasibility, costs, risks, and the business need.

C. It should ignore operational constraints.

D. It should be made without comparing alternatives.

**Correct answer: B**

Explanation: Recommendations should be based on the needs, context, and trade-offs associated with available options.

## 12. Revision Checklist

* [ ] Explain requirements analysis and design definition.
* [ ] Recall the six BABOK tasks in this knowledge area.
* [ ] Identify characteristics of effective requirements.
* [ ] Understand user stories, use cases, process models, and decision tables.
* [ ] Distinguish verification from validation.
* [ ] Explain requirements architecture.
* [ ] Compare build, buy, configure, outsource, and do-nothing options.
* [ ] Evaluate potential value and trade-offs.
* [ ] Apply requirements analysis concepts to a practical case.

## 13. Further Study Resources

* IIBA: https://www.iiba.org/
* BABOK Guide: https://www.iiba.org/standards-and-resources/babok/
* ECBA certification: https://www.iiba.org/business-analysis-certifications/ecba/

## 14. Final Exam Reminder

When analyzing a scenario, ask:

1. Is the requirement clearly expressed?
2. Does it satisfy relevant quality criteria?
3. Does it address the actual business need?
4. How does it relate to other requirements?
5. What design options could satisfy it?
6. Which option offers the most appropriate value within the organization's constraints?

Do not confuse a technically correct requirement with a requirement that is genuinely valuable to the business.
