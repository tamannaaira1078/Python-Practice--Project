class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if value<0:
            raise ValueError("Value cannot be negative")
        else:
            self._balance = value

    def deposit(self, amount):
        if amount<=0:
            raise ValueError("Deposit amount must be greater than zero") 
        self.balance+=amount       


    def withdraw(self, amount):
        if amount <=0:
            raise ValueError("Withdrawal amount must be greater than zero!")   
        elif amount>self.balance:
            raise ValueError("Amounts cannot be larger than the balance itself")
        self.balance -= amount


    def show_info(self):
        print(f"Owner: {self.owner}") 
        print(f"Balance: {self.balance}") 

    def __str__(self):
        return f"{self.owner} - Balance:{self.balance}"    


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance) 
        self.interest_rate = interest_rate


    def apply_interest(self):
        interest = self.balance*self.interest_rate  
        self.balance+=interest

    def show_info(self):
        super().show_info()
        print(f"Interest Rate:{self.interest_rate*100:.2f}%")
        

        
         

account_1 = BankAccount("Aira", 7000)
account_1.deposit(1000)
account_1.withdraw(500)
account_1.show_info()
print()

account_2 = SavingsAccount("Aira", 9000, 0.05)
account_2.apply_interest()
account_2.show_info()
print()

