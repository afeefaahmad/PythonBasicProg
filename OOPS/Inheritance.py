class A:
    def func1(self):
        print('A')
class B:
    def func2(self):
        print('B')
class C(A):
    def func3(self):
        print('C') #single inheritance
    
class D(A,B):
    def func4(self):
        print('D')  #multiple inheritance
class E(C):
    def func5(self):
        print('E')  #multilevel inheritance
        
obj1 = C()
obj1.func1()    #single inheritance

obj2 = D()
obj2.func1()
obj2.func2()    #multiple inheritance

obj3 = E()
obj3.func3()
obj3.func1()    #multilevel inheritance

#Hybrid: combination of multiple inheritance
#Multiple class inherited from same Parent class
