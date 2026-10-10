# 03 — Applications of Foundation Models

## 1. Learning Objectives

* Identify common foundation-model application patterns.
* Match business problems to appropriate generative AI capabilities.
* Understand chatbots, summarization, extraction, classification, and code generation.
* Explain RAG, agents, and tool use at a high level.
* Recognize model-selection considerations and application limitations.

## 2. What Is a Foundation-Model Application?

A foundation-model application integrates a pretrained model into a business process or user-facing product.

The model may be used directly through an API or combined with retrieval, application logic, databases, tools, and human review.

A typical application includes:

1. User input.
2. Input validation and preprocessing.
3. Prompt construction.
4. Model invocation.
5. Output validation.
6. Optional retrieval or tool execution.
7. Response delivery.
8. Monitoring and evaluation.

Not every application requires all these components.

## 3. Common Application Patterns

### 3.1 Text Generation

Produces new written content based on instructions.

Examples:

* Drafting emails.
* Generating product descriptions.
* Preparing reports.
* Creating marketing content.

Key risks include factual errors, inappropriate content, and inconsistent tone.

### 3.2 Summarization

Condenses a longer source into a shorter version while preserving important information.

Examples:

* Meeting summaries.
* Customer-support case summaries.
* Research-paper summaries.
* Executive reports.

For reliable summarization, provide the source material and verify that key facts are preserved.

### 3.3 Question Answering

Responds to questions using model knowledge, supplied context, or retrieved documents.

Examples:

* Frequently asked questions.
* Internal policy assistants.
* Product-support chatbots.
* Technical documentation assistants.

For private or frequently updated organizational information, retrieval may be more appropriate than relying solely on model knowledge.

### 3.4 Information Extraction

Identifies specified fields within unstructured content.

Example: Extracting invoice number, invoice date, supplier, and total amount from a document.

Structured output may be represented as JSON, but generated JSON must still be validated against a schema.

### 3.5 Classification

Assigns content to predefined categories.

Examples:

* Categorizing support tickets.
* Identifying review sentiment.
* Routing requests to the correct department.

Traditional ML may be cheaper or more consistent for high-volume, well-defined classification tasks. A foundation model may be useful when instructions or categories change frequently or require contextual understanding.

### 3.6 Translation and Rewriting

Transforms text into another language or style.

Examples:

* Translating customer communications.
* Simplifying technical documentation.
* Adjusting tone for different audiences.

Quality depends on language coverage, context, terminology, and the consequences of errors.

### 3.7 Code Generation

Generates code, explains existing code, or assists with debugging.

Examples:

* Creating boilerplate.
* Writing unit-test drafts.
* Explaining error messages.
* Suggesting SQL queries.

Generated code must be reviewed and tested for correctness, security, and maintainability.

### 3.8 Multimodal Applications

Use combinations of text, image, audio, video, or other modalities.

Examples:

* Answering questions about images.
* Summarizing recordings.
* Analyzing visual product defects.
* Creating descriptions of visual content.

Confirm that the selected model supports the required modalities and file formats.

## 4. Matching Business Problems to AI Capabilities

| Business requirement              | Suitable capability                         |
| --------------------------------- | ------------------------------------------- |
| Draft a customer email            | Text generation                             |
| Condense a long report            | Summarization                               |
| Find answers in internal policies | RAG-based question answering                |
| Extract fields from text          | Information extraction                      |
| Route support tickets             | Classification                              |
| Translate documentation           | Translation                                 |
| Generate a unit-test draft        | Code generation                             |
| Describe a product image          | Image understanding or multimodal inference |
| Retrieve similar documents        | Embedding-based semantic search             |

The best solution depends on accuracy requirements, data availability, cost, latency, and operational constraints.

## 5. Choosing a Foundation Model

Important selection factors include:

### Capability

Can the model perform the task at the required quality level?

### Modality

Does it support the required inputs and outputs, such as text, images, or audio?

### Context Window

Can it process the necessary amount of input and conversation history?

### Latency

Can it respond quickly enough for the user experience?

### Cost

Consider input tokens, output tokens, request volume, and any supporting infrastructure.

### Reliability

Does the model behave consistently across representative test cases?

### Security and Privacy

Can the application meet requirements for data handling, access control, and regulatory compliance?

### Availability

Is the model available in the intended AWS Region and deployment configuration?

### Customization

Can prompts, retrieval, fine-tuning, or other supported customization methods achieve the required behavior?

## 6. Prompt Templates and Reusable Components

Production applications often use templates rather than manually writing every prompt.

A prompt template can contain:

* Fixed system instructions.
* A task description.
* User-provided variables.
* Retrieved documents.
* Output requirements.

Example:

"Using only the supplied policy excerpts, answer the user's question. If the excerpts do not contain enough information, state that the answer is unavailable. Return the answer and the supporting document references."

Validate user inputs and retrieved text. Treat supplied documents as data, not as trusted instructions that can override application rules.

## 7. Retrieval-Augmented Generation in Applications

RAG is particularly useful when an application must answer questions using a controlled information source.

Example: An employee asks, "How many annual leave days can I carry over?"

