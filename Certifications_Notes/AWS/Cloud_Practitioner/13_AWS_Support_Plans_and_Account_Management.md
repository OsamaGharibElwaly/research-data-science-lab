# Module 13: AWS Support Plans and Account Management

## 1. Learning Objectives

By the end of this module, you should be able to:

* Identify the purpose of AWS Support plans.
* Compare AWS Support plan features and use cases.
* Understand AWS account management and account security basics.
* Explain AWS Organizations and consolidated billing.
* Understand AWS Control Tower at a high level.
* Identify the roles of AWS Support, AWS re:Post, and AWS Trusted Advisor.
* Recognize account governance and cost-management best practices.

## 2. AWS Support Plans

AWS Support plans provide different levels of technical assistance, guidance, and operational support.

The available plans and their features can change, so consult the official AWS Support page when preparing for the exam.

### 2.1 Basic Support

Basic Support is included for AWS customers at no additional charge.

Typical features include:

* Customer Service support for account and billing questions.
* Documentation, whitepapers, and technical resources.
* AWS re:Post community access.
* AWS Health Dashboard access.
* Basic checks and recommendations through eligible AWS services.

**Exam focus:** Basic Support is suitable for customers who primarily use self-service resources and do not require paid technical support.

### 2.2 Developer-Oriented Support

Developer-oriented support is intended for customers developing and testing applications on AWS.

It generally provides access to technical guidance through support cases, subject to the plan's terms and response targets.

Use cases include:

* Developing a new application.
* Testing AWS services.
* Getting guidance on development-related issues.

### 2.3 Business-Oriented Support

Business-oriented support is designed for production workloads that need more comprehensive technical assistance.

Typical capabilities may include:

* Technical support for production workloads.
* Guidance for a wider range of AWS services.
* Access to designated support features.
* Support for operational issues and troubleshooting.

**Exam focus:** Production workloads that require faster technical assistance generally need a higher support tier than Basic Support.

### 2.4 Enterprise-Level Support

Enterprise-level plans target organizations with critical workloads and more demanding operational requirements.

Depending on the selected plan, features may include:

* Proactive guidance.
* Technical account management or designated account-management resources.
* Architecture and operational reviews.
* Strategic planning and escalation assistance.
* Enhanced response targets.

Do not assume that every enterprise feature is included in every plan. Verify the current plan comparison.

## 3. Choosing a Support Plan

The correct support plan depends on business requirements rather than company size alone.

| Requirement                                       | General direction          |
| ------------------------------------------------- | -------------------------- |
| Self-service learning and basic account help      | Basic Support              |
| Application development and testing               | Developer-oriented support |
| Production workload technical support             | Business-oriented support  |
| Mission-critical workloads and proactive guidance | Enterprise-level support   |

### Scenario

A small company runs a customer-facing application on AWS. Its application is already in production, and outages directly affect revenue.

The company needs reliable technical support beyond documentation and community forums.

**Reasoning:** A business-oriented or higher support plan may be appropriate, depending on the required response targets and additional features.

## 4. AWS Account Management

An AWS account is a fundamental boundary for resources, permissions, billing, and administration.

Important account-management practices include:

* Protect the root user.
* Enable multi-factor authentication (MFA) for privileged identities.
* Avoid routine use of root credentials.
* Create individual identities and assign appropriate permissions.
* Monitor account activity.
* Review billing alerts and unexpected charges.
* Keep account contact information current.
* Establish procedures for account recovery and employee offboarding.

### 4.1 The Root User

The root user has extensive privileges over an AWS account.

Best practices include:

* Use a strong, unique password.
* Enable MFA.
* Do not create root access keys unless an exceptional, justified use case requires them.
* Use root credentials only for tasks that specifically require them.
* Protect recovery email and contact information.

**Exam focus:** Use least-privilege identities for daily administration instead of the root user.

## 5. AWS Organizations

AWS Organizations helps centrally manage multiple AWS accounts.

Key capabilities include:

* Grouping accounts into organizational units (OUs).
* Applying service control policies (SCPs).
* Managing consolidated billing.
* Separating environments or business units into accounts.
* Supporting centralized governance.

### 5.1 Organizational Units

An OU is a logical grouping of AWS accounts.

Example structure:

* Root

  * Production OU

    * Production Account
    * Disaster Recovery Account
  * Development OU

    * Development Account
    * Testing Account

This structure helps organize permissions, billing, and governance.

### 5.2 Service Control Policies

SCPs define the maximum permissions available to principals in member accounts within an organization.

Important distinction:

**An SCP does not grant permissions.** It establishes permission boundaries at the organization level. IAM policies must still grant the permissions required for an action.

SCPs can help prevent certain actions across accounts, such as using services or regions that an organization has prohibited.

## 6. Consolidated Billing

Consolidated billing combines billing information for multiple AWS accounts under an organization.

Benefits may include:

* One consolidated bill.
* Centralized cost visibility.
* Easier allocation of costs by account.
* Potential access to volume-based pricing benefits, depending on service rules and eligibility.

Consolidated billing does not mean that all accounts must share the same resources or application environments.

Organizations can maintain separate accounts while managing costs centrally.

