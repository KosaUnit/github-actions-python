# CI Python Demo

This is a simple project that demonstrates a basic Continuous Integration (CI) pipeline using GitHub Actions.

## Features

- Python function: Celsius to Fahrenheit conversion
- Unit tests with `pytest`
- Linting with `flake8`
- Automated CI pipeline using GitHub Actions:
  - Runs on every push
  - Installs dependencies
  - Lints the code
  - Runs all tests

## How to Use

Clone the repo and run locally:

```bash
pip install -r requirements.txt
flake8 .
pytest
