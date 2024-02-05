# Employee Management System

Employee Management System is a Django web application for managing departments and employees within an organization.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [MySQL Integration](#mysql-integration)
- [Usage](#usage)
  - [Adding Departments](#adding-departments)
  - [Managing Employees](#managing-employees)
- [Contributing](#contributing)
- [License](#license)

## Overview

This Django project consists of two main models: `Department` and `Employee`. It allows users to create, view, and manage departments and employees through a user-friendly web interface.

## Features

- Add and manage departments.
- Add employees to specific departments.
- View lists of departments and employees.
- Simple and intuitive web forms for data input.

## Getting Started

### Prerequisites

Make sure you have the following prerequisites installed on your machine:

- Python 3.x
- Django
- MySQL Server

### Installation

Follow these steps to set up the Employee Management System:

```bash
# Clone the repository
git clone https://github.com/your-username/employee-management-system.git

# Change into the project directory
cd employee-management-system

# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install project dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate
