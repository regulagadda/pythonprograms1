#set concept
#s ={ }
s= set() #empty set write like this
print(s)
print(type(s))

#example of set

#s={10,20,30,40,50}
s={10,45.6,"ratna",54,'A'} #set is a unorder collection of elements
print(s)

#dictionary is a collection of keys and values is paire.

d={1:"rani", 1:"kumari", 2:"esther",3:"esther",4:"vijaya"}

print(d)
print(type(d))
d1= d[3]="souji"  #value can change but key can't change.

print(d)
print(d1)

#range of values by default
#r=range(10)
r=range(2,30,3) #2 is starts, 30 is upto, 3 is difference
print(list(r))
print(type(r))
