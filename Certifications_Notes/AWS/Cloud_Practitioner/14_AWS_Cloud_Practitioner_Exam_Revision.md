# Module 14: AWS Cloud Practitioner Exam Revision

## 1. Purpose of This Module

This module consolidates the core concepts needed for the AWS Certified Cloud Practitioner exam.

It is designed for revision after completing the preceding modules. It is not a substitute for checking the current official exam guide, because exam domains, service coverage, and policies may change.

## 2. Understand the Exam Domains

The current exam guide should be your source of truth for the exact domain names, weightings, and objectives.

The exam traditionally focuses on four broad areas:

1. Cloud concepts.
2. Security and compliance.
3. Cloud technology and services.
4. Billing, pricing, and support.

Use the official exam guide to confirm the current percentage assigned to each domain.

### Recommended Revision Strategy

* Start with the domain that has the most objectives or your weakest performance.
* Learn service purpose and use cases before memorizing details.
* Practice distinguishing services that sound similar.
* Review incorrect answers and explain why each distractor is wrong.
* Take timed practice tests only after reviewing the underlying concepts.

## 3. Cloud Concepts

### 3.1 What Is Cloud Computing?

Cloud computing provides on-demand access to computing resources over a network, commonly with usage-based pricing.

Resources may include:

* Compute.
* Storage.
* Databases.
* Networking.
* Analytics.
* Security.
* Application services.

### 3.2 Benefits of Cloud Computing

**Agility:** Resources can be provisioned quickly.

**Elasticity:** Capacity can increase or decrease with demand.

**Pay-as-you-go pricing:** Customers can often pay according to consumption.

**Global reach:** AWS operates infrastructure across multiple geographic locations.

**Managed services:** AWS can operate parts of the underlying infrastructure or service.

**Economies of scale:** A large provider can achieve efficiencies that may be difficult for an individual organization to achieve independently.

### 3.3 Capital Expenditure and Operational Expenditure

Traditional infrastructure often requires substantial upfront capital expenditure (CapEx).

Cloud usage commonly shifts spending toward operational expenditure (OpEx), although the exact accounting treatment depends on the organization and arrangement.

Do not assume that cloud automatically costs less. Costs depend on architecture, usage, data transfer, storage, licensing, and operational choices.

### 3.4 High Availability and Fault Tolerance

* **High availability:** A system is designed to remain accessible despite certain failures.
* **Fault tolerance:** A system can continue operating despite a defined component failure, potentially with little or no interruption.
* **Disaster recovery:** Processes and resources used to restore operations after a major disruption.
* **Scalability:** The ability to handle increased workload by adding capacity.
* **Elasticity:** The ability to adjust capacity dynamically as demand changes.

## 4. AWS Global Infrastructure

### 4.1 Regions

An AWS Region is a separate geographic area containing multiple Availability Zones.

Choose a Region based on factors such as:

* Service availability.
* Latency.
* Regulatory and data-residency requirements.
* Pricing.
* Disaster-recovery requirements.

### 4.2 Availability Zones

An Availability Zone (AZ) consists of one or more discrete data centers with independent infrastructure designed to isolate failures.

Using multiple AZs can improve resilience against failures affecting an individual AZ.

### 4.3 Edge Locations

Edge locations support services such as Amazon CloudFront by bringing content and certain capabilities closer to users.

### 4.4 Key Distinctions

| Concept           | Main purpose                                                    |
| ----------------- | --------------------------------------------------------------- |
| Region            | Geographic deployment area                                      |
| Availability Zone | Failure-isolated infrastructure location within a Region        |
| Edge location     | Supports low-latency content delivery and related edge services |

## 5. AWS Compute Services

### Amazon EC2

Provides virtual servers with configurable compute, memory, storage, and networking.

Typical use cases:

* Hosting applications.
* Running custom software.
* Supporting workloads requiring operating-system control.

### AWS Lambda

Runs code in response to events without requiring the customer to manage the underlying servers.

Typical use cases:

* Event-driven processing.
* Scheduled automation.
* Lightweight APIs and backend tasks.

