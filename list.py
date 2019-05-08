# delete elements in list

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)

#shuffle 
from random import shuffle
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle(color)
print(color)

# second smallest and highest number

l=[10,2,30,12,38,46,93]
l1=len(l)
l.sort()
print('highest number is:',l[l1-1])
print('second highest number is:',l[l1-2])
print('lowest number is :',l[0])
print('second lowest number is :',l[1])

# common elements in list

color1 = ["Red", "Green", "Orange", "White"]
color2 = ["Black", "Green", "White", "Pink"]
color=[]
for i in color1:
    if i in color2:
        color.append(i)
print(color)

# remove from a key value pair

original_list = [{'key1':'value1', 'key2':'value2'}, {'key1':'value3', 'key2':'value4'}]
print("Original List: ")
print(original_list)
new_list = [{k: v for k, v in d.items() if k != 'key1'} for d in original_list]
print("New List: ")
print(new_list)



# create empty dict in list

n=5
l=[{} for _ in range(n)]
print(l)

# Split a list based on first character of word

from itertools import groupby
from operator import itemgetter

word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
    print(letter)
    for word in words:
        print(word)


# oops

class student:
    def __init__(self,name,age,section):
        self.name=name
        self.age=age
        self.section='section'
    #def talk(self):
     #   print(self.name)
      #  print(self.age)
       # print(self.section)
s=student('Bsreddy',24,'B')
print(s.__dict__)



# we can access instance variables with in the class by using self variable and outside of the by using object reference

class student:
    def __init__(self,name,age,section):
        self.name=name
        self.age=age
        self.section=section
    def talk(self):
        print(self.name)
        print(self.age)
        print(self.section)
s=student('bsreddy',24,'B')
s.talk()
s1=student('siddarth',9,'a')
s1.talk()
student.name='bhargavi'
s1.talk()

#
class Test:
    x=10
    def __init__(self):
        self.y=20
t1=Test()
t2=Test()
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)
Test.x=888
t1.y=999
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)

class stu:
    x=100
    def __init__(self):
        self.y=200

s1=stu()
s2=stu()

print('s1:',s1.x,s1.y)
print('s2:',s2.x,s2.y)
stu.x=500
s1.y=220
print('s1:',s1.x,s1.y)
print('s2:',s2.x,s2.y)
# static variable

class test:
    a=10
    def __init__(self):
        test.b=20
    def m1(self):
        test.c=30
    @classmethod
    def m2(cls):
        cls.d1=40
        test.d2=400
    @staticmethod
    def m3():
        
        test.e=50
print(test.__dict__)
t=test()
print(test.__dict__)
t.m1()
print(test.__dict__)
t.m2()
print(test.__dict__)
t.m3()
print(test.__dict__)
print(t.__dict__)
test.f=60
print(test.__dict__)


# how to access static variable

class test:
    a=10
    def __init__(self):
        print(self.a)
        print(test.a)
    def m1(self):
        print(self.a)
        print(test.a)
    @classmethod
    def m2(cls):
        print(cls.a)
        print(test.a)
    @staticmethod
    def m3():
        print(test.a)

t=test()
print(test.a)
t.m1()
t.m2()
t.m3()
t.b=50
print(t.b)

# modify the static variable

class test:
    a=10
    def __init__(self):
        test.a=200
    def m1(self):
        self.a=330
        test.a=300
    @classmethod
    def m2(cls):
        cls.a=400
    @staticmethod
    def m3():
        test.a=500
t=test()
print(t.a)
t.m1()
print(t.a)
print(t.__dict__)


class test:
    count=0
    def __init__(self):
        test.name='bsreddy'
        test.count+=1
    @classmethod
    def m1(cls):
        print(cls.name)
        print('no.of objects created:\n',cls.count)
t=test()
t.m1()
t1=test()
t1.m1()
t2=test()
t2.m1()
t3=test()


class student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks
s=student()
s.setName('bsreddy')
print(s.getName())
s.setMarks(35)
print(s.getMarks())


# passing one class to another class

class employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def display(self):
        print(self.eno)
        print(self.ename)
        print(self.esal)
class test:
    def modify(emp):
        emp.esal+=10000
        emp.display()
e=employee(100,'bsredd',12000)
test.modify(e)

# ducktype philosipy
class dog:
    def talk(self):
        print('bow....bow')
class goat:
    def talk(self):
        print('myah....myah')
def f1(obj):
    obj.talk()
l=[dog(),goat()]
for obj in l:
    f1(obj)


class dog:
    def talk(self):
        print('bow....bow')
class goat:
    def talk(self):
        print('myah....myah')
class cat:
    def bark(self):
        print('mya...mya')
def f1(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'bark'):
        obj.bark()
l=[dog(),goat(),cat()]
for obj in l:
    f1(obj)


# magic methods

'''class book:
    def __init__(self,pages):
        self.pages=pages
b=book(100)
b1=book(200)
print('the total number of pages:',b+b1)'''

# this method is operator overloading
class book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages+other.pages
    
b=book(100)
b1=book(200)
print('the total number of pages:',b+b1)



class student:
    def __init__(self,name,age,books):
        self.name=name
        self.age=age
        self.books=books
    def __add__(self,other):
        return self.name
        return self.age
    
        return self.books+other.books
s=student('bsreddy',24,12)
s1=student('siddarth',23,10)
print('details here:',s+s1 )


# method overloading with default argument

class test:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print('the sum of 3 numbers:',a+b+c)
        elif a!=None and b!=None:
            print('the sum of 2 numbers:',a+b)
        else:
            print('please provide 2 or 3 arguments')
t=test()
t.sum(10,20,30)
t.sum(10,20)
t.sum(10)

# * arguments

class test:
    def sum(self,*args):
        c=0
        for i in args:
            c+=i
        print('the sum:',c)
t=test()
t.sum(10,200,30)

# method overridding
class employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class person(employee):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
    def display(self):
        print(self.name)
        print(self.age)
        print(self.eno)
        print(self.esal)
p=person('bsreddy',24,1001,12000)
p.display()


class demo:
    def m1(self):
        print('property')
    def m2(self):
        print('aliabhatt')
class pro(demo):
    def m2(self):
        print('sonamkapoor')
        super().m2()
p=pro()
p.m1()
p.m2()
        

