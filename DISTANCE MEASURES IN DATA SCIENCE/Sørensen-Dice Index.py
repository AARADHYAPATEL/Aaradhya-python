def sorensen_dice_index(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    intersection = set1.intersection(set2)
    return (2 * len(intersection)) / (len(set1) + len(set2))


# Example usage
string1 = "hello"
string2 = "hallo"
print("Sørensen-Dice index:", sorensen_dice_index(string1, string2))
