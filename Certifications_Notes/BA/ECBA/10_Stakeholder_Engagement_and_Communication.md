# 10 — Business Analysis Perspectives

## 1. Module Objectives

By the end of this module, you should be able to:

* Explain the meaning of a business analysis perspective.
* Understand how context affects business analysis work.
* Distinguish common business analysis perspectives.
* Understand Agile, Business Intelligence, Information Technology, Business Architecture, and Business Process Management perspectives.
* Identify how techniques and deliverables vary across contexts.
* Apply perspective-based thinking to business scenarios.

## 2. Introduction

A business analysis perspective is a particular way of viewing business analysis work based on the context in which it is performed.

The business need, organizational environment, delivery approach, stakeholders, and solution type influence how an analyst works.

For example, a Business Analyst working on a data warehouse may focus on data quality, integration, reporting, and analytical needs. An analyst working on an Agile software team may focus on iterative delivery, backlog refinement, user stories, and frequent stakeholder feedback.

The underlying goal remains consistent: understand needs, facilitate change, and help deliver value.

The BABOK Guide describes several perspectives that provide specialized context for business analysis:

1. Agile.
2. Business Intelligence.
3. Information Technology.
4. Business Architecture.
5. Business Process Management.

These perspectives are not mutually exclusive. One initiative may involve several of them.

## 3. Agile Perspective

### 3.1 Definition

Agile is an approach to delivering value through iterative or incremental work, collaboration, feedback, and adaptation.

In an Agile environment, requirements may evolve as stakeholders learn more about the business problem and evaluate working solutions.

The Business Analyst helps the team understand needs, clarify requirements, manage priorities, and maintain alignment with business objectives.

### 3.2 Common Characteristics

* Frequent stakeholder collaboration.
* Incremental delivery.
* Iterative refinement of requirements.
* Continuous feedback.
* Adaptation to changing needs.
* Emphasis on delivering value.
* Close cooperation between business and delivery teams.

Agile does not mean working without planning or documentation. The appropriate level of documentation depends on the context.

### 3.3 Common Techniques

* User stories.
* Product backlog refinement.
* User story mapping.
* Workshops.
* Prototypes.
* Acceptance criteria.
* Iteration reviews.
* Retrospectives.
* Prioritization.

### 3.4 User Stories

A user story commonly describes a capability from a user's perspective.

Format:

"As a [user], I want [capability], so that [benefit]."

Example:

"As a customer, I want to track my order so that I know when it will arrive."

Acceptance criteria clarify the conditions that must be satisfied.

For example:

* The customer can access the current order status.
* The displayed status reflects the latest available information.
* The customer receives an understandable message when tracking information is unavailable.

### 3.5 Backlog Prioritization

A product backlog contains work items that may be considered for delivery.

Prioritization may consider:

* Business value.
* Customer impact.
* Risk.
* Dependencies.
* Urgency.
* Effort.
* Learning opportunities.

The person accountable for product value, often the Product Owner in Scrum, is responsible for effective product backlog management. The Business Analyst may support this work depending on the organization's roles.

### 3.6 Example

A company develops a mobile banking application.

Instead of attempting to deliver every feature at once, the team releases an initial version supporting secure login and balance viewing.

Customer feedback then informs the prioritization of transfers, notifications, and additional functionality.

The analyst helps clarify requirements and assess feedback as the product evolves.

## 4. Business Intelligence Perspective

### 4.1 Definition

Business Intelligence (BI) focuses on transforming data into information that supports reporting, analysis, monitoring, and business decision-making.

Business analysis in a BI context often involves understanding data sources, information needs, metrics, reporting requirements, and analytical capabilities.

### 4.2 Common Activities

* Identifying decision-making needs.
* Defining KPIs.
* Analyzing existing reports.
* Documenting data requirements.
* Assessing data quality.
* Understanding data sources.
* Defining reporting requirements.
* Supporting dashboard design.
* Validating analytical outputs.

### 4.3 Data Quality Dimensions

Useful data quality dimensions include:

**Accuracy:** Does the data correctly represent what it is intended to represent?

**Completeness:** Are required values present?

**Consistency:** Is information represented consistently across systems?

**Timeliness:** Is the data available when needed?

**Validity:** Does the data conform to defined rules and formats?

**Uniqueness:** Are duplicate records appropriately controlled?

### 4.4 Example

A retail manager wants to understand declining sales.

The analyst identifies relevant measures, including revenue, units sold, returns, discounts, customer segments, and product categories.

The analyst then investigates data sources, defines metric calculations, and documents reporting requirements.

A dashboard may reveal that the decline is concentrated in specific product categories or customer segments.

### 4.5 Reporting Requirements

A useful reporting requirement specifies:

* Intended audience.
* Business question.
* Required measures.
* Data sources.
* Filters and dimensions.
* Reporting frequency.
* Time period.
* Access restrictions.
* Accuracy and timeliness expectations.

Weak requirement: "Create a sales dashboard."

