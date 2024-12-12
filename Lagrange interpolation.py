def lagrange_interpolation(x_values, y_values, x):
    """
    Lagrange interpolation to estimate y for a given x using multiple known data points.

    :param x_values: List of X-coordinates of known points.
    :param y_values: List of Y-coordinates of known points.
    :param x: The value at which you want to interpolate.
    :return: Estimated y value.
    """
    n = len(x_values)
    result = 0.0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result

# User input for the number of data points
n = int(input("Enter the number of data points: "))

x_values = []
y_values = []

# Input data points
for i in range(n):
    x = float(input(f"Enter x{i+1}: "))
    y = float(input(f"Enter y{x}: "))
    x_values.append(x)
    y_values.append(y)

x_interpolate = float(input("Enter the value to interpolate: "))

# Perform Lagrange interpolation
result = lagrange_interpolation(x_values, y_values, x_interpolate)

print(f"Estimated y value at x = {x_interpolate}: {result}")
