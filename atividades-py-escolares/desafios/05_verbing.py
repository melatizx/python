def verbing(s):
    if(len(s)<3):
        output = s
        return output
    else:
        if(s[-3]+s[-2]+s[-1] == "ing"):
            output = s+"ly"
            return output
        else:
            output = s+"ing"
            return output

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
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(verbing, 'hail', 'hailing')
    test(verbing, 'swiming', 'swimingly')
    test(verbing, 'do', 'do')
