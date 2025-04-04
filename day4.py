#lambda
s1='good morning'
s2=lambda func:func.upper()
print(s2(s1))

n=lambda x:'positive' if x>0 else 'negative' if x<0 else 'zero'
print(n(5))
print(n(-3))
print(n(0))

sq=lambda x:x**2
print(sq(3))

def sq(x):
    return x**2
print(sq(2))

l=[lambda arg=x:arg*10 for x in range(1,5)] #without [] will get error
for i in l:
    print(i()) #to readable form we have to call i()

check=lambda x:'even' if x%2==0 else 'odd'
print(check(2))
print(check(3))

#lambda with multiple elements
cal=lambda x,y:(x+y,x-y,x*y)
res=cal(2,4)
print(res)

n=[1,2,3,4,5]
even=filter(lambda x:x%2==0,n) #filter() applies this condition and returns only the satisfied values
print(even) #non readable 
print(list(even))

a=[1,2,3,4,5,6]
b=map(lambda x:x*2,a) #map() iterates through a and applies the transformation
print(list(b))

from functools import reduce
a=[1,2,3,4]
b=reduce(lambda x,y:x*y,a) #reduce applies this operation across the list
print(b)

a='revature'
b=22
msg='my name is [0] and i am [1] year old'.format(a,b)
print(msg)

a='python'
print('this article is  written in {}'.format(a))
print('hi my name is {} and i amm {} years old'.format('user',12))

#fstring
name='cm'
age=22
print(f'hello,my name is {name} and i am {age} years old')

def fun(msg):
    def fun1():
        print(msg)
    fun1()
fun('hello')
print('-----------')

import inspect
def decorator(func):
    def wrapper():
        print('before calling the function')
        func()
        print('after calling')
    return wrapper
@decorator #applying decorator to function
def greet():
    print('hello')
greet()
print(inspect.signature(decorator))
    
#OOPS
class Dog:
    sound='bark'
d1=Dog()
print(d1.sound)
print('-----------')
class Dog:
    species='canine'
    def __init__(self,name,age): #self refers to the current instance of class
        self.name=name
        self.age=age
    def __str__(self): #tostring()
        return f'{self.name} is {self.age} years old'
d1=Dog('buddy',3)
d2=Dog('char',2)
print(d1.name)
print(d1.species)
print(d1)
print(d2)

#modify class and instance variable
d1.name='max'
print(d1.name)
Dog.species='german'
print(Dog.species)
print('---------')

class Animal:
    def __init__(self,name):
        self.name=name
class Cat(Animal):
    def sound(self):
        return 'meow'
a=Animal('generic animal')
c=Cat('tommy')
print(a.name)
print(c.name)
print(c.sound())

class Color:
    def __init__(self):
        self.name='green'
        self.lg=self.Lightgreen()
    def show(self):
        print('name:',self.name)
    class Lightgreen:
        def __init__(self):
            self.name='Lightgreen'
            self.code='024avc'
        def display(self):
            print('name:',self.name)
            print('code:',self.code)
outer=Color()
outer.show()
g=outer.lg
g.display()

class Parent():
    def show(self):
        print('inside parent')
class Child(Parent):
    def show(self):
        super().show()
        print('inside child')
o=Child()
o.show()

class Private:
    def __init__(self):
        self.__salary=500
    def salary(self):
        return self.__salary
obj=Private()
print(obj.salary())
#print(obj.__salary) #attribute error

class Protected:
    def __init__(self):
        self._salary=5000
    def salary(self):
        return self._salary
obj=Protected()
print(obj.salary())
#print(obj._salary)

#iterator 
n=[1,2,3,4,5]
iter_n=iter(n)
print(next(iter_n))
print(next(iter_n))

#local scope
def my():
    x=300
    print(x)
my()

#enclosing scope
def myf():
    x=300.0
    def myinner():
        print(x)
    myinner()
myf()

#global scope
x=30
def myfun():
    print(x) 
myfun()
print(x)

#module
#sample.py
def addition():
    print('inside add')
def sub(a,b):
    print('inside sub')
    print(a,b)
#example.py
import sample
sample.addition()
from sample import sub
sub(4,1)

#math module
import math
ceil=math.ceil(4.3)
print(ceil)
floor=math.floor(4.8)
print(floor)

import numpy as np
arr=np.array([1,2,3])
print(arr)
print(type(arr))
print('------')
a=np.zeros((2,3))
print(a)
b=np.ones((3,2))
print(b)
c=np.arange(0,10,2)
print(c)
d=np.linspace(0,1,5)
print(d)
e=np.random.rand(2,2)
print(e)
f=np.array([1,2,3])
g=np.array([4,5,6])
print(f+g)
print(f*g)
print(f**2)
print(np.sqrt(f))
a=np.array([[1,2],[3,4]])
b=np.array([[2,0],[1,3]])
print(np.dot(a,b))
print(np.transpose(a))
print(np.linalg.inv(a))
arr=np.array([[10,20,30],[40,50,60]])
print(arr[0,1])
print(arr[:,1])
print(arr[1])
arr=np.array([1,2,3,4])
print(arr.mean())
print(arr.sum())
print(arr.std())
print(arr.max())
print(arr.min())


import pandas as pd
# s=pd.Series([10,20,30,40],index=['a','b','c','d'])
# print(s)
data={'name':['sreeja','bob','charlie'],
      'age':[12,23,44],
      'city':['hyd','london','paris']}
df=pd.DataFrame(data)
# print(df)
df.head()
df.tail(2)
df.info()
df.describe()
df.columns
df.shape
print(df['age'])
print(df[['name','city']])
print(df[df['age']>28])
df.iloc[1]
df.loc[1]
df['age']+=1
df['country']='usa'
df.rename(columns={'age':'years'},inplace=True)
df.drop('city',axis=1)
print(df)
