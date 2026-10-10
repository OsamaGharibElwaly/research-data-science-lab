# 04 — Responsible AI and AI Governance

## 1. Learning Objectives

* Explain responsible AI and its major principles.
* Recognize bias, fairness, explainability, privacy, and transparency concerns.
* Understand human oversight and accountability.
* Identify generative AI risks and practical mitigation methods.
* Understand AI governance throughout the model lifecycle.
* Recognize the AWS services and capabilities relevant to responsible AI.

## 2. What Is Responsible AI?

Responsible AI means designing, developing, deploying, and monitoring AI systems in ways that consider their impacts on people, organizations, and society.

Responsible AI should be considered throughout the lifecycle, not only after a model has been deployed.

Important principles include:

* Fairness.
* Explainability.
* Transparency.
* Privacy and security.
* Robustness and reliability.
* Safety.
* Accountability.
* Human oversight.

The relative importance of each principle depends on the use case and its risks.

## 3. Fairness and Bias

### Bias

Bias can arise when data, model design, evaluation, or deployment conditions produce systematically inappropriate outcomes for particular groups or situations.

Possible sources include:

* Unrepresentative training data.
* Historical discrimination in source data.
* Incorrect labels.
* Sampling errors.
* Features that act as proxies for sensitive attributes.
* Deployment in an environment different from the training environment.

### Fairness

Fairness involves evaluating whether an AI system treats individuals or groups appropriately according to the context, applicable requirements, and chosen fairness criteria.

No single fairness metric works for every scenario. Different definitions can conflict, so the relevant criteria must be selected and documented.

### Mitigation

* Use representative datasets.
* Review labels and data quality.
* Evaluate performance across relevant subgroups.
* Document limitations.
* Apply suitable mitigation methods.
* Monitor real-world outcomes.
* Include qualified human oversight.

Removing an explicit sensitive attribute does not necessarily eliminate bias because other features may act as proxies.

## 4. Explainability and Interpretability

**Explainability** concerns the ability to explain why a model produced an output.

**Interpretability** concerns how directly a human can understand a model's behavior or internal decision logic.

Some models are easier to interpret than others. Complex models may require additional explanation techniques.

Examples:

* Feature importance.
* Local explanations for individual predictions.
* Model cards.
* Documentation of intended uses and limitations.
* Human-readable explanations of system workflows.

Explanations are approximations in many cases and should not automatically be treated as complete proof of how a model reasoned.

## 5. Transparency

Transparency means providing appropriate information about an AI system and how it is used.

Depending on the application, this may include:

* Disclosing that users are interacting with AI.
* Describing the intended purpose.
* Communicating limitations and uncertainty.
* Explaining what data is collected.
* Identifying when human review is involved.
* Documenting known risks and evaluation results.

Transparency should be understandable to the intended audience.

## 6. Privacy and Data Protection

AI applications may process personal, confidential, or proprietary information.

Potential risks include:

* Sending sensitive data to an inappropriate service.
* Excessive data collection.
* Unauthorized access to prompts or outputs.
* Retaining information longer than necessary.
* Exposing private information in logs.
* Retrieving documents the user is not authorized to access.

### Good Practices

* Collect only the data needed for the task.
* Apply access controls and least privilege.
* Encrypt data where appropriate.
* Avoid placing secrets or unnecessary personal data in prompts.
* Review logging and retention configurations.
* Follow applicable privacy and data-protection requirements.
* Verify service-specific data handling and retention terms.

Do not assume every AI service, model, configuration, or third-party integration has identical data-handling behavior.

## 7. Security and Robustness

Responsible AI also includes protecting applications against malicious input and unexpected behavior.

Common risks include:

* Prompt injection.
* Data poisoning.
* Unauthorized tool use.
* Sensitive-data disclosure.
* Adversarial inputs.
* Unsafe generated code.
* Model or application failures.

### Mitigation Strategies

