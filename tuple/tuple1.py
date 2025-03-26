#print vowles in given element
'''str=input('Enter a value')

vowles=['a','e','i','o','u']
count=0
for char in str:
    if char in vowles:
        count=count+1
print(count)'''

t1=()
t2=(10,20,20,30,40,50)
t3=('bala',100,'1ra')
t4=12,13,14, 9,6,15,10    
print(type(t1))
print(type(t2))
print(type(t3))
print(type(t4))
print(t1)
print(t2)
print(t3[0])
print(t4.index(14))
print(t2[:])
print(t3[:1])
print(t2.count(50))
print(tuple(sorted(t4)))