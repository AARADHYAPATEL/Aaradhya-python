import numpy as np
from scipy.special import rel_entr


def jensen_shannon_divergence(X, Y):
    M = 0.5 * (X + Y)
    return np.sqrt(0.5 * (rel_entr(X, M).sum() + rel_entr(Y, M).sum()))


# Example usage
point1 = np.array([1, 2])
point2 = np.array([3, 4])
print("Jensen-Shannon divergence:", jensen_shannon_divergence(point1, point2))
