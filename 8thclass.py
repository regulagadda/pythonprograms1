# read a string
str = input("Enter a string:\n")
# create a string with characters at multiples of 2
modified_string = str[::2]
print(modified_string)

s1="durga"
s2="soft"
s3=s1+s2
print(s3)
print(s3*2)

s='''pyThon is vEry eAsy"
"python is vEry eAsy"
"python is vEry eAsy"
"python is vEry easy"
"python is vEry easy"
"python is vEry easy'''
print(s.replace("python", "java"))
#print(s)
'''print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.count(" "))'''

'''s1=s.split(" ")
for i in s1:
    print(i)'''

n=168
count=0
count1=0
for i in range(1+n+1):
    if i%2==0:
        count=count+1
    else:
        count1=count+1
print("Even count:", count)
print("Odd count:", count1)