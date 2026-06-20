# 📔 Personal Journal Manager

A simple **Python-based Personal Journal Manager** that allows users to create, view, search, and delete journal entries through a menu-driven interface.

---

## 🌟 Project Overview

Personal Journal Manager helps users maintain a digital diary by storing journal entries with their respective date and time.

Each entry contains:

* 📅 Date
* ⏰ Time
* 📝 Journal Entry

The program stores data in a text file named:

```text
Personal_Journal.txt
```

---

# 🚀 Features

## ✍️ Add a New Entry

Users can create a journal entry by providing:

* Date (YYYY-MM-DD)
* Time (HH-MM-SS)
* Journal Content

The entry is then saved to the journal file.

---

## 📖 View All Entries

Displays all previously saved journal entries from the file.

---

## 🔍 Search Entries

Search for journal entries using:

* Keywords
* Dates
* Any matching text

---

## 🗑️ Delete All Entries

Removes all journal entries after user confirmation.

---

## ❌ Exit Program

Safely exits the application.

---

# 🏗️ OOP Concepts Used

## 1️⃣ Class and Object

The project is built using multiple classes:

| Class    | Purpose                    |
| -------- | -------------------------- |
| `add`    | Add journal entries        |
| `read`   | View journal entries       |
| `search` | Search journal entries     |
| `delete` | Delete all journal entries |

Example:

```python
addobj = add(date,time,entry)
```

---

## 2️⃣ Constructor (`__init__`)

Constructors are used to initialize objects automatically.

Example:

```python
def __init__(self,dt,tm,ent):
```

Used in:

* `add`
* `read`
* `delete`

---

## 3️⃣ Encapsulation

Data is stored inside objects using instance variables.

Example:

```python
self.date
self.time
self.entry
```

---

## 4️⃣ Methods

Methods are used to perform operations.

Examples:

```python
get_info()
search_info()
```

---

# 📂 File Handling Used

The project performs:

### Write Mode

```python
open("Personal_Journal.txt","+a")
```

Used for adding entries.

---

### Read Mode

```python
open("Personal_Journal.txt","r")
```

Used for displaying entries.

---

### Write Mode (Delete)

```python
open("Personal_Journal.txt","w")
```

Used to clear all entries.

---

# ⚠️ Exception Handling Used

The project uses Python exception handling to prevent crashes.

---

## ValueError

Occurs when user enters non-numeric menu choices.

Example:

```python
choice = int(input())
```

Handled by:

```python
except ValueError:
```

---

## FileNotFoundError

Occurs when the journal file does not exist.

Handled in:

```python
class read
```

---

## IndexError

Used when no journal entries are available.

Handled in:

```python
class read
```

and

```python
class delete
```

---

## Generic Exception

Used to catch unexpected errors.

Example:

```python
except Exception:
```

---

# 🔎 Possible Errors That Can Occur

## 1. Search Without Adding Entries

Problem:

```text
No Entries were found.
```

Reason:

The `journal` list is empty.

---

## 2. Searching After Restarting Program

Problem:

Search may not find entries stored in the file.

Reason:

Search operation uses the in-memory list:

```python
journal
```

instead of reading directly from the file.

---

## 3. Duplicate Header Issue

Every new entry writes:

```text
Date    Time    Entry
```

again into the file.

Result:

Multiple headers appear throughout the journal file.

---

## 4. Deleting Non-Existing File

Problem:

User tries deleting entries before any file exists.

Handled using exception handling.

---

## 5. Invalid Menu Input

Example:

```text
abc
```

instead of:

```text
1
```

Handled by:

```python
ValueError
```

---

# 📋 Program Flow

```text
Start
   │
   ▼
Display Menu
   │
   ├── Add Entry
   ├── View Entries
   ├── Search Entry
   ├── Delete Entries
   └── Exit
   │
   ▼
End
```

---

# 💻 Technologies Used

* Python 3
* Object-Oriented Programming
* File Handling
* Exception Handling

---

# 🎯 Learning Outcomes

Through this project, you can learn:

* Classes and Objects
* Constructors
* Encapsulation
* File Handling
* Exception Handling
* Menu Driven Programs
* Data Storage and Retrieval
* Basic Project Structure

---

## 👨‍💻 Author

**Janhavi Rathore**

Python Programming Project 🚀