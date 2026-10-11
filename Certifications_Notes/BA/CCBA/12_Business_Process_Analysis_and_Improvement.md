# 12 — Information Technology Business Analysis

## 1. Introduction

The Information Technology (IT) perspective examines business analysis in technology-enabled environments where solutions may involve software applications, infrastructure, integrations, data platforms, cloud services, and operational systems.

The business analyst helps translate business needs into requirements that can guide technical decisions while ensuring that technology supports organizational objectives.

The analyst does not need to be the architect or developer. The key responsibility is to establish shared understanding between business stakeholders and technical specialists.

## 2. Business and Technology Alignment

Technology investments should support defined business needs rather than being pursued simply because a technology is available.

### Alignment questions

* What business problem must be solved?
* Which capabilities are required?
* What does the current environment provide?
* Which systems are affected?
* What constraints apply?
* What benefits are expected?
* How will performance be measured?
* What risks may arise?

### Example

A company wants to migrate its application to the cloud.

Possible objectives:

* Reduce infrastructure maintenance.
* Improve availability.
* Increase capacity during peak demand.
* Improve disaster recovery.
* Reduce deployment delays.

The analyst should establish which objectives matter most and define how each will be evaluated.

Cloud migration itself is an implementation strategy, not a guaranteed business benefit.

## 3. Technology Environments

### On-premises infrastructure

Systems are hosted on infrastructure managed within an organization's facilities or controlled environment.

Considerations:

* Hardware capacity.
* Maintenance.
* Physical security.
* Network connectivity.
* Disaster recovery.
* Capital expenditure.
* Staffing requirements.

### Cloud computing

Computing resources are provided through cloud services.

Considerations:

* Service availability.
* Identity and access management.
* Network design.
* Data residency.
* Cost management.
* Scalability.
* Vendor dependency.
* Shared responsibility.
* Recovery objectives.

### Hybrid environments

Combine on-premises and cloud systems.

They may offer flexibility but introduce integration, identity, network, and operational complexity.

### Legacy systems

Older systems may be business-critical despite limited support or difficult integration.

Potential strategies include:

* Retaining the system.
* Wrapping it with an interface.
* Refactoring selected components.
* Replacing it.
* Migrating data.
* Retiring it.

The appropriate choice depends on business value, risk, cost, and technical constraints.

## 4. Functional and Non-Functional Requirements in IT

### Functional requirements

Describe capabilities or behavior.

Examples:

* Users can reset passwords.
* The application records approved transactions.
* The platform exports reports.
* The service sends notifications.

### Non-functional requirements

Describe quality attributes or operating conditions.

Examples:

* Availability.
* Performance.
* Scalability.
* Security.
* Reliability.
* Maintainability.
* Accessibility.
* Interoperability.
* Recoverability.

### Example: Availability

A service availability requirement may specify a monthly availability target of 99.9%.

A simple approximation of allowable downtime in a 30-day month is:

$$
30 \times 24 \times 60 \times 0.001
= 43.2\text{ minutes}
$$

This is a simplified calculation. Actual service-level definitions must specify measurement periods, exclusions, maintenance windows, and the method used to measure availability.

A percentage without a measurement method may be ambiguous.

## 5. Requirements for Security and Access

Security requirements should reflect business risk, regulatory obligations, and the sensitivity of information.

Important areas include:

* Authentication.
* Authorization.
* Least privilege.
* Audit logging.
* Encryption.
* Session management.
* Account lifecycle management.
* Data retention.
* Incident handling.
* Backup and recovery.

### Authentication vs. Authorization

**Authentication:** Establishes who or what is requesting access.

**Authorization:** Determines what the authenticated identity is permitted to do.

Example:

An employee signs in using multifactor authentication. The system then checks whether that employee may approve a payment.

Authentication alone does not grant every permission.

### Example requirements

* Users shall authenticate using the approved identity provider.
* Access to financial records shall be restricted according to assigned roles.
* Privileged actions shall be recorded in an auditable log.
* Sensitive data shall be encrypted in transit using approved mechanisms.

Security requirements should be specific, testable, and aligned with the organization's security standards.

## 6. Systems Integration and Interfaces

Systems integration allows applications and services to exchange information or coordinate activities.

Common integration methods include:

* APIs.
* Message queues.
* File exchanges.
* Database interfaces.
* Event-driven integration.
* Enterprise integration platforms.

### Interface requirements

An interface specification may define:

* Source and destination systems.
* Data elements.
* Data formats.
* Authentication.
* Error handling.
* Retry behavior.
* Timeouts.
* Rate limits.
* Expected response times.
* Data validation.
* Logging.
* Version compatibility.

### Example

An e-commerce platform sends an order to a warehouse system.

The analyst should clarify:

* When an order is sent.
* Which fields are required.
* How duplicate messages are handled.
* What happens if the warehouse system is unavailable.
* How failed messages are retried.
* How status updates return to the store.

