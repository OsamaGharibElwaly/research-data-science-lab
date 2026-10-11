
# Module 07: Additive Manufacturing and 3D Printing

## 1. Learning Objectives

After completing this module, you should be able to:

- Explain additive manufacturing from first principles.
- Compare powder-bed fusion, directed energy deposition, material extrusion, vat photopolymerization, binder jetting, and material jetting.
- Distinguish additive manufacturing from conventional subtractive and formative processes.
- Explain the effects of layer thickness, scan speed, energy input, build orientation, and support structures.
- Estimate build time, material utilization, and energy-related quantities.
- Understand porosity, anisotropy, residual stress, warpage, and surface roughness.
- Explain post-processing, inspection, qualification, and process monitoring.
- Apply design-for-additive-manufacturing principles.
- Connect additive manufacturing to industrial R&D, topology optimization, automation, and digital engineering.

## 2. Introduction and Scope

Additive manufacturing (AM) creates three-dimensional objects by adding material according to digital geometry, usually in successive layers or controlled deposition paths.

The process begins with a digital model, followed by preparation of build data, machine setup, material deposition or consolidation, and post-processing.

Unlike machining, AM can reduce the need for dedicated tooling and enable complex internal channels, lattice structures, and customized geometries. However, build rate, material cost, surface finish, dimensional accuracy, defect control, and qualification can limit its economic suitability.

Applications include:
- Aerospace brackets, ducts, and selected engine components.
- Automotive prototypes, tooling, and selected production parts.
- Customized medical implants and anatomical models.
- Dental products.
- Electronic housings and thermal-management components.
- Industrial spare parts and repair operations.

Not every 3D-printing process produces the same material properties. A polymer extrusion printer and a laser powder-bed fusion system have fundamentally different process physics and quality requirements.

## 3. The Digital Manufacturing Workflow

A typical workflow is:

1. Create or acquire CAD geometry.
2. Check geometry and repair model errors.
3. Select the manufacturing process and material.
4. Orient the component within the build volume.
5. Generate supports if required.
6. Slice the geometry into layers or generate deposition paths.
7. Configure machine and process parameters.
8. Execute the build.
9. Remove the component and supports.
10. Apply post-processing.
11. Inspect and validate the component.
12. Record traceability and process data.

Errors in the digital model can propagate into production. Important checks include units, surface closure, wall thickness, orientation, build-envelope limits, and feature resolution.

## 4. Major Additive Manufacturing Process Families

### 4.1 Material extrusion

Material extrusion deposits material through a nozzle or comparable extrusion mechanism.

Fused filament fabrication (FFF), often called fused deposition modeling in commercial contexts, is a widely used polymer implementation.

The material is heated and deposited along a programmed path. Adjacent roads and layers must bond sufficiently to produce the required properties.

Important parameters:
- Nozzle temperature.
- Build-plate temperature.
- Deposition speed.
- Layer height.
- Road width.
- Infill pattern and density.
- Cooling rate.
- Build orientation.

Common limitations include visible layer lines, anisotropic strength, voids between roads, and sensitivity to thermal history.

### 4.2 Vat photopolymerization

Vat photopolymerization selectively cures liquid photopolymer resin using light.

Stereolithography (SLA) and digital light processing (DLP) are common implementations.

Advantages include fine feature capability and good surface detail for suitable materials.

Limitations include resin handling, support requirements, post-curing, aging behavior, and restrictions on long-term thermal or mechanical performance for some resins.

### 4.3 Powder-bed fusion

Powder-bed fusion selectively fuses or melts regions of a powder bed using an energy source.

Examples include:
- Laser powder-bed fusion for metals.
- Electron beam powder-bed fusion for suitable conductive metal powders.
- Polymer powder-bed fusion processes such as selective laser sintering.

Process details differ substantially across materials and equipment.

Metal powder-bed fusion can create complex geometry, but it requires control of powder condition, atmosphere, thermal gradients, scan strategy, and residual stress.

### 4.4 Directed energy deposition

Directed energy deposition (DED) introduces feedstock into a localized energy source that melts or bonds the material as it is deposited.

Feedstock may be wire or powder, depending on the process.

Applications include:
- Repair of selected high-value components.
- Adding material to existing parts.
- Large metal structures.
- Functionally graded or multi-material research.

