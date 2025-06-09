nome = input('')
fixo = float(input(''))
vendas = float(input(''))

comissao = (vendas*15)/100
final = fixo+comissao
print(f'TOTAL = R$ {final:.2f}')