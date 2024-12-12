import numpy as np

def bisection(a, b, max_iterations=25):
    quest = float(input("What is the degree of f(x): "))
    count = 0
    numbers = []
    print("input the coefficeint of the polynomial: ")
    while count < quest + 1:
        count += 1
        nums = float(input(""))
        numbers.append(nums)
    num = np.poly1d(numbers)

    if num(a) * num(b) >= 0:
        raise ValueError("The bisection method may not converge on the given interval.")
    for _ in range(max_iterations):
        mid = (a + b) / 2
        if num(mid) == 0:
            return mid
        elif num(a) * num(mid) < 0:
            b = mid
        else:
            a = mid

    return (a + b) / 2

# Input function as a lambda function
#user_function = lambda x: np.poly1d(numbers)

# Input interval [a, b]
a = float(input("Enter the left endpoint (a): "))
b = float(input("Enter the right endpoint (b): "))

root = bisection(a, b)

print(f"Approximate root: {root:.4f}")
