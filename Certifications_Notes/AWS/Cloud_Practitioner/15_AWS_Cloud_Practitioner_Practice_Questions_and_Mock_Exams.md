# Module 15: AWS Cloud Practitioner Practice Questions and Mock Exams

## 1. Purpose

This module provides original practice questions for revising AWS Cloud Practitioner concepts.

These questions are for learning and self-assessment. They are not official AWS exam questions and do not guarantee the exact content of the live exam.

## 2. How to Use This Module

1. Answer each question before reading the explanation.
2. Record the questions you answered incorrectly.
3. Explain why the correct option is best.
4. Explain why each distractor is incorrect.
5. Revisit the related module when you identify a knowledge gap.
6. Repeat the test later without looking at the answers.

Suggested practice targets:

* Initial review: understand the reasoning behind each answer.
* Second attempt: answer without notes.
* Final preparation: complete a timed mock exam using the current exam format and official guidance.

---

# Part A: Practice Questions

## Question 1: Cloud Computing

A company wants to provision computing resources quickly and pay according to usage instead of purchasing physical servers in advance.

Which cloud benefit best matches this requirement?

A. Fixed capital expenditure
B. On-demand resources and usage-based pricing
C. Elimination of every operational cost
D. Guaranteed zero downtime

**Correct answer: B**

**Explanation:** Cloud computing allows customers to provision resources on demand and use pricing models based on consumption. It does not eliminate all costs or guarantee zero downtime.

## Question 2: AWS Global Infrastructure

A company wants to deploy an application across multiple isolated locations within one AWS geographic area to improve availability.

Which infrastructure concept should it consider?

A. Multiple Availability Zones
B. A single edge location
C. Multiple IAM users
D. A single S3 bucket

**Correct answer: A**

**Explanation:** Deploying across multiple Availability Zones can improve resilience against failures affecting an individual AZ.

## Question 3: Virtual Servers

A team needs a virtual server with control over the operating system and installed software.

Which service is most appropriate?

A. Amazon S3
B. Amazon EC2
C. Amazon Route 53
D. Amazon SNS

**Correct answer: B**

**Explanation:** EC2 provides configurable virtual compute instances.

## Question 4: Serverless Compute

An application needs to execute a small function when an object is uploaded to Amazon S3. The team wants to avoid managing servers for that function.

Which service is the best fit?

A. AWS Lambda
B. Amazon EBS
C. Amazon Redshift
D. AWS Direct Connect

**Correct answer: A**

**Explanation:** Lambda supports event-driven execution and can be integrated with S3 events.

## Question 5: Object Storage

A company needs durable object storage for documents, images, and backups.

Which service should it consider first?

A. Amazon EBS
B. Amazon S3
C. Amazon EC2
D. Amazon VPC

**Correct answer: B**

**Explanation:** Amazon S3 is AWS object storage.

## Question 6: Block Storage

An application running on an EC2 instance needs block storage for a supported operating-system or application volume.

Which service is appropriate?

A. Amazon EBS
B. Amazon CloudFront
C. Amazon Route 53
D. Amazon SNS

**Correct answer: A**

**Explanation:** EBS provides block storage for supported EC2 workloads.

## Question 7: Relational Databases

A company wants a managed relational database service and does not want to manage the underlying database infrastructure entirely by itself.

Which service should it consider?

A. Amazon DynamoDB
B. Amazon RDS
C. Amazon CloudFront
D. Amazon SQS

**Correct answer: B**

**Explanation:** Amazon RDS provides managed relational database capabilities.

## Question 8: NoSQL Databases

An application requires a managed NoSQL key-value and document database.

Which service is the best match?

A. Amazon DynamoDB
B. Amazon RDS
C. Amazon Redshift
D. Amazon EFS

**Correct answer: A**

**Explanation:** DynamoDB is a managed NoSQL database service.

## Question 9: Virtual Networking

