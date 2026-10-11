
# Module 05: Forming Processes and Metalworking

## 1. Learning Objectives

By completing this module, you should be able to:

- Explain plastic deformation and the mechanical behavior of metals during forming.
- Distinguish elastic deformation from plastic deformation.
- Compare rolling, forging, extrusion, drawing, sheet-metal stamping, and bending.
- Calculate true stress, true strain, forming force, reduction ratio, and idealized deformation work.
- Explain strain hardening, recrystallization, recovery, and texture development.
- Evaluate friction, lubrication, temperature, strain rate, and tool geometry.
- Identify defects such as cracks, wrinkles, laps, barreling, and springback.
- Apply design-for-manufacturing principles to formed metal components.
- Connect forming-process development to materials testing, simulation, quality engineering, and industrial R&D.

## 2. Introduction and Industrial Importance

Metal forming changes a material's shape by applying forces that cause plastic deformation. Unlike machining, which removes material, forming generally redistributes material while retaining most of its mass.

Forming processes are essential in automotive body panels, aircraft structures, structural beams, beverage cans, fasteners, pipes, medical instruments, and industrial machinery.

The principal advantages are high material utilization, potentially high production rates, and the ability to improve mechanical properties through controlled deformation and microstructural evolution.

However, forming requires appropriate combinations of material ductility, tooling, force, temperature, lubrication, and geometry. Excessive deformation can cause cracking, while poor process control can create residual stresses, dimensional errors, and nonuniform properties.

## 3. Fundamental Mechanics of Plastic Deformation

### 3.1 Elastic and plastic deformation

Elastic deformation is recoverable when the load is removed. Plastic deformation produces permanent shape change.

For small elastic strains in a uniaxial test:

\[
\sigma=E\varepsilon
\]

where:
- \(\sigma\) = engineering normal stress, Pa.
- \(E\) = Young's modulus, Pa.
- \(\varepsilon\) = engineering strain, dimensionless.

Once the material exceeds its relevant yield condition, plastic deformation begins. The actual yield behavior depends on alloy, heat treatment, temperature, strain rate, and loading state.

### 3.2 Engineering stress and strain

For a tensile specimen:

\[
\sigma_e=\frac{F}{A_0}
\]

\[
\varepsilon_e=\frac{L-L_0}{L_0}
\]

where:
- \(F\) = applied tensile force, N.
- \(A_0\) = initial cross-sectional area, m².
- \(L_0\) = initial gauge length, m.
- \(L\) = current gauge length, m.

Engineering stress uses the original area. As a specimen stretches, its cross-sectional area usually decreases, so engineering stress does not represent the actual force divided by the instantaneous area.

### 3.3 True stress and true strain

Before significant necking in a tensile test, assuming uniform deformation and approximately constant volume:

\[
\sigma_t=\frac{F}{A}
\]

\[
\varepsilon_t=\ln\left(\frac{L}{L_0}\right)
\]

For uniform tensile deformation:

\[
\sigma_t=\sigma_e(1+\varepsilon_e)
\]

\[
\varepsilon_t=\ln(1+\varepsilon_e)
\]

These conversions are not generally valid after substantial necking without additional measurement or modeling because deformation becomes nonuniform.

For idealized homogeneous plastic deformation of metals, volume is often approximated as constant:

\[
A_0L_0\approx AL
\]

This approximation is useful for many forming calculations, but it can be affected by porosity, damage, phase changes, or other mechanisms.

## 4. Plastic Flow and Strain Hardening

Many metals require increasing flow stress as plastic strain accumulates at a fixed temperature and strain rate. This behavior is called strain hardening or work hardening.

A commonly used empirical model is the Hollomon equation:

\[
\sigma_t=K\varepsilon_p^n
\]

where:
- \(\sigma_t\) = true flow stress, Pa.
- \(K\) = strength coefficient, Pa.
- \(\varepsilon_p\) = true plastic strain, dimensionless.
- \(n\) = strain-hardening exponent, dimensionless.

The model is an approximation over a material-specific strain range. It should not be extrapolated indiscriminately to zero strain, very large strain, or conditions involving significant temperature or strain-rate changes.

A higher strain-hardening exponent often indicates greater capacity for strain redistribution during tensile deformation, but forming limits also depend on anisotropy, thickness, geometry, and loading path.

## 5. Major Metal-Forming Processes

### 5.1 Rolling

Rolling passes metal between rotating rolls to reduce thickness, alter cross-section, or control surface and mechanical characteristics.

Types include:
- Hot rolling.
- Cold rolling.
- Flat rolling.
- Shape rolling.
- Ring rolling.

