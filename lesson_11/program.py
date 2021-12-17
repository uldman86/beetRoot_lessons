class MoneyHolder():
    def amount(self):
        return 0


class Cash(MoneyHolder):
    def __init__(self, s):
        self.s = s

    def amount(self):
        return self.s


class Gold(MoneyHolder):
    COAST = 50

    def __init__(self, weight):
        self.weight = weight

    def amount(self):
        return self.weight * self.COAST


class Wallet(MoneyHolder):
    def __init__(self):
        self.my_wallet = []

    def add(self, *values: MoneyHolder):
        for value in values:
            if isinstance(value, MoneyHolder):
                self.my_wallet.append(value)
        return self

    def amount(self):
        res = 0
        for i in self.my_wallet:
            i: MoneyHolder
            res += i.amount()
        return res


if __name__ == '__main__':
    cash_50 = Cash(50)
    cash_100 = Cash(100)
    gold_10 = Gold(10)
    wallet = Wallet()
    wallet.add(cash_50,cash_100,gold_10)
    print(wallet.amount())

    wallet_1 = Wallet()
    wallet_1.add(Cash(200), Cash(100))
    print(wallet_1.amount())
    wallet_1.add(wallet)
    print(wallet_1.amount())
    wallet_2 = Wallet().add(wallet_1)
    print(wallet_2.amount())
