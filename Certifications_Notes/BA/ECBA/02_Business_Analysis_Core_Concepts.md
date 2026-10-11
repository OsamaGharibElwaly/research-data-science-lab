# 02 — Business Analysis Core Concepts

## 1. Module Objectives

By the end of this module, you should be able to:

* Explain the six core concepts of business analysis.
* Understand the Business Analysis Core Concept Model (BACCM).
* Explain the relationships among change, need, solution, stakeholder, value, and context.
* Apply the BACCM to practical business scenarios.
* Distinguish requirements, designs, needs, and solutions.
* Recognize how context influences business analysis decisions.

## 2. Introduction to the BACCM

The Business Analysis Core Concept Model (BACCM) is a conceptual framework defined by IIBA to explain the fundamental concepts that underpin business analysis.

It contains six core concepts:

1. Change
2. Need
3. Solution
4. Stakeholder
5. Value
6. Context

These concepts are interconnected. Understanding one often requires considering the others.

For example, an organization may need to change its customer service process because customer complaints are increasing. Stakeholders have different expectations, and the organization must select a solution that creates value within its operational and regulatory context.

## 3. The Six Core Concepts

### 3.1 Change

Change is the transformation of an enterprise in response to a need.

Change may involve:

* Introducing a new system.
* Improving a business process.
* Restructuring an organization.
* Changing policies or procedures.
* Launching a new product.
* Automating repetitive tasks.

Change can be planned or emerge in response to unexpected circumstances.

**Example:** A bank changes its loan approval process to reduce processing time and improve customer experience.

The Business Analyst helps understand the change, its objectives, the stakeholders it affects, and the outcomes it should produce.

### 3.2 Need

A need is a problem or opportunity that motivates a change.

Needs may arise from:

* Customer dissatisfaction.
* Operational inefficiency.
* Regulatory requirements.
* Market opportunities.
* Competitive pressure.
* New technologies.
* Financial performance issues.

A need is not necessarily the same as a stakeholder's proposed solution.

**Example:**

A department manager says, "We need a new CRM."

The analyst investigates and discovers that employees cannot access accurate customer information across departments.

The underlying need may be to improve customer information accessibility and consistency. A new CRM is only one possible solution.

### 3.3 Solution

A solution is a specific way of satisfying one or more needs in a particular context.

Solutions may include:

* Software applications.
* Manual procedures.
* Business process redesign.
* Organizational changes.
* Training programs.
* Outsourcing arrangements.
* Combinations of people, processes, information, and technology.

**Example:** To reduce invoice-processing errors, an organization might implement automated validation, standardize invoice templates, train employees, or combine these approaches.

The analyst should evaluate alternatives rather than assume that the most technologically advanced solution is automatically the best.

### 3.4 Stakeholder

A stakeholder is an individual, group, or organization that has a relationship with the change, need, or solution.

Common stakeholders include:

* Customers.
* End users.
* Business sponsors.
* Managers.
* Employees.
* Project team members.
* Suppliers.
* Regulators.
* Operations teams.
* Executives.
* Support personnel.

Stakeholders may have conflicting needs.

For example, customers may want faster approval, while a compliance team requires additional verification.

Business analysis must identify and understand these perspectives.

### 3.5 Value

Value is the worth, importance, or usefulness of something to a stakeholder in a context.

Value is not limited to financial benefits. It may include:

* Higher revenue.
* Lower costs.
* Reduced risk.
* Improved customer satisfaction.
* Better accessibility.
* Faster service.
* Improved compliance.
* Higher employee productivity.
* Better decision-making.

Value is contextual: the same solution can create value for one stakeholder while introducing costs or risks for another.

**Example:** Automation reduces processing time but increases the need for employee training. The organization should evaluate the overall benefits and trade-offs.

### 3.6 Context

Context consists of the circumstances influencing, or being influenced by, a change.

Context may include:

* Organizational culture.
* Business strategy.
* Existing processes.
* Technology infrastructure.
* Laws and regulations.
* Market conditions.
* Available budgets.
* Skills and staffing.
* Geographic considerations.
* Time constraints.