Hot rolling occurs at temperatures where recovery or recrystallization can substantially influence deformation. Cold rolling occurs below the relevant recrystallization conditions and commonly increases strength through strain hardening.

Important variables include roll diameter, reduction, friction, speed, temperature, lubrication, and material flow stress.

### 5.2 Forging

Forging applies compressive forces using hammers or presses.

Common forms include:
- Open-die forging.
- Impression-die forging.
- Closed-die forging.
- Precision forging.

Forging can produce favorable grain-flow patterns and useful mechanical properties when the process is appropriately designed. It does not automatically guarantee defect-free material; laps, underfilling, internal cracking, and unsuitable grain flow remain possible.

### 5.3 Extrusion

Extrusion forces material through a die opening to produce a continuous product with a defined cross-section.

- **Direct extrusion:** material flows through a die in the direction of ram movement.
- **Indirect extrusion:** the die moves relative to the billet in a configuration that reduces some container-wall friction.
- **Hot extrusion:** deformation occurs at elevated temperature.
- **Cold extrusion:** deformation occurs at lower temperature, with potentially high forces and significant work hardening.

Applications include aluminum profiles, rods, tubes, and selected copper and steel products.

### 5.4 Drawing

Drawing pulls material through a die to reduce its cross-section.

Wire drawing produces wire and small rods; tube drawing can control tube diameter and wall thickness.

Drawing requires control of reduction per pass, die angle, lubrication, material ductility, and drawing stress. Excessive reduction or poor lubrication can cause fracture or surface damage.

### 5.5 Sheet-metal forming

Sheet-metal operations include:
- Blanking and punching.
- Bending.
- Deep drawing.
- Stretch forming.
- Flanging.
- Hemming.

Blanking and punching separate material using a punch and die. Bending changes angular geometry, while deep drawing forms a sheet into a cup-like or similar three-dimensional shape.

Deep drawing is sensitive to blank-holder force, friction, material anisotropy, draw ratio, and die geometry.

## 6. Rolling Mechanics

For a simple flat-rolling operation, thickness reduction is:

\[
\Delta h=h_0-h_f
\]

where:
- \(h_0\) = initial thickness, m.
- \(h_f\) = final thickness, m.
- \(\Delta h\) = thickness reduction, m.

Percentage reduction is:

\[
r=\frac{h_0-h_f}{h_0}\times100\%
\]

Under idealized volume conservation and negligible width change:

\[
h_0L_0\approx h_fL_f
\]

Thus:

\[
\frac{L_f}{L_0}\approx\frac{h_0}{h_f}
\]

Actual width spread, elastic roll deformation, slip, and nonuniform strain may modify these estimates.

### Numerical Example 1: Rolling reduction

A steel strip is reduced from 10 mm to 7 mm.

Known:
- \(h_0=10\text{ mm}\).
- \(h_f=7\text{ mm}\).

Absolute reduction:

\[
\Delta h=10-7=3\text{ mm}
\]

Percentage reduction:

\[
r=\frac{10-7}{10}\times100\%=30\%
\]

If width change is negligible, the approximate length ratio is:

\[
\frac{L_f}{L_0}\approx\frac{10}{7}=1.429
\]

**Interpretation:** The thickness decreases by 30%, while the strip length increases by approximately 42.9% under the idealized assumptions.

## 7. Forging, Friction, and Deformation

In forging, contact friction affects material flow. Friction can restrain surface flow, increase force requirements, and produce barreling in compression tests.

The actual forging force depends on:
- Projected contact area.
- Instantaneous flow stress.
- Part geometry.
- Friction.
- Strain rate.
- Temperature.
- Deformation history.

A first approximation is:

\[
F\approx \bar{\sigma}_f A_p
\]

where:
- \(F\) = forming force, N.
- \(\bar{\sigma}_f\) = representative average flow stress, Pa.
- \(A_p\) = projected loaded area, m².

This is a simplified estimate. Real forging loads may require correction factors or finite-element analysis.

### Numerical Example 2: Approximate forging force

A simple upsetting operation has an instantaneous projected area of \(0.015\text{ m}^2\) and average flow stress of 120 MPa.

Convert stress:

\[
\bar{\sigma}_f=120\times10^6\text{ Pa}
\]

Calculate force:

\[
F\approx120\times10^6(0.015)
\]

\[
F\approx1.8\times10^6\text{ N}
\]

**Answer:** The simplified estimate is 1.8 MN.

Friction, geometry, strain hardening, and press dynamics may require a larger actual capacity. Equipment selection should use a validated load estimate and suitable engineering margins.

