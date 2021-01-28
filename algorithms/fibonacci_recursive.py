from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n - 2) + fibonacci(n - 1)


""" USAGE:
fibonacci(50)
"""

"""
This code was built based on the book:
- Classic Computer Science Problems in Python by David Kopec
"""
