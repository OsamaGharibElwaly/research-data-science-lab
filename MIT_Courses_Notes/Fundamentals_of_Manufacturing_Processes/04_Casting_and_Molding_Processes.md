
# Module 04: Casting and Molding Processes

## 1. Learning Objectives

After completing this module, you should be able to:

- Explain the physical principles of casting and molding.
- Distinguish permanent-mold, expendable-mold, and pressure-assisted processes.
- Describe mold design, gating, risers, cores, solidification, and feeding.
- Apply heat-transfer and solidification-time equations.
- Explain shrinkage, porosity, inclusions, hot tearing, and other common defects.
- Compare sand casting, investment casting, die casting, injection molding, and compression molding.
- Estimate casting solidification time using Chvorinov's rule.
- Relate process parameters to dimensional accuracy, material properties, productivity, and cost.
- Apply DFM principles to cast and molded components.
- Develop experimental plans for industrial process optimization.

## 2. Introduction and Industrial Importance

Casting and molding produce components by introducing a material into a cavity whose geometry represents the desired component or a near-net shape. The material subsequently solidifies, cools, cures, or otherwise develops sufficient integrity to be removed and used.

**Casting** most commonly refers to liquid metals or alloys solidifying in a mold. The term is also used for some polymer, ceramic, and other material processes.

**Molding** is a broader term commonly used for shaping polymers, elastomers, ceramics, and other materials in a mold. The mechanism may involve melting and cooling, chemical curing, compaction, or combinations of these.

These processes can produce complex geometries that would be difficult or expensive to machine from solid stock.

Typical applications include:
- Automotive engine blocks, housings, and transmission components.
- Aerospace turbine components and structural parts.
- Electronic enclosures, connectors, and polymer housings.
- Medical-device components and disposable polymer products.
- Pumps, valves, industrial machinery, and household products.

The appropriate process depends on material, geometry, tolerances, required properties, production volume, tooling budget, and quality requirements.

## 3. Classification of Casting Processes

### 3.1 Sand casting

Sand casting uses a mold cavity formed in prepared sand. The mold is commonly broken to remove the solidified component.

Typical characteristics:
- Relatively economical tooling.
- Broad material compatibility.
- Ability to produce large components.
- Flexible geometry.
- Surface finish and dimensional accuracy often inferior to precision casting processes.
- Potential for mold-related inclusions, gas defects, and dimensional variability.

Sand casting is widely used for iron castings, steel castings, and many nonferrous alloys.

### 3.2 Permanent-mold casting

A reusable mold, often metallic, is used repeatedly. The mold's thermal properties influence solidification, cycle time, surface finish, and microstructure.

Advantages include repeatability and potentially improved surface finish compared with conventional sand casting.

Limitations include higher tooling investment, restrictions on geometry and undercuts, and limitations on alloy/process combinations.

### 3.3 Die casting

In die casting, molten metal is forced into a metallic die under pressure. It is especially important for high-volume production of suitable nonferrous alloys.

Two major variants are:

- **Hot-chamber die casting:** the injection mechanism is immersed in or closely coupled to the molten metal supply. It is used for compatible lower-melting alloys.
- **Cold-chamber die casting:** molten metal is transferred into an injection chamber before being forced into the die. It is common for aluminum alloys and other suitable alloys.

Advantages:
- High production rates.
- Good repeatability.
- Potentially thin walls and complex features.
- Reduced machining for suitable designs.

Limitations:
- High tooling and machine investment.
- Entrapped gas and porosity risks.
- Die wear and thermal fatigue.
- Restrictions on component size, geometry, and alloy compatibility.

### 3.4 Investment casting

A disposable pattern, often wax or another suitable material, is surrounded by refractory material. The pattern is removed and the resulting mold is filled with molten material.

Investment casting can produce intricate geometry and relatively fine details with reduced machining.

Applications include turbine components, precision industrial parts, and selected medical or aerospace components.

The process can involve substantial pattern, shell, thermal-processing, and inspection costs.

### 3.5 Centrifugal casting

Rotation produces centrifugal forces that influence how liquid material distributes within a rotating mold.

It is useful for certain cylindrical components, such as pipes, sleeves, and rings. Depending on the process, density differences can influence the distribution of inclusions and phases.

Centrifugal casting does not eliminate every type of porosity or segregation, and its benefits depend on geometry and process control.

## 4. Classification of Molding Processes

### 4.1 Injection molding

Injection molding is widely used for thermoplastics and can also be adapted to other material systems.

A typical thermoplastic injection-molding cycle is:

1. Polymer pellets enter a heated barrel.
2. A rotating screw conveys and melts the polymer.
3. The screw accumulates a controlled shot of melt.
4. The melt is injected into a closed mold.
5. Packing and holding pressure compensate for shrinkage while the material solidifies.
6. Cooling continues until ejection is safe.
7. The mold opens and the part is ejected.
8. The mold closes for the next cycle.

Cycle time depends on filling, packing, cooling, mold movement, and ejection. Cooling is often a major contributor.

### 4.2 Compression molding

A measured quantity of material is placed into a heated mold, which closes to apply pressure. The material flows and takes the cavity shape before cooling or curing.

Compression molding is used for selected thermosets, rubber compounds, and fiber-reinforced materials.

It can be suitable for relatively large parts and certain reinforced formulations, although cycle time, flash, material distribution, and tooling requirements need control.

### 4.3 Blow molding

Blow molding forms hollow products by expanding a heated polymer preform or parison against a mold wall.

Applications include bottles, containers, and selected hollow industrial components.

Wall-thickness distribution, parison design, material temperature, and blowing conditions affect quality.

### 4.4 Rotational molding

A mold containing a measured polymer charge rotates around one or more axes while heated. Material progressively coats the internal mold surface.

It is useful for some large hollow parts and low-to-medium-volume applications. Cycle times can be relatively long compared with high-volume injection molding.

### 4.5 Thermoforming

A thermoplastic sheet is heated until sufficiently deformable and then shaped using vacuum, pressure, or mechanical assistance.

It is commonly used for packaging, trays, panels, and certain medical products.

Sheet thickness distribution, heating uniformity, draw ratio, and mold geometry affect the finished part.

## 5. The Physics of Solidification

Metal casting involves coupled heat transfer, phase change, fluid flow, and volume changes.

When molten metal enters a cooler mold, heat transfers from the liquid into the mold and surrounding environment. The liquid cools to its liquidus temperature, may release latent heat as solidification progresses, and then cools further as a solid.

### 5.1 Sensible heat and latent heat

Sensible heat changes temperature without changing phase.

For a material of mass \(m\), specific heat capacity \(c_p\), and temperature change \(\Delta T\):

\[
Q_s=mc_p\Delta T
\]

where:
- \(Q_s\) = sensible heat, J.
- \(m\) = mass, kg.
- \(c_p\) = specific heat capacity, J/(kg·K).
- \(\Delta T\) = temperature change, K.

During a phase change:

\[
Q_L=mL_f
\]

where:
- \(Q_L\) = latent heat, J.
- \(L_f\) = latent heat of fusion, J/kg.

For an alloy solidifying over a temperature range, the actual thermal history is more complex than an instantaneous phase change at one temperature.

### Numerical Example 1: Approximate casting heat removal

Assume 10 kg of metal cools from 700°C to 500°C. Use an illustrative average specific heat capacity of 600 J/(kg·K), and assume latent heat released during solidification is 250 kJ/kg.

For sensible heat:

\[
Q_s=10(600)(700-500)
\]

\[
Q_s=1{,}200{,}000\text{ J}=1.2\text{ MJ}
\]

For latent heat:

\[
Q_L=10(250{,}000)=2.5\text{ MJ}
\]

Approximate total:

\[
Q_{\text{total}}=1.2+2.5=3.7\text{ MJ}
\]

