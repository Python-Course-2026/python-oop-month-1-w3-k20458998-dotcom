class ValidUser:
    """ЗАДАЧА: Сеттер пароля с проверкой длины >= 8 и наличия цифр"""
    def __init__(self, user, pwd): self.username, self._password = user, pwd
    @property
    def password(self): return "********"
    @password.setter
    def password(self, val):
        if len(val) < 8:
            raise ValueError
        if ('0' not in val or '1' not in val or '2' not in val or '3' not in val or '4' not in val or '5' not in val or '6' not in val or '7' not in val or '8' in val or '9' not in val):
            raise ValueError
        self._password = val
