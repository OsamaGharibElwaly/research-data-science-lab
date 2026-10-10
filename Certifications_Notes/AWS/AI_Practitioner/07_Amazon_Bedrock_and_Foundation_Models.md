# 07 — Amazon Bedrock and Foundation Models

## 1. Learning Objectives

* Explain Amazon Bedrock's purpose and core concepts.
* Understand foundation-model selection.
* Recognize model invocation and inference.
* Distinguish model customization, RAG, and prompt engineering.
* Understand Bedrock Knowledge Bases, Guardrails, and Agents at a high level.
* Identify security, evaluation, and cost considerations.

## 2. What Is Amazon Bedrock?

Amazon Bedrock is a managed AWS service for building generative AI applications with supported foundation models.

It provides a common service interface for accessing models from AWS and supported third-party providers.

Organizations can use Bedrock to build applications without managing the underlying foundation-model infrastructure directly.

## 3. Foundation Models in Bedrock

Foundation models may support different tasks and modalities.

Examples of model capabilities include:

* Text generation.
* Summarization.
* Conversational question answering.
* Embeddings.
* Image generation or understanding.
* Multimodal processing.

Not every model supports every capability. Check the model's supported modalities, context limits, Regions, API operations, and licensing or usage terms.

## 4. Selecting a Foundation Model

Consider the following criteria:

### Task Fit

Does the model support the required task?

### Quality

Does it perform well on representative examples?

### Latency

Can it meet response-time requirements?

### Cost

What are the expected input, output, and supporting infrastructure costs?

### Context Window

Can it process the required input and conversation context?

### Modality

Does it support the needed text, image, audio, or other inputs and outputs?

### Security and Data Handling

Does the model and application architecture meet organizational requirements?

### Availability

Is the model available in the intended AWS Region and account configuration?

A larger or more expensive model is not automatically the best choice. Evaluate alternatives against real requirements.

## 5. Model Invocation and Inference

Model invocation means sending a request to a model and obtaining its output.

A basic workflow:

1. Authenticate the request.
2. Prepare the prompt or input.
3. Select a supported model and invocation method.
4. Submit the request.
5. Receive the response.
6. Validate and process the output.
7. Return the result to the user.

Applications should handle timeouts, throttling, service errors, malformed responses, and unexpected model output.

Exact invocation APIs and permissions depend on the selected model and Bedrock features.

## 6. Prompt Engineering in Bedrock

Prompt engineering shapes model behavior through instructions, context, examples, and output requirements.

An effective prompt should:

* Define the task.
* Supply relevant context.
* Specify constraints.
* Define the output format.
* Avoid unnecessary ambiguity.

Example:

"Summarize the supplied customer feedback in five concise bullet points. Include recurring complaints and positive themes. Do not introduce claims absent from the source text."

For production use, test prompts against a representative evaluation set and maintain versions when changing important instructions.

## 7. Model Customization

Customization adapts a model to an application or domain.

Possible approaches include:

* Prompt engineering.
* Retrieval-Augmented Generation.
* Supported fine-tuning or other model customization methods.

### Prompt Engineering

Changes instructions and context without updating model weights.

Best suited to many task-definition, formatting, and behavior-guidance needs.

### RAG

Retrieves external information and supplies it to the model at inference time.

Best suited to applications that need relevant external documents, frequently updated knowledge, or source-grounded responses.

### Fine-Tuning

Uses additional training to adapt a supported model.

May be useful when a model needs more specialized behavior or task patterns that prompts alone do not reliably achieve.

The available customization options vary by model and service feature.

## 8. Amazon Bedrock Knowledge Bases

Knowledge Bases for Amazon Bedrock supports building retrieval workflows that connect foundation models to external information sources.

A typical RAG workflow includes:

1. Connect supported data sources.
2. Ingest and prepare documents.
3. Split content into chunks.
4. Generate embeddings.
5. Store searchable representations in a supported retrieval backend.
6. Retrieve relevant content for a query.
7. Supply retrieved context to a foundation model.
8. Generate an answer based on the available evidence.

### Benefits

* Makes external knowledge available to the model.
* Can support source-grounded question answering.
* Helps incorporate changing information without retraining a foundation model from scratch.
* Can simplify implementation through managed capabilities.

### Important Considerations

* Retrieval quality affects answer quality.
* Documents must be updated when information changes.
* Access controls must prevent unauthorized retrieval.
* Source citations should be checked for correctness.
* Retrieved content can contain malicious or misleading instructions.

A Knowledge Base does not guarantee that every generated answer is correct.

## 9. Amazon Bedrock Guardrails

Guardrails provides configurable controls for supported generative AI applications.

Depending on the feature and configuration, it can help address:

* Harmful content.
* Sensitive-information exposure.
* Denied topics.
* Some grounding-related risks.

### Example

A customer-service assistant should not return a response containing restricted personal information.

A suitable design can combine supported Guardrails controls with application-level authorization, data minimization, and output validation.

Guardrails are not a substitute for IAM, secure application logic, or appropriate data access policies.

## 10. Amazon Bedrock Agents

Agents for Amazon Bedrock helps build applications that use a foundation model to coordinate supported actions and interact with configured tools or APIs.

An agent may:

1. Interpret a user's goal.
2. Determine an appropriate next step.
3. Use a configured tool or action.
4. Process the result.
5. Continue or return a response.

### Example

A customer asks for an order update.

An agent could use a permitted order-lookup API, retrieve the order status, and produce a response based on the result.

