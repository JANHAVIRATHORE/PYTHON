# Stock Market Analysis System

## Project Overview

The **Stock Market Analysis System** is a Python-based data analysis project developed using Pandas, NumPy, Matplotlib, and Seaborn.

The project loads stock market data from a CSV file, cleans the data, performs price and return analysis, calculates moving averages, analyzes trading volume, studies correlations, and creates visualizations.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Dataset

The project uses a CSV file named:

```text
stocks.csv
```

The dataset contains stock information such as:

- Date
- Ticker
- Open
- High
- Low
- Close
- Adj Close
- Volume

The system allows selection of a stock ticker such as **AAPL, MSFT, or NFLX** for analysis.

## Features

### 1. Dataset Loading
- Load CSV dataset
- Display first and last records
- Display dataset information
- Display rows, columns, data types, and statistical summary

### 2. Data Cleaning
- Handle missing values
- Remove duplicate records
- Convert Date values
- Convert numeric columns
- Sort data by Date
- Remove invalid price and volume values

### 3. Date-wise Analysis
- Display starting and ending dates
- Search data for a specific date
- Analyze a date range
- Perform monthly and yearly analysis

### 4. Price Analysis
- Highest price
- Lowest price
- Highest closing price
- Lowest closing price
- Average Open, High, Low, and Close prices
- Starting and ending closing price

### 5. Daily Return Analysis
- Calculate daily returns
- Average return
- Highest and lowest return
- Positive return days
- Negative return days
- Return standard deviation

### 6. Moving Average Analysis
- 7-Day Moving Average
- 20-Day Moving Average
- 50-Day Moving Average
- Custom Moving Average

### 7. Volume Analysis
- Total trading volume
- Average trading volume
- Highest and lowest volume
- Highest volume day
- Monthly and yearly volume
- Volume and closing price correlation

### 8. Trend and Correlation Analysis
- Overall price change
- Percentage change
- Monthly growth and decline
- Correlation between Open, High, Low, Close, and Volume

### 9. Data Visualization
The project creates:
- Stock price line chart
- Moving average chart
- Trading volume chart
- Monthly closing price bar chart
- Daily return histogram
- Volume vs closing price scatter plot
- Closing price box plot
- Correlation heatmap

## Output

The project generates analysis results and saves visualization images such as:

```text
Stock_Price_Over_Time.png
Stock_Price_Moving_Averages.png
Trading_Volume_Over_Time.png
Average_Monthly_Closing_Price.png
Daily_Return_Distribution.png
Trading_Volume_Closing_Price.png
Closing_Price_Distribution.png
Stock_Market_Correlation_Heatmap.png
```

## Project Purpose

This project demonstrates practical use of Python libraries for **data cleaning, data analysis, statistical calculations, and data visualization** using stock market data.

## Author

**Janhavi Rathore**
