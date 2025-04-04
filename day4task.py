#single inheritance
class Parent:
    def display(self):
        print("Parent Class")

class Child(Parent):
    print('class child')
obj = Child()
obj.display()

#multiple
class A:
    def methodA(self):
        print("Class A")
class B:
    def methodB(self):
        print("Class B")
class C(A, B):
    print('class C')
obj = C()
obj.methodA()  
obj.methodB()

#multilevel
class GrandParent:
    def grandparent_method(self):
        print("Grandparent Class")
class Parent(GrandParent):
    def parent_method(self):
        print("Parent Class")
class Child(Parent):
    def child_method(self):
        print('child class')
obj = Child()
obj.grandparent_method() 

#hierarchical
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating.")
    def sleep(self):
        print(f"{self.name} is sleeping.")
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def bark(self):
        print(f"{self.name} the {self.breed} is barking.")
dog = Dog("Max", "Golden Retriever")
dog.eat()
dog.bark()

#method overloading
def product(a,b):
    p=a*b
    print(p)
product(2,3)
def product(a,b,c):
    p=a*b*c
    print(p)
product(3,5,2)

#method overriding
class Parent: 
    def myMethod(self):
        print ('Calling parent method')
class Child(Parent): 
    def myMethod(self):
        print ('Calling child method')
c = Child() 
c.myMethod() # child calls overridden method

#polymorphism
class Bird:
    def intro(self):
        print('type of bird')
    def flight(self):
        print('most birds can fly but some cannot')
class sparrow(Bird):
    def flight(self):
        print('sparrows can fly')
class ostrish(Bird):
    def flight(self):
        print('ostriches cannot fly')
b=Bird()
s=sparrow()
o=ostrish()
b.intro()
b.flight()
s.intro()
s.flight()
o.intro()
o.flight()

#encapsulation
class Student:
    def __init__(self, name="Rajaram", marks=50):
        self.name = name
        self.marks = marks
s1 = Student()
s2 = Student("Bharat", 25)
print ("Name: {} marks: {}".format(s1.name, s2.marks))
print ("Name: {} marks: {}".format(s2.name, s2.marks))