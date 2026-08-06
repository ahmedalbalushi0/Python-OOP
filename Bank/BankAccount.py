class Account:
    
    def __init__(self, acc, bal):
        self.account_no = acc
        self.balance = bal

    #debit method
    def debit(self,amount):
        self.balance -=amount
        print(amount,"OMR was debited from your account",self.account_no)

    #credit method
    def credit(self,amount):
        self.balance += amount
        print(amount,"OMR was credited from your accont",self.account_no)

acc1 = Account(1,1000)
print("Account No. :",acc1.account_no,"\nAcount Balance:",acc1.balance)
acc1.debit(500)
acc1.credit(10)