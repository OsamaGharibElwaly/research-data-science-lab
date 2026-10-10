# Module 08: AWS Security and Shared Responsibility

## 1. Learning Objectives

* Understand the AWS Shared Responsibility Model.
* Distinguish security of the cloud from security in the cloud.
* Explain the principles of least privilege and defense in depth.
* Understand encryption, data protection, and compliance.
* Identify AWS security services.
* Understand how customers can secure cloud workloads.
* Recognize common security risks and appropriate preventive controls.

## 2. Introduction to AWS Cloud Security

Cloud security involves protecting infrastructure, applications, identities, networks, and data against unauthorized access, misuse, and disruption.

AWS provides security capabilities and services, but customers must configure and use them appropriately.

Security depends on both the AWS services selected and the customer's implementation.

## 3. The AWS Shared Responsibility Model

The Shared Responsibility Model defines how security responsibilities are divided between AWS and its customers.

### AWS Responsibility: Security of the Cloud

AWS is responsible for protecting the infrastructure that runs AWS services.

This includes areas such as:

* Physical data centers.
* Physical servers and storage devices.
* Physical networking infrastructure.
* Facilities and environmental controls.
* Foundational infrastructure used to deliver cloud services.

### Customer Responsibility: Security in the Cloud

Customers are responsible for securing their data, identities, workloads, and configurations according to the services they use.

This can include:

* Data classification and protection.
* Identity and access management.
* Application security.
* Network configuration.
* Operating-system patching where applicable.
* Encryption settings.
* Security monitoring.
* Appropriate backup and recovery practices.

The precise division depends on the service and configuration.

## 4. Shared Responsibility by Service Type

### Amazon EC2: Infrastructure as a Service

Customers generally manage more of the workload stack, including:

* Guest operating system.
* Operating-system patches.
* Applications and installed software.
* Instance-level security configuration.
* Data and permissions.

AWS manages the underlying physical infrastructure and virtualization components.

### Managed Database Services

For services such as Amazon RDS, AWS manages more of the underlying database infrastructure and supported maintenance tasks.

Customers still manage appropriate database access, data protection, configuration, schema design, and application security.

### AWS Lambda: Serverless

AWS manages the underlying execution infrastructure and operating environment.

Customers remain responsible for function code, permissions, data, dependencies, and configuration.

### Key Principle

**Using a managed service changes the division of responsibilities; it does not eliminate the customer's security responsibilities.**

## 5. Principle of Least Privilege

Least privilege means granting users, applications, and services only the permissions they need to perform their required tasks.

### Example

A reporting application needs to read records from a particular S3 bucket but does not need to delete objects or administer the AWS account.

The appropriate permissions should allow the required reads while avoiding unnecessary write, delete, or administrative access.

### Benefits

* Reduces the impact of compromised credentials.
* Limits accidental changes.
* Supports separation of duties.
* Improves security governance.

Permissions should be reviewed regularly and adjusted as requirements change.

## 6. Defense in Depth

Defense in depth uses multiple layers of security rather than depending on a single control.

Possible layers include:

1. Identity and access controls.
2. Network security.
3. Application security.
4. Data encryption.
5. Logging and monitoring.
6. Backup and recovery.
7. Incident response procedures.

**Example:** A database may be protected by private networking, security groups, database authentication, encryption, monitoring, and backups.

If one control fails, other controls may reduce the impact.

## 7. Identity and Access Security

AWS Identity and Access Management (IAM) controls authentication and authorization for supported AWS resources.

Key concepts include:

* Users.
* Groups.
* Roles.
* Policies.
* Temporary credentials.
* Multi-factor authentication (MFA).

### Authentication vs. Authorization

**Authentication:** Verifies an identity.

**Authorization:** Determines which actions that identity is permitted to perform.

For example, signing in with valid credentials authenticates a user, while IAM permissions determine whether the user can read an S3 object.

### Security Best Practices

* Prefer federation and temporary credentials where appropriate.
* Use IAM roles for workloads that need AWS access.
* Enable MFA for privileged human access.
* Avoid unnecessary long-lived access keys.
* Review permissions regularly.
* Protect root-user credentials.

IAM and access management are covered in greater detail in Module 09.

## 8. Data Encryption

Encryption transforms data so it cannot be read without the appropriate decryption capability.

### Encryption at Rest

Protects stored data, such as files, database records, and storage volumes.

Examples include supported encryption options for Amazon S3, Amazon EBS, and Amazon RDS.

### Encryption in Transit

Protects data while it moves between systems, commonly using protocols such as TLS.

Examples include HTTPS connections to web applications and supported encrypted connections between services.

### AWS Key Management Service (AWS KMS)

AWS KMS helps create and manage cryptographic keys used by supported AWS services and applications.

Key access policies and permissions are important because encryption alone does not determine who can access the underlying data.

## 9. Logging, Monitoring, and Threat Detection

### AWS CloudTrail

Records supported AWS account and API activity.

It helps answer questions such as which identity performed an API action and when that activity occurred.

### Amazon CloudWatch

Collects and monitors metrics, logs, and other operational telemetry.

It can support alarms and operational visibility.

### Amazon GuardDuty

Provides managed threat detection using supported data sources and detection capabilities.

### AWS Security Hub

Helps aggregate and manage security findings and evaluate security posture across supported integrations.

### Amazon Inspector

Helps identify certain software vulnerabilities and unintended network exposure in supported workloads.

### AWS Config

Tracks supported resource configuration changes and can evaluate configurations against rules.

These services have different purposes and may be used together.

## 10. Compliance and Governance

Organizations must consider applicable laws, contractual obligations, industry standards, and internal policies.

