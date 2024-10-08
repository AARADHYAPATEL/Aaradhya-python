def find_duplicates(lst):
    return list(set([item for item in lst if lst.count(item) > 1]))

print(find_duplicates([1, 2, 3, 3, 4, 4]))
