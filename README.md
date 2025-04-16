# HeatMap-Understanding-Global-Temperature-Anomalies

Climate change is one of the most pressing challenges of our time. But how do we *see* this change? Behind every news headline, policy shift, and global summit lies a stream of numbers — decades of temperature data recorded from every corner of the planet.

In this project, we dive deep into historical global temperature anomalies to uncover the patterns, shifts, and signals that tell the story of a warming Earth. Using heatmaps and powerful visual tools, we transform complex datasets into intuitive visuals that anyone can understand.

Through this data story, we aim to answer:

- How has the Earth's temperature changed over time?
- Are there specific decades or regions where warming is more prominent?
- What can past patterns tell us about the future?

This project is not just a technical exercise — it's a journey to make climate data accessible, visual, and actionable for everyone. Whether you're a researcher, policymaker, or curious mind, this story invites you to explore the temperature records that shape our understanding of the planet's future.

Let’s discover what the data says — and what it means for us all.




![ Global Temperature dataset analysis](https://github.com/almazid82/HeatMap-Understanding-Global-Temperature-Anomalies/blob/main/Global%20temp.jpg)



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

## Data Update After Cleaning 
[Click here to see After Cleaning Data](https://github.com/almazid82/HeatMap-Understanding-Global-Temperature-Anomalies/blob/main/new%20cleaned_temperature_data.csv)



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


## 📊 Moving Average Trend Analysis 


![Moving Average Plot](https://raw.githubusercontent.com/almazid82/HeatMap-Understanding-Global-Temperature-Anomalies/main/Moving%20average%20plot.png) 

### 🌍 Overview  
This plot showcases the **global temperature anomalies from 1880 to 2024**, using a **5-year moving average** to smooth out short-term variations and highlight long-term warming trends.  

### 🔹 Key Observations  
- **Before 1940:** Temperature anomalies remained relatively stable.  
- **Post-1980:** A **consistent rise in temperature anomalies**, marking a warming phase.  
- **Extreme Peaks (2016 & 2024):** Confirming drastic temperature shifts over the years.  

### 🚀 Interpretation  
✔ **Global warming is steadily accelerating** over decades.  
✔ **Moving average helps differentiate actual climate trends from short-term fluctuations.**  
✔ **This method is useful for forecasting future temperature variations.**


## 📊 Box Plot Analysis - Temperature Anomaly Distribution  


![Temparature Anomaly Distribution(Box Plot)](https://raw.githubusercontent.com/almazid82/HeatMap-Understanding-Global-Temperature-Anomalies/main/Temparature%20anomaly%20distribution%20(%20Box%20plot).png)



### 🌍 Overview  
This box plot showcases **temperature anomaly trends from 1881 to 2024**, offering a visual breakdown of how climate variability has evolved over time.

### 🔹 Key Observations  
- **1881-1940:** Cooler temperatures, with anomalies predominantly negative.  
- **1940-1980:** Gradual warming trend emerges, reflected in rising median values.  
- **1980-2000:** Significant temperature anomalies and extreme events begin appearing.  
- **2000-2024:** Modern climate instability confirmed—anomalies reach unprecedented heights.  

### 🔥 Interpretation  
✔ **Climate change effects are now consistent and measurable over decades.**  
✔ **Temperature anomalies are expanding in variability, proving more extreme seasonal fluctuations.**  
✔ **Predictive modeling can leverage these insights to forecast future global temperatures.**  


# 🌡️ Global Warming Dataset – Seasonal Average Analysis

This section provides a summary of the **average temperature anomalies** for different seasons. The data helps analyze the seasonal variation of global warming impacts over time.

## 📊 Seasonal Average Temperature Anomalies

| Season  | Average Anomaly | Emoji |
|---------|------------------|--------|
| Winter  | 0.069444         | ❄️     |
| Spring  | 0.075139         | 🌸     |
| Summer  | 0.063333         | ☀️     |
| Autumn  | 0.089861         | 🍂     |

## 🔍 Observations

- **Autumn** shows the **highest average anomaly** (*0.089861*), indicating it may be warming faster than other seasons.
- **Summer** has the **lowest anomaly** (*0.063333*), but still shows signs of warming.
- All values are **positive**, confirming a **consistent temperature increase** across all seasons.

## 📝 Notes

- Data is based on a pilot analysis of the global warming dataset.
- Further insights can be drawn by comparing seasonal anomalies over multiple decades.

### 🗂️ Dataset Overview: CO₂ Emissions

We are now integrating the  
[📄 CO₂ Emissions Dataset (CSV)](https://github.com/almazid82/HeatMap-Understanding-Global-Temperature-Anomalies/blob/main/CO2%20emisson%20dataset.csv)  
to enhance our climate analysis with emission-based insights.

---

### 📌 Key Features of the Dataset

- **Source**: Global CO₂ Emission Records (Public data)
- **Format**: CSV
- **Time Period**: 1880 - Recent years
- **Frequency**: Annual
- **Primary Focus**: Emission in Million Metric Tons (MMT)

#### 📊 Key Columns:
| Column Name       | Description                                      |
|-------------------|--------------------------------------------------|
| `Year`            | The year of record                               |
| `Total_emissions` | Total global CO₂ emissions in MMT                |
| `Gas_Fuel`        | CO₂ from gas fuel consumption                    |
| `Liquid_Fuel`     | CO₂ from liquid fuel (e.g. oil)                  |
| `Solid_Fuel`      | CO₂ from solid fuel (e.g. coal)                  |
| `Cement`          | Emissions due to cement production               |
| `Gas_Flaring`     | Emissions from gas flaring                       |

---



> This dataset empowers us to trace the rise of emissions and compare it against global temperature shifts for a deeper, more accurate climate narrative.









## 🔄 Connecting the Dots: CO₂ Emissions vs. Global Temperature Anomalies

Climate change is more than just rising temperatures—**it's a story of cause and effect**.  
Until now, our project focused on understanding **temperature anomalies over time**.  
But to truly grasp *why* our planet is warming, we need to look deeper.

---

### 🌍 Introducing CO₂ Emissions Data

We're now adding a new dimension to our analysis:  
**Global CO₂ Emissions Dataset**

This dataset tracks yearly carbon dioxide emissions—**a key driver of global warming**—and will help us uncover the relationship between human activity and temperature changes.

---

### 🔍 Why This Matters

Temperature anomalies show the **symptoms**. CO₂ emissions reveal the **cause**.  
By bringing these two powerful datasets together, we can:

- Explore how closely **CO₂ levels align with temperature rise**
- Detect **critical periods** where emissions triggered sharp warming
- Move from simple observations to **evidence-backed climate insights**
- Build **predictive models** based on CO₂ trends

> **This shift transforms our project from a visual exploration into a data-driven climate narrative.**


## 🔗 Correlation Analysis: Temperature vs CO₂ Emissions

This correlation matrix shows the linear relationship between the *average yearly temperature (Jan-Dec)* and *Annual CO₂ emissions*.

|                         | Jan-Dec | Annual CO₂ emissions |
|-------------------------|---------|------------------------|
| *Jan-Dec*             | 1.000   | 0.934                  |
| *Annual CO₂ emissions*| 0.934   | 1.000                  |

### 📌 Interpretation

- The correlation between *temperature* and *CO₂ emissions* is *0.934, indicating a **strong positive relationship*.
- This means as *CO₂ emissions increase, the **average global temperature also tends to rise*.
- Correlation values range from *-1 to +1. A value of **+0.934* suggests a very strong link between the two variables.


# 🌍 CO₂ Emissions & Global Temperature Anomalies Analysis  

To better understand the relationship between **CO₂ emissions** and **temperature anomalies**, we’ve plotted both over time:

![CO₂ vs Temperature Anomaly Over Years](https://github.com/almazid82/HeatMap-Understanding-Global-Temperature-Anomalies/blob/main/CO2%20vs%20temparature%20anomaly%20over%20year.png)

## 📌 Overview  
This research explores how rising **CO₂ emissions impact global temperature anomalies**, providing insights into climate change acceleration.

---

## 🔎 Key Findings  
- **Positive correlation observed**: As **CO₂ emissions increase, temperature anomalies also rise**.  
- **Extreme emissions linked to peak temperature values** (1998, 2016, 2020, 2023).  
- **Future models predict sustained warming trends if CO₂ levels are not controlled.**  

### 📊 Scatter Plot Interpretation  
A visual representation of the **CO₂ vs. temperature anomaly correlation** confirms that **human-driven emissions directly contribute to global warming**.

---

## 🔥 Climate Change Implications  
✔ **CO₂ emissions are a key factor influencing climate shifts globally.**  
✔ **Temperature rise aligns with historical industrial CO₂ trends.**  
✔ **Predictive modeling should integrate emissions data for future climate projections.**


## 🤖 Model Training Summary – Linear Regression

To predict future global temperature anomalies, we trained a **Linear Regression model** using historical data from the dataset.

### 📊 Data Split
- **Training Set Size**: 114 rows
- **Test Set Size**: 29 rows
- **Feature (X)**: `Year`
- **Target (y)**: `Jan-Dec` (Average Annual Temperature Anomaly)

### ⚙️ Model Details
- **Model Used**: `LinearRegression()` from `scikit-learn`
- **Coefficient**: `0.00827458`  
- **Intercept**: `-16.083578`

The model equation is:

\[
\text{Predicted Anomaly} = 0.00827458 \times \text{Year} - 16.083578
\]

---

## 🔮 Future Temperature Prediction (2025–2050)

Using the trained model, we predicted the average global temperature anomaly for the years **2025 to 2050**. The model shows a **gradual increase in temperature**, indicating ongoing global warming.

> 🔍 Example:
> - **2025 Prediction**: `0.370` (approx.)
> - **2050 Prediction**: `0.577` (approx.)

These values are predicted based on historical linear trends, and the increase aligns with climate change concerns.

🖼️ The following chart visualizes both historical data and the model's predictions:

*(Insert graph here after running your matplotlib code)*

```python
plt.title("Future Temperature Predictions (2025–2050)")
# Your matplotlib plot will go here