import numpy as np
#import math
"""
    Linear Iteration (Fixed-Point Iteration) method for finding the root of a function.
    :param g: The iterative function g(x).
    :param x0: Initial guess for the root.
    :param tolerance: The desired level of accuracy.
    :param max_iterations: The maximum number of iterations.
    :return: Approximation of the root.
    """


max_iterations = 25
quest = int(input("Enter the degree of the polynomial: "))
numbers = []
for i in range(quest + 1):
    nums = float(input(f"Enter the coefficient for x^{quest}: "))
    quest -= 1
    numbers.append(nums)
    # return numbers.reverse()
num = np.poly1d(numbers)
print(num)
equation_str = input("Enter the equation in terms of x = f(x) using 'x' as the variable: ")
x_value = float(input("Enter the value of the initial guess 'x': "))
# Define a lambda function to evaluate the user's equation
for i in range(max_iterations):
    try:
        equation = lambda x: eval(equation_str)
        result = float(equation(x_value))
        result = float(f'{result:.4f}')
        x_value = float(f'{x_value:.4f}')
        if x_value == result:
            print(f'The root of the equation is {result}')
            break
        else:
            x_value = result

    except (NameError, SyntaxError):
        print("Invalid equation. Please check your input and try again.")
