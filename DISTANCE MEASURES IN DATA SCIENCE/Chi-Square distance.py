import numpy as np


def chi_square_distance(X, Y):
    X = X / np.sum(X)
    Y = Y / np.sum(Y)
    return np.sum((X - Y) ** 2 / (X + Y))


# Example usage
point1 = np.array([1, 2])
point2 = np.array([3, 4])
print("Chi-Square distance:", chi_square_distance(point1, point2))
