def double(x):
    return x * 2


sequence = [1, 3, 5, 9]

doubled = [
    double(x) for x in sequence
]

# Using FP like

doubled = list(map(double, sequence))

# Using Lambda Syntax

doubled = list(map(lambda x: x * 2, sequence))
