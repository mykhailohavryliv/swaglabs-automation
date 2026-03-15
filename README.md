# SwagLabs Automation

This project contains automated tests for the SwagLabs demo application using Playwright and pytest.

## Setup

1. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install Allure command-line tool:
   ```bash
   brew install allure
   ```

## Running Tests

Run tests with pytest:
```bash
python -m pytest
```

This will generate both HTML report (`report.html`) and Allure results (`allure-results/`).

## Viewing Allure Report

Generate and serve the Allure report:
```bash
allure serve allure-results
```

This will open a browser with the interactive Allure report.

## VS Code Tasks

Use the following tasks in VS Code:
- **Run Tests with Allure**: Runs the test suite
- **Generate Allure Report**: Generates and serves the Allure report (depends on running tests first)

## Test Structure

- `tests/`: Test files
- `pages/`: Page object models
- `config/`: Configuration settings
- `utils/`: Utility functions