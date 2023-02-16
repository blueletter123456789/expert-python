# ブール演算子を使用してオプションを組み合わせる
OPTIONS = {}


def register_option(name):
    return OPTIONS.setdefault(name, 1 << len(OPTIONS))


def has_options(options, name):
    return bool(options & name)


# オプションを定義する
BLUE = register_option('BLUE')
RED = register_option('RED')
WHITE = register_option('WHITE')

SET = BLUE | RED
print(has_options(SET, BLUE))
print(has_options(SET, WHITE))
