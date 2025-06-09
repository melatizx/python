def match_ends(words):
    qtd = 0
    for w in words:
        if (len(w)>= 2):
            if (w[0] == w[-1]):
                qtd += 1
    return qtd

def test(f, in_, expected):
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    test(match_ends, ['aba', 'xyz', 'aa', 'x', 'bbb'], 3)
    test(match_ends, ['', 'x', 'xy', 'xyx', 'xx'], 2)
    test(match_ends, ['aaa', 'be', 'abc', 'hello'], 1)
    # Meu teste
    test(match_ends, ['aaa', 'bbb', 'xxxxxxxx', 'seduc', 'ss', 'ax'], 4)
