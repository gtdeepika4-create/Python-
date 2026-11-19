# Task 1 — Analysis of the Milk Farmer Payment Problem

## Inputs
Farmer ID (text), litres, fat percentage, SNF percentage, shift (Morning/Evening), and entries over a ten-day payment period.

## Outputs
Rate per litre, payment for each valid milk entry, and the ten-day total for one farmer.

## Constants
- Base rate: ₹30.00/L
- Fat adjustment: ₹0.40 for each 0.1% fat step
- SNF adjustment: ₹0.30 for each 0.1% SNF step
- Reference fat: 3.5%; reference SNF: 8.5%
- Valid fat range: 2.0% to 7.0%, inclusive
- Ten-day period; litres cannot be negative

## Validation
ID cannot be blank; shift must be Morning or Evening; litres >= 0; fat in range; SNF > 0 and numeric. Only valid entries count toward totals.

## Assumptions
Farmer ID uniquely identifies a farmer; one farmer may have both shifts; totals are for one farmer and ten days. Rounding rules should be approved.

## Alternative and complexity
Separate variables become repetitive. A list of records and loops are easier to maintain. Processing n entries is O(n). Retaining entries uses O(n) storage; a running total uses O(1) extra space.

## Conclusion
Use named constants, validation, reusable functions and Decimal for money.