Which service provides a logically isolated virtual network for AWS resources?

A. AWS IAM
B. Amazon VPC
C. Amazon S3
D. AWS Artifact

**Correct answer: B**

**Explanation:** Amazon VPC lets customers define a virtual network, including IP ranges, subnets, and routing.

## Question 10: Content Delivery

A media company wants to deliver cached content to users through a global edge network to reduce latency.

Which service should it consider?

A. Amazon CloudFront
B. Amazon EBS
C. AWS Organizations
D. AWS Config

**Correct answer: A**

**Explanation:** CloudFront is AWS's content delivery network.

## Question 11: DNS

Which AWS service provides DNS and domain-routing capabilities?

A. Amazon Route 53
B. Amazon SQS
C. Amazon Inspector
D. AWS Lambda

**Correct answer: A**

**Explanation:** Route 53 provides DNS and related routing functionality.

## Question 12: Identity and Permissions

A company wants to grant a user permission to read objects in a specific S3 bucket without granting unnecessary privileges.

Which service should it use to manage AWS identity permissions?

A. AWS IAM
B. Amazon CloudFront
C. Amazon Redshift
D. AWS Budgets

**Correct answer: A**

**Explanation:** IAM manages identities and permissions. The policy should follow least privilege.

## Question 13: Shared Responsibility

Which statement best describes the AWS Shared Responsibility Model?

A. AWS is responsible for every customer configuration
B. Customers are responsible for the physical security of AWS data centers
C. AWS and customers have different, service-dependent security responsibilities
D. Customers have no security responsibilities when using managed services

**Correct answer: C**

**Explanation:** AWS manages security of the cloud, while customers retain responsibilities for security in the cloud. The exact division depends on the service.

## Question 14: API Activity

An administrator wants to investigate which identity performed an AWS API action.

Which service is most directly relevant?

A. AWS CloudTrail
B. Amazon CloudFront
C. Amazon EFS
D. AWS Pricing Calculator

**Correct answer: A**

**Explanation:** CloudTrail records AWS account and API activity.

## Question 15: Operational Monitoring

A team wants to monitor metrics, collect logs, and create alarms when a metric crosses a threshold.

Which service is appropriate?

A. Amazon CloudWatch
B. AWS Artifact
C. Amazon Route 53
D. AWS Organizations

**Correct answer: A**

**Explanation:** CloudWatch provides monitoring capabilities including metrics, logs, and alarms.

## Question 16: Threat Detection

A security team wants a service that helps detect suspicious activity and potential threats in its AWS environment.

Which service should it consider?

A. Amazon GuardDuty
B. Amazon EBS
C. AWS Pricing Calculator
D. Amazon QuickSight

**Correct answer: A**

**Explanation:** GuardDuty provides threat detection capabilities.

## Question 17: Vulnerability Management

A company wants to identify software vulnerabilities in supported compute workloads and other supported resources.

Which service is most relevant?

A. Amazon Inspector
B. Amazon SNS
C. AWS Budgets
D. Amazon Route 53

**Correct answer: A**

**Explanation:** Inspector supports vulnerability management for eligible resources.

## Question 18: Cost Estimation

Before deploying a new architecture, a team wants to estimate its expected AWS costs.

Which tool should it use?

A. AWS Pricing Calculator
B. AWS CloudTrail
C. AWS Config
D. Amazon Inspector

**Correct answer: A**

**Explanation:** The Pricing Calculator estimates costs based on planned services and usage assumptions.

## Question 19: Cost Analysis

A finance team wants to examine historical AWS spending and identify cost trends.

Which tool is the best fit?

A. AWS Cost Explorer
B. Amazon EKS
C. AWS IAM
D. Amazon EFS

**Correct answer: A**

**Explanation:** Cost Explorer helps analyze historical and forecasted costs.

## Question 20: Budget Alerts

A company wants to configure a budget and receive alerts when spending or usage approaches a defined threshold.

