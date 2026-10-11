# 04 — Elicitation and Collaboration

## 1. Introduction

Elicitation and Collaboration focuses on discovering information relevant to business analysis, confirming that the information is understood, communicating findings, and working effectively with stakeholders.

At the CBAP level, elicitation is more than asking questions. It requires selecting suitable techniques, managing competing perspectives, uncovering implicit needs, validating evidence, facilitating decisions, and maintaining productive stakeholder relationships.

## 2. Elicitation Fundamentals

Elicitation is the activity of drawing out or discovering information from stakeholders and other sources.

It may involve:

* Direct communication.
* Workshops.
* Interviews.
* Observation.
* Document analysis.
* Surveys.
* Experiments.
* Prototypes.
* Existing operational data.
* Market and industry research.

Elicitation is iterative. Information discovered in one activity may reveal new questions or invalidate earlier assumptions.

### 2.1 Elicitation Versus Requirements Gathering

Requirements gathering can imply collecting information that stakeholders already know and can articulate.

Elicitation is broader because important information may be:

* Implicit.
* Incomplete.
* Contradictory.
* Unknown to stakeholders.
* Hidden within existing processes.
* Difficult to express verbally.

A business analyst must help stakeholders discover and clarify their needs rather than simply record their initial statements.

## 3. Preparing for Elicitation

Preparation improves the quality and efficiency of elicitation activities.

Before an activity, define:

* Purpose and expected outcomes.
* Scope and boundaries.
* Required participants.
* Questions and discussion topics.
* Relevant background information.
* Technique and facilitation method.
* Time and resource constraints.
* Tools and materials.
* Documentation approach.
* Follow-up responsibilities.

Preparation should also consider stakeholder availability, accessibility needs, language differences, organizational sensitivities, and confidentiality.

### 3.1 Elicitation Objectives

Objectives should be specific enough to guide the session.

Weak objective:

"Discuss the new reporting system."

Improved objective:

"Identify the three most important reporting decisions, define the information needed for each, and document unresolved disagreements about metric definitions."

Clear objectives help determine whether the activity has succeeded.

## 4. Interviews

Interviews involve structured or semi-structured conversations with stakeholders or subject-matter experts.

### 4.1 Interview Types

**Structured interviews:** Use a predefined set of questions in a consistent order.

**Semi-structured interviews:** Use prepared questions while allowing exploration of emerging topics.

**Unstructured interviews:** Allow open-ended discussion when the subject is exploratory or poorly understood.

### 4.2 Effective Interview Questions

Open-ended questions encourage explanation.

Examples:

* How does the current process work?
* What causes the greatest delays?
* What information do you need to make decisions?
* What happens when an exception occurs?
* How do you determine whether the process is successful?

Closed-ended questions confirm specific details.

Examples:

* Is manager approval required?
* Does the system record a timestamp?
* Is the deadline measured in calendar days or business days?

Follow-up questions should explore unclear statements, examples, exceptions, and underlying causes.

### 4.3 Avoiding Leading Questions

A leading question suggests the expected answer.

Weak:

"Wouldn't an automated dashboard solve most of your problems?"

Better:

"What difficulties do you experience when preparing and using reports?"

The second question reduces bias and allows the stakeholder to describe the actual need.

### 4.4 Interview Documentation

Capture:

* Key statements and evidence.
* Business rules.
* Examples and exceptions.
* Assumptions.
* Conflicting perspectives.
* Decisions.
* Open questions.
* Follow-up actions.

Where appropriate, confirm the notes with the participant rather than assuming the analyst's interpretation is correct.

## 5. Workshops

A workshop brings multiple stakeholders together to achieve a defined outcome.

Workshops are useful for:

* Defining business needs.
* Mapping processes.
* Resolving requirement conflicts.
* Prioritizing requirements.
* Developing future-state models.
* Validating assumptions.
* Evaluating solution alternatives.

### 5.1 Workshop Roles

Possible roles include:

* Facilitator.
* Subject-matter experts.
* Decision-maker.
* Note-taker.
* Technical specialist.
* Observer.

The facilitator guides the process and encourages balanced participation. The facilitator should not allow a dominant participant to determine the outcome without appropriate evidence or authority.

### 5.2 Workshop Structure

A practical workshop may follow these steps:

