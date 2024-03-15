import numpy as np
from scipy.stats import pearsonr


def pearson_correlation(X, Y):
    return pearsonr(X, Y)[0]


# Example usage
point1 = np.array([1, 2])
point2 = np.array([3, 4])
print("Pearson correlation:", pearson_correlation(point1, point2))
