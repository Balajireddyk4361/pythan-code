#create an tuple
eids=()
uids=101,102,103,1034
unames=("balajireddy","rahul","modi","remo")

# read operator 
print(type(uids))
print(type(eids))
print(type(unames))
print(eids)
print(uids)
print(unames)
#reading via indexing
print(unames[0])
print(unames[2])
print(unames[3])
print(unames[2])
#update tuple object
unames[0]="rahul1"
print(unames)# update object is not support the tuple operator

#delete operator is not accept tuple
unames.pop()
print(unames)