Improved requirement: "Provide regional sales managers with weekly revenue, order volume, and return-rate measures, filterable by region and product category."

## 5. Information Technology Perspective

### 5.1 Definition

The Information Technology (IT) perspective addresses business analysis in technology-related initiatives.

These initiatives may involve application development, infrastructure, system integration, cloud migration, cybersecurity controls, or technology replacement.

The analyst connects business needs with technical possibilities and constraints.

### 5.2 Common Activities

* Identifying business and technical requirements.
* Understanding system interfaces.
* Documenting functional and non-functional requirements.
* Analyzing data flows.
* Identifying integration dependencies.
* Supporting solution evaluation.
* Clarifying operational requirements.
* Coordinating business and technical stakeholders.

### 5.3 Functional Requirements

Functional requirements describe what a solution must do.

Examples:

* Users can reset their passwords.
* The system generates monthly invoices.
* Managers can approve purchase requests.
* The application records completed transactions.

### 5.4 Non-Functional Requirements

Non-functional requirements describe qualities, constraints, or performance expectations.

Examples include:

* Performance.
* Availability.
* Security.
* Accessibility.
* Reliability.
* Maintainability.
* Scalability.
* Usability.

Example:

"The service shall maintain 99.9% monthly availability, measured according to the agreed monitoring and exclusion rules."

Non-functional requirements should be defined in measurable terms whenever appropriate.

### 5.5 System Integration

System integration connects applications, services, or data sources.

An analyst may need to identify:

* Source and destination systems.
* Data exchanged.
* Transfer frequency.
* Error handling.
* Authentication and authorization.
* Data transformation rules.
* Ownership of information.
* Monitoring requirements.

### 5.6 Example

A company moves an application to a cloud platform.

The analyst documents business continuity requirements, user access needs, data migration requirements, availability expectations, and integration dependencies.

Technical specialists determine implementation details while the analyst helps maintain alignment with business needs.

## 6. Business Architecture Perspective

### 6.1 Definition

Business Architecture provides a structured view of an organization and how its parts work together to deliver value.

It helps connect strategy with business capabilities, value streams, information, organizational structure, and initiatives.

### 6.2 Common Elements

**Business capabilities:** What the organization must be able to do.

**Value streams:** How value is created and delivered through a sequence of activities.

**Organizational structure:** How responsibilities and authority are arranged.

**Information concepts:** Important business information and relationships.

**Business strategy:** The organization's objectives and direction.

### 6.3 Capability Analysis

Capability analysis identifies what an organization can do today and what it must be able to do in the future.

Example: A logistics company may have capabilities in:

* Order management.
* Transportation planning.
* Warehouse operations.
* Shipment tracking.
* Customer service.
* Billing.

A strategic objective to provide real-time shipment visibility may require improvements in tracking, data integration, and customer communication capabilities.

### 6.4 Capability Maps

A capability map organizes an organization's capabilities into a structured view.

It can help stakeholders identify:

* Weak capabilities.
* Duplicate capabilities.
* Investment priorities.
* Strategic dependencies.
* Areas for improvement.

A capability map describes what the organization needs to do rather than necessarily specifying the detailed sequence of activities.

### 6.5 Example

A bank wants to expand its digital services.

Its strategy requires stronger digital identity verification, payment processing, fraud detection, and customer support capabilities.

Business architecture helps connect the strategic objective with these capabilities and identify which initiatives are needed.

## 7. Business Process Management Perspective

### 7.1 Definition

Business Process Management (BPM) focuses on understanding, analyzing, improving, and managing business processes.

A business process is a set of related activities that produces an outcome for a customer or another stakeholder.

BPM considers process performance, consistency, efficiency, quality, and alignment with organizational goals.

### 7.2 Process Lifecycle

A typical process improvement cycle may include:

1. Identify the process and its objectives.
2. Document the current process.
3. Measure performance.
4. Analyze bottlenecks and causes.
5. Design the improved process.
6. Implement the changes.
7. Monitor results.
8. Refine the process when necessary.

This is a practical lifecycle model; organizations may use different frameworks.

### 7.3 Common Techniques

* Process mapping.
* BPMN.
* Value stream mapping.
* Root-cause analysis.
* Process simulation.
* Performance measurement.
* Gap analysis.
* Workflow analysis.

### 7.4 Process Metrics

Common measures include:

* Cycle time.
* Throughput.
* Error rate.
* Cost per transaction.
* First-pass yield.
* Rework rate.
* Waiting time.
* Customer satisfaction.

### 7.5 Example

A company processes supplier invoices manually.

The analyst maps the process and discovers duplicate data entry, unclear approval responsibilities, and delays caused by missing information.

Potential improvements include standardized invoice submission, automated validation, clearer approval rules, and exception handling.

The analyst compares performance before and after implementation.

## 8. Comparing the Five Perspectives

