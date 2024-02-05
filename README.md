# Employee Management System

Employee Management System is a Django web application for managing departments and employees within an organization.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Screenshots](#screenshots)
  - [Installation](#installation)
  - [MySQL Integration](#mysql-integration)
- [Usage](#usage)
  - [Adding Departments](#adding-departments)
  - [Managing Employees](#managing-employees)

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

## Screenshots

### Add Employee

![Screenshot (42)](https://github.com/RachanaSonu/Employee_Management/assets/37769405/b4b653b9-24a0-47c0-9e55-77a07c1d9432)

### Department List

![Screenshot (51)](https://github.com/RachanaSonu/Employee_Management/assets/37769405/0cac2699-8329-49a4-8e85-6a2e701d566f)
![Screenshot (49)](https://github.com/RachanaSonu/Employee_Management/assets/37769405/ae0660a7-be1f-427c-af1d-068457d6d96b)
![Screenshot (53)](https://github.com/RachanaSonu/Employee_Management/assets/37769405/6dcfaf7c-96eb-420f-a7c5-0f031e483e1d)
![Screenshot (52)](https://github.com/RachanaSonu/Employee_Management/assets/37769405/c15bbdc1-7aac-4972-8c8a-8d18a45d8d8c)
![Screenshot (55)](https://github.com/RachanaSonu/Employee_Management/assets/37769405/5be7e683-01e3-4974-b08b-0c94352571e6)
![Screenshot (54)](https://github.com/RachanaSonu/Employee_Management/assets/37769405/18166d3e-842f-4db4-a83f-6cec4c7f0c2c)

### Installation

Follow these steps to set up the Employee Management System:

```bash
# Clone the repository
https://github.com/RachanaSonu/Employee_Management.git

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

# Run the development server
python manage.py runserver
```

## MySQL Integration

To use MySQL as the database for your Django project, follow these steps:

### Install the `mysqlclient` package:

```bash
pip install mysqlclient

# Update the DATABASES setting in your settings.py file:
# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
## Screenshots
![Screenshot (46)](https://github.com/RachanaSonu/Employee_Management/assets/37769405/ffb86bca-d85d-4018-8afb-144b10ca7153)

### Delete Employee

![Screenshot (44)](https://github.com/RachanaSonu/Employee_Management/assets/37769405/ff2cfb48-584e-433f-9ef4-fbaddfd9fae8)
![Screenshot (45)](https://github.com/RachanaSonu/Employee_Management/assets/37769405/678e255e-1d62-44c7-ae3d-36c951028e1c)

## Usage

### Adding Departments
- Visit http://127.0.0.1:8000/admin/ and log in with the superuser credentials.
- Add departments through the Django admin interface.
  
### Managing Employees
- Navigate to http://127.0.0.1:8000/department/ to view the list of departments.
- Click on a department to view and manage its employees.
- Add employees to a department using the "Add Employee" form.