**Interpretation:** Approximately 3.7 MJ must be removed under the stated simplified model.

The estimate assumes the temperature range includes the relevant solidification event. Actual calculations should use the alloy's liquidus and solidus temperatures, temperature-dependent properties, and appropriate enthalpy data.

## 6. Chvorinov's Rule

Chvorinov's rule estimates the solidification time of a casting:

\[
t_s=B\left(\frac{V}{A}\right)^n
\]

where:
- \(t_s\) = solidification time, s.
- \(B\) = mold constant, with units that make the equation dimensionally consistent.
- \(V\) = casting volume, m³ or another consistent volume unit.
- \(A\) = casting surface area transferring heat to the mold, m² or a consistent area unit.
- \(n\) = empirical exponent, often approximated as 2 in introductory calculations.

The ratio \(V/A\) is called the casting's modulus when used in this context.

The mold constant depends on the metal, mold material, interface conditions, and other thermal factors. Chvorinov's rule is an empirical approximation rather than a universal law.

### Numerical Example 2: Solidification time

A casting has volume \(V=0.002\text{ m}^3\) and cooling surface area \(A=0.04\text{ m}^2\). Assume \(B=1200\text{ s/m}^2\) and \(n=2\).

Calculate the modulus:

\[
\frac{V}{A}=\frac{0.002}{0.04}=0.05\text{ m}
\]

Calculate solidification time:

\[
t_s=1200(0.05)^2
\]

\[
t_s=1200(0.0025)=3.0\text{ s}
\]

**Answer:** Estimated solidification time is 3.0 seconds.

This result is illustrative and unusually short for many practical castings. It should not be treated as a realistic production prediction without validating the mold constant, geometry, and heat-transfer assumptions.

### 6.1 Comparing two sections

For the same metal and mold conditions, assuming \(n=2\):

\[
\frac{t_{s,1}}{t_{s,2}}=
\left(\frac{(V/A)_1}{(V/A)_2}\right)^2
\]

A section with twice the modulus is predicted to require four times the solidification time.

This explains why thick sections and junctions between heavy sections are common locations for last-to-solidify regions and shrinkage defects.

## 7. Mold Design: Sprues, Runners, Gates, Risers, and Cores

### 7.1 Gating system

The gating system guides molten material into the mold cavity.

Typical elements include:
- Pouring basin.
- Sprue.
- Runner.
- Gates.
- Filters or other flow-control features where appropriate.

The design should fill the cavity without excessive turbulence, premature freezing, erosion, or entrainment of air and oxide films.

### 7.2 Risers

A riser acts as a reservoir of liquid metal that can feed a casting as it contracts during solidification.

A riser should remain able to supply liquid to regions that need feeding. Its geometry, insulation, location, and solidification sequence are therefore important.

A riser that freezes too early may not prevent shrinkage porosity.

### 7.3 Cores

Cores create internal cavities or passages that cannot be formed directly by the outer mold geometry.

Core materials and supports must withstand handling, mold filling, and thermal exposure while permitting appropriate removal after solidification.

Core positioning errors may produce wall-thickness variation or internal dimensional defects.

## 8. Fluid Flow and Mold Filling

Molten-metal flow affects filling time, temperature distribution, oxide formation, gas entrainment, and mold erosion.

For incompressible flow, conservation of volume gives:

\[
Q_v=Av
\]

where:
- \(Q_v\) = volumetric flow rate, m³/s.
- \(A\) = flow cross-sectional area, m².
- \(v\) = average flow velocity, m/s.

For a simplified gravity-driven ideal flow from a reservoir:

\[
v=\sqrt{2gh}
\]

where:
- \(g\) = gravitational acceleration, approximately 9.81 m/s².
- \(h\) = vertical head, m.

This expression assumes negligible losses and is not a complete model of a real gating system.

### Numerical Example 3: Flow rate

A gate has a cross-sectional area of \(400\text{ mm}^2\) and average metal velocity of 0.8 m/s.

