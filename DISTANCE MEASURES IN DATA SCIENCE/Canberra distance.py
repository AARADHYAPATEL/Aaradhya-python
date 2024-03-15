import numpy as np
from scipy.spatial.distance import canberra


def canberra_distance(X, Y):
    return canberra(X, Y)


# Example usage
point1 = np.array([1, 2])
point2 = np.array([3, 4])
print("Canberra distance:", canberra_distance(point1, point2))
