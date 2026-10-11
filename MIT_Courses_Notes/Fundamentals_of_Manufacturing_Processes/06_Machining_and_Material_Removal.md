
# Module 06: Machining and Material Removal

## 1. Learning Objectives

By completing this module, you should be able to:

- Explain the mechanics of chip formation and material removal.
- Compare turning, milling, drilling, grinding, and nontraditional machining.
- Calculate cutting speed, spindle speed, feed rate, machining time, and material removal rate.
- Understand cutting forces, power, temperature, tool wear, and surface integrity.
- Explain tool materials, coatings, cutting fluids, and lubrication.
- Identify common machining defects and their causes.
- Evaluate the relationships among productivity, tolerance, surface finish, and cost.
- Apply Design for Manufacturability principles to machined components.
- Connect machining research to sensors, statistical process control, simulation, and optimization.

## 2. Introduction

Machining removes material from a workpiece to obtain the required geometry, dimensions, and surface characteristics.

Machining is used in aerospace components, automotive shafts, medical implants, molds, dies, electronics enclosures, precision instruments, and industrial equipment.

Unlike casting or forming, machining creates chips or other removed material. This can reduce material utilization, but machining is valuable when tight tolerances, complex surfaces, or high-quality functional interfaces are required.

Machining processes include:
- Turning.
- Milling.
- Drilling.
- Boring.
- Reaming.
- Grinding.
- Broaching.
- Sawing.
- Electrical discharge machining.
- Laser and abrasive machining.

The best process depends on workpiece material, geometry, required accuracy, surface finish, production quantity, machine capability, and total cost.

## 3. Fundamentals of Chip Formation

In conventional cutting, a cutting tool penetrates the workpiece and causes intense deformation in a region near the cutting edge.

Material separates from the workpiece and forms a chip. The process involves plastic deformation, friction, heat generation, and sometimes fracture or segmentation.

### 3.1 Primary deformation zone

The primary deformation zone is the region in which much of the material undergoes shear deformation as it becomes a chip.

### 3.2 Secondary deformation zone

The secondary zone is associated with deformation and friction at the chip-tool interface.

### 3.3 Tertiary deformation zone

The tertiary zone is associated with interaction between the tool flank and the newly generated workpiece surface.

These zones influence cutting force, temperature, tool wear, surface integrity, and energy consumption.

### 3.4 Chip types

| Chip type | Typical behavior | Engineering implications |
|---|---|---|
| Continuous | Chip remains relatively continuous | Common in ductile materials under suitable conditions; chip control may be necessary |
| Discontinuous | Chip separates into individual segments | May occur with brittle materials or unfavorable cutting conditions |
| Segmented | Repeating localized shear bands form segments | Can occur in difficult-to-cut materials and at elevated cutting speeds |
| Built-up edge | Workpiece material adheres to the cutting edge | May alter dimensions and surface finish |

Chip morphology depends on material, cutting speed, feed, depth of cut, tool geometry, friction, and temperature.

## 4. Machining Operations

### 4.1 Turning

Turning typically rotates the workpiece while a cutting tool advances relative to it.

Applications include shafts, cylindrical surfaces, grooves, threads, and facing operations.

Important variables include:
- Workpiece rotational speed.
- Cutting speed.
- Feed per revolution.
- Depth of cut.
- Tool geometry.
- Workholding stiffness.

### 4.2 Milling

Milling typically uses a rotating tool with multiple cutting edges.

Common types include:
- Face milling.
- Peripheral milling.
- End milling.
- Slot milling.
- Profile milling.

Because individual teeth enter and leave the cut, cutting forces and heat generation can vary over the tooth engagement cycle.

### 4.3 Drilling

Drilling produces holes using a rotating cutting tool or another hole-making method.

Hole quality depends on tool geometry, material, feed, speed, chip evacuation, coolant delivery, and machine alignment.

Deep-hole drilling may require specialized tooling and high-pressure coolant.

### 4.4 Grinding

Grinding uses abrasive grains to remove small amounts of material. It is widely used for precision finishing and for materials that are difficult to machine using conventional cutting tools.

Grinding can produce high accuracy and fine surface finishes, but excessive heat may cause burns, residual stresses, microcracking, or metallurgical damage.

### 4.5 Nontraditional machining

Nontraditional processes remove material using mechanisms other than conventional sharp-edge chip formation, or combine several mechanisms.

Examples:
- Electrical discharge machining (EDM).
- Electrochemical machining (ECM).
- Laser beam machining.
- Waterjet machining.
- Abrasive waterjet machining.
- Ultrasonic machining.

