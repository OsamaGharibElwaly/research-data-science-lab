# Product Analytics Tutorial

A practical introduction to **Product Analytics** covering the three core areas:

1. **Product Success Metrics / KPIs**
2. **Product Analytics & Dashboards**
3. **Tracking Plans**

The central idea is that analytics is **not a separate step** in product development. It supports the entire product cycle: defining success, tracking user behavior, analyzing performance, and iterating on the product.

---

## 1. What Is Product Analytics?

Product analytics helps teams understand how users interact with a product and use that information to improve the product.

It connects:

```text
Product Design
      ↓
Define Success
      ↓
Define Metrics / KPIs
      ↓
Track User Actions
      ↓
Analyze Behavior
      ↓
Identify Problems
      ↓
Improve Product
      ↓
Repeat
```

Without analytics, product decisions can become guesswork rather than a measurable and repeatable improvement process.

---

# 2. The Three Core Areas

The tutorial focuses on:

| Area         | Main Question                                       |
| ------------ | --------------------------------------------------- |
| **Metrics**  | How do we define whether the product is successful? |
| **Analysis** | How do we monitor and understand those metrics?     |
| **Tracking** | What data must we collect to answer our questions?  |

The tutorial teaches these in the order:

```text
Metrics → Analysis → Tracking
```

Although tracking normally happens before analysis in an actual product implementation, learning analysis first makes tracking easier to understand.

---

# 3. Product Success Metrics

## 3.1 The Product Metrics Pyramid

Product metrics can be organized as a pyramid.

```text
                    Focus Metric
                         ▲
          ┌──────────────┴──────────────┐
          │ Activation │ Engagement     │
          │ Retention  │ Onboarding     │
          └──────────────┬──────────────┘
                         │
                    User Journey
```

The tutorial identifies six important metrics:

1. **Exposure**
2. **Onboarding** — optional
3. **Activation**
4. **Engagement**
5. **Retention**
6. **Focus**

The method can be applied to an entire product or to an individual feature by creating a smaller metric pyramid around that feature.

---

# 4. Map the User Journey First

Before defining metrics, identify the important points in the user's journey.

### Three fundamental points

```text
Exposure
   ↓
Onboarding
   ↓
Activation
```

### Exposure

The first point inside the product that the product team controls.

Examples:

* Web application → Homepage
* Mobile application → Welcome screen

An advertisement or app-store impression is not considered exposure in this framework because it occurs outside the product itself.

### Onboarding

The completion of the steps required to gain access to the product's main functionality.

Onboarding is optional because some products allow users to access the core product without creating an account or completing onboarding.

### Activation

The point where the user performs the **key action that delivers value**.

Examples:

| Product            | Activation          |
| ------------------ | ------------------- |
| Messenger          | Send a message      |
| Video platform     | Watch a video       |
| Animation platform | Create an animation |

The key principle is to select the **most important value-generating action**.

---

# 5. The Core Product Metrics

## 5.1 Exposure

The number of users who reach the exposure point.

```text
Exposure = Number of users reaching exposure
```

Exposure is generally a reference point at the top of the funnel rather than a metric used to diagnose product performance.

---

## 5.2 Onboarding Success Rate

Measures the percentage of users who successfully complete onboarding.

One possible definition:

```text
Onboarding Success Rate
=
Users Completing Onboarding
/
Users Exposed
```

If there is a significant gap between exposure and starting onboarding, it can instead be defined as:

```text
Users Completing Onboarding
/
Users Starting Onboarding
```

This metric is optional depending on the product.

---

## 5.3 Activation Rate

Measures the conversion from the previous journey stage to the key action.

With onboarding:

```text
Activation Rate
=
Activated Users
/
Users Completing Onboarding
```

Without onboarding:

```text
Activation Rate
=
Activated Users
/
Exposed Users
```

The important principle is:

> Measure conversion between consecutive important stages of the user journey.

---

## 5.4 Engagement Rate

Activation tells us **whether** users performed the key action.

Engagement tells us **how much** active users use the product.

```text
Engagement
=
Total Key Actions
/
Users Performing Key Action
```

Example:

```text
100 videos watched
/
20 video watchers
=
5 videos per active user
```

Do not divide by all users because dormant users introduce noise into the measurement.

---

## 5.5 Retention Rate

Retention measures whether activated users continue performing the key action after a fixed period.

For example:

```text
30-Day Retention
=
Users Still Active After 30 Days
/
Users Who Initially Activated
```

Common periods include:

* 30 days
* 90 days

The appropriate period depends on the product's usage pattern.

---

## 5.6 Focus Metric

The focus metric is the top-level metric that represents overall product activity.

Possible definitions include:

* DAU — Daily Active Users
* WAU — Weekly Active Users
* MAU — Monthly Active Users

The definition of an **active user** must be tied to meaningful product behavior.

For example:

```text
YouTube-like product
Active User = User who watches a video
Focus Metric = Weekly Active Users
```

The other metrics help explain changes in the focus metric.

---

# 6. Why Rates Are Often Better Than Raw Numbers

A major principle in product analytics is to use **rates** where appropriate.

Suppose:

```text
Exposure ↓
```

Then downstream raw user counts may also decrease:

```text
Onboarding ↓
Activation ↓
Retention ↓
```

This does not necessarily mean those parts of the product became worse.

Using conversion rates helps isolate the performance of each stage:

```text
Onboarding Rate
=
Completed Onboarding
/
Started Onboarding

Activation Rate
=
Activated
/
Previous Stage

Retention Rate
=
Retained Users
/
Activated Users
```

**Exposure is the major exception**, because it is at the top of the funnel and therefore can reasonably be represented as a raw volume.

---

# 7. Example: SaaS Animation Product

Imagine a fictional animation application.

### User journey

```text
Homepage
   ↓
Account Creation
   ↓
Create Animation
   ↓
Export Animation
```

### Metrics

| Stage                         | Metric             |
| ----------------------------- | ------------------ |
| Homepage                      | Exposure           |
| Account creation              | Onboarding Success |
| Create animation              | Activation         |
| Animations per user           | Engagement         |
| Users returning after 90 days | Retention          |
| Weekly active users           | Focus              |

The focus metric is **WAU** because a professional animation application is expected to have a weekly usage pattern.

---

# 8. Metrics Can Be Applied to Features

The framework does not have to describe the entire product.

Suppose the animation application introduces an AI image-generation feature:

```text
Feature Exposure
      ↓
Generate/Add AI Image
      ↓
Repeated AI Image Usage
      ↓
Long-Term Feature Usage
```

Possible metrics:

* Exposure → users who see the feature
* Activation → users who use the feature
* Engagement → images added per user
* Retention → users who continue using the feature
* Focus → weekly users performing the feature's key action

This allows the same framework to evaluate both **products and individual features**.

---

# 9. Example: YouTube-Like Product

For a video platform:

```text
Homepage
   ↓
Watch Video
```

There is no required onboarding in this example.

### Metrics

```text
Exposure
= Users reaching homepage

Activation Rate
= Users watching a video
  /
  Exposed users

Engagement
= Videos watched
  /
  Video watchers

Retention
= Users still watching after 30 days
  /
  Initially activated users

Focus Metric
= Daily Active Users
```

The daily focus metric is appropriate because the platform can be used across all days of the week.

---

# 10. Example: E-Commerce

E-commerce requires some modification because purchasing can depend on factors outside the product experience, such as:

* Inventory
* Price
* Product availability

A useful activation point can therefore be **viewing a specific product** rather than immediately making a purchase.

```text
Homepage
   ↓
Product Viewed
   ↓
Purchase
   ↓
Repeat Purchase
```

