class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")


instance = ClassTest()
instance.instance_method()
instance.class_method()

ClassTest.class_method()
