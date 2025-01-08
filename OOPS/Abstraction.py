#Def: Abstraction refers to hiding the internal implementation details and showing only the required functionality. n abstract class is a class that cannot be instantiated.

#1.Partial Abstraction  2.Full Abstraction(Interface)
##Explain: An abstract class is a class that cannot be instantiated and may contain one or more abstract methods.

#1. Abstract classes can contain both abstract methods (which must be implemented by subclasses) and concrete methods (which can be used directly by subclasses).

from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    def description(self):
        print("This is a shape")
        
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
        
obj = Square(2)
obj.description()
print(obj.area())


#2. Interface : Python doesn't have a built-in interface keyword like Java, but we can achieve interface-like behavior using abstract classes where all methods are ab
from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
        
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
        
    def perimeter(self):
        return self.side * 4
        
obj = Square(2)
print(obj.area())
print(obj.perimeter())
