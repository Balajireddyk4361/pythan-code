# json file to convert python file

# import json
# emps='''{"ename":"balaji","eid":101,"esal":55000,"eloc":"ban","avai":true}'''
# a=json.loads(emps)
# print(emps)
# print(a)


# python file to convert json
# import json
# emp_dict=[{"ename":"balaji",
#           "eid":101,
#           "esal":55000,
#           "eloc":"ban",
#           "avai":True}]

# print(emp_dict)

# emp_json=json.dumps(emp_dict)
# print(emp_json)


# accesing the json dada from jsom file and convert the data from python 
# import json 

# fp=open ("emp.json","r")
# emp_dict=json.load(fp)

# # print(emp_dict)
# #print all enames 
# for emp in emp_dict:
#     print(emp["ename"])


import json
employees=[{'eid':101,
            'esal':50400,
            'ename':'Balaji',
            'avai':True}]
fp=open('write_json','w')

json.dump(employees,fp)

fp.close()
