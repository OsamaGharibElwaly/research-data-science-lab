
# Module 13: Process Selection, Cost, and Productivity

## 1. Learning Objectives

- Select manufacturing processes based on geometry, material, tolerance, volume, and performance.
- Distinguish fixed, variable, direct, indirect, and lifecycle costs.
- Calculate unit cost, break-even quantity, cycle time, throughput, and material utilization.
- Understand production capacity, bottlenecks, work-in-process, and manufacturing lead time.
- Apply basic economic analysis to competing manufacturing processes.
- Explain Overall Equipment Effectiveness (OEE).
- Use decision matrices, sensitivity analysis, and cost models for engineering decisions.
- Connect process selection to industrial R&D, supply chains, automation, and sustainability.

## 2. Introduction

Manufacturing process selection determines how a product will be transformed from raw material into a finished component.

The decision affects:
- Product quality.
- Production cost.
- Lead time.
- Manufacturing flexibility.
- Material utilization.
- Energy consumption.
- Labor requirements.
- Tooling investment.
- Environmental impact.
- Supply-chain resilience.

A process that is technically feasible may still be economically unsuitable. Conversely, a process with a high initial investment may become economical at sufficient production volume.

Process selection should therefore evaluate the complete manufacturing route rather than comparing individual machine-operation costs in isolation.

## 3. Manufacturing Process Selection Criteria

Important criteria include:

### Material compatibility

The process must be compatible with material melting behavior, hardness, ductility, chemical stability, thermal sensitivity, and reinforcement architecture.

### Geometry

Consider component size, wall thickness, internal features, undercuts, cavities, curvature, and accessibility.

### Dimensional accuracy

The process must be capable of achieving the required dimensional and geometric tolerances, with suitable inspection and finishing.

### Surface quality

Surface requirements may determine whether machining, polishing, coating, or other finishing operations are necessary.

### Production volume

Low-volume production may favor flexible processes and limited tooling. High-volume production may justify dedicated tooling and automation.

### Production rate

Required output must be achievable after considering cycle time, setup, downtime, yield, and capacity constraints.

### Risk and qualification

Safety-critical products may require validated processes, traceability, extensive inspection, and formal qualification.

## 4. Comparing Manufacturing Processes

| Process | Typical strengths | Typical limitations |
|---|---|---|
| Casting | Complex shapes and many metal geometries | Shrinkage, porosity, tooling, and finishing |
| Forming | High productivity for suitable ductile materials | Tooling cost and deformation limits |
| Machining | Precision and complex surface generation | Material removal, tool wear, and chip waste |
| Additive manufacturing | Geometric complexity and customization | Build rate, material cost, and qualification |
| Injection molding | High-volume polymer production | Mold investment and design constraints |
| Welding and joining | Component integration | Joint defects, thermal effects, and inspection |
| Composite processing | High specific stiffness and tailored properties | Anisotropy, process sensitivity, and repair complexity |

No process is universally superior. Selection depends on product requirements and the entire production system.

## 5. Manufacturing Cost Structure

Total manufacturing cost can be divided into several categories.

**Fixed costs** do not vary directly with output over the relevant planning range. Examples include certain tooling, setup, and equipment investments.

**Variable costs** change with production quantity. Examples include material consumption and some per-unit processing costs.

**Direct costs** can be assigned to a product or operation using the organization's accounting rules.

**Indirect costs** support production but may not be directly attributable to a single unit.

A simplified total cost model is:

\[
C_T=F+vN
\]

where:
- \(C_T\) = total cost, currency.
- \(F\) = fixed cost, currency.
- \(v\) = variable cost per unit, currency/unit.
- \(N\) = number of units produced, units.

Average cost per unit is:

\[
C_U=\frac{F}{N}+v
\]

This model assumes constant variable cost and fixed cost over the relevant production range.

## 6. Break-Even Analysis

For two processes:

\[
C_A=F_A+v_AN
\]

\[
C_B=F_B+v_BN
\]

At the break-even quantity:

\[
F_A+v_AN=F_B+v_BN
\]

Therefore:

\[
N^*=\frac{F_B-F_A}{v_A-v_B}
\]

provided the denominator is nonzero and the resulting quantity is relevant to the production decision.

### Numerical Example 1: Process selection

Process A:
- Fixed cost: \$40,000.
- Variable cost: \$8 per unit.

Process B:
- Fixed cost: \$10,000.
- Variable cost: \$14 per unit.

