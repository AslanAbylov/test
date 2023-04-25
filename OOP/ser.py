from datetime import datetime


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self.history = []

    @staticmethod
    def _time_now():
        return datetime.now()

    def deposit(self, amount):
        self.__balance += amount
        self.history.append([amount, self._time_now()])
        self.show_balance()


    def spend(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            print(f'вы отправили {amount} сомов')
            self.history.append([-amount, self._time_now()])
            self.show_balance()
        else:
            print('нету столько денег')


    def show_history(self):
        for amount, date in self.history:
            if amount > 0:
                transaction = 'Получено'
            else:
                transaction = 'Отправлено'
            print(f'{transaction} {amount} {date}')
            self.show_balance()

    def show_balance(self):
        print(f'ваш баланс {self.__balance}')


a = Account('asaln', 0)
a.deposit(500)
a.deposit(100)
a.spend(40)
a.deposit(80)
a.__balance = 10000000
a.show_history()
print(a.__dict__)
a.show_balance()