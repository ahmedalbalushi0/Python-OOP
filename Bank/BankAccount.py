class Account:
    
    def __init__(self, acc_no,acc_pass, bal):
        self.account_no = acc_no
        self.__acc_pass = acc_pass #private attribute
        self.balance = bal

    #reset password method
    def reset_pass(self, new_pass):
        self.__acc_pass = new_pass
        print("Password updated successfully")

    #debit method
    def debit(self,amount):
        self.balance -=amount
        print(amount,"OMR was debited from your account",self.account_no)
        print("Current balance:",self.get_balance())

    #credit method
    def credit(self,amount):
        self.balance += amount
        print(amount,"OMR was credited to your account",self.account_no)
        print("Current balance:",self.get_balance())

    #final balance
    def get_balance(self):
        return self.balance

acc1 = Account(13864761,"F5pi1",0)
print("Account No. :",acc1.account_no,"\nAcount Balance:",acc1.balance)
acc1.credit(750)
acc1.debit(110)
acc1.reset_pass("r501Qf")