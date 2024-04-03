# Python codes for simple data analysis

import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Load the iris dataset
iris = load_iris()
data = pd.DataFrame(iris.data, columns=iris.feature_names)
data['target'] = iris.target

# Get basic information about the data
data.info()

# Check the missing values
data.isnull().sum()

# Run Descriptive statistics for numerical features
data.describe()

# Distribution of features using histograms
data.hist(figsize=(10,6))
plt.show()

# Explore relationships between features with scatter plots
data.plot.scatter(x='sepal length (cm)', y='sepal width (cm)')
plt.show()

data.boxplot(by='target', column=['sepal length (cm)','sepal width (cm)'])
plt.show()
