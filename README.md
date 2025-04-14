# HeatMap-Understanding-Global-Temperature-Anomalies
 A comprehensive analysis of global temperature anomalies from 1880 to present, exploring seasonal, annual, and regional trends.
# 📌 Overview
# This project analyzes NASA's Global Temperature Dataset, focusing on data cleaning, preparation, and analysis. The dataset provides temperature variations across different months and seasons, helping to understand long-term trends in global warming.
## 🔍 Steps Covered 
1. Loading the CSV file: Importing and structuring the dataset   
2. Selecting relevant columns: Year, Jan-Dec, Dec-Nov, Winter, Spring, Summer, Autumn
3.Renaming columns: Making names more readable (e.g., DJF → Winter, MAM → Spring)
4. Handling missing values (***): Replacing them with NaN and cleaning up the dataset
5. Converting data types: Ensuring all temperature values are numerical
6. Checking skewness: Using df.skew() to analyze distribution patterns


# 🌍 HeatMap - Understanding Global Temperature Anomalies  


## 📊 Dataset Summary  

### Yearly Statistics:  
| Statistic  | Value  |
|------------|--------|
| **Total Years** | 144 |
| **Mean Year** | 1952.5 |
| **Standard Deviation** | 41.71 |
| **Minimum Year** | 1881 |
| **25th Percentile** | 1916.75 |
| **Median (50%)** | 1952.5 |
| **75th Percentile** | 1988.25 |
| **Maximum Year** | 2024 |

### **Skewness Analysis**  
Using `df.skew()` to check the distribution pattern:  
- **Temperature Anomalies:** Shows whether the dataset is **symmetrically distributed or skewed**  
- **Interpretation:** Helps identify trends in **global warming**  

## 🔍 Steps Covered  
✅ **Data Cleaning & Preparation**  
✅ **Handling Missing Values (`***` → `NaN`)**  
✅ **Checking Skewness (`df.skew()`)**  
✅ **Visualizing Trends Using Matplotlib & Seaborn**  

## 📈 Future Enhancements  
✔ **Advanced Temperature Forecasting Models**  
✔ **Comparison with CO₂ Emission Data**  
✔ **Regional Anomaly Analysis**