# Sales Data Analyzer

A menu-driven Python application for **data analysis, DataFrame operations, statistical analysis, and data visualization** using Pandas, NumPy, Matplotlib, and Seaborn.

The project is implemented using an object-oriented approach with a `SalesDataAnalyzer` class.

---

## Features

### 1. Dataset Loading
- Load CSV datasets using Pandas.
- Display the number of rows and columns.
- Handles missing file errors.

### 2. Data Exploration
- Display first 5 rows.
- Display last 5 rows.
- Display column names.
- Display data types.
- Display DataFrame information.

### 3. DataFrame Operations
- Add a new column.
- Drop a column.
- Rename a column.
- GroupBy operations:
  - Sum
  - Mean
  - Count
  - Minimum
  - Maximum
  - Transform with group mean
- Pivot Table:
  - Sum
  - Mean
  - Count
  - Minimum
  - Maximum
- Reindex DataFrame.
- Display the current DataFrame.

### 4. NumPy Operations
The project converts numeric Pandas data into NumPy arrays and supports:
- Array indexing.
- Array slicing.
- Element-wise mathematical operations.

### 5. DataFrame Combination
Supports:
- Concatenation
- Merge
- Join

A second CSV dataset can be loaded when performing combination operations.

### 6. Data Filtering and Searching
- Filter numeric values.
- Search text values.
- Case-insensitive text matching.

### 7. Sorting
Sort DataFrame values in:
- Ascending order
- Descending order

### 8. Aggregate Functions
Provides:
- Sum
- Mean
- Count

### 9. Statistical Analysis
Provides:
- Descriptive statistics
- Standard deviation
- Variance
- Percentiles
- Quartiles (Q1, Q2, Q3)

### 10. Missing Data Handling
Supports:
- Detecting missing values.
- Filling numeric missing values with mean.
- Dropping rows containing missing values.
- Replacing missing values with a user-provided value.

### 11. Data Visualization
The application supports the following charts:

| Visualization | Library |
|---|---|
| Bar Plot | Seaborn |
| Line Plot | Matplotlib |
| Scatter Plot | Matplotlib |
| Pie Chart | Matplotlib |
| Histogram | Matplotlib |
| Stack Plot | Matplotlib |
| Box Plot | Seaborn |
| Correlation Heatmap | Seaborn |

### 12. Save Visualization
- Stores the most recently generated figure.
- Allows the user to save the current visualization as a PNG file.

---

## Technologies Used

- **Python 3**
- **Pandas** – Data loading, cleaning, transformation, grouping, statistics
- **NumPy** – Numerical arrays and array operations
- **Matplotlib** – Data visualization
- **Seaborn** – Statistical visualization

---



###  Install Required Libraries

Run:

```bash
pip install pandas numpy matplotlib seaborn
```

---

## Project Structure

```text
Sales-Data-Analyzer/
│
├── sales_data_analyzer.ipynb
├── Sales_Data.csv
├── README.md
└── visualizations/
```


---

## The program displays a main menu:

```text
========== Data Analysis & Visualization Program ==========

1.Load Dataset
2.Explore Data
3.Perform DataFrame Operations
4.Handle Missing Data
5.Generate Descriptive statistics
6.Data Visualization
7.Save Visualization
8.Exit
```

---

## Basic Workflow

A typical workflow is:

```text
Load CSV
   ↓
Explore Dataset
   ↓
Clean / Modify Data
   ↓
Perform DataFrame Operations
   ↓
Perform Statistical Analysis
   ↓
Create Visualization
   ↓
Save Visualization
```

### Example

1. Select **1 - Load Dataset**.
2. Enter the CSV file path.
3. Select **2 - Explore Data** to inspect the dataset.
4. Use **3 - Perform DataFrame Operations** for transformations.
5. Use **4 - Handle Missing Data** if required.
6. Use **5 - Generate Descriptive Statistics**.
7. Use **6 - Data Visualization**.
8. Generate a chart.
9. Select **7 - Save Visualization** to save the latest chart.

---

## Object-Oriented Design

The main functionality is encapsulated inside:

```python
class SalesDataAnalyzer:
```

The class stores the application state using:

```python
self.data
self.df
self.df2
self.fig
```

### Main Attributes

| Attribute | Purpose |
|---|---|
| `self.data` | Stores the CSV path |
| `self.df` | Stores the main DataFrame |
| `self.df2` | Stores the second DataFrame |
| `self.fig` | Stores the latest Matplotlib figure |

---

## Important Methods

### Dataset

```python
load_dataset()
```

Loads a CSV file into a Pandas DataFrame.

### Exploration

```python
head_row()
last_row()
col_name()
data_type()
basic_info()
```

### DataFrame Operations

```python
add_cols()
drop_cols()
rename_cols()
group_data()
pivottable()
re_index()
show_data()
```

### NumPy Operations

```python
indexing()
slicing()
mathematical_operations()
```

### Combining DataFrames

```python
Concate_data()
merge_data()
join_data()
```

### Filtering and Sorting

```python
split_dataframe()
filter_value()
search_value()
sort_dataframe()
```

### Statistics and Missing Values

```python
aggregate_function()
statistical_analysis()
missing_value()
fill_value()
drop_missing()
replace_missing()
```

### Visualization

```python
plot_bar()
plot_line()
plot_scatter()
plot_pie()
plot_histogram()
plot_stack()
plot_box()
plot_heatmap()
save_visualization()
```

---

## Example Dataset

The application can work with a CSV file such as:

```csv
Product,Category,Sales,Quantity,Profit
Laptop,Electronics,50000,5,8000
Phone,Electronics,30000,10,5000
Chair,Furniture,12000,6,2500
Table,Furniture,20000,4,4000
```

The exact column names are not fixed because the program asks the user to select columns interactively.

---

## Error Handling

The program includes checks for common situations such as:

- Dataset not loaded.
- File not found.
- Invalid column names.
- Invalid numeric columns.
- Invalid sorting order.
- Invalid DataFrame index input.
- No visualization generated before saving.

---

## Visualization Saving

After generating a visualization, select:

```text
7. Save Visualization
```

Then enter a filename, for example:

```text
sales_chart
```

The program saves:

```text
sales_chart.png
```

The `self.fig` attribute ensures that the most recently generated visualization can be saved.

---

## Learning Objectives

This project demonstrates practical use of:

- Python classes and objects
- Encapsulation
- Pandas DataFrames
- NumPy arrays
- Data cleaning
- Data transformation
- GroupBy
- Pivot tables
- DataFrame indexing and slicing
- Concatenation, merge, and join
- Filtering and searching
- Sorting
- Aggregation
- Statistical analysis
- Missing-value handling
- Matplotlib visualization
- Seaborn visualization
- File handling
- Menu-driven programming

---

## Author

**Sales Data Analyzer Project**

Built as a Python Data Analysis learning project using Pandas, NumPy, Matplotlib, and Seaborn.

---

