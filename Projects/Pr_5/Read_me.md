# 🚀 Employee Management System

A Python-based **Object-Oriented Programming (OOP)** project that demonstrates core OOP concepts through a menu-driven Employee Management System.

---

## 📖 Project Overview

The Employee Management System allows users to create and manage different types of employees, including:

* 👨‍💼 Employees
* 👨‍💻 Developers
* 🧑‍💼 Managers

The project is designed to showcase Python OOP principles such as inheritance, encapsulation, method overriding, constructors, and polymorphism.

---

## ✨ Features

### 👨‍💻 Create Developers

* Add developer details
* Store programming language expertise
* Assign custom salary

### 👨‍💼 Create Employees

* Add basic employee information
* Store employee ID and salary

### 🧑‍💼 Create Managers

* Add manager details
* Assign department information
* Store management salary

### 📋 View Records

* Display all Developers
* Display all Employees
* Display all Managers

### 🚪 Exit System

* Verify inheritance relationships using `issubclass()`
* Safely terminate the program

---

## 🛠️ OOP Concepts Implemented

| Concept                 | Implementation                         |
| ----------------------- | -------------------------------------- |
| Classes & Objects       | Employee, Manager, Developer           |
| Inheritance             | Manager and Developer inherit Employee |
| Encapsulation           | Employee ID and Salary attributes      |
| Constructors            | `__init__()`                           |
| Method Overriding       | `get_Info()` and `setInfo()`           |
| Setter Method           | `setInfo()`                            |
| Getter / Display Method | `get_Info()`                           |
| Polymorphism            | Same methods behaving differently      |
| super()                 | Parent class method invocation         |
| issubclass()            | Inheritance verification               |
| Menu Driven Interface   | Interactive user experience            |

---

## 📂 Class Structure

Employee
├── Manager
└── Developer

---

## 📸 Program Menu

```text
Choose an Option:

1. Create a Developer
2. Create a Employee
3. Create a Manager
4. Show Details
5. Exit
```

---

## 🧪 Sample Output

```text
Choose an Option:
1. Create a Developer

Enter Name: John
Enter Age: 25
Enter Employee Id: DEV101
Enter Salary: 50000
Enter Programming Language: Python

Developer Created Successfully!
```

```text
Name: John
Age: 25
Employee Id: DEV101
Salary: $50000
Programming Language: Python
```

---

## 💻 Technologies Used

* Python 3
* Object-Oriented Programming
* Command Line Interface (CLI)

---

## 🎯 Learning Outcomes

Through this project, you will understand:

* Creating classes and objects
* Using inheritance effectively
* Implementing encapsulation
* Method overriding
* Working with constructors
* Building menu-driven applications
* Applying real-world OOP concepts

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone <repository-url>
```

2. Navigate to the project directory

```bash
cd Employee-Management-System
```

3. Run the program

```bash
python employee_management.py
```

---

## 🌟 Future Enhancements

* Update Employee Information
* Delete Employee Records
* Search Employees by ID
* Store Data in Files
* Database Integration
* Graphical User Interface (GUI)

---

## 👨‍💻 Author

**Janhavi Rathore**

Python Programming Project 🚀

---

