# HeatMap-Understanding-Global-Temperature-Anomalies


![ Global Temperature dataset analysis](https://github.com/almazid82/HeatMap-Understanding-Global-Temperature-Anomalies/blob/main/Global%20temp.jpg)


This project presents a comprehensive data-driven analysis of global temperature anomalies from 1880 to the present. It explores seasonal, annual, and regional variations in temperature trends to understand the long-term impacts of climate change.

Using visual heatmaps, line graphs, and statistical summaries, the analysis aims to highlight key patterns and significant deviations in temperature across different time periods and geographic zones. The ultimate goal is to provide valuable insights into global warming trends and support climate-awareness initiatives through accessible and interpretable data visualization.

Key Features:

Historical data analysis (1880–Present)

Seasonal and annual trend comparison

Regional heatmap visualizations

Anomaly detection and pattern recognition

Interactive and informative visuals for presentation

Here, [Click here to download the Dataset without cleaning](./GLB.Ts+dSST.csv)– Contains global temperature anomaly data from 1880 to present, including monthly, seasonal, and annual values. This dataset is used as the foundation for all analysis and visualization in this project.


## 📌 Overview: This project analyzes NASA's Global Temperature Dataset, focusing on data cleaning, preparation, and analysis. The dataset provides temperature variations across different months and seasons, helping to understand long-term trends in global warming.
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


## 📈 Trend Analysis


![Trend Analysis](https://raw.githubusercontent.com/almazid82/HeatMap-Understanding-Global-Temperature-Anomalies/main/Trend%20analysis.png)
  

### 🌍 Observations from Global Temperature Anomalies  

1️⃣ **Long-Term Warming Trend**  
   - From **1880 to 1940**, temperature anomalies were relatively stable, fluctuating around **-0.25°C to 0.00°C**.  
   - After **1940**, a noticeable increase in temperature anomalies is observed, marking the beginning of a **consistent warming phase**.  

2️⃣ **Sharp Rise from 1980s Onward**  
   - Post-1980, temperature anomalies show a **steep upward trend**.  
   - By **2000s**, anomalies exceeded **0.50°C**, indicating rapid global warming.  
   - In the **2020s**, the anomalies **crossed 1.25°C**, reinforcing the severe impact of climate change.  

3️⃣ **Evidence of Climate Change Acceleration**  
   - Earlier fluctuations were **smaller and less frequent**, showing a relatively balanced climate.  
   - In recent years, **larger jumps** suggest increasing human-induced climate change influences.  

### 🔥 Interpretation  
✔ **Global warming has accelerated significantly over the last 40 years.**  
✔ Temperature anomalies are **not stabilizing**, indicating ongoing climatic shifts.  
✔ Further investigation into **seasonal variations and future temperature forecasting** could provide more insights into climate trends. 


## 🔥 Correlation Analysis of Global Temperature Anomalies  

![Heatmap - Correlation of the Temperature Across the Season](https://raw.githubusercontent.com/almazid82/HeatMap-Understanding-Global-Temperature-Anomalies/main/(Heatmap)%20Correlation%20of%20the%20tempature%20accross%20the%20season.png)

### 🌍 Understanding Correlation in Temperature Data  
The heatmap visualizes the **correlation coefficients** between different seasonal and yearly temperature anomalies.  
- **Correlation close to 1** → Strong positive relationship between variables  
- **Correlation close to 0** → Weak or no relationship between variables  

### 🔹 Key Observations from the Heatmap  
| Variable Pair | Correlation Value | Interpretation |
|--------------|------------------|----------------|
| **Year ↔ Jan-Dec** | `0.88` | Strong correlation, showing yearly trends impact annual temperature anomalies |
| **Winter ↔ Spring** | `0.96` | Highly correlated, indicating seasonal consistency in temperature variations |
| **Spring ↔ Summer** | `0.97` | Spring temperatures strongly influence summer anomalies |
| **Summer ↔ Autumn** | `0.97` | Summer and autumn anomalies have a strong relationship, possibly due to prolonged warming |
| **Winter ↔ Autumn** | `0.91` | Moderately high correlation, showing year-round warming effects |
| **Jan-Dec ↔ Dec-Nov** | `1.00` | Identical correlation, confirming annual temperature trends remain consistent |

### 📌 Interpretation  
- **Yearly temperature trends** significantly affect seasonal anomalies.  
- **Winter, Spring, and Summer** anomalies are tightly linked, showing **seasonal continuity in temperature shifts**.  
- **The strongest correlations** are between **adjacent seasons**, reinforcing gradual transitions in climate patterns over time.  


