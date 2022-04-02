#conditional statements (if, else if, nested if, elif,if else)

'''i=10
if i == 10:
    print("true")
else:
    print("false")

#at run time
i=int(input("enter num1:"))
j=int(input("enter num2:"))
if i>j:
    print(i, "is big")
else:
    print(j, "is big")

#ternary operator
i=int(input("enter num1:"))
j=int(input("enter num2:"))
k=int(input("enter num3:"))

max=i if i>j and i>k else j if j>k else k

print("max value is:", max)'''
#else if, nested if, elif

'''i=int(input("enter numnber:"))
if i>20:
    print(i, "is greater than 20")
else:
    if i>15:
        print(i, "is greater than 15")
    else:
        print(i, "is not greater than 15 and 20")'''

#nested if

i=int(input("enter number:"))
if i==1:
    print("one")
else:
    if i ==2:
        print("two")
    else:
     if i==3:
      print("three")
     else:
      if i==4:
       print("four")
      else:
          print("invalid number")

#elif

i=int(input("enter number:"))
if i==1:
    print("one")

elif i==2:
        print("two")
elif i==3:
      print("three")
elif i==4:
       print("four")
else:
    print("invalid number")