### Amazon ECS and Amazon EKS

* **Amazon ECS:** Container orchestration service.
* **Amazon EKS:** Managed Kubernetes service.

### AWS Fargate

Provides serverless compute for supported container workloads, including Amazon ECS and Amazon EKS configurations.

### AWS Elastic Beanstalk

Helps deploy and manage applications while AWS handles much of the underlying infrastructure setup and operational configuration.

### AWS Auto Scaling

Helps adjust capacity based on defined conditions or demand.

### Amazon Lightsail

Offers simplified cloud resources for smaller applications and projects.

## 6. AWS Storage Services

### Amazon S3

Object storage for files, backups, data lakes, static assets, and other unstructured data.

### Amazon EBS

Block storage commonly attached to Amazon EC2 instances.

### Amazon EFS

Managed elastic file storage for supported Linux workloads.

### Amazon FSx

Managed file systems for supported file-system technologies and workloads.

### AWS Storage Gateway

Connects on-premises environments with AWS storage services through supported hybrid-storage configurations.

### AWS Backup

Provides centralized backup management for supported AWS services and workloads.

### Amazon S3 Storage Classes

Storage classes differ in access patterns, availability design, retrieval costs, and minimum storage-duration considerations.

Choose based on:

* How frequently data is accessed.
* How quickly it must be retrieved.
* Retention requirements.
* Resilience requirements.
* Total cost.

## 7. AWS Database Services

| Service            | Main purpose                                                                 |
| ------------------ | ---------------------------------------------------------------------------- |
| Amazon RDS         | Managed relational databases                                                 |
| Amazon Aurora      | Relational database compatible with supported MySQL or PostgreSQL interfaces |
| Amazon DynamoDB    | Managed NoSQL key-value and document database                                |
| Amazon Redshift    | Data warehousing and analytics                                               |
| Amazon ElastiCache | In-memory caching                                                            |
| Amazon Neptune     | Graph database                                                               |
| Amazon DocumentDB  | Managed document database compatible with supported MongoDB workloads        |

### Relational vs. NoSQL

**Relational databases** organize data into tables with defined relationships and support SQL.

**NoSQL databases** use data models such as key-value and document structures and may be suited to flexible schemas and particular access patterns.

Select a database according to data structure, query patterns, consistency requirements, scale, and operational needs.

## 8. AWS Networking and Content Delivery

### Amazon VPC

Creates a logically isolated virtual network for AWS resources.

### Subnets

Divide a VPC's IP address range into smaller network segments.

### Internet Gateway

Allows eligible resources in a VPC to communicate with the internet when routing and security rules permit.

### NAT Gateway

Allows resources in private subnets to initiate supported outbound internet connections without making those resources directly reachable through the NAT Gateway.

### Security Groups

Act as stateful virtual firewalls associated with supported resources or network interfaces.

### Network ACLs

Act as stateless network filters at the subnet level.

### Amazon Route 53

Provides DNS and related domain-routing capabilities.

### Amazon CloudFront

A content delivery network (CDN) that caches and delivers content through a global edge network.

### AWS Direct Connect

Provides a dedicated network connection between an organization's network and AWS.

### AWS Site-to-Site VPN

Creates an encrypted VPN connection between an on-premises network and an AWS network.

## 9. Security and Compliance

### 9.1 Shared Responsibility Model

AWS and the customer share security responsibilities.

**AWS is responsible for security of the cloud**, including the underlying physical infrastructure and managed infrastructure components.

**The customer is responsible for security in the cloud**, with the exact responsibilities depending on the service used.

Customer responsibilities may include:

* IAM permissions.
* Data classification.
* Application security.
* Configuration choices.
* Encryption settings.
* Operating-system patching for customer-managed systems.

With managed services, AWS operates more of the underlying infrastructure, but customers retain responsibilities such as access control and appropriate data handling.

### 9.2 IAM

AWS Identity and Access Management controls authentication-related identities and authorization through permissions.

Key concepts:

* Users.
* Groups.
* Roles.
* Policies.
* Least privilege.
* Temporary credentials.
* Multi-factor authentication.

