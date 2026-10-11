# 10 — Agile Business Analysis

## 1. Introduction

Agile business analysis applies business analysis principles and techniques in environments where solutions are delivered incrementally and requirements may evolve as stakeholders learn more.

The objective is not merely to deliver software quickly. It is to deliver useful outcomes, obtain feedback, reduce uncertainty, and adapt the solution as evidence emerges.

## 2. Agile Values and Principles

Agile approaches generally emphasize:

* Individuals and interactions.
* Working solutions.
* Customer collaboration.
* Responding to change.
* Frequent delivery.
* Continuous improvement.
* Technical quality.
* Sustainable collaboration.

These principles influence business analysis activities, but they do not remove the need for sound requirements, governance, security, or risk management.

## 3. The Product Vision

A product vision describes the intended future state of a product and the value it should provide.

A useful vision answers:

* Who are the primary users?
* What problem are they experiencing?
* What value will the product provide?
* How will success be measured?
* What differentiates the product?
* What constraints affect delivery?

### Example

Vision: Enable small retailers to manage stock accurately and reduce losses through a simple, affordable inventory platform.

Potential measures:

* Inventory accuracy.
* Time required to record stock movements.
* Stockout frequency.
* User adoption.
* Cost per location.

A clear vision guides prioritization when new ideas compete for attention.

## 4. Product Roadmaps

A product roadmap communicates the expected direction of product development.

It may include:

* Strategic outcomes.
* Major capabilities.
* Expected release themes.
* Dependencies.
* Key risks.
* Time horizons.

A roadmap is not necessarily a fixed promise that every feature will be delivered on a specific date. In adaptive environments, plans change as evidence and priorities change.

### Outcome-oriented roadmap

Instead of listing only features such as "dashboard" and "notifications," a roadmap may define:

* Improve inventory visibility.
* Reduce manual reporting.
* Increase fulfillment reliability.

Features are then evaluated based on their contribution to these outcomes.

## 5. Product Backlogs

A product backlog is an ordered collection of work that may contribute to product improvement.

Items may include:

* User stories.
* Defects.
* Technical improvements.
* Research tasks.
* Spikes or experiments.
* Compliance requirements.
* Infrastructure work.

The backlog should be understandable, prioritized, and refined regularly.

### Backlog refinement

Refinement may involve:

1. Clarifying the user need.
2. Breaking down large items.
3. Identifying dependencies.
4. Adding acceptance criteria.
5. Estimating effort.
6. Resolving uncertainty.
7. Reassessing priority.

Backlog refinement is collaborative. The product owner or other designated role may own ordering decisions, while the business analyst supports clarification and analysis.

## 6. User Stories

A user story commonly follows this format:

"As a [user], I want [capability], so that [benefit]."

Example:

"As a warehouse manager, I want to view stock levels across locations so that I can transfer inventory before a stockout occurs."

A good story describes a meaningful capability and its benefit.

### INVEST heuristic

User stories are often evaluated using the INVEST heuristic:

* **Independent:** Can be developed with limited dependency on other stories.
* **Negotiable:** Leaves room for collaboration rather than prescribing every detail prematurely.
* **Valuable:** Provides a clear benefit.
* **Estimable:** Can be estimated sufficiently for planning.
* **Small:** Can be completed within an appropriate delivery period.
* **Testable:** Has clear conditions for determining whether it is complete.

INVEST is a useful guideline, not an absolute rule. Some stories cannot be fully independent.

## 7. Acceptance Criteria

Acceptance criteria define the conditions that a story or requirement must satisfy.

Example story:

"As a customer, I want to reset my password so that I can regain access to my account."

Acceptance criteria:

* A user can request a reset using the approved account identifier.
* The system provides a secure reset process.
* Reset links expire according to the defined security policy.
* A successful reset allows the user to sign in with the new password.
* The process does not disclose sensitive account information to unauthorized parties.

Criteria should be specific enough to support review and testing.

### Given-When-Then

A common format is:

* **Given:** The initial context.
* **When:** The action or event occurs.
* **Then:** The expected result.

Example:

Given a customer has entered a valid delivery address,

When the customer submits the order,

Then the system calculates the applicable delivery charge.

Additional scenarios should cover invalid addresses, unavailable services, and other relevant exceptions.

## 8. Epics and Story Decomposition

An epic is a large body of work that is often divided into smaller stories.

Example epic: Improve order tracking.

Potential stories:

1. View current order status.
2. Receive shipment confirmation.
3. View estimated delivery date.
4. Receive delay notifications.
5. Contact support about a delayed order.

Stories should be decomposed so that meaningful functionality can be delivered and evaluated incrementally.

Avoid splitting work only by technical layer if that prevents users from receiving a usable outcome.

## 9. Prioritization in Agile Environments

Agile prioritization balances business value, risk, urgency, effort, and dependencies.

### MoSCoW

* Must have.
* Should have.
* Could have.
* Won't have this time.

### Value vs. effort

A simple matrix compares expected value against implementation effort.

| Category                | Typical Interpretation         |
| ----------------------- | ------------------------------ |
| High value, low effort  | Strong early candidate         |
| High value, high effort | Important strategic investment |
| Low value, low effort   | Optional improvement           |
| Low value, high effort  | Often a low-priority candidate |

This is a decision aid rather than an automatic ranking method.

### Risk-based prioritization

High-risk work may be performed early to reduce uncertainty.

For example, an uncertain payment gateway integration may deserve an early technical experiment even if it is not the most visible customer feature.

## 10. Agile Planning and Delivery

A common iterative delivery cycle includes:

1. Select work based on priority and capacity.
2. Clarify requirements.
3. Design and implement the increment.
4. Test the solution.
5. Demonstrate the result.
6. Collect feedback.
7. Review performance.
8. Refine the backlog.

