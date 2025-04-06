#json
import json
x='{"name":"xyz","age":35}'
z=json.loads(x)
print(z['name'])
print(z['age'])
x={
    "name":"xyz",
    "age": 35
}
y=json.dumps(x)
print(y)

import re
x='The rain in spain'
y=re.search("^The.*spain$",x)
if y:
    print('yes the match is correct')
else:
    print('not matching')
Y=re.findall("ai",x)
print(y)
print("----")
z=re.search("\s",x)
print(z)
d=re.split("\s",x)
print(d)
e=re.sub("\s","$",x)
print(e)

pattern=r"\d+"
text='there are 123 apples'
match=re.search(pattern,text)
if match:
    print("match found:",match.group())

pattern=r"\d+"
text='there are 123 apples and 456 oranges'
match=re.findall(pattern,text)
print(match)

pattern=r"(\d+)-(\d+)-(\d+)"
text='the event is on 2025-03-26'
match=re.search(pattern,text)
if match:
    print("year:",match.group(1))
    print("month:",match.group(2))
    print('day:',match.group(3))

email_pattern=r"[a-zA-Z0-9._%+-]  +@[a-zA-Z0-9.-]   +\.[a-zA-Z]{2,}"
text='please contact at example@example.com'
match=re.search(email_pattern,text)
if match:
    print('email found:',match.group())
    
logging
import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug('hello,debug!')
logging.info('hello,info!')
logging.warning('hello,warning')
logging.error('hello,error!')
logging.critical('hello,critical')

#creates file
logging.basicConfig(
    level=logging.DEBUG,
    filename='app.log',
    filemode='a',
    format='%(name)s-%(levelname)s-%(message)s')               
logging.debug('hello,debug!')
logging.info('hello,info!')
logging.warning('hello,warning')
logging.error('hello,error!')
logging.critical('hello,critical')

#pylint
import pylint
for n in range(11):
    print(n)
# covention - displayed when program is not following the standard rule
# refactor - displayed for bad code smell
# warning - displayed for python specific problem

try:
    x=10/0
except ZeroDivisionError:
    print('div by zero')
finally:
    print('completed')
    
try:
    n=int(input('n:'))
    result=10/n
except Exception as e:
    print('an unexcepted')
except ValueError as e:
    print('invalid:{e}')
except ZeroDivisionError as e:
    print('cannot div by zero')
else:
    print(f'result;{result}')
finally:
    print('code executed')

def checkage(age):
    if age<18:
        raise ValueError('age must be 18')
    else:
        print('you are eligible')
try:
    checkage(16)
except ValueError as e:
    print(f'error')

#custom exception
class NotEligible(Exception):
    pass
def checkage(age):
    if age<18:
        raise NotEligible('age must be 18')
    else:
        print('eligible')
try:
    checkage(11)
except NotEligible as e:
    print('error')

file=open('test.txt','r')
content=file.read()
print(content)
content1=file.readlines()
content2=file.readlines()
file.close()
file=open('test.txt','w')
file=open('test.txt','a')
file.write('hey hii')
file.close()

import os
if os.path.exists('test.txt'):
    with open('test.txt','r') as file:
        content=file.read()
        print(content)
else:
    print('file not exist')

import os
os.remove('test1.txt')
os.rmdir('myfloder')
try:
    with open('test.txt','r') as file:
        data=file.read()
    with open('test1.txt','w')as filewrite:
        filewrite.write(data)
    print('file copied')
except FileNotFoundError:
    print('input or output operation file')
except IOError as e:
    print(f'I/o exception:{e}')
except Exception as e:
    print('an unexcepted error')
    
import mysql.connector
myDB=mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345'
)
print(myDB)

import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='12345',
    database='newdb'
)
cursor=conn.cursor()
cursor.execute("SELECT * FROM newdb.student")
for row in cursor:
    print(row)
conn.close()