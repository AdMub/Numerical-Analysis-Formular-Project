import numpy as np  # we import the library numerical python that can assist in
# constructing algebraic equations in python


# we define a function, and we name it bisection, which takes in three arguments.
def bisection(a, b, max_iterations=25):

    poly_deg = int(input("What is the degree of f(x): "))  # the user is requested to put in the degree of the
    # polynomial to which he wants to solve, and the 'int' functions helps to convert whatever numerical value inputted,
    # to an integer value that can be used subsequently

    power = poly_deg  # the value of the degree, is then ascribed to another variable 'power', which is the power of the
    # polynomial varying

    count = 0  # since we will be working with loops in these codes, certain conditions has to be put in place to try
    # to regulate the loop in an appropriate manner.

    numbers = []  # the library "numpy" essentially works with lists, so a list has to be built by the user, to make the
    # codes to a dynamic one, allowing multiple usage.

    while count < poly_deg + 1:  # we start the while loop with this condition

        print(f"input the coefficient of X^{power}: ")  # the user is prompted to give a specific value

        nums = float(input(""))  # the user is requested for the value of the coefficient of the certain "x" to what
        # ever degree, and the number is converted to a "float type", which allows python to read the entry as a decimal

        numbers.append(nums)  # the value of the coefficient is added to the list initially defined as being empty,
        # therefore the building of the list begins

        power -= 1  # every loop,the value of 'power' is reduced by one
        count += 1  # every loop, the value of 'count' is increased by one
    num = np.poly1d(numbers)  # the line comes in play when the loop is completed. the values in the list built is used
    # by the library 'numpy' to construct the polynomial.

    if num(a) * num(b) >= 0:  # this is to put the condition to which root bisection method will work into play
        raise ValueError("The bisection method may not converge on the given interval.")
    for _ in range(max_iterations):  # another loop is initiated to the certain numbers of iterations initially defined
        mid = (a + b) / 2
        if num(mid) == 0:
            return mid
        elif num(a) * num(mid) < 0:
            b = mid
        else:
            a = mid

    return (a + b) / 2

# Input function as a lambda function
# user_function = lambda x: np.poly1d(numbers)


# Input interval [a, b]
a = float(input("Enter the left endpoint (a): "))  # the user is prompted for the left end of the interval in which the
# root is to be calculated
b = float(input("Enter the right endpoint (b): "))  # the user is prompted for the right end of the interval in which
# the root is to be calculated

root = bisection(a, b)  # the funtion initially defined is called into action at this point, and every line of code in
# the function block is ran by the IDE


print(f"Approximate root: {root:.4f}")  # this line of code prints out the final root of the equation, corrected to 4d.p
