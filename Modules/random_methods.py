
# # randam nukmbers in range
# import random
# # help (random)

# print(random.randint(1000,9999))


# write python script
# to generate 100-4 digit otp numbers

from random import randint

for x in range(10):
    print(randint(1000,9999))



# lotery lucky dip system

from random import randint

lotery_NO=[]  

for x in range(10):
    lotery_NO.append(randint(100,999))
print(lotery_NO)
 



# choosing choises randam numbers

from random import randint,choice

lotery_NO=[]

for x in range(10):
    lotery_NO.append(randint(10,20))
print(lotery_NO)
print(choice(lotery_NO))


from random import choice
enames=['bala','hati','san','push','dhoni','modi']
print(choice(enames))


# user define modules 