* Validate inputs and outputs.
* Separate trusted instructions from untrusted content.
* Restrict model-connected tools.
* Use least-privilege permissions.
* Test adversarial and edge-case scenarios.
* Apply monitoring and incident response.
* Use suitable guardrails and policy enforcement.
* Require confirmation for sensitive actions.

Guardrails can reduce risks but cannot guarantee that all unsafe behavior will be prevented.

## 8. Generative AI-Specific Risks

### Hallucinations

A model can generate plausible but false information.

**Mitigation:** Use trusted sources, retrieval, verification, uncertainty handling, and human review.

### Toxic or Harmful Content

A model may generate offensive, discriminatory, or otherwise harmful content.

**Mitigation:** Apply appropriate content controls, test relevant scenarios, and monitor outcomes.

### Copyright and Intellectual Property

Generated content may raise questions about ownership, licensing, attribution, or similarity to existing works.

**Mitigation:** Review applicable legal requirements, organizational policies, source-data arrangements, and generated outputs.

### Misinformation

Generated content may be used to spread false claims or impersonate individuals.

**Mitigation:** Use provenance measures where appropriate, review high-impact content, and provide suitable disclosure.

### Overreliance

Users may trust a model's output without verifying it.

**Mitigation:** Communicate limitations and define when independent verification is required.

### Data Leakage

An application may expose confidential data through prompts, retrieved content, outputs, or logs.

**Mitigation:** Apply access controls, data minimization, secure logging, and testing.

## 9. Human Oversight and Accountability

Human oversight is important when AI decisions have meaningful consequences.

Examples include:

* Hiring and employment.
* Lending and financial services.
* Healthcare.
* Legal decisions.
* Public services.
* Critical infrastructure.

Organizations should establish:

* Clear ownership of AI systems.
* Defined approval responsibilities.
* Escalation procedures.
* Review and appeal processes where appropriate.
* Incident reporting.
* Documentation of decisions and changes.

Human involvement is not automatically effective. Reviewers need adequate information, competence, authority, and time to challenge an AI recommendation.

## 10. AI Governance

AI governance is the collection of policies, roles, procedures, controls, and monitoring activities used to manage AI systems responsibly.

### Governance Lifecycle

1. Identify the business purpose.
2. Classify the potential risks.
3. Define data and privacy requirements.
4. Select suitable models and services.
5. Establish evaluation criteria.
6. Conduct testing and approvals.
7. Deploy with appropriate safeguards.
8. Monitor performance and incidents.
9. Review changes and periodically reassess risk.
10. Retire systems when no longer appropriate.

### Governance Documentation

Useful documentation may include:

* Intended use and prohibited use.
* Data sources and data lineage.
* Model selection rationale.
* Evaluation results.
* Known limitations.
* Security and privacy controls.
* Human oversight requirements.
* Approval records.
* Monitoring and incident records.

## 11. Risk-Based Governance

Not all AI systems require the same level of oversight.

A low-impact tool that suggests internal document headings may need fewer controls than an AI system influencing medical treatment or credit decisions.

Risk assessment should consider:

* Severity of potential harm.
* Likelihood of failure or misuse.
* Number of people affected.
* Sensitivity of processed data.
* Degree of automation.
* Reversibility of decisions.
* Applicable laws and industry requirements.

Controls should be proportionate to the risk and reviewed when the application changes.

## 12. AWS Responsible AI Context

### Amazon Bedrock Guardrails

Amazon Bedrock Guardrails provides configurable controls for supported generative AI applications. Depending on the configuration and supported features, controls can address topics such as harmful content, sensitive information, denied topics, and grounding-related checks.

The exact capabilities depend on the feature, model, and configuration. Guardrails are one part of a broader security and governance approach.

### Amazon SageMaker AI

SageMaker AI includes capabilities for developing, deploying, and managing ML models. Relevant governance practices include model evaluation, documentation, monitoring, and controlled deployment.

### AWS IAM