Possible metrics:

* Exposure → homepage users
* Activation → users viewing an item
* Purchase conversion → product viewers who purchase
* Engagement → purchases per purchaser
* Retention → buyers who return and purchase again
* Focus → daily active users

---

# 11. Product Analytics Data: Events

Product analytics tools primarily work with **events**.

An event represents:

```text
Who + Did What + When
```

Conceptually:

```text
Event
├── User ID
├── Timestamp
└── Action
```

Examples:

* `Sign Up`
* `Watch Video`
* `Order Placed`
* `Video Published`

Events are captured by implementing tracking code in the product.

---

# 12. Event Properties

Properties provide **context about an event**.

Example:

```text
Event: Video Viewed

Properties:
├── Video Name
├── Video Duration
├── Video Category
└── Channel Name
```

Another example:

```text
Event: Order Placed

Properties:
├── Order Cost
├── Item
└── Category
```

Think of it as:

```text
Event = What happened?
Property = Context about what happened?
```

Properties allow analysts to filter and break down events.

---

# 13. Product Analytics Tools

The tutorial demonstrates the workflow using **Mixpanel**.

Other tools mentioned include:

* Mixpanel
* Amplitude
* PostHog
* Adobe Analytics
* Pendo
* Heap

The underlying concepts are similar across product analytics platforms.

---

# 14. Building a Product Analytics Dashboard

A dashboard is essentially a collection of reports.

```text
Dashboard
│
├── Focus Metric
├── Activation
├── Engagement
├── Retention
└── Other Analysis
```

The tutorial uses Mixpanel's **Insights** report and **Funnels** report.

---

# 15. Insights Reports

Insights is useful for analyzing individual events and trends.

Example:

```text
Event: Watch Video
Aggregation: Unique Users
Time: Weekly
```

This produces:

```text
Weekly Active Users
```

when an active user is defined as someone who watches a video.

---

# 16. Funnel Analysis

Funnels measure conversion between multiple steps.

Example:

```text
Sign Up
   ↓
Watch Video
```

Formula:

```text
Activation Rate
=
Users who Watch Video
/
Users who Sign Up
```

A funnel also has a **funnel window**.

For example:

```text
Funnel Window = 7 days
```

A user must complete the subsequent funnel steps within that period to be counted as converted.

Funnels can also show conversion rates over time rather than only the current funnel snapshot.

---

# 17. Measuring Engagement in Mixpanel

To measure:

```text
Videos watched per video watcher
```

use:

```text
Watch Video
→ Frequency per User
→ Average
```

This normalizes the metric by the users who actually performed the action rather than including dormant users.

---

# 18. Retention Analysis

Retention analysis uses two events.

Example:

```text
Cohort Event:
Sign Up

Return Event:
Watch Video
```

The analysis asks:

> Of users who performed the first action, how many returned and performed the second action later?

Retention can be analyzed by cohorts to compare groups of users who started at different times.

---

# 19. Filtering and Breaking Down Data

Event properties allow you to answer more detailed questions.

Suppose we want to know:

> Which video category gets the most views?

Use:

```text
Event: Watch Video
Aggregation: Total Event Count
Breakdown: Category
```

This allows comparisons between categories.

You can also filter the data:

```text
Platform = Mobile
```

or:

```text
Country = Argentina
```

The same event/property concepts can be applied across insights, funnels, retention, and other reports.

---

# 20. Dashboard Structure

A useful dashboard can contain:

```text
┌─────────────────────────────────────┐
│ Product KPI Dashboard               │
├─────────────────────────────────────┤
│ Focus Metric — WAU                  │
├─────────────────────────────────────┤
│ Activation Rate                     │
├─────────────────────────────────────┤
│ Engagement Rate                     │
├─────────────────────────────────────┤
│ Retention                           │
├─────────────────────────────────────┤
│ Supporting Analysis                 │
└─────────────────────────────────────┘
```

Dashboards can also include:

* Text blocks
* Images
* Layout adjustments
* Global filters
* Date ranges
* Country filters
* Platform filters

A dashboard-level filter can affect the reports throughout the dashboard.

---

# 21. Tracking Plans

A **tracking plan** is the blueprint given to the engineering team describing what product behavior should be tracked.

It connects:

```text
Business Questions
       ↓
Metrics / KPIs
       ↓
Events + Properties
       ↓
Engineering Implementation
       ↓
Product Analytics Tool
       ↓
Reports / Dashboards
```

The tracking plan should contain the events and properties necessary to calculate the metrics and answer important product questions.

---

# 22. Tracking Plan Structure

A typical tracking plan can contain:

| Column                     | Purpose                           |
| -------------------------- | --------------------------------- |
| Event Name                 | Name of the tracked action        |
| Trigger / Event Definition | What causes the event             |
| Property Name              | Context associated with the event |
| Property Description       | Meaning of the property           |
| Data Type                  | String, number, boolean, etc.     |
| Sample Values              | Examples showing expected values  |

---

# 23. Event Naming

Use a consistent naming convention.

The tutorial recommends an **object-action** structure.

Examples:

```text
Video Viewed
Video Published
Channel Subscribed
```

Conceptually:

```text
Object + Action
```

Consistency is critical because analytics platforms can be case-sensitive.

For example, avoid creating:

```text
Video Viewed
video viewed
VIDEO VIEWED
```

as separate naming variations. Choose one convention and use it consistently.

---

# 24. Event Triggers Must Represent Completed Actions

An event should represent the **successful completion of an action**, not merely the user's attempt.

Bad:

```text
User clicks "Publish"
→ Video Published
```

Better:

```text
User clicks "Publish"
       ↓
Publishing succeeds
       ↓
Video Published
```

Otherwise, a failed publishing attempt could incorrectly appear as a successful publication.

---

# 25. Choosing Property Names

Be specific.

Instead of:

```text
name
```

prefer:

```text
video_name
channel_name
```

This prevents ambiguity when multiple entities have names.

### Data types

| Type    | Example               |
| ------- | --------------------- |
| String  | `"Analytics Academy"` |
| Number  | `4.5`                 |
| Boolean | `true` / `false`      |

Sample values help engineers understand exactly what should be tracked.

---

# 26. The Most Important Tracking Principle

## Start With Questions, Not Events

Do **not** start with:

> "Let's track everything."

Instead:

```text
What questions do we need to answer?
              ↓
What KPIs do we need?
              ↓
What events are required?
              ↓
What properties are required?
```

Tracking everything can create:

* Noisy data
* Messy analytics
* Unnecessary engineering work
* Difficult QA
* Data that still cannot answer the questions you care about

The tracking plan should therefore be **question-driven**.

---

# 27. Tracking Plan Example

For a video-sharing platform:

### Core KPIs

```text
Weekly Active Users
Activation Rate
Engagement
14-Day Retention
```

### Questions

```text
Which video gets the most views?
Which channel gets the most views?
How many minutes of video are published every day?
What portion of viewers become content creators?
```

From these requirements, derive the required events.

---

# 28. Example Events

### 1. Homepage Viewed

```text
Event:
Homepage Viewed

Trigger:
User arrives at homepage
```

No additional property is necessarily required for the core metric.

### 2. Sign Up Completed

```text
Event:
Sign Up Completed

Trigger:
User successfully completes signup
```

### 3. Video Viewed

```text
Event:
Video Viewed

Trigger:
User watches/views a video
```

Possible properties:

```text
video_name
channel_name
```

### 4. Video Published

```text
Event:
Video Published

Trigger:
Video is successfully published
```

Possible properties:

```text
video_name
channel_name
video_duration
```

The tutorial demonstrates that a small number of well-designed events can support many KPIs and product questions.

