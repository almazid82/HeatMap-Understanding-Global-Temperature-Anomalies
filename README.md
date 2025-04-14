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

## 📊 Skewness Analysis  

### Understanding Skewness  
Skewness helps us determine whether the dataset is **symmetrically distributed** or **leaning more towards one side**.  
- **Positive Skew (> 0)** → Data is **right-skewed** (more lower values, long tail on the right).  
- **Negative Skew (< 0)** → Data is **left-skewed** (more higher values, long tail on the left).  
- **Skewness = 0** → Data is **perfectly symmetric**.

### 🔹 Skewness Results from the Dataset  
| Category | Skewness Value | Interpretation |
|----------|---------------|----------------|
| **Year** | `0.0` | Perfectly symmetrical distribution |
| **Jan-Dec** | `0.955` | Moderately **right-skewed**, indicating more lower temperature anomalies |
| **Dec-Nov** | `0.954` | Similar right-skewed trend as **Jan-Dec** |
| **Winter** | `0.765` | Right-skewed, but less extreme than summer/autumn |
| **Spring** | `0.851` | Right-skewed, showing more frequent lower values |
| **Summer** | `0.963` | Noticeably right-skewed, suggesting more lower anomalies |
| **Autumn** | `1.089` | Strongly right-skewed, indicating a heavy right tail |

### 🌍 Interpretation  
- **All seasonal categories show positive skewness**, meaning **lower temperature anomalies** are more frequent, but extreme highs exist.  
- **Autumn (1.089) has the strongest skew**, showing the highest variation in anomalies.  
- **Year column is 0.0**, indicating that time itself has a **balanced spread** within the dataset.  

🚀 This skewness analysis helps identify **how temperature distributions vary over different seasons**, providing insights into **climate change trends**!