Planning occurs at multiple levels:

* Product vision.
* Roadmap.
* Release planning.
* Iteration planning.
* Daily coordination.
* Review and retrospective.

Different agile frameworks use different terminology and event structures.

## 11. Stakeholder Collaboration

Agile environments require frequent communication among:

* Customers.
* Product owners.
* Business analysts.
* Developers.
* Testers.
* Designers.
* Operations teams.
* Compliance specialists.

The analyst helps stakeholders:

* Clarify needs.
* Resolve ambiguities.
* Explore alternatives.
* Define acceptance criteria.
* Review increments.
* Understand trade-offs.
* Make evidence-based decisions.

Frequent collaboration reduces the risk of delivering a technically correct but unsuitable solution.

## 12. Definition of Done

A Definition of Done is a shared set of conditions used to determine whether an increment meets the team's completion standard.

It may include:

* Implementation completed.
* Code reviewed.
* Automated tests passed.
* Security checks completed.
* Documentation updated.
* Acceptance criteria satisfied.
* Required deployment checks passed.

The Definition of Done differs from acceptance criteria.

**Acceptance criteria** describe the conditions for a particular requirement or story.

**Definition of Done** describes the general quality and completion standard applicable to work.

## 13. Agile Metrics

Useful measures include:

* Lead time.
* Cycle time.
* Defect rate.
* Escaped defects.
* Work item completion.
* Customer satisfaction.
* Adoption.
* Business outcome measures.
* Release frequency.

### Velocity

Velocity measures the amount of work a team completes during an iteration, using the team's chosen estimation method.

Velocity can help with local forecasting, but it should not be used to compare different teams as though their estimates were standardized.

Increasing velocity does not automatically mean increasing business value.

### Cycle time

Cycle time measures the elapsed time between defined start and finish points for a work item.

The team must define these points consistently for the metric to be meaningful.

## 14. Agile and Change Management

Requirements can change as the team learns from feedback, experiments, and delivery.

Changes should still be assessed for:

* Business value.
* Risk.
* Cost.
* Dependencies.
* Security.
* Compliance.
* Effect on existing commitments.

Agile does not mean every request should be accepted immediately. A new request may be added to the backlog and prioritized against other work.

## 15. Practical Case Study: Retail Inventory Application

A startup develops an inventory application for small shops.

### Product vision

Help shop owners reduce stockouts and manual recordkeeping.

### Initial backlog

* Record stock receipts.
* Record sales.
* View current stock.
* Receive low-stock alerts.
* Export stock reports.

### First increment

The team prioritizes stock receipts and sales recording because accurate balances depend on these capabilities.

### Acceptance criteria for stock receipts

* Authorized users can record a product receipt.
* The quantity must be greater than zero.
* The product must exist in the catalog.
* The system updates the recorded stock balance.
* The transaction is recorded for audit purposes.

### Feedback

Pilot users report that recording deliveries takes too many steps.

The team investigates and simplifies the workflow.

### Evaluation

The team tracks:

* Time to record a delivery.
* Inventory accuracy.
* Low-stock alert usefulness.
* Weekly active users.
* Stockout frequency.

The product evolves according to actual user behavior and measured outcomes.

## 16. Knowledge Check

**Question 1:** What is the main purpose of a product backlog?

A. To list only completed work
B. To maintain an ordered collection of potential product work
C. To prevent all changes
D. To replace stakeholder communication

**Question 2:** What does the "V" in INVEST represent?

A. Verified
B. Valuable
C. Variable
D. Versioned

**Question 3:** What is the primary purpose of acceptance criteria?

A. To describe the conditions a specific story or requirement must satisfy
B. To define the organization's annual budget
C. To replace all testing
D. To guarantee business profitability

**Question 4:** Which statement about velocity is correct?

A. It is a universal productivity measure across teams.
B. It measures business value directly.
C. It can support forecasting within a team but is not a direct measure of value.
D. Higher velocity always means better quality.

**Question 5:** What is the main difference between acceptance criteria and the Definition of Done?

A. There is no difference.
B. Acceptance criteria apply to particular work; the Definition of Done establishes a general completion standard.
C. The Definition of Done applies only to stakeholders.
D. Acceptance criteria are used only before project approval.

**Question 6:** A new feature request appears during an iteration. What should the team do?

A. Accept it without assessment.
B. Evaluate it and manage its priority and timing through the agreed process.
C. Delete all existing backlog items.
D. Ignore the stakeholder permanently.

### Answers and Explanations

1. **B.** The backlog organizes and orders potential work.
2. **B.** INVEST stands for Independent, Negotiable, Valuable, Estimable, Small, and Testable.
3. **A.** Acceptance criteria define the expected conditions for a specific item.
4. **C.** Velocity supports team-level forecasting but does not directly measure value.
5. **B.** Acceptance criteria are item-specific; the Definition of Done is a broader standard.
6. **B.** New requests should be assessed and prioritized rather than accepted automatically.

## 17. Revision Summary

* Agile business analysis supports iterative delivery and continuous learning.
* The product vision explains the intended value.
* The roadmap communicates product direction.
* The backlog organizes and prioritizes work.
* User stories describe user needs and benefits.
* Acceptance criteria define item-specific conditions.
* The Definition of Done establishes a shared completion standard.
* Agile metrics must be interpreted carefully.
* Adaptability does not eliminate governance, quality, or risk management.

## 18. Further Study

Review the BABOK Guide's Agile perspective, the current Scrum Guide where relevant, and the Agile Manifesto. Practice writing user stories, decomposing epics, defining acceptance criteria, and prioritizing backlog items.
