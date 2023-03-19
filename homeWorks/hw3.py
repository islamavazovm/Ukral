class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def set_name(self, name):
        self._name = name

    def get_name(self):
         return self._name

    def set_balace(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance


    def moneyX(self):
        amount = int(input("Введите сумму для пополнения: "))
        self._balance += amount

    def _kill(self):
        self._balance = 0

    def __jackpot(self):
        self._balance *= 10

    def _merge_balance(self, other):
        self._balance += other._balance
        other._balance = 0


class Bank_competitor(Bank):
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    @property
    def get_name(self):
        return self._name

    @get_name.setter
    def set_name(self, name):
        self._name = name

    @property
    def get_balance(self):
        return self._balance

    @get_balance.setter
    def set_balace(self, balance):
        self._balance = balance



















