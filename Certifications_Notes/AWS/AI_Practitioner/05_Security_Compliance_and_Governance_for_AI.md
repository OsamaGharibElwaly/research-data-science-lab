# 05 — Security, Compliance, and Governance for AI

## 1. Learning Objectives

By the end of this module, you should be able to:

* Identify security risks in AI and generative AI applications.
* Understand data protection, access control, and encryption.
* Explain prompt injection, data poisoning, and sensitive-data exposure.
* Recognize AWS security and compliance responsibilities.
* Identify governance controls for AI workloads.
* Match common security requirements to appropriate AWS services.

## 2. AI Security Fundamentals

AI security involves protecting data, models, infrastructure, applications, and users against unauthorized access, manipulation, misuse, and failure.

An AI application may involve several components:

1. User interface.
2. Application backend.
3. Model endpoint or foundation-model API.
4. Data sources and retrieval systems.
5. External tools and APIs.
6. Logging and monitoring infrastructure.

Each component introduces potential security risks.

### Security Objectives

* **Confidentiality:** Prevent unauthorized disclosure of information.
* **Integrity:** Prevent unauthorized modification of data, models, and outputs.
* **Availability:** Ensure authorized users can access services when needed.
* **Authenticity:** Verify identities and the origin of requests or information.
* **Accountability:** Maintain appropriate records of actions and decisions.

## 3. Common AI Security Threats

### 3.1 Prompt Injection

Prompt injection occurs when malicious or untrusted input attempts to manipulate a model's behavior by introducing instructions that conflict with the application's intended behavior.

Examples:

* A document instructs a chatbot to reveal confidential information.
* A webpage tells an agent to ignore its original task.
* A user attempts to bypass content restrictions.

**Mitigations:**

* Treat retrieved documents and user input as untrusted data.
* Separate trusted application instructions from external content.
* Restrict tool permissions.
* Validate tool arguments and outputs.
* Enforce access control outside the model.
* Test adversarial inputs.
* Require approval for sensitive actions.

Prompt instructions alone are not a reliable security boundary.

### 3.2 Data Poisoning

Data poisoning involves manipulating training or other data used by an AI system to influence its behavior.

Possible consequences:

* Reduced accuracy.
* Biased predictions.
* Backdoors or targeted failures.
* Incorrect associations learned by the model.

**Mitigations:**

* Validate data sources and provenance.
* Restrict dataset modification permissions.
* Review anomalous examples.
* Maintain versioned datasets.
* Monitor model behavior.
* Apply appropriate training-data quality checks.

### 3.3 Sensitive Information Disclosure

An AI application may expose:

* Personal information.
* Credentials and API keys.
* Proprietary documents.
* Financial information.
* Confidential business data.

**Mitigations:**

* Minimize sensitive information in prompts.
* Apply access controls to source documents.
* Redact sensitive information when appropriate.
* Protect logs and outputs.
* Use encryption and secure secret storage.
* Review service-specific data handling terms.

### 3.4 Model and Application Abuse

Attackers may attempt to exploit an AI application through excessive requests, malicious file uploads, unauthorized tool calls, or resource-intensive prompts.

Controls include authentication, rate limiting, input validation, request-size limits, monitoring, and cost controls.

### 3.5 Insecure Output Handling

Generated text, code, HTML, SQL, or tool arguments may be unsafe.

Examples:

* Executing generated code without review.
* Rendering untrusted HTML without sanitization.
* Executing generated SQL with excessive database permissions.
* Passing model-generated commands directly to a privileged system.

Validate and constrain outputs before using them in downstream systems.

## 4. Data Protection

### Data Classification

Organizations may classify data as:

* Public.
* Internal.
* Confidential.
* Restricted or highly sensitive.

The exact categories depend on organizational policy.

Data classification determines how data may be collected, stored, processed, shared, and retained.

### Data Minimization

Collect and process only the information needed for the intended task.

For example, a support chatbot usually does not need a customer's full payment-card details to answer a general question about delivery.

### Encryption

* **Encryption in transit:** Protects data while moving between systems.
* **Encryption at rest:** Protects stored data.

AWS services support different encryption configurations. Verify the relevant service's defaults, available controls, and customer responsibilities.

### Secrets Management

Credentials, API keys, and database passwords should not be embedded in source code or prompts.

Use suitable secret-management capabilities, rotate credentials when appropriate, and restrict access.

## 5. Identity and Access Management

AWS Identity and Access Management (IAM) controls access to AWS resources.

Important concepts:

* **IAM user:** An identity that can authenticate to AWS when configured.
* **IAM role:** An identity with permissions that trusted principals can assume.
* **IAM policy:** A document defining allowed or denied actions and resources.
* **Least privilege:** Grant only the permissions required for a task.
* **Temporary credentials:** Short-lived credentials used instead of long-lived credentials where appropriate.
* **Multi-factor authentication (MFA):** Adds another authentication factor.

### AI Security Example

Suppose an AI agent can look up orders and issue refunds.

A secure design should give the agent only the permissions needed for its task. Read-only order lookup should not automatically grant unrestricted access to payment systems or all customer records.

Never rely solely on a model instruction to prevent unauthorized operations. Enforce permissions in the underlying systems.

## 6. AWS Security Services

### AWS IAM

Controls access to AWS resources through identities, policies, and roles.

### AWS KMS

AWS Key Management Service (AWS KMS) helps create and manage cryptographic keys used by supported AWS services and applications.

### AWS Secrets Manager

Stores and manages secrets such as database credentials and API keys, with supported rotation and access-control capabilities.

### AWS CloudTrail

Records supported AWS account activity and API events. It is useful for auditing and investigating actions.

