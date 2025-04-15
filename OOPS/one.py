class Account():
    '''class creaytede by balaji'''
    def open_account(self):
       print('Account is opened successfully')
    def deposit_amount(self,amount):
        print('Amount deposited successs')
    def  withdrawl(self):
        print('Amount withdraled')
    @classmethod
    def update_min_bal(cls,amount):
        print('minimam bal is updated')
    @staticmethod
    def cal_intrest():
       print('utility method')

a1=Account()  
a2=Account  
print(a1.__dict__)
print(a2.__dict__)
print(Account.__dict__)


a1.open_account()
a1.deposit_amount(5000)
a1.withdrawl()
a1.update_min_bal(600)
a1.cal_intrest()

# a2.open_account()
# a2.deposit_amount(6000)
# a2.withdrawl()
# a2.update_min_bal(5000)
# a2.cal_intrest()