# 06 — AWS AI and ML Services

## 1. Learning Objectives

* Identify major AWS AI and ML services.
* Distinguish Amazon Bedrock from Amazon SageMaker AI.
* Match AWS AI services to business use cases.
* Understand common service-selection considerations.
* Recognize supporting AWS services used in AI architectures.

## 2. Overview of AWS AI and ML

AWS offers services for building, training, deploying, and integrating AI capabilities.

Some services provide ready-to-use AI APIs. Others support custom model development, generative AI applications, data processing, or application infrastructure.

The exam emphasizes choosing a suitable service for a described requirement.

## 3. Amazon Bedrock

Amazon Bedrock is a managed service that provides access to supported foundation models from AWS and third-party model providers through a unified service interface.

### Common Use Cases

* Text generation.
* Summarization.
* Conversational applications.
* Question answering.
* Retrieval-Augmented Generation (RAG).
* Agent-based applications.
* Model evaluation and supported customization workflows.

### Key Benefits

* Access supported foundation models through managed APIs.
* Build generative AI applications without managing the underlying foundation-model infrastructure directly.
* Integrate with other AWS services.
* Use supported features such as knowledge bases and guardrails.

### Exam Recognition

Choose Amazon Bedrock when a scenario emphasizes building a generative AI application using managed foundation models.

Feature availability depends on the selected model, AWS Region, permissions, and service configuration.

## 4. Amazon SageMaker AI

Amazon SageMaker AI provides capabilities for building, training, tuning, deploying, and managing machine learning models.

### Common Use Cases

* Training custom ML models.
* Preparing and processing datasets.
* Experimenting with algorithms.
* Tuning model hyperparameters.
* Deploying inference endpoints.
* Managing ML workflows.

### Exam Recognition

Choose SageMaker AI when the requirement emphasizes custom ML development, training, tuning, or deployment control.

Bedrock and SageMaker AI have overlapping areas, but they serve different primary workflows. Choose based on the scenario rather than assuming one is universally better.

## 5. AWS AI Services for Specific Tasks

### Amazon Rekognition

Analyzes images and videos using supported computer-vision capabilities.

Example: Detecting objects or analyzing visual content.

### Amazon Textract

Extracts text and structured information from supported document formats.

Example: Processing invoices, forms, and scanned documents.

### Amazon Comprehend

Provides NLP capabilities such as sentiment analysis, entity recognition, and other supported text analysis tasks.

Example: Identifying customer sentiment in product reviews.

### Amazon Transcribe

Converts speech into text.

Example: Generating a transcript of a customer-service call.

### Amazon Polly

Converts text into speech.

Example: Generating spoken responses for an application.

### Amazon Translate

Provides machine translation between supported languages.

Example: Translating customer communications.

### Amazon Lex

Provides capabilities for building conversational interfaces and chatbots using speech and text.

Example: Creating a customer-service bot that gathers information and routes requests.

### Amazon Personalize

Helps build personalized recommendation experiences using user-item interaction data and supported recommendation capabilities.

Example: Recommending products to customers.

### Amazon Kendra

Provides intelligent enterprise search capabilities for finding relevant information across supported data sources.

Example: Searching internal documents and organizational knowledge.

### Amazon Forecast

Historically provided managed time-series forecasting capabilities. Do not assume current availability for new deployments: verify its service status and current AWS guidance before selecting it in a real architecture.

For general forecasting requirements, SageMaker AI and other currently supported AWS approaches may be appropriate.

## 6. Service Selection Table

| Requirement                        | Service to recognize |
| ---------------------------------- | -------------------- |
| Access managed foundation models   | Amazon Bedrock       |
| Build and train custom ML models   | Amazon SageMaker AI  |
| Analyze images and videos          | Amazon Rekognition   |
| Extract information from documents | Amazon Textract      |
| Analyze text sentiment or entities | Amazon Comprehend    |
| Convert speech to text             | Amazon Transcribe    |
| Convert text to speech             | Amazon Polly         |
| Translate text                     | Amazon Translate     |
| Build conversational interfaces    | Amazon Lex           |
| Personalized recommendations       | Amazon Personalize   |
| Enterprise search                  | Amazon Kendra        |

Check current AWS documentation for service availability, feature support, and any changes before deployment.

