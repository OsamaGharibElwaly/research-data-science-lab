
# Module 10: Surface Engineering and Heat Treatment

## 1. Learning Objectives

- Explain how heat treatment changes the microstructure and properties of metals.
- Distinguish annealing, normalizing, quenching, tempering, and precipitation hardening.
- Understand phase transformations in steel and the role of time-temperature history.
- Compare surface hardening, case hardening, coatings, and surface finishing.
- Calculate simplified heat-treatment and coating-related quantities.
- Explain hardness, wear, fatigue, residual stress, and corrosion mechanisms.
- Select surface treatments based on application requirements.
- Connect heat treatment to process optimization, materials characterization, and industrial R&D.

## 2. Introduction

Heat treatment modifies material properties through controlled heating, holding, and cooling. Surface engineering modifies the surface or near-surface region to improve properties such as wear resistance, corrosion resistance, hardness, friction, or fatigue performance.

The surface is often where components interact with their environment. Contact stresses, sliding, oxidation, chemical attack, and fatigue cracks may originate at or near the surface.

Applications include:
- Gears, shafts, bearings, and automotive transmission components.
- Turbine components and aerospace landing-gear systems.
- Cutting tools and dies.
- Medical instruments and selected implants.
- Pumps, valves, and chemical-processing equipment.
- Industrial molds and high-wear machine parts.

A treatment must improve the intended property without creating unacceptable brittleness, distortion, residual stress, dimensional changes, or environmental risks.

## 3. Metallurgical Foundations

### 3.1 Crystal structure and phases

Metallic materials contain atoms arranged in crystal structures. In steel, the arrangement of iron atoms and the presence of carbon influence phase stability and mechanical properties.

Important steel phases and microstructures include:

- **Ferrite:** A relatively soft iron-rich phase with limited carbon solubility.
- **Austenite:** A face-centered cubic phase stable under suitable temperature and composition conditions.
- **Cementite:** Iron carbide, Fe3C, a hard and brittle constituent.
- **Pearlite:** A microstructure consisting of alternating ferrite and cementite.
- **Bainite:** A transformation microstructure with morphology and properties dependent on composition and thermal history.
- **Martensite:** A hard transformation product formed when suitable austenite is cooled rapidly enough to suppress competing transformations.

Actual microstructures depend on alloy chemistry, prior structure, heating conditions, and cooling rate.

### 3.2 Phase diagrams

Phase diagrams indicate which phases are thermodynamically stable under specified equilibrium conditions. The iron-carbon diagram is particularly important for understanding steel processing.

However, equilibrium phase diagrams alone cannot predict the full microstructure produced by rapid cooling. Transformation kinetics and time-temperature-transformation (TTT) or continuous-cooling-transformation (CCT) diagrams are also important.

### 3.3 Diffusion

Diffusion describes atomic transport driven by concentration gradients and thermodynamic forces.

A simplified one-dimensional Fick's first law is:

\[
J=-D\frac{\partial C}{\partial x}
\]

where:

- \(J\) = diffusion flux, mol/(m²·s) when \(C\) is mol/m³.
- \(D\) = diffusion coefficient, m²/s.
- \(C\) = concentration, mol/m³.
- \(x\) = position, m.

The negative sign indicates diffusion down the concentration gradient under the simple model.

The diffusion coefficient commonly increases with temperature and can be represented approximately by:

\[
D=D_0\exp\left(-\frac{Q}{RT}\right)
\]

where:

- \(D_0\) = pre-exponential factor, m²/s.
- \(Q\) = activation energy for diffusion, J/mol.
- \(R\) = gas constant, 8.314 J/(mol·K).
- \(T\) = absolute temperature, K.

This relation explains why diffusion-controlled processes such as carburizing accelerate significantly at higher temperatures.

## 4. Major Heat-Treatment Processes

### 4.1 Annealing

Annealing involves heating and controlled cooling to obtain a desired condition, which may include reduced hardness, improved ductility, reduced residual stress, or a more suitable microstructure.

The exact cycle depends on alloy and objective.

### 4.2 Normalizing

Normalizing is commonly applied to steels by heating into a suitable austenitizing range followed by cooling in air or another specified environment.

It can refine grain structure and produce a more uniform microstructure than some prior processing routes. Outcomes depend on composition and section thickness.

### 4.3 Quenching

