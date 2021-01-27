class Subject:
    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def notifyAll(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)


class Observer:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        pass


class Observer1(Observer):
    def notify(self, subject, *args):
        print(type(self).__name__, ':: Got', args, 'From', subject)


class Observer2(Observer):
    def notify(self, subject, *args):
        print(type(self).__name__, ':: Got', args, 'From', subject)


""" USAGE:
subject = Subject()

observer1 = Observer1(subject)
observer2 = Observer2(subject)

subject.notifyAll("notification")
"""
