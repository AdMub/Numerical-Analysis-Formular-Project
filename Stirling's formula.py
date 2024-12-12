import math

def stirling_approximation(n):
    """
    Calculate an approximation of n! using Stirling's formula.

    :param n: The number for which to estimate the factorial.
    :return: The estimated factorial value.
    """
    if n == 0:
        return 1
    else:
        return math.sqrt(2 * math.pi * n) * (n / math.e)**n

# User input
n = int(input("Enter a non-negative integer (n) to estimate n!: "))
result = stirling_approximation(n)
print(f"{n}! (Stirling's Approximation): {result}")
