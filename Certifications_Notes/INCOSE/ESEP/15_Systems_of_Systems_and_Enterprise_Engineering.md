# 15. Systems of Systems and Enterprise Engineering

## 1. Purpose

This module examines Systems of Systems (SoS) and enterprise engineering, where multiple independently useful systems must cooperate to achieve broader objectives. It focuses on emergent behavior, distributed ownership, interoperability, governance, capability planning, and enterprise-level trade-offs.

## 2. Learning Objectives

* Distinguish a system from a System of Systems.
* Explain the principal characteristics of SoS environments.
* Understand emergent behavior and cross-system dependencies.
* Compare directed, acknowledged, collaborative, and virtual SoS arrangements.
* Explain enterprise architecture and capability-based planning.
* Manage interoperability, governance, and integration across organizational boundaries.
* Evaluate enterprise-level risks and trade-offs.

## 3. Core Concepts

### 3.1 What Is a System of Systems?

A System of Systems is a collection of constituent systems that interact to deliver capabilities or outcomes that cannot be achieved as effectively by the individual systems alone.

Examples include:

* National air traffic management.
* Emergency response networks.
* Smart-city infrastructure.
* Integrated transportation systems.
* Defense command and control.
* Enterprise-wide information systems.

A SoS is not simply a large system. Its defining characteristics often include operational independence of constituent systems, managerial independence, geographic distribution, evolutionary development, and emergent behavior.

### 3.2 System Versus System of Systems

| Dimension         | Individual system                           | System of Systems                                          |
| ----------------- | ------------------------------------------- | ---------------------------------------------------------- |
| Primary objective | Deliver a defined system capability         | Coordinate capabilities across constituent systems         |
| Ownership         | Often under one authority                   | May involve multiple independent owners                    |
| Requirements      | Primarily system-specific                   | Include mission-level and cross-system needs               |
| Interfaces        | Defined within system boundaries            | Often span organizations and independently managed systems |
| Change control    | Can be centrally coordinated                | Requires negotiation across owners                         |
| Evolution         | Usually governed by one lifecycle authority | Constituent systems may evolve at different rates          |
| Behavior          | More directly controlled within boundaries  | May include emergent behavior from interactions            |

The distinction is contextual. A collection of components does not become a SoS simply because it is large or distributed.

### 3.3 Principal SoS Characteristics

A commonly used framework describes five characteristics:

1. **Operational independence:** Each constituent system can perform useful functions independently.
2. **Managerial independence:** Each constituent system may have its own management, priorities, and resources.
3. **Geographic distribution:** Systems may operate in different locations and environments.
4. **Evolutionary development:** The overall capability and its constituent systems change over time.
5. **Emergent behavior:** Interactions produce outcomes that are not fully explained by the behavior of individual systems alone.

Not every SoS exhibits these characteristics to the same degree, but they help identify the engineering challenges.

### 3.4 Types of Systems of Systems

Four commonly discussed categories are:

**Directed SoS**

A central authority has significant control over the constituent systems and the overall objective. Constituent systems may retain independent functionality, but their development and operation are coordinated through strong direction.

**Acknowledged SoS**

A recognized SoS authority establishes objectives, architecture, and coordination mechanisms, while constituent systems retain substantial independent ownership and control.

**Collaborative SoS**

Constituent systems cooperate voluntarily to achieve mutually beneficial outcomes. Authority is distributed and coordination depends heavily on agreements and shared incentives.

**Virtual SoS**

A broader capability emerges from interactions among systems without a single clearly defined central authority or agreed global plan.

These categories describe governance and control patterns, not levels of technical complexity.

### 3.5 Emergent Behavior

Emergent behavior arises from interactions among system elements or constituent systems.

Examples include:

* Traffic congestion caused by the interaction of individually functioning transportation systems.
* Communication failures caused by incompatible protocols across otherwise operational networks.
* Resource shortages caused by several organizations responding to the same event.
* Delays caused by dependencies among independently managed information systems.

Emergent behavior may be beneficial or harmful.

Engineers should identify important interactions, define scenarios, model dependencies where practical, and monitor actual system-level outcomes.

### 3.6 Interoperability

Interoperability is the ability of systems to exchange information, services, or resources and use them effectively.

It includes several dimensions:

* **Technical interoperability:** Connectivity, protocols, interfaces, and compatible data exchange.
* **Semantic interoperability:** Shared understanding of the meaning of exchanged information.
* **Organizational interoperability:** Compatible processes, responsibilities, and decision-making arrangements.
* **Operational interoperability:** Ability to coordinate activities in the actual operating environment.

Two systems may be technically connected but operationally incompatible. For example, they may exchange timestamps but interpret time zones or event priorities differently.

### 3.7 SoS Architecture

SoS architecture must address more than the internal architecture of each constituent system.

It should identify:

* Mission objectives and required capabilities.
* Constituent systems and their responsibilities.
* Cross-system interfaces and dependencies.
* Information and resource flows.
* Operational scenarios.
* Performance and availability expectations.
* Security boundaries and trust relationships.
* Governance and change-control mechanisms.
* Evolution and integration strategies.

The architecture should support cooperation without unnecessarily removing the independence of constituent systems.

### 3.8 Enterprise Engineering

Enterprise engineering applies structured engineering principles to an enterprise's people, processes, information, technology, resources, and governance.

The enterprise may be a company, public institution, government organization, or a network of collaborating organizations.

Enterprise engineering connects business strategy to operational capabilities and the systems required to deliver them.

### 3.9 Enterprise Architecture

Enterprise architecture provides structured descriptions of how an organization operates and how its business, information, applications, technology, and capabilities relate to one another.

It helps decision-makers evaluate:

