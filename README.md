# Library Management System

#### **_Software Development Project, Masters of Computer Science by Bhavya Babuta, student at SRH, Berlin School of Technology_**

## Table of Contents

1. [Git](#git)
2. [Diagrams](#diagrams)
   - [Activity Diagram](#activity-diagram)
   - [Use Case Diagram](#use-case-diagram)
   - [Class Diagram](#class-diagram)
3. [Requirements Engineering](#requirements-engineering)
4. [Analysis Learning Unit](#analysis-learning-unit)
5. [DDD](#ddd)
6. [Metrics](#metrics)
7. [Clean Code Development](#clean-code-development)
8. [Build Management](#build-management)
9. [Unit Tests](#unit-tests)
10. [IDE](#ide)
11. [Functional Programming](#functional-programming)

## 1. Git

In my repository, I have made numerous commits, that helped me understand as well practice the following git concepts:-

- commit
- push
- pull
- force push
- commit amend
- pull requests
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
- actions

Some of the git concepts can be well-viewed in the commit history as well as closed pull requests in this repository

---

## 2. Diagrams

- [Activity Diagram](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/images/diagrams/Activity-Diagram.png?raw=true)

- [Use Case Diagram](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/images/diagrams/Use-Case-Diagram.png?raw=true)

- [Class Diagram](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/images/diagrams/Class-Diagram.png?raw=true)

---

## 3. Requirements Engineering

---

## 4. Analysis Learning Unit

---

## 5. DDD

---

## 6. Metrics

- [Sonarcube](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/images/sonarcube/quality_gate_passed.png)
- [Depandabot Alerts for Security Vulnerabilities](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/images/dependabot/dependabot.png)
- [PyLint code ratings](https://github.com/babutabhavya/Software-Development-SEM-1/blob/main/images/pylint/pylint.png)

---

## 7. Clean Code Development

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
