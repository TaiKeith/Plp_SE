#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load and explore the dataset
try:
    iris = load_iris()
    data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    data['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

    print("First 5 rows of the dataset:")
    print(data.head())

    print("\nDataset Info:")
    print(data.info())

    print("\nMissing Values:")
    print(data.isnull().sum())

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Since there are no missing values, no cleaning is necessary

# Basic Data Analysis
print("\nBasic Statistics:")
print(data.describe())

print("\nMean values grouped by species:")
grouped = data.groupby('species').mean()
print(grouped)

# Data Visualization
sns.set(style='whitegrid')

# 1. Line chart: Mean petal length per species (simulate time trend)
plt.figure(figsize=(8, 5))
grouped['petal length (cm)'].plot(kind='line', marker='o')
plt.title('Mean Petal Length per Species')
plt.ylabel('Petal Length (cm)')
plt.xlabel('Species')
plt.grid(True)
plt.xticks(ticks=range(len(grouped)), labels=grouped.index)
plt.tight_layout()
plt.savefig("line_chart.png")
plt.show()

# 2. Bar chart: Average sepal width by species
plt.figure(figsize=(8, 5))
sns.barplot(x='species', y='sepal width (cm)', data=data, ci=None)
plt.title('Average Sepal Width per Species')
plt.xlabel('Species')
plt.ylabel('Sepal Width (cm)')
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()

# 3. Histogram: Distribution of petal length
plt.figure(figsize=(8, 5))
sns.histplot(data['petal length (cm)'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig("histogram.png")
plt.show()

# 4. Scatter Plot: Sepal Length vs Petal Length
plt.figure(figsize=(8, 5))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=data)
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.show()

# Observations
print("\nObservations:")
print("- Setosa generally has shorter petal length and sepal length.")
print("- Versicolor and Virginica have overlapping features, but Virginica tends to have the largest petals.")
print("- The histogram shows a bimodal distribution of petal length, suggesting two dominant clusters.")
print("- There's a positive correlation between sepal length and petal length, especially for Virginica.")
