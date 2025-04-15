# without constructor 


class Test:
    def __init__(self):
        print('constructor is created')
    def gett_details(self):
        print('instance method')
    @classmethod
    def update_bal(cls):
       print('class method')
    @staticmethod
    def sum(a,b):
       print('static method')       

Test()      