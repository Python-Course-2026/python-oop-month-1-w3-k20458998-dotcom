class Wallet:
    """ЗАДАЧА: Сложение кошельков через __add__ (новый Wallet) и длина через __len__ (целый баланс)"""
    def __init__(self, name, balance): self.name, self.balance = name, balance
    def __add__(self, other):
        n_name = "Joint Account"
        n_balance = self.balance + other.balance
        return Wallet(n_name, n_balance)
    def __len__(self):
        return int(self.balance)