DED often requires finishing machining and careful control of dilution, geometry, thermal cycles, and deposition stability.

### 4.5 Binder jetting

Binder jetting selectively deposits a binder into a powder bed. The resulting green part commonly requires subsequent curing, depowdering, sintering, infiltration, or other processing depending on the material system.

It can support high-throughput production for suitable applications, but shrinkage, dimensional control, density, and final mechanical properties depend on the complete process route.

### 4.6 Material jetting

Material jetting deposits droplets of build material that are subsequently solidified or cured.

It is useful for selected detailed polymer parts and multi-material visual prototypes. Material properties, aging, and long-term structural performance must be evaluated for the intended application.

### 4.7 Sheet lamination

Sheet lamination bonds successive sheets or layers of material and then creates the desired geometry through cutting or related operations.

Its suitability depends on the material system, bonding mechanism, geometry, and required properties.

## 5. Comparison of AM Processes

| Process | Feedstock | Main mechanism | Typical strengths | Important limitations |
|---|---|---|---|---|
| Material extrusion | Filament, pellets, or other extrudable feedstock | Deposition through a nozzle | Accessible equipment and material flexibility | Layer bonding and anisotropy |
| Vat photopolymerization | Liquid photopolymer | Light-induced curing | Fine details and surface quality | Resin properties and post-curing |
| Metal powder-bed fusion | Metal powder | Localized melting or fusion | Complex metal geometry | Residual stress, powder handling, and cost |
| Polymer powder-bed fusion | Polymer powder | Thermal fusion or sintering | Complex parts with reduced support requirements in suitable systems | Powder aging, roughness, and thermal management |
| Directed energy deposition | Wire or powder | Localized energy-assisted deposition | Repair and larger deposits | Finishing needs and geometric control |
| Binder jetting | Powder and liquid binder | Selective binding followed by downstream processing | Potentially productive powder-based manufacturing | Shrinkage and downstream densification |
| Material jetting | Liquid droplets | Droplet deposition and solidification | Fine details and selected multi-material parts | Material limitations and aging |
| Sheet lamination | Sheets or layers | Bonding and contour formation | Certain layered and hybrid constructions | Bond integrity and geometric constraints |

## 6. Layer Thickness and Build Time

In many layer-based processes, thinner layers increase vertical resolution but require more layers.

A simplified estimate of layer count is:

\[
N_L=\frac{H}{t_L}
\]

where:
- \(N_L\) = number of layers, dimensionless.
- \(H\) = build height, mm.
- \(t_L\) = layer thickness, mm.

The result should be rounded up to an integer when calculating an actual build.

A simplified time estimate is:

\[
t_{\text{build}}\approx N_Lt_{\text{layer}}
\]

where:
- \(t_{\text{build}}\) = estimated build time.
- \(t_{\text{layer}}\) = average time per layer.

Real build time also depends on scanning or deposition path length, recoating, platform movement, heating, cooling, support structures, and machine-specific operations.

### Numerical Example 1: Layer count

A component has a build height of 60 mm and layer thickness of 0.15 mm.

\[
N_L=\frac{60}{0.15}=400
\]

If the average layer time is 25 seconds:

\[
t_{\text{build}}=400(25)=10{,}000\text{ s}
\]

Convert to hours:

\[
t_{\text{build}}=\frac{10{,}000}{3600}\approx2.78\text{ h}
\]

**Answer:** Approximately 400 layers and 2.78 hours under the simplified model.

The estimate excludes setup, warm-up, cooling, removal, and post-processing.

## 7. Energy Input in Metal Additive Manufacturing

Energy input is often analyzed alongside material feed rate, scan speed, hatch spacing, and layer thickness.

For some laser powder-bed fusion studies, a volumetric energy density indicator is used:

\[
E_v=\frac{P}{vht}
\]

where:
- \(E_v\) = nominal volumetric energy density, J/mm³.
- \(P\) = laser power, W or J/s.
- \(v\) = scan speed, mm/s.
- \(h\) = hatch spacing, mm.
- \(t\) = layer thickness, mm.

Because:

\[
\frac{\text{J/s}}{(\text{mm/s})(\text{mm})(\text{mm})}
=\frac{\text{J}}{\text{mm}^3}
\]

the units are consistent.

This metric is useful for comparing selected parameter combinations, but it does not uniquely determine part quality. Two parameter sets with equal nominal energy density can produce different melt pools, defects, and microstructures.