These processes can be useful for hard materials, delicate geometries, complex cavities, or features difficult to create conventionally. Their limitations differ: EDM requires electrically conductive workpieces, ECM involves electrochemical considerations, and laser processes can create thermal effects.

## 5. Cutting Speed and Spindle Speed

For a rotating workpiece or tool:

\[
V_c=\frac{\pi DN}{1000}
\]

when \(D\) is in millimeters, \(N\) is in revolutions per minute, and \(V_c\) is in meters per minute.

Rearranging:

\[
N=\frac{1000V_c}{\pi D}
\]

where:
- \(V_c\) = cutting speed, m/min.
- \(D\) = relevant diameter, mm.
- \(N\) = rotational speed, rev/min.

For turning, the diameter is generally the workpiece diameter at the cutting location. For milling, the relevant diameter is the cutter diameter.

### Numerical Example 1: Spindle speed

A turning operation uses a workpiece diameter of 50 mm and a cutting speed of 150 m/min.

Known:

\[
D=50\text{ mm},\qquad V_c=150\text{ m/min}
\]

Calculate:

\[
N=\frac{1000(150)}{\pi(50)}
\]

\[
N\approx955\text{ rev/min}
\]

**Answer:** The theoretical spindle speed is approximately 955 rpm.

The actual setting must respect machine limits, workholding stability, tool recommendations, and the workpiece's geometry.

## 6. Feed Rate and Machining Time

In turning:

\[
v_f=fN
\]

where:
- \(v_f\) = axial feed rate, mm/min.
- \(f\) = feed per revolution, mm/rev.
- \(N\) = rotational speed, rev/min.

For a simple constant-diameter turning pass:

\[
t_m=\frac{L}{fN}
\]

where:
- \(t_m\) = cutting time, min.
- \(L\) = tool travel distance, mm.

The actual travel distance may exceed the finished component length because of approach, overtravel, and tool-path requirements.

### Numerical Example 2: Turning time

A tool must travel 120 mm. Feed is 0.25 mm/rev, and spindle speed is 800 rpm.

Feed rate:

\[
v_f=0.25(800)=200\text{ mm/min}
\]

Machining time:

\[
t_m=\frac{120}{200}=0.60\text{ min}
\]

\[
t_m=36\text{ s}
\]

**Answer:** Idealized cutting time is 36 seconds.

Tool changes, loading, inspection, approach, and other non-cutting operations increase total cycle time.

## 7. Material Removal Rate

For turning, a commonly used approximation is:

\[
Q\approx V_cf a_p
\]

where:
- \(Q\) = material removal rate, mm³/min.
- \(V_c\) = cutting speed, mm/min.
- \(f\) = feed, mm/rev.
- \(a_p\) = depth of cut, mm.

This expression assumes conventional turning geometry and uses consistent units. Cutting speed must be converted from m/min to mm/min.

### Numerical Example 3: Turning material removal rate

Given:
- Cutting speed \(V_c=120\text{ m/min}=120{,}000\text{ mm/min}\).
- Feed \(f=0.20\text{ mm/rev}\).
- Depth of cut \(a_p=1.5\text{ mm}\).

Then:

\[
Q\approx120{,}000(0.20)(1.5)
\]

\[
Q\approx36{,}000\text{ mm}^3/\text{min}
\]

Converting to cm³/min:

\[
Q=36\text{ cm}^3/\text{min}
\]

**Interpretation:** Approximately 36 cm³ of material is removed per minute under the assumed cutting conditions.

This is a geometric estimate. Tool engagement, interruptions, actual chip thickness, and machine limitations can affect the effective rate.

## 8. Milling Mechanics

For milling, the tooth feed is commonly expressed as:

\[
f_z=\frac{v_f}{Nz}
\]

where:
- \(f_z\) = feed per tooth, mm/tooth.
- \(v_f\) = table feed, mm/min.
- \(N\) = spindle speed, rev/min.
- \(z\) = number of effective cutting teeth.

Therefore:

\[
v_f=f_zNz
\]

The nominal material removal rate for a rectangular engagement can be approximated as:

\[
Q=a_pa_ev_f
\]

where:
- \(a_p\) = axial depth of cut, mm.
- \(a_e\) = radial width of cut, mm.
- \(v_f\) = table feed, mm/min.

### Numerical Example 4: Milling feed and removal rate

A cutter has four effective teeth. Spindle speed is 1,500 rpm and feed per tooth is 0.08 mm/tooth.

Table feed:

\[
v_f=0.08(1500)(4)=480\text{ mm/min}
\]

