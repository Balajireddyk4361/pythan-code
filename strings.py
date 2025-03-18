'''text = "hello world"
print(text.title())
text = "development"
i=text.split("e")
print(i)'''

#title
a="Python"
x=a.isupper()
print(x)
#isupper 

#uppper
a="PythON"
x=a.upper()
print(x)
#swap
a="PYthon"
x=a.swapcase()
print(x)
#join
a="PYthon"
x=a.join("abc")
print(x)
#replacement
a="development"
x=a.replace("e","s",2)
print(x)
#endswith
a="development"
x=a.endswith("t")
print(x)
#count
a="development"
x=a.count("e")
print(x)
#map
a=[1,2,3,4,5]
def double (val):
    
    return val*2
res=list(map(double,a))
print(res)