## 8. Deep Drawing and Formability

Deep drawing transforms a flat blank into a hollow component. Material flows from the flange into the die cavity while the punch drives the sheet.

Common defects include:
- Wrinkling.
- Tearing.
- Excessive thinning.
- Earing.
- Surface marking.
- Springback after unloading.

The drawing ratio is often expressed as:

\[
DR=\frac{D_0}{D_p}
\]

where:
- \(D_0\) = initial blank diameter, m.
- \(D_p\) = punch diameter, m.
- \(DR\) = dimensionless drawing ratio.

The maximum feasible drawing ratio depends on the material, tooling, lubrication, blank-holder force, and process sequence. There is no universal safe value for every material and geometry.

### Formability factors

- **Ductility:** ability to sustain plastic deformation before fracture.
- **Plastic anisotropy:** directional differences in plastic deformation behavior.
- **Strain-rate sensitivity:** dependence of flow stress on deformation rate.
- **Forming-limit curve:** experimentally determined boundary associated with localized necking for specified sheet conditions and loading paths.
- **Friction:** affects material flow and local strain distribution.

A tensile elongation value alone is not sufficient to predict performance in every sheet-forming operation.

## 9. Hot Working and Cold Working

| Characteristic | Hot working | Cold working |
|---|---|---|
| Temperature | Elevated relative to relevant recrystallization conditions | Lower temperature, typically near ambient |
| Flow stress | Often lower | Often higher |
| Required force | Often lower for comparable deformation | Often higher |
| Surface oxidation | Can be significant | Usually lower, depending on environment |
| Dimensional control | Thermal contraction and scale may complicate control | Often better for suitable processes |
| Strain hardening | May be offset by recovery or recrystallization | Usually accumulates more strongly |
| Microstructure | May refine grains under suitable conditions | May develop elongated grains and texture |
| Typical applications | Large reductions and bulk shaping | Sheet finishing, wire drawing, precision dimensions |

The distinction is based on material behavior rather than a universal temperature threshold. Different alloys have different recrystallization and recovery behavior.

## 10. Microstructural Evolution

Plastic deformation changes the arrangement of dislocations and the shape and orientation of grains.

### 10.1 Recovery

Recovery rearranges or annihilates some defects, reducing stored energy and changing properties without necessarily producing new grains.

### 10.2 Recrystallization

Recrystallization forms new, relatively low-dislocation-density grains in a sufficiently deformed material under suitable thermal conditions.

It can reduce work hardening and improve ductility.

### 10.3 Grain growth

At sufficiently high temperature or long exposure, grains can grow. Excessive grain growth may reduce desired properties or create nonuniform behavior.

### 10.4 Texture and anisotropy

Forming can orient crystallographic directions preferentially. The resulting texture may produce direction-dependent yield behavior and plastic flow.

In sheet metal, anisotropy can contribute to earing during deep drawing. Process engineers may select suitable sheet grades, orientations, and tooling conditions to control it.

## 11. Defects and Troubleshooting

| Defect | Potential cause | Engineering response |
|---|---|---|
| Edge cracking | Low ductility, poor edge quality, excessive strain | Improve material condition, edge preparation, or reduction schedule |
| Centerline cracking | Stress state and deformation conditions | Review process geometry and reduction schedule |
| Wrinkling | Excessive unsupported compressive deformation | Optimize blank-holder force and tooling |
| Tearing | Localized thinning or excessive strain | Improve material selection and strain distribution |
| Springback | Elastic recovery after unloading | Compensate tool geometry and evaluate material behavior |
| Barreling | Friction restraining surface flow in compression | Improve lubrication and contact conditions |
| Laps or folds | Improper material flow or die design | Revise preform and die geometry |
| Surface scoring | Tool wear, contamination, or poor lubrication | Improve tooling maintenance and cleanliness |
| Dimensional variation | Temperature, tooling, force, or material variability | Monitor process conditions and inspect output |
| Excessive forming force | High flow stress, friction, or unsuitable geometry | Review material condition, lubrication, and process design |

Defect correction should be evidence-based. A change that reduces one defect may increase another or alter final properties.

## 12. Manufacturing Parameters and Productivity

Critical variables include:
- Initial stock geometry.
- Reduction per pass.
- Forming temperature.
- Strain rate and press speed.
- Tool geometry.
- Lubricant type and application.
- Die and roll temperature.
- Material batch and heat treatment.
- Cooling rate.
- Tool wear.

Higher production speed may improve output but increase heat generation, lubrication demands, dynamic loads, or defect risk. Optimization should consider the cost per conforming part rather than cycle time alone.

