def newton_raphson(func, func_prime, x0, tolerance=1e-6, max_iterations=100):
    """
    Newton-Raphson method for finding the root of a function.

    :param func: The function for which you want to find the root.
    :param func_prime: The derivative of the function.
    :param x0: Initial guess for the root.
    :param tolerance: The desired level of accuracy.
    :param max_iterations: The maximum number of iterations.
    :return: Approximation of the root.
    """
    x = x0
    for i in range(max_iterations):
        fx = func(x)
        if abs(fx) < tolerance:
            return x
        fpx = func_prime(x)
        if fpx == 0:
            # Avoid division by zero
            return None
        x = x - fx / fpx
    return None  # Root not found within the maximum number of iterations

# Example usage:
def sample_function(x):
    return x**3 - 2*x**2 + 4

def sample_function_prime(x):
    return 3*x**2 - 4*x

initial_guess = 1.5
root = newton_raphson(sample_function, sample_function_prime, initial_guess)

if root is not None:
    print(f"Approximate root: {root}")
else:
    print("Root not found within the maximum number of iterations.")
