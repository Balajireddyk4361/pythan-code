# enames={'balaji','ravi','rahul','raghavam'}
# print(enames)

# # if you want to add some data in set elements use update method because add method is not available
# enames.update('z')
# print(enames)


s1={'a','b','c','e'}
s2={'a1','a2','a3'}
s3={'Balajireddy'}

s1.update(s2)
print(s1)
s1.update(s3,{'b1','b2','be'})
print(s1)