# List

def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total


# Dict

def named(**kwargs):
    print(kwargs)


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


print_nicely(name="Bob", age=25, test='Test')
