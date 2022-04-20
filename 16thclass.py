#help('modules')
#import datetime
#help('datetime')

'''from math import*
print(sqrt(4))
print(pow(3,2))
print(sin(4))
print(cos(6))
print(radians(4))
print(factorial(6))'''

'''import datetime

x=datetime.datetime.now()
print(x)'''

'''from datetime import *
x=datetime.now()
print(x)
print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)'''

from datetime import*
#x=datetime(2022,12,5,23,32,5)
x=datetime.now()

print(x)
print(x.strftime('%A')) #weekday full version
print(x.strftime('%a')) #weekday short version
print(x.strftime('%B')) #month full version
print(x.strftime('%b')) #month short version
print(x.strftime('%Y')) #year full version
print(x.strftime('%y')) #year short version

