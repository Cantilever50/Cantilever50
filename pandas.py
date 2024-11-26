# data_analysis.py

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Data Loading
# Load the dataset (example: a CSV file)
# Replace 'your_data.csv' with your actual dataset file path
file_path = 'MathE dataset (4).csv'  # Replace with your data file path
data = pd.read_csv(file_path)

# Step 2: Data Exploration
# Display basic information about the dataset
print("Basic Information:")
print(data.info())

# Display the first few rows of the dataset
print("\nFirst 5 Rows of the Dataset:")
print(data.head())

# Describe the dataset to get summary statistics
print("\nSummary Statistics:")
print(data.describe())

# Step 3: Basic Data Analysis
# Check for missing values in each column
missing_values = data.isnull().sum()
print("\nMissing Values in Each Column:")
print(missing_values)

# Check the distribution of categorical variables (if any)
categorical_columns = data.select_dtypes(include=['object']).columns
print("\nCategorical Variables Distribution:")
for col in categorical_columns:
    print(f"\n{col} Value Counts:")
    print(data[col].value_counts())

# Step 4: Visualizations
# 1. Histogram of numeric columns
numeric_columns = data.select_dtypes(include=[np.number]).columns
data[numeric_columns].hist(bins=15, figsize=(10, 8))
plt.suptitle('Distribution of Numeric Features', fontsize=16)
plt.tight_layout()
plt.show()

# 2. Correlation heatmap between numeric features
corr_matrix = data[numeric_columns].corr()
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap of Numeric Features', fontsize=16)
plt.show()

# 3. Pairplot to visualize relationships between numeric columns
sns.pairplot(data[numeric_columns])
plt.suptitle('Pairplot of Numeric Features', fontsize=16)
plt.show()

# Step 5: Observations/Findings
# You can make observations based on the analysis above.
# Example observations:
print("\nFindings/Observations:")
print("1. There are missing values in some columns. These need to be handled before further analysis.")
print("2. Based on the correlation heatmap, some features are highly correlated, which may indicate multicollinearity.")
print("3. The distribution of certain numeric features is skewed, suggesting a need for normalization or transformation.")
print("4. The pairplot suggests that Feature A and Feature B have a positive relationship, while Feature C shows no clear pattern.")