Set costs equal:

\[
40{,}000+8N=10{,}000+14N
\]

\[
30{,}000=6N
\]

\[
N=5000
\]

At 5,000 units, both processes cost:

\[
C=40{,}000+8(5000)=\$80{,}000
\]

**Answer:** The break-even quantity is 5,000 units. Process B is cheaper below this quantity, and Process A is cheaper above it under the stated cost model.

## 7. Material Utilization and Scrap

Material utilization is:

\[
\eta_m=\frac{m_{\text{accepted product}}}
{m_{\text{material input}}}\times100\%
\]

where the mass accounting boundary must be defined consistently.

Low utilization can increase material cost and waste-management requirements. However, high utilization alone does not guarantee low total cost because processing time, yield, finishing, and material price also matter.

### Numerical Example 2: Material utilization

A machining operation consumes 50 kg of allocated raw material and produces 18 kg of accepted components.

\[
\eta_m=\frac{18}{50}\times100\%=36\%
\]

**Answer:** Material utilization is 36%.

Chips may have recycling value, but their recovery value does not make the initial process equivalent to one with no material waste.

## 8. Cycle Time, Throughput, and Capacity

Cycle time is the time required to complete a defined production cycle.

For a simple sequential operation, a cycle may include loading, processing, unloading, and other required tasks.

An idealized production rate is:

\[
R=\frac{1}{t_c}
\]

where:
- \(R\) = units per unit time.
- \(t_c\) = cycle time per unit.

If cycle time is expressed in seconds:

\[
R_h=\frac{3600}{t_c}
\]

where \(R_h\) is idealized units per hour.

### Numerical Example 3: Machine production rate

A machine has a cycle time of 45 seconds per unit.

\[
R_h=\frac{3600}{45}=80\text{ units/hour}
\]

**Answer:** The idealized rate is 80 units per hour.

Actual output will be lower if the machine experiences downtime, rejects, changeovers, or material shortages.

## 9. Bottlenecks and Production Flow

A bottleneck is a resource or process step that limits the throughput of the overall production system.

For a simple serial line with stable operation, the maximum sustainable throughput is constrained by the slowest effective stage.

Suppose three operations have effective cycle times:
- Operation A: 20 seconds.
- Operation B: 35 seconds.
- Operation C: 25 seconds.

If each unit must pass through all three operations and sufficient buffers are available, Operation B is the bottleneck.

The theoretical steady-state output is constrained to:

\[
R_h=\frac{3600}{35}\approx102.9\text{ units/hour}
\]

This assumes that each operation's stated effective cycle time adequately represents its production behavior.

Improving a non-bottleneck operation may not increase total throughput. Improving the bottleneck often has the greatest immediate effect.

## 10. Little's Law and Work-in-Process

Little's Law relates average work-in-process, throughput, and average flow time:

\[
WIP=TH\times FT
\]

where:
- \(WIP\) = average work-in-process, units.
- \(TH\) = average throughput, units/time.
- \(FT\) = average flow time, time.

### Numerical Example 4: Work-in-process

A factory completes an average of 120 units per hour, and average production flow time is 2.5 hours.

\[
WIP=120(2.5)=300\text{ units}
\]

**Answer:** Average work-in-process is 300 units under the stated steady-state assumptions.

Increasing WIP does not automatically improve throughput. Excessive WIP can increase lead time, handling, storage, and the time required to detect process problems.

## 11. Overall Equipment Effectiveness

Overall Equipment Effectiveness (OEE) combines availability, performance, and quality:

\[
OEE=A\times P\times Q
\]

where:
- \(A\) = availability.
- \(P\) = performance.
- \(Q\) = quality rate.

The factors are expressed as fractions between 0 and 1.

Availability:

\[
A=\frac{\text{Operating time}}{\text{Planned production time}}
\]

Performance compares actual output rate with the defined ideal rate over the operating period.

Quality rate:

\[
Q=\frac{\text{Good units}}{\text{Total units produced}}
\]

### Numerical Example 5: OEE

Suppose:
- Availability = 0.90.
- Performance = 0.85.
- Quality rate = 0.98.

Then:

\[
OEE=0.90(0.85)(0.98)
\]

\[
OEE=0.7497
\]

\[
OEE\approx75.0\%
\]

**Answer:** OEE is approximately 75.0%.

The definition of planned production time, ideal cycle time, and quality rate must be consistent. OEE is a diagnostic metric, not a complete measure of profitability.