### Numerical Example 2: Nominal energy density

Assume:
- \(P=200\text{ W}\).
- \(v=800\text{ mm/s}\).
- \(h=0.10\text{ mm}\).
- \(t=0.04\text{ mm}\).

Then:

\[
E_v=\frac{200}{800(0.10)(0.04)}
\]

\[
E_v=\frac{200}{3.2}=62.5\text{ J/mm}^3
\]

**Answer:** The nominal volumetric energy density is 62.5 J/mm³.

This is a process indicator, not a universal optimum. Appropriate settings must be developed for the machine, alloy, powder condition, and target properties.

## 8. Material Utilization

Material utilization compares material retained in the finished part with material consumed by the manufacturing process.

A simplified definition is:

\[
\eta_m=\frac{m_{\text{part}}}{m_{\text{input}}}\times100\%
\]

where:
- \(\eta_m\) = material utilization, %.
- \(m_{\text{part}}\) = mass retained in the part, kg.
- \(m_{\text{input}}\) = mass consumed or allocated under a defined accounting boundary, kg.

### Numerical Example 3: Material utilization

A build consumes 2.0 kg of allocated feedstock and produces 1.4 kg of finished components.

\[
\eta_m=\frac{1.4}{2.0}\times100\%=70\%
\]

**Answer:** Material utilization is 70% under the specified accounting boundary.

Unused powder may be reusable in qualified processes. Its condition, handling history, and applicable reuse limits must be considered before counting it as fully recoverable material.

## 9. Thermal History, Microstructure, and Anisotropy

Layer-based processes impose repeated heating and cooling cycles.

In metal AM, the thermal history affects:
- Grain morphology.
- Phase transformations.
- Precipitation.
- Residual stress.
- Distortion.
- Porosity.
- Mechanical properties.

Rapid solidification can create fine microstructural features, but the final properties depend on alloy chemistry, heat treatment, local cooling rates, and process conditions.

In polymer extrusion, adjacent deposited roads must bond through interfacial contact and molecular mobility. If the interface does not develop sufficient bonding, the component may be weaker across layer boundaries.

Build orientation therefore affects mechanical behavior, surface finish, support requirements, and dimensional accuracy.

## 10. Common AM Defects

| Defect | Possible mechanism | Potential response |
|---|---|---|
| Lack-of-fusion porosity | Insufficient or poorly distributed energy, overlap, or material contact | Optimize process parameters and validate melt-pool behavior |
| Gas porosity | Entrapped gas or feedstock-related effects | Improve feedstock control and process conditions |
| Keyhole porosity | Unstable deep melt-pool behavior under some conditions | Adjust energy delivery and scan strategy |
| Warpage | Residual stress and nonuniform thermal contraction | Optimize orientation, supports, thermal conditions, and stress relief |
| Cracking | Thermal stress, material sensitivity, or unsuitable processing | Review alloy, preheating, process parameters, and heat treatment |
| Surface roughness | Layer stair-stepping, particles, or deposition behavior | Change orientation, parameters, or finishing strategy |
| Delamination | Insufficient interlayer bonding | Improve interface formation and thermal conditions |
| Dimensional error | Shrinkage, distortion, machine calibration, or scan strategy | Calibrate and compensate using validated data |
| Support failure | Inadequate support geometry or excessive process loads | Improve support design and build orientation |
| Polymer warpage | Differential shrinkage and cooling | Improve thermal control and geometry |

Defect names do not uniquely identify their causes. Confirm suspected mechanisms through appropriate inspection and experimentation.

## 11. Post-Processing and Qualification

Post-processing can be essential for achieving final properties and dimensions.

Depending on the process, it may include:
- Support removal.
- Stress-relief heat treatment.
- Hot isostatic pressing.
- Machining.
- Grinding or polishing.
- Chemical or abrasive finishing.
- Surface coating.
- Cleaning and depowdering.
- Resin washing and post-curing.
- Infiltration or sintering.

Hot isostatic pressing (HIP) combines elevated temperature and isostatic gas pressure to reduce certain internal defects in suitable materials. It does not automatically correct every defect or guarantee complete restoration of fatigue performance.

Qualification should address material, machine, process settings, geometry, inspection, traceability, and application-specific requirements.

