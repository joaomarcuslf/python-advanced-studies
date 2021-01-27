from abc import ABCMeta, abstractmethod


class IGraphic(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def print():
        """print information"""


class Ellipse(IGraphic):
    def print(self):
        print("Ellipse")


class Circle(IGraphic):
    def print(self):
        print("Circle")


class CompositeGraphic(IGraphic):
    def __init__(self):
        self.child_graphics = []

    def add(self, graphic):
        self.child_graphics.append(graphic)

    def print(self):
        for g in self.child_graphics:
            g.print()


""" USAGE:
ellipse1 = Ellipse()
circle1 = Circle()

composite1 = CompositeGraphic()
composite1.add(ellipse1)

composite2 = CompositeGraphic()

composite2.add(circle1)
composite2.add(composite1)

composite2.print()
"""

""" from: https://github.com/Sean-Bradley/Design-Patterns-In-Python/blob/master/composite/composite.py"""
