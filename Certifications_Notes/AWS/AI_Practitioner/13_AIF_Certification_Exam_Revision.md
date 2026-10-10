# Module 13: AWS Certified AI Practitioner — Exam Revision

## 1. Module Objectives

This module consolidates the core concepts required for the AWS Certified AI Practitioner (AIF-C01) exam. It focuses on understanding AI and machine learning concepts, generative AI, foundation models, responsible AI, security, and AWS AI services.

**Study principle:** Understand what a technology does, when to use it, its limitations, and why one AWS service is more appropriate than another in a given scenario.

## 2. Exam Preparation Strategy

Before booking the exam, verify the current exam guide and official preparation resources on the AWS certification website. Exam domains and their weightings can change.

Official resources:

* AWS Certified AI Practitioner: https://aws.amazon.com/certification/certified-ai-practitioner/
* AWS Skill Builder: https://skillbuilder.aws/
* AWS Documentation: https://docs.aws.amazon.com/

Use this revision module alongside the current official exam guide rather than treating this document as a replacement for it.

## 3. AI, Machine Learning, and Deep Learning

### Artificial Intelligence

Artificial intelligence (AI) refers to systems designed to perform tasks associated with human intelligence, such as understanding language, recognizing patterns, reasoning, and generating content.

### Machine Learning

Machine learning (ML) enables systems to learn patterns from data and use those patterns to make predictions or decisions.

Common ML problem types:

| Problem type      | Purpose                    | Example                         |
| ----------------- | -------------------------- | ------------------------------- |
| Classification    | Predict a category         | Detect fraudulent transactions  |
| Regression        | Predict a numerical value  | Estimate house prices           |
| Clustering        | Group similar observations | Segment customers               |
| Forecasting       | Predict future values      | Estimate future demand          |
| Anomaly detection | Identify unusual patterns  | Detect abnormal network traffic |

### Learning Approaches

* **Supervised learning:** Learns from labeled examples.
* **Unsupervised learning:** Finds patterns in unlabeled data.
* **Reinforcement learning:** Learns through actions, rewards, and penalties.
* **Self-supervised learning:** Creates learning signals from the data itself.

### Deep Learning

Deep learning uses neural networks with multiple layers. It is especially useful for complex data such as images, audio, video, and natural language.

Remember: deep learning is a subset of machine learning, which is a subset of AI.

## 4. Core Machine Learning Concepts

### Training, Validation, and Testing

* **Training data:** Used to learn model parameters.
* **Validation data:** Used to compare models or tune hyperparameters.
* **Test data:** Used to estimate final performance on unseen data.

### Overfitting and Underfitting

* **Overfitting:** The model learns training-specific details and performs poorly on new data.
* **Underfitting:** The model fails to learn the important patterns in the data.
* **Generalization:** The ability to perform well on unseen examples.

### Common Metrics

| Metric                         | Meaning                                                 | Typical use                                       |
| ------------------------------ | ------------------------------------------------------- | ------------------------------------------------- |
| Accuracy                       | Fraction of predictions that are correct                | Balanced classification problems                  |
| Precision                      | Fraction of predicted positives that are truly positive | When false positives are costly                   |
| Recall                         | Fraction of actual positives that are detected          | When false negatives are costly                   |
| F1 score                       | Harmonic mean of precision and recall                   | Balancing precision and recall                    |
| Mean absolute error (MAE)      | Average absolute prediction error                       | Regression                                        |
| Root mean squared error (RMSE) | Square root of average squared error                    | Regression, with greater penalty for large errors |

Accuracy can be misleading when classes are imbalanced. Choose metrics according to the business problem and the cost of different errors.

## 5. Generative AI and Foundation Models

### Generative AI

Generative AI creates new content, including text, images, audio, video, and code, based on patterns learned from data.

### Foundation Models

A foundation model is trained on broad data and can be adapted to multiple tasks.

Common concepts:

* **Tokens:** Units of text or other content processed by a model.
* **Embeddings:** Numerical representations of content that capture semantic relationships.
* **Inference:** Using a trained model to generate outputs or make predictions.
* **Prompt:** Instructions and context supplied to a model.
* **Context window:** The amount of input and generated content a model can handle in a single interaction.
* **Temperature:** A generation setting that can affect output variability; exact behavior depends on the model and service.
* **Multimodal model:** A model that can process or generate multiple data types.