Convert area:

\[
A=400\times10^{-6}=4.0\times10^{-4}\text{ m}^2
\]

Calculate flow:

\[
Q_v=Av=(4.0\times10^{-4})(0.8)
\]

\[
Q_v=3.2\times10^{-4}\text{ m}^3/\text{s}
\]

A cavity volume of \(0.0064\text{ m}^3\) would have an idealized filling time:

\[
t_f=\frac{0.0064}{3.2\times10^{-4}}=20\text{ s}
\]

This estimate assumes constant flow and ignores changes in head, losses, branching, and the volume of the gating system. Actual filling must be validated against the process geometry and material behavior.

## 9. Shrinkage and Feeding

Most metals contract during cooling, although the magnitude and sequence depend on composition and phase changes.

Three stages are often distinguished:
1. Liquid contraction as temperature decreases.
2. Volume change during solidification.
3. Solid-state contraction after solidification.

Casting design must manage the resulting volume changes.

### 9.1 Shrinkage porosity

Shrinkage porosity forms when liquid metal cannot adequately feed regions contracting during solidification.

Potential controls:
- Appropriate riser sizing and placement.
- Directional solidification.
- Chills or local thermal management.
- Suitable casting geometry.
- Improved feeding paths.
- Process simulation and validation.

### 9.2 Directional solidification

Directional solidification seeks to control the solidification sequence so that liquid feeding remains available to regions that solidify later.

A common strategy is to encourage solidification to progress toward a properly designed riser. This must be adapted to the alloy, mold, geometry, and cooling conditions.

## 10. Common Casting Defects

| Defect | Typical mechanism | Possible corrective action |
|---|---|---|
| Gas porosity | Gas entrapment or gas release | Improve melt quality, venting, and filling conditions |
| Shrinkage cavity | Inadequate feeding during solidification | Redesign risers and solidification sequence |
| Misrun | Incomplete cavity filling | Review temperature, filling time, gating, and wall thickness |
| Cold shut | Inadequate fusion between meeting flow fronts | Improve filling conditions and flow-front temperature |
| Hot tearing | Restrained contraction during vulnerable solidification stages | Modify geometry, mold restraint, alloy, or process conditions |
| Inclusions | Entrained oxides, sand, slag, or other foreign material | Improve melt handling, filtration, and mold integrity |
| Sand erosion | High-velocity flow damages the mold | Adjust gating, mold strength, and flow conditions |
| Mold shift | Misalignment of mold sections | Improve locating features and clamping |
| Surface roughness | Mold surface, coating, or filling effects | Improve mold preparation and process control |
| Dimensional variation | Shrinkage, thermal effects, mold movement | Improve tooling design and dimensional control |

Defects may have several interacting causes. Changing one parameter without confirming the mechanism can worsen another defect.

## 11. Polymer Injection Molding: Process Physics

Injection molding introduces additional effects related to polymer viscosity, viscoelasticity, crystallization, and thermal degradation.

### 11.1 Viscosity

Viscosity measures resistance to flow. Polymer melt viscosity depends on temperature, molecular structure, and shear rate.

Many polymer melts are shear-thinning: their apparent viscosity decreases as shear rate increases over a relevant range.

Consequently, filling behavior depends on the interaction among injection speed, temperature, cavity geometry, and pressure.

### 11.2 Packing and shrinkage

After the cavity fills, holding pressure can compensate for material contraction while the gate remains sufficiently open.

If packing is inadequate, sink marks and internal voids may form. Excessive packing can cause flash, higher residual stress, or difficult ejection.

### 11.3 Cooling

The mold removes heat until the component has enough rigidity for ejection.

Cooling-system layout strongly influences cycle time, warpage, and dimensional repeatability.

Nonuniform cooling can create differential shrinkage and residual stresses.

### 11.4 Numerical Example 4: Injection-molding cycle time

A component has the following cycle stages:

- Filling: 2.0 s.
- Packing and holding: 5.0 s.
- Cooling: 12.0 s.
- Mold opening, ejection, and closing: 3.0 s.

Assume these stages occur sequentially.

\[
t_c=2+5+12+3=22\text{ s}
\]

Ideal output per hour:

\[
Q=\frac{3600}{22}\approx163.6\text{ cycles/hour}
\]

If one part is produced per cycle, ideal output is approximately 164 parts/hour.

If a validated redesign reduces cooling time from 12 s to 9 s:

\[
t_{c,\text{new}}=2+5+9+3=19\text{ s}
\]

\[
Q_{\text{new}}=\frac{3600}{19}\approx189.5\text{ parts/hour}
\]

Ideal output increases by approximately:

\[
\frac{189.5-163.6}{163.6}\times100
\approx15.8\%
\]

This improvement is only acceptable if ejected-part temperature, warpage, mechanical properties, and dimensional stability remain within specification.

## 12. Manufacturing Parameters and Their Effects

### 12.1 Metal casting parameters

| Parameter | Potential effect |
|---|---|
| Pouring temperature | Fluidity, freezing behavior, gas interaction, mold degradation |
| Mold temperature | Cooling rate, filling behavior, solidification time |
| Filling velocity | Filling time, turbulence, erosion, gas entrainment |
| Gating design | Flow distribution and oxide or inclusion risks |
| Alloy composition | Freezing range, shrinkage behavior, mechanical properties |
| Riser geometry | Feeding effectiveness and yield |
| Cooling conditions | Microstructure, residual stress, and dimensional stability |
| Mold permeability | Gas escape and mold-related defect risk |

### 12.2 Polymer molding parameters

| Parameter | Potential effect |
|---|---|
| Melt temperature | Viscosity, filling, degradation risk |
| Mold temperature | Cooling, surface quality, crystallization, cycle time |
| Injection speed | Flow-front behavior, shear heating, air entrapment |
| Injection pressure | Filling and pressure losses |
| Packing pressure and time | Shrinkage compensation and residual stress |
| Cooling time | Cycle time and dimensional stability |
| Screw speed and back pressure | Melt preparation and material history |
| Gate geometry | Filling balance and gate-freeze timing |

Parameter interactions matter. Increasing melt temperature may improve filling but increase cooling demand or degradation risk.

## 13. Process Comparison and Selection

| Process | Typical volume | Tooling cost | Typical strengths | Important limitations |
|---|---|---|---|---|
| Sand casting | Low to high, depending on application | Low to moderate | Large parts and broad alloy range | Mold variability and finishing needs |
| Investment casting | Low to medium or high for suitable parts | Moderate to high | Complex geometry and fine detail | Multi-stage process and shell costs |
| Die casting | Usually medium to very high | High | Fast cycles and repeatable detail | High investment and porosity concerns |
| Permanent-mold casting | Medium to high for compatible parts | Moderate to high | Reusable tooling and repeatability | Geometry and alloy limitations |
| Injection molding | Medium to very high | High | High-volume polymer production | Expensive tooling and material-specific constraints |
| Compression molding | Application-dependent | Moderate to high | Selected thermosets and reinforced parts | Cycle time and process-specific flow limits |
| Blow molding | Medium to very high | Moderate to high | Hollow polymer products | Wall-thickness control |
| Thermoforming | Medium to high | Low to moderate for suitable tooling | Sheet-based parts and packaging | Thickness distribution and trimming |

Volume categories are approximate and overlap. Actual economic suitability depends on part size, material, tolerances, tooling life, labor, and scrap.

## 14. Design for Manufacturability

### 14.1 Design principles for castings

- Maintain reasonably uniform wall thickness where feasible.
- Avoid abrupt section transitions.
- Use generous fillets at suitable intersections.
- Minimize isolated heavy sections that may become hot spots.
- Provide draft where needed for pattern removal.
- Design cores and internal passages for support and removal.
- Include machining allowance only where required.
- Locate critical dimensions so they can be inspected.
- Consider parting-line location and gating access.
- Account for shrinkage and distortion using validated process data.