A successful API call does not necessarily mean the business transaction has completed successfully.

## 7. Data Migration

Data migration transfers information from one system or structure to another.

Typical activities include:

1. Identify source data.
2. Profile existing data.
3. Define mapping rules.
4. Cleanse records.
5. Transform formats.
6. Load data.
7. Validate results.
8. Reconcile totals.
9. Obtain business acceptance.
10. Monitor post-migration issues.

### Common risks

* Missing records.
* Duplicate records.
* Incorrect transformations.
* Lost relationships.
* Invalid reference data.
* Inconsistent identifiers.
* Unexpected downtime.
* Incomplete historical records.

### Example

A CRM migration transfers 100,000 customer records.

Validation may include:

* Record counts.
* Required-field completeness.
* Duplicate rates.
* Identifier consistency.
* Sample-based comparisons.
* Relationship integrity.
* Business reconciliation.

Matching record counts alone does not prove that migrated data is accurate.

## 8. Software Development Life Cycle

The Software Development Life Cycle (SDLC) describes activities associated with creating, modifying, testing, deploying, and maintaining software.

A simplified lifecycle includes:

1. Planning.
2. Requirements analysis.
3. Design.
4. Development.
5. Testing.
6. Deployment.
7. Operations and maintenance.

Different delivery approaches organize these activities differently.

### Predictive delivery

Requirements and plans are often established early, with formal change management.

### Iterative delivery

The solution is refined through repeated cycles.

### Incremental delivery

The solution is delivered in usable portions.

### DevOps-oriented delivery

Development and operations practices are integrated to support reliable, repeatable delivery and operation.

Business analysis may occur throughout the lifecycle rather than being restricted to the beginning.

## 9. Testing and Acceptance

Testing provides evidence that a solution behaves as expected under defined conditions.

Common testing levels and types include:

**Unit testing:** Tests small units of software.

**Integration testing:** Tests interactions among components or systems.

**System testing:** Evaluates the integrated solution against its requirements.

**User acceptance testing (UAT):** Evaluates whether the solution is acceptable for intended business use.

**Regression testing:** Checks whether changes have adversely affected existing functionality.

**Performance testing:** Evaluates behavior under defined load or performance conditions.

**Security testing:** Evaluates security properties and identifies vulnerabilities.

These categories can overlap and may be organized differently by different teams.

### Business analyst contributions

The analyst may:

* Clarify expected behavior.
* Review testability.
* Help define acceptance criteria.
* Support test scenario development.
* Resolve requirement ambiguities.
* Coordinate stakeholder participation.
* Help assess business acceptance.

Testing should be based on traceable requirements and business risks.

## 10. Deployment and Operational Readiness

A technically complete solution may not be ready for production.

Operational readiness may require:

* Deployment procedures.
* Monitoring.
* Logging.
* Backup and recovery.
* Support ownership.
* Incident procedures.
* User training.
* Access configuration.
* Documentation.
* Capacity planning.
* Rollback procedures.
* Service-level definitions.

### Example

A new reporting application passes functional tests but lacks monitoring and recovery procedures.

The solution may fail operationally even though its core features work correctly.

The analyst should ensure that relevant operational requirements and transition needs are identified and addressed.

## 11. IT Service Management

IT Service Management (ITSM) focuses on managing IT services so that they meet agreed business needs.

Common service management activities include:

* Incident management.
* Problem management.
* Change enablement.
* Service request management.
* Configuration management.
* Service level management.
* Knowledge management.

### Incident vs. Problem

**Incident:** An unplanned interruption or reduction in service quality.

Example: Users cannot access the application.

**Problem:** The underlying cause, or potential cause, of one or more incidents.

Example: A database connection limit causes recurring outages.

Incident management restores service as appropriate. Problem management investigates causes and helps prevent recurrence.

### Change enablement

Changes to production environments should be assessed and managed according to their risk and the organization's controls.

The goal is to enable useful change while reducing avoidable disruption.

Business analysts may help document business impact, requirements, acceptance conditions, and stakeholder communications.

## 12. Cloud and Infrastructure Requirements

Infrastructure-related business analysis may cover:

* Compute capacity.
* Storage.
* Network connectivity.
* Identity management.
* Backup.
* Disaster recovery.
* Monitoring.
* Logging.
* Automation.
* Resource tagging.
* Cost controls.

### Recovery objectives

**Recovery Time Objective (RTO):** The targeted time within which a service or process should be restored after a disruption.

**Recovery Point Objective (RPO):** The maximum targeted amount of data loss measured in time that may be acceptable following a disruption.

Example:

* RTO: Restore the service within four hours.
* RPO: Recover data to a point no more than 15 minutes before the disruption.

These targets should be derived from business impact and agreed with the relevant stakeholders.

