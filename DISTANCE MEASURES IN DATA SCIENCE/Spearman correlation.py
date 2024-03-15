import numpy as np
from scipy.stats import spearmanr


def spearman_correlation(X, Y):
    return spearmanr(X, Y)[0]


# Example usage
point1 = np.array([1, 2])
point2 = np.array([3, 4])
print("Spearman correlation:", spearman_correlation(point1, point2))
