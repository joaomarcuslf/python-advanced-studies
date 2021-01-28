def fibonacci(n):
    if n == 0:
        return 0

    last = 0
    next = 1

    for _ in range(1, n):
        last, next = next, last + next

    return next


""" USAGE:
fibonacci(50)
"""

"""
This code was built based on the book:
- Classic Computer Science Problems in Python by David Kopec
"""
