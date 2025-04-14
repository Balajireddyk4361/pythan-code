'''from insuffientBalError  import InsuffientBalErr

amount=int(input("Enter Amount:"))
acc_Bal = 15000

if acc_Bal < amount:
    #print("Low Balance")
    raise InsuffientBalErr("Low Balance")
else:
    print("Withdrawl and Enjoy")

print("Good Morning")
'''

#with error handling
'''from InsuffientBalError import InsuffientBalErr as LowBalError

acc_Bal=15000
try:
    amount = int(input("Enter Amount"))
    if acc_Bal<amount:
        raise LowBalError("Buddy - Low Bal! Please Check!")
    else:
        print("Please Withdrawl and Enjoy!")

except LowBalError as err:
    print(err)
except:
    print("Check the code! Default Errors")


print("Good Moring")'''