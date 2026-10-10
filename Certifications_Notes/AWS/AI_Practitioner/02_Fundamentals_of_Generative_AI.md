# 02 — Fundamentals of Generative AI

## 1. Learning Objectives

* Define generative AI and foundation models.
* Explain large language models and tokenization.
* Understand training, fine-tuning, and inference.
* Recognize the roles of prompts, embeddings, and attention.
* Identify generative AI benefits, limitations, and common use cases.

## 2. What Is Generative AI?

Generative AI is a category of AI that produces new content by learning statistical patterns and representations from data.

Examples include:

* Text generation and summarization.
* Image generation.
* Code generation.
* Speech synthesis.
* Question answering.
* Synthetic data generation.

Traditional discriminative models commonly predict labels or values. Generative models learn to produce new outputs consistent with learned patterns.

## 3. Foundation Models

A Foundation Model (FM) is a model trained on broad data that can be adapted to many tasks.

Foundation models may support:

* Text generation.
* Summarization.
* Translation.
* Question answering.
* Image understanding.
* Multimodal tasks.

A model's actual capabilities depend on its architecture, training data, available modalities, context window, and deployment configuration.

### Benefits

* Reuse one model across multiple tasks.
* Reduce the need to train a model from scratch.
* Accelerate application development.
* Adapt behavior using prompts, retrieval, or fine-tuning.

### Limitations

* May generate incorrect information.
* May reproduce biases in training data.
* Can have limited knowledge of recent events.
* May expose sensitive information if applications are poorly designed.
* Can incur significant inference costs.

## 4. Large Language Models (LLMs)

An LLM is a foundation model specialized in processing and generating language.

Many modern LLMs use the Transformer architecture and generate text by predicting the next token based on the preceding context.

Example:

Input: "The capital of France is"

Possible continuation: "Paris."

The model generates tokens iteratively until it reaches a stopping condition or generation limit.

## 5. Tokens and Tokenization

A token is a unit of text processed by a model. It may represent a word, part of a word, punctuation, or another text segment.

Tokenization converts text into token IDs that a model can process.

Why tokens matter:

* API usage may be billed according to input and output tokens.
* Context windows limit how much information can be processed in a request.
* Long prompts can increase latency and cost.
* Tokenization differs between models and languages.

Do not assume one token always equals one word.

## 6. Embeddings

An embedding is a numerical vector representing information such as text, images, or other content.

Embeddings are useful for:

* Semantic search.
* Document retrieval.
* Recommendation systems.
* Clustering.
* Similarity comparisons.
* Retrieval-Augmented Generation (RAG).

Semantically similar texts may have nearby vectors in an embedding space, depending on the model and similarity measure.

Example:

Query: "How can I reset my password?"

A semantic retrieval system may find a document titled "Account recovery instructions" even though the wording differs.

## 7. Attention and Transformers

Attention allows a model to weigh relationships between different parts of an input.

For language models, attention helps represent contextual relationships between tokens.

Transformers use attention mechanisms and other neural-network components to process sequences efficiently and learn complex language patterns.

Important distinction: attention is a mechanism, while a Transformer is a model architecture that incorporates attention.

## 8. Training and Adaptation

### Pretraining

A model learns general patterns from a large training corpus.

For many LLMs, pretraining involves predicting missing or subsequent tokens.

### Fine-Tuning

Fine-tuning continues training a pretrained model on a more specialized dataset to adapt its behavior.

Examples:

* Domain-specific language.
* Instruction following.
* Classification.
* Specialized response formats.

Fine-tuning can improve task-specific behavior but requires suitable data, evaluation, and resources.

### Inference

Inference is the process of running a trained model to produce an output.

Inference considerations include:

* Latency.
* Throughput.
* Input and output token counts.
* Model availability.
* Cost.
* Output quality.

## 9. Prompt Engineering

A prompt is the instruction and context provided to a generative model.

Effective prompts commonly specify:

1. **Task:** What the model should do.
2. **Context:** Relevant background information.
3. **Constraints:** What to include or avoid.
4. **Format:** The required output structure.
5. **Examples:** Demonstrations when helpful.

### Example

Weak prompt:

"Analyze this feedback."

Improved prompt:

"Classify each customer review as positive, neutral, or negative. Give one sentence explaining the classification. Return the result as JSON with the fields `sentiment` and `reason`. Do not invent information absent from the review."

### Prompting Techniques

* **Zero-shot prompting:** Give instructions without examples.
* **Few-shot prompting:** Include examples of desired behavior.
* **Role prompting:** Specify a useful role or perspective.
* **Structured prompting:** Define an output format or schema.
* **Chain-of-thought-style reasoning requests:** Ask for careful problem-solving; do not assume the model's explanations guarantee correctness.

A well-written prompt improves the chance of a useful response but does not guarantee factual accuracy.

## 10. Temperature and Output Controls

Generation parameters influence output behavior.