| Perspective                 | Primary Focus                                       | Example Deliverable                           |
| --------------------------- | --------------------------------------------------- | --------------------------------------------- |
| Agile                       | Iterative delivery and evolving requirements        | User stories and acceptance criteria          |
| Business Intelligence       | Data, reporting, and decision support               | KPI definitions and dashboard requirements    |
| Information Technology      | Technology-enabled change                           | Functional and non-functional requirements    |
| Business Architecture       | Strategic capabilities and organizational structure | Capability map                                |
| Business Process Management | Process performance and improvement                 | Current-state and future-state process models |

The deliverables shown are examples, not exclusive outputs. A single perspective may use many techniques and deliverables.

## 9. Combining Perspectives

Real-world initiatives often involve multiple perspectives.

Consider a manufacturer introducing predictive maintenance.

**Business Architecture:** Identifies the capability needed to improve equipment reliability.

**Business Process Management:** Examines the maintenance workflow and current sources of delay.

**Business Intelligence:** Defines equipment-performance measures and reporting requirements.

**Information Technology:** Defines sensor integration, data storage, security, and application requirements.

**Agile:** Supports iterative delivery and feedback as the solution is developed.

The analyst selects techniques according to the needs of the initiative rather than treating perspectives as isolated disciplines.

## 10. Practical Case Study

### Scenario: Digital Transformation in a Logistics Company

The company wants to reduce shipment delays and improve customer visibility.

### Business Need

Customers lack reliable information about shipment status, while operations teams rely on manual updates.

### Applying the Perspectives

**Business Architecture**

Identify shipment tracking and customer communication as capabilities requiring improvement.

**Business Process Management**

Map shipment creation, dispatch, tracking updates, exception handling, and delivery confirmation.

**Business Intelligence**

Define on-time delivery rate, average delay, tracking-data freshness, and customer inquiry volume.

**Information Technology**

Define system integrations, access controls, data requirements, availability, and notification functionality.

**Agile**

Deliver an initial tracking capability, gather user feedback, and refine later releases based on value and priorities.

### Expected Outcome

The company can measure whether the initiative improves visibility, reduces customer inquiries, and supports more reliable deliveries.

## 11. Practice Questions

### Question 1

Which perspective most directly focuses on iterative delivery and frequent feedback?

A. Business Architecture.

B. Agile.

C. Business Intelligence.

D. Business Process Management.

**Correct answer: B**

Explanation: Agile emphasizes iterative delivery, collaboration, and adaptation.

### Question 2

A company needs dashboards showing revenue by region and product category. Which perspective is especially relevant?

A. Business Intelligence.

B. Business Architecture only.

C. Organizational recruitment only.

D. Business Process Management only.

**Correct answer: A**

Explanation: BI focuses on data, reporting, metrics, and decision support.

### Question 3

Which perspective helps connect strategic objectives with the capabilities an organization must possess?

A. Business Architecture.

B. Agile testing only.

C. Document archiving.

D. Interview scheduling.

**Correct answer: A**

Explanation: Business Architecture links strategy with capabilities and organizational structure.

### Question 4

A company wants to reduce invoice processing time by identifying unnecessary steps. Which perspective is most directly relevant?

A. Business Process Management.

B. Market branding.

C. Business Architecture only.

D. Product advertising.

**Correct answer: A**

Explanation: BPM focuses on process analysis, performance, and improvement.

### Question 5

Which is an example of a non-functional requirement?

A. Users can submit an order.

B. Managers can approve requests.

C. The service shall meet an agreed availability target.

D. The system generates an invoice.

**Correct answer: C**

Explanation: Availability describes a quality attribute rather than a specific business function.

### Question 6

A predictive maintenance initiative needs sensor integration, equipment KPIs, and a redesigned maintenance workflow. What should the analyst conclude?

A. Only one business analysis perspective can be used.

B. Multiple perspectives can contribute to the same initiative.

C. Business analysis ends when a technology is selected.

D. Metrics are unnecessary when sensors are installed.

**Correct answer: B**

Explanation: Complex initiatives frequently combine several perspectives.

## 12. Revision Checklist

* [ ] Explain what a business analysis perspective is.
* [ ] Describe the Agile perspective.
* [ ] Understand the Business Intelligence perspective.
* [ ] Understand the Information Technology perspective.
* [ ] Explain Business Architecture.
* [ ] Explain Business Process Management.
* [ ] Distinguish capabilities from processes.
* [ ] Distinguish functional from non-functional requirements.
* [ ] Identify useful deliverables for each perspective.
* [ ] Apply multiple perspectives to a single business initiative.

## 13. Further Study Resources

* IIBA: https://www.iiba.org/
* BABOK Guide: https://www.iiba.org/standards-and-resources/babok/
* ECBA certification: https://www.iiba.org/business-analysis-certifications/ecba/

## 14. Final Exam Reminder

Read the scenario carefully and identify its primary focus:

* Iterative delivery and adaptation: Agile.
* Data, reporting, and decision support: Business Intelligence.
* Technology-enabled change: Information Technology.
* Strategy and organizational capabilities: Business Architecture.
* Process performance and improvement: Business Process Management.

Several perspectives may apply simultaneously. Select the answer that best matches the main problem described.
