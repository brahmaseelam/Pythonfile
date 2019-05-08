'''import requests
import json

r=requests.get('https://youtube.com')
print(r.text)

def fun(l):
    smallest=2
    smallestindex=l[2]
    for i,val in enumerate(l):
        if val>smallestindex:
            smallestindex=val
            smallest=i
    l.pop(smallest)
    return l
x=fun([10,20,30,4,320,540,3,2,12,32,54,34])
print(x)


n=123
rev=0
while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
print(rev)


x=[10,3,54,32,34,54,232,653,34,2]
print(x)
for i in range(len(x)):
    for j in range(len(x)-1):
        if x[j]>x[j+1]:
            x[j],x[j+1]=x[j+1],x[j]
            print('x[j]:',x[j],'x[j+1]:',x[j+1],'x:',x)



l=[1,2,5,10,20,50,100,200,500,2000]
n=len(l)
c=513
i=n-1
r=[]
while i>=0:
    while c>=l[i]:
        c-=l[i]
        print('c:',c,'l[i]:',l[i])
        r.append(l[i])
    i-=1
for i in range(len(r)):
               print(r[i],end=' ')'''
               



arr = [900, 940, 950, 1100, 1500, 1800] 
dep = [910, 1120, 1130,1200, 1900, 2000] 
arr.sort()
dep.sort()
platform=1
result=1
i=1
j=0
n=len(arr)
while n>i and n>j:
    if arr[i]<dep[j]:
        platform+=1
        i+=1
        if platform>result:
            result=platform
    else:
        platform-=1
        j+=1
print(result)
 
        
