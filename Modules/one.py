#math module
'''from math import pi, sqrt,ceil,floor

print(pi)
print(sqrt(100))
print(ceil(5.1))
print(floor(5.9))'''

'''
#we are prrinting the modules
import math
print(dir(math))

print(math.pi)

print(math.e)'''

# how to find current directory
'''import os
DIR=os.path.dirname(__file__)
print(DIR)'''


#randam module

#several functions to generate randam value


# print 10 randam numbers 1o to 100
'''from random import randint

for x in range(10):
    print(randint(90,100))'''

#random => print randam floating in range 0 to 1

'''from random import random
for x in range(10):
    print(random())'''

# Randrange => stepping    [srartimg , stoping , steping]
#stepping value and stoping value is optional

'''from random import randrange

for x in range(10):
    print(randrange(10,100,1))'''

# choice ()
#it wont generate any randam number
#but, it will return rendom elemnts for list, tuple,set  


from random import choice
enames=['rg','bg','tg','hg']

for x in range(6):
    print(choice(enames))