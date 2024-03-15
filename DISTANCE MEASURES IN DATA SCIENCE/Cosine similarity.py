import numpy as np
from scipy.spatial import distance


def cosine_similarity(p1, p2):
    return 1 - distance.cosine(p1, p2)


# Example usage
point1 = np.array([1, 2])
point2 = np.array([3, 4])
print("Cosine similarity:", cosine_similarity(point1, point2))
