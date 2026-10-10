# 10 — AI Prompt Engineering and RAG Fundamentals

## 1. Learning Objectives

* Understand prompt engineering and common prompting techniques.
* Construct clear and effective prompts.
* Recognize prompt injection and instruction-conflict risks.
* Explain embeddings, vector search, and semantic retrieval.
* Describe the RAG lifecycle.
* Understand how prompt engineering and RAG complement each other.

## 2. What Is Prompt Engineering?

Prompt engineering is the practice of designing inputs and instructions to guide a generative AI model toward a desired result.

A prompt may include:

* Instructions.
* Background context.
* User input.
* Examples.
* Constraints.
* Output-format requirements.
* Retrieved information.

Effective prompts improve task clarity, but they cannot guarantee that the model will always produce correct or safe results.

## 3. Components of an Effective Prompt

### Task

Clearly define what the model must do.

### Context

Provide relevant background information.

### Constraints

Specify limitations, boundaries, or prohibited behavior.

### Output Format

Describe the expected structure, such as JSON, a table, or a concise paragraph.

### Examples

Provide demonstrations when they help clarify the desired response.

### Evidence Requirements

Explain which sources the model should use and how to handle missing information.

## 4. Prompting Techniques

### 4.1 Zero-Shot Prompting

The model receives instructions without examples.

Example:

"Classify this support ticket as Billing, Technical Support, or Account Access."

Useful when the task is straightforward and the model already understands the requested format.

### 4.2 Few-Shot Prompting

The prompt includes examples of inputs and desired outputs.

Example:

* Input: "I was charged twice." Output: Billing.
* Input: "I cannot sign in." Output: Account Access.
* Input: "The application crashes." Output: Technical Support.

Then the model classifies a new ticket.

Few-shot prompting can clarify task boundaries but consumes additional context tokens.

### 4.3 Role Prompting

The prompt assigns a role or perspective.

Example:

"You are a technical documentation assistant. Explain the procedure for a junior system administrator."

A role can shape tone and task framing but does not grant expertise, permissions, or factual guarantees.

### 4.4 Structured Prompting

The prompt specifies a required output structure.

Example:

"Return valid JSON with the fields `category`, `priority`, and `summary`."

Validate the result with a parser or schema validator because instructions alone do not guarantee valid JSON.

### 4.5 Context-Grounded Prompting

The prompt supplies trusted source material and asks the model to use it.

Example:

"Answer the question using only the policy excerpt below. If the excerpt does not provide the answer, state that the information is unavailable."

This approach can reduce unsupported answers, especially when paired with verification and retrieval.

## 5. Improving Prompt Quality

A useful process is:

1. Define the business task.
2. Identify the intended audience.
3. Provide necessary context.
4. Specify the desired output.
5. Define evidence and uncertainty requirements.
6. Test representative examples.
7. Review failure cases.
8. Refine the prompt.
9. Version and evaluate changes.

Avoid adding unnecessary instructions that make the prompt longer without improving the result.

## 6. Prompt Engineering Limitations

Prompt engineering cannot reliably:

* Guarantee factual accuracy.
* Eliminate hallucinations.
* Replace access-control mechanisms.
* Prevent every prompt injection.
* Make an unsupported model capability available.
* Replace appropriate testing and monitoring.

Use application logic and security controls for requirements that must be enforced consistently.

## 7. Prompt Injection

Prompt injection occurs when malicious input attempts to manipulate the model's instructions or behavior.

Examples:

* A document instructs the model to reveal secrets.
* A webpage tells an agent to call an unauthorized tool.
* A user attempts to bypass intended restrictions.

### Mitigation

* Treat external content as untrusted.
* Clearly separate application instructions from retrieved data.
* Avoid exposing secrets to the model.
* Restrict connected tools.
* Validate tool calls.
* Enforce permissions outside the model.
* Test adversarial scenarios.
* Require approval for consequential actions.

Prompt formatting alone is not a complete defense.

## 8. What Is Retrieval-Augmented Generation?

Retrieval-Augmented Generation (RAG) combines information retrieval with generative AI.

Instead of relying only on information learned during training, the application retrieves relevant external information and supplies it as context for the response.

RAG is especially useful for:

* Internal company documents.
* Frequently updated information.
* Technical documentation.
* Product manuals.
* Knowledge-base question answering.
* Domain-specific information.

## 9. RAG Architecture

A common RAG system has two stages.

### Stage A: Document Ingestion

1. Collect source documents.
2. Extract text and relevant metadata.
3. Split documents into chunks.
4. Generate embeddings.
5. Store embeddings and searchable content in an appropriate retrieval system.
6. Preserve document identifiers and access-control metadata.

### Stage B: Query and Generation

1. Receive the user's question.
2. Authenticate and authorize the user.
3. Generate a query representation when needed.
4. Retrieve relevant content.
5. Filter results according to permissions.
6. Construct a prompt with the retrieved context.
7. Invoke a foundation model.
8. Validate the output.
9. Return the answer and source references where supported.

The exact implementation depends on the retrieval system and model.

## 10. Embeddings

An embedding is a numerical vector representing content such as a document, passage, image, or query.

Embedding models are commonly used to represent text so that semantically related content can be retrieved.

Example:

Query: "How can I regain access to my account?"

Potentially relevant document: "Password reset and account recovery guide."

