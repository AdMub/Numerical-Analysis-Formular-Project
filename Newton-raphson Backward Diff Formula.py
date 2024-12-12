def backward_difference_coefficients(y_values):
    """
    Calculate backward difference coefficients for Newton's divided difference interpolation.

    :param y_values: List of Y-values of known points.
    :return: List of backward difference coefficients.
    """
    n = len(y_values)
    coeffs = [y_values]

    for i in range(n - 1):
        next_row = []
        for j in range(len(coeffs[i]) - 1):
            diff = coeffs[i][j + 1] - coeffs[i][j]
            next_row.append(diff)
        coeffs.append(next_row)

    return [row[-1] for row in coeffs]

def newton_raphson_backward_difference(x0, h, y_values, x):
    """
    Newton-Raphson method with backward difference interpolation to estimate y for a given x.

    :param x0: The initial X-coordinate of the first known point.
    :param h: The spacing between data points.
    :param y_values: List of Y-values of known points.
    :param x: The value at which you want to interpolate.
    :return: Estimated y value.
    """
    n = len(y_values)
    t = (x - x0) / h

    backward_coeffs = backward_difference_coefficients(y_values)
    result = backward_coeffs[0]

    for i in range(1, n):
        term = backward_coeffs[i]
        for j in range(i):
            term *= (t + j) / (j + 1)
        result += term

    return result

# User input for the initial X, spacing, and the number of data points
x0 = float(input("Enter the initial X (x0): "))
h = float(input("Enter the spacing (h): "))
n = int(input("Enter the number of data points: "))

y_values = [ ]

# Input data points
for i in range(n):
    y = float(input(f"Enter y{i+1}: "))
    y_values.append(y)

x_interpolate = float(input("Enter the value to interpolate: "))

# Perform Newton-Raphson method with backward difference interpolation
result = newton_raphson_backward_difference(x0, h, y_values, x_interpolate)

print(f"Estimated y value at x = {x_interpolate}: {result}")
