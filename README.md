# LabInsight# LabInsight – Diagnostic Report Analysis and Trend Engine

## Project Information

- **Project Name:** LabInsight
- **Project Type:** Python Console-Based Application
- **Project Owner:** Deeksha M
- **Developer:** Deeksha M
- **Programming Language:** Python
- **Data Storage:** CSV File Handling
- **Project Status:** Developed Prototype

## Overview

LabInsight is a Python-based, menu-driven console application designed to simplify laboratory test report analysis. It compares patient test results against predefined reference ranges, identifies abnormal values, generates structured reports, and compares current results with previously stored reports.

The project demonstrates Python programming, modular development, conditional logic, file handling, and CSV-based data persistence.

## Features

- **Reference Range Management:** Maintains predefined reference ranges for common laboratory tests, including gender-specific ranges where applicable.
- **Patient Information Management:** Accepts patient ID, name, and gender.
- **Test Panel Selection:** Supports Complete Blood Count (CBC), Blood Sugar, Lipid Profile, and All Tests.
- **Automated Result Classification:** Categorizes test results as LOW, NORMAL, or HIGH.
- **Report Generation:** Displays structured patient reports with test values, units, reference ranges, and result status.
- **Historical Report Comparison:** Compares current test results with previous reports using patient ID.
- **Patient Report History:** Retrieves previously stored patient reports.
- **CSV-Based Data Storage:** Maintains report records locally for future access.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| CSV | Patient report storage |
| CSV Module | Reading and writing report records |
| OS Module | Directory and file management |
| Datetime Module | Date and report ID generation |

## Project Structure

```text
LabInsight/
│
├── main.py
├── reference_ranges.py
├── analyzer.py
├── report_generator.py
├── history.py
│
└── reports/
    └── patient_reports.csv
```

## Module Description

### 1. main.py
- Controls the main application.
- Displays the menu-driven interface.
- Collects patient information and laboratory test values.
- Coordinates analysis, report generation, and storage.

### 2. reference_ranges.py
- Stores predefined laboratory reference ranges.
- Maintains gender-specific ranges where applicable.
- Organizes laboratory tests into different panels.
- Provides functions to retrieve reference ranges.

### 3. analyzer.py
- Performs laboratory result analysis.
- Compares entered values against predefined reference ranges.
- Classifies results as LOW, NORMAL, or HIGH.

### 4. report_generator.py
- Generates structured patient reports.
- Displays test results and abnormal value indicators.
- Provides comparisons between current and previous reports.

### 5. history.py
- Creates and manages the report storage directory.
- Saves patient reports in CSV format.
- Retrieves previous reports using patient ID.
- Supports historical report comparison.

## How It Works

1. Launch the application.
2. Select an option from the main menu.
3. Enter patient details.
4. Select the required laboratory test panel.
5. Enter the test results.
6. The analysis module compares values with predefined reference ranges.
7. The application classifies each result as LOW, NORMAL, or HIGH.
8. A structured report is generated.
9. The report is saved in a CSV file.
10. Previous reports can be retrieved and compared using patient ID.

## Data Storage

LabInsight uses local CSV file storage instead of a database.

Patient reports are stored at:

`reports/patient_reports.csv`

The CSV file maintains the following fields:

- Patient ID
- Patient Name
- Report ID
- Date
- Test Name
- Test Value
- Unit
- Result Status

The application uses Python's CSV module to append new records and retrieve existing patient reports.

## Installation and Execution

### Prerequisites

- Python 3.x
- Windows, Linux, or macOS
- Command-line terminal

No external Python packages are required for the current implementation.

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
```

### Step 2: Navigate to the Project Directory

```bash
cd LabInsight
```

### Step 3: Run the Application

```bash
python main.py
```

On Windows, you can also use:

```bash
py main.py
```

## Application Menu

```text
==================================================
                 LABINSIGHT
      DIAGNOSTIC REPORT ANALYSIS SYSTEM
==================================================

1. Enter New Patient Report
2. View Previous Patient Reports
3. Exit

==================================================
```

## Sample Result Classification

| Test | Sample Value | Status |
|---|---:|---|
| Hemoglobin | 14.5 g/dL | NORMAL |
| Glucose | 95 mg/dL | NORMAL |
| Platelets | 250 × 10³/uL | NORMAL |
| WBC | 7 × 10³/uL | NORMAL |
| Total Cholesterol | 220 mg/dL | HIGH |

*Sample values and reference ranges are illustrative and intended only for demonstrating the application.*

## Concepts Demonstrated

- Python modular programming
- Functions and dictionaries
- Conditional statements
- Loops and input validation
- File handling
- CSV data processing
- Data persistence
- Date and time handling
- Historical data comparison

## Future Enhancements

- Integration with MySQL or MongoDB.
- Graphical user interface.
- Secure patient authentication and access control.
- PDF report generation.
- More laboratory test categories.
- Graphical visualization of historical trends.
- Configurable, clinically validated reference ranges.

## Limitations

- The current implementation is a console-based prototype.
- Data is stored locally in a CSV file.
- It does not include cloud storage or multi-user access controls.
- Reference ranges are illustrative and are not suitable for clinical diagnosis.
- Result classification is rule-based and does not use Artificial Intelligence or Machine Learning.

## Disclaimer

LabInsight is an educational software project developed to demonstrate automated laboratory result classification and report management. It is not a medical diagnostic system and should not be used to make medical decisions.

## Project Owner & Developer

**Deeksha M**

Project Owner and Developer of LabInsight.

## Conclusion

LabInsight demonstrates how Python can be used to develop a modular application for laboratory report analysis, automated result classification, local data management, and historical report comparison.

---

**Developed by Deeksha M**