### Amazon CloudWatch

Collects supported metrics, logs, and alarms to help monitor operational behavior.

### Amazon GuardDuty

Detects potential threats by analyzing supported AWS data sources and activity signals.

### AWS Config

Records resource configurations and can evaluate them against configured rules or conformance packs.

### Amazon Bedrock Guardrails

Provides configurable controls for supported generative AI applications. Depending on configuration and supported features, these can address harmful content, sensitive information, denied topics, and grounding-related concerns.

Guardrails complement, rather than replace, application security controls.

## 7. Compliance and Regulatory Considerations

Compliance means meeting applicable legal, regulatory, contractual, and organizational requirements.

Relevant requirements depend on:

* The country or jurisdiction.
* Industry.
* Type of data processed.
* Purpose of the AI system.
* Customer and contractual obligations.

Common compliance concerns include:

* Personal data protection.
* Data retention.
* Data residency.
* Access auditing.
* Consent and lawful processing.
* Intellectual property.
* Industry-specific requirements.

Do not assume that using an AWS service automatically makes an entire application compliant.

Organizations must assess their architecture, configuration, data practices, and responsibilities.

## 8. AWS Shared Responsibility Model

AWS operates under a shared responsibility model.

### AWS Responsibility: Security of the Cloud

AWS is responsible for protecting the underlying cloud infrastructure, including relevant physical facilities, hardware, networking, and managed infrastructure.

### Customer Responsibility: Security in the Cloud

Customer responsibilities depend on the service and architecture and may include:

* Configuring access permissions.
* Protecting application data.
* Managing identities.
* Securing application code.
* Configuring network controls.
* Selecting encryption settings where applicable.
* Monitoring activity.
* Meeting organizational and legal obligations.

Managed services can reduce infrastructure-management responsibilities, but they do not eliminate all customer security responsibilities.

## 9. AI Governance Controls

An AI governance program should establish:

* Approved use cases.
* Risk classification.
* Data ownership.
* Access policies.
* Model evaluation requirements.
* Human oversight.
* Change management.
* Audit and documentation practices.
* Incident response.
* Periodic reviews.

High-impact use cases may require stronger controls and more frequent assessments than low-risk internal productivity tools.

## 10. Secure AI Application Lifecycle

1. Define the intended use and security requirements.
2. Classify the data.
3. Select an appropriate model and service.
4. Configure identity and access controls.
5. Secure data storage and transmission.
6. Validate inputs and outputs.
7. Test adversarial scenarios.
8. Deploy with suitable monitoring.
9. Review logs and security events.
10. Update controls when threats or requirements change.

## 11. Scenario-Based Exam Practice

**Scenario A:** An AI application stores credentials directly in source code.

Recommended action: Move credentials to an appropriate secrets-management solution and restrict access.

**Scenario B:** A model can read every employee document despite serving only the HR department.

Recommended action: Enforce document-level authorization and least privilege.

**Scenario C:** A retrieved webpage tells an agent to transfer money.

Recommended action: Treat the webpage as untrusted input, restrict tools, validate actions, and require suitable authorization.

**Scenario D:** An organization needs to investigate which AWS API actions occurred.

Recommended service: AWS CloudTrail.

**Scenario E:** An organization wants to monitor application metrics and create alarms.

Recommended service: Amazon CloudWatch.

**Scenario F:** An organization needs managed cryptographic-key capabilities.

Recommended service: AWS KMS.

## 12. Knowledge Check

1. What is prompt injection?
2. How does data poisoning differ from prompt injection?
3. What is the principle of least privilege?
4. What is the difference between encryption in transit and at rest?
5. Which service records supported AWS API activity?
6. Which service manages cryptographic keys?
7. Why are AI guardrails not a complete replacement for application security?
8. What does the AWS shared responsibility model describe?
9. Why should generated code be validated before execution?
10. Does using AWS automatically make an AI application compliant?

### Answers

1. Malicious or untrusted input that attempts to manipulate model behavior.
2. Data poisoning manipulates training or other data; prompt injection targets model behavior through input instructions.
3. Grant only the permissions required for a task.
4. In-transit encryption protects data moving between systems; at-rest encryption protects stored data.
5. AWS CloudTrail.
6. AWS KMS.
7. They cannot replace access control, secure application design, validation, and operational monitoring.
8. The division of security responsibilities between AWS and its customers.
9. Generated code may be incorrect, vulnerable, or unsafe.
10. No. Compliance depends on the entire solution and applicable requirements.

## 13. Revision Checklist

* [ ] Identify prompt injection and data poisoning.
* [ ] Understand data leakage and insecure output handling.
* [ ] Apply least privilege and secure secret management.
* [ ] Distinguish encryption in transit and at rest.
* [ ] Match IAM, KMS, Secrets Manager, CloudTrail, CloudWatch, GuardDuty, and Config to their uses.
* [ ] Explain the AWS shared responsibility model.
* [ ] Understand compliance and AI governance responsibilities.
* [ ] Recognize why defense in depth is necessary.

## 14. Official Resources

* AWS Security: https://aws.amazon.com/security/
* AWS Shared Responsibility Model: https://aws.amazon.com/compliance/shared-responsibility-model/
* AWS IAM: https://aws.amazon.com/iam/
* AWS KMS: https://aws.amazon.com/kms/
* AWS Secrets Manager: https://aws.amazon.com/secrets-manager/
* Amazon Bedrock Guardrails: https://aws.amazon.com/bedrock/guardrails/

---

**Exam focus:** Given an AI security or compliance scenario, identify the threat, the appropriate control, the relevant AWS service, and the correct allocation of responsibilities.
