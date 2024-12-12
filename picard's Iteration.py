import sympy as sp


def picards_iteration(func, y0, n):
    """
    Solve a first-order ODE using Picard's iteration.

    :param func: The ODE function y(x) = f(x, y).
    :param y0: Initial guess for the solution.
    :param n: Number of iterations.
    :return: Approximated solution after n iterations.
    """
    y = y0  # Initialize with the initial guess

    for i in range(n):
        y = func.subs(sp.Function('y')(x), y)  # Replace y(x) with the current estimate

    return y


# User input
x = sp.symbols('x')
y = sp.Function('y')(x)

ode_expression = input("Enter the ODE in the form y(x) = f(x, y), e.g., y(x) = x - y(x): ")
ode = sp.Eq(y, sp.sympify(ode_expression))

initial_guess = sp.sympify(input("Enter the initial guess for y(x): "))
num_iterations = int(input("Enter the number of iterations: "))

# Convert the symbolic ODE to a function for iterative evaluation
ode_func = sp.lambdify(x, ode.rhs, 'numpy')
# Convert the initial guess to a numeric value
y0 = float(initial_guess)
# Perform Picard's iteration
approximated_solution = picards_iteration(ode, y0, num_iterations)

print(f"Approximated solution after {num_iterations} iterations: y(x) = {approximated_solution}")