### Agent Security

* Grant only necessary permissions.
* Validate inputs to connected APIs.
* Limit consequential actions.
* Use confirmation or approval when appropriate.
* Log important operations.
* Handle failed actions safely.

A foundation model should not be trusted to enforce permissions by itself.

## 11. Evaluation

Model evaluation helps determine whether a model or application is suitable for its intended use.

Assess:

* Accuracy and relevance.
* Groundedness.
* Completeness.
* Format compliance.
* Safety.
* Robustness.
* Latency.
* Cost.

Use representative prompts and expected outcomes. Include edge cases, ambiguous questions, and adversarial examples.

For RAG systems, evaluate retrieval quality as well as generation quality.

## 12. Security and Access

Amazon Bedrock applications should use suitable AWS identity and access controls.

Important practices:

* Apply least-privilege IAM policies.
* Restrict access to model invocation and management operations.
* Secure source documents and retrieval systems.
* Protect credentials.
* Monitor supported activity.
* Avoid unnecessary sensitive information in prompts and logs.
* Verify the relevant service's data-handling terms.

IAM controls access to AWS operations; application-level controls may also be required to restrict what individual users can ask or retrieve.

## 13. Cost and Performance

Costs depend on the selected model, supported pricing structure, usage, and additional features.

Possible cost factors include:

* Input and output tokens.
* Model or inference configuration.
* Embedding generation.
* Document ingestion.
* Retrieval infrastructure.
* Agent actions and supporting services.
* Logging and storage.
* Provisioned capacity, where applicable.

### Cost Optimization

* Select a model appropriate to the task.
* Keep prompts concise without removing necessary context.
* Limit unnecessary output length.
* Cache appropriate results when safe.
* Monitor usage.
* Set suitable quotas and alerts.
* Test performance before increasing traffic.

Pricing models vary by feature, model, and Region; consult current AWS pricing before estimating production costs.

## 14. Bedrock vs. SageMaker AI

| Amazon Bedrock                                                   | Amazon SageMaker AI                                                   |
| ---------------------------------------------------------------- | --------------------------------------------------------------------- |
| Managed access to supported foundation models                    | Broader ML development and lifecycle platform                         |
| Common choice for generative AI applications                     | Common choice for custom model training and deployment workflows      |
| Supports features such as Knowledge Bases and Agents             | Supports model-building, training, tuning, and deployment workflows   |
| Abstracts much of the underlying foundation-model infrastructure | Offers different levels of control over ML environments and workflows |

The services can complement each other in a larger architecture.

## 15. Scenario-Based Exam Practice

**Scenario A:** A company wants to build a chatbot using a supported foundation model without managing model infrastructure.

Recommended service: Amazon Bedrock.

**Scenario B:** A chatbot must answer questions using frequently updated internal documents.

Recommended approach: A Bedrock Knowledge Base or another suitable RAG implementation.

**Scenario C:** A model generates harmful responses that need additional controls.

Recommended consideration: Amazon Bedrock Guardrails, combined with application-level safeguards.

**Scenario D:** An application must look up an order through a controlled API.

Recommended consideration: An appropriately configured Bedrock agent or application workflow with restricted tool permissions.

**Scenario E:** A model's output format changes unpredictably.

Recommended actions: Improve the prompt, constrain the format where supported, validate the output, and evaluate the workflow.

## 16. Knowledge Check

1. What is Amazon Bedrock?
2. What factors should influence foundation-model selection?
3. What is model invocation?
4. How does RAG differ from fine-tuning?
5. What is the role of a Bedrock Knowledge Base?
6. What problem do Guardrails help address?
7. What distinguishes an agent from basic model invocation?
8. Why is least privilege important for agents?
9. Why must RAG applications evaluate retrieval quality?
10. How can an organization control model-related costs?

### Answers

1. A managed service for accessing supported foundation models and building generative AI applications.
2. Task fit, quality, latency, cost, modality, context window, security, and availability.
3. Sending an input to a model and receiving its output.
4. RAG retrieves external context at inference time; fine-tuning updates model parameters through additional training.
5. It supports retrieval of external knowledge for use in generative AI applications.
6. Certain risks such as harmful content, sensitive information, denied topics, and supported grounding-related issues.
7. An agent can coordinate supported actions through configured tools.
8. To limit unauthorized access and unintended actions.
9. Poor retrieval can supply irrelevant or incomplete evidence to the model.
10. Select suitable models, optimize prompts, monitor usage, and apply appropriate quotas and alerts.

## 17. Revision Checklist

* [ ] Explain Amazon Bedrock and foundation models.
* [ ] Understand model selection and invocation.
* [ ] Distinguish prompting, RAG, and fine-tuning.
* [ ] Explain Knowledge Bases, Guardrails, and Agents.
* [ ] Apply least privilege to model-connected tools.
* [ ] Understand evaluation, cost, and performance considerations.
* [ ] Distinguish Bedrock from SageMaker AI.

## 18. Official Resources

* Amazon Bedrock: https://aws.amazon.com/bedrock/
* Amazon Bedrock Documentation: https://docs.aws.amazon.com/bedrock/
* Bedrock Knowledge Bases: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html
* Bedrock Guardrails: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html
* Bedrock Agents: https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html

---

**Exam focus:** Understand when to use Bedrock, how foundation models are selected and invoked, and how RAG, Guardrails, Agents, and evaluation support generative AI applications.
