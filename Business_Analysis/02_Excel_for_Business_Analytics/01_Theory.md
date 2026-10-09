# Excel for Business Analytics — Theory

## 1. Introduction

Business analytics uses data to describe performance, investigate problems, and support decisions. Excel provides a flexible environment for performing these tasks.

A good spreadsheet model has four characteristics:

* **Accuracy:** formulas calculate the intended quantities.
* **Transparency:** assumptions and definitions are visible.
* **Reproducibility:** another analyst can repeat the workflow.
* **Decision relevance:** results answer a clearly defined business question.

## 2. Workbook architecture

A professional workbook separates different responsibilities.

| Worksheet     | Purpose                                                    |
| ------------- | ---------------------------------------------------------- |
| Raw_Data      | Preserve the original imported data.                       |
| Clean_Data    | Store standardized, validated records.                     |
| Analysis      | Calculate KPIs, summaries, and intermediate results.       |
| Dashboard     | Present important findings and recommendations.            |
| Documentation | Record definitions, assumptions, sources, and limitations. |

For small assignments, documentation may be included in the README or in a clearly labeled section of the workbook.

Do not overwrite raw data during cleaning. Retaining the original records helps investigate discrepancies and reproduce results.

## 3. Data structure

A typical transactional dataset contains:

* **Records:** rows representing observations.
* **Fields:** columns representing variables.
* **Dimensions:** descriptive attributes such as region, product category, and date.
* **Measures:** numerical values such as revenue, units, and cost.
* **Keys:** identifiers used to recognize records or connect datasets.

### Grain

The grain describes what one row represents.

For example, one order may contain multiple products. If each row represents an order line, counting rows does not necessarily count orders.

Always define the grain before calculating totals or averages.

## 4. Excel Tables

Convert structured source data into an Excel Table using Insert → Table.

Tables provide:

* Automatic expansion when new records are added.
* Built-in sorting and filtering.
* Readable structured references.
* Easier formula maintenance.
* Convenient sources for PivotTables.

Suppose a Table is named `Sales` and includes `Units`, `UnitPrice`, and `DiscountRate`.

A calculated Revenue column can use:

`=[@Units]*[@UnitPrice]*(1-[@DiscountRate])`

Structured references make the calculation easier to interpret than fixed cell coordinates.

## 5. Cell references

Excel has three common reference types.

| Type     | Example    | Behavior when copied         |
| -------- | ---------- | ---------------------------- |
| Relative | A2         | Row and column can change.   |
| Absolute | $A$2       | Row and column remain fixed. |
| Mixed    | $A2 or A$2 | One dimension remains fixed. |

If the tax rate is stored in cell F1 and the pretax price is in B2:

`=B2*(1+$F$1)`

Copying this formula down changes B2 to B3, B4, and so on, while keeping the tax-rate reference fixed.

## 6. Essential formulas

Assume the `Sales` Table contains `Region`, `Category`, `Revenue`, `Cost`, `OrderID`, and `Status`.

| Business requirement                      | Formula                                                       |
| ----------------------------------------- | ------------------------------------------------------------- |
| Total revenue                             | `=SUM(Sales[Revenue])`                                        |
| Total cost                                | `=SUM(Sales[Cost])`                                           |
| Revenue for a selected region in A2       | `=SUMIFS(Sales[Revenue],Sales[Region],A2)`                    |
| Count delayed lines                       | `=COUNTIFS(Sales[Status],"Delayed")`                          |
| Average line revenue for a category in A2 | `=AVERAGEIFS(Sales[Revenue],Sales[Category],A2)`              |
| Label a margin                            | `=IF([@Margin]>=0.3,"High","Review")`                         |
| Lookup a product cost                     | `=XLOOKUP(A2,Products[SKU],Products[UnitCost],"Missing SKU")` |

Formula separators may be commas or semicolons depending on regional settings.

### IF and IFS

`IF` returns one result when a condition is true and another when it is false.

`=IF(B2>=1000,"Target achieved","Below target")`

`IFS` handles multiple conditions:

`=IFS(B2>=10000,"Large",B2>=5000,"Medium",TRUE,"Small")`

Order conditions carefully because the first matching condition determines the result.

### SUMIFS and COUNTIFS

These functions aggregate records meeting one or more conditions.

For example:

`=SUMIFS(Sales[Revenue],Sales[Region],"North",Sales[Category],"Office")`

This calculates revenue for Office products in the North region.

### IFERROR

`IFERROR` handles errors such as a missing lookup result.

`=IFERROR(A2/B2,0)`

Use it only when the fallback is appropriate. Returning zero can hide an underlying data-quality issue, so production workbooks should also expose exceptions.

## 7. Lookup functions

`XLOOKUP` retrieves a corresponding value from a reference table.

`=XLOOKUP([@SKU],Products[SKU],Products[UnitCost],"Missing SKU")`

For older versions of Excel, `INDEX` and `MATCH` can provide an alternative:

`=IFERROR(INDEX(Products[UnitCost],MATCH(A2,Products[SKU],0)),"Missing SKU")`

Check that the lookup key is unique when the business rule expects one result per key. Duplicate reference keys can cause misleading results.

## 8. Data cleaning and validation

Common data-quality problems include:

* Missing identifiers
* Duplicate transactions
* Numbers stored as text
* Inconsistent category spelling
* Invalid dates
* Unexpected negative values
* Unmatched lookup keys

Recommended controls:

1. Preserve a raw-data copy.
2. Check required fields for blanks.
3. Validate dates and numeric ranges.
4. Compare category values against an approved list.
5. Investigate duplicates using the intended record key.
6. Reconcile totals before and after transformations.
7. Document how each issue was treated.

Two identical-looking rows are not necessarily duplicates. They may represent two legitimate transactions.

## 9. Business KPIs

### Revenue

Revenue represents the monetary value of sales according to the business's accounting definition.

A simplified order-line formula is:

`Revenue = Units × Unit Price × (1 − Discount Rate)`

This definition excludes taxes and other adjustments unless explicitly incorporated.

### Gross profit

`Gross Profit = Revenue − Cost of Goods Sold`

Gross profit measures what remains after the defined product costs, before other operating expenses.

### Gross margin

`Gross Margin = Gross Profit / Revenue`

Express the result as a percentage.

If revenue is 10,000 and gross profit is 2,500, gross margin is 25%.

For an overall business margin, divide total gross profit by total revenue. Do not simply average regional percentages when the goal is the overall margin.

### Average order value

`AOV = Total Order Revenue / Number of Distinct Orders`

When the dataset contains multiple order lines, first sum revenue by OrderID and then average the order totals.

Average line revenue and average order value answer different questions.

### Operational rates

A delayed-line rate can be calculated as:

`Delayed-Line Rate = Delayed Lines / Total Eligible Lines`

The denominator must match the business question. A line-level rate is not automatically an order-level rate or a delivery SLA rate.

## 10. PivotTables

PivotTables summarize data by dimensions.

Example:

* Rows: Region
* Columns: Category
* Values: Sum of Revenue

This creates a regional/category revenue summary.

Always confirm whether the Values field uses Sum, Count, or Average. A numeric field may be summarized by Count when Excel interprets its contents as text.

Refresh the PivotTable after updating the source data.

## 11. Visualization

| Business question                       | Recommended chart   |
| --------------------------------------- | ------------------- |
| How has revenue changed over time?      | Line chart          |
| Which region has the highest revenue?   | Bar or column chart |
| How does margin vary by category?       | Bar chart           |
| How are order values distributed?       | Histogram           |
| Are two numerical variables associated? | Scatter plot        |

Use clear titles, units, reporting periods, and data labels where useful.

Avoid decorative 3-D charts and truncated axes that exaggerate differences. Charts can reveal patterns but do not independently prove causation.

## 12. What-If Analysis

Excel offers several tools for scenario analysis.

* **Goal Seek:** find the input required to reach a target output.
* **Scenario Manager:** compare different sets of assumptions.
* **Data Tables:** examine how changing one or two inputs affects an output.

A simplified profit model is:

`Profit = Units × (Price − Variable Cost) − Fixed Cost`

If fixed cost is 1,000 and contribution per unit is 20:

`Break-even Units = 1,000 / 20 = 50`

This assumes constant contribution per unit and fixed costs. Real businesses may face capacity limits, changing costs, and price-sensitive demand.

## 13. Statistical significance and business significance

Statistical significance and business significance are different concepts.

A statistically detectable difference may be too small to matter operationally. Conversely, an economically important difference may be estimated imprecisely when the sample is small.

When reporting comparisons, include:

* Magnitude of the difference
* Sample size
* Relevant uncertainty
* Business context
* Data-collection limitations

Do not interpret observational associations as proof that one variable caused another.

## 14. Spreadsheet auditing and professional practice

Before sharing a workbook:

* Verify the record grain and keys.
* Check missing and invalid values.
* Confirm formulas are consistent down calculated columns.
* Reconcile totals to an independent calculation.
* Refresh PivotTables.
* Document metric definitions and assumptions.
* Label charts and reporting periods.
* Test zero values, missing lookups, and newly added records.
* Record the source and refresh date.
* Make recommendations proportionate to the evidence.

## 15. Common mistakes

1. Counting rows as distinct orders.
2. Averaging percentages without considering their denominators.
3. Copying formulas with incorrect cell references.
4. Hiding data-quality errors with IFERROR.
5. Forgetting to refresh PivotTables.
6. Deleting apparent duplicates without investigation.
7. Treating missing data as zero without justification.
8. Confusing gross profit with net profit.
9. Presenting a percentage without its denominator.
10. Making causal claims from descriptive analysis.

## Conclusion

Excel is most effective when formulas, data quality, business definitions, and communication work together. The objective is not merely to produce a spreadsheet; it is to produce a reliable analytical result that supports a defensible decision.