AWS Identity and Access Management helps control which identities and services can access AWS resources. Apply least privilege to AI-related resources and tools.

### AWS CloudTrail

AWS CloudTrail records supported account activity and API events, helping organizations audit actions and investigate activity.

### Amazon CloudWatch

Amazon CloudWatch supports monitoring through metrics, logs, and alarms for integrated services and applications.

### AWS Shared Responsibility

AWS is responsible for security of the cloud, while customers remain responsible for aspects of security in the cloud, depending on the service and deployment model.

For AI workloads, customer responsibilities can include:

* Configuring permissions.
* Protecting application data.
* Managing prompts and retrieved documents.
* Securing integrations.
* Reviewing generated outputs.
* Meeting applicable compliance obligations.

## 13. Responsible AI Scenario Examples

### Scenario A: Biased Hiring Recommendations

An AI system consistently ranks candidates from a particular group lower.

Appropriate actions include investigating training data and labels, evaluating subgroup performance, reviewing features and decision criteria, and introducing suitable mitigation and human oversight.

### Scenario B: Internal Policy Chatbot

A chatbot retrieves confidential HR documents for unauthorized users.

The problem is not solved merely by instructing the model not to reveal secrets. Enforce document-level authorization during retrieval and protect downstream outputs and logs.

### Scenario C: Incorrect Medical Information

A generative model gives a confident but incorrect medical answer.

Mitigations may include using trusted evidence, restricting the intended scope, requiring professional review, communicating uncertainty, and evaluating high-risk cases.

### Scenario D: Autonomous Refund Processing

An agent can issue refunds without limits.

Apply least privilege, transaction limits, validation, audit logging, and approval requirements for consequential or unusual transactions.

## 14. Knowledge Check

1. What is responsible AI?
2. Name four common sources of bias.
3. How do explainability and transparency differ?
4. Why does removing a sensitive feature not always eliminate bias?
5. What is prompt injection?
6. Why is human oversight important in high-impact use cases?
7. What is AI governance?
8. Which AWS service controls access to AWS resources?
9. What is the purpose of Amazon Bedrock Guardrails?
10. Why should governance controls be proportionate to risk?

### Answers

1. Designing and operating AI systems with appropriate attention to safety, fairness, privacy, accountability, and other impacts.
2. Unrepresentative data, biased historical records, incorrect labels, sampling errors, and proxy features.
3. Explainability concerns understanding model outputs; transparency concerns communicating relevant information about the system and its use.
4. Other features may act as proxies for sensitive attributes.
5. An attack that attempts to manipulate a model through malicious or untrusted instructions.
6. AI can produce errors or harmful outcomes that require informed review and intervention.
7. Policies, roles, controls, procedures, and monitoring used to manage AI risks.
8. AWS IAM.
9. To apply supported configurable controls to help reduce certain generative AI risks.
10. Different applications have different potential impacts and require different levels of control.

## 15. Revision Checklist

* [ ] Explain the major responsible AI principles.
* [ ] Identify sources and consequences of bias.
* [ ] Understand explainability and transparency.
* [ ] Recognize privacy, security, and data-leakage risks.
* [ ] Explain hallucinations, prompt injection, and harmful content.
* [ ] Understand human oversight and accountability.
* [ ] Describe AI governance across the lifecycle.
* [ ] Identify relevant AWS security, monitoring, and guardrail capabilities.

## 16. Official Resources

* AWS Responsible AI: https://aws.amazon.com/ai/responsible-ai/
* Amazon Bedrock Guardrails: https://aws.amazon.com/bedrock/guardrails/
* AWS IAM: https://aws.amazon.com/iam/
* AWS CloudTrail: https://aws.amazon.com/cloudtrail/
* AWS CloudWatch: https://aws.amazon.com/cloudwatch/

---

**Exam focus:** Identify responsible AI risks in a scenario and select appropriate governance, human oversight, privacy, security, and mitigation practices.