* **Temperature:** Influences randomness in token selection. Higher values often produce more varied outputs; lower values often produce more predictable outputs.
* **Maximum output tokens:** Limits the length of generated output.
* **Top-p sampling:** Restricts token selection to a probability mass determined by the configured threshold.

The exact behavior depends on the model and API. Not every model supports every parameter.

## 11. Hallucinations

A hallucination occurs when a generative model produces information that appears plausible but is false, unsupported, or fabricated.

Examples:

* Invented citations.
* Incorrect legal or technical statements.
* Fabricated product features.
* Incorrect answers presented confidently.

### Reducing Hallucination Risk

* Provide trusted source material.
* Use retrieval-augmented generation.
* Ask the model to distinguish evidence from uncertainty.
* Validate outputs against authoritative sources.
* Apply structured output validation.
* Use human review for high-impact decisions.

These methods reduce risk but do not eliminate hallucinations.

## 12. Multimodal AI

Multimodal models process or generate more than one type of information.

Modalities may include:

* Text.
* Images.
* Audio.
* Video.
* Structured or spatial data.

Examples:

* Asking questions about an image.
* Summarizing an audio recording.
* Generating captions for a video.
* Producing text and images in a combined workflow.

Always verify which input and output modalities a particular model supports.

## 13. Retrieval-Augmented Generation (RAG)

RAG combines information retrieval with generative AI.

Typical workflow:

1. Collect trusted documents.
2. Split documents into chunks.
3. Convert chunks into embeddings.
4. Store embeddings and metadata in a retrieval system.
5. Convert a user query into a suitable search representation.
6. Retrieve relevant content.
7. Provide retrieved content and the query to the model.
8. Generate a grounded answer.

### Why Use RAG?

* Incorporate internal or domain-specific knowledge.
* Provide information that may not be present in pretraining.
* Support document-based question answering.
* Improve traceability by returning sources.

RAG does not automatically guarantee correctness. Retrieval quality, document freshness, context selection, and model behavior all matter.

### RAG vs. Fine-Tuning

| RAG                                            | Fine-tuning                                               |
| ---------------------------------------------- | --------------------------------------------------------- |
| Retrieves external information at request time | Changes model parameters through additional training      |
| Useful for frequently changing knowledge       | Useful for adapting behavior or specialized task patterns |
| Can provide source documents                   | Does not inherently provide citations                     |
| Requires retrieval infrastructure              | Requires training data and fine-tuning resources          |

The two approaches can be combined.

## 14. AWS Generative AI Context

### Amazon Bedrock

Amazon Bedrock provides managed access to supported foundation models and capabilities for building generative AI applications.

Depending on the model and feature, it can support:

* Model invocation.
* Prompt experimentation.
* Knowledge bases and RAG workflows.
* Guardrails.
* Agents and tool-oriented workflows.
* Model customization options.

Specific features vary by model, Region, and service configuration.

### Amazon SageMaker AI

Amazon SageMaker AI provides tools for building, training, tuning, deploying, and managing ML models. It is relevant when teams need greater control over ML workflows and infrastructure.

A useful exam distinction:

* Choose **Amazon Bedrock** when the scenario emphasizes building generative AI applications using managed foundation models.
* Choose **Amazon SageMaker AI** when the scenario emphasizes broader ML development, training, tuning, and deployment workflows.

## 15. Knowledge Check

1. What is a foundation model?
2. What does tokenization do?
3. What is an embedding?
4. How does fine-tuning differ from inference?
5. What is a hallucination?
6. What is the main purpose of RAG?
7. What does temperature influence?
8. Which AWS service is designed for managed access to foundation models?

### Answers

1. A broadly trained model adaptable to many tasks.
2. Converts input text into tokens or token IDs for processing.
3. A numerical vector representation of information.
4. Fine-tuning updates model parameters; inference uses a model to generate outputs.
5. An incorrect or unsupported generated claim.
6. Retrieve relevant external information and provide it to a generative model.
7. The randomness or diversity of generated token selection.
8. Amazon Bedrock.

## 16. Revision Checklist

* [ ] Explain generative AI and foundation models.
* [ ] Understand LLMs, tokens, embeddings, and attention.
* [ ] Distinguish pretraining, fine-tuning, and inference.
* [ ] Identify effective prompting techniques.
* [ ] Explain temperature and context-window limitations.
* [ ] Describe hallucinations and mitigation methods.
* [ ] Explain multimodal AI and RAG.
* [ ] Distinguish RAG from fine-tuning.
* [ ] Identify Amazon Bedrock's role.

## 17. Official Resources

* AWS Generative AI: https://aws.amazon.com/generative-ai/
* Amazon Bedrock: https://aws.amazon.com/bedrock/
* AWS Machine Learning: https://aws.amazon.com/machine-learning/

---

**Exam focus:** Recognize foundation-model concepts, prompting techniques, model limitations, and the distinction between RAG, fine-tuning, and ordinary inference.
