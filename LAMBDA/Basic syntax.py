# Regular function
def add(x, y):
    return x + y


# Equivalent lambda function
lambda_add = lambda x, y: x + y

# Using both functions
result_regular = add(3, 5)
result_lambda = lambda_add(3, 5)

print("Result (Regular function):", result_regular)
print("Result (Lambda function):", result_lambda)
