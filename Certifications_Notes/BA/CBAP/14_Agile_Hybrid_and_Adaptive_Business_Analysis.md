# 14. Agile, Hybrid, and Adaptive Business Analysis

## 1. Learning Objectives

By the end of this module, you should be able to:

* Explain how business analysis operates in agile and adaptive environments.
* Compare predictive, adaptive, and hybrid delivery approaches.
* Understand product vision, roadmaps, backlogs, and iterative planning.
* Apply user stories, acceptance criteria, and backlog refinement.
* Explain how requirements evolve through feedback and experimentation.
* Understand prioritization, incremental delivery, and definition of done.
* Support CBAP-style questions involving uncertainty, collaboration, and changing requirements.

## 2. Business Analysis in Adaptive Environments

Business analysis helps organizations understand needs, define desired outcomes, evaluate options, and deliver value.

In an adaptive environment, the team expects that some requirements and solution details will evolve as it learns more about the problem and receives feedback.

The analyst's purpose is not to prevent every change. It is to ensure that changes are understood, evaluated, and directed toward business value.

Adaptive business analysis emphasizes:

* Frequent stakeholder collaboration.
* Incremental delivery.
* Continuous learning.
* Early validation of assumptions.
* Prioritization based on value and risk.
* Lightweight documentation that remains sufficient for the context.
* Rapid feedback and adjustment.

Agile does not mean having no requirements, no planning, or no governance.

## 3. Predictive, Adaptive, and Hybrid Approaches

| Dimension    | Predictive                             | Adaptive                               | Hybrid                                  |
| ------------ | -------------------------------------- | -------------------------------------- | --------------------------------------- |
| Planning     | More detailed upfront                  | Repeated and incremental               | Combines upfront and iterative planning |
| Requirements | More baseline-oriented                 | Evolve as knowledge grows              | Some stable, some evolving              |
| Delivery     | Often larger releases                  | Frequent increments                    | Multiple delivery patterns              |
| Feedback     | At defined checkpoints                 | Frequent throughout development        | Depends on workstream                   |
| Change       | Assessed against established baselines | Expected and reprioritized             | Managed according to context            |
| Best fit     | Stable, well-understood scope          | Uncertain needs and evolving solutions | Mixed constraints and uncertainty       |

No approach is universally superior. Selection should reflect uncertainty, regulatory obligations, dependencies, stakeholder availability, technical risks, and delivery constraints.

### Hybrid Example

A bank may use detailed upfront planning for regulatory approval while developing its customer-facing mobile interface through iterative delivery.

The overall initiative may combine predictive governance with adaptive solution development.

## 4. Agile Principles and Business Analysis

Agile values working solutions, collaboration, responding to change, and customer cooperation.

For a business analyst, these values translate into practical behaviors:

* Collaborate with stakeholders instead of relying only on formal handoffs.
* Validate requirements through working increments.
* Make decisions using feedback and evidence.
* Avoid documentation that adds no meaningful value.
* Preserve documentation required for compliance, maintenance, and operational support.
* Adapt plans as new information emerges.

Agile teams still need clarity about business objectives, constraints, risks, and acceptance conditions.

## 5. Product Vision and Roadmaps

### Product Vision

The product vision communicates the desired future and the problem the product is intended to solve.

A useful vision answers:

* Who is the target user?
* What problem are they experiencing?
* What outcome should improve?
* Why is the product valuable?
* How will success be evaluated?

### Product Roadmap

A roadmap communicates strategic direction and anticipated outcomes over time.

It may include:

* Strategic themes.
* Target customer outcomes.
* Major capabilities.
* Milestones.
* Dependencies.
* Release expectations.
* Assumptions and risks.

A roadmap should not be treated as an immutable list of promised features when uncertainty is high.

### Product Goal and Release Goal

A product goal describes a meaningful future outcome for the product. A release goal describes the intended outcome of a planned release or delivery period.

The wording and governance of these artifacts vary by organization and framework.

## 6. Product Backlog and Prioritization

