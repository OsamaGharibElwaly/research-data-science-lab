# 01 — Fundamentals of AI and Machine Learning

## 1. Learning Objectives

By the end of this module, you should be able to:

* Define Artificial Intelligence (AI), Machine Learning (ML), Deep Learning (DL), and Generative AI.
* Distinguish between supervised, unsupervised, and reinforcement learning.
* Understand common ML problem types and algorithms.
* Explain the ML lifecycle and basic model evaluation concepts.
* Recognize common AI use cases and AWS-related terminology.

## 2. Artificial Intelligence (AI)

Artificial Intelligence is the field of computer science focused on building systems that perform tasks associated with human intelligence, such as reasoning, learning, understanding language, recognizing images, and making decisions.

### Common AI Applications

* Natural language processing and translation.
* Computer vision and image recognition.
* Recommendation systems.
* Fraud detection.
* Virtual assistants and chatbots.
* Forecasting and predictive analytics.

## 3. Machine Learning (ML)

Machine Learning is a subset of AI that enables systems to learn patterns from data and use those patterns to make predictions or decisions without explicitly programming every rule.

### Traditional Programming vs. Machine Learning

**Traditional programming:**

Input data + Explicit rules → Output

**Machine learning training:**

Training data + Learning algorithm → Trained model

**Machine learning inference:**

New input data + Trained model → Prediction

### Important Terminology

* **Dataset:** A collection of data used for analysis or model development.
* **Feature:** An input variable used by a model.
* **Label:** The target value a supervised model learns to predict.
* **Algorithm:** A procedure used to learn patterns from data.
* **Model:** The learned representation produced by training.
* **Training:** The process of learning model parameters from data.
* **Inference:** Using a trained model to generate predictions.
* **Hyperparameter:** A configuration value set before or during training, such as learning rate.
* **Overfitting:** A model learns training data too closely and generalizes poorly.
* **Underfitting:** A model fails to capture important patterns in the data.
* **Generalization:** The ability to perform well on previously unseen data.

## 4. Types of Machine Learning

### 4.1 Supervised Learning

Supervised learning trains a model using labeled examples.

**Classification:** Predicts a category.

Examples:

* Spam or not spam.
* Fraudulent or legitimate transaction.
* Customer churn or retention.

**Regression:** Predicts a numerical value.

Examples:

* House prices.
* Product demand.
* Delivery time.

Common algorithms include linear regression, logistic regression, decision trees, random forests, and support vector machines.

### 4.2 Unsupervised Learning

Unsupervised learning identifies patterns in data without predefined target labels.

**Clustering:** Groups similar observations.

Example: Segmenting customers according to purchasing behavior.

**Dimensionality reduction:** Reduces the number of input variables while preserving useful information.

Example: Compressing high-dimensional data for visualization.

Common techniques include K-means clustering, hierarchical clustering, and principal component analysis (PCA).

### 4.3 Reinforcement Learning

Reinforcement learning trains an agent to choose actions through interaction with an environment.

Key concepts:

* **Agent:** The decision-making entity.
* **Environment:** The system in which the agent operates.
* **Action:** A choice made by the agent.
* **Reward:** Feedback indicating the value of an action.
* **Policy:** A strategy for selecting actions.

Example: Training a robot to navigate an environment while maximizing rewards.

## 5. Deep Learning

Deep Learning is a subset of ML that uses neural networks with multiple layers to learn complex patterns.

Common applications include speech recognition, computer vision, language modeling, and generative AI.

Important architectures:

* **CNNs:** Commonly used for image-related tasks.
* **RNNs:** Designed for sequential data; traditional examples include time-series and text processing.
* **Transformers:** Use attention mechanisms and are widely used in modern language models.
* **Autoencoders:** Learn compressed representations of data.
* **GANs:** Use competing generator and discriminator networks to generate synthetic data.

## 6. Generative AI

Generative AI creates new content based on patterns learned from training data.

It can generate:

* Text and summaries.
* Images and artwork.
* Audio and speech.
* Video.
* Code and structured outputs.

Generative AI differs from traditional predictive ML because its primary objective is often to produce new content rather than only assign labels or predict a numerical target.

A large language model (LLM) is a model designed to process and generate language. Foundation models are trained on broad datasets and can be adapted to many downstream tasks.

## 7. The Machine Learning Lifecycle

