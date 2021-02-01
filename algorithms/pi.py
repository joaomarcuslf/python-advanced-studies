def pi_digits(term):
    if term <= 0:
        yield 3
        yield 0
        return
    elif term == 1:
        yield 3
        yield 1
        return

    k, a, b, a1, b1 = 2, 4, 1, 12, 4

    while term > 0:
        p, q, k = k * k, 2 * k + 1, k + 1
        a, b, a1, b1 = a1, b1, p*a + q*a1, p*b + q*b1
        digit, digit_check = a/b, a1/b1

        while digit == digit_check and term > 0:
            yield int(digit)

            term -= 1
            a, a1 = 10*(a % b), 10*(a1 % b1)
            digit, digit_check = a/b, a1/b1


def pi(nth_term):
    digits = [str(n) for n in list(pi_digits(nth_term))]
    return "%s.%s\n" % (digits.pop(0), "".join(digits))


""" USAGE:
print(pi(0))
print(pi(1))
print(pi(2))
print(pi(3))
print(pi(4))
print(pi(5))
print(pi(6))
print(pi(7))
print(pi(8))
print(pi(9))
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
"""

"""
This code was built based on the book:
- Classic Computer Science Problems in Python by David Kopec
"""
