# 直接参照や変更されたくない変数は先頭にアンダースコア
_observers = []


def add_observer(observer):
    _observers.append(observer)


def get_observer():
    """ 返り値の受け取り側で、_observers変数が変更されないようtuple化
    """
    return tuple(_observers)