1. Define the business problem.
2. Collect relevant data.
3. Clean and prepare the data.
4. Select an appropriate algorithm.
5. Train the model.
6. Evaluate the model.
7. Deploy the model.
8. Monitor performance and data quality.
9. Retrain or update the model when needed.

The lifecycle is iterative. Monitoring can reveal data drift, changing business requirements, or degraded model performance.

## 8. Model Evaluation

### Classification Metrics

* **Accuracy:** Proportion of all predictions that are correct.
* **Precision:** Proportion of positive predictions that are actually positive.
* **Recall:** Proportion of actual positive cases correctly identified.
* **F1 score:** Harmonic mean of precision and recall.

Accuracy can be misleading when classes are highly imbalanced.

Example: If only 1% of transactions are fraudulent, a model that predicts every transaction as legitimate achieves 99% accuracy but detects no fraud.

### Regression Metrics

* **MAE:** Mean absolute error.
* **MSE:** Mean squared error.
* **RMSE:** Root mean squared error.

Lower error values generally indicate better predictive performance when comparing models on the same dataset and metric.

### Data Splits

* **Training set:** Used to fit the model.
* **Validation set:** Used to compare models and tune hyperparameters.
* **Test set:** Used for final evaluation on held-out data.

Avoid data leakage: information unavailable at prediction time must not improperly influence training or evaluation.

## 9. AWS Context

Amazon Web Services provides cloud infrastructure and managed services for AI and ML.

Examples include:

* **Amazon SageMaker AI:** Build, train, deploy, and manage ML models.
* **Amazon Bedrock:** Build generative AI applications using supported foundation models through managed APIs.
* **Amazon Rekognition:** Analyze images and videos.
* **Amazon Textract:** Extract text and structured information from documents.
* **Amazon Transcribe:** Convert speech into text.
* **Amazon Polly:** Convert text into speech.
* **Amazon Comprehend:** Perform NLP tasks such as entity recognition and sentiment analysis.

Learn each service's primary purpose rather than memorizing service names alone.

## 10. Key Exam Distinctions

| Concept                | Main purpose                                                       |
| ---------------------- | ------------------------------------------------------------------ |
| Supervised learning    | Learn from labeled examples                                        |
| Unsupervised learning  | Discover patterns without target labels                            |
| Reinforcement learning | Learn actions through rewards                                      |
| Classification         | Predict categories                                                 |
| Regression             | Predict numerical values                                           |
| Deep learning          | Learn complex patterns using multilayer neural networks            |
| Generative AI          | Generate new content                                               |
| Training               | Learn model parameters                                             |
| Inference              | Produce outputs from a trained model                               |
| SageMaker AI           | ML development and lifecycle platform                              |
| Amazon Bedrock         | Managed access to foundation models for generative AI applications |

## 11. Knowledge Check

1. Which type of ML uses labeled examples?
2. Is predicting monthly sales a classification or regression task?
3. Which ML approach is suitable for grouping customers without predefined categories?
4. What is the difference between training and inference?
5. Why can accuracy be misleading for fraud detection?
6. Which AWS service provides managed access to foundation models?
7. What is overfitting?
8. Which evaluation metric balances precision and recall?

### Answers

1. Supervised learning.
2. Regression.
3. Unsupervised learning, commonly clustering.
4. Training learns model parameters; inference uses the trained model.
5. A model may achieve high accuracy by predicting only the majority class.
6. Amazon Bedrock.
7. Learning training-specific patterns that do not generalize well to unseen data.
8. F1 score.

## 12. Revision Checklist

* [ ] Explain AI, ML, deep learning, and generative AI.
* [ ] Distinguish the three major ML learning approaches.
* [ ] Identify classification and regression problems.
* [ ] Understand features, labels, training, inference, and hyperparameters.
* [ ] Recognize overfitting, underfitting, and data leakage.
* [ ] Understand common evaluation metrics.
* [ ] Match major AWS AI services to their primary use cases.

## 13. Official Resources

* AWS Certified AI Practitioner: https://aws.amazon.com/certification/certified-ai-practitioner/
* AWS Machine Learning: https://aws.amazon.com/machine-learning/
* Amazon SageMaker AI: https://aws.amazon.com/sagemaker/
* Amazon Bedrock: https://aws.amazon.com/bedrock/

---

**Exam focus:** Understand the concepts, select the appropriate ML approach for a scenario, and recognize the AWS service best suited to the described task.