A product backlog is an ordered collection of work that may contribute to product improvement.

Items may include:

* Features.
* User stories.
* Defects.
* Technical improvements.
* Research tasks.
* Risk reduction.
* Compliance work.

The backlog is not simply a list of stakeholder requests. Items need to be understood, refined, compared, and ordered.

### Prioritization Factors

Consider:

* Business value.
* Customer impact.
* Urgency.
* Risk reduction.
* Dependencies.
* Cost and effort.
* Regulatory deadlines.
* Technical feasibility.
* Cost of delay.
* Confidence in assumptions.

A feature with moderate direct value may deserve priority if it removes a critical dependency or prevents a serious risk.

### MoSCoW

MoSCoW categorizes requirements as:

* **Must have:** Essential for the defined scope or outcome.
* **Should have:** Important but not absolutely essential.
* **Could have:** Desirable if capacity permits.
* **Won't have this time:** Explicitly excluded from the current scope.

The final category does not necessarily mean the item will never be delivered.

### Weighted Scoring

A team can compare options by assigning scores to agreed criteria.

Example criteria:

* Customer value: 40%.
* Risk reduction: 30%.
* Strategic alignment: 20%.
* Implementation feasibility: 10%.

If each criterion is scored from 1 to 5, the team calculates a weighted total.

The scores support discussion; they do not replace judgment. Criteria, weights, and assumptions should be transparent.

## 7. User Stories

A user story expresses a need from the perspective of a user or stakeholder.

Common format:

**As a** [user],
**I want** [capability],
**so that** [benefit].

Example:

As a customer, I want to track my order status so that I can plan when to receive the delivery.

A good story describes a meaningful outcome without prescribing unnecessary implementation details.

### INVEST Heuristic

A commonly used user-story heuristic is INVEST:

* **Independent:** Can be developed with limited dependence on other stories.
* **Negotiable:** Details can be discussed.
* **Valuable:** Provides value to a user or stakeholder.
* **Estimable:** The team can estimate the work sufficiently.
* **Small:** Fits within a manageable delivery increment.
* **Testable:** Its completion can be verified.

INVEST is a heuristic, not a universal compliance checklist.

## 8. Acceptance Criteria

Acceptance criteria define the conditions a story or requirement must satisfy to be accepted.

Example story: A customer wants to reset a forgotten password.

Possible acceptance criteria:

1. The user can request a reset using a registered email address.
2. The system sends a time-limited reset link.
3. The link cannot be reused after successful completion.
4. Invalid or expired links produce an appropriate message.
5. The process does not reveal whether an arbitrary email address has an account.
6. The new password must satisfy the organization's password policy.

Acceptance criteria should be clear, observable, and testable.

### Given–When–Then

A common format for expressing behavior is:

* **Given:** The initial context.
* **When:** The action or event occurs.
* **Then:** The expected outcome.

Example:

Given a registered customer has requested a password reset,
When the customer submits a valid reset token and a compliant new password,
Then the system updates the password and invalidates the token.

This format helps align stakeholders, developers, and testers around expected behavior.

## 9. Backlog Refinement

Backlog refinement is the ongoing activity of improving backlog items so the team can understand and plan them.

Activities include:

* Clarifying user needs.
* Splitting large stories.
* Identifying dependencies.
* Defining acceptance criteria.
* Estimating effort where appropriate.
* Identifying risks and assumptions.
* Reviewing business value.
* Removing obsolete items.

Refinement should reduce uncertainty without requiring every future requirement to be fully specified in advance.

### Splitting Stories

A story may be too large when it combines several independent outcomes or cannot be completed and validated within a reasonable increment.

Possible splitting strategies:

* By workflow step.
* By user type.
* By business rule.
* By data variation.
* By basic and advanced functionality.
* By happy path and important exceptions.

Avoid splitting a story into tasks that each deliver no independently meaningful value when an outcome-oriented split is possible.

## 10. Iterative and Incremental Delivery

