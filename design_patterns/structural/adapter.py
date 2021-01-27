# Deprecated
class ClassA:
    def method_a(self, email, name):
        print(f"method A: {email} {name}")

# New Module to be adapted


class ClassB:
    def method_b(self, name, email):
        print(f"method B: {email} {name}")


class ClassBAdapter(ClassB):
    def __init__(self):
        self.class_b = ClassB()

    def method_a(self, email, name):
        self.class_b.method_b(name, email)

    def method_a(self, name, email):
        self.class_b.method_b(name, email)


""" USAGE:
module = ClassBAdapter()

module.method_a("João", "joaomarcuslf")
"""