AWS provides compliance information, reports, and tools that can support customer compliance programs.

However:

* Using AWS does not automatically make a workload compliant.
* Customers remain responsible for their own configurations and processes.
* Compliance requirements vary by workload, industry, and jurisdiction.
* Organizations should verify which AWS services and controls are relevant to their specific obligations.

Official resource: https://aws.amazon.com/compliance/

## 11. Common Security Risks

### Excessive Permissions

Users or applications have more permissions than necessary.

**Mitigation:** Apply least privilege and review IAM policies.

### Publicly Exposed Data

Sensitive resources are unintentionally accessible to the public.

**Mitigation:** Review resource policies, access settings, and public exposure controls.

### Unprotected Credentials

Access keys or passwords are exposed in source code or logs.

**Mitigation:** Use appropriate secrets-management mechanisms, temporary credentials, and credential rotation procedures.

### Unpatched Software

Vulnerable operating systems or applications remain outdated.

**Mitigation:** Establish patch management and vulnerability remediation processes.

### Missing Monitoring

Suspicious activity goes undetected.

**Mitigation:** Configure appropriate logging, monitoring, alerting, and incident response.

### Inadequate Backups

An incident causes data loss without a tested recovery path.

**Mitigation:** Configure backups, retention, access controls, and regular recovery tests.

## 12. Exam-Focused Revision Notes

* AWS manages security of the cloud.
* Customers manage security in the cloud according to the service used.
* EC2 customers manage more of the guest operating system than customers using Lambda.
* Least privilege grants only necessary permissions.
* Defense in depth uses multiple security layers.
* Authentication verifies identity; authorization determines permitted actions.
* Encryption at rest protects stored data.
* Encryption in transit protects data moving between systems.
* AWS KMS supports cryptographic key management.
* CloudTrail records supported account and API activity.
* CloudWatch monitors metrics and logs.
* GuardDuty provides threat detection.
* Security Hub helps manage security findings.
* Inspector helps identify supported vulnerabilities and exposure.
* AWS Config tracks resource configuration changes and evaluates configurations.
* Compliance is a shared effort and depends on the workload and applicable requirements.
* Managed cloud services reduce certain operational responsibilities but do not eliminate customer security obligations.

## 13. Knowledge Check

**Question 1:** Under the AWS Shared Responsibility Model, who is responsible for physical security of AWS data centers?

A. Every individual customer
B. AWS
C. The customer's application developer only
D. The customer's end users

**Answer:** B — AWS is responsible for physical security of its cloud infrastructure.

**Question 2:** A customer runs an application on EC2. Who is generally responsible for patching its guest operating system?

A. AWS in every case
B. The customer
C. Amazon Route 53
D. No one

**Answer:** B — For EC2, customers generally manage the guest operating system and its patching.

**Question 3:** Which principle recommends granting only the permissions needed for a task?

A. Least privilege
B. Unlimited access
C. Public access
D. Shared storage

**Answer:** A — Least privilege limits unnecessary permissions.

**Question 4:** Which service records supported AWS API activity for auditing?

A. AWS CloudTrail
B. Amazon CloudFront
C. Amazon EFS
D. Amazon Lightsail only

**Answer:** A — CloudTrail records supported account and API activity.

**Question 5:** Which service helps detect threats using supported AWS data sources?

A. Amazon GuardDuty
B. Amazon EBS
C. Amazon Route 53 only
D. AWS Budgets

**Answer:** A — GuardDuty provides managed threat detection.

**Question 6:** Which statement about AWS compliance is correct?

A. Every AWS workload is automatically compliant
B. Customers have no compliance responsibilities
C. AWS provides compliance resources, but customers must address their own workload obligations
D. Encryption automatically satisfies every regulation

**Answer:** C — Compliance depends on the customer's workload, configuration, and applicable requirements.

## 14. Practical Exercise

A company runs a customer database on Amazon RDS and a web application on EC2.

Identify at least six security controls it should consider.

### Suggested Solution

1. Use least-privilege IAM permissions.
2. Restrict database access using appropriate network and database controls.
3. Keep the EC2 guest operating system and application software appropriately patched.
4. Enable suitable encryption at rest and in transit.
5. Protect credentials and secrets.
6. Enable appropriate CloudTrail logging and CloudWatch monitoring.
7. Evaluate GuardDuty and other relevant security services.
8. Configure backups and test recovery.
9. Review public access and security group rules.
10. Document incident response and compliance requirements.

## 15. Official Learning Resources

* AWS Shared Responsibility Model: https://aws.amazon.com/compliance/shared-responsibility-model/
* AWS Security: https://aws.amazon.com/security/
* AWS IAM: https://aws.amazon.com/iam/
* AWS KMS: https://aws.amazon.com/kms/
* AWS CloudTrail: https://aws.amazon.com/cloudtrail/
* Amazon GuardDuty: https://aws.amazon.com/guardduty/
* AWS Security Hub: https://aws.amazon.com/security-hub/
* AWS Compliance: https://aws.amazon.com/compliance/

## 16. Module Completion Checklist

* [ ] Explain security of the cloud versus security in the cloud.
* [ ] Compare responsibilities for EC2, managed databases, and Lambda.
* [ ] Apply least privilege and defense in depth.
* [ ] Distinguish authentication and authorization.
* [ ] Explain encryption at rest and in transit.
* [ ] Identify CloudTrail, CloudWatch, GuardDuty, Security Hub, Inspector, and AWS Config.
* [ ] Explain why using AWS does not automatically guarantee compliance.
* [ ] Complete the knowledge check without consulting the answers.
