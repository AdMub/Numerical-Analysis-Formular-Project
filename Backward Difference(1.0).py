def backward_difference(f, x, h):
    """
    Calculate the derivative of a function using the backward difference method.

    :param f: The function to differentiate.
    :param x: The point at which to estimate the derivative.
    :param h: The step size.
    :return: The approximate derivative.
    """
    df = (f(x) - f(x - h)) / h
    return df

# User input
def user_function(x):
    return x**2  # Replace this with your desired function

x_value = float(input("Enter the value of x: "))
step_size = float(input("Enter the step size (h): "))

result = backward_difference(user_function, x_value, step_size)
print(f"The derivative at x = {x_value} is approximately {result}")