### Foundation Model Adaptation

| Technique                            | Main purpose                                                    |
| ------------------------------------ | --------------------------------------------------------------- |
| Prompt engineering                   | Improve behavior by changing instructions and context           |
| Retrieval-Augmented Generation (RAG) | Ground responses in external or organizational information      |
| Fine-tuning                          | Adapt model behavior using additional training                  |
| Continued pretraining                | Continue training on a further corpus of data                   |
| Model selection                      | Choose a model that best fits the task, constraints, and budget |

RAG does not automatically retrain the foundation model. It retrieves relevant information and supplies it as context during generation.

## 6. Prompt Engineering

Effective prompts often specify:

1. **Role:** The perspective or task the model should perform.
2. **Task:** The requested action.
3. **Context:** Relevant background information.
4. **Constraints:** Rules, limits, and exclusions.
5. **Output format:** The structure expected in the response.
6. **Examples:** Demonstrations of the desired result, when useful.

Common techniques:

* **Zero-shot prompting:** Provide instructions without examples.
* **Few-shot prompting:** Provide a small number of examples.
* **Structured prompting:** Organize instructions and context into clear sections.
* **Prompt chaining:** Break a complex task into sequential prompts.
* **Grounded prompting:** Supply trusted information to reduce unsupported answers.

A well-written prompt can improve results, but it cannot guarantee factual accuracy or eliminate security risks.

## 7. Retrieval-Augmented Generation (RAG)

Typical RAG workflow:

1. Collect approved documents.
2. Extract and clean text.
3. Split documents into chunks.
4. Generate embeddings.
5. Store embeddings and associated content in a retrieval system.
6. Retrieve relevant chunks for a user query.
7. Supply retrieved context to the foundation model.
8. Generate and evaluate the answer.

Important concepts:

* **Chunking:** Dividing documents into manageable sections.
* **Vector search:** Finding content with similar vector representations.
* **Semantic search:** Retrieving content based on meaning rather than only exact keyword matches.
* **Metadata filtering:** Restricting retrieval using attributes such as department, document type, or access permissions.
* **Grounding:** Connecting an answer to supplied evidence.

RAG quality depends on document quality, chunking, embedding quality, retrieval, ranking, prompt design, and model behavior.

## 8. Responsible AI

Key principles:

* **Fairness:** Avoid unjustified differences in outcomes across groups.
* **Explainability:** Help people understand relevant aspects of model behavior.
* **Transparency:** Communicate how AI is used and what its limitations are.
* **Privacy:** Protect personal and confidential information.
* **Security:** Prevent unauthorized access and manipulation.
* **Robustness:** Maintain acceptable behavior under realistic variation and challenging inputs.
* **Governance:** Establish accountability, controls, and monitoring.

Common risks include bias, hallucinations, privacy leakage, harmful outputs, prompt injection, and overreliance on automated decisions.

Human review is especially important for consequential decisions.

## 9. AWS AI and Machine Learning Services

### Service Selection

| Service             | Main purpose                                                                                                                          |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon Bedrock      | Build generative AI applications using supported foundation models and related capabilities                                           |
| Amazon SageMaker AI | Build, train, customize, deploy, and manage machine learning models                                                                   |
| Amazon Rekognition  | Analyze images and video                                                                                                              |
| Amazon Textract     | Extract text and structured information from documents                                                                                |
| Amazon Transcribe   | Convert speech to text                                                                                                                |
| Amazon Polly        | Convert text to speech                                                                                                                |
| Amazon Translate    | Translate between languages                                                                                                           |
| Amazon Comprehend   | Analyze text using natural language processing                                                                                        |
| Amazon Lex          | Build conversational interfaces                                                                                                       |
| Amazon Kendra       | Enterprise search                                                                                                                     |
| Amazon Personalize  | Create personalized recommendations                                                                                                   |
| Amazon Forecast     | Historically associated with time-series forecasting; verify current availability and guidance before selecting it for a new solution |

Service capabilities and availability can change. Use current AWS documentation when studying specific features.

### Bedrock Versus SageMaker AI

Choose **Amazon Bedrock** when the main goal is to use supported foundation models to build generative AI applications with managed capabilities.

Choose **Amazon SageMaker AI** when the main requirement involves developing, training, tuning, deploying, or managing machine learning models with broader ML workflows.

The services can complement each other; the choice depends on the actual workload.

