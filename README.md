# GitHub Actions CI/CD: Python Data Engineering Pipeline

This project demonstrates a working **CI/CD pipeline** using **GitHub Actions** for a simple but realistic data engineering workflow.

---

## ✅ Features

- Python function: Celsius to Fahrenheit conversion (basic example)
- Data pipeline: Cleans raw weather data from a CSV file
- **CI (Continuous Integration)**:
  - Linting with `flake8`
  - Unit tests with `pytest`
- **CD (Continuous Deployment)**:
  - Runs the data transformation script after successful tests

---

## 🧪 Tech Stack

- Python 3.10
- `pytest`
- `flake8`
- `pandas`
- GitHub Actions (CI/CD)

---

## 🚀 Pipeline Overview

The CI/CD pipeline runs on every push and includes:

1. Checkout the code
2. Set up Python 3.10
3. Install dependencies
4. Lint the code with `flake8`
5. Run tests with `pytest`
6. **Deploy**: Run `transform.py` to clean raw CSV data

---

## 📂 Files

| File                  | Purpose                          |
|-----------------------|----------------------------------|
| `main.py`             | Simple Celsius→Fahrenheit logic |
| `test_main.py`        | Unit test for the function       |
| `transform.py`        | Data pipeline (ETL logic)        |
| `test_transform.py`   | Unit test for transformation     |
| `weather.csv`         | Sample input file                |
| `cleaned_weather.csv` | Output written during CD         |
| `.github/workflows/ci.yml` | CI/CD workflow config      |

---