---

# 29. Event Reuse

You do not necessarily need a new event for every metric.

For example:

```text
Video Viewed
```

can support:

* Weekly Active Users
* Activation
* Engagement
* Retention
* Video popularity
* Category analysis

Similarly:

```text
Sign Up Completed
```

can support:

* Activation funnels
* Retention cohorts
* Viewer → creator conversion

Good event design therefore maximizes the analytical value of each event.

---

# 30. How Metrics and Tracking Work Together

Example:

### Question

> Which video gets the most views?

### Required event

```text
Video Viewed
```

### Required property

```text
video_name
```

### Analysis

```text
Video Viewed
→ Total Event Count
→ Breakdown by video_name
```

Without `video_name`, you know how many videos were viewed but not **which videos** were responsible for those views.

---

# 31. Another Example: Video Duration

Question:

> How many minutes of video are published every day?

Required event:

```text
Video Published
```

Required property:

```text
video_duration
```

Possible type:

```text
Number
```

For example:

```text
video_duration = 270 seconds
```

Tracking duration in a consistent unit and converting later can make the data easier to work with.

---

# 32. How Many Events Should You Track?

There is no universal number.

However, the tutorial gives an important practical guideline:

> A new or relatively simple product will often need fewer than 20 well-designed events.

If you find yourself designing around 100 unique events, it may indicate that you are tracking too much.

The goal is not:

```text
Maximum Data
```

The goal is:

```text
Useful Data
```

Every additional event also creates engineering and QA work.

---

# 33. The Complete Product Analytics Workflow

The real-world order should be:

```text
1. Define Product KPIs
          ↓
2. Define Business / Product Questions
          ↓
3. Create Tracking Plan
          ↓
4. Engineering Implements Tracking
          ↓
5. QA the Events
          ↓
6. Data Flows into Analytics Tool
          ↓
7. Build Reports
          ↓
8. Build Dashboard
          ↓
9. Analyze Results
          ↓
10. Improve Product
          ↓
11. Define New Questions / Metrics
          ↓
12. Update Tracking Plan
          ↓
        Repeat
```

The tutorial emphasizes that this is a continuous process rather than a one-time implementation.

---

# 34. Product Analytics + A/B Testing

A/B or split testing was not covered in depth in the tutorial.

The basic idea is:

```text
Version A
   vs.
Version B
   ↓
Compare Product Metrics
   ↓
Determine Which Performs Better
```

The product analytics framework can provide the metrics needed to evaluate the experiment, while A/B testing introduces additional statistical considerations.

---

# 35. Key Mental Model

The most important mental model from the tutorial is:

```text
                FOCUS
                  ▲
                  │
        ┌─────────┼─────────┐
        │         │         │
   ACTIVATION ENGAGEMENT RETENTION
        ▲         ▲         ▲
        │         │         │
        └──── USER JOURNEY ─┘
                  ▲
                  │
             ONBOARDING
                  ▲
                  │
              EXPOSURE
```

Then:

```text
Metrics
   ↓
Questions
   ↓
Events
   ↓
Properties
   ↓
Tracking Plan
   ↓
Data
   ↓
Analysis
   ↓
Product Decisions
```

---

# 36. Practical Checklist

## Product Metrics

* [ ] Identify the user journey
* [ ] Define exposure
* [ ] Determine whether onboarding is required
* [ ] Identify the key activation action
* [ ] Define engagement
* [ ] Define retention period
* [ ] Select DAU, WAU, or MAU as appropriate
* [ ] Establish the focus metric
* [ ] Ensure lower-level metrics help explain the focus metric

## Tracking Plan

* [ ] Start from questions
* [ ] Identify required KPIs
* [ ] Define required events
* [ ] Define required properties
* [ ] Use consistent event naming
* [ ] Define successful event triggers
* [ ] Specify data types
* [ ] Provide sample values
* [ ] Avoid unnecessary events

## Dashboard

* [ ] Create focus metric report
* [ ] Create activation funnel
* [ ] Create engagement report
* [ ] Create retention report
* [ ] Add relevant breakdowns
* [ ] Add filters
* [ ] Add explanatory text
* [ ] Organize the dashboard clearly

---

# 37. Core Takeaways

### 1. Analytics is part of the entire product lifecycle

It should influence product design, development, launch, analysis, and iteration.

### 2. Start with the user journey

Identify:

```text
Exposure → Onboarding → Activation → Engagement → Retention
```

and connect these to the focus metric.

### 3. Rates help isolate performance

Conversion rates can reveal whether a specific stage is improving or deteriorating instead of simply reflecting changes in upstream traffic.

### 4. Events represent actions

```text
Event = User + Action + Timestamp
```

### 5. Properties provide context

```text
Event = What happened?
Property = Details about what happened?
```

### 6. Start tracking from questions

Do not collect data simply because it is technically possible.

### 7. Good tracking plans are highly valuable

A poorly designed tracking plan can prevent teams from answering the questions they actually care about.

### 8. Product analytics is iterative

The process continuously evolves:

```text
Measure
  ↓
Understand
  ↓
Improve
  ↓
Measure Again
```

---

# 38. Mini Practice Exercise

Choose any product and complete the following.

### Product

```text
________________________________
```

### User Journey

```text
Exposure:
________________________________

Onboarding:
________________________________

Activation:
________________________________

Engagement:
________________________________

Retention:
________________________________
```

### Focus Metric

```text
DAU / WAU / MAU:

________________________________
```

### Metrics

```text
Exposure:
________________________________

Onboarding Rate:
________________________________

Activation Rate:
________________________________

Engagement:
________________________________

Retention:
________________________________
```

### Product Questions

```text
1. __________________________________
2. __________________________________
3. __________________________________
4. __________________________________
```

### Tracking Events

| Event | Trigger | Properties |
| ----- | ------- | ---------- |
|       |         |            |
|       |         |            |
|       |         |            |
|       |         |            |

---

# 39. Final Framework

When approaching a new product analytics problem, remember:

```text
┌───────────────────────────────┐
│       1. PRODUCT              │
│       What are we building?   │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│       2. USER JOURNEY         │
│       How do users get value? │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│       3. KPIs                 │
│       How do we measure it?   │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│       4. QUESTIONS            │
│       What do we need to know?│
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│       5. TRACKING PLAN        │
│       What must we collect?   │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│       6. ANALYSIS             │
│       What is happening?      │
└───────────────┬───────────────┘
                ↓
┌───────────────────────────────┐
│       7. DECISIONS            │
│       What should we change?  │
└───────────────┬───────────────┘
                ↓
             ITERATE
```

**The goal of Product Analytics is not simply to collect data. It is to create a repeatable system for understanding user behavior and using that understanding to improve the product.**
---

Now Complete Guide Using GPT:

# Product Analytics — Complete Guide

> A practical and comprehensive guide to Product Analytics: from understanding users and products to measuring behavior, retention, experimentation, and business impact.

---

## Table of Contents