If axial depth is 3 mm and radial width is 10 mm:

\[
Q=3(10)(480)
\]

\[
Q=14{,}400\text{ mm}^3/\text{min}
=14.4\text{ cm}^3/\text{min}
\]

**Answer:** Table feed is 480 mm/min and the approximate removal rate is 14.4 cm³/min.

The calculation assumes a rectangular material engagement and does not capture every cutter-engagement or chip-thickness effect.

## 9. Cutting Forces, Power, and Energy

Cutting forces arise from plastic deformation, friction, and tool-workpiece interaction.

A useful first-order power estimate is:

\[
P_c=F_cV_c
\]

where:
- \(P_c\) = cutting power, W.
- \(F_c\) = main cutting force, N.
- \(V_c\) = cutting speed, m/s.

For this equation, cutting speed must be in meters per second.

If cutting speed is in m/min, convert it by dividing by 60.

Machine input power must exceed cutting power because motors, drives, and other systems have losses.

### Numerical Example 5: Cutting power

A cutting force is 1,000 N and cutting speed is 2 m/s.

\[
P_c=1000(2)=2000\text{ W}
\]

\[
P_c=2.0\text{ kW}
\]

If overall efficiency from machine input to cutting power is assumed to be 80%:

\[
P_{\text{input}}=\frac{2.0}{0.80}=2.5\text{ kW}
\]

**Answer:** Cutting power is 2.0 kW and estimated input power is 2.5 kW under the stated efficiency assumption.

## 10. Cutting Tool Materials and Coatings

| Tool material | Typical advantages | Important limitations |
|---|---|---|
| High-speed steel | Toughness and complex tool geometry | Lower hot hardness than many advanced tool materials |
| Cemented carbide | High hardness and productivity | Can be vulnerable to chipping under unsuitable conditions |
| Ceramic | High hot hardness and potential for high-speed cutting | Brittle behavior and limited suitability for interrupted cuts in some applications |
| Cubic boron nitride | Useful for selected hardened ferrous materials | High cost and application-specific limits |
| Polycrystalline diamond | Excellent wear resistance for suitable nonferrous and abrasive materials | Diamond reacts unfavorably with iron-based materials under many cutting conditions |
| Coated carbide | Improved wear resistance and thermal or chemical behavior for suitable applications | Performance depends on coating, substrate, material, and cutting conditions |

Coatings may improve abrasion resistance, reduce adhesion, alter friction, and protect the substrate at elevated temperature.

No tool material is optimal for every workpiece, cutting speed, and operation.

## 11. Tool Wear and Tool Life

Common wear mechanisms include:
- Flank wear.
- Crater wear.
- Notch wear.
- Chipping.
- Plastic deformation of the cutting edge.
- Thermal cracking.
- Adhesive wear.

A common empirical tool-life model is Taylor's equation:

\[
V_cT^n=C
\]

where:
- \(V_c\) = cutting speed.
- \(T\) = tool life, commonly in minutes.
- \(n\) = empirical exponent for the tested conditions.
- \(C\) = empirical constant with units consistent with the selected variables.

This model is empirical and should be calibrated for the specific tool-workpiece system and operating range.

If cutting speed increases, tool life often decreases significantly, but the exact relationship depends on the materials, coatings, feed, depth of cut, coolant, and failure criterion.

## 12. Surface Finish and Dimensional Accuracy

Surface finish describes surface texture, while dimensional accuracy describes how closely the produced geometry matches the specified dimensions.

Common roughness parameters include:
- \(R_a\): arithmetic mean of absolute profile deviations from the mean line.
- \(R_z\): a peak-to-valley-related roughness measure whose precise definition depends on the applicable standard.

For an idealized turning operation, geometric roughness can be related to feed and tool-nose radius. One common approximation is:

\[
R_a\approx\frac{f^2}{32r_\epsilon}
\]

where:
- \(R_a\) = estimated arithmetic roughness, mm.
- \(f\) = feed per revolution, mm/rev.
- \(r_\epsilon\) = tool-nose radius, mm.

This is a simplified geometric estimate. Real roughness also depends on built-up edge, tool wear, vibration, material behavior, and machine condition.

## 13. Common Machining Defects

