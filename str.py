# swap two numbers
x=10
y=20
temp=x
x=y
y=temp
print('x--',x)
print('y--',y)

#ternary operator

#syntax: a if a<b else b

a=10
b=20
x=a if a<b else b
print(x)


a=10;b=20;c=30
x=a if a<b and b<c else b if b<c else c
print(x)


# read multiple values in a single line

'''x,y=[int(x) for x in input('enter values :').split(',')]
print('x*y:',x*y)

# eval function

x=eval(input('enter a list:'))
print(x)'''

#formated methods

x=10
y=20
z=30
print('the value of x:%i and y:%i and z:%d'%(x,y,z))

#another method
a=10
b='siddarth'
print('his name is : {0},and age is :{1}'.format(b,a))


#pyramid star program

n=5
for i in range(1,n+1):
    print(' '*(n-i),end='')
    print('* '*i)

# string +ve and -ve index
s='this is string in python'
i=0
for x in s:
    print('+ve index:{} -ve index:{} and word:{}'.format(i,i-len(s),x))
    i+=1

s='this is python'
n=len(s)
i=0
while i<n:
    print(s[i],end='')
    i+=1
i=-1
while i>=-n:
    print(s[i],end=' ')
    i-=1
print()

# identity operator
x='this is python string'
y='django'
if y not in x:
    print('y is not found in x')

# all positions of sub string

s='this is a python strig'
s1='s'
pos=-1
while True:
    pos=s.find(s1,pos+1,len(s))
    if pos==-1:
        break
    print('position:',pos)
    f=True
if f==False:
    print('not found ')

# alternative method using for loop
s='abcredsabdescfdabcabdebacdba'
s1='a'
p=-1
for i in s:
    p=s.find(s1,p+1,len(s))
    if p==-1:
        break
    print('found at position:',p)



# important programs
# 1.reverse program

s='this is a string'
i=-1
for j in s:
    print(s[i],end='')
    i-=1
# alternate
s='this is a python\n'
i=-1
while i>=-len(s):
    print(s[i],end='')
    i-=1

# reverse order of words

s='this is a python string'
l=s.split()
l1=[]
i=len(l)-1
while i>=0:
    l1.append(l[i])
    i-=1
output=' '.join(l1)
print(output)

# alternative method
s='this is a string'
l=s.split()
l1=[]
i=-1
for j in l:
    l1.append(l[i])
    i-=1
output=' '.join(l1)
print(output)

# reverse content
s='python strings are very useful'
l=s.split()
l1=[]
i=0
while i<len(l):
    l1.append(l[i][::-1])
    i+=1
r=' '.join(l1)
print(r)

# alternative method
s='python strings are very useful'
l=s.split()
l1=[]
i=0
for j in l: 
    l1.append(l[i][::-1])
    i+=1
r=' '.join(l1)
print(r)


# duplicate elements remove in list

l=[1,2,3,4,5,1,2,3,4,5]
l2=[]
for i in l:
    if i not in l2:
        l2.append(i)
print(l2)
    



# odd position and even position

s='this is a python string'
i=0
while i<len(s):
    print('\neven position:{} and word : {}'.format(i,s[i]),end='')
    i+=2
i=1
while i<len(s):
    print('\nodd position:{} and word:{}\n'.format(i,s[i]),end='')
    i+=2


# merge two strings
s='bsreddy'
s1='bhargavi'
output=''
i,j=0,0
while i<len(s) or j<len(s1):
    if i<len(s):
        output+=s[i]
        i+=1
    if j<len(s1):
        output+=s1[j]
        j+=1
print(output)


s='sreeja'
s1='bsredd'
r=''
i,j=0,0
while i<len(s) and j<len(s1):
    if i<len(s):
        r+=s[i]
        i+=1
    if j<len(s1):
        r+=s1[j]
        j+=1
print(r)



# sort the characters of the string

s='b4a1d3'
s1=s2=''
for x in s:
    if x.isalpha():
        s1+=x
    else:
        s2+=x
for x in sorted(s1):
    output+=x
for x in sorted(s2):
    output+=x
print(output)

s='bsredyy12l01a0467'
s1=s2=''
for x in s:
    if x.isalpha():
        s1+=x
    else:
        s2+=x
for x in s1:
    output+=x
for x in s2:
    output+=x
print(output)

# i/p:a4b3c3  o/p:aaaabbbccc

s='a4b3c3'
output=''
for i in s:
    if i.isalpha():
        output+=i
        previous=i
    else:
        output+=previous*(int(i)-1)
print(output)


a='b4c3e2'
output=''
for x in a:
    if x.isalpha():
        output+=x
        previous=x
    else:
        output+=previous*(int(x)-1)
print(output)
        
# remove duplicates
s='abcabdcbsedbrfdbasbdbbfdbsebbd'
l=[]
for i in s:
    if i not in l:
        l.append(i)
print(''.join(l))

# i/p: a4b3c5 o/p:aebdch
s='a4b3c5'
output=''
for i in s:
    if i.isalpha():
        output+=i
        previous=i
    else:
        output+=chr(ord(previous)+int(i))
print(output)


# i/p: abcdabcsvabcds  o/p:
 
s='abcdabcsvabcds'
d={}
for x in s:
    if x in d.keys():
        d[x]+=1
    else:
        d[x]=1
for k,v in d.items():
    print('{}:{}'.format(k,v))


s='d54fgrd453'
r1=r2=''
for i in s:
    if i.isalpha():
        r1+=i
    else:
        r2+=i
for i in r1:
    a+=i
for i in r2:
    a+=i
print(a)



# list

'''vowels=['a','e','i','o','u']
word=input('enter the word to search:')
found=[]
for l in vowels:
    if l in word:
        if l not in found:
            found.append(l)
print(found)'''


# what does the folling code output

def list(value,l=[]):
    l.append(value)
    return l
l=list(10)
l1=list(123,[])
l2=list('a')
print(l,l1,l2)

# sort method
s = [3, 6, 4, 5, 2, 1, 7, 8, 11, 12]
for k in range(len(s)):
    for m in range(len(s)-1):
        if s[m]>s[m+1]:
            s[m],s[m+1] = s[m+1],s[m]
print (s)

 # nested list as single list
l = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
flat_list=[]
for sublist in l:
    for item in sublist:
        flat_list.append(item)
print(flat_list)
        

#2nd nested list

'''l=[1,2,[3,4,[5,6]],7,8,[9,[10]]]
output=[]
def removenestings(l):
    for i in l:
        if type(i)==list:
            removenestings(i)
        else:
            output.append(i)
print('the original list:',l)
removenestings(l)
print('after removing nesting list :',output)'''

 
