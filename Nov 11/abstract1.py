from abc import ABC,abstractmethod
class Process(ABC):
    @abstractmethod
    def Square(x):
        return x**2
class child_process(Process):
    def Square(x):
        return Process.Square(x)
    xyz= 142.165
obj = child_process
# print(obj.Square(12))