Which service should it use?

A. AWS Budgets
B. Amazon CloudFront
C. AWS Lambda only
D. Amazon DynamoDB

**Correct answer: A**

**Explanation:** AWS Budgets supports cost and usage budgets with alerting capabilities.

## Question 21: Multi-Account Management

A large organization wants to centrally manage multiple AWS accounts.

Which service is most appropriate?

A. AWS Organizations
B. Amazon Athena
C. Amazon EBS
D. Amazon Kinesis

**Correct answer: A**

**Explanation:** AWS Organizations provides centralized multi-account management.

## Question 22: Organization-Level Restrictions

An organization wants to restrict certain actions across member accounts, even when an individual IAM policy might otherwise allow them.

Which mechanism can help define the maximum permissions available within those accounts?

A. Service control policies
B. Amazon CloudFront distributions
C. S3 lifecycle rules
D. CloudWatch dashboards

**Correct answer: A**

**Explanation:** SCPs define organization-level permission boundaries. They do not grant permissions.

## Question 23: Message Queuing

A system needs to decouple application components by storing messages until consumers process them.

Which service is most appropriate?

A. Amazon SQS
B. Amazon CloudFront
C. AWS Artifact
D. Amazon Route 53

**Correct answer: A**

**Explanation:** SQS provides managed message queuing.

## Question 24: Notifications and Pub/Sub

A system needs to publish a message and distribute it to subscribed endpoints.

Which service should it consider?

A. Amazon SNS
B. Amazon EBS
C. Amazon VPC
D. AWS Config

**Correct answer: A**

**Explanation:** SNS supports pub/sub messaging and notifications.

## Question 25: SQL Analytics

A data analyst wants to run SQL queries against supported data stored in Amazon S3 without managing database servers for the query engine.

Which service is most appropriate?

A. Amazon Athena
B. Amazon EBS
C. AWS IAM
D. Amazon Route 53

**Correct answer: A**

**Explanation:** Athena supports SQL querying of data in S3 without requiring the analyst to provision traditional database servers.

## Question 26: Managed Kubernetes

A company wants a managed Kubernetes service on AWS.

Which service should it consider?

A. Amazon EKS
B. Amazon S3
C. Amazon RDS only
D. AWS Budgets

**Correct answer: A**

**Explanation:** Amazon EKS is AWS's managed Kubernetes service.

## Question 27: Container Compute

A team wants to run supported containers without managing the underlying servers.

Which option is relevant?

A. AWS Fargate
B. Amazon Route 53
C. AWS Artifact
D. AWS Organizations

**Correct answer: A**

**Explanation:** Fargate provides serverless compute for supported container workloads.

## Question 28: Configuration Tracking

An organization wants to track resource configuration changes and evaluate resources against configuration rules.

Which service is the best fit?

A. AWS Config
B. Amazon CloudFront
C. Amazon SQS
D. AWS Pricing Calculator

**Correct answer: A**

**Explanation:** AWS Config records and evaluates resource configurations.

## Question 29: Compliance Reports

A compliance officer needs access to AWS compliance reports and related agreements.

Which service should the officer investigate?

A. AWS Artifact
B. Amazon EFS
C. Amazon EC2
D. Amazon SNS

**Correct answer: A**

**Explanation:** AWS Artifact provides access to eligible AWS compliance reports and agreements.

## Question 30: Cloud Migration and Hybrid Connectivity

A company wants a dedicated network connection between its premises and AWS.

Which service should it consider?

A. AWS Direct Connect
B. Amazon CloudFront
C. Amazon S3 Glacier storage classes only
D. Amazon DynamoDB

**Correct answer: A**

**Explanation:** Direct Connect provides dedicated network connectivity between an organization's network and AWS.

---

# Part B: Mock Exam 1

## Instructions

* Answer all questions before checking the key.
* Choose one answer unless the question explicitly says otherwise.
* Suggested practice time: 20–25 minutes for this short mock exam.
* This is a learning exercise, not an official exam-length simulation.

