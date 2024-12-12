def simpsons_three_eighth_rule(func, a, b, n):
    """
    Calculate the definite integral of a function using Simpson's 3/8 Rule.

    :param func: The function to be integrated.
    :param a: The lower limit of integration.
    :param b: The upper limit of integration.
    :param n: The number of subintervals (steps), which must be a multiple of 3.
    :return: The approximate integral value.
    """
    h = (b - a) / n
    integral = func(a) + func(b)

    for i in range(1, n):
        x_i = a + i * h
        if i % 3 == 0:
            integral += 2 * func(x_i)
        else:
            integral += 3 * func(x_i)

    return (3 * h * integral) / 8

# User input
import sympy as sp  # You can use the SymPy library to define your function symbolically

x = sp.symbols('x')  # Define the variable x symbolically
func_expression = input("Enter the function to integrate in terms of 'x': ")
func = sp.sympify(func_expression)
a = float(input("Enter the lower limit of integration (a): "))
b = float(input("Enter the upper limit of integration (b): "))
n = int(input("Enter the number of subintervals (n): "))
func_lambda = sp.lambdify(x, func, 'numpy')


result = simpsons_three_eighth_rule(func_lambda, a, b, n)
print(f"Approximate integral value using Simpson's 3/8 Rule: {result}")