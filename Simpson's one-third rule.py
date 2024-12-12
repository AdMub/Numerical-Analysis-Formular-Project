def simpsons_one_third_rule(func, a, b, n):
    """
    Calculate the definite integral of a function using Simpson's 1/3 Rule.

    :param func: The function to be integrated.
    :param a: The lower limit of integration.
    :param b: The upper limit of integration.
    :param n: The number of subintervals (steps), which must be even.
    :return: The approximate integral value.
    """
    h = (b - a) / n
    integral = func(a) + func(b)

    for i in range(1, n):
        x_i = a + i * h
        if i % 2 == 0:
            integral += 2 * func(x_i)
        else:
            integral += 4 * func(x_i)

    return h * integral / 3

# User input (similar to the Trapezoidal Rule example)
import sympy as sp

x = sp.symbols('x')
func_expression = input("Enter the function to integrate in terms of 'x': ")
func = sp.sympify(func_expression)
a = float(input("Enter the lower limit of integration (a): "))
b = float(input("Enter the upper limit of integration (b): "))
n = int(input("Enter the number of subintervals (n, must be even): "))

func_lambda = sp.lambdify(x, func, 'numpy')

result = simpsons_one_third_rule(func_lambda, a, b, n)
print(f"Approximate integral value using Simpson's 1/3 Rule: {result}")
