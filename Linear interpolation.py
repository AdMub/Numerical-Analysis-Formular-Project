def linear_interpolation(x1, y1, x2, y2, x):
    """
    Linear interpolation to estimate y for a given x between (x1, y1) and (x2, y2).

    :param x1: X-coordinate of the first known point.
    :param y1: Y-coordinate of the first known point.
    :param x2: X-coordinate of the second known point.
    :param y2: Y-coordinate of the second known point.
    :param x: The value at which you want to interpolate.
    :return: Estimated y value.
    """
    if x1 == x2:
        return y1  # Avoid division by zero

    return y1 + (y2 - y1) * (x - x1) / (x2 - x1)

# User input for known data points and the value to interpolate
x1 = float(input("Enter x0: "))
y1 = float(input("Enter y0: "))
x2 = float(input("Enter x1: "))
y2 = float(input("Enter y1: "))
x_interpolate = float(input("Enter the value to interpolate: "))

# Perform linear interpolation
result = linear_interpolation(x1, y1, x2, y2, x_interpolate)

print(f"Estimated y value at x = {x_interpolate}: {result}")
