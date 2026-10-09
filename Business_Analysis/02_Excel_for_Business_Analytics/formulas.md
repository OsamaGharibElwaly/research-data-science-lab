# Excel Formulas and Functions for Business Analytics

## 1. Formula Basics

Excel formulas begin with `=`.

Examples:

```excel
=A2+B2
=C2*D2
=SUM(E2:E20)
```

Common operators:

| Operator | Meaning                  |
| -------- | ------------------------ |
| `+`      | Addition                 |
| `-`      | Subtraction              |
| `*`      | Multiplication           |
| `/`      | Division                 |
| `^`      | Exponentiation           |
| `=`      | Equal to                 |
| `<>`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

Use parentheses when they improve clarity or control calculation order.

## 2. Relative and Absolute References

A relative reference changes when a formula is copied.

```excel
=A2*B2
```

An absolute reference remains fixed.

```excel
=A2*$H$1
```

If cell `H1` contains a tax rate, `$H$1` keeps the reference fixed when copying the formula down.

A mixed reference fixes only one part:

* `$A2` fixes the column.
* `A$2` fixes the row.

## 3. Arithmetic and Summary Functions

Assume the dataset has these columns:

| Column | Field        |
| ------ | ------------ |
| A      | OrderID      |
| B      | Region       |
| C      | Category     |
| D      | Quantity     |
| E      | UnitPrice    |
| F      | UnitCost     |
| G      | DiscountRate |

### Revenue

```excel
=D2*E2
```

If discount is applied to the selling price:

```excel
=D2*E2*(1-G2)
```

### Total Revenue

```excel
=SUM(H2:H100)
```

### Average Revenue per Line

```excel
=AVERAGE(H2:H100)
```

### Highest Revenue

```excel
=MAX(H2:H100)
```

### Lowest Revenue

```excel
=MIN(H2:H100)
```

### Number of Numeric Entries

```excel
=COUNT(H2:H100)
```

### Number of Non-Empty Cells

```excel
=COUNTA(A2:A100)
```

`COUNT` counts numeric cells. `COUNTA` counts non-empty cells.

## 4. Conditional Functions

### IF

Returns one result when a condition is true and another when it is false.

```excel
=IF(H2>=500,"High Value","Standard")
```

### AND

Returns `TRUE` when all specified conditions are true.

```excel
=AND(B2="North",H2>=500)
```

### OR

Returns `TRUE` when at least one condition is true.

```excel
=OR(B2="North",B2="South")
```

### Combining IF and AND

```excel
=IF(AND(H2>=500,I2>0),"Review","Normal")
```

Here, `H2` is revenue and `I2` is profit.

## 5. Conditional Aggregation

### SUMIF

Adds values that satisfy one condition.

```excel
=SUMIF(B2:B100,"North",H2:H100)
```

This calculates revenue for the North region.

### SUMIFS

Adds values that satisfy multiple conditions.

```excel
=SUMIFS(H2:H100,B2:B100,"North",C2:C100,"Technology")
```

This calculates revenue for Technology in the North region.

### COUNTIF

Counts cells satisfying one condition.

```excel
=COUNTIF(B2:B100,"North")
```

### COUNTIFS

Counts records satisfying multiple conditions.

```excel
=COUNTIFS(B2:B100,"North",C2:C100,"Technology")
```

### AVERAGEIF

Calculates an average for records meeting one condition.

```excel
=AVERAGEIF(B2:B100,"North",H2:H100)
```

### AVERAGEIFS

Calculates an average for records meeting multiple conditions.

```excel
=AVERAGEIFS(H2:H100,B2:B100,"North",C2:C100,"Technology")
```

## 6. Lookup Functions

Lookup functions retrieve information associated with a key.

Suppose a product reference table contains product codes in column `A` and categories in column `B`.

### XLOOKUP

```excel
=XLOOKUP(J2,$A$2:$A$20,$B$2:$B$20,"Not Found")
```

The formula searches for the value in `J2`, finds it in the product-code range, and returns the corresponding category.

`XLOOKUP` is not available in every older version of Excel.

### VLOOKUP Alternative

```excel
=IFERROR(VLOOKUP(J2,$A$2:$B$20,2,FALSE),"Not Found")
```

`FALSE` requests an exact match.

## 7. Error Handling

### IFERROR

```excel
=IFERROR(I2/H2,0)
```

This returns zero when the division produces an error.

However, replacing every error with zero can hide data problems. Use it only when zero is a justified business treatment.

For a profit margin, a blank result may be more appropriate when revenue is zero:

```excel
=IF(H2=0,"",I2/H2)
```

## 8. Text Functions

### TRIM

Removes extra spaces from text.

```excel
=TRIM(B2)
```

### UPPER and LOWER

```excel
=UPPER(B2)
=LOWER(B2)
```

### LEFT and RIGHT

```excel
=LEFT(A2,3)
=RIGHT(A2,4)
```

These functions can help extract parts of identifiers, provided the identifier format is consistent.

## 9. Date Functions

If `A2` contains a valid Excel date:

```excel
=YEAR(A2)
=MONTH(A2)
=DAY(A2)
```

To return the first day of the month:

```excel
=DATE(YEAR(A2),MONTH(A2),1)
```

This can be useful for grouping transactions into calendar months.

## 10. Percentage Calculations

### Percentage Contribution

```excel
=CategoryRevenue/TotalRevenue
```

For example:

```excel
=H2/$H$101
```

If `H101` contains the total revenue, the absolute reference preserves the total cell when the formula is copied.

### Percentage Change

```excel
=(CurrentPeriod-PreviousPeriod)/PreviousPeriod
```

A previous-period value of zero requires special treatment because the percentage change is undefined.

## 11. Recommended Calculated Columns

For a retail dataset, useful calculated fields include:

| Field           | Formula                                  |
| --------------- | ---------------------------------------- |
| Gross Sales     | `=Quantity*UnitPrice`                    |
| Discount Amount | `=GrossSales*DiscountRate`               |
| Net Revenue     | `=GrossSales-DiscountAmount`             |
| Total Cost      | `=Quantity*UnitCost`                     |
| Profit          | `=NetRevenue-TotalCost`                  |
| Profit Margin   | `=IF(NetRevenue=0,"",Profit/NetRevenue)` |

The exact definitions must match the organization's accounting and reporting rules.

## 12. Common Formula Errors

| Problem                   | Likely Cause                          | Recommended Check                   |
| ------------------------- | ------------------------------------- | ----------------------------------- |
| `#DIV/0!`                 | Division by zero or blank denominator | Check the denominator               |
| `#N/A`                    | Lookup value not found                | Check keys, spaces, and data types  |
| `#VALUE!`                 | Incompatible data types               | Check text and numeric values       |
| Incorrect total           | Wrong range or duplicate records      | Verify the range and source         |
| Unexpected formula result | Relative reference shifted            | Check cell references               |
| Formula shown as text     | Cell formatted as text or missing `=` | Check formatting and formula syntax |

## Practice

1. Calculate net revenue using quantity, unit price, and discount rate.
2. Calculate total profit.
3. Calculate revenue for the North region.
4. Count orders in the South region.
5. Calculate revenue for Technology in the North region.
6. Create a label for records with revenue of at least 500.
7. Calculate profit margin while avoiding division by zero.
8. Use a lookup function to retrieve a product category.
