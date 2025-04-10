emps=[{'eid':101,'ename':'bala','esal':90000},
      {'eid':102,'ename':'sana','esal':80000},
      {'eid':103,'ename':'mala','esal':70000},]

# for emp in emps:
#     print(emp['eid'])
for emp in emps:
        print(emp['ename'])

total=0
for emp in emps:    
    total=total+emp['esal'] 
    print(total)