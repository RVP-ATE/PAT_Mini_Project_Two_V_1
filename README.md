# OrangeHRM Web Application Automation Testing

## 📌 Project Overview

This project automates functional testing for the **OrangeHRM demo web application** using **Python Selenium** and the **Pytest framework**, with a focus on robust test architecture using **Page Object Model (POM)** and **Data Driven Testing Framework (DDTF)**. It includes positive and negative test scenarios, and generates detailed HTML test reports.

## 🔗 Application Under Test

- **URL:** [https://opensource-demo.orangehrmlive.com/web/index.php/auth/login](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)

---

## ✅ Features Implemented

1. Automated login testing with multiple users (valid & invalid) using data from Excel.
2. Verification of visibility and clickability of dashboard menus.
3. New user creation and login verification.
4. Validation of newly created users under Admin ➝ User Management.
5. Page Object Model implementation for modularity.
6. Explicit waits for stable execution.
7. Pytest HTML report generation.
8. Exception handling and logging.


---

## 🛠️ Tech Stack

- **Python 3.x**
- **Selenium**
- **Pytest**
- **Pytest-HTML**
- **Openpyxl** (for Excel-based DDTF)
- **POM (Page Object Model)**
- **Explicit Waits**
- **OOP Principles**

---


---

## 📋 Test Cases Covered

### ✅ Test Case 1: Login Tests (DDTF)
- Tests login using multiple sets of credentials from Excel
- Verifies success via cookies/session
- Logs out after each login

### ✅ Test Case 2: Home URL Verification
- Checks if the homepage loads correctly

### ✅ Test Case 3: Login Field Visibility
- Verifies if username and password input boxes are displayed

### ✅ Test Case 4: Menu Visibility Post-Login
- Verifies if menus like Admin, PIM, Leave, etc., are visible and clickable

### ✅ Test Case 5: User Creation & Login
- Creates a new user from the Admin panel and verifies login

### ✅ Test Case 6: User Record Verification
- Verifies if the new user exists in Admin → User Management

---

## 🧪 Running the Tests

### ✅ Install Dependencies

✅ Run All Tests with HTML Report
bash
Copy
Edit
pytest --html=reports/test_report.html
✅ Run Specific Test
bash
Copy
Edit
pytest tests/test_login.py

⚙️ Configuration
Edit config/config.yaml:

yaml
Copy
Edit
base_url: "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
browser: "chrome"
implicit_wait: 10


🧹 Coding Guidelines
Follows PyLint conventions

Python OOPS-based design

Modular POM implementation

Explicit Waits instead of time.sleep

Exception Handling for every action

🔚 Teardown
The browser is automatically closed after each test using fixtures in conftest.py.

📃 Notes
All positive and negative scenarios are covered.

HTML reports generated in the /reports directory.

Excel format used for DDTF.

YAML used for configuration (and optional KDTF).

You must have Python 3.7+ installed to run the project.

👨‍💻 Author
PAVAN KUMAR RV



