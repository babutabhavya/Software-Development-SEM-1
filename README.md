# Library Management System [![Python CI](https://github.com/babutabhavya/Software-Development-SEM-1/actions/workflows/deploy.yml/badge.svg)](https://github.com/babutabhavya/Software-Development-SEM-1/actions/workflows/deploy.yml)

#### ***Software Development Project, Masters of Computer Science by Bhavya Babuta, student at SRH, Berlin School of Technology***

## Table of Contents

- [Prerequisites](#prerequisites)
- [Makefile commands](#makefile-commands)
1. [Git](#1-git)
2. [Diagrams](#2-diagrams)
3. [Requirements Engineering](#3-requirements-engineering)
4. [Analysis Learning Unit](#4-analysis-learning-unit)
5. [DDD](#5-ddd)
6. [Metrics](#6-metrics)
7. [Clean Code Development](#7-clean-code-development)
8. [Build Management](#8-build-management)
9. [Unit Tests](#8-unit-tests)
10. [IDE](#10-ide)
11. [Functional Programming](#12-functional-programming)

## Prerequisites

Before running the build management commands, make sure you have the following installed on your system:

- **Python:** The project uses Python, and you can install it from [python.org](https://www.python.org/).
- **Pip:** Pip is the package installer for Python. You can check if you have it installed by running `pip --version`. If not, you can install it using the instructions on the [official Pip website](https://pip.pypa.io/en/stable/installation/).
- **Pipenv:** Pipenv is used for virtual environment management. You can install it using `pip install pipenv`.
- **Makefile:** The build management commands are defined in the Makefile. Make sure you have `make` installed on your system. On Linux, you can typically install it with `sudo apt-get install make`, and on macOS, it comes pre-installed.

## Makefile commands

- **`makemigrations`**: Create database migration files for changes in models.
- **`migrate`**: Apply database migrations to update the database schema.
- **`run`**: Start the Django development server to run the application.
- **`setup`**: Install project dependencies, including development dependencies.
- **`check-format`**: Check code formatting using Black without making changes.
- **`format`**: Format code using Black to adhere to the specified style.
- **`check-import-order`**: Check import order using isort with a profile for Black.
- **`import-order`**: Organize import order using isort with a profile for Black.
- **`lint`**: Run pylint to perform static code analysis on the project.
- **`check`**: Check code formatting, import order, and linting.
- **`test`**: Run pytest to execute all tests in the project with coverage.
- **`help`**: Display a help message with available Makefile targets and their explanations.


## 1. Git

In my repository, I have made numerous commits, that helped me understand as well practice the following git concepts:-

- commit
- push
- pull
- force push
- commit amend
- [pull requests](https://github.com/babutabhavya/Software-Development-SEM-1/pulls?q=is%3Apr+is%3Aclosed)
- merge
- set-origin
- add-origin
- undo
- revert
- rules
  - main
    - Restrict deletions
    - Restrict force push
    - Require a pull request to merge
    - Requires Python_CI build management and SonarQube checks to pass before merge
  - dev-branches
    - Requires Python_CI build management and SonarQube checks to pass before merge
    - Need to be updated with the default branch
- actions

Some of the git concepts can be well-viewed in the commit history as well as closed pull requests in this repository

---

## 2. Diagrams

- [Activity Diagram](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/images/diagrams/Activity-Diagram.png?raw=true)

- [Use Case Diagram](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/images/diagrams/Use-Case-Diagram.png?raw=true)

- [Class Diagram](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/images/diagrams/Class-Diagram.png?raw=true)

---

## 3. Requirements Engineering

### Functional Requirements

- User Management

- Borrowing and Returning

- Library Management

    - Library User Management

    - Library Books Management

### Non-Functional Requirements

- Performance

- Scalability

- Compatibility

- Reliability

- Security

### [JIRA](https://bhavya-babuta.atlassian.net/jira/software/projects/LS/boards/5)

- Kanban Board [Screenshot](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/images/jira/kanban-board.png?raw=true)
- Timeline [Screenshot](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/images/jira/timeline.png?raw=true)
- Backlog Story Board [Screenshot](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/images/jira/backlog.png?raw=true)
- Backlog Board [Screenshot](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/images/jira/board.png?raw=true)
---


### [Trello](https://trello.com/b/OlFhoenB/library-management-system)
- Tasklist [Screenshot](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/images/trello/trello.png?raw=true)


## 4. Analysis Learning Unit

1. [Checklist](https://bhavyababuta.notion.site/Checklist-8cc4b860f2214ac7804f9a4c421f7336?pvs=4)
2. [Analysis](https://bhavyababuta.notion.site/Analysis-e3719825f60f446393e0901c0bb67e59?pvs=4)

---

## 5. DDD

[PDF](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/docs/ddd.pdf)

---

## 6. Metrics

- [Sonarcube](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/images/sonarcube/quality_gate_passed.png)
- [Depandabot Alerts for Security Vulnerabilities](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/images/dependabot/dependabot.png)
- [PyLint code ratings](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/images/pylint/pylint.png)
- [pytest code coverage](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/images/pytest/pytest.png)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=babutabhavya_Software-Development-SEM-1&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=babutabhavya_Software-Development-SEM-1)

[![SonarCloud](https://sonarcloud.io/images/project_badges/sonarcloud-black.svg)](https://sonarcloud.io/summary/new_code?id=babutabhavya_Software-Development-SEM-1)

---

## 7. Clean Code Development

### A.)

1. Code Comments and Docstrings
Code comments are like helpful notes to yourself and others, explaining how your code works and making it easier to understand. To see this, refer [here](https://github.com/babutabhavya/Software-Development-SEM-1/blob/93f5cc24d9793c2ad99b2839f866d981105084e0/lms/book/views.py#L6)

2. Exception Handling
Using "as" in exception handling (eg. except Exception as e) is a good Python practice because it allows to catch and inspect the specific exception instance, providing valuable information for debugging or logging. To see this refer [here](https://github.com/babutabhavya/Software-Development-SEM-1/blob/93f5cc24d9793c2ad99b2839f866d981105084e0/lms/library/serializers.py#L27)

3. Validating request data in serialisers than in views
Validation in serializers is preferable to in views because it centralizes data validation logic, promoting code reusability and ensuring consistent validation across different views. This approach also enhances maintainability by keeping data integrity concerns encapsulated within the serializer layer. To see this refer [here](https://github.com/babutabhavya/Software-Development-SEM-1/blob/93f5cc24d9793c2ad99b2839f866d981105084e0/lms/library/serializers.py#L21)

4. MVC Architecture
Django's MVT/MVC architecture promotes a clear separation of concerns, enhancing code organization and maintainability. It facilitates modular development by isolating data models, presentation logic, and HTML template rendering. TO see this, refer [here](https://github.com/babutabhavya/Software-Development-SEM-1/tree/main/lms/book)

5. Re-usability
Implemented re-usability using fixtures in PyTest enhances test modularization by providing reusable setup, promoting cleaner and more maintainable test code. It ensures consistent test environments, facilitating reliable and reproducible testing scenarios. To see this, refer [here](https://github.com/babutabhavya/Software-Development-SEM-1/blob/93f5cc24d9793c2ad99b2839f866d981105084e0/lms/library/tests/test_library_views.py#L7)

6. Seperation between test and dev environment
Maintaining a clear separation between test and dev environments prevents unintended interference, ensuring that changes and experiments in the development environment do not impact the stability of testing scenarios. This demarcation supports reliable testing and accurate results.
To see this refer [this](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/lms/.pytest.ini)

7. Use of import-order package to correctly order imports
By employing the "import-order" package, code's imports are neat and tidy, fostering clarity and teamwork. It ensures a consistent import order, making it simpler for everyone to understand and manage the project's dependencies. The follow an order in which the frameworks are imported first, then the third party outside the framework and then the internal modules are arranged. To see this refer [here](https://github.com/babutabhavya/Software-Development-SEM-1/blob/93f5cc24d9793c2ad99b2839f866d981105084e0/Makefile#L20)


### B.) [Clean Code Development Cheat Sheet](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/docs/clean-code-development.pdf)

---

## 8. Build Management

Build management for this projected has been implemented through [MAKEFILE\*](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/Makefile) and [GITHUB ACTIONS\*](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/.github/workflows/deploy.yml).

The github actions is configured using a YAML file to execute the CI on pull requests on all branches and push to the main branch (which has been restricted using rules to be only possible through pull requests). The the main jobs at CI are:-

1. Checkout code
2. Setup python (Specifically version 3.9)
3. Check if the branch is non-main branch (This can be configured to export some DEV_VARS, if needed)
4. Upgrade pip, install pipenv as the virtual environment manager and setup the virtual enviroment using the makefile's setup file.
5. Perform the following checks using the makefile's check command
   - pylint
   - import-order
   - black (formatter)
   - pytest

---

## 9. Unit Tests

[Test DIR 1](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/lms/library/tests/test_library_views.py)

[Test DIR 2](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/lms/user/tests/test_user_views.py)

The library choosen to perform unit tests for this project is pytest, enhanced using pytest-django and pytest-cov plugins.

pytest-django is a pylint plugin to facilitate enhanced linting for python's django and django rest framework which has been used for this project.

pytest-cov is a pylint plugin to enable the coverage report of the pytests. The [make test](https://github.com/babutabhavya/Software-Development-SEM-1/blob/bb25be984994588cfc22277588d424446d2331a4/Makefile#L32) command has an option `--cov` and `--cover-report=html` that generates the coverage report in html whenever these tests are run.

---

## 10. IDE

The IDE that has been used is a Visual Studio Code, and the list of my favourite shortcuts include:-

- **_CMD + SHIT + P_**
- **_CMD + J_** = Open the terminal
- **_CMD + B_** = Show/Hide the Primary Side Bar
- **_CMD + CONTROL + B_** = Show/Hide the Secondary Side Bar
- **_Collapse Folders in Explorer_** from primary sidebar
- **_Close All Editors_** from primary sidebar
- **_CMD + UP-KEY_** - Go to the top of the file
- **_CMD + DOWN-KEY_** - Go to the bottom of the file
- **_OPTION + UP-KEY _**- Move the current cursor line up by one
- **_OPTION + DOWN-KEY_** - Move the current cursor line down by one

---

## 11. Functional Programming

- [Only Final Data Structures [Javascript]](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/functional-programming/final-data-structure/main.py)
- [Side-Effect Free Functions [Python]](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/functional-programming/side-effect-free-functions/index.js)
- [The use of Higher Order Functions [ReactJS]](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/functional-programming/hoc/withSideBar.jsx)
- [Functions as Parameters and Return Values [Javascript]](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/functional-programming/functions-as-params-return-vals/index.js)
- [Use of Closures/Anonymous Functions [Javascript]](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/functional-programming/anonymous-functions/index.js)

---
