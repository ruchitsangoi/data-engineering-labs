import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the combined CSV file
df = pd.read_csv("data/combined_data.csv")

# Basic info
print("\n--- Dataset Overview ---")
print(df.info())

# Basic stats
print("\n--- Summary Statistics ---")
print(df.describe())

# Missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# Check unique values per column
print("\n--- Unique Values per Column ---")
print(df.nunique())

# Distribution of a numeric column (change column name as per your dataset)
if "age" in df.columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df["age"], kde=True, bins=20)
    plt.title("Age Distribution")
    plt.show()

# Correlation heatmap
numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
if len(numeric_cols) > 1:
    plt.figure(figsize=(10, 6))
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()
