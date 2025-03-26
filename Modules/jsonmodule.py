# json means javascript object notation
# json trans for the data from one file to another
# 
# fp=open('abc.text')
# data=fp.read()
# print(data)
# 

#read abc.text file and write data into new file
# '''fp1=open('abc.text','r')
# data=fp1.read()
# fp2=open('xyz.text','w')
# fp2.write(data)
# print("new files created")
# fp1.close()
# fp2.close() '''

# convet json data to python dict object
import json
emp_data='''
         {
         "eid":101,
         "ename":"Rahul",
         "loc":true
         }
         '''
emp_dict=json.loads(emp_data)
print(type(emp_dict))
print(emp_dict)