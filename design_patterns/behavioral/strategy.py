def add(*args):
    result = 0

    for num in args:
        result += num

    return result


def subtract(*args):
    result = 0

    for num in args:
        result -= num

    return result


class Startegy:
    def execute(self, *args, key):
        if key == 'add':
            return add(*args)
        elif key == 'subtract':
            return subtract(*args)
        else:
            return f"No Key in strategy"


""" USAGE:
strategy = Startegy()

print(strategy.execute(1, 2, 3, 5, key="add"))
print(strategy.execute(1, 2, 3, 5, key="subtract"))
"""