| Problem | Potential causes | Possible corrective action |
|---|---|---|
| Chatter | Dynamic instability, weak setup, tool overhang | Improve rigidity and revise speed or tool engagement |
| Poor surface finish | Excessive feed, wear, vibration, built-up edge | Optimize feed and tool condition |
| Burrs | Plastic deformation during cutting or exit | Adjust tool path and use deburring or specialized geometry |
| Dimensional drift | Thermal expansion, wear, workholding movement | Improve compensation and inspection |
| Tool breakage | Excessive load, impact, poor chip evacuation | Review engagement, tool selection, and operating conditions |
| Thermal damage | Excessive heat or inadequate cooling | Optimize parameters and coolant delivery |
| Chip entanglement | Inadequate chip control | Use suitable chip-breaker geometry and cycle strategy |
| Hole-position error | Runout, deflection, alignment, or workholding error | Improve fixturing and hole-making strategy |

## 14. Coolants and Lubrication

Cutting fluids may provide cooling, lubrication, chip evacuation, and corrosion protection.

Common approaches include:
- Flood coolant.
- Minimum quantity lubrication.
- High-pressure coolant.
- Dry machining.
- Through-tool coolant.

The correct strategy depends on tool material, workpiece, operation, chip behavior, environmental requirements, and equipment capability.

Coolant selection should account for worker exposure, mist control, maintenance, contamination, disposal, and compatibility with the machine and workpiece.

## 15. Process Planning and Cost

A machining operation's cost includes more than cutting time.

Relevant factors:
- Material cost.
- Machine operating cost.
- Labor and handling.
- Tool consumption.
- Setup and programming.
- Inspection.
- Scrap and rework.
- Coolant and maintenance.
- Energy.
- Workholding and fixturing.

For production planning, distinguish cutting time from cycle time and total lead time.

A high removal rate may reduce cutting time but increase tool consumption or compromise quality. The optimal condition minimizes total cost while satisfying technical constraints.

## 16. Design for Manufacturability

- Avoid unnecessarily deep, narrow cavities.
- Reduce the number of setups when feasible.
- Standardize hole sizes and tool features.
- Provide adequate tool access.
- Minimize unnecessary tight tolerances.
- Use realistic internal corner radii.
- Consider workholding surfaces and datum selection.
- Design features so they can be inspected.
- Consider whether near-net-shape manufacturing can reduce stock removal.
- Specify surface finish according to functional requirements.

## 17. Industrial R&D and Automation

Modern machining research can involve:
- Force and vibration sensors.
- Acoustic emission.
- Spindle power monitoring.
- Tool-wear imaging.
- Digital twins.
- Computer-aided process planning.
- Adaptive feed control.
- Tool-life prediction.
- Energy optimization.
- Statistical process control.

A practical R&D project should relate sensor signals to independently verified outcomes such as tool wear, roughness, dimensional deviation, or failure.

Machine-learning systems should be evaluated across different tools, batches, and operating conditions to avoid overestimating performance from narrowly collected data.

## 18. Common Misconceptions

- Maximum cutting speed always produces the lowest manufacturing cost.
- Surface roughness and dimensional accuracy are the same property.
- Coolant always improves tool life.
- A tool coating guarantees superior performance in every operation.
- High material removal rate always means high productivity.
- All vibration is caused by an unbalanced rotating component.
- A machine's nominal power rating guarantees sufficient power under every cutting condition.
- Machining removes only material and has no effect on the remaining surface's properties.

## 19. Summary

Machining produces specified geometry by removing material through controlled mechanical, thermal, or electrochemical mechanisms. Cutting speed, feed, depth of cut, tool geometry, and material properties influence productivity, power, tool wear, and surface quality. Engineering calculations estimate spindle speed, cycle time, material removal rate, and power, but real processes require validation. Effective machining combines suitable tooling, stable fixturing, process monitoring, and design choices that balance accuracy, cost, and throughput.

## 20. Review Questions

1. Explain the primary, secondary, and tertiary deformation zones.
2. Calculate spindle speed from cutting speed and diameter.
3. Distinguish feed per revolution from feed per tooth.
4. Why can increasing cutting speed reduce tool life?
5. Compare carbide, ceramic, CBN, and diamond cutting tools.
6. What is chatter, and how can it be mitigated?
7. Distinguish surface roughness from dimensional accuracy.
8. How does chip evacuation influence drilling?
9. Why is material removal rate insufficient as a productivity metric?
10. Design an experiment to optimize milling conditions for surface finish and tool life.

## 21. Challenging Exercises with Complete Solutions

### Exercise 1: Spindle speed and turning time

A shaft has a diameter of 40 mm. The target cutting speed is 100 m/min. The tool travel length is 150 mm, and feed is 0.20 mm/rev. Estimate spindle speed and ideal cutting time.

**Solution**

\[
N=\frac{1000V_c}{\pi D}
\]

