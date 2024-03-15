import sympy as sym

x = sym.Symbol('x')  # Symbolize X
func = x ** 4 + 4 * x ** 2 + 5 * x - 6  # Function
sym.Derivative(func, x)  # Derivative expression
sym.Derivative(func, x, evaluate=True)  # Calculate the derivative of func
func.diff(x) # Or us this for the same

# Create functions with lambdify
expr = sym.lambdify(x, func)
expr_der = sym.lambdify(x, func.diff(x))
print(f'value of func at x=5: {expr(637)}')
print(f'derivative of func at x=5: {expr_der(372)}')
