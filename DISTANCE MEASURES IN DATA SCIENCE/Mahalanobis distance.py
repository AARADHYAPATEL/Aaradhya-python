import numpy as np
from scipy.spatial.distance import cdist


def mahalanobis_distance(X, Y):
    return cdist(X.reshape(1, -1), Y.reshape(1, -1), 'mahalanobis', VI=np.cov(X))


# Example usage
point1 = np.array([1, 2])
point2 = np.array([3, 4])
print("Mahalanobis distance:", mahalanobis_distance(point1, point2))