## 7. Supporting AWS Services

AI systems often need storage, compute, security, integration, and monitoring.

### Amazon S3

Object storage for datasets, documents, model artifacts, and application files.

### AWS Lambda

Runs event-driven code without requiring customers to manage the underlying servers directly.

### Amazon API Gateway

Creates and manages APIs that connect applications to backend services.

### AWS IAM

Manages access permissions for AWS resources.

### Amazon CloudWatch

Collects supported metrics, logs, and alarms.

### AWS CloudTrail

Records supported AWS account activity and API events.

### AWS Glue

Supports data integration, data preparation, and ETL workflows.

### Amazon Athena

Enables SQL queries against supported data in sources such as Amazon S3 without managing traditional database servers.

### AWS Step Functions

Coordinates multi-step workflows using supported service integrations.

### AWS KMS

Provides cryptographic-key management for supported AWS services and applications.

## 8. Example Architecture: Document Assistant

A document assistant may include:

1. Amazon S3 to store documents.
2. A document-processing and ingestion pipeline.
3. A retrieval system or supported Bedrock Knowledge Base.
4. Amazon Bedrock to generate answers using retrieved context.
5. An application backend to authenticate users.
6. IAM permissions to control service access.
7. CloudWatch and CloudTrail for suitable monitoring and auditing.

The architecture should enforce user authorization when retrieving documents and avoid exposing confidential content through logs or generated responses.

## 9. Example Architecture: Custom Prediction Model

A predictive application might use:

1. Amazon S3 for datasets.
2. Data preparation using an appropriate AWS data service or processing workflow.
3. SageMaker AI to train and evaluate the model.
4. A supported deployment option for inference.
5. A backend API to accept requests.
6. CloudWatch to monitor operational behavior.

The correct design depends on data volume, latency, deployment requirements, budget, and model complexity.

## 10. Selecting a Service

Ask these questions:

1. Is the task generative AI or a specific AI capability?
2. Does the organization need a ready-to-use API or a custom-trained model?
3. Does the solution require a particular modality?
4. Is the service available in the required Region?
5. What are the data-protection requirements?
6. What are the expected request volume, latency, and cost?
7. Which supporting services are needed?

### Important Distinctions

* Bedrock provides managed access to foundation models.
* SageMaker AI supports broader custom ML development and lifecycle workflows.
* Rekognition focuses on images and videos.
* Textract focuses on document text and structured extraction.
* Comprehend focuses on NLP tasks.
* Transcribe converts speech to text.
* Polly converts text to speech.
* Translate handles machine translation.

## 11. Knowledge Check

1. Which AWS service is designed for managed access to foundation models?
2. Which service supports custom model training and deployment?
3. Which service extracts text and structured data from forms?
4. Which service converts recorded speech to text?
5. Which service converts text into spoken audio?
6. Which service supports sentiment analysis?
7. Which service provides object storage for datasets?
8. Which service controls AWS resource permissions?
9. Which service records supported API activity?
10. Which service is suited to orchestrating multi-step workflows?

### Answers

1. Amazon Bedrock.
2. Amazon SageMaker AI.
3. Amazon Textract.
4. Amazon Transcribe.
5. Amazon Polly.
6. Amazon Comprehend.
7. Amazon S3.
8. AWS IAM.
9. AWS CloudTrail.
10. AWS Step Functions.

## 12. Revision Checklist

* [ ] Explain Amazon Bedrock and SageMaker AI.
* [ ] Match common AWS AI services to their primary tasks.
* [ ] Recognize supporting storage, API, security, and monitoring services.
* [ ] Select services based on the business requirement.
* [ ] Understand that availability and capabilities can vary by Region and configuration.
* [ ] Verify current service status before relying on older services.

## 13. Official Resources

* AWS AI: https://aws.amazon.com/ai/
* AWS Machine Learning: https://aws.amazon.com/machine-learning/
* Amazon Bedrock: https://aws.amazon.com/bedrock/
* Amazon SageMaker AI: https://aws.amazon.com/sagemaker/
* AWS Analytics: https://aws.amazon.com/big-data/datalakes-and-analytics/

---

**Exam focus:** Identify the AWS service whose primary capability most closely matches the requirement in the question.