## 12. Labor Productivity and Automation

Labor productivity may be measured as output per labor hour:

\[
P_L=\frac{N_g}{H_L}
\]

where:
- \(P_L\) = labor productivity, good units per labor hour.
- \(N_g\) = good units produced.
- \(H_L\) = labor hours.

Automation can reduce repetitive labor and improve consistency, but it may increase capital investment, maintenance requirements, integration complexity, and the cost of failures.

A sound business case should consider:
- Labor savings.
- Capacity improvement.
- Scrap reduction.
- Downtime.
- Maintenance.
- Training.
- Safety.
- Changeover flexibility.
- System integration.
- Product-mix variability.

## 13. Net Present Value and Investment Decisions

When costs and benefits occur over multiple periods, time value of money matters.

A simplified net present value model is:

\[
NPV=-I_0+\sum_{t=1}^{n}\frac{CF_t}{(1+r)^t}
\]

where:
- \(NPV\) = net present value, currency.
- \(I_0\) = initial investment, currency.
- \(CF_t\) = net cash flow during period \(t\), currency.
- \(r\) = discount rate per period.
- \(n\) = number of periods.

A positive NPV indicates a positive discounted value under the chosen assumptions and cash-flow model.

### Numerical Example 6: Investment appraisal

A machine costs \$20,000 and generates an estimated net cash benefit of \$8,000 at the end of each of the next three years. Assume a discount rate of 10% per year.

\[
NPV=-20{,}000+
\frac{8000}{1.10}+
\frac{8000}{1.10^2}+
\frac{8000}{1.10^3}
\]

\[
NPV\approx-20{,}000+7272.73+6611.57+6010.52
\]

\[
NPV\approx-\$105.18
\]

**Answer:** NPV is approximately -\$105 under the stated assumptions.

The investment is close to break-even in discounted terms. Real analysis should include residual value, taxes, maintenance, risk, and any additional operating costs.

## 14. Process Selection Decision Matrix

A weighted decision matrix compares alternatives against selected criteria.

A general score is:

\[
S_j=\sum_{i=1}^{m}w_i r_{ij}
\]

where:
- \(S_j\) = total score for alternative \(j\).
- \(w_i\) = weight assigned to criterion \(i\).
- \(r_{ij}\) = rating of alternative \(j\) against criterion \(i\).
- \(m\) = number of criteria.

Weights should sum to 1 if interpreted as normalized fractions.

The ratings are often subjective or ordinal. A score supports discussion but does not replace engineering validation.

## 15. Sustainability and Lifecycle Cost

Sustainable manufacturing considers:
- Material consumption.
- Energy use.
- Water use.
- Emissions.
- Scrap and recycling.
- Product lifetime.
- Repairability.
- Transportation.
- End-of-life recovery.

Lifecycle cost may include acquisition, operation, maintenance, downtime, energy, disposal, and other relevant costs over the product's life.

A process with a higher purchase price may be preferable if it reduces energy consumption, defects, downtime, or maintenance sufficiently.

## 16. Industrial R&D and Optimization

Industrial R&D can improve process selection through:
- Time studies.
- Cost modeling.
- Design of experiments.
- Discrete-event simulation.
- Bottleneck analysis.
- Predictive maintenance.
- Statistical process control.
- Energy monitoring.
- Digital twins.
- Multi-objective optimization.

Optimization must respect constraints such as safety, quality, capacity, delivery commitments, and capital availability.

## 17. Common Misconceptions

- The process with the lowest variable cost is always cheapest.
- Maximum machine speed guarantees maximum production output.
- More automation always improves profitability.
- High OEE guarantees a profitable factory.
- The bottleneck is always the machine with the longest nominal cycle.
- Material utilization alone determines sustainability.
- Break-even analysis captures every financial risk.
- A weighted decision matrix proves the best technical solution.

## 18. Summary

Manufacturing process selection integrates technical feasibility, cost, capacity, quality, and lifecycle considerations. Fixed and variable costs determine break-even quantities, while cycle time and bottlenecks constrain production throughput. OEE, productivity, WIP, and investment appraisal provide complementary views of factory performance. The best decision balances economic results with quality, flexibility, reliability, and long-term operational risk.

## 19. Review Questions