Quenching cools a heated component rapidly enough to produce a targeted transformation or property state.

Quench media include water, oil, polymer solutions, gases, and other controlled cooling systems.

Risks include:
- Cracking.
- Distortion.
- Nonuniform hardness.
- Residual stress.
- Unwanted microstructures.

The appropriate quench severity depends on the alloy, geometry, and required properties.

### 4.4 Tempering

Tempering reheats a previously hardened steel to a specified temperature below the relevant transformation range and holds it for a defined time.

It generally reduces the brittleness of as-quenched martensitic steel while adjusting hardness and toughness.

The outcome depends on temperature, time, composition, and prior microstructure.

### 4.5 Precipitation hardening

Certain alloys are strengthened by forming a controlled distribution of fine precipitates.

A typical route includes:
1. Solution heat treatment.
2. Quenching to retain a supersaturated solid solution.
3. Aging to develop strengthening precipitates.

This process is used for selected aluminum, nickel, titanium, and other alloy systems.

## 5. Heat-Transfer Considerations

During heat treatment, temperature changes within a component depend on geometry, thermal properties, and boundary conditions.

Thermal diffusivity is:

\[
\alpha=\frac{k}{\rho c_p}
\]

where:
- \(\alpha\) = thermal diffusivity, m²/s.
- \(k\) = thermal conductivity, W/(m·K).
- \(\rho\) = density, kg/m³.
- \(c_p\) = specific heat capacity, J/(kg·K).

A characteristic thermal diffusion time is approximately:

\[
t_c\sim\frac{L^2}{\alpha}
\]

where \(L\) is a characteristic length, m.

This is a scaling estimate, not a complete furnace or quenching model. Actual temperature fields depend on convection, radiation, phase changes, and component geometry.

## 6. Surface Hardening and Case Hardening

### 6.1 Carburizing

Carburizing introduces carbon into the surface of suitable steels at elevated temperatures. The enriched surface can subsequently be hardened through an appropriate heat treatment.

The objective is commonly a hard wear-resistant case combined with a tougher core.

### 6.2 Nitriding

Nitriding introduces nitrogen into the surface of suitable alloys. It can create hard surface compounds and diffusion zones without requiring the same transformation route as conventional carburizing and quenching.

Process temperature, alloy composition, compound-layer control, and dimensional stability are important.

### 6.3 Induction hardening

Induction heating rapidly heats a surface region through electromagnetic coupling. Subsequent quenching transforms the heated region in suitable steels.

The hardened depth depends on frequency, power, heating time, geometry, material properties, and quenching conditions.

### 6.4 Flame hardening

A flame heats a localized surface region, followed by quenching. It can be useful for selected large steel components, but process uniformity and distortion must be managed.

## 7. Coatings and Surface Treatments

Surface engineering also includes processes that deposit, convert, or modify a surface.

Examples include:
- Physical vapor deposition (PVD).
- Chemical vapor deposition (CVD).
- Thermal spraying.
- Electroplating.
- Anodizing.
- Conversion coatings.
- Shot peening.
- Laser surface treatment.
- Polishing and grinding.

PVD and CVD can create functional thin films, while thermal spraying deposits thicker coating systems. Anodizing modifies the surface of suitable metals through an electrochemical process.

Shot peening introduces localized plastic deformation that can create compressive residual stresses near the surface. These stresses can improve fatigue performance in suitable applications, but the result depends on material, coverage, intensity, and subsequent processing.

## 8. Wear and Surface Failure

Wear mechanisms include:
- Adhesive wear.
- Abrasive wear.
- Surface fatigue.
- Erosive wear.
- Fretting.
- Tribochemical wear.

The appropriate solution depends on the mechanism. Increasing hardness may help abrasive wear but may not solve lubrication failure, coating delamination, or corrosive wear.

Corrosion is an electrochemical or chemical degradation process. Surface treatments can improve protection, but coating defects, galvanic interactions, and environmental exposure must be considered.

## 9. Hardness and Case Depth

Hardness testing estimates resistance to localized indentation. Common methods include Rockwell, Vickers, and Brinell testing.

Hardness is not identical to tensile strength, fracture toughness, or fatigue life. Correlations between hardness and strength are material-dependent.

Case depth can be defined by different conventions, including effective case depth based on a specified hardness threshold. The relevant definition must be taken from the applicable specification or standard.

### Numerical Example 1: Diffusion distance