1. State the objective and expected outputs.
2. Confirm scope and ground rules.
3. Present relevant background and evidence.
4. Gather individual perspectives.
5. Discuss similarities and differences.
6. Analyze issues and alternatives.
7. Resolve decisions where possible.
8. Record unresolved items and owners.
9. Summarize agreements and next steps.

### 5.3 Managing Conflict

Conflicts may arise from different incentives, terminology, assumptions, or priorities.

Useful responses include:

* Clarifying definitions.
* Separating facts from opinions.
* Returning to agreed business objectives.
* Making trade-offs explicit.
* Comparing alternatives against common criteria.
* Identifying the authorized decision-maker.
* Recording unresolved issues for escalation.

Consensus is valuable when achievable, but not every decision requires unanimous agreement.

## 6. Observation and Job Shadowing

Observation involves examining stakeholders performing their actual work.

It can reveal:

* Informal workarounds.
* Hidden dependencies.
* Repeated errors.
* Differences between documented and actual processes.
* Interruptions and bottlenecks.
* Environmental constraints.
* Unwritten business rules.

### 6.1 Active and Passive Observation

In active observation, the analyst may ask questions or participate in the activity.

In passive observation, the analyst watches without substantially changing the workflow.

The appropriate method depends on the objective and the risk of influencing the observed behavior.

### 6.2 Example

A procedure document states that employees enter customer information once.

Observation reveals that employees re-enter the same information into three disconnected systems.

The finding identifies a potential integration or process redesign opportunity that interviews alone may not uncover.

### 6.3 Observation Limitations

Observation may be affected by:

* Participants changing their behavior because they are being watched.
* Unusual conditions during the observation period.
* Privacy restrictions.
* Limited access to relevant work.
* The analyst misinterpreting what is observed.

Use additional evidence to validate important conclusions.

## 7. Surveys and Questionnaires

Surveys collect information from a relatively large group of people.

They are useful for:

* Measuring satisfaction.
* Ranking problems.
* Identifying common needs.
* Collecting feedback across locations.
* Testing assumptions at scale.

### 7.1 Survey Design

Effective surveys use:

* Clear language.
* Neutral wording.
* Relevant questions.
* Logical ordering.
* Appropriate response options.
* Reasonable length.
* Clear instructions.

Avoid double-barreled questions.

Weak:

"Is the system fast and easy to use?"

A respondent may find it fast but difficult to use.

Better:

1. How satisfied are you with the system's speed?
2. How easy is the system to use?

### 7.2 Survey Limitations

Potential problems include:

* Low response rates.
* Sampling bias.
* Ambiguous questions.
* Self-selection bias.
* Incomplete responses.
* Overreliance on subjective perceptions.

Survey results should be interpreted according to the sampling method and the characteristics of respondents.

## 8. Document Analysis

Document analysis examines existing information to understand business rules, processes, requirements, and constraints.

Potential sources include:

* Policies and procedures.
* Contracts.
* Existing requirements.
* Process documentation.
* System manuals.
* Reports.
* Regulations.
* Meeting minutes.
* Historical incident records.
* Data dictionaries.

### 8.1 Document Analysis Questions

Ask:

* Is the document current?
* Who owns and approves it?
* Does actual practice match the documented process?
* Are terms defined consistently?
* Are there conflicting versions?
* Are important exceptions missing?
* What assumptions does the document contain?
* What evidence supports its claims?

Documents can provide valuable historical context, but their existence does not guarantee accuracy.

## 9. Prototyping

A prototype is a representation of a possible solution used to explore or validate requirements.

Types include:

* Paper sketches.
* Wireframes.
* Clickable interface mockups.
* Interactive simulations.
* Technical proof-of-concept models.

### 9.1 Benefits

Prototypes help stakeholders:

* Visualize a proposed interface.
* Discover missing requirements.
* Clarify terminology.
* Evaluate alternative workflows.
* Identify usability problems.
* Provide more concrete feedback.

### 9.2 Prototype Risks

Stakeholders may mistake a prototype for a finished product or assume that all demonstrated behavior is feasible and approved.

The analyst should clearly identify:

* What is implemented.
* What is simulated.
* What is not included.
* What assumptions remain unresolved.
* What feedback is being requested.

## 10. Brainstorming and Collaborative Discovery

