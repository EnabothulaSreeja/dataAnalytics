# str
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

#tuple functions
t=(1,2,3,4,2)
print(t[1])
print(t[-2])
print(t.count(2))
print(max(t))
print(min(t))
print(sum(t))
print(sorted(t))

#grade
a=int(input('enter number:'))
if a>=90 and a<=100:
    print('grade A')
elif a>=80 and a<=70:
    print('grade B')
elif a>=60 and a<=70:
    print('grade C')
else:
    print('fail')

#reverse 
a=input('enter:')
print(a[::-1])

rev=a[::-1]
#palindrome
if a==rev:
    print('palindrome')
else:
    print('not palindrome')

#prime
n=int(input('n:'))
for i in range(2,n):
    if n%i==0:
        print('not prime')
        break
    else:
        print('prime')
        break

#fibonacci
a=0
b=1
for i in range(1,11):
    c=a+b
    print(c)
    a=b
    b=c

#even and odd
a=2
b=3
if a%2==0:
    print('even')
if b%2!=0:
    print('odd')

# 1 to 100 even @
for i in range(2,100,2):
    print(i)
    print('@')

#collection iterate each element and square it
l=[1,2,3,4]
for i in l:
    print(i)
    print('square:',i*i)

#dictinary
d={'sreeja':'name','age':22,'hyd':'city'}
for k in d:
    print(k)
print(d['hyd'])
print(d['age'])
print(d['sreeja'])

#get data
name=input('name:')
age=input('age:')
address=input('address:')
def display():
    print(name)
    print(age)
    print(address)
display()