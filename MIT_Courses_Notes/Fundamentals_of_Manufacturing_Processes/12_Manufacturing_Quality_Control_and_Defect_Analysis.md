
# Module 12: Manufacturing Quality Control and Defect Analysis

## 1. Learning Objectives

- Distinguish quality assurance, quality control, inspection, and process improvement.
- Understand variation, defect rates, yield, and process capability.
- Calculate control limits, defect rates, and basic process capability indices.
- Interpret control charts and distinguish common-cause from special-cause variation.
- Apply root-cause analysis, Pareto analysis, fishbone diagrams, and the 5 Whys.
- Explain failure mode and effects analysis (FMEA).
- Design experiments for manufacturing process improvement.
- Connect quality engineering with automation, industrial R&D, and continuous improvement.

## 2. Introduction

Manufacturing quality is the degree to which a product or process satisfies defined requirements and intended use.

Quality engineering is not limited to finding defective products. It also aims to prevent defects, reduce variation, understand failure mechanisms, and maintain stable production.

Applications include:
- Automotive safety-critical components.
- Aerospace structures and propulsion systems.
- Electronic circuit boards and semiconductor packaging.
- Medical devices.
- Industrial machinery and consumer products.

A mature quality system integrates product design, material control, process validation, measurement, supplier management, traceability, and corrective action.

## 3. Quality Assurance and Quality Control

**Quality assurance (QA)** focuses on planned systems and activities intended to provide confidence that requirements will be met.

**Quality control (QC)** focuses on operational techniques and activities used to verify and control product or process conformity.

**Inspection** measures or examines characteristics to determine whether specified requirements are satisfied.

**Process improvement** systematically changes a process to achieve better performance, such as lower defect rates, shorter cycle time, or reduced cost.

Inspection alone cannot guarantee quality. A process that continuously creates defects may remain expensive even if every defect is detected.

## 4. Manufacturing Variation

Manufacturing output varies because of:
- Material batches.
- Tool wear.
- Machine condition.
- Operator methods.
- Temperature and humidity.
- Measurement systems.
- Setup variation.
- Supplier variation.
- Process interactions.

Variation can be described statistically.

For observations \(x_1,x_2,\ldots,x_n\), the sample mean is:

\[
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i
\]

The sample standard deviation is:

\[
s=\sqrt{\frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}}
\]

where:
- \(\bar{x}\) = sample mean.
- \(s\) = sample standard deviation.
- \(n\) = sample size.
- \(x_i\) = individual observation.

The sample standard deviation estimates dispersion around the sample mean. Its reliability depends on sample size and the data-generating process.

## 5. Defects, Defectives, and Yield

A **defect** is a nonconforming characteristic or failure to meet a requirement.

A **defective unit** is a unit classified as nonconforming under the defined acceptance rules.

One unit may contain multiple defects.

First-pass yield is commonly defined as:

\[
FPY=\frac{\text{Units passing without rework}}
{\text{Units entering the process}}\times100\%
\]

### Numerical Example 1: First-pass yield

A line processes 2,000 units. Of these, 1,860 pass without rework.

\[
FPY=\frac{1860}{2000}\times100\%=93\%
\]

**Answer:** First-pass yield is 93%.

If reworked units eventually pass, final yield may be higher than first-pass yield. Both metrics are useful, but they answer different questions.

## 6. Defect Rates and DPMO

Defects per million opportunities (DPMO) is calculated as:

\[
DPMO=
\frac{D}{N O}\times10^6
\]

where:
- \(D\) = total defects observed.
- \(N\) = number of units inspected.
- \(O\) = defined opportunities for defects per unit.

The opportunity definition must be consistent and meaningful.

### Numerical Example 2: DPMO

A process produces 5,000 units. Inspectors identify 40 defects across a defined set of 4 opportunities per unit.

\[
DPMO=\frac{40}{5000(4)}\times10^6
\]

\[
DPMO=2000
\]

**Answer:** 2,000 defects per million opportunities.

DPMO is not the same as the percentage of defective units.

## 7. Statistical Process Control

Statistical process control (SPC) uses process data to assess stability and identify unusual changes.

