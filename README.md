# HeatMap-Understanding-Global-Temperature-Anomalies
 A comprehensive analysis of global temperature anomalies from 1880 to present, exploring seasonal, annual, and regional trends.
# 📌 Overview
# This project analyzes NASA's Global Temperature Dataset, focusing on data cleaning, preparation, and analysis. The dataset provides temperature variations across different months and seasons, helping to understand long-term trends in global warming.
# 🔍 Steps Covered
 ✅ Loading the CSV file: Importing and structuring the dataset
 ✅ Selecting relevant columns: Year, Jan-Dec, Dec-Nov, Winter, Spring, Summer, Autumn
 ✅ Renaming columns: Making names more readable (e.g., DJF → Winter, MAM → Spring)
 ✅ Handling missing values (***): Replacing them with NaN and cleaning up the dataset
 ✅ Converting data types: Ensuring all temperature values are numerical
 ✅ Checking skewness: Using df.skew() to analyze distribution patterns