## 13. Design for Manufacturability

A formed component should be designed with the selected operation in mind.

Useful principles:
- Avoid unnecessary abrupt section changes.
- Maintain adequate bend radii for the selected material and thickness.
- Account for springback.
- Avoid excessive reductions in one forming pass.
- Design realistic flange widths and draw depths.
- Consider grain direction where anisotropy matters.
- Provide tool access and appropriate locating features.
- Avoid geometries that trap material or cause folds.
- Include suitable allowances for finishing and dimensional correction.

For sheet metal, the minimum practical bend radius depends on alloy, temper, thickness, direction relative to rolling, and required surface quality.

For forged components, suitable parting lines, draft, fillets, and preform geometry improve die filling and reduce defects.

## 14. Industrial R&D and Simulation

Industrial R&D can combine:
- Tensile and compression testing.
- Forming-limit measurements.
- Tribology and lubrication trials.
- Instrumented press measurements.
- Digital image correlation.
- Metallography and hardness mapping.
- Finite-element simulation.
- Statistical experimental design.

Finite-element forming models can predict stress, strain, thinning, temperature, contact pressure, and springback. Their accuracy depends on constitutive models, friction assumptions, mesh quality, boundary conditions, and experimental validation.

A useful research workflow is:

1. Characterize the material.
2. Define the geometry and process constraints.
3. Establish a baseline experiment.
4. Build and calibrate a simulation.
5. Identify influential parameters.
6. Run a designed experiment or optimization.
7. Validate predicted improvements on real equipment.
8. Document process windows and uncertainty.

## 15. Common Misconceptions

- All plastic deformation reduces material strength.
- Hot working is always better than cold working.
- The highest possible forming speed always maximizes productivity.
- A material with high tensile elongation will succeed in every forming operation.
- Lubrication only reduces friction and has no other process effects.
- A simulation predicts real forming behavior accurately without calibration.
- Springback can be eliminated entirely through tool design in every application.
- Forging automatically guarantees superior properties regardless of grain flow and process quality.

## 16. Summary

Metal forming produces permanent shape change through controlled plastic deformation. Rolling, forging, extrusion, drawing, and sheet forming differ in geometry, stress state, material flow, and tooling. True stress and true strain describe deformation more appropriately than engineering measures in many plastic-flow analyses. Temperature, strain hardening, friction, anisotropy, and strain rate determine process behavior. Reliable manufacturing requires balancing force, ductility, dimensional accuracy, productivity, and microstructural performance.

## 17. Review Questions

1. Distinguish elastic deformation from plastic deformation.
2. Why is true stress different from engineering stress?
3. Explain the physical meaning of strain hardening.
4. Compare hot working and cold working.
5. What is the purpose of a forming-limit curve?
6. Explain why friction influences forging force and material flow.
7. What causes springback in sheet-metal forming?
8. How can anisotropy contribute to earing?
9. Why does a simplified forging-force estimate require validation?
10. Propose an experiment to reduce cracking during wire drawing.

## 18. Challenging Exercises with Complete Solutions

### Exercise 1: True stress and true strain

A tensile specimen has engineering strain of 0.20 and engineering stress of 250 MPa. Assume uniform deformation and approximately constant volume.

Calculate true strain and true stress.

**Solution**

True strain:

\[
\varepsilon_t=\ln(1+\varepsilon_e)
\]

\[
\varepsilon_t=\ln(1.20)\approx0.1823
\]

True stress:

\[
\sigma_t=\sigma_e(1+\varepsilon_e)
\]

\[
\sigma_t=250(1.20)=300\text{ MPa}
\]

**Answer:** True strain is approximately 0.182 and true stress is 300 MPa.

These conversions assume uniform deformation and should not be applied directly after substantial necking without additional analysis.

### Exercise 2: Rolling reduction and length

A strip is rolled from 8 mm to 5 mm thickness. Its initial length is 2 m. Assume width remains constant and volume is conserved.

Calculate percentage thickness reduction and final length.

**Solution**

Reduction:

\[
r=\frac{8-5}{8}\times100\%=37.5\%
\]

Volume conservation:

\[
h_0L_0=h_fL_f
\]

Rearrange:

\[
L_f=\frac{h_0L_0}{h_f}
\]

\[
L_f=\frac{8(2)}{5}=3.2\text{ m}
\]

**Answer:** Thickness reduction is 37.5%, and idealized final length is 3.2 m.

Real rolling may involve width spread and other deviations.

### Exercise 3: Idealized drawing stress

