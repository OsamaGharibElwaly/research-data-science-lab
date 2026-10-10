# 11 — AI Evaluation and Model Limitations

## 1. Learning Objectives

* Understand why AI systems must be evaluated before deployment.
* Identify common generative AI failure modes.
* Distinguish model quality, application quality, and operational quality.
* Recognize common evaluation metrics.
* Understand hallucinations, bias, drift, and robustness.
* Identify ways to reduce risk and improve reliability.

## 2. Why AI Evaluation Matters

AI evaluation determines whether a model or application performs adequately for its intended purpose.

Evaluation can reveal:

* Incorrect outputs.
* Poor relevance.
* Biased performance.
* Unsupported claims.
* Unsafe responses.
* Weak retrieval.
* Inconsistent formatting.
* Excessive latency.
* High cost.

A model that produces impressive examples may still fail on realistic or adversarial inputs.

## 3. Types of AI Evaluation

### 3.1 Model Evaluation

Assesses the model's performance on a defined task.

Examples:

* Classification accuracy.
* Regression error.
* Text-generation quality.
* Multimodal task performance.

### 3.2 Application Evaluation

Assesses the entire system, including prompts, retrieval, business logic, APIs, and output handling.

A good model can be part of a poor application if the retrieval system supplies incorrect context or the backend mishandles results.

### 3.3 Operational Evaluation

Assesses production behavior.

Important measures include:

* Latency.
* Throughput.
* Availability.
* Error rate.
* Cost per request.
* Resource utilization.

### 3.4 Responsible AI Evaluation

Assesses fairness, safety, privacy, explainability, and other relevant risks.

The evaluation method should match the system's intended use and potential impact.

## 4. Traditional ML Metrics

### Classification

**Accuracy:** Fraction of predictions that are correct.

**Precision:** Fraction of predicted positive cases that are truly positive.

**Recall:** Fraction of actual positive cases that are correctly identified.

**F1 score:** Harmonic mean of precision and recall.

**ROC-AUC:** Measures ranking discrimination across classification thresholds under the chosen evaluation setup.

The appropriate metric depends on the business cost of false positives and false negatives.

### Regression

**MAE:** Average absolute prediction error.

**MSE:** Average squared prediction error.

**RMSE:** Square root of mean squared error.

Lower values generally indicate smaller prediction errors when comparing the same dataset and metric.

## 5. Generative AI Evaluation

Generative AI outputs are often open-ended, so evaluation may require several criteria.

### Relevance

Does the answer address the user's question?

### Correctness

Are the factual claims accurate?

### Groundedness

Are the claims supported by the supplied evidence or retrieved context?

### Completeness

Does the response cover the important parts of the request?

### Coherence

Is the response understandable and logically organized?

### Format Compliance

Does the response follow the required structure?

### Safety

Does the response avoid inappropriate, harmful, or policy-violating content?

### Citation Quality

Do the cited sources exist and support the associated claims?

No single score captures every dimension of generative AI quality.

## 6. Hallucinations

A hallucination is a generated statement that appears plausible but is false, unsupported, or fabricated.

Examples:

* Invented research references.
* Incorrect technical details.
* Fabricated company policies.
* Incorrect claims about a product.
* Unsupported explanations presented confidently.

### Causes and Contributing Factors

Hallucinations can be associated with:

* Missing or ambiguous context.
* Limitations in learned knowledge.
* Poor retrieval.
* Ambiguous prompts.
* Generation uncertainty.
* Conflicting source documents.
* Model limitations.

### Mitigation

* Supply trusted context.
* Use retrieval when appropriate.
* Validate factual claims.
* Ask the system to acknowledge missing evidence.
* Check citations.
* Use human review for consequential decisions.
* Evaluate against representative examples.

These practices can reduce hallucination risk but do not eliminate it.

## 7. Bias and Fairness Evaluation

Models can perform differently across populations or input groups.

Evaluation may include:

* Comparing error rates across relevant groups.
* Reviewing data representation.
* Checking label quality.
* Identifying proxy variables.
* Assessing potential disparate impact.
* Investigating complaints and real-world outcomes.

Fairness criteria must be selected based on the use case and applicable requirements. Different fairness measures can conflict.

## 8. Robustness and Reliability

Robustness refers to how well a system performs under varied, noisy, unusual, or adversarial conditions.

Test cases may include:

* Typos.
* Ambiguous instructions.
* Unexpected file formats.
* Long inputs.
* Missing information.
* Conflicting documents.
* Malicious instructions.
* Unsupported requests.
* Temporary service failures.

Reliability also requires appropriate timeout handling, retries, error handling, and fallback behavior.

## 9. Data Drift and Concept Drift

### Data Drift

A change in the distribution of input features over time.

Example: A customer-support model receives a new vocabulary and different request types after a product launch.

### Concept Drift

A change in the relationship between input features and the target variable.

Example: Customer behavior changes so that historical signals no longer predict churn as accurately.

### Response

* Monitor input data.
* Track model quality when labels are available.
* Investigate performance changes.
* Reassess features and training data.
* Retrain or update the model when justified.
* Validate changes before deployment.

