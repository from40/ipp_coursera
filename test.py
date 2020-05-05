class BankAccount:
    """ Class definition modeling the behavior of a simple bank account """

    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self._account = initial_balance
        self._total_fees = 0
        self._fee = 5

    def deposit(self, amount):
        """Deposits the amount into the account."""
        self._account += amount

    def withdraw(self, amount):
        """
        Withdraws the amount from the account. Each withdrawal resulting
        in a negative balance also deducts a penalty fee of 5 dollars
        from the balance.
        """
        if self._account - amount < 0:
            self._account = self._account - (self._fee + amount)
            self._total_fees += self._fee
        else:
            self._account = self._account - amount

    def get_balance(self):
        """Returns the current balance in the account."""
        return self._account

    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self._total_fees

my_account = BankAccount(10)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(20)
my_account.withdraw(5)
my_account.deposit(10)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(30)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(50)
my_account.deposit(30)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25)
my_account.withdraw(10)
my_account.deposit(20)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
print(my_account.get_balance(), my_account.get_fees())
