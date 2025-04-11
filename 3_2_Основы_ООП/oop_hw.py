class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Сумма должна быть положительной")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if amount > self.__balance:
            raise ValueError("Недостаточно средств для списания")
        self.__balance -= amount

    def get_balance(self):
        print(f"Текущий баланс {self.__balance}")

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner,balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self._BankAccount__balance += self._BankAccount__balance * self.interest_rate

class CheckingAccount(BankAccount):
    def __init__(self,owner, balance=0):
        super().__init__(owner, balance)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self._BankAccount__balance -= amount

#
# acc = SavingsAccount("Кайо", 0)       # создаём счёт
# acc.deposit(500)                      # пополняем на 500
# acc.withdraw(100)                    # снимаем 100
# acc.apply_interest()                 # применяем 5% годовых
# acc.get_balance()                    # печатаем итоговый баланс