## 10. AWS Infrastructure and Security

Understand the roles of these services:

* **Amazon S3:** Object storage for documents, datasets, and other files.
* **AWS Lambda:** Run code in response to events without managing servers directly.
* **Amazon API Gateway:** Create and manage APIs.
* **Amazon IAM:** Manage identities, roles, and permissions.
* **AWS KMS:** Manage encryption keys.
* **Amazon CloudWatch:** Collect metrics, logs, and alarms.
* **AWS CloudTrail:** Record account activity and API events.
* **AWS Step Functions:** Coordinate workflows using state machines.
* **Amazon DynamoDB:** Managed NoSQL database.

Security revision checklist:

* Apply least-privilege access.
* Protect credentials and secrets.
* Encrypt sensitive data where appropriate.
* Control access to training data and model inputs.
* Log relevant activity and monitor for suspicious behavior.
* Evaluate privacy and data-retention requirements.
* Review the shared responsibility model.

## 11. Pricing and Cost Optimization

Common cost drivers include:

* Input and output tokens for generative AI inference.
* Number of model requests.
* Model choice and generation settings.
* Compute instance type and runtime.
* Data storage and transfer.
* Endpoint availability and utilization.
* Training duration and experiment frequency.

Cost optimization approaches:

1. Select a model that meets the quality requirement without unnecessary capacity.
2. Reduce unnecessary prompt and output tokens.
3. Use caching where appropriate and safe.
4. Avoid unnecessary repeated model calls.
5. Scale compute according to demand.
6. Monitor usage and set budgets and alerts.
7. Evaluate total application cost, not only the model's inference price.

Use the AWS Pricing Calculator for estimates, AWS Cost Explorer for cost analysis, and AWS Budgets for budget monitoring and alerts.

## 12. Scenario-Based Decision Guide

| Scenario                                         | Likely concept or service                                                           |
| ------------------------------------------------ | ----------------------------------------------------------------------------------- |
| Generate answers from internal company documents | Foundation model with RAG, potentially using Bedrock Knowledge Bases                |
| Train and deploy a custom predictive model       | SageMaker AI                                                                        |
| Extract text and tables from scanned forms       | Textract                                                                            |
| Convert recorded speech to text                  | Transcribe                                                                          |
| Convert written content to spoken audio          | Polly                                                                               |
| Translate customer messages                      | Translate                                                                           |
| Analyze sentiment in text                        | Comprehend                                                                          |
| Identify objects in images                       | Rekognition                                                                         |
| Control access to AWS resources                  | IAM                                                                                 |
| Monitor application logs and metrics             | CloudWatch                                                                          |
| Audit account API activity                       | CloudTrail                                                                          |
| Reduce inference expenses                        | Model selection, token reduction, caching, and usage monitoring                     |
| Reduce unsupported generated answers             | Improve grounding and retrieval, evaluate outputs, and add appropriate human review |

These are typical associations, not exclusive rules. Always read the full scenario.

## 13. Final Revision Checklist

Before the exam, confirm that you can explain:

* [ ] AI, ML, deep learning, and generative AI.
* [ ] Supervised, unsupervised, reinforcement, and self-supervised learning.
* [ ] Classification, regression, clustering, and anomaly detection.
* [ ] Training, validation, testing, overfitting, and underfitting.
* [ ] Precision, recall, accuracy, F1, MAE, and RMSE.
* [ ] Tokens, embeddings, inference, context windows, and foundation models.
* [ ] Prompt engineering, RAG, fine-tuning, and model selection.
* [ ] Hallucinations, bias, fairness, privacy, and human oversight.
* [ ] The intended uses of major AWS AI services.
* [ ] Bedrock versus SageMaker AI.
* [ ] IAM, encryption, logging, monitoring, and shared responsibility.
* [ ] AWS AI pricing drivers and cost optimization.
* [ ] The domains and requirements in the current official exam guide.

## 14. Recommended Study Method

For each topic:

1. Explain it in your own words without looking at the notes.
2. Identify a realistic business scenario where it would be useful.
3. Compare it with at least one alternative.
4. Identify its limitations and risks.
5. Answer practice questions and record the reason for every mistake.
6. Revisit weak topics before attempting another timed practice test.

**Completion criterion:** You can explain the main concepts clearly and choose an appropriate approach for unfamiliar scenarios, not merely recognize definitions.