**Iterative development** improves a solution through repeated cycles of feedback and refinement.

**Incremental development** adds usable capabilities in successive portions.

They can be combined: a team may deliver a basic feature, evaluate it, and then improve it in later iterations.

### Feedback Cycle

1. Identify a problem or opportunity.
2. Define a hypothesis and expected outcome.
3. Prioritize a small increment.
4. Build or configure the solution.
5. Validate it with stakeholders or users.
6. Measure results.
7. Adapt the backlog and approach.

This cycle reduces the risk of spending substantial resources on assumptions that prove incorrect.

## 11. Minimum Viable Product and Experiments

A minimum viable product (MVP) is a version designed to test important assumptions and provide enough value or learning to justify further decisions.

An MVP is not necessarily a low-quality or incomplete production system. Its scope should be appropriate to the hypothesis being tested and the context in which it will be used.

### Example

A company wants to introduce a new delivery subscription.

Before building a complex subscription platform, it may test customer interest through a limited pilot with clear eligibility rules and manual fulfillment.

The experiment should define:

* Hypothesis.
* Target population.
* Intervention.
* Success metric.
* Observation period.
* Decision threshold.
* Risks and ethical constraints.

A successful experiment supports a decision; it does not automatically prove that the full product will succeed at scale.

## 12. Definition of Ready and Definition of Done

### Definition of Ready

Some teams use a Definition of Ready to indicate whether an item is sufficiently understood to begin work.

Possible elements include:

* Clear business objective.
* Identified stakeholders.
* Understandable scope.
* Testable acceptance criteria.
* Known dependencies.
* No unresolved blocker that prevents meaningful work.

This is a team practice, not a mandatory Scrum artifact.

### Definition of Done

The Definition of Done describes the quality conditions required for work to be considered complete.

Possible elements:

* Implementation completed.
* Code reviewed.
* Automated tests passed.
* Security checks completed.
* Documentation updated.
* Acceptance criteria satisfied.
* Deployment requirements met.

A completed story is not necessarily the same as an accepted business outcome. Both product quality and business value matter.

## 13. Managing Changing Requirements

When a stakeholder requests a change, the analyst should understand:

* What problem prompted the change?
* Which business objective does it support?
* What evidence supports the request?
* What is the impact on current priorities?
* Does it introduce dependencies or risks?
* Is it required for legal or regulatory reasons?
* What work would be delayed if it were prioritized?

In adaptive delivery, a new request may be added to the backlog and prioritized against other work rather than automatically interrupting the current iteration.

The team should still respond appropriately to urgent defects, safety issues, legal obligations, or critical business risks.

## 14. Agile Roles and Collaboration

Roles vary by framework and organization. In Scrum, the formal accountabilities are Product Owner, Scrum Master, and Developers.

Business analysis responsibilities may be performed by a dedicated business analyst, a product manager, a product owner, developers, or several team members.

### Business Analyst Contributions

* Investigate business needs.
* Facilitate stakeholder collaboration.
* Clarify product outcomes.
* Model workflows and rules.
* Define and refine requirements.
* Support prioritization.
* Identify assumptions and dependencies.
* Validate delivered capabilities.
* Evaluate whether business objectives are being achieved.

A business analyst should not assume sole ownership of all product decisions or substitute for the accountable decision-maker.

## 15. Agile Metrics

Useful measures may include:

* Lead time.
* Cycle time.
* Throughput.
* Defect trends.
* Customer satisfaction.
* Adoption rate.
* Outcome-based business KPIs.
* Escaped defects.
* Forecast accuracy.

### Velocity

Velocity is commonly calculated as the amount of estimated work completed in an iteration by a particular team.

Velocity is primarily a planning aid for that team. Comparing velocity across teams can be misleading because estimation scales and working practices differ.

### Output Versus Outcome

* **Output:** What was delivered, such as a new reporting feature.
* **Outcome:** What changed as a result, such as a reduction in time spent preparing reports.
* **Impact:** The broader business effect, such as improved decision speed or lower operating cost.

