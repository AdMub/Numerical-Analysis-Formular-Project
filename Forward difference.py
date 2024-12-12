def forward_difference_interpolation(x0, h, y_values, x):
    """
    Forward Difference interpolation to estimate y for a given x using equally spaced data points.

    :param x0: The initial X-coordinate of the first known point.
    :param h: The spacing between data points.
    :param y_values: List of Y-values of known points.
    :param x: The value at which you want to interpolate.
    :return: Estimated y value.
    """
    n = len(y_values)
    t = (x - x0) / h

    result = 0.0

    for i in range(n):
        term = y_values[i]
        for j in range(i):
            term *= (t - j)
            term /= (j + 1)
        result += term

    return result

# User input for the initial X, spacing, and the number of data points
x0 = float(input("Enter the initial X (x0): "))
h = float(input("Enter the spacing (h): "))
n = int(input("Enter the number of data points: "))

y_values = []

# Input data points
for i in range(n):
    y = float(input(f"Enter y{i+1}: "))
    y_values.append(y)

x_interpolate = float(input("Enter the value to interpolate: "))

# Perform Forward Difference interpolation
result = forward_difference_interpolation(x0, h, y_values, x_interpolate)

print(f"Estimated y value at x = {x_interpolate}: {result}")