Brainstorming generates a broad set of ideas before detailed evaluation.

A useful process is:

1. Define the problem.
2. Generate ideas independently or collectively.
3. Record all relevant ideas.
4. Group related ideas.
5. Clarify ambiguous proposals.
6. Evaluate ideas against agreed criteria.
7. Select candidates for further analysis.

Separating idea generation from evaluation can reduce premature rejection of potentially useful alternatives.

Brainstorming produces hypotheses and options, not proof that a proposed solution will work.

## 11. Collaborative Modeling

Collaborative modeling helps stakeholders develop a shared understanding of complex information.

Common models include:

* Process flow diagrams.
* Business process models.
* Context diagrams.
* Data models.
* State diagrams.
* Decision tables.
* Use cases.
* User journey maps.
* Capability maps.

Models can reveal contradictions and omissions more effectively than unstructured discussion.

### 11.1 Process Modeling Example

Consider an order approval process:

1. Customer submits an order.
2. System validates required information.
3. Credit status is checked.
4. Orders within the credit limit are approved automatically.
5. Orders exceeding the limit are routed to a manager.
6. The customer receives an order status update.

The model should also identify exceptions, such as missing information, failed validation, and unavailable approvers.

## 12. Confirming Elicitation Results

Confirmation determines whether the information captured accurately represents what was discussed or discovered.

Activities may include:

* Reviewing meeting notes.
* Confirming business rules.
* Validating process diagrams.
* Demonstrating prototypes.
* Resolving ambiguous statements.
* Checking stakeholder interpretations.
* Recording unresolved questions.

Confirmation of elicitation results is not necessarily formal approval of every requirement.

Formal verification and validation of requirements may involve additional activities and distinct acceptance criteria.

### 12.1 Managing Conflicting Information

When sources disagree:

1. Identify the conflicting statements.
2. Determine the source and authority of each statement.
3. Check dates and document versions.
4. Investigate actual practice.
5. Consult relevant subject-matter experts.
6. Review governing policies and regulations.
7. Document the resolution or escalate the decision.

The analyst should not silently choose one interpretation without a defensible basis.

## 13. Communicating Business Analysis Information

Effective communication ensures that stakeholders understand relevant information and can make appropriate decisions.

### 13.1 Audience Adaptation

Different audiences need different levels of detail.

Executives may need:

* Business outcomes.
* Financial implications.
* Major risks.
* Strategic alternatives.
* Decisions required.

Technical teams may need:

* Detailed requirements.
* Data definitions.
* Integration behavior.
* Constraints.
* Acceptance criteria.

Operations teams may need:

* Process changes.
* Responsibilities.
* Exception handling.
* Training requirements.
* Operational impacts.

### 13.2 Communication Channels

Possible channels include:

* Meetings.
* Reports.
* Presentations.
* Email.
* Collaboration platforms.
* Requirements repositories.
* Dashboards.
* Demonstrations.
* Decision logs.

Select channels based on urgency, complexity, confidentiality, accessibility, and the need for an auditable record.

## 14. Collaboration and Relationship Management

Effective collaboration depends on trust, transparency, listening, and respect for different perspectives.

### 14.1 Active Listening

Active listening involves:

* Giving the speaker attention.
* Asking clarifying questions.
* Paraphrasing key statements.
* Confirming interpretations.
* Identifying emotional or operational concerns.
* Avoiding premature conclusions.

Example:

Stakeholder: "The system never gives us the information we need."

Analyst: "Can you describe a recent decision where the required information was missing?"

The follow-up transforms a broad complaint into an investigable issue.

### 14.2 Psychological Safety

Stakeholders should be able to raise concerns, admit uncertainty, and challenge assumptions without unnecessary fear of embarrassment or retaliation.

Psychological safety can improve the discovery of risks and defects that might otherwise remain hidden.

### 14.3 Distributed and Remote Collaboration

Remote elicitation may require:

* Shared visual collaboration tools.
* Clear agendas.
* Pre-read materials.
* Time-zone coordination.
* Written summaries.
* Explicit decision records.
* Accessible meeting formats.
* Asynchronous feedback opportunities.

Important decisions should not rely solely on informal conversations that affected stakeholders cannot access.

## 15. Advanced Case Study: Manufacturing Quality Problems

### Scenario

