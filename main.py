from abc import ABC, abstractmethod
class Absclass(ABC):
    def display(self,x):
        print("Passed value is",x)
    @abstractmethod
    def task(self):
        print("This is an abstract-class it hides unnessary infomation!")
class test(Absclass):
    def task(self):
        print("This is a test Class")
one=test()
one.task()
one.display(78)
