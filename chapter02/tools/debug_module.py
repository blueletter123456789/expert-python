# python3 -m pdb debug_module.py
# lで現在の行
# nで次の行
# qで終了
# hでヘルプ
def div(a, b):
    return a / b


if __name__ == '__main__':
    c = div(2, 3)
    print(c)

    breakpoint()
    print('debug finish')
