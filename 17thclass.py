from calendar import *
'''m=3
y=2022
print(month(y,m))
#print(month(1947,8))
print(calendar(2022,2,1,6)) #y w l c
#y--- year
#w ---- width of the character
#l ---- line per week
#c ---- column seperation

print(leapdays(1920,2022))
print(isleap(2022)) #it returns true or false'''

#random modules:
#1. random():
'''from random import *
for i in range(5):
    #print(random())
#2. randint():

    #print(randint(2,20))

#3. uniform():

    #print(uniform(2,20))

#4. randomrange (start, stop, step):

    #print(randrange(2,20,2))
from random import *
l=["ratna", "rani", "elsi", "vijaya"]
print(choice(l))'''

#array

#import  array

#A= array.array([10,20,30,40]) #error occured because typecode character mentioned
#A=array.array('i',[10,20,30,40,50])
from array import *
A=array('i',[10,20,30,40,50])
print(A)
print(type(A))
#index
print(A[0])
print(A[1])
print(A[2])
print(A[3])
print(A[4])
#add one character by using append method
'''A.append(33)
print(A)
#add multiple characters at a time by using extend method
A.extend([25,45,74,85])
print(A)
#remove multiple characters at a time by using remove method
A.remove(10)
print(A)
A.insert(2,50)
print(A)
#for i in A:
for i in range(4):
    print(A[i])
    #print(i)

#copy one array to another array
B=A
print(B)
B.insert(1,44)
print(B)
print(A)
print(id(A))
print(id(B))'''

#B=array('i',[i for i in A])
#B=array(A.typecode,[i*2 for i in A])
B=array('i',[i*2 for i in A])
print(B)
print(A)
print(id(A))
print(id(B))