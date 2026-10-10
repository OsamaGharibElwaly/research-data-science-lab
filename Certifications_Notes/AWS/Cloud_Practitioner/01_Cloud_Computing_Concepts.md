# Module 01: Cloud Computing Concepts

## 1. Learning Objectives

By the end of this module, you should be able to:

* Define cloud computing and explain its main benefits.
* Compare cloud deployment models.
* Understand the AWS Cloud Value Proposition.
* Explain CapEx versus OpEx.
* Identify the six advantages of cloud computing.
* Understand scalability, elasticity, agility, and high availability.
* Compare cloud-based infrastructure with traditional on-premises infrastructure.

## 2. What Is Cloud Computing?

Cloud computing is the on-demand delivery of IT resources over the internet, typically with pay-as-you-go pricing.

Instead of buying and maintaining physical servers, organizations can rent computing power, storage, databases, networking, and other services from cloud providers such as Amazon Web Services (AWS).

### Traditional IT vs. Cloud Computing

| Traditional IT                                 | Cloud Computing                                 |
| ---------------------------------------------- | ----------------------------------------------- |
| Purchase physical servers                      | Provision virtual servers on demand             |
| Large upfront investment                       | Pay for resources used                          |
| Hardware upgrades require planning             | Resources can be adjusted quickly               |
| Organization maintains physical infrastructure | AWS manages the underlying cloud infrastructure |
| Capacity planning is critical                  | Capacity can be provisioned as needed           |

**Example:** A startup can launch a website using Amazon EC2 without purchasing physical servers or building its own data center.

## 3. Cloud Deployment Models

### 3.1 Public Cloud

Infrastructure is provided by a cloud provider and shared across multiple customers through logically isolated environments.

* No need to own physical data centers.
* Resources can be provisioned quickly.
* Customers pay according to their usage and pricing model.

**Example:** Hosting an application on AWS.

### 3.2 Private Cloud

Cloud infrastructure is dedicated to a single organization. It may be hosted on-premises or by a third party.

* Greater control over the environment.
* May support specialized regulatory requirements.
* Can involve significant infrastructure and operational costs.

**Example:** A bank operates a private cloud for workloads that require dedicated infrastructure.

### 3.3 Hybrid Cloud

Combines on-premises or private infrastructure with public cloud services.

* Supports gradual cloud migration.
* Can integrate existing systems with cloud applications.
* May introduce networking and management complexity.

**Example:** A company keeps a legacy database on-premises while hosting its customer-facing website on AWS.

## 4. Cloud Service Models

### 4.1 Infrastructure as a Service (IaaS)

Provides fundamental computing resources such as virtual machines, storage, and networking.

The customer manages the operating system, applications, and much of the configuration.

**AWS example:** Amazon EC2.

### 4.2 Platform as a Service (PaaS)

Provides a platform for building and deploying applications while reducing the need to manage underlying infrastructure.

**AWS example:** AWS Elastic Beanstalk, which helps deploy and manage applications.

### 4.3 Software as a Service (SaaS)

Provides complete software applications that users access through a browser or application.

**Example:** A hosted email or customer relationship management application.

### Comparison

| Model | Customer Focus                              | Example                  |
| ----- | ------------------------------------------- | ------------------------ |
| IaaS  | Managing operating systems and applications | Amazon EC2               |
| PaaS  | Building and deploying applications         | AWS Elastic Beanstalk    |
| SaaS  | Using a finished application                | Hosted business software |

## 5. AWS Cloud Value Proposition

AWS offers several important benefits.

### 5.1 Trade Capital Expense for Variable Expense

Traditional IT often requires large upfront purchases. Cloud computing allows organizations to pay for resources as they consume them.

### 5.2 Benefit from Massive Economies of Scale

AWS aggregates demand across many customers, which can help reduce the cost of infrastructure services.

### 5.3 Stop Guessing Capacity

Organizations can provision resources according to demand instead of purchasing enough hardware for an uncertain future peak.

### 5.4 Increase Speed and Agility

Developers can provision resources in minutes rather than waiting for hardware procurement and installation.

### 5.5 Stop Spending Money Running and Maintaining Data Centers

AWS operates its underlying cloud infrastructure, allowing customers to focus more on their business applications.

### 5.6 Go Global in Minutes

AWS Regions allow organizations to deploy workloads in different geographic areas without building their own data centers worldwide.

## 6. Capital Expenditure vs. Operational Expenditure

**Capital expenditure (CapEx):** Money spent purchasing long-term assets, such as physical servers and networking equipment.

**Operational expenditure (OpEx):** Ongoing costs of operating a business, including cloud service consumption.

| CapEx                                | OpEx                                                      |
| ------------------------------------ | --------------------------------------------------------- |
| Large upfront hardware purchases     | Recurring or usage-based cloud charges                    |
| Requires forecasting future capacity | Resources can be adjusted as needs change                 |
| Hardware may depreciate over time    | Costs are tied to the selected services and pricing model |

Cloud computing does not eliminate all upfront or fixed costs. Certain cloud commitments and implementation projects can still involve substantial expenditure.

## 7. Essential Cloud Concepts

### Scalability

The ability to increase or decrease resources to meet changing demand.

