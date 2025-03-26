'''a={10,20,30,40,40,50,6,10,50,30,40}

print(a)
print(type(a))
emp=set([1,2,3,4,5,6,7,])
print(type(emp))
print((emp)) '''



# how to create empty set object
'''s1=set()
print(s1)'''

#set methods
# 1) add method
eid={101,102,103,104,105,106}
eid.add(107)
print(eid)
eid.update([10,20,30])
print(eid)

enames={'balajireddy','san','bahubali','rowdy'}
enames.update(['san','kancham'])
print(enames)

enames.discard('san')
print(enames)

enames.pop()
print(enames)

# enames.remove('rowdy')
# print(enames)

enames.clear()
print(enames)