Two broad categories of variation are:

- **Common-cause variation:** Variation inherent in the current process system.
- **Special-cause variation:** Variation associated with a specific, identifiable change or event.

A stable process is not necessarily capable of meeting specifications. Stability and capability must be evaluated separately.

### 7.1 Control charts

A control chart plots a statistic over time with a center line and statistically determined control limits.

Common examples include:
- \(\bar{X}\)- and R-charts.
- \(\bar{X}\)- and S-charts.
- Individuals and moving-range charts.
- p-charts.
- np-charts.
- c-charts.
- u-charts.

The appropriate chart depends on the data type, sampling plan, and statistical assumptions.

### 7.2 Individuals-chart limits

For an individuals chart using a moving range of two consecutive observations, a common estimate is:

\[
UCL=\bar{x}+2.66\overline{MR}
\]

\[
CL=\bar{x}
\]

\[
LCL=\bar{x}-2.66\overline{MR}
\]

where:
- \(UCL\) = upper control limit.
- \(CL\) = center line.
- \(LCL\) = lower control limit.
- \(\bar{x}\) = average of individual observations.
- \(\overline{MR}\) = average moving range.

These constants apply to the specified individuals/moving-range setup. Other chart designs use different factors.

### Numerical Example 3: Individuals-chart limits

Suppose:

\[
\bar{x}=50.0\text{ mm},\qquad \overline{MR}=0.30\text{ mm}
\]

Then:

\[
UCL=50.0+2.66(0.30)=50.798\text{ mm}
\]

\[
LCL=50.0-2.66(0.30)=49.202\text{ mm}
\]

**Answer:** Approximate limits are 50.798 mm and 49.202 mm.

These limits are statistical process-control limits, not product specification limits. Additional run-pattern rules may identify instability even when no point exceeds a limit.

## 8. Process Capability

Capability indices compare process variation and centering with engineering specifications.

The within-process capability index is commonly written as:

\[
C_p=\frac{USL-LSL}{6\sigma}
\]

The centered capability index is:

\[
C_{pk}=
\min\left(
\frac{USL-\mu}{3\sigma},
\frac{\mu-LSL}{3\sigma}
\right)
\]

where:
- \(USL\) = upper specification limit.
- \(LSL\) = lower specification limit.
- \(\mu\) = process mean.
- \(\sigma\) = appropriate estimate of within-process standard deviation.

\(C_p\) measures potential capability under the model, while \(C_{pk}\) accounts for off-center operation.

Capability indices are meaningful only when the process is sufficiently stable and the assumptions behind the estimates are reasonable. Non-normal data may require alternative methods.

### Numerical Example 4: Capability

A component specification is 10.00 ± 0.15 mm. Assume a stable process with mean 10.02 mm and standard deviation 0.03 mm.

\[
USL=10.15\text{ mm}
\]

\[
LSL=9.85\text{ mm}
\]

\[
C_p=\frac{10.15-9.85}{6(0.03)}
=\frac{0.30}{0.18}
\approx1.67
\]

For \(C_{pk}\):

\[
C_{pu}=\frac{10.15-10.02}{3(0.03)}
=\frac{0.13}{0.09}\approx1.44
\]

\[
C_{pl}=\frac{10.02-9.85}{3(0.03)}
=\frac{0.17}{0.09}\approx1.89
\]

\[
C_{pk}=\min(1.44,1.89)=1.44
\]

**Answer:** \(C_p\approx1.67\) and \(C_{pk}\approx1.44\).

The lower \(C_{pk}\) reflects the process mean being closer to the upper specification limit.

## 9. Root-Cause Analysis

Root-cause analysis attempts to identify the underlying mechanisms responsible for a problem rather than merely treating its symptoms.

Common tools include:

### Pareto analysis

Ranks categories by frequency, cost, severity, or another selected measure.

A Pareto chart can help prioritize improvement, but it does not prove causation.

### Fishbone diagram

Organizes possible causes under categories such as:
- People.
- Equipment.
- Materials.
- Methods.
- Measurement.
- Environment.

The categories should be adapted to the problem.

### Five Whys

Repeatedly asks why a problem occurred to develop a causal explanation.

