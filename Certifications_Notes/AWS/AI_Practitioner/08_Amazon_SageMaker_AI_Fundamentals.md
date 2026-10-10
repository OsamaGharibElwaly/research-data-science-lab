# 08 — Amazon SageMaker AI Fundamentals

## 1. Learning Objectives

* Explain the purpose of Amazon SageMaker AI.
* Understand the machine learning lifecycle on AWS.
* Identify data preparation, training, tuning, deployment, and monitoring concepts.
* Distinguish training from inference.
* Recognize common model evaluation and operational practices.
* Understand when SageMaker AI is appropriate compared with Amazon Bedrock.

## 2. What Is Amazon SageMaker AI?

Amazon SageMaker AI is an AWS service that supports building, training, tuning, deploying, and managing machine learning models.

It is relevant when organizations need to develop custom models or manage ML workflows.

Common use cases include:

* Demand forecasting.
* Fraud detection.
* Classification.
* Regression.
* Customer segmentation.
* Custom deep learning.
* Model deployment and inference.

The exact available features and workflow options depend on the selected SageMaker AI capabilities and configuration.

## 3. The Machine Learning Lifecycle

A typical ML lifecycle consists of:

1. Define the business problem.
2. Collect and prepare data.
3. Explore the dataset.
4. Engineer relevant features.
5. Split the dataset.
6. Select an algorithm.
7. Train the model.
8. Tune hyperparameters.
9. Evaluate performance.
10. Deploy the model.
11. Monitor production behavior.
12. Retrain or update when necessary.

The process is iterative. Evaluation may reveal that the data, features, algorithm, or business assumptions need to change.

## 4. Data Preparation

High-quality data is essential for reliable model performance.

Common data preparation tasks include:

* Handling missing values.
* Removing duplicates.
* Correcting inconsistent formats.
* Investigating outliers.
* Encoding categorical features.
* Scaling numerical features when appropriate.
* Creating useful features.
* Checking labels.
* Reviewing class imbalance.
* Protecting sensitive information.

### Data Splitting

* **Training data:** Used to fit model parameters.
* **Validation data:** Used for model comparison and hyperparameter tuning.
* **Test data:** Used for final evaluation.

The test set should not be repeatedly used to make modeling decisions, because doing so can undermine its value as an unbiased evaluation set.

### Data Leakage

Data leakage occurs when training or evaluation uses information that would not legitimately be available at prediction time.

Example: A model predicting whether a customer will cancel is trained using a feature recorded only after the cancellation occurred.

Prevent leakage through appropriate feature design, temporal splitting when necessary, and careful preprocessing.

## 5. Model Training

Training is the process of learning model parameters from a dataset.

A training workflow typically specifies:

* Training data.
* Algorithm or model architecture.
* Hyperparameters.
* Compute resources.
* Training code or supported training configuration.
* Output location for model artifacts.

Training results in a model artifact or another supported output that can be evaluated and potentially deployed.

The choice of compute should reflect dataset size, model complexity, training time, and budget.

## 6. Algorithms and Problem Types

### Classification

Predicts a category.

Examples:

* Fraud or legitimate.
* Churn or retention.
* Approved or rejected, where appropriate to the business context.

### Regression

Predicts a numerical value.

Examples:

* House price.
* Monthly demand.
* Delivery duration.

### Clustering

Groups observations based on similarity without predefined labels.

Example: Customer segmentation.

### Deep Learning

Uses multilayer neural networks for complex patterns, including image, language, and other high-dimensional tasks.

SageMaker AI supports workflows for different algorithms and frameworks, subject to the selected features and configuration.

## 7. Hyperparameter Tuning

Hyperparameters are configuration values selected before or during training rather than learned directly as ordinary model parameters.

Examples include:

* Learning rate.
* Batch size.
* Tree depth.
* Number of training iterations.
* Regularization strength.

Hyperparameter tuning evaluates candidate configurations and compares their results using a selected objective metric.

For example, a classification task might tune a model to maximize F1 score when both precision and recall are important.

Tuning consumes time and compute, so define reasonable search ranges and resource limits.

## 8. Model Evaluation

The appropriate metric depends on the problem.

### Classification Metrics

* Accuracy.
* Precision.
* Recall.
* F1 score.
* ROC-AUC, where appropriate.

### Regression Metrics

* Mean Absolute Error (MAE).
* Mean Squared Error (MSE).
* Root Mean Squared Error (RMSE).

### Business Evaluation

A technically accurate model may still be unsuitable if it is too slow, too expensive, difficult to maintain, or poorly aligned with business objectives.

Evaluate both model quality and operational requirements.

## 9. Deployment and Inference

Inference uses a trained model to generate predictions.

Common deployment patterns include:

### Real-Time Inference

Designed for requests that require low-latency responses through a supported endpoint or inference configuration.

Example: Scoring a transaction during checkout.

### Batch Inference

Processes many records without requiring a separate real-time response for every request.

Example: Generating overnight predictions for a large customer dataset.

### Asynchronous Inference

Useful for supported workloads involving larger payloads or processing times that do not fit a typical synchronous request pattern.

### Serverless Inference

A supported deployment option for certain workloads that avoids managing provisioned endpoint instances directly, subject to service limits and configuration.

The best deployment pattern depends on latency, traffic, payload size, throughput, availability, and cost.

## 10. Model Monitoring

Model performance can degrade after deployment.

