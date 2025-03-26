#read json file and print all employees names 

import json

fp1=open('emp.json','r')
emp_data=json.load(fp1)
print(type(emp_data))

for emp in emp_data:
    print(emp['ename'])