It should not be used mechanically: real problems may have several interacting causes.

### Fault tree analysis

Uses logical relationships between failure events to investigate how a system-level failure may occur.

### Design of experiments

DOE evaluates the effects of selected factors and their interactions using a planned experimental design.

## 10. Failure Mode and Effects Analysis

FMEA systematically identifies potential failure modes, their effects, causes, and controls.

Typical entries include:
- Failure mode.
- Effect of failure.
- Cause or mechanism.
- Existing prevention controls.
- Detection controls.
- Severity.
- Occurrence.
- Detection rating.
- Recommended actions.

Some FMEA approaches calculate a risk priority number:

\[
RPN=S\times O\times D
\]

where:
- \(S\) = severity rating.
- \(O\) = occurrence rating.
- \(D\) = detection rating.

The rating scales must be defined by the organization or applicable methodology.

An RPN is a prioritization aid, not a complete risk model. A high-severity failure may require action even if its RPN is not the largest.

## 11. Corrective and Preventive Action

A structured improvement cycle may include:

1. Define the problem quantitatively.
2. Contain potentially affected product.
3. Verify measurement-system reliability.
4. Collect process and inspection evidence.
5. Identify plausible causal mechanisms.
6. Test the most important hypotheses.
7. Implement corrective action.
8. Validate effectiveness.
9. Update procedures and training.
10. Monitor for recurrence.

A corrective action should address the cause of the problem, not merely add another inspection step.

## 12. Quality Costs

Quality-related costs include:
- Prevention costs.
- Appraisal costs.
- Internal failure costs.
- External failure costs.

Internal failures include scrap and rework discovered before delivery. External failures include warranty claims, returns, and field failures.

Reducing inspection costs while increasing external failures may worsen total cost of quality.

## 13. Automation and Industrial R&D

Modern quality engineering uses:
- Machine vision.
- Automated dimensional inspection.
- Sensor-based monitoring.
- Manufacturing execution systems.
- Statistical dashboards.
- Predictive maintenance.
- Traceability systems.
- Machine-learning-assisted anomaly detection.

Data analytics must account for missing measurements, class imbalance, changing process conditions, label quality, and false alarms.

An algorithm that detects known defects in historical data is not necessarily reliable when applied to new products or machines.

## 14. Common Misconceptions

- Inspection alone creates quality.
- A stable process is automatically capable.
- Control limits and specification limits are interchangeable.
- A high DPMO necessarily means the same percentage of units is defective.
- The largest Pareto category is always the root cause.
- A high capability index proves the measurement system is reliable.
- Every FMEA failure should be prioritized by RPN alone.
- More data always leads to better decisions.

## 15. Summary

Quality engineering uses measurement, statistics, process knowledge, and structured problem-solving to prevent defects and improve production. SPC assesses stability, while capability analysis compares process behavior with specifications. Root-cause analysis and FMEA help identify risks and prioritize action. Effective improvement requires reliable measurements, validated causal explanations, and continued monitoring.

## 16. Review Questions

1. Distinguish quality assurance from quality control.
2. Calculate first-pass yield for 970 conforming units out of 1,000 processed.
3. Explain the difference between a defect and a defective unit.
4. Distinguish control limits from specification limits.
5. What assumptions support interpretation of \(C_p\) and \(C_{pk}\)?
6. Why does a stable process not necessarily meet specifications?
7. Explain how a Pareto chart supports prioritization.
8. What are the limitations of an RPN in FMEA?
9. How can measurement-system variation mislead a quality investigation?
10. Design a quality-improvement experiment for recurring injection-molding defects.

## 17. Challenging Exercises with Complete Solutions

### Exercise 1: Yield and defectives

A line processes 4,000 units. Of these, 3,880 pass without rework. Calculate first-pass yield and the percentage that fail first-pass inspection.

**Solution**

\[
FPY=\frac{3880}{4000}\times100\%=97\%
\]

First-pass failure percentage:

\[
100\%-97\%=3\%
\]

**Answer:** First-pass yield is 97%, and first-pass failures account for 3%.

### Exercise 2: DPMO

