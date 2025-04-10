emp={
    'eid':101,
   'ename':'balaji',
   'loc':True
}
emp['email']='kancham@123'
print(emp)

#del emp['eid']
#print(emp)

emp['ename']='reddy'
print(type(emp['eid'])) 

print(emp['ename'])

print(emp)

print(type('loc'))

emp.pop('email')
print(emp)

# emp.clear()
# print(emp)

print(emp.get('eid'))
print(emp.get('ename'))
print(emp.keys())
print(emp.values())


for key in emp.keys():
    print(key)

for value in emp.values():
    print(value)

for k,v in emp.items():
    print(k,':',v)  

    #i=0
    # while emp[i]-1:
    #     print(emp[i])
    # i+1

    