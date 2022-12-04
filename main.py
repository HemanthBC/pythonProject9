# Recursion Exercise 1
# Problem
# Write a recursive function called recursive_sum that takes an integer as a parameter. Return the sum of all integers between 0 and the number passed to recursive_sum.
# Expected Output
# •	If the function call is recursive_sum(5), then the function would return 15
# •	If the function call is recursive_sum(10), then the function would return 55


def recursive_sum(n):
    if n < 1:
        return 0

    else:
        return n + recursive_sum(n - 1)

print(recursive_sum(10))
# gives 55 as answer
