def everetts_interpolation(x_values, y_values, target_x):
    result = 0.0
    n = len(x_values)

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term = term*(target_x-x_values[j])/(x_values[i] - x_values[j])
        result += term

    return result


w = int(input("How many data points are you working with: "))
x_values = []
y_values = []
d = 0

for c in range(w):
    x = float(input(f'input the value of x{d+1}: '))
    y = float(input(f'input the value of y{d+1}: '))
    x_values.append(x)
    y_values.append(y)
    d +=1

target_x = float(input('What is the number to interpolate at: '))

interpolated_value = everetts_interpolation(x_values, y_values, target_x)
print(f"Interpolated value at x = {target_x}: {interpolated_value}")

