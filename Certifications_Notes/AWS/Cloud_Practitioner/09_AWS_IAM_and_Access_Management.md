# Module 09: AWS IAM and Access Management

## 1. Learning Objectives

* Understand AWS Identity and Access Management (IAM).
* Distinguish IAM users, groups, roles, and policies.
* Explain authentication, authorization, and least privilege.
* Understand multi-factor authentication (MFA).
* Learn how IAM policies control access to AWS resources.
* Understand temporary credentials and IAM roles.
* Recognize root-user security best practices.

## 2. What Is AWS IAM?

AWS Identity and Access Management (IAM) is a service that helps control who can access AWS resources and what actions they can perform.

IAM supports authentication and authorization for AWS environments.

### Main IAM Components

* **Users:** Identities that can represent individual people or applications requiring long-term credentials.
* **Groups:** Collections of IAM users to which permissions can be assigned through group policies.
* **Roles:** Identities that provide permissions to trusted principals that assume the roles.
* **Policies:** Documents defining permissions.
* **MFA:** An additional authentication factor used to strengthen account security.

IAM is a global AWS service for its core identity and access management resources.

## 3. Authentication vs. Authorization

### Authentication

Authentication verifies an identity.

Examples include signing in with credentials or completing an MFA challenge.

### Authorization

Authorization determines which actions an authenticated or otherwise trusted identity is permitted to perform.

**Example:** A user successfully signs in to AWS but cannot terminate EC2 instances because the applicable permissions do not allow that action.

Remember:

* Authentication = Who are you?
* Authorization = What are you allowed to do?

## 4. IAM Users

An IAM user is an identity created within an AWS account.

A user may have supported credentials for accessing AWS, such as console credentials or programmatic access keys.

### Example

A company creates an IAM user for an administrator who needs access to specific AWS services.

### Best Practices

* Avoid creating unnecessary long-term credentials.
* Apply least privilege.
* Require MFA for appropriate human access.
* Review unused credentials and permissions.
* Prefer federation and temporary credentials for workforce access when appropriate.

For many workforce scenarios, AWS recommends centralized identity management rather than creating separate long-lived IAM users for everyone.

## 5. IAM Groups

An IAM group is a collection of IAM users.

Groups help administrators manage permissions for users with similar responsibilities.

### Example

An organization creates:

* Developers group.
* Operations group.
* Read-only auditing group.

Each group receives policies appropriate to its responsibilities.

Groups contain IAM users; IAM roles are not members of IAM groups.

## 6. IAM Roles

An IAM role is an identity with permissions that trusted principals can assume.

Roles can provide temporary credentials instead of requiring long-term access keys.

### Common Use Cases

* Allowing EC2 applications to access S3.
* Allowing Lambda functions to access required AWS services.
* Granting cross-account access.
* Supporting federated workforce access.
* Allowing supported external identities to access AWS resources.

### Example: EC2 Accessing S3

An application running on EC2 needs to read objects from an S3 bucket.

Instead of embedding permanent access keys in the application, an administrator attaches an appropriate IAM role to the instance.

The application obtains temporary credentials through the supported AWS credential mechanism.

This reduces the risk of exposed long-term credentials.

## 7. IAM Policies

An IAM policy is a document that defines permissions.

Policies are commonly written in JSON and specify which actions are allowed or denied on which resources, potentially subject to conditions.

### Main Policy Elements

* `Version`: The policy language version.
* `Statement`: One or more permission statements.
* `Effect`: `Allow` or `Deny`.
* `Action`: The API actions covered by the statement.
* `Resource`: The resources to which the statement applies.
* `Condition`: Optional requirements that must be satisfied.

### Example Policy

