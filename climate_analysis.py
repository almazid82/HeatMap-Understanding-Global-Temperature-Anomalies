import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# ── 1. LOAD RAW TEMPERATURE DATA ──────────────────────────────────────────────
df = pd.read_csv("GLB.Ts+dSST.csv", skiprows=1)
df = df[['Year', 'J-D', 'D-N', 'DJF', 'MAM', 'JJA', 'SON']]
df.columns = ['Year', 'Jan-Dec', 'Dec-Nov', 'Winter', 'Spring', 'Summer', 'Autumn']

# ── 2. CLEAN DATA ──────────────────────────────────────────────────────────────
df.replace('***', np.nan, inplace=True)
df = df.apply(lambda col: col.map(lambda x: x.strip() if isinstance(x, str) else x))
df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

# Fill missing values: median for skewed columns, interpolation for rest
df.fillna(df.median(numeric_only=True), inplace=True)
df.interpolate(method='linear', inplace=True)
df = df.dropna()

df.to_csv("new cleaned_temperature_data.csv", index=False)
print("Temperature data cleaned. Shape:", df.shape)
print(df.head())

# ── 3. TREND ANALYSIS ─────────────────────────────────────────────────────────
plt.figure(figsize=(12, 5))
plt.plot(df['Year'], df['Jan-Dec'], marker='o', markersize=2, linestyle='-', color='tomato')
plt.xlabel("Year")
plt.ylabel("Temperature Anomaly (°C)")
plt.title("Global Temperature Anomaly Over Years (NASA GISS)")
plt.tight_layout()
plt.savefig("Trend analysis.png", dpi=150)
plt.show()

# ── 4. MOVING AVERAGE SMOOTHING ───────────────────────────────────────────────
df['Rolling_Mean_5yr'] = df['Jan-Dec'].rolling(window=5).mean()
plt.figure(figsize=(12, 5))
plt.plot(df['Year'], df['Jan-Dec'], label="Annual Anomaly", alpha=0.5)
plt.plot(df['Year'], df['Rolling_Mean_5yr'], label="5-Year Moving Average", linestyle="dashed", linewidth=2, color='navy')
plt.xlabel("Year")
plt.ylabel("Temperature Anomaly (°C)")
plt.title("Global Temperature Trend with 5-Year Moving Average")
plt.legend()
plt.tight_layout()
plt.savefig("Moving average plot.png", dpi=150)
plt.show()

# ── 5. SEASONAL CORRELATION HEATMAP ───────────────────────────────────────────
plt.figure(figsize=(8, 6))
sns.heatmap(df[['Jan-Dec', 'Winter', 'Spring', 'Summer', 'Autumn']].corr(),
            annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
plt.title("Correlation of Temperature Anomalies Across Seasons")
plt.tight_layout()
plt.savefig("(Heatmap) Correlation of the tempature accross the season.png", dpi=150)
plt.show()

# ── 6. BOX PLOT — OUTLIER DETECTION ──────────────────────────────────────────
plt.figure(figsize=(10, 5))
sns.boxplot(data=df[['Jan-Dec', 'Winter', 'Spring', 'Summer', 'Autumn']])
plt.title("Temperature Anomaly Distribution by Season")
plt.ylabel("Temperature Anomaly (°C)")
plt.tight_layout()
plt.savefig("Temparature anomaly distribution ( Box plot).png", dpi=150)
plt.show()

# ── 7. CO₂ vs TEMPERATURE ANALYSIS ───────────────────────────────────────────
co2_df = pd.read_csv("CO2 emisson dataset.csv")
temp_df = pd.read_csv("new cleaned_temperature_data.csv")
merged_df = temp_df.merge(co2_df, on="Year", how="inner")

correlation = merged_df[['Jan-Dec', 'Annual CO₂ emissions']].corr()
print("\nCorrelation (Temperature vs CO₂):\n", correlation)

plt.figure(figsize=(8, 6))
sns.scatterplot(x=merged_df['Annual CO₂ emissions'], y=merged_df['Jan-Dec'], color='firebrick')
plt.xlabel("CO₂ Emissions (tonnes)")
plt.ylabel("Temperature Anomaly (°C)")
plt.title("CO₂ Emissions vs Global Temperature Anomaly")
plt.tight_layout()
plt.savefig("CO2 vs temparature anomaly over year.png", dpi=150)
plt.show()

# ── 8. LINEAR REGRESSION — FUTURE TEMPERATURE FORECAST ───────────────────────
X = merged_df[['Year']]
y = merged_df['Jan-Dec']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
print(f"\nModel R² Score: {model.score(X_test, y_test):.4f}")
print(f"Coefficient: {model.coef_[0]:.6f}  |  Intercept: {model.intercept_:.4f}")

future_years = pd.DataFrame({'Year': np.arange(2025, 2051)})
predictions = model.predict(future_years)

plt.figure(figsize=(12, 5))
plt.plot(merged_df['Year'], merged_df['Jan-Dec'], label="Historical Data", color='steelblue')
plt.plot(future_years['Year'], predictions, label="Forecast (2025–2050)",
         linestyle="dashed", color="red", linewidth=2)
plt.xlabel("Year")
plt.ylabel("Temperature Anomaly (°C)")
plt.title("Global Temperature Forecast 2025–2050 (Linear Regression)")
plt.legend()
plt.tight_layout()
plt.savefig("Forcasting for present-2050.png", dpi=150)
plt.show()