1. Compare fixed and variable manufacturing costs.
2. Calculate the break-even quantity for two competing processes.
3. Why might a high-investment process be cheaper at high volume?
4. Explain the relationship between bottlenecks and throughput.
5. State Little's Law and describe its assumptions.
6. Calculate OEE from availability, performance, and quality.
7. Why is OEE not a complete measure of profitability?
8. Explain how NPV supports equipment investment decisions.
9. How can material utilization conflict with total-cost optimization?
10. Develop a decision matrix for selecting between machining and additive manufacturing.

## 20. Challenging Exercises with Complete Solutions

### Exercise 1: Break-even quantity

Process A costs \$15,000 in fixed costs and \$12 per unit. Process B costs \$5,000 in fixed costs and \$17 per unit. Calculate the break-even quantity.

**Solution**

\[
C_A=15{,}000+12N
\]

\[
C_B=5{,}000+17N
\]

\[
15{,}000+12N=5{,}000+17N
\]

\[
10{,}000=5N
\]

\[
N=2000
\]

**Answer:** Break-even quantity is 2,000 units.

### Exercise 2: Throughput and bottleneck

A production line has three serial stages with effective cycle times of 18, 30, and 24 seconds. Estimate ideal steady-state throughput in units per hour.

**Solution**

The bottleneck cycle time is 30 seconds.

\[
R_h=\frac{3600}{30}=120\text{ units/hour}
\]

**Answer:** The idealized throughput is 120 units per hour.

### Exercise 3: OEE

A machine has 450 minutes of operating time out of 500 planned minutes. Its performance rate is 92%, and 980 of 1,000 produced units are accepted.

**Solution**

Availability:

\[
A=\frac{450}{500}=0.90
\]

Performance:

\[
P=0.92
\]

Quality:

\[
Q=\frac{980}{1000}=0.98
\]

Therefore:

\[
OEE=0.90(0.92)(0.98)=0.81144
\]

\[
OEE\approx81.1\%
\]

**Answer:** OEE is approximately 81.1%.

### Exercise 4: Little's Law

A factory has an average WIP of 480 units and average throughput of 160 units per hour. Calculate average flow time.

**Solution**

\[
WIP=TH\times FT
\]

Rearrange:

\[
FT=\frac{WIP}{TH}
\]

\[
FT=\frac{480}{160}=3\text{ hours}
\]

**Answer:** Average flow time is 3 hours.

### Exercise 5: Manufacturing investment

An automation system costs \$50,000. It produces net cash benefits of \$20,000 per year for three years. Use a 10% annual discount rate and ignore residual value. Calculate NPV.

**Solution**

\[
NPV=-50{,}000+
\frac{20{,}000}{1.10}+
\frac{20{,}000}{1.10^2}+
\frac{20{,}000}{1.10^3}
\]

\[
NPV\approx-50{,}000+18{,}181.82+16{,}528.93+15{,}026.30
\]

\[
NPV\approx-\$262.95
\]

**Answer:** NPV is approximately -\$263 under the stated assumptions. The project is close to financial break-even but slightly negative at the selected discount rate.

## 21. Glossary

- **Bottleneck:** Resource limiting the throughput of a production system.
- **Break-even quantity:** Output quantity at which competing cost models are equal.
- **Cycle time:** Time associated with completing a defined production cycle.
- **Fixed cost:** Cost that remains approximately constant within a specified operating range.
- **Lifecycle cost:** Total relevant cost over a defined asset or product life.
- **Little's Law:** Relationship between average WIP, throughput, and flow time.
- **NPV:** Net present value of discounted cash flows.
- **OEE:** Overall Equipment Effectiveness.
- **Throughput:** Rate at which good output passes through a system.
- **Variable cost:** Cost that changes with output under a defined cost model.
- **WIP:** Work-in-process inventory.

## 22. References and Further Learning

1. [NIST](https://www.nist.gov/) — manufacturing productivity and advanced manufacturing research.
2. [NIST Engineering Statistics Handbook](https://www.itl.nist.gov/div898/handbook/) — statistical analysis.
3. [SME](https://www.sme.org/) — manufacturing engineering and production systems.
4. [ASQ](https://asq.org/) — quality and continuous improvement.
5. [MIT OpenCourseWare](https://ocw.mit.edu/) — operations research, engineering economics, and manufacturing-related study.
6. Groover, M. P. *Fundamentals of Modern Manufacturing: Materials, Processes, and Systems*.
7. Hopp, W. J., and Spearman, M. L. *Factory Physics*.

This is a custom instructional module, not an official MIT syllabus. Use organization-specific accounting rules and validated operating data for real investment and process-selection decisions.