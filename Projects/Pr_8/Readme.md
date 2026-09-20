# NumPy Data Analyzer

A menu-driven **NumPy Data Analyzer** built with Python and Object-Oriented Programming (OOP).  
The project allows users to create 1D, 2D, and 3D NumPy arrays and perform common array operations such as indexing, slicing, mathematical operations, searching, sorting, filtering, combining, splitting, and statistical calculations.

---

## 📌 Project Overview

**NumPy Data Analyzer** is a console-based application designed for practicing:

- Python functions and classes
- Object-Oriented Programming
- NumPy arrays
- 1D, 2D, and 3D array handling
- Indexing and slicing
- Mathematical operations
- Array searching, sorting, and filtering
- Aggregate and statistical functions
- Menu-driven program design

The project stores the active NumPy array inside a `DataAnalyzer` object and provides separate methods for different operations.

---

## ✨ Features

### 1. Array Creation

The application supports:

- 1D NumPy arrays
- 2D NumPy arrays
- 3D NumPy arrays

Users enter the required dimensions and individual elements through the console.

### 2. Indexing

The indexing feature supports indexes according to the array dimension.

Examples:

```python
# 1D
array[2]

# 2D
array[1, 2]

# 3D
array[0, 1, 2]
```

The program accepts comma-separated indexes such as:

```text
2
1,2
0,1,2
```

### 3. Slicing

The current slicing feature uses:

```python
array[start:end]
```

For a 1D array, this extracts a range of elements.

For multidimensional arrays, `array[start:end]` slices the first axis. For example, for a 2D array it slices rows, and for a 3D array it slices layers.

### 4. Mathematical Operations

The application provides:

- Addition
- Subtraction
- Multiplication
- Division

The operations are performed using NumPy array arithmetic.

### 5. Combine Arrays

The application accepts another set of elements and combines it with the current array.

The current implementation uses:

```python
np.concatenate((self.array.flatten(), second_array))
```

Therefore, the combined result is a 1D array.

### 6. Split Arrays

The application uses:

```python
np.array_split()
```

to divide the current array into a user-selected number of parts.

### 7. Search

Users can search for a value using:

```python
np.where()
```

The program displays the indexes where the value occurs.

### 8. Sorting

The application displays:

- Ascending order
- Reverse/descending order

using NumPy sorting functions.

### 9. Filtering

The application filters values using Boolean indexing.

For example:

```python
array[array > number]
array[array < number]
```

It displays values greater than and less than the user-selected number.

### 10. Statistical Operations

The current application supports:

- Sum
- Mean
- Median
- Standard deviation
- Variance

---

## 🧱 OOP Structure

The project uses a class:

```python
class DataAnalyzer:
```

### Constructor

The constructor initializes an empty NumPy array:

```python
def __init__(self):
    self.array = np.array([])
```

### Encapsulation

The active array is stored as an instance attribute:

```python
self.array
```

This allows the methods of `DataAnalyzer` to work with the same array.

### Private Method

The project uses:

```python
def __check_array(self):
```

The double underscore makes it a private-style method using Python's name-mangling mechanism.

It checks whether an array has been created before an operation is performed.

### Instance Methods

Operations such as:

```python
create_1d_array()
create_2d_array()
create_3d_array()
indexing()
slicing()
add()
sub()
multi()
div()
combine()
split()
search()
filter_array()
sort_array()
```

are instance methods and are called through the object:

```python
obj = DataAnalyzer()
obj.create_1d_array()
```

---

## 🗂️ Project Structure

A simple project structure can be:

```text
NumPy-Data-Analyzer/
│
├── numpy_analyzer.ipynb
├── README.md
```

---

## ⚙️ Requirements

### Software

- Python 3.x
- NumPy


---


## 🖥️ Main Menu

The application provides the following menu:

```text
Welcome to the Numpy Analyzer!

Choose an option:

1. Create a NumPy array
2. Indexing and slicing
3. Perform Mathematical operations
4. Combine and Split Arrays
5. Search, Sort, or Filter Arrays
6. Compute Aggregates and Statistics
7. Exit
```

---

## 🧮 NumPy Concepts Used

This project demonstrates several important NumPy concepts:

| Concept | NumPy Function / Syntax |
|---|---|
| Create array | `np.array()` |
| Concatenate | `np.concatenate()` |
| Flatten | `array.flatten()` |
| Split | `np.array_split()` |
| Search | `np.where()` |
| Sort | `np.sort()` |
| Boolean filtering | `array[condition]` |
| Sum | `np.sum()` |
| Mean | `np.mean()` |
| Median | `np.median()` |
| Standard deviation | `np.std()` |
| Variance | `np.var()` |
| Indexing | `array[index]` |
| Multidimensional indexing | `array[row, column]` / `array[layer, row, column]` |
| Slicing | `array[start:end]` |

---

## 👩‍💻 Author

**NumPy Data Analyzer Project**

Built as a Python/NumPy learning project with an emphasis on Object-Oriented Programming and practical array analysis.

---
