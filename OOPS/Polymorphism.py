#Functions, methods or operators to behave differently based on the type of data they are handling

1. Compile-time-polymorphism (Overloading) : Python does not support method overloading directly (like in Java or C++),
    but it can be achieved using default arguments or variable-length arguments.

class Calculator:
    def add(self,a,b,c=0):
        return a+b+c
        
obj = Calculator()
print(obj.add(5,10))
print(obj.add(5,10,1))

2. Run-time-polymorphism (Overriding) : A child class provides a specific implementation of a method that is already defined in its parent class.
class Parent:
    def show(self):
        print("Hello from Parent")

class Child(Parent):
    def show(self):
        print("Hello from Child")

obj = Child()
obj.show()  # Output: Hello from Child
#child overrides parent

******************************************************************
#To avoid above situation

