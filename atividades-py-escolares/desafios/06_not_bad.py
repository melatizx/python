def not_bad(s):
    if "not" in s:
        n = s.index("not")
        if "bad" in s:
            b = s.index("bad")
            if (n>b):
                output = s
                return output
            else:
                output = s.replace(s[n:b+3], "good") 
                return output
        else: 
            output = s
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
    test(not_bad, 'This movie is not so bad', 'This movie is good')
    test(not_bad, 'This dinner is not that bad!', 'This dinner is good!')
    test(not_bad, 'This tea is not hot', 'This tea is not hot')
    test(not_bad, "It's bad yet not", "It's bad yet not")