\[
N=\frac{1000(100)}{\pi(40)}
\approx796\text{ rpm}
\]

Feed rate:

\[
v_f=fN=0.20(796)=159.2\text{ mm/min}
\]

Cutting time:

\[
t_m=\frac{150}{159.2}\approx0.942\text{ min}
\]

\[
t_m\approx56.5\text{ s}
\]

**Answer:** Approximately 796 rpm and 56.5 seconds, excluding approach and non-cutting time.

### Exercise 2: Milling material removal rate

A milling operation uses an axial depth of 4 mm, radial engagement of 12 mm, and table feed of 600 mm/min. Calculate the approximate material removal rate.

**Solution**

\[
Q=a_pa_ev_f
\]

\[
Q=4(12)(600)=28{,}800\text{ mm}^3/\text{min}
\]

\[
Q=28.8\text{ cm}^3/\text{min}
\]

**Answer:** Approximately 28.8 cm³/min.

### Exercise 3: Cutting power

A turning operation has a main cutting force of 800 N and cutting speed of 180 m/min. Estimate cutting power. Assume machine efficiency is 75%.

**Solution**

Convert speed:

\[
V_c=\frac{180}{60}=3\text{ m/s}
\]

Cutting power:

\[
P_c=800(3)=2400\text{ W}=2.4\text{ kW}
\]

Estimated input power:

\[
P_{\text{input}}=\frac{2.4}{0.75}=3.2\text{ kW}
\]

**Answer:** Cutting power is 2.4 kW and estimated input power is 3.2 kW.

### Exercise 4: Taylor tool life

For an illustrative tool-workpiece system, assume:

\[
V_cT^{0.25}=300
\]

where speed is in m/min and tool life is in minutes. Estimate tool life at 150 m/min.

**Solution**

\[
T^{0.25}=\frac{300}{150}=2
\]

Raise both sides to the fourth power:

\[
T=2^4=16\text{ min}
\]

**Answer:** The model predicts 16 minutes of tool life.

The constants are hypothetical and should not be used for a real tool without experimental calibration.

### Exercise 5: Comparing production times

Process A removes a component's required material in 5 minutes and needs 2 minutes of setup allocation per part. Process B takes 4 minutes of machining and 4 minutes of setup allocation per part. Compare total allocated time for 100 parts.

**Solution**

Process A:

\[
t_A=100(5+2)=700\text{ min}
\]

Process B:

\[
t_B=100(4+4)=800\text{ min}
\]

Difference:

\[
800-700=100\text{ min}
\]

**Answer:** Process A requires 700 minutes, while Process B requires 800 minutes under the stated per-part allocation.

If setup time is actually a one-time batch cost rather than a per-part allocation, the calculation must be changed accordingly.

## 22. Glossary

- **Burr:** Unwanted material projecting from an edge after machining.
- **Chatter:** Self-excited or forced vibration affecting the cutting process.
- **Chip:** Material removed from the workpiece during cutting.
- **Cutting speed:** Relative surface speed at the cutting interface.
- **Feed:** Tool or workpiece advance relative to the cutting operation.
- **Material removal rate:** Volume of material removed per unit time.
- **Roughness:** Surface-texture characteristic quantified by defined profile parameters.
- **Spindle speed:** Rotational speed of the machine spindle.
- **Tool life:** Operating duration until a defined tool-failure or wear criterion is reached.
- **Turning:** Machining operation commonly using a rotating workpiece.
- **Milling:** Machining operation using a rotating multi-edge cutting tool.
- **EDM:** Electrical discharge machining.
- **ECM:** Electrochemical machining.
- **Workholding:** Methods used to secure a workpiece during manufacturing.

## 23. References and Further Learning

1. [MIT OpenCourseWare](https://ocw.mit.edu/) — engineering mechanics and manufacturing-related resources.
2. [NIST Manufacturing](https://www.nist.gov/manufacturing) — manufacturing measurement and process research.
3. [Society of Manufacturing Engineers](https://www.sme.org/) — machining technology and manufacturing education.
4. Groover, M. P. *Fundamentals of Modern Manufacturing: Materials, Processes, and Systems*.
5. Kalpakjian, S., and Schmid, S. R. *Manufacturing Engineering and Technology*.
6. Shaw, M. C. *Metal Cutting Principles*.
7. [Sandvik Coromant](https://www.sandvik.coromant.com/) — cutting-tool technology and machining guidance.
8. [ISO Standards](https://www.iso.org/standards.html) — dimensional inspection, tooling, and manufacturing-related standards.

This is a custom instructional module, not an official MIT course syllabus.