**Example:** A cloud-based system may be suitable for one company but inappropriate for another because of data residency requirements or infrastructure limitations.

The analyst must evaluate solutions in the actual context in which they will operate.

## 4. Understanding the Relationships Between Core Concepts

The six concepts should not be memorized as isolated definitions.

Consider this sequence:

1. A need creates a reason for change.
2. Stakeholders experience or influence the need and change.
3. A solution is developed or selected to address the need.
4. The solution is evaluated in its context.
5. Value is assessed based on stakeholder outcomes.
6. Evaluation may reveal additional needs and lead to further change.

This is a conceptual relationship, not a mandatory project sequence.

### Example: Online Appointment System

A medical clinic experiences overcrowding.

* **Need:** Reduce waiting time and improve appointment management.
* **Change:** Transform the appointment booking process.
* **Stakeholders:** Patients, receptionists, doctors, administrators, and IT support.
* **Solution:** Online booking, automated reminders, and improved scheduling rules.
* **Value:** Reduced waiting time, fewer missed appointments, and better staff utilization.
* **Context:** Privacy requirements, staff skills, patient accessibility, budget, and existing systems.

A solution that works technically but excludes patients who cannot use digital services may fail to deliver the expected overall value.

## 5. Requirements and Designs

Requirements and designs are related but distinct concepts.

### Requirements

A requirement represents a need, capability, condition, or characteristic that must be satisfied.

Requirements can describe:

* Business objectives.
* Stakeholder needs.
* Solution behavior.
* Quality expectations.
* Constraints.

### Designs

A design represents a possible solution approach or describes how a solution could satisfy requirements.

For example:

**Requirement:** Customers must be able to reset their passwords without contacting support.

**Design:** Provide a password-reset page that sends a time-limited verification link to the registered email address.

The requirement describes the expected capability. The design describes one implementation approach.

A single requirement may be satisfied by several different designs.

## 6. The Three Common Categories of Requirements

A useful classification distinguishes business, stakeholder, and solution requirements.

### Business Requirements

Describe the goals, objectives, and outcomes that explain why a change is needed.

Example: Reduce customer onboarding time by 40%.

### Stakeholder Requirements

Describe the needs of a stakeholder or stakeholder group that must be satisfied to achieve the business requirements.

Example: Customer service representatives need a consolidated view of each customer's onboarding status.

### Solution Requirements

Describe the capabilities and characteristics of a solution that will meet stakeholder requirements.

Solution requirements are commonly divided into:

* **Functional requirements:** What the solution must do.
* **Non-functional requirements:** How well the solution must perform or what qualities and constraints it must satisfy.

Example functional requirement: The system shall allow users to upload identification documents.

Example non-functional requirement: The system shall display the onboarding dashboard within two seconds under the agreed operating conditions.

### Transition Requirements

Transition requirements describe temporary capabilities needed to move from the current state to the future state.

Examples include:

* Migrating customer records.
* Training employees.
* Converting legacy data.
* Running old and new systems in parallel.
* Preparing operational support teams.

Transition requirements are necessary during implementation but may no longer be relevant once the transition is complete.

## 7. The Business Analysis Context

The same business problem may require different solutions in different environments.

Consider two organizations that want to automate invoice processing.

Organization A has:

* A modern cloud infrastructure.
* Structured digital invoices.
* An experienced IT team.
* A flexible budget.

Organization B has:

* Legacy software.
* Mostly paper invoices.
* Limited technical support.
* Strict infrastructure restrictions.

The best solution may differ because the context differs.

A Business Analyst should consider organizational capabilities, constraints, risks, stakeholder expectations, and external factors before recommending an approach.

## 8. Practical Case Study

### Scenario: Warehouse Order Errors

An e-commerce warehouse has experienced an increase in incorrect customer shipments.

Management proposes buying barcode scanners.

The analyst investigates and discovers:

* Product labels are sometimes incorrect.
* Employees use inconsistent picking procedures.
* Inventory records are updated late.
* Temporary employees receive limited training.
* Supervisors cannot easily identify error patterns.