A manufacturer experiences an increase in product defects. Management suspects that employees are not following procedures and requests mandatory retraining.

### Elicitation Strategy

**Interviews:** Speak with operators, supervisors, quality engineers, and maintenance staff.

**Observation:** Observe production under normal operating conditions.

**Document analysis:** Review inspection records, work instructions, equipment maintenance logs, and defect reports.

**Data analysis:** Compare defect rates by product, shift, machine, material batch, and operating conditions.

**Workshop:** Bring together relevant stakeholders to evaluate possible causes and validate findings.

### Findings

Illustrative findings reveal:

* A machine has inconsistent calibration.
* A work instruction is outdated.
* Defect rates increase with a particular material batch.
* Training gaps affect only a small subset of operations.

### Recommendation

The evidence supports a combination of equipment maintenance, document correction, supplier investigation, and targeted training rather than mandatory retraining alone.

### Key Lesson

Elicitation techniques complement one another. Interviews reveal perceptions, observation reveals actual behavior, documents provide context, and data analysis helps test hypotheses.

## 16. Knowledge Check

### Questions

1. How does elicitation differ from simply collecting requirements?
2. When is a semi-structured interview appropriate?
3. Why should leading questions be avoided?
4. What advantages do workshops provide over separate interviews?
5. How can observation reveal hidden process problems?
6. What are the main risks of survey-based elicitation?
7. How can prototypes improve requirements discovery?
8. What is the difference between confirming elicitation results and formally approving requirements?
9. How should conflicting stakeholder information be handled?
10. Why should communication be adapted to the audience?

### Answers and Explanations

1. Elicitation actively discovers and clarifies information, including information stakeholders may not initially recognize or articulate.
2. When a common set of topics is needed but follow-up questions and exploration are also valuable.
3. Leading questions introduce bias and may steer stakeholders toward a preferred answer.
4. Workshops support shared understanding, collaborative modeling, and resolution of conflicts among participants.
5. Observation can expose workarounds, bottlenecks, and differences between documented and actual processes.
6. Low response rates, biased samples, ambiguous questions, and incomplete responses.
7. Prototypes make proposed behavior tangible and help stakeholders identify missing or misunderstood requirements.
8. Confirmation checks whether information was captured accurately; formal approval is a governance decision authorizing acceptance or use.
9. Investigate sources, authority, evidence, and context; document the resolution or escalate it appropriately.
10. Stakeholders need information suited to their responsibilities, decisions, and technical knowledge.

## 17. Practical Exercises

### Exercise 1: Interview Design

Prepare a semi-structured interview guide for investigating delays in a customer support process. Include open-ended questions, follow-up questions, and questions designed to validate specific business rules.

### Exercise 2: Workshop Facilitation

Design a 60-minute workshop to resolve disagreement between finance and operations about the definition of an overdue order. Specify the objective, participants, agenda, evidence, and expected output.

### Exercise 3: Observation Plan

Choose a repetitive administrative process. Develop an observation checklist that captures tasks, handoffs, exceptions, waiting time, rework, and workarounds.

### Exercise 4: Survey Quality

Write five survey questions for evaluating a new reporting platform. Identify possible sources of bias and explain how you would improve each question.

### Exercise 5: Triangulation

Choose a business problem and specify how interviews, document analysis, observation, and quantitative data could be combined to validate the underlying cause.

### Exercise 6: Prototype Evaluation

Create a low-fidelity prototype for a business workflow. Define what stakeholders should evaluate and how feedback will be documented, prioritized, and confirmed.

## 18. Recommended References

* IIBA, *A Guide to the Business Analysis Body of Knowledge (BABOK® Guide)*, Version 3.
* IIBA, official CBAP certification resources.
* ISO 9241-210, Human-Centred Design for Interactive Systems.
* ISO 9001, Quality Management Systems — Requirements.
* International Association of Facilitators, professional facilitation resources.

## 19. Module Summary

Elicitation and Collaboration enables business analysts to discover, clarify, confirm, and communicate information while building effective stakeholder relationships. Interviews, workshops, observation, surveys, document analysis, prototyping, and collaborative modeling provide complementary perspectives. The strongest analysis combines these methods, validates evidence, manages conflicting interpretations, and turns stakeholder input into a shared understanding of business needs.
