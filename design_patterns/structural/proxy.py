from abc import ABCMeta, abstractmethod
import datetime


class IComponent(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def method(self):
        """A method to implement"""


class Component(IComponent):
    def method(self):
        print("The method has been called")


class ProxyComponent(IComponent):
    def __init__(self):
        self.component = Component()

    def method(self):
        f = open("log.txt", "a")
        f.write("%s : method was proxied\n" % (datetime.datetime.now()))
        self.component.method()


""" USAGE:
component1 = Component()
component1.method()

component2 = ProxyComponent()
component2.method()
"""

""" from: https://github.com/Sean-Bradley/Design-Patterns-In-Python/blob/master/proxy/proxy.py """
