def greet(*args, greeting="Hello"):
    for name in args:
        print(f"{greeting}, {name}")


greet('João', 'Letícia')
greet('João', 'Letícia', greeting="Hi")
