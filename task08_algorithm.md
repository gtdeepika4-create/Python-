# Task 8 — Plan the Algorithm Before Coding

## Steps
Understand inputs/formula/outputs and invalid cases; plan validation and total; implement functions; test against manual calculations.

## Pseudocode
```text
BEGIN
  total = 0
  FOR each of 10 days
    INPUT farmer_id, litres, fat, snf, shift
    IF ID is nonblank AND litres >= 0 AND fat in [2.0, 7.0]
       AND snf > 0 AND shift is Morning or Evening
      fat_steps = ROUND((fat - 3.5) / 0.1)
      snf_steps = ROUND((snf - 8.5) / 0.1)
      rate = 30 + 0.40 * fat_steps + 0.30 * snf_steps
      payment = ROUND(litres * rate, 2)
      DISPLAY payment
      total = total + payment
    ELSE
      DISPLAY invalid entry
    END IF
  END FOR
  DISPLAY total
END
```

## Flow outline
Start → Read entry → Validate → Invalid? show error / Valid? calculate rate & payment → Add total → More entries? loop → Display total → End.

## Hand trace
- 10 L, fat 4.0, SNF 8.0 → rate ₹29.30 → ₹293.00
- 5 L, fat 3.0, SNF 7.0 → rate ₹23.50 → ₹117.50
- 8 L, fat 8.0, SNF 7.0 → invalid (fat out of range)
Valid total = ₹410.50.