## 13. Technical Debt

Technical debt represents future costs or limitations associated with technical decisions, shortcuts, or deferred improvements.

Examples:

* Outdated dependencies.
* Missing automated tests.
* Duplicated code.
* Weak monitoring.
* Poorly documented interfaces.
* Unsupported software.

Technical debt may increase maintenance effort, security exposure, and delivery risk.

Business analysis should consider the business consequences of technical debt rather than treating every technical improvement as equally important.

Prioritization may consider:

* Risk reduction.
* Operational cost.
* Reliability.
* Security.
* Delivery speed.
* Future capability requirements.

## 14. Practical Case Study: Cloud Migration

A company operates a business-critical order management application on an aging server.

### Business objectives

* Improve availability.
* Reduce recovery time.
* Support seasonal demand.
* Reduce manual infrastructure maintenance.

### Current-state findings

* Recovery procedures are undocumented.
* Capacity planning is manual.
* Monitoring is limited.
* Database backups are not regularly recovery-tested.
* The application depends on a legacy database.

### Requirements

**Availability:** Define the required service availability and measurement method.

**Recovery:** Establish appropriate RTO and RPO targets.

**Security:** Define identity, access, encryption, and audit requirements.

**Performance:** Define expected load and response-time thresholds.

**Integration:** Document dependencies on payment, warehouse, and reporting systems.

**Operations:** Define monitoring, alerting, backup, support, and deployment procedures.

### Alternatives

1. Upgrade the existing environment.
2. Migrate to infrastructure-as-a-service.
3. Refactor selected application components.
4. Replace the application with a commercial product.
5. Use a phased hybrid approach.

### Recommended analysis

Compare the alternatives based on business value, cost, technical feasibility, migration complexity, downtime, security, operational readiness, and long-term maintainability.

A cloud migration should not be approved solely because the cloud offers flexible infrastructure. It should be justified by the organization's needs and expected value.

## 15. Knowledge Check

**Question 1:** What is the difference between authentication and authorization?

A. Authentication verifies identity; authorization determines permitted actions.
B. Authentication encrypts data; authorization creates backups.
C. Both terms mean exactly the same thing.
D. Authorization always happens before any identity verification.

**Question 2:** Which requirement is most clearly non-functional?

A. Users can create orders.
B. The system shall generate invoices.
C. The service shall achieve the agreed availability target.
D. Managers can approve transactions.

**Question 3:** What does RPO describe?

A. The time required to hire replacement staff
B. The targeted maximum amount of data loss measured in time
C. The number of system users
D. The maximum software development duration

**Question 4:** What is the difference between an incident and a problem?

A. An incident is a service disruption; a problem concerns its underlying or potential cause.
B. An incident is always permanent.
C. A problem is always a user request.
D. They are interchangeable terms.

**Question 5:** Why is data migration validation necessary?

A. Matching record counts guarantees correctness.
B. It helps establish whether records and relationships were transferred accurately.
C. It removes the need for backups.
D. It guarantees that users will adopt the new system.

**Question 6:** What is the main purpose of user acceptance testing?

A. To test only individual code functions
B. To evaluate whether the solution is acceptable for intended business use
C. To replace security testing
D. To approve the organization's annual budget

**Question 7:** What should guide a cloud migration decision?

A. Technology trends alone
B. Business needs, costs, risks, constraints, and expected value
C. The provider's marketing claims alone
D. The assumption that cloud systems never fail

### Answers and Explanations

1. **A.** Authentication establishes identity; authorization determines permissions.
2. **C.** Availability is a quality attribute.
3. **B.** RPO describes the targeted recovery point in terms of acceptable data loss.
4. **A.** Incidents concern service disruption, while problems concern underlying or potential causes.
5. **B.** Validation checks data accuracy, completeness, mappings, and relationships.
6. **B.** UAT evaluates suitability for intended business use.
7. **B.** Technology choices should be evaluated against business objectives and constraints.

## 15. Revision Summary

* IT business analysis connects business needs with technology-enabled solutions.
* Functional requirements define behavior; non-functional requirements define quality attributes and operating conditions.
* Security requirements include authentication, authorization, least privilege, and auditing.
* Integration requirements must cover data exchange, errors, retries, and dependencies.
* Data migration requires mapping, cleansing, reconciliation, and validation.
* Testing provides evidence against defined requirements.
* Operational readiness includes monitoring, recovery, support, and deployment procedures.
* ITSM distinguishes incidents from problems and manages changes.
* RTO and RPO address different aspects of recovery.
* Cloud migration must be justified by business value, not technology trends alone.

## 16. Further Study

Review the BABOK Guide's Information Technology perspective and study relevant foundational concepts in requirements engineering, cloud computing, IT service management, systems integration, data migration, and software testing. Practice translating business needs into measurable technical and operational requirements.
