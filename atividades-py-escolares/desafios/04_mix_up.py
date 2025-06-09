def mix_up(a, b):
    la1 = a[0]
    la2 = a[1]
    lb1 = b[0]
    lb2 = b[1]
    output = ""
    if(len(a)>2 and len(b)>2):
        a = lb1+lb2+a[2:]
        b = la1+la2+b[2:]
        output = f"{a} {b}"
    return output 

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
    test(mix_up, ('mix', 'pod'), 'pox mid')
    test(mix_up, ('dog', 'dinner'), 'dig donner')
    test(mix_up, ('gnash', 'sport'), 'spash gnort')
    test(mix_up, ('pezzy', 'firm'), 'fizzy perm')
