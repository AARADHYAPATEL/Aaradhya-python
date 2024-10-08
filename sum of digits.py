def sum_of_digits(x):
    return sum(int(digit) for digit in str(x))

print(sum_of_digits(12345))  # 15