A batch of 10,000 units has 60 observed defects across 3 defined opportunities per unit. Calculate DPMO.

**Solution**

\[
DPMO=\frac{60}{10{,}000(3)}\times10^6
\]

\[
DPMO=2000
\]

**Answer:** 2,000 DPMO.

### Exercise 3: Process capability

A stable process has \(USL=50.20\) mm, \(LSL=49.80\) mm, mean \(50.05\) mm, and standard deviation \(0.05\) mm. Calculate \(C_p\) and \(C_{pk}\).

**Solution**

\[
C_p=\frac{50.20-49.80}{6(0.05)}
=\frac{0.40}{0.30}=1.33
\]

Upper capability:

\[
C_{pu}=\frac{50.20-50.05}{3(0.05)}
=\frac{0.15}{0.15}=1.00
\]

Lower capability:

\[
C_{pl}=\frac{50.05-49.80}{3(0.05)}
=\frac{0.25}{0.15}=1.67
\]

\[
C_{pk}=\min(1.00,1.67)=1.00
\]

**Answer:** \(C_p\approx1.33\), \(C_{pk}=1.00\).

### Exercise 4: FMEA prioritization

A failure mode has severity 8, occurrence 4, and detection rating 5. Calculate RPN. A proposed action reduces occurrence to 2 and detection rating to 3, with severity unchanged.

**Solution**

Initial:

\[
RPN_1=8(4)(5)=160
\]

After action:

\[
RPN_2=8(2)(3)=48
\]

Reduction:

\[
160-48=112
\]

Percentage reduction:

\[
\frac{112}{160}\times100\%=70\%
\]

**Answer:** RPN decreases from 160 to 48, a 70% reduction under the defined scoring model. The team must separately verify that the action actually reduces risk.

### Exercise 5: Cost of poor quality

A factory produces 20,000 units per month. Its defect rate is 4%, and each defective unit costs \$18 in scrap or rework. A proposed improvement reduces the defect rate to 1.5% and costs \$3,000 per month. Determine the net monthly benefit.

**Solution**

Initial defective units:

\[
N_1=20{,}000(0.04)=800
\]

Initial failure cost:

\[
C_1=800(18)=\$14{,}400
\]

New defective units:

\[
N_2=20{,}000(0.015)=300
\]

New failure cost:

\[
C_2=300(18)=\$5{,}400
\]

Gross savings:

\[
S=14{,}400-5{,}400=\$9{,}000
\]

Net benefit:

\[
B=9{,}000-3{,}000=\$6{,}000
\]

**Answer:** Estimated net monthly benefit is \$6,000, assuming the stated rates and costs remain valid.

## 18. Glossary

- **Capability:** Ability of a process to meet specifications under defined assumptions.
- **Common-cause variation:** Variation arising from the existing process system.
- **Control chart:** Time-ordered chart with statistically derived control limits.
- **Defect:** Nonconforming characteristic or failure to meet a requirement.
- **DPMO:** Defects per million opportunities.
- **FMEA:** Failure Mode and Effects Analysis.
- **First-pass yield:** Proportion of units passing without rework.
- **Quality assurance:** Planned activities intended to provide confidence in conformity.
- **Quality control:** Operational activities used to assess and control conformity.
- **Root-cause analysis:** Investigation of underlying failure mechanisms.
- **Special-cause variation:** Variation attributable to a specific unusual influence.
- **SPC:** Statistical Process Control.

## 19. References and Further Learning

1. [NIST Engineering Statistics Handbook](https://www.itl.nist.gov/div898/handbook/) — statistical methods and process analysis.
2. [ASQ](https://asq.org/) — quality engineering, SPC, and improvement methods.
3. [ISO 9001](https://www.iso.org/iso-9001-quality-management.html) — quality management systems.
4. [AIAG](https://www.aiag.org/) — automotive quality tools and FMEA resources.
5. [ASTM International](https://www.astm.org/) — inspection and testing standards.
6. Montgomery, D. C. *Introduction to Statistical Quality Control*.

This is a custom instructional module, not an official MIT syllabus. Use appropriate statistical assumptions and applicable quality standards when applying these calculations to real production.