* **Vertical scaling:** Increasing the capacity of an individual resource, such as moving to a larger EC2 instance.
* **Horizontal scaling:** Adding or removing resource instances, such as adding more EC2 instances behind a load balancer.

### Elasticity

The ability to automatically or dynamically adjust resources as demand changes.

**Example:** An Auto Scaling group adds EC2 instances during a sales event and removes excess instances when demand falls.

### Agility

The ability to experiment, develop, and deploy services quickly.

### High Availability

Designing systems to remain accessible despite individual component failures, commonly by using redundant resources and multiple Availability Zones.

### Fault Tolerance

Designing systems to continue operating even when particular components fail, potentially without interruption.

### Reliability

The ability of a system to perform its intended functions correctly and consistently.

### Global Reach

The ability to serve customers in multiple geographic markets using cloud infrastructure distributed across regions.

## 8. AWS Shared Responsibility: An Introduction

Cloud security responsibilities are divided between AWS and its customers.

* **AWS:** Security of the cloud, including the underlying physical facilities, hardware, and foundational infrastructure.
* **Customer:** Security in the cloud, including customer data, access permissions, and many workload configurations.

The exact division depends on the service used. For example, customers have more operating-system responsibilities with EC2 than with a fully managed service.

Detailed security responsibilities are covered in Module 08.

## 9. Exam-Focused Revision Notes

* Cloud computing provides on-demand IT resources over the internet.
* Public cloud infrastructure is operated by a cloud provider for multiple customers.
* Private cloud infrastructure is dedicated to one organization.
* Hybrid cloud combines public cloud with private or on-premises infrastructure.
* IaaS provides infrastructure resources; PaaS provides an application platform; SaaS provides complete software.
* CapEx generally involves upfront asset purchases; OpEx generally involves operating costs.
* Scalability adjusts capacity; elasticity adjusts resources in response to changing demand.
* Horizontal scaling adds instances; vertical scaling increases the capacity of an instance.
* AWS can help reduce the need for upfront infrastructure investment.
* Cloud adoption does not automatically guarantee lower costs, high availability, or security; architecture and configuration still matter.

## 10. Knowledge Check

**Question 1:** A company wants to avoid purchasing physical servers before launching a new application. Which benefit of cloud computing is most relevant?

A. Increased capital expenditure
B. Trading capital expense for variable expense
C. Mandatory private cloud deployment
D. Elimination of all operational costs

**Answer:** B — Cloud computing can reduce upfront infrastructure purchases in favor of usage-based costs.

**Question 2:** A website needs to add more server instances during periods of high traffic. Which concept does this illustrate?

A. Horizontal scaling
B. Capital expenditure
C. Private cloud
D. Depreciation

**Answer:** A — Horizontal scaling adds instances to increase capacity.

**Question 3:** Which cloud service model provides virtual machines while allowing the customer to manage the operating system?

A. SaaS
B. IaaS
C. PaaS
D. On-premises only

**Answer:** B — IaaS provides infrastructure resources such as virtual machines.

**Question 4:** A company operates its own data center and connects it to AWS. Which deployment model does this represent?

A. SaaS
B. Public cloud only
C. Hybrid cloud
D. Dedicated software

**Answer:** C — Hybrid cloud combines on-premises or private infrastructure with public cloud resources.

**Question 5:** Which concept describes automatically adjusting resources as demand changes?

A. Elasticity
B. Depreciation
C. Capital expenditure
D. Manual procurement

**Answer:** A — Elasticity allows resources to adjust dynamically as demand changes.

## 11. Practical Exercise

Consider an online store that receives ordinary traffic most of the year but experiences a significant traffic increase during holiday sales.

Write a short analysis answering:

1. Why might cloud computing be preferable to purchasing physical servers?
2. How could horizontal scaling help?
3. How could elasticity reduce unnecessary resource consumption?
4. Which costs might remain even after migrating to AWS?
5. What availability measures should the company consider?

### Suggested Solution

Cloud computing allows the store to provision resources without purchasing hardware for peak demand far in advance. Horizontal scaling adds application instances as traffic increases, while elasticity allows capacity to decrease when demand falls. The store must still manage costs such as compute, storage, data transfer, and support where applicable. It should also consider load balancing, redundant resources, backups, monitoring, and deployment across multiple Availability Zones where appropriate.

## 12. Official Learning Resources

* AWS Cloud Practitioner: https://aws.amazon.com/certification/certified-cloud-practitioner/
* AWS Cloud Essentials: https://aws.amazon.com/training/learn-about/cloud-practitioner/
* AWS Cloud Computing: https://aws.amazon.com/what-is-cloud-computing/
* AWS Well-Architected Framework: https://aws.amazon.com/architecture/well-architected/

## 13. Module Completion Checklist

* [ ] Explain cloud computing in your own words.
* [ ] Compare public, private, and hybrid cloud.
* [ ] Distinguish IaaS, PaaS, and SaaS.
* [ ] Explain the AWS Cloud Value Proposition.
* [ ] Compare CapEx and OpEx.
* [ ] Distinguish scalability, elasticity, and high availability.
* [ ] Answer the knowledge-check questions without looking at the solutions.
