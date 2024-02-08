num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

res1 = num1 > num2 and num3 > num4
res2 = num1 > num2 or num3 > num4
res3 = not num1 == num2

print("If both the conditions are true, then the result will be: ", res1)
print("If any of the conditions are true, then the result will be: ", res2)
print("If the condition is true, then the result will be: ", res3)
