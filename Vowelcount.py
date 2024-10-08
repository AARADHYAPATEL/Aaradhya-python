def count_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in s:
        if char.lower() in vowels:
            count += 1
    print("The number of vowels in the string are:", count)

s = input("Enter a string: ")
count_vowels(s)