import pandas as pd
import numpy as np

# 1. Load CSV
df = pd.read_csv("C:/Users/shams/Downloads/GLB.Ts+dSST.csv", skiprows=1)

# 2. Select important columns
df = df[['Year', 'J-D', 'D-N', 'DJF', 'MAM', 'JJA', 'SON']]

# 3. Rename columns for better understanding
df.columns = ['Year', 'Jan-Dec', 'Dec-Nov', 'Winter', 'Spring', 'Summer', 'Autumn']

# ✅ 4. Replace '***' with np.nan FIRST
df.replace('***', np.nan, inplace=True)

# (Optional but helpful) Remove any extra spaces in strings
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# ✅ 5. Now drop missing values
df = df.dropna()

# 6. Convert all data to numeric (except Year)
df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

# 7. Check result
print(df.head())

# 8. check the description of the data
print(df.describe())

# 9. check skewness to know what can we use to fill up miissing value ( if skewed then we will use median otherwise we will use mean)
print(df.skew())

df.fillna(df.median(), inplace=True)
print(df.isnull().sum())  # যদি সব কলামে 0 আসে, তাহলে missing data fill হয়ে গেছে


df.fillna(df.mean(), inplace=True)  # Mean দিয়ে পূরণ
df.interpolate(method='linear', inplace=True)  # Linear interpolation ব্যবহার করে পূরণ


df.to_csv("new cleaned_temperature_data.csv", index=False)

### Data Visualitation

## Trend Analysis (Yearly & Seasonal Variations
#  দেখতে পারবে কোন বছরগুলোতে বড় পরিবর্তন ঘটেছে।


import matplotlib.pyplot as plt
plt.plot(df['Year'], df['Jan-Dec'], marker='o', linestyle='-')
plt.xlabel("Year")
plt.ylabel("Temperature Anomaly")
plt.title("Global Temperature Anomaly Over Years")
plt.show()

## Heatmap for Correlation Analysis
# কোন season-এর সাথে তাপমাত্রার পরিবর্তন বেশি সম্পর্কিত?

import seaborn as sns
plt.figure(figsize=(12,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation of Temperature Anomalies Across Seasons")
plt.show()


## Moving Average & Smoothing Trend
# তাপমাত্রা পরিবর্তনের সাধারণ প্রবণতা বোঝার জন্য moving average ব্যবহার করা


df['Rolling_Mean'] = df['Jan-Dec'].rolling(window=5).mean()
plt.plot(df['Year'], df['Jan-Dec'], label="Original Data")
plt.plot(df['Year'], df['Rolling_Mean'], label="5-Year Moving Average", linestyle="dashed")
plt.legend()
plt.show()



##Anomaly Detection (Finding Outliers)
#Box Plot ব্যবহার করে outliers নির্ণয় করা

sns.boxplot(data=df[['Jan-Dec', 'Winter', 'Spring', 'Summer', 'Autumn']])
plt.title("Temperature Anomaly Distribution")
plt.show()


#মৌসুমভিত্তিক তাপমাত্রার গড় বের করা
seasonal_avg = df[['Winter', 'Spring', 'Summer', 'Autumn']].mean()
print(seasonal_avg)


import pandas as pd  

# CO₂ নির্গমনের ডেটাসেট লোড করা  
co2_df = pd.read_csv("C:/Users/shams/OneDrive/Pictures/Al MAZID/HeatMap-Understanding-Global-Temperature-Anomalies/CO2 emisson dataset.csv")

# গ্লোবাল তাপমাত্রার ডেটাসেট লোড করা  
temperature_df = pd.read_csv("C:/Users/shams/OneDrive/Pictures/Al MAZID/HeatMap-Understanding-Global-Temperature-Anomalies/cleaned_temperature_data.csv")  

# Year কলামের মাধ্যমে দুইটি ডেটাসেট merge করা  
df = temperature_df.merge(co2_df, on="Year", how="inner")

# finding out the correlation between jan to Dec with CO2 emission 
correlation = df[['Jan-Dec', 'Annual CO₂ emissions']].corr()
print(correlation)



## Visualization (Scatter Plot) তৈরি করা
#এই গ্রাফ দেখাবে CO₂ নির্গমনের সাথে তাপমাত্রার পরিবর্তন কীভাবে ঘটছে।
#যদি ডাটা একটি ঊর্ধ্বমুখী রেখা তৈরি করে, তাহলে এটি প্রমাণ করবে যে CO₂ নির্গমন তাপমাত্রা বৃদ্ধির সাথে সরাসরি সম্পর্কিত


import matplotlib.pyplot as plt  
import seaborn as sns  

plt.figure(figsize=(8,6))  
sns.scatterplot(x=df['Annual CO₂ emissions'], y=df['Jan-Dec'])  
plt.xlabel("CO₂ Emissions")  
plt.ylabel("Temperature Anomaly")  
plt.title("CO₂ vs Temperature Anomaly Over Years")  
plt.show()

from sklearn.model_selection import train_test_split  

# Feature & Target Variable ঠিক করা --- এটি নিশ্চিত করবে যে X_train এবং y_train ঠিকভাবে তৈরি হয়েছে

X = df[['Year']]  # Features  
y = df[['Jan-Dec']]  # Target  

# Train-Test Split  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train.shape, y_train.shape)  # Train Dataset-এর Shape পরীক্ষা করো
print(X_test.shape, y_test.shape)  # Test Dataset-এর Shape পরীক্ষা করো



# Model Training (Linear Regression)       এটি নিশ্চিত করবে যে মডেল সফলভাবে train হয়েছে

from sklearn.linear_model import LinearRegression  

# মডেল তৈরি এবং প্রশিক্ষণ  
model = LinearRegression()  
model.fit(X_train, y_train)  

# Model coefficients দেখার জন্য  
print("Model Coefficient:", model.coef_)  
print("Model Intercept:", model.intercept_)


import numpy as np

# ভবিষ্যতের বছর সেটআপ করা  
future_years = pd.DataFrame({'Year': np.arange(2025, 2050)})  

# Prediction চালানো  
predictions = model.predict(future_years)

# Visualization তৈরি করা  
import matplotlib.pyplot as plt  

plt.figure(figsize=(10,5))
plt.plot(df['Year'], df['Jan-Dec'], label="Actual Data")  
plt.plot(future_years, predictions, label="Predicted Data", linestyle="dashed", color="red")  
plt.xlabel("Year")  
plt.ylabel("Temperature Anomaly")  
plt.title("Future Temperature Predictions (2025-2050)")  
plt.legend()  
plt.show()