### 14.2 Design principles for molded polymers

- Use consistent wall thickness when feasible.
- Avoid abrupt thickness changes.
- Apply draft to support ejection.
- Use ribs and bosses carefully to limit sink marks and stress concentrations.
- Place gates and weld lines away from critical load paths where possible.
- Account for shrinkage and fiber orientation in reinforced polymers.
- Provide appropriate ejection surfaces.
- Design undercuts only when the tooling strategy supports them.

DFM recommendations are process-dependent. A geometry appropriate for injection molding may be inappropriate for sand casting or machining.

## 15. Quality Control and Inspection

Casting and molding quality assurance may include:

- Visual inspection.
- Dimensional measurement.
- Mass and density checks.
- Radiography or computed tomography for internal defects.
- Ultrasonic inspection where suitable.
- Penetrant or magnetic-particle inspection for applicable surface or near-surface flaws.
- Metallography and mechanical testing.
- Polymer moisture, melt-flow, and thermal testing where relevant.
- Process-data monitoring and statistical process control.

Not every inspection method detects every defect. Inspection selection must match defect type, material, geometry, access, acceptance criteria, and required detection capability.

## 16. Industrial R&D and Process Optimization

A casting or molding optimization project should define measurable outputs, such as:
- Defect rate.
- Porosity fraction.
- Dimensional deviation.
- Surface roughness.
- Mechanical strength.
- Cycle time.
- Material yield.
- Energy consumption.
- Cost per conforming part.

### Example: Experimental optimization

An engineer studies the influence of pouring temperature and filling velocity on casting porosity.

A structured experiment can:
1. Establish a baseline.
2. Define safe experimental ranges.
3. Change factors according to a planned design.
4. Record material lot, mold condition, and environmental variables.
5. Measure porosity using a consistent inspection method.
6. Fit a suitable statistical model.
7. Examine interactions and uncertainty.
8. Confirm the proposed settings in independent production trials.

Changing one parameter at a time can miss interactions. For example, a higher pouring temperature may be beneficial at one filling velocity but detrimental at another.

### Process simulation

Computational models may predict:
- Filling patterns.
- Temperature distribution.
- Solidification sequence.
- Feeding behavior.
- Porosity risk.
- Residual stress and distortion.

Simulation results depend on material properties, boundary conditions, mesh quality, and model assumptions. Validation against experimental evidence remains necessary.

### Connection to Computer Engineering

A manufacturing R&D engineer with programming skills can develop:
- Sensor-data pipelines.
- Computer-vision inspection systems.
- Statistical defect-analysis tools.
- Process-parameter optimization algorithms.
- Digital twins.
- Machine-learning models for defect prediction.

A predictive model should be evaluated using independent production data, appropriate validation splits, calibration where needed, and metrics that reflect actual defect and cost consequences.

## 17. Common Misconceptions

- All casting defects can be solved by increasing pouring temperature.
- A larger riser always eliminates shrinkage.
- High pressure eliminates every type of die-casting porosity.
- Faster mold filling always improves quality.
- A shorter molding cycle is always better.
- Polymer shrinkage is identical for every grade and geometry.
- Simulation results are automatically accurate without validation.
- A process that produces the correct external geometry necessarily produces acceptable internal properties.
- High production volume alone guarantees that die casting or injection molding is economical.

## 18. Summary

Casting and molding transform liquid, softened, or otherwise processable materials into shaped products using cavities. Their performance depends on material behavior, flow, heat transfer, solidification or curing, tooling, and process control. Chvorinov's rule provides an initial estimate of metal-casting solidification time, while mass and heat balances support process analysis. Common defects include porosity, shrinkage, incomplete filling, warpage, and dimensional variation. Successful process selection balances geometry, properties, production volume, tooling cost, quality, and validated manufacturing capability.