A wire has an initial cross-sectional area of 20 mm² and a final area of 12 mm². Assume an idealized, frictionless process with a representative flow stress of 200 MPa. Use the simplified estimate:

\[
\sigma_d=\bar{\sigma}_f\ln\left(\frac{A_0}{A_f}\right)
\]

Calculate idealized drawing stress and the corresponding force based on the final area.

**Solution**

Area ratio:

\[
\frac{A_0}{A_f}=\frac{20}{12}=1.667
\]

Drawing stress:

\[
\sigma_d=200\ln(1.667)
\]

\[
\sigma_d\approx200(0.5108)=102.2\text{ MPa}
\]

Convert final area:

\[
A_f=12\times10^{-6}\text{ m}^2
\]

Force:

\[
F=\sigma_dA_f
\]

\[
F=102.2\times10^6(12\times10^{-6})
\]

\[
F\approx1226\text{ N}
\]

**Answer:** Idealized drawing stress is approximately 102 MPa, and estimated force is 1.23 kN.

This simplified model excludes redundant deformation, friction, die geometry effects, and other real-process losses.

### Exercise 4: Forging load

A forging operation has an average flow stress of 180 MPa and projected area of \(0.025\text{ m}^2\). Estimate the load using \(F\approx\bar{\sigma}_fA_p\).

**Solution**

Convert flow stress:

\[
\bar{\sigma}_f=180\times10^6\text{ Pa}
\]

Calculate:

\[
F=180\times10^6(0.025)
\]

\[
F=4.5\times10^6\text{ N}
\]

**Answer:** The simplified forging load is 4.5 MN.

Actual press capacity must account for geometry, friction, strain-rate effects, process variation, and engineering safety requirements.

### Exercise 5: Production-rate improvement

A forming press produces one part every 8 seconds. A process improvement reduces cycle time to 7.2 seconds. Assume continuous operation without downtime or rejects.

Calculate original and new hourly production rates and the percentage improvement.

**Solution**

Original rate:

\[
R_1=\frac{3600}{8}=450\text{ parts/hour}
\]

New rate:

\[
R_2=\frac{3600}{7.2}=500\text{ parts/hour}
\]

Percentage improvement:

\[
\%\Delta R=\frac{500-450}{450}\times100\%
\]

\[
\%\Delta R\approx11.1\%
\]

**Answer:** Production increases from 450 to 500 parts/hour, an idealized improvement of 11.1%.

Validate that the shorter cycle does not increase tool wear, defects, or maintenance downtime.

## 19. Glossary

- **Anisotropy:** Direction-dependent material behavior.
- **Cold working:** Plastic deformation at temperatures where recovery and recrystallization are limited relative to the deformation process.
- **Drawing:** Pulling material through a die to reduce its cross-section.
- **Extrusion:** Forcing material through a die to produce a defined cross-section.
- **Flow stress:** Stress required to sustain plastic deformation under specified conditions.
- **Formability:** Ability to undergo a forming operation without unacceptable failure.
- **Forging:** Shaping material primarily through compressive loading.
- **Plastic deformation:** Permanent deformation remaining after unloading.
- **Recrystallization:** Formation of new grains that reduces stored deformation energy under suitable conditions.
- **Rolling:** Deformation between rolls to change thickness or cross-section.
- **Springback:** Elastic recovery after forming loads are removed.
- **Strain hardening:** Increase in flow stress associated with accumulated plastic deformation under specified conditions.
- **True strain:** Logarithmic strain measure based on incremental deformation.
- **True stress:** Applied force divided by the instantaneous cross-sectional area.
- **Work hardening:** Another term for strain hardening.
- **Yield strength:** Stress associated with the onset of defined plastic deformation.

## 20. References and Further Learning

1. [MIT OpenCourseWare](https://ocw.mit.edu/) — engineering mechanics, materials, and manufacturing learning resources.
2. [ASM International](https://www.asminternational.org/) — metal forming, metallurgy, and materials-processing references.
3. [Society of Manufacturing Engineers](https://www.sme.org/) — manufacturing technology and professional resources.
4. Groover, M. P. *Fundamentals of Modern Manufacturing: Materials, Processes, and Systems*.
5. Kalpakjian, S., and Schmid, S. R. *Manufacturing Engineering and Technology*.
6. Hosford, W. F., and Caddell, R. M. *Metal Forming: Mechanics and Metallurgy*.
7. [NIST Manufacturing](https://www.nist.gov/manufacturing) — manufacturing research and measurement resources.
8. [ASTM International](https://www.astm.org/) — standards and test methods relevant to materials and forming.

This is a custom instructional module, not an official MIT course syllabus.