from numpy import *

#array
A=array([10,20,30,40,50,60])
print(A)
print(type(A))
print(A.dtype)
print(A.ndim)
print(A.shape)
print(A.size)
print(A.sum())

#linspace (start, stop, no of part)
A=linspace(2,20,7)
print(A)
print(type(A))
print(A.dtype)
print(A.ndim)
print(A.shape)
print(A.size)
print(A.sum())

#logspace (start, stop, noof parts)
A=logspace(2,20,9)
print(A)
print(type(A))
print(A.dtype)
print(A.ndim)
print(A.shape)
print(A.size)
print(A.sum())

#arange (start, stop, no of parts)

A=arange(2,20,7)
print(A)
print(type(A))
print(A.dtype)
print(A.ndim)
print(A.shape)
print(A.size)
print(A.sum())

#zeros()

A=zeros(8)
A=zeros(8,int)
print(A)
print(type(A))
print(A.dtype)
print(A.ndim)
print(A.shape)
print(A.size)
print(A.sum())

#ones()

A=ones(5)
A=ones(5,int)
print(A)
print(type(A))
print(A.dtype)
print(A.ndim)
print(A.shape)
print(A.size)
print(A.sum())
#multi die array or two die array

'''A=array([[10,20,30,40],
         [90,20,60,40],
         [23,45,67,89]])
B=array([[10,20,30,40],
         [90,20,60,40],
         [23,45,67,89]])
print(A)
print(B)
print(A+B)
print(A-B)
print(A*B)

print(A)
print(A.dtype)
print(A.ndim)
print(A.shape)
print(A.size)
print("Max values is:", A.max( ))
print("Min value is:", A.min( ))
print("row wise max value:", A.max(axis=0))
print("row wise min value:", A.min(axis=1))
print("col wise max value:", A.max(axis=0))
print("col wise max value:", A.max(axis=1))
print(A.sum())
print(A)
print(A.ndim)
B=A.flatten() #convert two die to single dimention
print(B)
print(B.ndim)'''