A simplified diffusion-length estimate is:

\[
x\sim\sqrt{Dt}
\]

Assume an effective diffusion coefficient of \(2.0\times10^{-11}\text{ m}^2/\text{s}\) and a process time of 4 hours.

Convert time:

\[
t=4(3600)=14{,}400\text{ s}
\]

Calculate:

\[
x\sim\sqrt{(2.0\times10^{-11})(14{,}400)}
\]

\[
x\sim\sqrt{2.88\times10^{-7}}
\]

\[
x\sim5.37\times10^{-4}\text{ m}
\]

\[
x\sim0.537\text{ mm}
\]

**Answer:** The characteristic diffusion distance is approximately 0.54 mm.

This is a scaling estimate, not a guaranteed case depth. A real concentration profile requires appropriate boundary conditions, concentration-dependent properties where relevant, and process-specific data.

## 10. Residual Stress and Distortion

Residual stress remains after external forces or thermal gradients are removed. It can result from:
- Nonuniform cooling.
- Phase transformations.
- Plastic deformation.
- Coating deposition.
- Machining.
- Welding.
- Shot peening.

Residual stress can improve or reduce component performance depending on its magnitude, distribution, and direction.

Heat treatment may relieve some stresses but can also create new stresses or distortion. Process sequence is therefore important.

## 11. Process Selection

| Objective | Possible processes | Key considerations |
|---|---|---|
| Through-hardening | Quenching and tempering | Section size, hardenability, distortion |
| Hard surface with tougher core | Carburizing or other case-hardening route | Case depth, core properties, fatigue |
| Surface nitrogen enrichment | Nitriding | Alloy suitability, compound layer, dimensions |
| Localized hardening | Induction or flame hardening | Geometry, hardened depth, repeatability |
| Thin wear-resistant film | PVD or CVD | Adhesion, substrate temperature, coating thickness |
| Corrosion protection | Appropriate coatings or conversion treatments | Environment, defects, galvanic effects |
| Fatigue improvement | Shot peening or other validated surface treatment | Residual stress, surface integrity, service conditions |

## 12. Industrial R&D and Process Optimization

Useful R&D activities include:
- Hardness mapping.
- Metallographic examination.
- X-ray diffraction residual-stress measurements.
- Wear testing.
- Corrosion testing.
- Coating adhesion testing.
- Heat-transfer simulation.
- Transformation modeling.
- Design of experiments for time-temperature optimization.
- Automated inspection and furnace-data analytics.

Process validation should connect treatment parameters to measurable outcomes such as hardness profile, case depth, dimensional change, fatigue life, or corrosion performance.

## 13. Common Misconceptions

- Hardness and toughness mean the same thing.
- The hardest possible surface is always best.
- Every steel can be hardened using the same quench.
- Heat treatment produces no dimensional change.
- A coating eliminates every corrosion risk.
- Higher treatment temperature always improves properties.
- Diffusion distance is exactly equal to case depth.
- Surface compressive stress guarantees unlimited fatigue life.

## 14. Summary

Heat treatment controls microstructure through thermal history, phase transformation, and diffusion. Surface engineering targets the properties of the near-surface region through hardening, coatings, and mechanical or chemical modification. Treatment selection must balance hardness, toughness, fatigue, wear, corrosion, dimensional stability, and cost. Reliable production requires material-specific procedures, measurement, and validation.

## 15. Review Questions

1. Distinguish annealing, normalizing, quenching, and tempering.
2. Why is tempering often performed after hardening steel?
3. Explain the Arrhenius relationship for diffusion.
4. Why can rapid quenching produce cracking?
5. Compare carburizing and nitriding.
6. How does induction hardening differ from through-hardening?
7. Why is hardness not a complete measure of component reliability?
8. Explain how residual stress can influence fatigue.
9. Compare PVD and thermal spraying.
10. Design an experiment to optimize case depth while limiting distortion.

## 16. Challenging Exercises with Solutions

### Exercise 1: Diffusion distance

Given \(D=5.0\times10^{-12}\text{ m}^2/\text{s}\) and \(t=10{,}000\text{ s}\), estimate the diffusion distance using \(x\sim\sqrt{Dt}\).

**Solution**

\[
x\sim\sqrt{(5.0\times10^{-12})(10{,}000)}
\]

\[
x\sim\sqrt{5.0\times10^{-8}}
\]

