def jaccard_similarity(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)


# Example usage
string1 = "hello"
string2 = "hallo"
print("Jaccard similarity:", jaccard_similarity(string1, string2))