* Current capabilities and limitations.
* Target-state architecture.
* Dependencies among systems and processes.
* Gaps between current and required capabilities.
* Investment priorities.
* Transition plans.
* Technical debt and duplication.
* Governance and standards.

Enterprise architecture is not merely an inventory of IT assets. It should connect technology decisions to organizational objectives.

### 3.10 Capability-Based Planning

Capability-based planning begins with the outcomes an organization must achieve, rather than starting with a preferred technology.

A capability can require coordinated contributions from people, processes, information, facilities, and technology.

A typical workflow is:

1. Define strategic objectives.
2. Identify required operational capabilities.
3. Assess existing capabilities.
4. Identify gaps and dependencies.
5. Develop alternative solutions.
6. Evaluate cost, risk, benefits, and feasibility.
7. Prioritize investments.
8. Define transition stages.
9. Measure delivered capability and operational outcomes.

This approach reduces the risk of purchasing technology without understanding the operational problem it must solve.

## 4. Governance and Coordination

### 4.1 Distributed Decision-Making

In a SoS, no single organization may have authority over every constituent system.

Governance therefore needs to clarify:

* Who owns each constituent system.
* Who defines mission-level objectives.
* Who approves cross-system interface changes.
* How costs and benefits are distributed.
* How disputes are resolved.
* Who accepts system-level risks.
* How performance is measured across organizational boundaries.

Effective governance respects legitimate constituent-system constraints while protecting the overall mission.

### 4.2 Interface Agreements

Interface agreements may define:

* Protocols and data formats.
* Service expectations and performance limits.
* Timing and synchronization requirements.
* Security and identity requirements.
* Error handling and recovery.
* Version compatibility.
* Change-notification periods.
* Ownership and escalation procedures.

Interfaces should be treated as managed engineering assets, not informal assumptions.

### 4.3 Evolution and Incremental Integration

Constituent systems may have different funding cycles, release schedules, lifetimes, and technical constraints.

Useful practices include:

* Establish stable interface contracts.
* Use versioning and compatibility policies.
* Test integration incrementally.
* Provide simulators or test environments where appropriate.
* Define migration and deprecation strategies.
* Maintain fallback and degraded-operation modes.
* Review cross-system risks after major changes.

### 4.4 Enterprise-Level Risk

Enterprise risks often cross organizational boundaries.

Examples include:

* A single supplier becoming a critical dependency.
* Multiple systems relying on the same identity provider.
* Incompatible data definitions across departments.
* A cybersecurity incident spreading through trusted connections.
* A shared infrastructure failure affecting several services.
* Competing local optimization goals harming overall performance.

Risk management should therefore include dependencies, common-cause failures, cascading effects, and mission-level consequences.

## 5. Practical Example: Smart-City Emergency Response

A city operates separate traffic management, emergency dispatch, ambulance tracking, hospital capacity, and public notification systems.

Each constituent system can perform useful functions independently. However, effective emergency response requires coordinated behavior.

The SoS engineering team might:

1. Define the overall emergency-response objective.
2. Map constituent systems and their owners.
3. Identify cross-system operational scenarios.
4. Define shared data semantics and interface requirements.
5. Establish timing and availability expectations.
6. Assess privacy, security, and access-control constraints.
7. Simulate high-demand and partial-failure scenarios.
8. Agree on governance and incident escalation.
9. Test end-to-end response performance.
10. Monitor actual outcomes and update the architecture.

A technically functioning dispatch system may still contribute to poor emergency response if hospital capacity information is stale or traffic-routing information arrives too late.

The mission outcome must be assessed across the SoS, not solely within individual systems.

## 6. Exercises

### Exercise 1: Identify a SoS

Choose a national railway network or a university-wide digital services environment. Identify three constituent systems, their independent functions, and two emergent risks.

### Exercise 2: Governance

Three organizations operate independent systems but need to exchange critical information. What governance and interface mechanisms would you establish?

### Exercise 3: Enterprise Investment

An organization wants to replace its software because a new platform is popular. Explain how capability-based planning could improve the decision.

## 7. Suggested Answers

**Exercise 1:** For a railway network, constituent systems might include signaling, passenger information, and ticketing. Emergent risks could include inconsistent service information and disruptions caused by dependencies between signaling and operational scheduling.

**Exercise 2:** Establish shared objectives, system ownership, interface specifications, data definitions, security agreements, change notification, compatibility rules, incident escalation, and a method for resolving disputes.

**Exercise 3:** Begin with required business capabilities, assess current gaps, compare alternatives, evaluate lifecycle cost and risk, and prioritize investments according to measurable outcomes rather than technology popularity.

## 8. Professional Application Evidence

Record examples where you:

* Coordinated engineering work across independent teams.
* Resolved a cross-system interface issue.
* Defined or reviewed shared data and interoperability requirements.
* Assessed an enterprise-level dependency.
* Contributed to capability planning or architecture roadmaps.
* Helped balance local priorities against mission-level objectives.
* Established governance for a distributed technical environment.

## 9. Key Takeaways

* A SoS coordinates independently useful systems to achieve broader outcomes.
* Emergent behavior arises from interactions and may be difficult to predict.
* Interoperability includes technical, semantic, organizational, and operational dimensions.
* SoS governance must account for distributed ownership and independent evolution.
* Enterprise architecture should connect strategy, capabilities, processes, and technology.
* Capability-based planning begins with required outcomes rather than preferred products.

## 10. Suggested References

* INCOSE Systems Engineering Handbook.
* ISO/IEC/IEEE 15288, Systems and software engineering — System life cycle processes.
* ISO/IEC/IEEE 42010, Architecture description.
* Relevant INCOSE material on Systems of Systems Engineering.
* Applicable enterprise architecture frameworks and organizational governance standards.
