# Module 01 — Business Analytics Fundamentals

## Overview

Business analytics is the systematic use of data, quantitative methods, business knowledge, and critical thinking to improve decisions.

This module introduces the concepts and workflows that underpin the wider Business Analytics curriculum. It focuses on understanding business problems, defining metrics, evaluating evidence, identifying data-quality issues, and communicating actionable recommendations.

The goal is not simply to produce charts or calculate numbers. It is to determine what the evidence means, what decisions it supports, and what limitations should influence those decisions.

## Prerequisites

* No previous analytics experience is required.
* Basic familiarity with spreadsheets is helpful.
* Basic arithmetic, percentages, and averages are sufficient.
* Python is optional for the introductory theory but recommended for the practical examples.

## Learning objectives

By the end of this module, learners should be able to:

1. Define business analytics and distinguish it from reporting, business intelligence, and data science.
2. Translate a business problem into measurable analytical questions.
3. Explain descriptive, diagnostic, predictive, and prescriptive analytics.
4. Identify units of analysis, variables, measures, dimensions, metrics, and KPIs.
5. Calculate and interpret basic business performance metrics.
6. Describe the analytics lifecycle from problem framing to monitoring.
7. Recognize data-quality problems, bias, and limitations in business evidence.
8. Distinguish correlation from causation.
9. Explain why statistical significance and business significance are different.
10. Communicate recommendations with supporting evidence, assumptions, and limitations.

## Topic outline

### 1. Introduction to Business Analytics

* Data, information, evidence, insight, and decisions
* Business analytics versus reporting and business intelligence
* Business analytics versus data science
* The importance of business context

### 2. Types of Analytics

* Descriptive analytics: What happened?
* Diagnostic analytics: Why might it have happened?
* Predictive analytics: What may happen?
* Prescriptive analytics: What should we do?

### 3. Business Problem Framing

* Stakeholders and business decisions
* Problem statements and analytical questions
* Objectives, constraints, and success criteria
* Hypotheses and alternative explanations

### 4. Data Fundamentals

* Rows, columns, observations, and variables
* Units of analysis and identifiers
* Categorical and numerical variables
* Data sources and data-quality considerations

### 5. Metrics and KPIs

* Measures, metrics, dimensions, and KPIs
* Revenue, profit, margin, conversion, and service rates
* Denominators and metric definitions
* Targets, thresholds, and guardrail metrics

### 6. The Analytics Lifecycle

* Problem framing
* Data acquisition
* Data validation and preparation
* Exploration and analysis
* Validation and interpretation
* Communication, action, and monitoring

### 7. Data Quality and Responsible Analytics

* Missing values, duplicates, and invalid records
* Selection bias and survivorship bias
* Confounding and correlation versus causation
* Privacy, fairness, and responsible data use
* Reproducibility and documentation

### 8. Communicating Business Insights

* Findings versus interpretations
* Recommendations and expected impact
* Assumptions and limitations
* Executive summaries and decision memos

## Tools and libraries

**Required**

* Text editor
* Excel, LibreOffice Calc, or Google Sheets

**Recommended**

* Python 3.10+
* Jupyter Notebook
* pandas
* matplotlib

Install the optional Python dependencies:

```bash
python -m pip install pandas matplotlib jupyter
```

The example notebooks use synthetic data and do not require external downloads.

## Practical business applications

* **Retail:** sales, average order value, margins, and returns.
* **Marketing:** conversion rates, customer acquisition, and campaign performance.
* **Customer service:** response time, resolution rate, and customer satisfaction.
* **Operations:** delivery delays, capacity, and process efficiency.
* **Finance:** profitability, budget variance, and financial performance.
* **Supply chain:** on-time delivery, stockouts, and inventory management.

## Learning sequence

1. Read `01_Theory.md`.
2. Work through `02_Examples.ipynb`.
3. Complete `03_Exercises.ipynb` without viewing the solutions.
4. Analyze the scenario in `04_Case_Study.ipynb`.
5. Review your work against `05_Solutions.ipynb`.
6. Explore the references in `resources.md`.

## Expected deliverables

* A business problem-framing brief.
* A metric dictionary containing formulas, units, denominators, and limitations.
* Completed beginner, intermediate, and advanced exercises.
* A reproducible analysis notebook.
* A case-study decision memo with evidence, recommendations, risks, and a monitoring plan.

## Suggested assessment

| Assessment area                            | Weight |
| ------------------------------------------ | -----: |
| Problem framing                            |    20% |
| Metric definitions and data quality        |    20% |
| Analytical correctness and reproducibility |    20% |
| Interpretation and limitations             |    20% |
| Communication and recommendations          |    20% |

## Further learning

See `resources.md` for recommended textbooks, official documentation, online learning platforms, and references on responsible analytics.