### Question 1

Which benefit allows a company to increase or decrease resources as demand changes?

A. Elasticity
B. Fixed capacity
C. Manual procurement only
D. Capital expenditure

### Question 2

Which AWS component is designed to help isolate failures within a Region?

A. Availability Zone
B. IAM group
C. S3 prefix
D. Billing alert

### Question 3

Which service provides managed object storage?

A. Amazon S3
B. Amazon EC2
C. Amazon VPC
D. Amazon RDS

### Question 4

Which service is primarily used for API activity history?

A. AWS CloudTrail
B. Amazon CloudWatch
C. AWS Budgets
D. AWS Trusted Advisor

### Question 5

Which service helps manage identities and permissions?

A. AWS IAM
B. Amazon CloudFront
C. Amazon Redshift
D. Amazon Athena

### Question 6

Which AWS service provides a managed relational database?

A. Amazon RDS
B. Amazon SQS
C. Amazon Route 53
D. Amazon EFS

### Question 7

Which service provides global content delivery?

A. Amazon CloudFront
B. Amazon EBS
C. AWS Organizations
D. Amazon Inspector

### Question 8

Which service can help detect threats?

A. Amazon GuardDuty
B. AWS Pricing Calculator
C. Amazon EFS
D. Amazon Lightsail only

### Question 9

Which tool helps estimate the cost of a planned AWS architecture?

A. AWS Pricing Calculator
B. AWS CloudTrail
C. Amazon Inspector
D. AWS Artifact

### Question 10

Which service helps centrally manage multiple AWS accounts?

A. AWS Organizations
B. Amazon Athena
C. Amazon EBS
D. Amazon SNS

### Question 11

Which service is most suitable for a managed NoSQL key-value database?

A. Amazon DynamoDB
B. Amazon RDS
C. Amazon Redshift
D. Amazon EFS

### Question 12

Which service supports monitoring metrics, logs, and alarms?

A. Amazon CloudWatch
B. AWS Organizations
C. AWS Artifact
D. Amazon Route 53

### Question 13

Which statement about SCPs is correct?

A. They grant all permissions automatically
B. They define the maximum permissions available within affected accounts
C. They replace all IAM policies
D. They encrypt all stored data

### Question 14

Which service is designed for managed Kubernetes?

A. Amazon EKS
B. Amazon S3
C. AWS Budgets
D. Amazon Route 53

### Question 15

Which service supports SQL queries against supported data in Amazon S3?

A. Amazon Athena
B. Amazon EBS
C. AWS IAM
D. Amazon CloudFront

### Mock Exam 1 Answer Key

1. **A — Elasticity:** Capacity adjusts to changing demand.
2. **A — Availability Zone:** AZs provide failure isolation within a Region.
3. **A — Amazon S3:** Object storage.
4. **A — AWS CloudTrail:** Records account and API activity.
5. **A — AWS IAM:** Manages identities and permissions.
6. **A — Amazon RDS:** Managed relational database service.
7. **A — Amazon CloudFront:** Global content delivery network.
8. **A — Amazon GuardDuty:** Threat detection.
9. **A — AWS Pricing Calculator:** Estimates planned costs.
10. **A — AWS Organizations:** Multi-account management.
11. **A — Amazon DynamoDB:** Managed NoSQL database.
12. **A — Amazon CloudWatch:** Metrics, logs, and alarms.
13. **B — Maximum permissions:** SCPs restrict available permissions but do not grant them.
14. **A — Amazon EKS:** Managed Kubernetes.
15. **A — Amazon Athena:** SQL analytics for supported S3 data.

---

# Part C: Mock Exam 2

## Instructions

These questions focus on distinguishing similar AWS services and selecting services based on scenarios.

### Question 1

A company has an EC2 application that requires persistent block storage. Which service should it consider?