The query and document can be related even when they do not use identical words.

## 11. Vector Search and Similarity

A vector retrieval system stores or indexes embeddings and searches for relevant vectors.

Common similarity measures include:

* Cosine similarity.
* Dot product.
* Euclidean distance.

The suitable measure depends on the embedding model and retrieval implementation.

### Semantic Search vs. Keyword Search

**Keyword search** matches words or terms.

**Semantic search** attempts to find content related in meaning, even when exact wording differs.

Many practical systems combine semantic retrieval, keyword retrieval, metadata filtering, and reranking.

## 12. Chunking

Chunking divides documents into smaller pieces for indexing and retrieval.

### Small Chunks

Advantages:

* More focused retrieval.
* Less irrelevant text in the context.

Limitations:

* May lose surrounding context.
* May split related information across multiple chunks.

### Large Chunks

Advantages:

* Preserve more context.
* May keep related ideas together.

Limitations:

* Can include irrelevant material.
* Consume more context tokens.
* May reduce retrieval precision.

Chunk size and overlap should be tested against the document types and evaluation queries.

## 13. RAG Evaluation

RAG quality depends on both retrieval and generation.

### Retrieval Quality

Assess whether the system retrieves the correct evidence.

Possible measures include precision at k, recall at k, and ranking-related metrics.

### Generation Quality

Assess whether the final answer:

* Is correct.
* Uses the retrieved evidence.
* Answers the question.
* Avoids unsupported claims.
* Provides accurate citations.
* Follows the requested format.

### Operational Quality

Measure latency, cost, reliability, and access-control behavior.

A strong generator cannot compensate reliably for missing or incorrect retrieval results.

## 14. RAG vs. Fine-Tuning

| RAG                                                  | Fine-tuning                                                            |
| ---------------------------------------------------- | ---------------------------------------------------------------------- |
| Retrieves external content at inference time         | Uses additional training to modify model parameters                    |
| Suitable for changing or source-specific knowledge   | Suitable for adapting task behavior or specialized patterns            |
| Can return source references                         | Does not inherently provide citations                                  |
| Requires retrieval and data-ingestion infrastructure | Requires training data and supported customization resources           |
| Can be updated by refreshing indexed data            | Knowledge changes may require additional training or another mechanism |

RAG and fine-tuning can be combined when appropriate.

## 15. Amazon Bedrock and RAG

Amazon Bedrock provides features for building generative AI applications, including supported Knowledge Bases functionality.

A Bedrock Knowledge Base can help manage supported ingestion and retrieval workflows, reducing the amount of custom retrieval infrastructure an application must implement.

When evaluating a solution, consider:

* Supported data sources.
* Retrieval configuration.
* Embedding model compatibility.
* Metadata filtering.
* Access-control requirements.
* Source attribution.
* Model and Region availability.
* Current pricing.

## 16. Practical Example

**Business requirement:** Build an internal assistant that answers employee questions using company policies.

Recommended approach:

1. Store approved policy documents.
2. Index them through a suitable retrieval workflow.
3. Authenticate employees.
4. Restrict retrieval to authorized documents.
5. Retrieve the most relevant passages.
6. Instruct the model to answer using the supplied evidence.
7. Return supporting references when available.
8. Record appropriate operational metrics.
9. Evaluate retrieval accuracy and answer quality.
10. Refresh the index when policies change.

Do not assume that a prompt such as "Never reveal confidential documents" can replace actual authorization.

## 17. Knowledge Check

1. What is prompt engineering?
2. How does few-shot prompting differ from zero-shot prompting?
3. Why should generated JSON be validated?
4. What is prompt injection?
5. What is an embedding?
6. Why is chunking important in RAG?
7. How does semantic search differ from keyword search?
8. What are the two main stages of a RAG workflow?
9. Why must RAG evaluate retrieval and generation separately?
10. How does RAG differ from fine-tuning?

### Answers

1. Designing prompts to guide model behavior.
2. Few-shot prompting includes examples; zero-shot prompting does not.
3. Models may produce invalid JSON or violate the expected schema.
4. Malicious input that attempts to manipulate model behavior.
5. A numerical vector representation of content.
6. It determines the size and context of retrievable document segments.
7. Semantic search targets meaning; keyword search targets matching terms.
8. Document ingestion and query-time retrieval/generation.
9. Incorrect retrieval can lead to incorrect answers even when generation is otherwise strong.
10. RAG retrieves external context; fine-tuning updates model parameters through additional training.

## 18. Revision Checklist

* [ ] Identify prompt components and prompting techniques.
* [ ] Understand prompt injection and its mitigations.
* [ ] Explain embeddings and vector search.
* [ ] Understand document chunking.
* [ ] Describe the complete RAG lifecycle.
* [ ] Distinguish semantic and keyword search.
* [ ] Compare RAG with fine-tuning.
* [ ] Recognize Amazon Bedrock Knowledge Bases.
* [ ] Evaluate retrieval, generation, security, latency, and cost.

## 19. Official Resources

* Amazon Bedrock: https://aws.amazon.com/bedrock/
* Bedrock Knowledge Bases: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html
* AWS Machine Learning: https://aws.amazon.com/machine-learning/

---

**Exam focus:** Recognize effective prompting strategies, explain how RAG works, and identify the appropriate approach for grounding model responses in external knowledge.