\[
x\sim2.24\times10^{-4}\text{ m}
\]

\[
x\sim0.224\text{ mm}
\]

**Answer:** Approximately 0.224 mm.

### Exercise 2: Thermal diffusivity

A material has \(k=45\text{ W/(m·K)}\), \(\rho=7800\text{ kg/m}^3\), and \(c_p=500\text{ J/(kg·K)}\). Calculate thermal diffusivity.

**Solution**

\[
\alpha=\frac{k}{\rho c_p}
\]

\[
\alpha=\frac{45}{7800(500)}
\]

\[
\alpha=\frac{45}{3{,}900{,}000}
\]

\[
\alpha\approx1.15\times10^{-5}\text{ m}^2/\text{s}
\]

**Answer:** Approximately \(1.15\times10^{-5}\text{ m}^2/\text{s}\).

### Exercise 3: Characteristic thermal time

Using the diffusivity from Exercise 2, estimate \(t_c\sim L^2/\alpha\) for \(L=0.02\text{ m}\).

**Solution**

\[
t_c\sim\frac{(0.02)^2}{1.15\times10^{-5}}
\]

\[
t_c\sim\frac{0.0004}{1.15\times10^{-5}}
\]

\[
t_c\sim34.8\text{ s}
\]

**Answer:** Approximately 35 seconds as a characteristic scaling time.

### Exercise 4: Coating material volume

A component has a coated surface area of \(0.15\text{ m}^2\). The coating thickness is \(80\ \mu\text{m}\). Estimate coating volume.

**Solution**

Convert thickness:

\[
t=80\times10^{-6}\text{ m}
\]

For a uniform thin coating:

\[
V=At
\]

\[
V=0.15(80\times10^{-6})
\]

\[
V=1.2\times10^{-5}\text{ m}^3
\]

Convert to cm³:

\[
1.2\times10^{-5}\text{ m}^3=12\text{ cm}^3
\]

**Answer:** Approximately 12 cm³, assuming uniform thickness and negligible geometric complications.

### Exercise 5: Heat-treatment cost comparison

Process A costs \$600 per batch plus \$4 per component. Process B costs \$200 per batch plus \$7 per component. Calculate the break-even batch quantity.

**Solution**

\[
C_A=600+4N
\]

\[
C_B=200+7N
\]

Set equal:

\[
600+4N=200+7N
\]

\[
400=3N
\]

\[
N=133.33
\]

**Answer:** The continuous break-even point is approximately 133.33 components. Process B is cheaper at 133 components or fewer under the stated cost model; Process A is cheaper at 134 components or more.

## 17. Glossary

- **Annealing:** Heat treatment designed to achieve a specified material condition.
- **Austenite:** Face-centered cubic iron-rich phase in suitable steels.
- **Case hardening:** Creating a hardened surface region while retaining different properties in the core.
- **Diffusion:** Atomic transport through material.
- **Hardness:** Resistance to localized indentation or deformation under a specified test.
- **Heat-affected zone:** Material region altered by thermal exposure without necessarily melting.
- **Martensite:** Transformation product that can provide high hardness in suitable steels.
- **Nitriding:** Surface treatment introducing nitrogen into suitable alloys.
- **Precipitation hardening:** Strengthening through controlled formation of fine precipitates.
- **Quenching:** Controlled rapid cooling to obtain a desired transformation or property state.
- **Residual stress:** Stress remaining without external loading.
- **Tempering:** Heat treatment applied to previously hardened material to adjust its properties.

## 18. References and Further Learning

1. [ASM International](https://www.asminternational.org/) — heat treatment, metallurgy, coatings, and failure analysis.
2. [NIST](https://www.nist.gov/) — materials measurement and manufacturing research.
3. [TWI](https://www.twi-global.com/) — surface engineering, welding, and materials technology.
4. [ASTM International](https://www.astm.org/) — relevant hardness, coating, and materials-testing standards.
5. [ISO Standards](https://www.iso.org/standards.html) — international standards for heat treatment and surface engineering.
6. Callister, W. D., and Rethwisch, D. G. *Materials Science and Engineering: An Introduction*.
7. Totten, G. E., editor. *Steel Heat Treatment: Metallurgy and Technologies*.

This is a custom instructional module, not an official MIT syllabus. Numerical estimates are simplified and should not replace material-specific process specifications.