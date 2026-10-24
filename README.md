# Week 2: Student Grade Calculator

## Project Overview
An interactive Python application designed to calculate student grades based on numerical marks (0-100). The program features strict input validation using error handling and a `while` loop, modular functions, and custom motivational feedback messages for each grade bracket.

## Grading Logic
- **A**: 90 - 100 (Outstanding achievement)
- **B**: 80 - 89 (Very Good)
- **C**: 70 - 79 (Good effort)
- **D**: 60 - 69 (Passed)
- **F**: 0 - 59 (Needs Improvement)

## Technical Features
- **Functions**: `calculate_grade()` for grading logic and `get_valid_marks()` for input handling.
- **Conditional Logic**: Multi-branch `if-elif-else` structures.
- **Input Validation**: Uses `while True` and `try-except ValueError` blocks to reject non-numeric inputs and values outside the 0–100 boundary.
- **Formatting**: Python f-strings used for report layout.

## Setup & Execution
1. Ensure Python 3.x is installed.
2. Run the script:
   ```bash
   python grade_calculator.py