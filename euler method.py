def euler_method(func, x0, y0, x_end, h):
    """
    Solve a first-order ODE using the Euler method.

    :param func: The ODE function f(x, y).
    :param x0: Initial x value.
    :param y0: Initial y value.
    :param x_end: Final x value.
    :param h: Step size.
    :return: Lists of x and y values representing the solution.
    """
    x_values = [x0]
    y_values = [y0]

    while x0 < x_end:
        y0 = y0 + h * func(x0, y0)
        x0 = x0 + h

        x_values.append(x0)
        y_values.append(y0)

    return x_values, y_values

# User input
import sympy as sp

x = sp.symbols('x')
y = sp.Function('y')(x)

ode_expression = input("Enter the ODE in the form of y' = f(x, y), e.g., y' = x - y: ")
ode = sp.Eq(y.diff(x), sp.sympify(ode_expression))

x0 = float(input("Enter the initial x value: "))
y0 = float(input("Enter the initial y value: "))
x_end = float(input("Enter the final x value: "))
step_size = float(input("Enter the step size (h): "))

# Convert the symbolic ODE to a lambda function for numerical evaluation
ode_func = sp.lambdify((x, y), ode.rhs, 'numpy')

x_values, y_values = euler_method(ode_func, x0, y0, x_end, step_size)

# Print the results
for x, y in zip(x_values, y_values):
    print(f"x = {x}, y = {y}")