### 9.3 AWS Organizations and SCPs

Organizations centrally manages accounts.

Service control policies restrict the maximum permissions available to identities in affected accounts. They do not grant permissions.

### 9.4 Encryption

* Encryption at rest protects stored data.
* Encryption in transit protects data while moving between systems.
* AWS Key Management Service (AWS KMS) helps create and manage cryptographic keys for supported integrations.

### 9.5 Logging and Threat Detection

| Service           | Main purpose                                                    |
| ----------------- | --------------------------------------------------------------- |
| AWS CloudTrail    | Records account and API activity                                |
| Amazon CloudWatch | Metrics, logs, alarms, and operational monitoring               |
| Amazon GuardDuty  | Threat detection                                                |
| AWS Security Hub  | Centralized security findings and security-posture capabilities |
| Amazon Inspector  | Vulnerability management for supported resources                |
| AWS Config        | Records and evaluates resource configurations                   |
| AWS Artifact      | Access to AWS compliance reports and related agreements         |

Do not confuse monitoring, audit logging, configuration tracking, and threat detection; these are related but different functions.

## 10. Monitoring and Operations

### Amazon CloudWatch

Use CloudWatch to monitor metrics, collect logs, create alarms, and observe operational behavior.

### AWS CloudTrail

Use CloudTrail to investigate who performed an AWS API action, when it occurred, and which identity or service was involved, based on the available event records.

### AWS Config

Use AWS Config to record resource configurations and evaluate compliance against configuration rules.

### AWS Systems Manager

Provides operational tools for supported AWS and hybrid resources, including capabilities for managing instances and automating operational tasks.

### AWS Trusted Advisor

Provides checks and recommendations related to areas such as cost, security, performance, and fault tolerance. Availability of individual checks depends on current AWS terms and account entitlements.

## 11. AWS Application Integration and Analytics

| Service            | Main purpose                                    |
| ------------------ | ----------------------------------------------- |
| Amazon SQS         | Message queuing                                 |
| Amazon SNS         | Pub/sub messaging and notifications             |
| Amazon EventBridge | Event routing and event-driven integration      |
| AWS Step Functions | Workflow orchestration                          |
| AWS Glue           | Data integration and ETL                        |
| Amazon Athena      | SQL queries against supported data in Amazon S3 |
| Amazon Kinesis     | Streaming data services                         |
| Amazon QuickSight  | Business intelligence and visualization         |

### Common Distinctions

* SQS stores messages in a queue for consumers to process.
* SNS distributes messages to subscribed endpoints.
* EventBridge routes events to configured targets.
* Step Functions coordinates steps in workflows.
* Athena queries supported data in S3 using SQL.
* Glue supports data integration and ETL workloads.

## 12. Pricing and Cost Management

### 12.1 Pricing Models

Common EC2 purchasing options include:

* On-Demand Instances.
* Savings Plans.
* Reserved Instances for eligible services and configurations.
* Spot Instances.

The suitability of each option depends on workload predictability, flexibility, interruption tolerance, and commitment requirements.

### 12.2 AWS Free Tier and Offers

AWS free usage offers and eligibility rules can change. Always review the current terms, service limits, and expiration dates.

Do not assume that every AWS service or usage amount is free.

### 12.3 Cost Tools

| Tool                            | Purpose                                   |
| ------------------------------- | ----------------------------------------- |
| AWS Pricing Calculator          | Estimate costs before deployment          |
| AWS Cost Explorer               | Analyze historical and forecasted costs   |
| AWS Budgets                     | Set cost or usage budgets and alerts      |
| AWS Billing and Cost Management | Manage billing information and cost tools |
| Cost and Usage Reports          | Detailed billing and usage data           |

### 12.4 Cost Optimization

Common practices include:

* Right-sizing resources.
* Deleting unused resources.
* Selecting appropriate storage classes.
* Using commitments for suitable predictable workloads.
* Reviewing data-transfer charges.
* Monitoring budgets.
* Tagging resources for cost allocation.
* Using lifecycle policies where appropriate.

## 13. AWS Support and Account Management

