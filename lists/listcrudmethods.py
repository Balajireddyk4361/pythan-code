enames=['balaji','ramu','raghu','balaji','pushpa','pushpa']
new_enames=['san chi','aquaman','robo','san chi']
print(len(enames))
print(enames.count(5))
print(enames.index('ramu'))
enames.append('orange')
print(enames)
enames.append('remo')
print(enames)
enames.insert(0,"revoi")
print(enames)

enames.extend(new_enames)
print(enames)

# enames.extend('balaji')
# print(enames)

enames.pop()
print(enames)

enames.remove('aquaman')
print(enames)

# enames.clear()
# print(enames)

enames.reverse()
print(enames)

# sort method usage
enames.sort()
print(enames)

eid=[102,101,103,105,101,99]
eid.sort()
print(eid)

enames.sort(reverse=True)
print(enames)

#desending operations usin sort method
eid.sort(reverse=True)
print(eid)

#addition oprration 
l1=[10,20,30,40]
l2=[10,9,8,7,6,]
l3=l1+l2
print(l3)


# repitition using * multiplicatinn method
l1=[10,20,30,40]
l2=[10,9,8,7,6,]
l3=l1*6
print(l3)

#membership operator to element is present are not
 
print('balaji' in enames)
print(110 in l1)