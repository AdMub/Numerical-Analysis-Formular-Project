#Error_S = -((b - a)^5 / (180 * n^4)) * f''''(c)

def estimate_simpsons_error(func, a, b, n):
    """
    Estimate the error in Simpson's Rule approximation.

    :param func: The function being integrated.
    :param a: The lower limit of integration.
    :param b: The upper limit of integration.
    :param n: The number of subintervals used in Simpson's Rule (must be even).
    :return: Estimated absolute error.
    """
    h = (b - a) / n
    c = (a + b) / 2  # Midpoint of the interval
    fourth_derivative = sp.diff(func, x, 4)  # Calculate the fourth derivative symbolically
    error = abs(-((b - a)**5 / (180 * n**4)) * fourth_derivative.evalf(subs={x: c}))
    return error

# User input (assuming you've already calculated the Simpson's Rule approximation)
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

error_estimate = estimate_simpsons_error(func, a, b, n)
print(f"Estimated absolute error in Simpson's Rule approximation: {error_estimate}")
