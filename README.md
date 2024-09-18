# Mobile Web Testing Framework

A robust and flexible mobile web testing framework built with Selenium, pytest, and Python. This framework leverages configuration files for easy setup and supports multiple device emulations, making it ideal for testing mobile versions of web applications like Twitch.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [1. Install pyenv](#1-install-pyenv)
  - [2. Set Up Python Environment](#2-set-up-python-environment)
  - [3. Install Dependencies](#3-install-dependencies)
- [Recommended IDE](#recommended-ide)
- [Running Tests](#running-tests)
  - [Basic Usage](#basic-usage)
  - [Specify Device and Environment](#specify-device-and-environment)
- [Project Structure](#project-structure)


## Features

- **Device Emulation:** Easily switch between different mobile devices like iPhone X.
- **Configurable Environments:** Supports multiple environments (development, testing, production) via `config.yaml`.
- **Reusable Actions:** Common Selenium actions are abstracted into a `BaseAction` module for reusability.
- **Structured Test Cases:** Tests inherit from a `BaseTest` class, ensuring consistent setup and teardown.
- **Flexible Configuration:** Centralized configuration management using YAML files.
- **Integration with CI/CD:** Easily integrate with continuous integration pipelines.

## Prerequisites

- **Operating System:** macOS, Linux, or Windows.
- **Python:** Version 3.8 or higher.
- **Git:** For version control.
- **Chrome Browser:** Latest version recommended.

## Installation

### 1. Install pyenv

[`pyenv`](https://github.com/pyenv/pyenv) allows you to easily switch between multiple versions of Python. Follow the installation instructions for your operating system.
Basically, for Mac, just run below command.
```bash
brew update
brew install pyenv
```
and paste below code to `~/.zshrc`
```bash
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```
### 2. Set Up Python Environment
#### macOS/Linux

- Python for Mac, for short

  - install python3.8 `pyenv install 3.8`
  - use python3.8 `pyenv global 3.8`
- Please see detail installation, https://github.com/pyenv/pyenv

### 3. Install Dependencies

install all requirements `pip install -r requirements.txt`
Or you can download PyCharm Community Edition, and open this project, PyCharm will guide you.

## Recommended IDE

PyCharm

PyCharm is highly recommended for Python development due to its powerful features:

- Intelligent Code Editor: Code completion, inspections, and quick fixes.
- Integrated Testing: Run and debug pytest directly from the IDE.
- Version Control Integration: Seamless Git integration.
- Virtual Environment Support: Easily manage and switch between virtual environments.

Setup Tips:

### 1.	Open the Project:
 - Launch PyCharm and open the mobile_web_test directory.
### 2.	Configure the Interpreter:
 - Go to File > Settings > Project: mobile_web_test > Python Interpreter.
 - Select the mobile-web-test-env virtual environment created by pyenv.
### 3.	Run Tests:
 - Right-click on the tests directory or individual test files and select Run pytest in filename.

## Running Tests

### Basic Usage

To run all tests with default settings (iPhone X and production environment):
```bash
pytest
```

### Specify Device and Environment
```bash
# Use Desktop Device with production environment
pytest --device=Desktop --env=production
# Use default Device iPhoneX with production environment
pytest --env=production
```

After running, if you have pytest-html installed, a test report `report.html` will be generated.

## Project Structure
```bash
mobile_web_test/
│
├── actions/
│   ├── __init__.py
│   └── base_action.py
│
├── config/
│   ├── __init__.py
│   └── config.yaml
│
├── devices/
│   ├── __init__.py
│   ├── base_device.py
│   └── iphone_x.py
│
├── tests/
│   ├── __init__.py
│   ├── base_test.py
│   └── test_launch_web.py
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── home_page.py
│   ├── search_page.py
│   ├── search_result_page.py
│   └── video_stream_page.py
│
├── screenshot/
│
├── testResults/
│
├── conftest.py
├── requirements.txt
├── pytest.ini
└── README.md
```
Directory Overview:

 - actions/: Contains reusable Selenium actions.
 - config/: Configuration files and configuration loader.
 - devices/: Device emulation classes.
 - tests/: Test cases and base test class.
 - pages/: Page Object Model classes representing web pages.
 - conftest.py: Pytest configuration and fixtures.
 - requirements.txt: Python dependencies.
 - pytest.ini: Pytest configuration file.