The following illustrative identity-based policy allows listing a particular S3 bucket and reading objects in that bucket.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket"
      ],
      "Resource": "arn:aws:s3:::example-training-bucket"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject"
      ],
      "Resource": "arn:aws:s3:::example-training-bucket/*"
    }
  ]
}
```

The bucket name is illustrative and must be replaced with the intended resource.

## 8. Types of IAM Policies

### Identity-Based Policies

Attached to identities such as users, groups, or roles.

They define what the identity can do.

### Resource-Based Policies

Attached to supported resources, such as an S3 bucket.

They specify which principals can access that resource and under what conditions.

### AWS Managed Policies

Created and maintained by AWS.

They can simplify permission management, but their permissions should be reviewed before use.

### Customer Managed Policies

Created and maintained by the customer.

They allow organizations to define reusable permissions for their requirements.

### Inline Policies

Embedded directly in a single identity.

They can be useful for specific permissions, although managed policies are often easier to reuse and maintain.

## 9. Explicit Deny and Permission Evaluation

IAM permissions are evaluated according to AWS authorization rules.

A key exam principle is:

**An applicable explicit Deny overrides an Allow.**

In many ordinary cases, access is denied when no applicable Allow grants the requested permission.

However, real authorization decisions can also involve resource policies, permissions boundaries, service control policies, session policies, and other controls.

Do not assume that adding one Allow policy always guarantees access.

## 10. Multi-Factor Authentication (MFA)

MFA strengthens authentication by requiring an additional factor beyond a password.

Supported options can include authenticator applications and security keys.

### Why MFA Matters

* Reduces reliance on passwords alone.
* Helps protect privileged access.
* Adds a barrier against compromised passwords.

### Root-User Security

The AWS account root user has extensive account-level privileges.

Best practices include:

* Enable MFA.
* Do not use root credentials for routine tasks.
* Avoid creating root access keys.
* Secure the recovery methods.
* Use appropriately permissioned identities for daily administration.

## 11. Temporary Credentials and Federation

Temporary credentials are issued for a limited duration and are commonly used with IAM roles.

They reduce the need to distribute permanent access keys.

Federation allows users to authenticate through a trusted identity provider and obtain access to AWS according to configured permissions.

AWS IAM Identity Center supports workforce access to multiple AWS accounts and applications.

## 12. IAM Best Practices

1. Apply least privilege.
2. Use IAM roles for AWS workloads where appropriate.
3. Prefer temporary credentials.
4. Enable MFA for human and privileged access.
5. Protect root-user credentials.
6. Avoid embedding access keys in source code.
7. Review unused permissions.
8. Use groups or centralized identity management to simplify administration.
9. Audit relevant account activity with AWS CloudTrail.
10. Use policies that restrict access to the required actions and resources.

## 13. Exam-Focused Revision Notes

* IAM controls access to AWS resources.
* Users represent identities within an AWS account.
* Groups organize IAM users.
* Roles provide permissions to trusted principals that assume them.
* Policies define permissions.
* Authentication verifies identity; authorization determines permitted actions.
* An applicable explicit Deny overrides an Allow.
* Least privilege reduces unnecessary permissions.
* IAM roles can provide temporary credentials.
* EC2 applications should use suitable IAM roles rather than embedded long-term keys.
* MFA adds another authentication factor.
* The root user should not be used for routine administrative work.
* IAM Identity Center supports workforce access across AWS accounts and applications.
* Resource-based policies are attached to supported resources.
* IAM is global for its core identity and access management resources.

## 14. Knowledge Check

**Question 1:** Which IAM component groups users for permission management?

A. IAM Group
B. Amazon VPC
C. Amazon EBS
D. AWS Region

**Answer:** A — IAM groups organize users.

**Question 2:** An application running on EC2 needs to read objects from S3. Which approach is generally recommended?

A. Hardcode permanent access keys into the application
B. Assign an appropriate IAM role to the EC2 instance
C. Make the bucket public
D. Disable all authorization

**Answer:** B — An IAM role can provide temporary credentials to the application.

**Question 3:** What happens when an applicable explicit Deny conflicts with an Allow?

A. Allow always wins
B. Deny takes precedence
C. The policy is ignored in every case
D. The user automatically becomes an administrator

**Answer:** B — Explicit Deny takes precedence.

**Question 4:** What is the primary purpose of MFA?

A. To increase storage capacity
B. To strengthen authentication
C. To accelerate DNS resolution
D. To reduce database size

**Answer:** B — MFA adds another authentication factor.

**Question 5:** Which IAM component defines permissions?

A. IAM policy
B. Availability Zone
C. EC2 instance type
D. Route table

**Answer:** A — IAM policies define permissions.

**Question 6:** What is the recommended use of the AWS root user?

A. Routine daily development
B. All application API calls
C. Tasks that specifically require root-user privileges
D. Every database query

**Answer:** C — Root access should be reserved for tasks that require it.

## 15. Practical Exercise

A company has three teams:

* Developers who need to deploy applications.
* Auditors who need to review configurations.
* An EC2 application that needs read access to one S3 bucket.

Propose an IAM design.

### Suggested Solution

* Assign developer permissions according to deployment responsibilities.
* Give auditors appropriate read-only permissions.
* Attach an IAM role to the EC2 workload with narrowly scoped S3 read permissions.
* Require MFA for appropriate human access.
* Avoid unnecessary long-term credentials.
* Review policies regularly and audit relevant activity.

## 16. Official Learning Resources

* AWS IAM: https://aws.amazon.com/iam/
* IAM User Guide: https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html
* IAM Best Practices: https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html
* AWS IAM Identity Center: https://aws.amazon.com/iam/identity-center/
* AWS Security: https://aws.amazon.com/security/

## 17. Module Completion Checklist

* [ ] Distinguish users, groups, roles, and policies.
* [ ] Explain authentication and authorization.
* [ ] Understand Allow and Deny evaluation.
* [ ] Explain the purpose of MFA.
* [ ] Understand temporary credentials and federation.
* [ ] Explain IAM roles for EC2 applications.
* [ ] Apply least privilege to example scenarios.
* [ ] Complete the knowledge check without consulting the answers.
