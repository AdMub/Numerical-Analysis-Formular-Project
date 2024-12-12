#Error_T = -((b - a)^3 / (12 * n^2)) * f''(c)

def estimate_trapezoidal_error(func, a, b, n):
    """
    Estimate the error in the Trapezoidal Rule approximation.

    :param func: The function being integrated.
    :param a: The lower limit of integration.
    :param b: The upper limit of integration.
    :param n: The number of subintervals used in the Trapezoidal Rule.
    :return: Estimated absolute error.
    """
    h = (b - a) / n
    c = (a + b) / 2  # Midpoint of the interval
    second_derivative = sp.diff(func, x, 2)  # Calculate the second derivative symbolically
    error = abs(-((b - a)**3 / (12 * n**2)) * second_derivative.evalf(subs={x: c}))
    return error

# User input (assuming you've already calculated the Trapezoidal approximation)
def trapezoidal_rule(func, a, b, n):
    """
    Calculate the definite integral of a function using the Trapezoidal Rule.

    :param func: The function to be integrated.
    :param a: The lower limit of integration.
    :param b: The upper limit of integration.
    :param n: The number of subintervals (steps).
    :return: The approximate integral value.
    """
    h = (b - a) / n
    integral = (func(a) + func(b)) / 2  # Include the endpoints

    for i in range(1, n):
        x_i = a + i * h
        integral += func(x_i)

    return h * integral

# User input
import sympy as sp  # You can use the SymPy library to define your function symbolically

x = sp.symbols('x')  # Define the variable x symbolically
func_expression = input("Enter the function to integrate in terms of 'x': ")
func = sp.sympify(func_expression)
a = float(input("Enter the lower limit of integration (a): "))
b = float(input("Enter the upper limit of integration (b): "))
n = int(input("Enter the number of subintervals (n): "))

# Convert the symbolic function to a lambda function for numerical evaluation
func_lambda = sp.lambdify(x, func, 'numpy')

result = trapezoidal_rule(func_lambda, a, b, n)



error_estimate = estimate_trapezoidal_error(func, a, b, n)
print(f"Estimated absolute error in Trapezoidal Rule approximation: {error_estimate}")
