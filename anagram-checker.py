def is_anagram(s1, s2):
    if sorted(s1) == sorted(s2):
        return "is anagram"
    else:
        return "It is not a anagram"

print(is_anagram("listen", "silent"))