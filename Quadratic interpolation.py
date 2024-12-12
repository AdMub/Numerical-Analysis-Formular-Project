def quadratic_interpolation(x0, y0, x1, y1, x2, y2, x):
    """
    Quadratic interpolation to estimate y for a given x using three known points.

    :param x1: X-coordinate of the first known point.
    :param y1: Y-coordinate of the first known point.
    :param x2: X-coordinate of the second known point.
    :param y2: Y-coordinate of the second known point.
    :param x3: X-coordinate of the third known point.
    :param y3: Y-coordinate of the third known point.
    :param x: The value at which you want to interpolate.
    :return: Estimated y value.
    """
    L1 = ((x - x1) * (x - x2)) / ((x0 - x1) * (x0 - x2))
    L2 = ((x - x0) * (x - x2)) / ((x1 - x0) * (x1 - x2))
    L3 = ((x - x0) * (x - x1)) / ((x2 - x0) * (x2 - x1))

    result = y0 * L1 + y1 * L2 + y2 * L3
    return result

# User input for three known data points and the value to interpolate
x0 = float(input("Enter x0: "))
y0 = float(input("Enter y0: "))
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
x_interpolate = float(input("Enter the value to interpolate: "))

# Perform quadratic interpolation
result = quadratic_interpolation(x0, y0, x1, y1, x2, y2, x_interpolate)

print(f"Estimated y value at x = {x_interpolate}: {result}")