## 12. Design for Additive Manufacturing

DFAM exploits capabilities of additive processes while respecting their limitations.

Useful principles include:
- Consolidate assemblies when doing so improves function and reliability.
- Consider topology optimization for structural efficiency.
- Design internal channels with cleaning and inspection in mind.
- Minimize unnecessary supports.
- Account for orientation-dependent properties.
- Consider overhangs, minimum feature size, and wall thickness.
- Provide machining allowance on critical surfaces.
- Include access for powder removal.
- Avoid enclosed cavities that trap unused material.
- Evaluate support-removal access and finishing requirements.

A geometry that can be printed is not necessarily economical, inspectable, certifiable, or safe for service.

## 13. Economics and Process Selection

Total AM cost may include:
- Feedstock.
- Machine depreciation.
- Machine operating time.
- Labor and supervision.
- Setup and build preparation.
- Support material.
- Post-processing.
- Inspection and qualification.
- Failed builds and scrap.
- Energy and facility requirements.

AM can be attractive for low-volume production, complex geometry, customization, or repair. Conventional processes may remain preferable for high-volume simple components.

A fair comparison should consider the complete manufacturing route, not merely the price of the printing operation.

## 14. Industrial R&D, Automation, and Digital Twins

Potential research directions include:
- Melt-pool imaging.
- Thermal-camera monitoring.
- Acoustic sensing.
- In-situ defect detection.
- Process-parameter optimization.
- Machine-learning-assisted quality prediction.
- Topology optimization.
- Automated build planning.
- Digital twins.
- Qualification and traceability systems.

A robust study should use ground-truth inspection data, account for differences among machines and material batches, and test whether predictions generalize to new production conditions.

## 15. Common Misconceptions

- All 3D-printed parts have inferior mechanical properties to conventional parts.
- Higher energy density always improves quality.
- A successful prototype proves production readiness.
- Additive manufacturing eliminates all material waste.
- Every printed metal part requires the same heat treatment.
- Layer thickness alone determines build quality.
- Complex geometry is always cheaper to print than to machine.
- A visually acceptable part is necessarily free of internal defects.

## 16. Summary

Additive manufacturing creates components by controlled material addition using digital models. Process families differ in feedstock, energy source, bonding mechanism, accuracy, and material behavior. Layer thickness, orientation, thermal history, and process parameters influence productivity and quality. Defects such as porosity, cracking, warpage, and poor interlayer bonding require process-specific control. Industrial success depends on validated manufacturing parameters, suitable post-processing, inspection, qualification, and realistic total-cost analysis.

## 17. Review Questions

1. How does additive manufacturing differ from subtractive manufacturing?
2. Compare material extrusion, vat photopolymerization, and powder-bed fusion.
3. What information does nominal volumetric energy density provide, and what does it omit?
4. Why can build orientation affect mechanical properties?
5. Explain the difference between lack-of-fusion and gas porosity.
6. Why may post-processing be necessary for metal AM?
7. What is the role of supports?
8. Why is material utilization dependent on the accounting boundary?
9. How can in-situ monitoring contribute to quality assurance?
10. Propose an experimental plan to reduce porosity in a metal AM process.

## 18. Challenging Exercises with Complete Solutions

### Exercise 1: Layer count and build time

A part has a height of 48 mm. The layer thickness is 0.08 mm, and average layer time is 18 seconds. Estimate layer count and build time.

**Solution**

\[
N_L=\frac{48}{0.08}=600
\]

\[
t_{\text{build}}=600(18)=10{,}800\text{ s}
\]

\[
t_{\text{build}}=\frac{10{,}800}{3600}=3.0\text{ h}
\]

**Answer:** 600 layers and approximately 3 hours under the simplified model.

### Exercise 2: Volumetric energy density

A laser operates at 250 W with scan speed 1,000 mm/s, hatch spacing 0.12 mm, and layer thickness 0.05 mm. Calculate nominal volumetric energy density.

**Solution**

\[
E_v=\frac{P}{vht}
\]

\[
E_v=\frac{250}{1000(0.12)(0.05)}
\]

\[
E_v=\frac{250}{6}=41.67\text{ J/mm}^3
\]

**Answer:** Approximately 41.7 J/mm³.

The result is an indicator for the specified process configuration, not proof of acceptable part quality.

### Exercise 3: Material utilization

