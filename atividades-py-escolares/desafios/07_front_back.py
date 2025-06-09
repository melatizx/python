import math
def front_back(a, b):

    tam_a = len(a)
    tam_b = len(b)

    metade_a = tam_a // 2 if tam_a % 2 == 0 else math.ceil(tam_a / 2)
    metade_b = tam_b // 2 if tam_b % 2 == 0 else math.ceil(tam_b / 2)
    return (a[:metade_a] + b[:metade_b] + a[metade_a:] + b[metade_b:])


def test(f, in_, expected):
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'
        
    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')

if __name__ == '__main__':
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
