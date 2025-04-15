class Accout():
    def __init__(self,id,name,amount):
        self.acc_id=id
        self.acc_name=name
        self.acc_bal=amount
    def deposit_amount(self,amount):
        self.acc_bal=self.acc_bal+amount
    def m(self):
        self.acc_bal=self.acc_bal-amount    
            




a1=Accout(101,'Balajireddy',5000)
print(a1.__dict__)
a1.deposit_amount(1000)
print(a1.__dict__)