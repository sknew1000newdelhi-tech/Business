class Acount:
     def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

     def debit (self, amount) :
         self.balance -= amount
         print("Rs.", amount, "was debited")
         print("Total balance=", self, self.get_balance())
     def credit(self, amount):
         self.balance += amount
         print("Rs.", amount, "was credit")
         print("Total balance=", self, self.get_balance())
     def get_balance(self):
         return self.balance

account = Acount(10000, 112345)
account.debit(2000)
account.credit(50000)
account.debit(5000)
account.debit(5000)
account.credit(20000)
account.debit(7000)