## 19. Review Questions

1. How does sand casting differ from die casting?
2. Explain the roles of sprues, runners, gates, risers, and cores.
3. Distinguish sensible heat from latent heat.
4. What does Chvorinov's rule predict, and what are its limitations?
5. Why does a thick casting section often solidify later than a thin section?
6. Explain the difference between gas porosity and shrinkage porosity.
7. How does packing pressure influence injection-molded polymer parts?
8. Why can increasing injection speed cause problems as well as improve filling?
9. What are the advantages and disadvantages of permanent tooling?
10. Design a small experimental study to reduce porosity in an aluminum casting.

## 20. Challenging Exercises with Complete Solutions

### Exercise 1: Solidification-time comparison

Two castings use the same metal and mold system. Their moduli are:

\[
M_1=0.03\text{ m}, \qquad M_2=0.045\text{ m}
\]

Assume Chvorinov's rule with \(n=2\), and casting 1 solidifies in 18 seconds. Estimate the solidification time of casting 2.

**Solution**

For the same mold constant:

\[
\frac{t_2}{t_1}=\left(\frac{M_2}{M_1}\right)^2
\]

Substitute:

\[
t_2=18\left(\frac{0.045}{0.03}\right)^2
\]

\[
t_2=18(1.5)^2=18(2.25)
\]

\[
t_2=40.5\text{ s}
\]

**Answer:** Estimated solidification time is 40.5 seconds.

The estimate assumes equivalent thermal conditions and geometry behavior represented adequately by the same mold constant.

### Exercise 2: Casting yield

A foundry pours 500 kg of metal. Finished acceptable castings weigh 365 kg. The remaining metal is in runners, risers, gates, and rejected castings. Calculate casting yield and non-product metal mass.

**Solution**

Casting yield:

\[
Y=\frac{\text{Mass of acceptable castings}}
{\text{Mass poured}}\times100
\]

\[
Y=\frac{365}{500}\times100=73\%
\]

Non-product mass:

\[
m_{\text{non-product}}=500-365=135\text{ kg}
\]

**Answer:** Yield is 73%, and non-product mass is 135 kg.

The 135 kg is not necessarily all waste: runners and risers may be recyclable, depending on alloy quality and foundry practice. Rejected castings may also be recoverable through remelting where permitted.

### Exercise 3: Gating flow rate

Molten metal flows through a gate of area \(250\text{ mm}^2\) at an average velocity of 1.2 m/s. The cavity volume is \(0.003\text{ m}^3\). Estimate ideal filling time.

**Solution**

Convert the gate area:

\[
A=250\times10^{-6}=2.5\times10^{-4}\text{ m}^2
\]

Calculate volumetric flow:

\[
Q_v=Av=(2.5\times10^{-4})(1.2)
\]

\[
Q_v=3.0\times10^{-4}\text{ m}^3/\text{s}
\]

Calculate filling time:

\[
t_f=\frac{V}{Q_v}
=\frac{0.003}{3.0\times10^{-4}}
\]

\[
t_f=10\text{ s}
\]

**Answer:** Ideal filling time is 10 seconds.

This calculation assumes constant flow and excludes the gating-system volume, changes in flow velocity, and thermal losses.

### Exercise 4: Injection-molding output and scrap

An injection-molding machine has a 24-second cycle and produces two parts per cycle. Its operational availability is 90%. The first-pass yield is 98%. Estimate good parts per operating hour when the machine is scheduled for one hour.

**Solution**

Ideal cycles per scheduled hour:

\[
N_c=\frac{3600}{24}=150\text{ cycles}
\]

Available cycles after downtime:

\[
N_{c,\text{actual}}=150(0.90)=135\text{ cycles}
\]

Total parts:

\[
N_{\text{total}}=135(2)=270\text{ parts}
\]

Expected good parts:

\[
N_{\text{good}}=270(0.98)=264.6
\]