1. [What Is Product Analytics?](#1-what-is-product-analytics)
2. [Product Analytics vs Other Analytics](#2-product-analytics-vs-other-analytics)
3. [The Product Analytics Mindset](#3-the-product-analytics-mindset)
4. [The Product Analytics Framework](#4-the-product-analytics-framework)
5. [Users, Events, and Entities](#5-users-events-and-entities)
6. [Event Tracking](#6-event-tracking)
7. [North Star Metric](#7-north-star-metric)
8. [Metrics Hierarchy](#8-metrics-hierarchy)
9. [Acquisition Analytics](#9-acquisition-analytics)
10. [Activation Analytics](#10-activation-analytics)
11. [Engagement Analytics](#11-engagement-analytics)
12. [Conversion Analytics](#12-conversion-analytics)
13. [Retention Analytics](#13-retention-analytics)
14. [Churn Analytics](#14-churn-analytics)
15. [Funnel Analysis](#15-funnel-analysis)
16. [Cohort Analysis](#16-cohort-analysis)
17. [Segmentation](#17-segmentation)
18. [User Journey Analysis](#18-user-journey-analysis)
19. [Path Analysis](#19-path-analysis)
20. [Feature Analytics](#20-feature-analytics)
21. [Adoption Analysis](#21-adoption-analysis)
22. [Stickiness](#22-stickiness)
23. [DAU, WAU, MAU](#23-dau-wau-mau)
24. [Product-Market Fit Analytics](#24-product-market-fit-analytics)
25. [A/B Testing](#25-ab-testing)
26. [Experiment Design](#26-experiment-design)
27. [Statistical Significance](#27-statistical-significance)
28. [Guardrail Metrics](#28-guardrail-metrics)
29. [Segmentation in Experiments](#29-segmentation-in-experiments)
30. [Causal Thinking](#30-causal-thinking)
31. [Revenue Analytics](#31-revenue-analytics)
32. [Pricing Analytics](#32-pricing-analytics)
33. [Subscription Analytics](#33-subscription-analytics)
34. [E-commerce Product Analytics](#34-e-commerce-product-analytics)
35. [Marketplace Analytics](#35-marketplace-analytics)
36. [SaaS Analytics](#36-saas-analytics)
37. [Mobile App Analytics](#37-mobile-app-analytics)
38. [B2B Product Analytics](#38-b2b-product-analytics)
39. [Customer Analytics](#39-customer-analytics)
40. [Customer Lifetime Value](#40-customer-lifetime-value)
41. [Customer Acquisition Cost](#41-customer-acquisition-cost)
42. [LTV:CAC](#42-ltvcac)
43. [Product Analytics Data Model](#43-product-analytics-data-model)
44. [SQL for Product Analytics](#44-sql-for-product-analytics)
45. [Python for Product Analytics](#45-python-for-product-analytics)
46. [Visualization](#46-visualization)
47. [Dashboards](#47-dashboards)
48. [Analytics Workflow](#48-analytics-workflow)
49. [Common Mistakes](#49-common-mistakes)
50. [Product Analytics Case Study](#50-product-analytics-case-study)
51. [Exercises](#51-exercises)
52. [Advanced Exercises](#52-advanced-exercises)
53. [Portfolio Projects](#53-portfolio-projects)
54. [Product Analytics Checklist](#54-product-analytics-checklist)
55. [Final Mental Model](#55-final-mental-model)

---

# 1. What Is Product Analytics?

Product Analytics is the systematic analysis of how users interact with a product.

The objective is not simply:

> "What happened?"

Instead, Product Analytics asks:

> "What are users doing, why are they doing it, where are they struggling, and what should the product team do next?"

A Product Analyst connects:

```text
User Behavior
      ↓
Product Experience
      ↓
Metrics
      ↓
Analysis
      ↓
Insights
      ↓
Product Decisions
      ↓
Business Outcomes
```

Typical questions:

* Where do users drop out?
* Which features create the most value?
* Which users retain?
* Why do users churn?
* Which onboarding flow performs better?
* Which feature should we build next?
* Does a new feature improve activation?
* Does a price increase reduce conversion?
* Which customer segment generates the most value?
* What behavior predicts retention?

---

# 2. Product Analytics vs Other Analytics

| Type                   | Main Question                                                         |
| ---------------------- | --------------------------------------------------------------------- |
| Descriptive Analytics  | What happened?                                                        |
| Diagnostic Analytics   | Why did it happen?                                                    |
| Predictive Analytics   | What will probably happen?                                            |
| Prescriptive Analytics | What should we do?                                                    |
| Product Analytics      | How are users interacting with the product and how can we improve it? |
| Marketing Analytics    | Which acquisition activities work?                                    |
| Financial Analytics    | What is happening financially?                                        |
| Operations Analytics   | How efficiently does the organization operate?                        |

Product Analytics sits at the intersection of:

```text
Statistics
   +
Data Analytics
   +
Behavioral Science
   +
Product Management
   +
Business
   +
Experimentation
```

---

# 3. The Product Analytics Mindset

A strong Product Analyst does not begin with a dashboard.

They begin with a **decision**.

Bad approach:

```text
Let's calculate DAU.
```

Better:

```text
We believe users are not returning frequently enough.

What evidence would confirm or reject this hypothesis?
```

Even better:

```text
If weekly retention is low because users fail to experience
the core product value during onboarding, improving activation
should increase retention.
```

This creates:

```text
Problem
→ Hypothesis
→ Measurement
→ Analysis
→ Experiment
→ Decision
```

---

# 4. The Product Analytics Framework

A useful framework:

```text
ACQUISITION
    ↓
ACTIVATION
    ↓
ENGAGEMENT
    ↓
RETENTION
    ↓
MONETIZATION
    ↓
REFERRAL
```

This is closely related to the AARRR framework:

```text
Acquisition
Activation
Retention
Revenue
Referral
```

But Product Analytics should not blindly optimize each stage independently.

Example:

```text
Increasing acquisition
      ↓
more users
      ↓
but lower-quality users
      ↓
lower activation
      ↓
lower retention
```

Therefore:

> Metrics must be interpreted as a system.

---

# 5. Users, Events, and Entities

Product Analytics is fundamentally event-based.

A user performs an action.

Example:

```text
User 1042
    ↓
opened_app
    ↓
searched_product
    ↓
viewed_product
    ↓
added_to_cart
    ↓
started_checkout
    ↓
purchased
```

## Core entities

Typical entities:

* User
* Account
* Session
* Device
* Product
* Order
* Subscription
* Organization
* Feature
* Experiment

---

# 6. Event Tracking

An event represents an action.

Examples:

```text
app_opened
account_created
onboarding_completed
product_viewed
search_performed
cart_created
item_added
checkout_started
purchase_completed
subscription_started
feature_used
```

A good event contains properties.

Example:

```json
{
  "event": "product_viewed",
  "user_id": 123,
  "product_id": 501,
  "timestamp": "2026-09-14T15:30:00",
  "device": "mobile",
  "country": "Egypt",
  "price": 250,
  "category": "electronics"
}
```

### Event design principles

Events should be:

* understandable
* consistent
* stable
* measurable
* documented
* tied to user behavior

Avoid vague events:

```text
button_clicked
thing_happened
page_action
```

Prefer:

```text
checkout_started
product_added_to_cart
payment_completed
```

---

# 7. North Star Metric

The North Star Metric attempts to represent the core value users receive from the product.

Examples:

| Product    | Possible North Star          |
| ---------- | ---------------------------- |
| Spotify    | Time spent listening         |
| Airbnb     | Nights booked                |
| Uber       | Completed trips              |
| YouTube    | Meaningful viewing           |
| Slack      | Teams actively collaborating |
| E-commerce | Successful purchases         |

A good North Star should connect:

```text
User Value
     +
Business Value
```

It should not simply be:

```text
Revenue
```

Revenue is important, but it may be a lagging outcome rather than a measure of product value.

---

# 8. Metrics Hierarchy

A useful hierarchy:

```text
North Star Metric
       ↓
Input Metrics
       ↓
Behavioral Metrics
       ↓
Diagnostic Metrics
```

Example:

### North Star

```text
Successful orders
```

### Input metrics

```text
Product views
Add-to-cart rate
Checkout initiation
Payment completion
```

### Diagnostic metrics

```text
Page load time
Payment errors
Stock availability
Search failure rate
```

This prevents teams from focusing exclusively on the final business outcome.

---

# 9. Acquisition Analytics

Acquisition measures how users arrive.

Sources may include:

* Organic search
* Paid search
* Social media
* Referral
* Email
* Direct
* Partnerships

Important metrics:

```text
Visitors
Signups
Cost per acquisition
Conversion rate
Channel conversion
CAC
```

But acquisition should not stop at signup.

A channel producing:

```text
10,000 registrations
```

may be worse than one producing:

```text
2,000 registrations
```

if those 2,000 users retain and purchase at much higher rates.

Therefore:

```text
Acquisition
→ Activation
→ Retention
→ Revenue
```

should be analyzed together.

---

# 10. Activation Analytics

Activation occurs when a user experiences the product's core value.

Examples:

### Project management

```text
Create account
→ Create project
→ Add teammate
→ Create task
```

Activation might be:

```text
Created first project + first task
```

### E-commerce

```text
Signup
→ Search
→ Product view
→ Add to cart
```

Activation might be:

```text
First meaningful shopping interaction
```

Activation is often more useful than signup count.

---

# 11. Engagement Analytics

Engagement measures how users interact with the product.

Examples:

* Sessions
* Sessions per user
* Actions per session
* Feature usage
* Time spent
* Content consumed
* Transactions
* Messages sent

However:

> More activity does not always mean more value.

A user spending 3 hours fixing a broken interface is not necessarily more engaged than a user completing their task in 10 minutes.

Always distinguish:

```text
Activity
vs
Value
```

---

# 12. Conversion Analytics

Conversion measures movement between stages.

General formula:

```text
Conversion Rate =
Conversions / Eligible Users
```

Example:

```text
10,000 visitors
1,000 signups

Signup conversion =
1,000 / 10,000
= 10%
```

Conversion can be calculated between:

```text
Landing page → Signup
Signup → Activation
Activation → Purchase
Trial → Subscription
```

---

# 13. Retention Analytics

Retention asks:

> Do users come back and continue receiving value?

Basic retention:

```text
Retention Rate =
Returning Users / Original Cohort
```

Example:

```text
Day 0 cohort = 1,000 users
Day 7 returning = 350

D7 retention = 35%
```

Retention is often more meaningful than raw acquisition.

A product with:

```text
1,000,000 users
```

and terrible retention may be weaker than:

```text
50,000 users
```

with strong retention.

---

# 14. Churn Analytics

Churn is the opposite side of retention.

For customers:

```text
Customer Churn =
Customers Lost / Customers at Start
```

For subscriptions:

```text
Subscription Churn =
Cancelled Subscriptions / Starting Subscriptions
```

But churn should be investigated.

Possible causes:

```text
Price
Poor onboarding
Missing feature
Technical problems
Competitor
Low perceived value
Bad customer support
Seasonality
```

Do not treat churn as a single metric.

Analyze:

```text
Who churned?
When?
After which behavior?
Which plan?
Which acquisition channel?
Which feature?
```

---

# 15. Funnel Analysis

A funnel represents sequential stages.

Example:

```text
10,000 visitors
      ↓
3,000 signups
      ↓
1,500 activated
      ↓
800 added to cart
      ↓
500 purchased
```

Calculate conversion at each stage.

```text
Visitor → Signup = 30%

Signup → Activation = 50%

Activation → Cart = 53.3%

Cart → Purchase = 62.5%
```

Overall conversion:

```text
500 / 10,000 = 5%
```

### Funnel questions

* Where is the largest drop?
* Is the drop expected?
* Does the drop differ by device?
* Does it differ by country?
* Did it change after a release?
* Is there a technical problem?
* Does one segment behave differently?

---

# 16. Cohort Analysis

A cohort is a group sharing a common characteristic.

Common cohort definitions:

```text
Signup month
First purchase month
Acquisition channel
First product
Subscription start date
Experiment assignment
```

Example:

| Cohort | Week 0 | Week 1 | Week 2 | Week 3 |
| ------ | -----: | -----: | -----: | -----: |
| Jan    |   100% |    42% |    31% |    25% |
| Feb    |   100% |    48% |    36% |    30% |
| Mar    |   100% |    51% |    40% |    34% |

The March cohort is performing better.

Possible explanation:

```text
New onboarding
+
Better acquisition
+
Product improvement
```

Cohort analysis helps distinguish:

```text
Time effects
vs
User effects
```

---

# 17. Segmentation

Segmentation means comparing meaningful user groups.

Possible dimensions:

### Demographic

* Age
* Country
* Region

### Behavioral

* Heavy users
* Light users
* Feature adopters
* Purchasers

### Acquisition

* Organic
* Paid
* Referral

### Product

* Plan
* Device
* Platform

### Business

* SMB
* Enterprise
* Industry

Example:

```text
Overall retention = 30%

Mobile = 24%
Desktop = 38%
```

This suggests investigating mobile experience.

---

# 18. User Journey Analysis

A user journey describes the sequence of experiences.

Example:

```text
Ad
 ↓
Landing page
 ↓
Signup
 ↓
Onboarding
 ↓
Search
 ↓
Product
 ↓
Cart
 ↓
Checkout
 ↓
Purchase
```

The goal is to identify:

```text
friction
confusion
drop-off
loops
dead ends
successful paths
```

---

# 19. Path Analysis

Path analysis asks:

> What actions do users perform before or after a specific event?

Example:

```text
Search
→ Product View
→ Product View
→ Cart
→ Checkout
```

Another user:

```text
Search
→ Filter
→ Product View
→ Cart
```

If successful users frequently use filters:

```text
Hypothesis:
Improving filtering may increase conversion.
```

Important:

> Correlation does not prove causation.

---

# 20. Feature Analytics

When a new feature launches, measure:

### Adoption

```text
Feature users / Eligible users
```

### Frequency

```text
Feature uses / Feature users
```

### Repeat usage

```text
Users returning to feature / Feature users
```

### Impact

Compare:

```text
Feature adopters
vs
non-adopters
```

But be careful.

Feature adopters may already be better users.

This is why experimentation is important.

---

# 21. Adoption Analysis

Feature adoption can be measured through stages:

```text
Eligible
   ↓
Exposed
   ↓
Tried
   ↓
Activated
   ↓
Repeated
   ↓
Retained
```

A feature can have:

```text
High exposure
Low trial
```

Meaning users see it but don't understand it.

Or:

```text
High trial
Low repeat usage
```

Meaning users try it but don't find enough value.

---

# 22. Stickiness

Stickiness measures how frequently users return.

A common formula:

```text
DAU / MAU
```

Example:

```text
DAU = 20,000
MAU = 100,000

Stickiness = 20%
```

Higher stickiness generally indicates more frequent usage.

But the appropriate level depends on the product.

A banking product does not need users to open it 10 times per day.

---

# 23. DAU, WAU, MAU

### DAU

Daily Active Users.

### WAU

Weekly Active Users.

### MAU

Monthly Active Users.

These metrics require a clear definition of:

> What does "active" mean?

For example:

```text
Opening an app
```

may be too weak.

A better definition might be:

```text
Completed a meaningful product action.
```

---

# 24. Product-Market Fit Analytics

Product-market fit is not a single dashboard metric.

Signals include:

```text
Retention
Organic growth
Repeat usage
Referral
Customer satisfaction
Willingness to pay
Low churn
```

A common survey question:

> How would you feel if you could no longer use this product?

Responses can help estimate how strongly users value the product.

But survey evidence should be combined with behavioral evidence.

---

# 25. A/B Testing

A/B testing compares two variants.

```text
Control
   vs
Treatment
```

Example:

```text
A = old checkout

B = redesigned checkout
```

Randomly assign users.

Then compare:

```text
Conversion_A
vs
Conversion_B
```

Example:

```text
A = 10.0%
B = 11.2%
```

Observed lift:

```text
(11.2 - 10.0) / 10.0
= 12%
```

---

# 26. Experiment Design

Before launching an experiment define:

### Hypothesis

```text
Changing checkout layout will increase purchase conversion
because users will have fewer distractions.
```

### Primary metric

```text
Purchase conversion
```

### Secondary metrics

```text
Checkout completion
Revenue per user
```

### Guardrails

```text
Refund rate
Payment errors
Customer complaints
```

### Population

```text
Eligible users
```

### Duration

Long enough to capture normal behavior.

---

# 27. Statistical Significance

Observed differences may happen by chance.

Suppose:

```text
A = 10.0%
B = 10.4%
```

The difference is:

```text
0.4 percentage points
```

That does not automatically mean B is better.

We need uncertainty.

Typical concepts:

* Null hypothesis
* Alternative hypothesis
* p-value
* confidence interval
* statistical power
* minimum detectable effect
* sample size

---

# 28. Guardrail Metrics

Optimizing one metric can damage another.

Example:

```text
New promotion
```

may increase:

```text
Purchases ↑
```

but also:

```text
Refunds ↑
```

Therefore define guardrails.

Typical guardrails:

```text
Revenue
Retention
Latency
Error rate
Refunds
Complaints
Churn
Cancellation
```

A successful experiment should improve the target metric **without unacceptable damage elsewhere**.

---

# 29. Segmentation in Experiments

Overall experiment result:

```text
+5%
```

But segments may show:

```text
Mobile: +10%
Desktop: +1%
New users: +15%
Existing users: -2%
```

This creates questions.

However, avoid randomly searching dozens of segments until finding significance.

That increases false-positive risk.

Predefine important segments where possible.

---

# 30. Causal Thinking

Product Analytics frequently encounters:

```text
Correlation ≠ Causation
```

Suppose:

```text
Users who use Feature X retain more.
```

Possible explanations:

### A

Feature X causes retention.

### B

Highly engaged users naturally use Feature X.

### C

Both are caused by another factor.

### D

Selection bias.

Therefore:

```text
Observation
→ Hypothesis
→ Experiment
→ Causal evidence
```

is stronger than:

```text
Observation
→ Conclusion
```

---

# 31. Revenue Analytics

Important revenue metrics include:

```text
Revenue
ARPU
ARPPU
MRR
ARR
Conversion
Average Order Value
Revenue per user
Revenue retention
```

### ARPU

```text
Revenue / Active Users
```

### ARPPU

```text
Revenue / Paying Users
```

---

# 32. Pricing Analytics

Pricing questions:

* What happens if price increases?
* Which plans convert?
* Which users are price-sensitive?
* Does discounting increase long-term value?
* Which features justify premium pricing?

Analyze:

```text
Price
→ Conversion
→ Retention
→ Revenue
→ Lifetime Value
```

Optimizing conversion alone may produce bad outcomes.

---

# 33. Subscription Analytics

Subscription lifecycle:

```text
Trial
 ↓
Activation
 ↓
Paid
 ↓
Renewal
 ↓
Expansion
 ↓
Cancellation
```

Important metrics:

```text
Trial conversion
MRR
ARR
Churn
Renewal rate
Expansion
Downgrade
Upgrade
Net Revenue Retention
```

---

# 34. E-commerce Product Analytics

Core funnel:

```text
Visit
 ↓
Search
 ↓
Product View
 ↓
Add to Cart
 ↓
Checkout
 ↓
Purchase
```

Useful metrics:

```text
Search conversion
Product conversion
Add-to-cart rate
Cart abandonment
Checkout abandonment
Purchase conversion
AOV
Repeat purchase
```

---

# 35. Marketplace Analytics

Marketplaces have at least two sides.

```text
Buyer
    ↕
Marketplace
    ↕
Seller
```

Metrics may include:

### Buyer side

```text
Searches
Views
Purchases
Repeat purchases
```

### Seller side

```text
Listings
Orders
Fulfillment
Seller retention
```

A marketplace must often balance:

```text
Supply
vs
Demand
```

---

# 36. SaaS Analytics

Typical SaaS funnel:

```text
Visitor
 ↓
Signup
 ↓
Activation
 ↓
Trial
 ↓
Paid
 ↓
Renewal
 ↓
Expansion
```

Key metrics:

```text
Activation rate
Trial conversion
MRR
ARR
Churn
NRR
LTV
CAC
```

---

# 37. Mobile App Analytics

Important dimensions:

```text
OS
Device
Version
Country
Acquisition source
```

Metrics:

```text
Install
Activation
D1 retention
D7 retention
D30 retention
Crash rate
Session frequency
Feature adoption
```

Always investigate version-specific changes.

Example:

```text
Retention suddenly falls after version 8.2.
```

Potential explanation:

```text
Bug introduced in 8.2.
```

---

# 38. B2B Product Analytics

B2B products differ because users and buyers may be different.

```text
Employee
    ↓
Uses product

Manager
    ↓
Evaluates product

Procurement
    ↓
Purchases product

Executive
    ↓
Renews contract
```

Analyze:

```text
Seat activation
Team adoption
Account engagement
Feature usage
Expansion
Renewal
```

Account-level analytics is critical.

---

# 39. Customer Analytics

Customer analytics connects:

```text
Behavior
+
Value
+
Lifecycle
```

Possible segments:

```text
New
Activated
Engaged
At-risk
Churned
Returning
Power user
High-value
```

---

# 40. Customer Lifetime Value

Basic LTV concept:

```text
LTV ≈ Average Revenue per Customer
      × Customer Lifetime
```

For subscription products:

```text
LTV ≈ ARPA × Gross Margin / Churn Rate
```

These are simplified models and depend on assumptions.

LTV should be treated as an estimate rather than a perfectly known quantity.

---

# 41. Customer Acquisition Cost

CAC:

```text
CAC =
Total Acquisition Cost
/
Number of New Customers
```

Example:

```text
Marketing + Sales = $100,000
New customers = 2,000

CAC = $50
```

But acquisition cost definitions should be consistent.

---

# 42. LTV:CAC

A commonly used comparison:

```text
LTV:CAC =
LTV / CAC
```

Example:

```text
LTV = $300
CAC = $100

LTV:CAC = 3
```

The appropriate target depends heavily on business model, margins, growth stage, and measurement assumptions.

---

# 43. Product Analytics Data Model

A simple event table:

| user_id | event        | timestamp | platform | product_id |
| ------- | ------------ | --------- | -------- | ---------- |
| 1       | signup       | ...       | web      | null       |
| 1       | product_view | ...       | web      | 101        |
| 1       | add_to_cart  | ...       | web      | 101        |
| 1       | purchase     | ...       | web      | 101        |

Useful tables:

```text
users
events
sessions
products
orders
subscriptions
experiments
experiment_assignments
```

---

# 44. SQL for Product Analytics

## Daily active users

```sql
SELECT
    DATE(timestamp) AS day,
    COUNT(DISTINCT user_id) AS dau
FROM events
WHERE event = 'meaningful_action'
GROUP BY DATE(timestamp)
ORDER BY day;
```

## Funnel

```sql
SELECT
    COUNT(DISTINCT CASE
        WHEN event = 'signup'
        THEN user_id END) AS signups,

    COUNT(DISTINCT CASE
        WHEN event = 'activation'
        THEN user_id END) AS activated,

    COUNT(DISTINCT CASE
        WHEN event = 'purchase'
        THEN user_id END) AS purchasers
FROM events;
```

## Feature adoption

```sql
SELECT
    COUNT(DISTINCT user_id) * 1.0 /
    (SELECT COUNT(DISTINCT user_id) FROM users) AS adoption_rate
FROM events
WHERE event = 'feature_used';
```

## Users with multiple purchases

```sql
SELECT
    user_id,
    COUNT(*) AS purchases
FROM events
WHERE event = 'purchase'
GROUP BY user_id
HAVING COUNT(*) > 1;
```

## Revenue by channel

```sql
SELECT
    acquisition_channel,
    SUM(revenue) AS revenue
FROM purchases
GROUP BY acquisition_channel
ORDER BY revenue DESC;
```

---

# 45. Python for Product Analytics

Typical workflow:

```python
import pandas as pd
import matplotlib.pyplot as plt

events = pd.read_csv("events.csv")

events["timestamp"] = pd.to_datetime(events["timestamp"])

daily_users = (
    events
    .groupby(events["timestamp"].dt.date)["user_id"]
    .nunique()
)

daily_users.plot()
plt.title("Daily Active Users")
plt.xlabel("Date")
plt.ylabel("Users")
plt.show()
```

### Funnel calculation

```python
steps = [
    "signup",
    "activation",
    "add_to_cart",
    "purchase"
]

funnel = {}

for step in steps:
    funnel[step] = events.loc[
        events["event"].eq(step),
        "user_id"
    ].nunique()

funnel
```

---

# 46. Visualization

Useful visualizations:

### Time series

```text
DAU
Revenue
Retention
Conversion
```

### Funnel

```text
Visitors
 ↓
Signups
 ↓
Activation
 ↓
Purchase
```

### Cohort heatmap

Useful for:

```text
Retention
Revenue
Engagement
```

### Segmentation

Useful for:

```text
Country
Device
Plan
Channel
```

### Distribution

Useful for:

```text
Order value
Sessions
Time to activation
Number of purchases
```

---

# 47. Dashboards

A useful product dashboard should answer:

```text
1. Are we healthy?
2. What changed?
3. Where did it change?
4. Why might it have changed?
5. What should we investigate?
```

Example dashboard:

```text
------------------------------------------------
PRODUCT HEALTH
------------------------------------------------

DAU          125K       ↑ 8%
WAU          310K       ↑ 4%
MAU          820K       ↑ 3%

Activation   42%        ↑ 5%
Retention    31%        ↓ 2%
Conversion   8.2%       ↑ 0.7%

------------------------------------------------
FUNNEL
------------------------------------------------

Visitors        100%
Signup           32%
Activation       18%
Purchase          8%

------------------------------------------------
RETENTION
------------------------------------------------

Cohort | D1 | D7 | D30
Jan    | 48 | 31 | 20
Feb    | 51 | 34 | 22
Mar    | 54 | 37 | 25
------------------------------------------------
```

A dashboard should support decisions rather than simply display numbers.

---

# 48. Analytics Workflow

A professional workflow:

```text
1. Define business problem
          ↓
2. Define analytical question
          ↓
3. Define hypothesis
          ↓
4. Identify required data
          ↓
5. Validate data
          ↓
6. Explore
          ↓
7. Segment
          ↓
8. Analyze
          ↓
9. Visualize
          ↓
10. Communicate
          ↓
11. Recommend action
          ↓
12. Measure outcome
```

---

# 49. Common Mistakes

## Mistake 1 — Vanity metrics

Example:

```text
Total downloads
```

without asking whether users actually use the product.

---

## Mistake 2 — Confusing correlation with causation

```text
Users using feature X retain better.
```

This does not prove X causes retention.

---

## Mistake 3 — Ignoring denominators

Never report:

```text
500 purchases
```

without context.

Prefer:

```text
500 / 10,000 eligible users = 5%
```

---

## Mistake 4 — Looking only at averages

Average users may hide:

```text
Power users
Casual users
Inactive users
```

---

## Mistake 5 — Over-segmentation

Creating hundreds of segments increases noise and false discoveries.

---

## Mistake 6 — Optimizing one metric

```text
Conversion ↑
Retention ↓
Refunds ↑
```

may be a bad product change.

---

## Mistake 7 — Ignoring data quality

Before analyzing:

```text
Missing values
Duplicates
Invalid timestamps
Incorrect events
Bot traffic
Tracking changes
```

must be investigated.

---

# 50. Product Analytics Case Study

## Scenario

You work as a Product Analyst for an e-commerce company.

The company reports:

```text
Traffic ↑ 20%
Signups ↑ 15%
Purchases ↓ 8%
```

The product manager asks:

> Why are purchases decreasing?

### Step 1 — Don't immediately conclude

Possible causes:

```text
Traffic quality
Conversion
Product availability
Checkout
Payment
Pricing
Technical bugs
Seasonality
```

### Step 2 — Build funnel

```text
Visitors
 ↓
Signups
 ↓
Product Views
 ↓
Cart
 ↓
Checkout
 ↓
Purchase
```

### Step 3 — Segment

Compare:

```text
Mobile vs Desktop
New vs Existing
Country
Traffic source
Browser
App version
```

### Step 4 — Find anomaly

Suppose:

```text
Desktop conversion = stable

Mobile conversion = -20%
```

Then investigate mobile.

Suppose:

```text
Android 8.4 = -35%
iOS = stable
```

Now investigate Android version 8.4.

Suppose a checkout payment error increased:

```text
2% → 18%
```

The likely explanation becomes:

```text
Android 8.4
→ checkout payment failures
→ lower purchase conversion
→ lower purchases
```

This is much stronger than saying:

> "Purchases decreased because users don't like the new design."

---

# 51. Exercises

## Exercise 1 — Metric Classification

Classify each as:

```text
Acquisition
Activation
Engagement
Retention
Revenue
Diagnostic
```

1. Signup rate
2. D30 retention
3. Revenue
4. Sessions per user
5. CAC
6. Product-view rate
7. Payment error rate
8. Trial activation

---

## Exercise 2 — Funnel

Given:

```text
Visitors = 20,000
Signups = 6,000
Activated = 3,000
Cart = 1,500
Purchases = 900
```

Calculate:

1. Visitor → signup
2. Signup → activation
3. Activation → cart
4. Cart → purchase
5. Visitor → purchase

Then identify the largest percentage drop.

---

## Exercise 3 — Retention

A cohort contains:

```text
Day 0 = 5,000
Day 1 = 2,000
Day 7 = 1,250
Day 30 = 500
```

Calculate:

```text
D1
D7
D30
```

Then explain which metric is most concerning.

---

## Exercise 4 — DAU/MAU

Given:

```text
DAU = 25,000
MAU = 125,000
```

Calculate stickiness.

What does the result mean?

---

## Exercise 5 — Segmentation

Overall conversion:

```text
8%
```

Segments:

```text
Mobile = 5%
Desktop = 12%
```

Questions:

1. What should you investigate?
2. What additional dimensions would you examine?
3. Can you conclude mobile users are less valuable?

---

## Exercise 6 — Feature Adoption

A product has:

```text
100,000 eligible users
20,000 tried the feature
8,000 used it again
```

Calculate:

```text
Trial adoption
Repeat usage among adopters
Repeat usage among eligible users
```

Interpret the results.

---

## Exercise 7 — Churn

At the beginning of the month:

```text
Customers = 10,000
Customers lost = 700
```

Calculate churn.

Then investigate possible causes.

---

## Exercise 8 — SQL

Write SQL to calculate:

```text
daily active users
```

where an active user is defined as someone who performs:

```text
purchase
```

---

## Exercise 9 — SQL Funnel

Write SQL that calculates the number of unique users who:

```text
signup
activation
purchase
```

Then calculate conversion between stages.

---

## Exercise 10 — Cohort Analysis

Given:

```text
January cohort = 1,000
D7 = 400
D30 = 250

February cohort = 1,500
D7 = 525
D30 = 300

March cohort = 2,000
D7 = 800
D30 = 500
```

Calculate D7 and D30 retention for each cohort.

Which cohort performs best?

---

# 52. Advanced Exercises

## Exercise 11 — Diagnose a Funnel

You receive:

```text
Visitors:       +30%
Signups:        +25%
Activation:     +20%
Cart:           -5%
Checkout:       -10%
Purchases:      -18%
```

Write a complete analytical investigation.

Consider:

```text
Acquisition quality
Product changes
Pricing
Inventory
Checkout
Payment
Technical errors
Device
Country
Traffic source
```

---

## Exercise 12 — Experiment Analysis

Control:

```text
Users = 50,000
Purchases = 5,000
```

Treatment:

```text
Users = 50,000
Purchases = 5,400
```

Calculate:

```text
Conversion A
Conversion B
Absolute lift
Relative lift
```

Then explain why this alone is not enough to declare success.

---

## Exercise 13 — Feature Impact

Users who adopted a feature:

```text
Retention = 45%
```

Non-adopters:

```text
Retention = 25%
```

Question:

> Can we conclude that the feature increases retention?

Explain the confounding problem.

Design an experiment to investigate.

---

## Exercise 14 — Product Diagnosis

A company has:

```text
DAU ↑
Sessions ↑
Revenue ↓
Retention ↓
```

Generate at least five hypotheses.

Rank them according to:

```text
Impact
Likelihood
Ease of investigation
```

---

## Exercise 15 — Product Decision

Two features are proposed.

### Feature A

```text
Expected users = 100,000
Expected adoption = 30%
Expected revenue impact = $50K/month
```

### Feature B

```text
Expected users = 20,000
Expected adoption = 80%
Expected revenue impact = $100K/month
```

Which would you prioritize?

What additional information would you request before deciding?

---

# 53. Portfolio Projects

## Project 1 — E-commerce Funnel Analytics

Build:

```text
Event dataset
↓
Cleaning
↓
Funnel
↓
Conversion
↓
Segmentation
↓
Dashboard
↓
Recommendations
```

Questions:

* Where do users drop?
* Which device performs best?
* Which acquisition channel converts?
* Which products have high abandonment?

---

## Project 2 — SaaS Retention Analytics

Build:

```text
Signup cohorts
↓
D1/D7/D30 retention
↓
Feature adoption
↓
Churn analysis
```

Deliver:

* cohort table
* retention visualization
* churn segments
* recommendations

---

## Project 3 — A/B Testing

Create:

```text
Control
Treatment
```

Analyze:

```text
Conversion
Revenue
Retention
Guardrails
```

Perform statistical testing.

---

## Project 4 — Product Health Dashboard

Create a dashboard containing:

```text
DAU
WAU
MAU
Activation
Retention
Conversion
Revenue
Feature adoption
```

Then create an executive summary:

```text
What changed?
Why?
What should we do?
```

---

## Project 5 — Product Analytics for Logistics

This is particularly useful for applying Product Analytics to your interest in logistics and supply chains.

Imagine a logistics platform.

Users:

```text
Drivers
Dispatchers
Customers
Warehouse operators
Managers
```

Events:

```text
shipment_created
shipment_assigned
driver_accepted
pickup_completed
delivery_started
delivery_completed
delivery_failed
```

Analyze:

```text
Driver activation
Shipment funnel
Delivery completion
Failed deliveries
Time to assignment
Driver retention
Customer retention
```

Then investigate:

> Which behavioral patterns predict successful deliveries?

---

# 54. Product Analytics Checklist

Before starting:

```text
[ ] What is the business problem?
[ ] What decision needs to be made?
[ ] Who is the user?
[ ] What behavior matters?
[ ] What is the desired outcome?
```

Data:

```text
[ ] Are events correctly tracked?
[ ] Are timestamps valid?
[ ] Are users duplicated?
[ ] Are bots excluded?
[ ] Are missing values understood?
```

Analysis:

```text
[ ] Calculate rates, not only counts
[ ] Compare cohorts
[ ] Segment important populations
[ ] Check time trends
[ ] Investigate anomalies
[ ] Consider alternative explanations
```

Experiment:

```text
[ ] Define hypothesis
[ ] Define primary metric
[ ] Define guardrails
[ ] Randomize correctly
[ ] Determine sample size
[ ] Avoid early stopping
[ ] Analyze uncertainty
```

Communication:

```text
[ ] What happened?
[ ] Why?
[ ] How confident are we?
[ ] What should we do?
[ ] How will we measure success?
```

---

# 55. Final Mental Model

The most important Product Analytics mental model is:

```text
                    PRODUCT
                       │
                       ↓
                  USER BEHAVIOR
                       │
          ┌────────────┼────────────┐
          ↓            ↓            ↓
      Acquisition   Engagement   Retention
          │            │            │
          └────────────┼────────────┘
                       ↓
                    VALUE
                       ↓
                  CONVERSION
                       ↓
                    REVENUE
                       ↓
                  BUSINESS
                    IMPACT
```

But analytics should work in the opposite direction too:

```text
Business Problem
       ↓
Product Question
       ↓
User Behavior
       ↓
Data
       ↓
Metric
       ↓
Analysis
       ↓
Hypothesis
       ↓
Experiment
       ↓
Evidence
       ↓
Decision
       ↓
Product Change
       ↓
Measure Again
```

The goal is therefore **not to become someone who calculates more metrics**.

The goal is to become someone who can move from:

```text
DATA
  ↓
BEHAVIOR
  ↓
INSIGHT
  ↓
DECISION
  ↓
ACTION
  ↓
IMPACT
```

That is the core of Product Analytics.

---

# Recommended Learning Order

For practical mastery, study in this order:

```text
1. Product Analytics Mindset
2. Events & Tracking
3. Metrics
4. Funnels
5. Segmentation
6. Cohorts
7. Retention
8. Engagement
9. Feature Analytics
10. User Journeys
11. SQL
12. Python
13. Visualization
14. Experimentation
15. A/B Testing
16. Causal Thinking
17. Revenue Analytics
18. LTV / CAC
19. Product Dashboards
20. Complete Case Studies
```

Then combine Product Analytics with your existing strengths:

```text
Product Analytics
       +
Statistics
       +
Time Series
       +
Experimentation
       +
Machine Learning
       +
Software Engineering
       ↓
Advanced Product / Decision Analytics
```

This combination is especially useful for domains such as:

```text
E-commerce
SaaS
Manufacturing
Transportation
Logistics
Supply Chain
FinTech
```

---

# Final Challenge

Build a complete Product Analytics project where you receive only raw events.

Your job:

```text
Raw Events
    ↓
Data Quality
    ↓
Event Taxonomy
    ↓
Metrics
    ↓
Funnel
    ↓
Cohorts
    ↓
Retention
    ↓
Segmentation
    ↓
Feature Analysis
    ↓
Experiment
    ↓
Statistical Analysis
    ↓
Dashboard
    ↓
Business Recommendation
```

Your final report should answer only five questions:

### 1. What happened?

### 2. Why did it happen?

### 3. Who was affected?

### 4. What should the product team do?

### 5. How will we know whether the solution worked?

If you can answer these questions from messy behavioral data, you are practicing **real Product Analytics**, rather than simply creating dashboards.