A polymer printing job allocates 1.5 kg of material and produces 0.9 kg of accepted parts. Calculate material utilization and allocated material per kilogram of accepted product.

**Solution**

Material utilization:

\[
\eta_m=\frac{0.9}{1.5}\times100\%=60\%
\]

Allocated material per kilogram of accepted product:

\[
m_{\text{allocated}}=\frac{1.5}{0.9}
\approx1.67\text{ kg/kg}
\]

**Answer:** Material utilization is 60%, and approximately 1.67 kg of allocated material is consumed per kilogram of accepted product under this accounting method.

### Exercise 4: Build orientation and production time

Orientation A requires 500 layers with an average layer time of 20 seconds. Orientation B requires 400 layers at the same average time. Estimate the build-time reduction as a percentage.

**Solution**

Orientation A:

\[
t_A=500(20)=10{,}000\text{ s}
\]

Orientation B:

\[
t_B=400(20)=8{,}000\text{ s}
\]

Reduction:

\[
\%\text{ reduction}=
\frac{10{,}000-8{,}000}{10{,}000}\times100\%
\]

\[
=20\%
\]

**Answer:** Orientation B reduces the simplified layer-based build time by 20%.

Support requirements, scan paths, thermal effects, and mechanical performance must also be considered before choosing an orientation.

### Exercise 5: AM versus conventional production cost

An AM component costs \$80 per unit plus a one-time setup cost of \$200. A conventional process costs \$25 per unit plus tooling of \$3,000. Ignore maintenance, inspection, and financing. Find the break-even production quantity.

**Solution**

AM total cost:

\[
C_A=200+80N
\]

Conventional total cost:

\[
C_C=3000+25N
\]

At break-even:

\[
200+80N=3000+25N
\]

\[
55N=2800
\]

\[
N=\frac{2800}{55}\approx50.91
\]

Since production quantity is an integer, compare 50 and 51 units.

At 50 units:

\[
C_A=200+80(50)=\$4200
\]

\[
C_C=3000+25(50)=\$4250
\]

At 51 units:

\[
C_A=200+80(51)=\$4280
\]

\[
C_C=3000+25(51)=\$4275
\]

**Answer:** AM is cheaper at 50 units under the stated model, while the conventional process becomes cheaper at 51 units. The continuous break-even point is approximately 50.91 units.

Real comparisons should include finishing, failure rates, inspection, material qualification, and any additional costs omitted here.

## 19. Glossary

- **Additive manufacturing:** Production of components by adding material from digital geometry.
- **Build orientation:** Orientation of a part relative to the manufacturing build axes.
- **Build volume:** Space within which the machine can manufacture parts.
- **DFAM:** Design for Additive Manufacturing.
- **Directed energy deposition:** Process using localized energy to fuse deposited feedstock.
- **Layer thickness:** Nominal vertical increment between layers in a layer-based process.
- **Lack of fusion:** Incomplete bonding or fusion between material regions.
- **Melt pool:** Localized liquid region created by an energy source in a melting process.
- **Powder-bed fusion:** Process that selectively fuses or melts material in a powder bed.
- **Residual stress:** Stress remaining after external loads or imposed thermal conditions are removed.
- **Support structure:** Temporary or sacrificial material supporting a build.
- **Topology optimization:** Computational optimization of material distribution under defined objectives and constraints.
- **Vat photopolymerization:** Selective curing of liquid photopolymer using light.
- **Volumetric energy density:** Nominal energy-per-volume indicator used for selected AM process comparisons.

## 20. References and Further Learning

1. [NIST Additive Manufacturing](https://www.nist.gov/additive-manufacturing) — measurement science and additive manufacturing research.
2. [ASTM International](https://www.astm.org/) — additive manufacturing standards and terminology.
3. [ISO Standards](https://www.iso.org/standards.html) — international standards for additive manufacturing and qualification.
4. [MIT OpenCourseWare](https://ocw.mit.edu/) — engineering fundamentals and materials-related learning.
5. Gibson, I., Rosen, D. W., and Stucker, B. *Additive Manufacturing Technologies*.
6. [America Makes](https://www.americamakes.us/) — additive manufacturing research and industry resources.
7. [Society of Manufacturing Engineers](https://www.sme.org/) — manufacturing engineering resources.

This is a custom instructional module, not an official MIT course syllabus.