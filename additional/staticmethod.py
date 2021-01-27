class ClassTest:
    @staticmethod
    def static_method():
        print(f"Called static_method. We don't get any object or class info here.")


ClassTest.static_method()