**Answer:** Expected output is approximately 265 good parts per scheduled hour.

Actual output is an integer and will vary. The calculation assumes the stated availability and yield are representative and that each cycle produces two parts.

### Exercise 5: Cooling-time optimization

A molded component currently requires a 30-second cycle. Cooling accounts for 18 seconds, while all other operations total 12 seconds. An improved cooling design is expected to reduce cooling time by 25%. Estimate the new cycle time and percentage increase in ideal production rate.

**Solution**

New cooling time:

\[
t_{\text{cool,new}}=18(1-0.25)=13.5\text{ s}
\]

New cycle time:

\[
t_{\text{new}}=12+13.5=25.5\text{ s}
\]

Original ideal rate:

\[
R_1=\frac{3600}{30}=120\text{ cycles/hour}
\]

New ideal rate:

\[
R_2=\frac{3600}{25.5}\approx141.18\text{ cycles/hour}
\]

Percentage increase:

\[
\%\Delta R=\frac{R_2-R_1}{R_1}\times100
\]

\[
\%\Delta R=\frac{141.18-120}{120}\times100
\approx17.6\%
\]

**Answer:** The new cycle time is 25.5 seconds, and ideal production rate increases by approximately 17.6%.

The design must still achieve adequate cooling, ejection stability, dimensional control, and required mechanical properties.

## 21. Glossary

- **Casting:** Shaping a material by introducing it into a mold and allowing it to solidify or otherwise set.
- **Chvorinov's rule:** Empirical relationship estimating casting solidification time from the volume-to-surface-area ratio.
- **Cold shut:** Defect where meeting liquid fronts fail to fuse adequately.
- **Core:** Mold element used to create internal geometry.
- **Die casting:** Forcing molten metal into a reusable metallic die.
- **Gate:** Opening through which material enters a mold cavity.
- **Hot tearing:** Cracking during vulnerable stages of solidification and contraction.
- **Injection molding:** Forcing material into a closed mold, commonly used for polymers.
- **Latent heat:** Energy absorbed or released during a phase change.
- **Mold:** Tool or cavity that defines the shape of a product during processing.
- **Porosity:** Presence of pores or voids within a material.
- **Riser:** Reservoir designed to feed a casting during solidification.
- **Runner:** Passage distributing material from the sprue or main feed channel toward the gates.
- **Shrinkage:** Volume or dimensional reduction associated with cooling, solidification, or polymer processing.
- **Sprue:** Channel that delivers molten material from the pouring basin into the gating system.
- **Thermoforming:** Shaping a heated thermoplastic sheet using a mold and applied pressure or vacuum.
- **Yield:** Fraction of input material converted into acceptable product under a defined accounting method.

## 22. References and Further Learning

1. [MIT OpenCourseWare](https://ocw.mit.edu/) — university engineering courses and technical learning materials.
2. [NIST Manufacturing](https://www.nist.gov/manufacturing) — manufacturing research, measurement, and process-related resources.
3. [ASM International](https://www.asminternational.org/) — metalcasting, metallurgy, defects, and materials-processing references.
4. [American Foundry Society](https://www.afsinc.org/) — metalcasting technology, industry resources, and professional education.
5. [Society of Manufacturing Engineers](https://www.sme.org/) — manufacturing process knowledge and professional development.
6. Groover, M. P. *Fundamentals of Modern Manufacturing: Materials, Processes, and Systems*. A broad textbook covering casting, molding, forming, machining, and manufacturing systems.
7. Kalpakjian, S., and Schmid, S. R. *Manufacturing Engineering and Technology*. A comprehensive reference on manufacturing processes and engineering principles.
8. [ASTM International](https://www.astm.org/) — relevant material specifications, testing methods, and inspection standards.
9. [ISO Standards](https://www.iso.org/standards.html) — international standards catalog.

Use the current standard and the relevant process-specific requirements for production qualification. The equations and numerical examples in this module are educational models; production decisions require validated material data, equipment limits, and process trials.