Potential causes include:

* Changes in input data.
* Changes in customer behavior.
* Changes in business processes.
* Data quality problems.
* Infrastructure failures.
* New types of input not represented in training data.

### Data Drift

Input data distributions change over time.

### Concept Drift

The relationship between input features and the target changes.

### Operational Monitoring

Track relevant signals such as:

* Latency.
* Error rates.
* Throughput.
* Resource utilization.
* Data quality.
* Prediction distributions.
* Model quality when ground-truth labels become available.

Monitoring does not automatically solve model degradation. Teams need procedures for investigation, retraining, validation, and controlled rollout.

## 11. MLOps Fundamentals

MLOps applies software engineering, automation, monitoring, and operational discipline to the ML lifecycle.

Common practices include:

* Versioning data and code.
* Tracking experiments.
* Reproducible training.
* Automated testing.
* Model evaluation gates.
* Controlled deployment.
* Monitoring.
* Rollback procedures.
* Documented model changes.

MLOps helps make ML systems more repeatable, maintainable, and reliable.

## 12. SageMaker AI and Supporting AWS Services

### Amazon S3

Can store training data, processed datasets, and model artifacts.

### AWS IAM

Controls access to resources and operations.

### Amazon CloudWatch

Supports monitoring through metrics, logs, and alarms for integrated components.

### AWS CloudTrail

Records supported account activity and API events.

### AWS Glue

Can support data integration and preparation workflows.

### Amazon Athena

Can query supported data sources such as data stored in Amazon S3.

These services may complement SageMaker AI but are not all required for every project.

## 13. SageMaker AI vs. Amazon Bedrock

| Requirement                                                                           | Typical starting point |
| ------------------------------------------------------------------------------------- | ---------------------- |
| Build a generative AI application using managed foundation models                     | Amazon Bedrock         |
| Train a custom predictive model                                                       | Amazon SageMaker AI    |
| Tune and deploy custom ML workflows                                                   | Amazon SageMaker AI    |
| Use a supported foundation model through a managed API                                | Amazon Bedrock         |
| Manage broader ML experimentation and deployment workflows                            | Amazon SageMaker AI    |
| Ground a generative AI assistant in external documents using managed Bedrock features | Amazon Bedrock         |

Some architectures use both services. Selection depends on the task and required control.

## 14. Scenario-Based Exam Practice

**Scenario A:** A company wants to predict future product demand from historical sales.

Approach: Build a forecasting model using an appropriate ML workflow, potentially with SageMaker AI.

**Scenario B:** A model performs well on training data but poorly on unseen records.

Possible issue: Overfitting, data leakage, or distribution differences.

**Scenario C:** A fraud model must score transactions as they arrive.

Potential deployment: A suitable real-time inference configuration.

**Scenario D:** A company needs to generate predictions for millions of records overnight.

Potential deployment: A suitable batch inference workflow.

**Scenario E:** Input data changes significantly after deployment.

Recommended action: Investigate data drift, assess model quality, and determine whether retraining or other remediation is required.

**Scenario F:** A team needs reproducible training and controlled model releases.

Recommended practices: Versioning, automated evaluation, deployment controls, monitoring, and rollback planning.

## 15. Knowledge Check

1. What is Amazon SageMaker AI?
2. What is the purpose of a validation dataset?
3. What is data leakage?
4. How do training and inference differ?
5. What is hyperparameter tuning?
6. When might batch inference be more appropriate than real-time inference?
7. What is data drift?
8. What is concept drift?
9. Why is model monitoring necessary?
10. How does SageMaker AI differ from Amazon Bedrock?

### Answers

1. An AWS service for building, training, tuning, deploying, and managing ML models.
2. It supports model comparison and hyperparameter selection.
3. The use of information in training or evaluation that would not legitimately be available at prediction time.
4. Training learns model parameters; inference uses a trained model to generate outputs.
5. Comparing candidate hyperparameter configurations against an evaluation objective.
6. When processing many records without requiring an immediate response for each record.
7. A change in the distribution of input data.
8. A change in the relationship between features and the target.
9. To detect operational issues, changing data, and degraded performance.
10. SageMaker AI supports broader custom ML workflows; Bedrock provides managed access to supported foundation models and generative AI features.

## 16. Revision Checklist

* [ ] Explain the SageMaker AI lifecycle.
* [ ] Understand data preparation, feature engineering, and leakage.
* [ ] Distinguish training, validation, and test datasets.
* [ ] Understand model training and hyperparameter tuning.
* [ ] Match metrics to classification and regression tasks.
* [ ] Distinguish real-time, batch, asynchronous, and serverless inference.
* [ ] Explain data drift and concept drift.
* [ ] Recognize MLOps practices.
* [ ] Identify supporting AWS services.
* [ ] Distinguish SageMaker AI from Bedrock.

## 17. Official Resources

* Amazon SageMaker AI: https://aws.amazon.com/sagemaker/
* SageMaker AI Documentation: https://docs.aws.amazon.com/sagemaker/
* AWS Machine Learning: https://aws.amazon.com/machine-learning/
* Amazon S3: https://aws.amazon.com/s3/
* Amazon CloudWatch: https://aws.amazon.com/cloudwatch/

---

**Exam focus:** Understand the ML lifecycle, identify model development and deployment requirements, and select the appropriate SageMaker AI workflow or supporting AWS capability.
