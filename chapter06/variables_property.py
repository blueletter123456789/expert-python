# 内部のメソッドからのみ参照される変数は、プライベートな変数として定義する
class Citizen:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"


citizen = Citizen('Taro', 'Yamada')
print(citizen.full_name)