* Basic Support provides self-service resources and account/billing assistance.
* Higher support plans offer additional technical support and features.
* AWS Organizations supports multi-account management.
* Consolidated billing combines billing information across accounts.
* AWS Control Tower helps establish and govern a multi-account landing zone.
* AWS re:Post supports community-based learning and troubleshooting.
* The root user should be protected and used sparingly.

Always check current plan features before the exam.

## 14. High-Value Service Comparison Table

| Requirement                               | Service to consider    |
| ----------------------------------------- | ---------------------- |
| Virtual server                            | Amazon EC2             |
| Event-driven serverless code              | AWS Lambda             |
| Object storage                            | Amazon S3              |
| Persistent block storage for EC2          | Amazon EBS             |
| Managed relational database               | Amazon RDS             |
| Managed NoSQL key-value/document database | Amazon DynamoDB        |
| Isolated virtual network                  | Amazon VPC             |
| Global content delivery                   | Amazon CloudFront      |
| DNS and domain routing                    | Amazon Route 53        |
| API activity history                      | AWS CloudTrail         |
| Metrics, logs, and alarms                 | Amazon CloudWatch      |
| Resource configuration tracking           | AWS Config             |
| Threat detection                          | Amazon GuardDuty       |
| Vulnerability management                  | Amazon Inspector       |
| SQL analytics on supported S3 data        | Amazon Athena          |
| Data warehouse                            | Amazon Redshift        |
| Cost estimates                            | AWS Pricing Calculator |
| Historical cost analysis                  | AWS Cost Explorer      |
| Cost alerts                               | AWS Budgets            |
| Multi-account management                  | AWS Organizations      |
| Workflow orchestration                    | AWS Step Functions     |

## 15. Common Exam Traps

1. **CloudTrail vs. CloudWatch:** CloudTrail records API activity; CloudWatch monitors operational data.
2. **S3 vs. EBS:** S3 is object storage; EBS is block storage.
3. **RDS vs. DynamoDB:** RDS is relational; DynamoDB is NoSQL.
4. **Security Groups vs. Network ACLs:** Security groups are stateful; network ACLs are stateless.
5. **Region vs. Availability Zone:** A Region contains multiple AZs.
6. **IAM vs. Organizations:** IAM manages identities and permissions; Organizations manages multiple accounts and organization-level controls.
7. **GuardDuty vs. Inspector:** GuardDuty detects threats; Inspector identifies vulnerabilities in supported resources.
8. **Budgets vs. Cost Explorer:** Budgets helps set thresholds and alerts; Cost Explorer analyzes costs.
9. **SNS vs. SQS:** SNS distributes messages; SQS queues messages.
10. **Shared responsibility:** AWS manages the underlying cloud infrastructure, but customers retain service-dependent security responsibilities.

## 16. Final Revision Checklist

* [ ] I can explain cloud computing and its benefits.
* [ ] I can distinguish Regions, Availability Zones, and edge locations.
* [ ] I know the main compute, storage, database, and networking services.
* [ ] I understand the shared responsibility model.
* [ ] I can distinguish IAM, Organizations, and SCPs.
* [ ] I can distinguish CloudTrail, CloudWatch, and Config.
* [ ] I know the purpose of major security services.
* [ ] I can distinguish AWS pricing and cost tools.
* [ ] I understand the main support-plan categories.
* [ ] I have reviewed the current official exam guide.
* [ ] I have completed timed practice questions and reviewed mistakes.

## 17. Official Exam Resources

* AWS Certified Cloud Practitioner: https://aws.amazon.com/certification/certified-cloud-practitioner/
* AWS Certification Exam Guides: https://aws.amazon.com/certification/certification-prep/
* AWS Skill Builder: https://skillbuilder.aws/
* AWS Documentation: https://docs.aws.amazon.com/
* AWS Pricing Calculator: https://calculator.aws/
* AWS Free Tier: https://aws.amazon.com/free/

**Final recommendation:** Before scheduling the exam, verify the current exam guide, study the listed objectives, and use practice tests to identify weak areas rather than relying on memorized answer patterns.