A. Amazon EBS
B. Amazon S3
C. Amazon CloudFront
D. Amazon SNS

### Question 2

A team wants to run code in response to an event without provisioning a server for the function.

A. AWS Lambda
B. Amazon EBS
C. Amazon Route 53
D. AWS Artifact

### Question 3

Which statement best describes the AWS Shared Responsibility Model?

A. Customers are never responsible for security
B. AWS and customers have different responsibilities depending on the service
C. AWS customers secure the physical data centers
D. AWS is responsible for every customer-created IAM policy

### Question 4

Which service helps track resource configuration history and evaluate configuration rules?

A. AWS Config
B. Amazon CloudFront
C. Amazon SNS
D. AWS Pricing Calculator

### Question 5

A team wants to publish a notification to multiple subscribers.

A. Amazon SNS
B. Amazon EBS
C. Amazon RDS
D. AWS Direct Connect

### Question 6

A team needs a queue to decouple producers from consumers.

A. Amazon SQS
B. Amazon Route 53
C. Amazon CloudFront
D. Amazon Redshift

### Question 7

Which service helps analyze AWS spending trends?

A. AWS Cost Explorer
B. AWS CloudTrail
C. Amazon GuardDuty
D. Amazon Inspector

### Question 8

Which service offers managed file storage for supported Linux workloads?

A. Amazon EFS
B. Amazon SNS
C. AWS IAM
D. Amazon CloudFront

### Question 9

Which service helps create and manage cryptographic keys for supported AWS integrations?

A. AWS Key Management Service (AWS KMS)
B. Amazon Route 53
C. AWS Organizations
D. Amazon Athena

### Question 10

A company wants to establish a governed multi-account landing zone.

A. AWS Control Tower
B. Amazon S3
C. Amazon SQS
D. Amazon DynamoDB

### Question 11

Which service provides a managed data warehouse?

A. Amazon Redshift
B. Amazon EBS
C. Amazon Route 53
D. AWS IAM

### Question 12

Which statement about Security Groups and Network ACLs is correct?

A. Both are stateless
B. Security Groups are stateful; Network ACLs are stateless
C. Security Groups are used only for DNS
D. Network ACLs grant IAM permissions

### Question 13

Which service helps identify vulnerabilities in supported workloads?

A. Amazon Inspector
B. Amazon CloudFront
C. Amazon SNS
D. AWS Budgets

### Question 14

Which pricing approach may suit a flexible workload that can tolerate interruptions?

A. Spot Instances
B. A mandatory Dedicated Host for every workload
C. On-Demand Instances only
D. A fixed monthly storage bucket

### Question 15

Which statement about the root user is the best practice?

A. Use root credentials for all daily tasks
B. Share root credentials with all administrators
C. Protect root access and use it only when necessary
D. Store root credentials in application code

### Mock Exam 2 Answer Key

1. **A — Amazon EBS:** Block storage for supported EC2 workloads.
2. **A — AWS Lambda:** Event-driven serverless compute.
3. **B — Shared responsibilities:** The division depends on the service and configuration.
4. **A — AWS Config:** Configuration history and evaluation.
5. **A — Amazon SNS:** Pub/sub notifications.
6. **A — Amazon SQS:** Managed message queuing.
7. **A — AWS Cost Explorer:** Cost analysis.
8. **A — Amazon EFS:** Managed file storage.
9. **A — AWS KMS:** Cryptographic key management.
10. **A — AWS Control Tower:** Multi-account landing-zone setup and governance.
11. **A — Amazon Redshift:** Data warehousing.
12. **B — Stateful vs. stateless:** Security Groups are stateful; Network ACLs are stateless.
13. **A — Amazon Inspector:** Vulnerability management for supported resources.
14. **A — Spot Instances:** Can offer lower prices for interruptible workloads.
15. **C — Protect root access:** Use root credentials sparingly and secure them.

---

