s='welcome to revature'
print(s[1])
print(s[-2])

#list
l=[(1,2,3),(3,4,5),'hii',1.0]
print(l)
l.append('world')
print(l)
l.extend('rev')
print(l)
l.remove('r')
print(l)
l.pop()
print(l)
l.insert(1,'sreeja')
print(l)
l.reverse()
print(l)
print(len(l))


a=['hii','hello','hey']
print(a[1])
print(a[0])
print(a[-4]) #index out of range

#tuple
t=(1,2,3,4)
print(t[1])
print(t[-2])

#boolean
valid=True
invalid=False
print(type(True))
print(type(invalid))
print(type(valid))

#set
s=set()
s=set("hellowelcomehello")
print(s)
s1=set(['hii','hello','hii'])
print(s1)

#str
s='sreeja enabothula'
print(s[0])
print(s[1:6])
print(s.upper())
print(s.lower())
print(s.format())
print(s.capitalize())
print(s.count(s))
print(len(s))
print(s.find('a'))
print(s.replace('sreeja','hello'))
print(s.rstrip())
print(s.lstrip())

#range
n=range(1,10,2)
print(list(n))

#frozenset
fs=frozenset({1,2,3})
print(fs)
fs.add(4) #error it is immutable

#dictionary
d={'name':'sreeja','age':22,'city':'warangal'}
print(d)
print(d['name'])

#binary
b=([65,66,67])
print(b)
c=bytes([65,66,67])
print(c)

#none
x=None
y
print(y)
print(type(x))
print(type(y))

a=20
b=33
if b>a:
    print('b is greater than a')
elif a ==b:
    print('a is equal to b')
else:
    print('a is greater than b')

i=8
if i!=0:
    if i>0:
        print('positive')
if i==0:
    if i<0:
        print('negative')
    else:
        print('i is 0')
        
n=5
while n>0:
    n-=1
    if n==2:
        break
    
    print(n)
print('end loop')

n=5
while n>0:
    n-=1
    if n==2:
        continue
    
    print(n)
print('end loop')

t=('apple','banana','graphs')
for i in t:
    print(i)

x=[1,2]
y=[3,4]
for i in x:
    for j in y:
        print(i,j)

s={1:'sree',2:'ja',3:'hey'}
for k in s:
    print(k)

def hi():
    print('good afternoon')
hi()

def hi(name):
    print('good afternoon',name)
hi('sreeja')

def add(a,b):
    return a+b
res=add(2,3)
print('sum:',res)

def hi(name='guest'):
    print('good afternoon',name)
hi()
hi('sreeja')

def det():
    name='sreeja'
    age=22
    return name,age
n,a=det()
print('name:',n,'age:',a)

def all(*n):
    return sum(n) #predefined function -- sum
print(all(1,2,3,4,5))

def info(**details):
    for key,values in details.items():
        print(key,':',values)
info(name='sreeja',age=22)

#array
import array
a=array.array('u','applebanana') #type error and u-unicode, i-int
for a in a:print(a[0])

a=array.array('i',[2,4,5,22,3,1])
print(a[2])
print(len(a))
sort=sorted(a)
print(sort)