A RAG system can retrieve the relevant HR policy section and ask the model to answer using that evidence.

### Benefits

* Uses organization-specific information.
* Can incorporate recently updated documents.
* Can return citations or source references.
* Reduces reliance on the model's internal knowledge alone.

### Risks

* The correct document may not be retrieved.
* Documents may be outdated.
* Similar documents may conflict.
* The model may misinterpret the retrieved content.
* Sensitive information may be exposed without access controls.

RAG systems should respect document permissions during retrieval, not merely after generating the answer.

## 8. Foundation Models and Agents

An AI agent combines a model with instructions, tools, and a process for choosing actions toward a goal.

Possible tools include:

* Search systems.
* Business APIs.
* Databases.
* Calculators.
* Ticketing systems.
* Inventory systems.

Example: A support agent may retrieve an order, check its delivery status, and draft a response.

An agent differs from a basic chatbot because it can select and execute supported actions through tools rather than only generating text.

### Agent Safety

* Restrict tool permissions.
* Validate tool inputs.
* Require confirmation for consequential actions when appropriate.
* Log operations.
* Apply timeouts and limits.
* Handle failures safely.
* Prevent untrusted input from controlling privileged operations.

Do not grant an agent broader permissions than its task requires.

## 9. Human-in-the-Loop Workflows

Human review is valuable when model outputs affect important decisions.

Examples:

* Medical information review.
* Financial recommendations.
* Legal document analysis.
* Hiring-related workflows.
* High-value refunds.
* Production infrastructure changes.

Human review should be designed into the workflow, with clear responsibility for approval and correction.

## 10. Application Quality and Evaluation

Evaluate applications against representative examples before deployment.

Useful measures include:

* Task accuracy.
* Relevance.
* Completeness.
* Groundedness.
* Citation correctness.
* Format compliance.
* Latency.
* Cost per request.
* User satisfaction.
* Safety and policy violations.

Use a test dataset that reflects realistic users, difficult questions, edge cases, and potentially adversarial inputs.

A model that performs well on a few demonstrations may still fail on production data.

## 11. AWS Services and Application Patterns

### Amazon Bedrock

Useful for building applications that invoke supported foundation models and use supported generative AI features.

Depending on the selected features, it can support model access, knowledge bases, guardrails, agents, and customization options.

### Amazon SageMaker AI

Useful for broader ML development, training, deployment, and model management workflows.

### AWS Lambda

Can run event-driven application logic and connect services without managing servers directly.

### Amazon S3

Can store documents, datasets, and other objects used by an AI application, subject to appropriate permissions and data-management controls.

### Amazon API Gateway

Can expose APIs that connect clients to application backends, including serverless inference workflows.

### Amazon CloudWatch

Supports monitoring through metrics, logs, and alarms for services and applications that integrate with it.

Choose services based on the architecture and required capabilities; not every generative AI application needs every service.

## 12. Example Architecture

A document question-answering application might use:

1. Amazon S3 to store source documents.
2. A supported ingestion process to prepare and index documents.
3. A vector retrieval system or supported knowledge-base configuration.
4. Amazon Bedrock to access a foundation model.
5. An application backend to authenticate users and manage requests.
6. Logging and monitoring to evaluate system behavior.

Architecture choices vary with scale, security, retrieval needs, and service availability.

## 13. Knowledge Check

1. Which capability is appropriate for condensing a long report?
2. When is RAG especially useful?
3. Why must generated JSON be validated?
4. What distinguishes an AI agent from a basic text-generation workflow?
5. Name four factors involved in model selection.
6. Why should document permissions be enforced during retrieval?
7. When is human approval particularly important?
8. Which AWS service provides managed access to foundation models?

### Answers

1. Summarization.
2. When the application needs relevant external or frequently updated knowledge.
3. The model may omit fields, use incorrect types, or produce invalid structures.
4. An agent can select and invoke tools to perform supported actions.
5. Capability, modality, latency, cost, security, context window, reliability, or availability.
6. To prevent unauthorized information from entering the model's context.
7. When errors can cause significant financial, legal, safety, or operational consequences.
8. Amazon Bedrock.

## 14. Revision Checklist

* [ ] Match business requirements to foundation-model capabilities.
* [ ] Understand generation, summarization, extraction, classification, and translation.
* [ ] Compare model capability, cost, latency, modality, and security.
* [ ] Explain reusable prompt templates.
* [ ] Identify where RAG adds value.
* [ ] Distinguish agents from simple chatbots.
* [ ] Understand least privilege and human approval.
* [ ] Recognize AWS services used in AI application architectures.

## 15. Official Resources

* Amazon Bedrock: https://aws.amazon.com/bedrock/
* AWS Generative AI: https://aws.amazon.com/generative-ai/
* Amazon SageMaker AI: https://aws.amazon.com/sagemaker/
* AWS Lambda: https://aws.amazon.com/lambda/
* Amazon S3: https://aws.amazon.com/s3/

---

**Exam focus:** Given a business scenario, identify the foundation-model capability, appropriate application pattern, key model-selection criteria, and relevant AWS service.
