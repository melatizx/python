ext = [
    "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis",
    "dezessete", "dezoito", "dezenove", "vinte"
]
dez = [
    'zero', 'dez', 'vinte', 'trint', 'quarenta', 'cinquenta', 'sessenta',
    'setenta', 'oitenta', 'noventa'
]

num = int(input("Digite um numero entre 0 a 99: "))
if num >= 0 and num <= 100:
  if num < 21:
    print(f"{ext[num]}")
  else:
    x = divmod(num, 10)
    if x[1] == 0:
      print(dez[x[0]])
    else:
      print(f"{dez[x[0]]} e {ext[x[0]]}")
else: 
  print("Tente novamente!")