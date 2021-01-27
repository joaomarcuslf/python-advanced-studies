from abc import ABC, abstractmethod


class Context:
    _state = None

    def __init__(self, state):
        self.transition_to(state)

    def transition_to(self, state):
        self._state = state
        self._state.context = self

    def state1(self):
        self._state.handle1()

    def state2(self):
        self._state.handle2()


class State(ABC):
    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context):
        self._context = context

    @abstractmethod
    def handle1(self):
        pass

    @abstractmethod
    def handle2(self):
        pass


class ConcreteStateA(State):
    def handle1(self):
        print("Doing Something to go to a new state...")
        self.context.transition_to(ConcreteStateB())

    def handle2(self):
        print("Handle2: ConcreteStateA")
        pass


class ConcreteStateB(State):
    def handle1(self):
        print("Handle1: ConcreteStateB")
        pass

    def handle2(self):
        print("Doing Something to go to a new state...")
        self.context.transition_to(ConcreteStateA())


""" USAGE:
context = Context(ConcreteStateA())

context.state1()
context.state1()

context.state2()
context.state2()
"""
