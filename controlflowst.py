# wap to verify given number is even or not

num=int(input("Enter Number"))
print(type(num))

if num %2 ==0:
    print("yes given no is Even Number")
else:
    print("No.given num is odd num")


    #wap verify given number is three digit number are not
    num=int(input("Enter Number"))
    if num>=100 and num<=999:
      print("yes  it is three digit number")
    else:
       print("no it is not a thre digit number")