## 7. AWS Control Tower

AWS Control Tower helps establish and govern a multi-account AWS environment based on recommended landing-zone practices.

It can help organizations:

* Set up a multi-account environment.
* Apply governance controls.
* Manage account provisioning.
* Establish guardrails.
* Improve visibility across accounts.

**Exam distinction:**

* **AWS Organizations:** Centrally manages multiple accounts and organization-level policies.
* **AWS Control Tower:** Helps set up and govern a multi-account environment using an integrated landing-zone approach.

## 8. AWS Support and Community Resources

### AWS re:Post

AWS re:Post is an online community where users can ask questions, find answers, and learn from AWS experts and other customers.

It is useful for self-service troubleshooting and knowledge sharing.

### AWS Health Dashboard

AWS Health provides information about AWS service events that may affect resources or accounts.

It helps customers understand relevant service disruptions, scheduled changes, and other operational events.

### AWS Trusted Advisor

AWS Trusted Advisor provides checks and recommendations that can help improve areas such as:

* Cost optimization.
* Security.
* Fault tolerance.
* Performance.
* Service quotas and operational considerations.

The checks available depend on the service, account, and support entitlements.

**Exam focus:** Trusted Advisor provides recommendations; it does not replace an organization's responsibility to assess and implement them.

## 9. Account Governance Best Practices

A well-governed AWS environment should include:

1. A documented account structure.
2. Strong authentication for privileged users.
3. Least-privilege IAM permissions.
4. Centralized logging and monitoring where appropriate.
5. Billing alerts and cost reviews.
6. Defined ownership of resources.
7. Account recovery and incident-response procedures.
8. Periodic permission and configuration reviews.
9. Clear separation of production and non-production environments when appropriate.

## 10. Exam Revision Notes

Remember these distinctions:

* Basic Support provides self-service resources and account/billing assistance.
* Higher support plans provide additional technical assistance and features.
* AWS Organizations manages multiple accounts.
* SCPs restrict the maximum available permissions; they do not grant permissions.
* Consolidated billing centralizes billing across accounts.
* Control Tower helps establish and govern a multi-account landing zone.
* Trusted Advisor offers recommendations and checks.
* The root user should be protected and used sparingly.
* MFA strengthens authentication but does not replace authorization policies.

## 11. Knowledge Check

### Question 1

Which AWS service helps centrally manage multiple AWS accounts?

A. Amazon CloudFront
B. AWS Organizations
C. Amazon Route 53
D. Amazon S3

**Answer: B. AWS Organizations**

Explanation: Organizations provides centralized account management and organization-level policies.

### Question 2

What is the primary purpose of an SCP?

A. To grant administrator permissions to every user
B. To create IAM users automatically
C. To define the maximum permissions available within an organization
D. To encrypt every object in Amazon S3

**Answer: C. To define the maximum permissions available within an organization**

Explanation: An SCP restricts the permissions that can be used; it does not grant permissions.

### Question 3

Which feature combines billing information across multiple AWS accounts?

A. Consolidated billing
B. Amazon CloudWatch
C. AWS CloudTrail
D. Amazon Inspector

**Answer: A. Consolidated billing**

### Question 4

Which service helps establish and govern a multi-account AWS environment?

A. AWS Control Tower
B. Amazon DynamoDB
C. AWS Glue
D. Amazon EBS

**Answer: A. AWS Control Tower**

### Question 5

What is the recommended approach to using the AWS root user?

A. Use it for every daily administrative task
B. Share its credentials with the team
C. Use it only for tasks requiring root access and protect it carefully
D. Store its password in source code

**Answer: C. Use it only for tasks requiring root access and protect it carefully**

## 12. Practical Exercise

Design a simple account structure for a small organization.

Requirements:

* Separate production and development resources.
* Centralize billing.
* Restrict certain actions across member accounts.
* Protect privileged access.

Your design should include:

1. An AWS Organization.
2. Production and Development OUs or equivalent account groupings.
3. Separate AWS accounts where appropriate.
4. SCPs for organization-level restrictions.
5. MFA and least-privilege IAM access.
6. Consolidated billing and cost monitoring.

Write a short explanation of why each component is needed.

## 13. Official Resources

* AWS Support: https://aws.amazon.com/premiumsupport/
* AWS Organizations: https://aws.amazon.com/organizations/
* AWS Control Tower: https://aws.amazon.com/controltower/
* AWS Trusted Advisor: https://aws.amazon.com/premiumsupport/technology/trusted-advisor/
* AWS Health: https://health.aws.amazon.com/health/home
* AWS re:Post: https://repost.aws/
* AWS Shared Responsibility Model: https://aws.amazon.com/compliance/shared-responsibility-model/

## 14. Completion Checklist

* [ ] I can distinguish the main AWS Support plan categories.
* [ ] I understand root-user security best practices.
* [ ] I can explain AWS Organizations and OUs.
* [ ] I understand that SCPs do not grant permissions.
* [ ] I can explain consolidated billing.
* [ ] I understand the purpose of AWS Control Tower.
* [ ] I can identify the purpose of Trusted Advisor and AWS Health.
* [ ] I completed the knowledge check and practical exercise.
