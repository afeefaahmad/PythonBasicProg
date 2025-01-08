OOP Concepts Involved in super().__init__()
1. Inheritance
When a child class inherits from a parent class, it can reuse the properties and methods of the parent class. Using super().__init__(), we can initialize the parent class attributes without rewriting its logic in the child class.

Example (Inheritance):

python
Copy code
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call Parent's constructor
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Create an instance of Child
child = Child("Alice", 10)
child.display()  # Output: Name: Alice, Age: 10
Explanation:
The Child class inherits from Parent.
super().__init__(name) calls the constructor of Parent and initializes name.
The Child class then initializes age separately.
This avoids duplicating the logic of initializing name in both classes.
2. Encapsulation
Encapsulation refers to bundling data (attributes) and methods into a single unit (class) while restricting direct access to some of the attributes.

Example (Encapsulation with Private Attributes):

python
Copy code
class Parent:
    def __init__(self, name):
        self.__name = name  # Private attribute

    def get_name(self):
        return self.__name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call Parent's constructor
        self.age = age

    def display(self):
        print(f"Name: {self.get_name()}, Age: {self.age}")

# Create an instance of Child
child = Child("Bob", 12)
child.display()  # Output: Name: Bob, Age: 12
Explanation:
Parent has a private attribute __name and a public method get_name() to access it.
The child class uses super().__init__(name) to initialize __name indirectly, maintaining encapsulation.
3. Polymorphism
Polymorphism allows a method to behave differently based on the class it belongs to. Using super(), we can call overridden methods of the parent class from the child class.

Example (Polymorphism with Method Overriding):

python
Copy code
class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}.")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call Parent's constructor
        self.age = age

    def greet(self):
        super().greet()  # Call Parent's greet method
        print(f"I am {self.age} years old.")

# Create an instance of Child
child = Child("Charlie", 8)
child.greet()
Output:

plaintext
Copy code
Hello, I am Charlie.
I am 8 years old.
Explanation:
The greet() method in Child overrides the method in Parent.
super().greet() calls the parent class’s greet() method first, followed by the child class’s specific implementation.
4. Code Reusability
Using super().__init__() promotes code reuse by allowing a child class to inherit and extend the functionality of a parent class without duplicating code.

Example (Code Reusability):

python
Copy code
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)  # Reuse Vehicle's constructor
        self.doors = doors

    def display_info(self):
        super().display_info()  # Reuse Vehicle's display_info method
        print(f"Doors: {self.doors}")

# Create an instance of Car
car = Car("Toyota", "Corolla", 4)
car.display_info()
Output:

plaintext
Copy code
Brand: Toyota, Model: Corolla
Doors: 4
Explanation:
The Car class reuses the Vehicle class’s constructor and display_info() method by using super().__init__() and super().display_info().
This reduces code duplication and improves maintainability.
When to Use super().__init__()
When a child class extends the functionality of a parent class.
Instead of rewriting the parent’s initialization logic, use super().__init__() to reuse it.

When dealing with multiple inheritance.
In Python, super() handles the Method Resolution Order (MRO), ensuring that the correct parent class's constructor is called in a consistent order.

Example (Multiple Inheritance with MRO):

python
Copy code
class A:
    def __init__(self):
        print("A's constructor")

class B(A):
    def __init__(self):
        super().__init__()  # Call A's constructor
        print("B's constructor")

class C(B):
    def __init__(self):
        super().__init__()  # Call B's constructor
        print("C's constructor")

# Create an instance of C
c = C()
Output:

plaintext
Copy code
A's constructor
B's constructor
C's constructor
Explanation:
super().__init__() ensures that the constructors of all parent classes are called in the correct order based on Python's MRO.