### BACCM Analysis

**Need:** Reduce incorrect shipments and associated costs.

**Change:** Improve warehouse picking, verification, and inventory processes.

**Stakeholders:** Warehouse employees, supervisors, customers, inventory managers, IT staff, and finance teams.

**Possible solutions:** Barcode scanning, standardized procedures, improved labeling, training, and real-time inventory updates.

**Value:** Fewer returns, lower shipping costs, improved customer satisfaction, and more reliable inventory.

**Context:** Warehouse layout, equipment costs, staff turnover, system compatibility, and order volume.

### Conclusion

Barcode scanners may help, but they will not necessarily solve incorrect labeling or poor training. The analyst should assess the full business problem before recommending a solution.

## 9. Practice Questions

### Question 1

Which BACCM concept describes the circumstances influencing a change?

A. Value.

B. Context.

C. Need.

D. Solution.

**Correct answer: B**

Explanation: Context includes the organizational, technological, regulatory, and environmental circumstances surrounding the change.

### Question 2

A stakeholder says that the organization needs a mobile application. What should the Business Analyst determine?

A. Which mobile framework is most popular.

B. Whether the stakeholder has authority to purchase software.

C. The underlying need and expected business outcome.

D. Which developer can begin immediately.

**Correct answer: C**

Explanation: The analyst should understand the need before committing to a proposed solution.

### Question 3

Which example best represents value?

A. Installing a server.

B. Writing a requirements document.

C. Reducing customer complaints and processing costs.

D. Scheduling a requirements workshop.

**Correct answer: C**

Explanation: Value represents the worth or usefulness produced for stakeholders. Activities and deliverables may contribute to value but are not automatically valuable outcomes themselves.

### Question 4

Which requirement category describes the need to migrate records before launching a new system?

A. Business requirement.

B. Stakeholder requirement.

C. Transition requirement.

D. Functional requirement.

**Correct answer: C**

Explanation: Data migration supports the temporary transition from the existing environment to the future state.

### Question 5

A system allows users to complete a transaction. A separate requirement states that the transaction must complete within three seconds. How should these requirements generally be classified?

A. Both are transition requirements.

B. The first is functional; the second is non-functional.

C. The first is a business requirement; the second is a stakeholder register.

D. Both are exclusively business requirements.

**Correct answer: B**

Explanation: Completing a transaction describes functionality. The performance threshold describes a quality requirement.

### Question 6

Which statement best describes the relationship between requirements and designs?

A. Requirements and designs always mean the same thing.

B. Requirements describe needs or conditions; designs describe possible ways to satisfy them.

C. Designs are always produced before any business need is identified.

D. Requirements should specify every implementation detail.

**Correct answer: B**

Explanation: Requirements express what must be achieved or satisfied, while designs explore how a solution might accomplish it.

### Question 7

Which BACCM concept is most directly concerned with the people or groups affected by a change?

A. Stakeholder.

B. Solution.

C. Change.

D. Context.

**Correct answer: A**

Explanation: Stakeholders have a relationship with the need, change, or solution and may influence its success.

## 10. Revision Checklist

* [ ] Recall all six BACCM concepts.
* [ ] Explain each concept in your own words.
* [ ] Apply the six concepts to a practical business scenario.
* [ ] Distinguish needs from proposed solutions.
* [ ] Distinguish requirements from designs.
* [ ] Identify business, stakeholder, solution, and transition requirements.
* [ ] Distinguish functional from non-functional requirements.
* [ ] Explain why value depends on context and stakeholder perspectives.
* [ ] Identify competing stakeholder needs and solution trade-offs.

## 11. Further Study Resources

* IIBA: https://www.iiba.org/
* BABOK Guide: https://www.iiba.org/standards-and-resources/babok/
* ECBA certification: https://www.iiba.org/business-analysis-certifications/ecba/

## 12. Final Exam Reminder

When a scenario mentions the BACCM, identify the underlying need, the proposed change, the relevant stakeholders, the possible solution, the expected value, and the surrounding context. Pay particular attention to the difference between a business need and a stakeholder's preferred solution.