A detected distribution shift does not automatically mean retraining is necessary; investigate its effect on the task.

## 10. Evaluating RAG Systems

RAG evaluation must consider retrieval and generation.

### Retrieval Evaluation

Questions include:

* Was the correct document retrieved?
* Were relevant passages ranked highly?
* Were necessary sources omitted?
* Were unauthorized documents retrieved?

Possible measures include precision at k, recall at k, and ranking metrics.

### Generation Evaluation

Questions include:

* Is the answer supported by retrieved context?
* Does it answer the user's question?
* Are citations accurate?
* Does it acknowledge missing evidence?
* Does it avoid adding unsupported claims?

### End-to-End Evaluation

Also test:

* Access-control enforcement.
* Latency.
* Cost.
* Failure handling.
* User experience.

## 11. Human Evaluation and Automated Evaluation

### Human Evaluation

Qualified reviewers assess outputs using a rubric.

Advantages:

* Can identify subtle quality and safety problems.
* Supports nuanced judgment.
* Can evaluate usefulness and clarity.

Limitations:

* Requires time and resources.
* May involve subjective differences.
* Needs consistent review guidelines.

### Automated Evaluation

Scripts, metrics, or evaluator models assess outputs against defined criteria.

Advantages:

* Can scale across many test cases.
* Supports repeated regression testing.
* Can quickly identify format or rule violations.

Limitations:

* May fail to recognize subtle errors.
* Can inherit evaluator biases.
* May incorrectly reward plausible but unsupported outputs.

A combined approach is often appropriate for high-quality evaluation.

## 12. Test Datasets and Regression Testing

Build an evaluation dataset that represents expected production usage.

Include:

* Common requests.
* Rare but important cases.
* Ambiguous inputs.
* Difficult examples.
* Security attacks.
* Known failure cases.
* Representative user groups.
* Expected outputs or evaluation rubrics.

When prompts, models, retrieval settings, or application logic change, rerun important tests to detect regressions.

Avoid using the final test dataset repeatedly to tune the system without preserving an independent evaluation set.

## 13. AWS Evaluation Context

Amazon Bedrock provides supported model-evaluation capabilities that can help assess models against defined criteria and datasets. Exact options depend on the model, feature, and configuration.

Amazon SageMaker AI supports broader ML development and evaluation workflows.

Amazon CloudWatch can help monitor operational metrics and logs for integrated components.

AWS CloudTrail can help audit supported AWS API activity.

For every evaluation workflow, verify current service support and permissions.

## 14. Example Evaluation Plan

**Application:** Internal document assistant.

Evaluation dimensions:

1. Retrieval relevance.
2. Answer correctness.
3. Groundedness.
4. Citation correctness.
5. Refusal or abstention when evidence is missing.
6. Authorization and privacy.
7. Prompt-injection resistance.
8. Latency.
9. Cost per request.
10. User feedback.

Create a representative test set, define acceptance thresholds, run evaluations before release, and repeat them after important changes.

## 15. Knowledge Check

1. Why is model evaluation necessary?
2. What is the difference between accuracy and recall?
3. What is a hallucination?
4. How does data drift differ from concept drift?
5. Why should RAG retrieval and generation be evaluated separately?
6. What is regression testing?
7. What are the advantages of human evaluation?
8. What is one limitation of automated evaluation?
9. Why must fairness metrics be selected carefully?
10. Which AWS service supports operational metrics, logs, and alarms?

### Answers

1. To determine whether the model or application meets quality, safety, and operational requirements.
2. Accuracy measures all correct predictions; recall measures the fraction of actual positive cases identified.
3. A false or unsupported generated claim presented as plausible information.
4. Data drift changes input distributions; concept drift changes the relationship between inputs and targets.
5. Poor retrieval can produce unsupported answers even when the model generates fluent text.
6. Repeating tests after changes to identify newly introduced failures.
7. Humans can judge nuanced correctness, relevance, usefulness, and safety.
8. Automated evaluators may miss subtle errors or reproduce their own biases.
9. Different definitions of fairness may conflict and have different implications across use cases.
10. Amazon CloudWatch.

## 16. Revision Checklist

* [ ] Distinguish model, application, operational, and responsible AI evaluation.
* [ ] Understand classification and regression metrics.
* [ ] Recognize hallucinations and mitigation techniques.
* [ ] Understand bias, fairness, robustness, and reliability.
* [ ] Distinguish data drift from concept drift.
* [ ] Explain RAG retrieval and generation evaluation.
* [ ] Compare human and automated evaluation.
* [ ] Understand test datasets and regression testing.
* [ ] Identify relevant AWS evaluation and monitoring capabilities.

## 17. Official Resources

* Amazon Bedrock: https://aws.amazon.com/bedrock/
* Amazon SageMaker AI: https://aws.amazon.com/sagemaker/
* Amazon CloudWatch: https://aws.amazon.com/cloudwatch/
* AWS Responsible AI: https://aws.amazon.com/ai/responsible-ai/

---

**Exam focus:** Identify model limitations, select suitable evaluation methods, and recognize the safeguards needed to make AI outputs reliable and appropriate for the intended task.