# Part D: Scenario-Based Revision

## Scenario 1: Unexpected Spending

A developer launches several test instances and forgets to stop them. The team wants to detect unexpected spending and receive alerts.

**Recommended approach:**

* Use AWS Budgets to configure spending thresholds and alerts.
* Use Cost Explorer to analyze costs and trends.
* Review running resources and remove unused resources when safe.
* Consider tagging resources to improve cost allocation.

## Scenario 2: Investigating an Unauthorized API Action

An administrator notices an unexpected change to an AWS resource.

**Recommended approach:**

* Use CloudTrail to investigate the API activity.
* Identify the available event details, including the principal and event time.
* Review relevant permissions and account-security controls.
* Use CloudWatch or other monitoring systems where relevant.
* Follow the organization's incident-response procedures.

## Scenario 3: A Highly Available Web Application

A company wants its web application to remain available if one Availability Zone experiences a disruption.

**Possible design considerations:**

* Deploy application resources across multiple Availability Zones.
* Use an appropriate load-balancing configuration.
* Design data storage and databases for the required availability.
* Monitor the application and test recovery procedures.

No single service automatically guarantees that the entire application will remain available; the architecture must be designed for resilience.

## Scenario 4: Restricting Access Across Accounts

A company wants to prevent member accounts from using certain services.

**Recommended approach:**

* Use AWS Organizations to manage the accounts.
* Consider SCPs to define organization-level permission restrictions.
* Configure IAM policies to grant the required permissions.
* Test restrictions carefully before applying them broadly.

Remember: SCPs do not grant permissions.

## Scenario 5: Moving Data to the Cloud

A company wants to migrate files and databases from an on-premises environment.

**Planning considerations:**

* Determine data volume and transfer speed requirements.
* Evaluate network connectivity options, including VPN and Direct Connect.
* Choose suitable storage and database services.
* Plan security, data transfer costs, validation, and rollback.
* Use migration services and tools appropriate to the specific workload.

---

# Part E: Score Tracking

Use this table to record your performance across attempts.

| Attempt            | Correct | Total | Percentage | Main weaknesses |
| ------------------ | ------: | ----: | ---------: | --------------- |
| Practice Questions |         |    30 |            |                 |
| Mock Exam 1        |         |    15 |            |                 |
| Mock Exam 2        |         |    15 |            |                 |
| Retake             |         |       |            |                 |

Calculate your score as:

$$
\text{Score (\%)} = \frac{\text{Correct Answers}}{\text{Total Questions}} \times 100
$$

A strong practice score is useful, but it does not guarantee exam success. Review incorrect answers and make sure you understand the service choices.

## Error Log Template

For every incorrect answer, record:

* **Question number:**
* **My selected answer:**
* **Correct answer:**
* **Why I chose incorrectly:**
* **Concept to review:**
* **Related AWS service:**
* **Review date:**

## Final Exam-Day Checklist

* [ ] I reviewed the current official exam guide.
* [ ] I can explain the major cloud-computing benefits.
* [ ] I can distinguish the main AWS compute, storage, database, and networking services.
* [ ] I understand the shared responsibility model.
* [ ] I can distinguish IAM, Organizations, and SCPs.
* [ ] I can distinguish CloudTrail, CloudWatch, and AWS Config.
* [ ] I understand cost estimation, cost analysis, and budget alerts.
* [ ] I reviewed the differences between similar services.
* [ ] I completed both mock exams and reviewed my errors.
* [ ] I understand that these practice questions are original study material, not official exam questions.

## Official Resources

* AWS Certified Cloud Practitioner: https://aws.amazon.com/certification/certified-cloud-practitioner/
* AWS Certification Exam Guides: https://aws.amazon.com/certification/certification-prep/
* AWS Skill Builder: https://skillbuilder.aws/
* AWS Documentation: https://docs.aws.amazon.com/
* AWS Pricing Calculator: https://calculator.aws/
