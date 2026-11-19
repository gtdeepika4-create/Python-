# Python Programming Assignment 1 — Milk Payment Calculator

**Student:** Deepika Gopu  
**Register Number:** 1911260133  
**Course:** CSA0803 — Python Programming (CO1)

## Project contents
- `task01_analysis.md` — problem analysis, inputs/outputs, constants, validation, assumptions, complexity.
- `task02_types_precision.py` — Python types, arithmetic, float vs Decimal, integer paise.
- `task03_constants_variables.py` — constants, rate card, dynamic typing and swapping.
- `task04_expressions.py` — payment formula and rounding/operator experiments.
- `task05_input_validation.py` — interactive input and validation.
- `task06_functions.py` — payment functions and ten-day total example.
- `milkrate.py` and `Task07_import_example.py` — reusable module and import demonstration.
- `task08_algorithm.md` — pseudocode, flow outline and hand trace.
- `task09_calculator_tests.py` — Decimal payment calculator with validation and test cases.
- `task10_benchmark.py` — performance/precision comparison at 300, 6,000 and 150,000 entries.
- `task11_design_recommendation.py` — JSON rate card creation/load and recommendation demo.
- `Task12_seasonal_design.py` — seasonal rates and bonus threshold adaptation.
- `tests/` — unit tests for the calculator.
- `screenshots/` — place your genuine execution screenshots here.

## Requirements
Python 3.9+ recommended. The project uses only the Python standard library.

## Run
Open a terminal in this folder and run the relevant task, for example:

```bash
python task02_types_precision.py
python task05_input_validation.py
python task09_calculator_tests.py
python -m unittest discover -s tests -v
python task10_benchmark.py
python Task12_seasonal_design.py
```

For Task 7, run both:
```bash
python milkrate.py
python Task07_import_example.py
```

Task 5 is interactive. Try valid and invalid inputs. Do not submit screenshot placeholders as evidence—capture your own terminal output.

## GitHub upload
1. Extract the ZIP.
2. Create/open your GitHub repository.
3. Upload the extracted files/folders (or use Git).
4. Add real execution screenshots into `screenshots/`.
5. Update the GitHub repository link in your assignment document.

## Rounding note
The examples use nearest 0.1 percentage-point steps and, in the Decimal-based calculator, `ROUND_HALF_UP` for cents and step counts. Confirm the cooperative's official rounding policy before real deployment.

## Accuracy note
The source assignment's Task 9 expected amounts for the 'above standard' and 'below standard' cases do not match its own stated formula. This package uses the formula consistently: 10 L at 4.0% fat / 9.0% SNF calculates to ₹335.00, and 5 L at 3.0% fat / 7.5% SNF calculates to ₹125.00. Confirm these discrepancies with your instructor before submission.
