#arithmetic----,  +, -, *, %, **, //
a=5
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%b)
print(a//b)

#relational----- <, >, <=, >=, ==, != (true or false)

A=10
B=30
print(A<B)
print(A>B)
print(A>=B)
print(A<=B)
print(A==B)
print(A!=B)

#assignment----- +, - ,*, /, %, **, //

a=5
print(a)
a=a+2 #a+=2
print(a)
a=a-2
print(a)
a=a*2
print(a)
a=a**2
print(a)
a//=2
print(a)

#logical----- and, or, not (true or false)

print(2<3 and 3<5)
print(2<3 or 3<5)
print( not 3<5)
print(6<5 or 3<7)
print(2<9 and 9<2)
print( not 8<5)

#membership------ in:, not in: (true or false)

l=[10,20,30,40,50]
#print(10 in l)
print(100 in l)

#identify----- is:, not is: (true or false)

a="ratna" #a=2
b="Ratna" #b=2
#b=5
print(a is b)
print(id(a))
print(id(b))

#bitwise------ AND(&), OR(|), XOR(^), NOT(~), <<, >>
'''a  b  a&b a|b  a^b ~a ~b
   0  0   0   0   0   1   1
   0  1   0   1   1   1   0
   1  0   0   1   1   0   1
   1  1   1   1   0   0   0 '''

a=10
b=12
print(bin(a))
print(bin(b))
print(bin(a&b))
print(bin(a|b))
print(bin(a^b))
print(bin(~a))
print(bin(~b))
print(a>>2)
print(a<<3)
print(a+b)