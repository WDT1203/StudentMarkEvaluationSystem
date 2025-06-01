# Student Mark Evaluation System

## Overview

This repository provides a Python-based system for evaluating student progression outcomes based on their academic credits. The system allows both students and staff to input module credits, validates the input, determines progression outcomes (such as "Progress", "Trailer", "Retriever", or "Exclude"), and provides summary statistics, including a histogram. The application can also save results to a text file.

## Features

- **User Modes**: Supports both student and staff workflows.
- **Input Validation**: Accepts only valid credit values (0, 20, 40, 60, 80, 100, 120) for pass, defer, and fail.
- **Outcome Calculation**:
  - Progress
  - Progress (module trailer)
  - Do not progress - module retriever
  - Exclude
- **Result Display**: Shows outcomes in the terminal and as lists.
- **Histogram Generation**: Visualizes outcome distribution using a bar chart (with a simple graphics library).
- **File Output**: Saves all results and input credits to a text file.
- **Simple Graphics**: Includes a beginner-friendly object-oriented graphics library for visualizations.

## Getting Started

### Prerequisites

- Python 3.x
- Tkinter (usually included with Python, required for graphics)

### Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/WDT1203/StudentMarkEvaluationSystem.git
   cd StudentMarkEvaluationSystem
   ```

2. **Run the main program:**
   ```bash
   python main.py
   ```

3. **Follow the prompts:**
   - Choose either 'student' or 'staff' mode.
   - Enter pass, defer, and fail credits when prompted. Input values must be in the range: 0, 20, 40, 60, 80, 100, or 120.
   - The system will display the progression outcome and, for staff, generate a histogram and save results to a file.

## File Structure

- `main.py`: Main application logic, input handling, and outcome calculations.
- `graphics.py`: Simple object-oriented graphics library (by John Zelle) used for generating bar charts.

## Example Workflow

1. **Student** enters credits, receives their outcome, and the program exits.
2. **Staff** can enter multiple students' credits, see all outcomes, and view/save a histogram of results.

## Credits

- The graphics library is adapted from John Zelle's work for "Python Programming: An Introduction to Computer Science".
- Programmed by: W.Dumindu Tharushika

## License

- The graphics library is released under the GPL. See http://www.gnu.org/licenses/gpl.html.
- The rest of the code is for educational use.

---

*For questions or suggestions, please open an issue or contact the repository author.*
