from abc import ABCMeta, abstractstaticmethod


class TableFactory():
    def get_table(self, furniture):
        print(f"Starting: get_table - {furniture}")


class ChairFactory():
    def get_chair(self, furniture):
        print(f"Starting: get_chair - {furniture}")


class IFurnitureFactory(metaclass=ABCMeta):
    @abstractstaticmethod
    def get_furniture(furniture):
        pass


class FurnitureFactory(IFurnitureFactory):
    @staticmethod
    def get_furniture(furniture):
        try:
            if furniture in ["SmallChair", "MediumChair", "BigChair"]:
                return ChairFactory().get_chair(furniture)
            if furniture in ["SmallTable", "MediumTable", "BigTable"]:
                return TableFactory().get_table(furniture)
            raise AssertionError("No Furniture Factory Found")
        except AssertionError as _e:
            print(_e)
        return None


""" USAGE:
FurnitureFactory.get_furniture("SmallChair")
"""