Delivering more features does not necessarily create more value.

## 16. Worked Case Study: Customer Support Portal

### Problem

A company receives many repetitive support requests. Leadership wants to launch a self-service portal.

### Initial Assumption

The team assumes that a large knowledge base will significantly reduce support volume.

### Adaptive Approach

1. Analyze existing support-ticket categories.
2. Identify the most frequent, costly request types.
3. Interview customers and support staff.
4. Create a small initial set of self-service articles.
5. Pilot the articles with a limited user group.
6. Measure successful self-service resolution, repeat contacts, and customer satisfaction.
7. Refine the content and prioritize additional capabilities.

### Example Success Measures

* Reduction in repetitive tickets.
* Percentage of users resolving issues without agent intervention.
* Repeat-contact rate.
* Customer satisfaction.
* Accuracy and freshness of published information.

The team should investigate poor results rather than simply expanding the knowledge base. The underlying problem may involve unclear procedures, account restrictions, or missing product capabilities.

## 17. Practice Questions

### Question 1

A stakeholder requests a new feature during an adaptive delivery project. What should the analyst do first?

A. Reject the request because the backlog is already defined
B. Automatically interrupt current work
C. Understand the need, evaluate the impact, and support prioritization
D. Implement the request without consulting the team

**Answer: C.** Requests should be evaluated against value, urgency, risks, and existing commitments.

### Question 2

Which statement best describes acceptance criteria?

A. They define observable conditions that a requirement or story must satisfy
B. They replace all testing activities
C. They are the same as the product vision
D. They describe only the technical architecture

**Answer: A.**

### Question 3

A team completes many features but customer retention does not improve. What should it investigate?

A. Whether more features can be delivered regardless of value
B. Whether the delivered capabilities address the underlying customer problem
C. Whether velocity can be increased artificially
D. Whether customer feedback should be discontinued

**Answer: B.** The team must evaluate outcomes, not just output.

### Question 4

A product team uses a Definition of Ready. What is its purpose?

A. Guarantee that no requirement will ever change
B. Indicate whether work is sufficiently understood to begin
C. Replace the Definition of Done
D. Guarantee that every story delivers the same amount of value

**Answer: B.**

### Question 5

Why can comparing velocity across teams be misleading?

A. Velocity cannot be measured
B. All teams must use identical estimates
C. Teams may use different estimation scales and working practices
D. Velocity measures customer satisfaction directly

**Answer: C.**

## 18. Practical Exercises

### Exercise A: Write User Stories

For an online appointment system, write five stories using the user-story format. Give each story at least three testable acceptance criteria.

### Exercise B: Prioritize a Backlog

Create a backlog of eight features. Prioritize them using MoSCoW or a transparent weighted-scoring model. Explain the most important trade-offs.

### Exercise C: Design an Experiment

Choose a proposed product feature. Define a hypothesis, target users, minimum experiment, success metric, decision threshold, and risks.

### Exercise D: Output Versus Outcome

For a reporting dashboard, define:

* Three possible outputs.
* Three measurable user outcomes.
* Two business-impact measures.

Explain how you would determine whether the dashboard is creating value.

## 19. Knowledge Summary

* Adaptive analysis emphasizes learning, feedback, and value.
* Agile does not eliminate requirements, planning, or governance.
* User stories describe needs; acceptance criteria define verifiable conditions.
* Backlog items should be refined and prioritized.
* MVPs and experiments test important assumptions.
* Definition of Done and Definition of Ready serve different purposes.
* Velocity is not a direct measure of business value.
* Evaluate outcomes and impact, not only delivered features.

## 20. References and Further Study

* IIBA, *A Guide to the Business Analysis Body of Knowledge (BABOK Guide), Version 3*.
* Scrum Guide, current official edition.
* Agile Manifesto and its principles.
* Kanban University, flow and Kanban resources.
* IIBA, *Agile Extension to the BABOK Guide*.

This module is an independent study aid, not official IIBA examination material.
