def flatten(lst):
    return set([item for sublist in lst for item in sublist])

print(flatten([[1, 2], [3, 4], [5, 6]]))  # {1, 2, 3, 4, 5, 6}