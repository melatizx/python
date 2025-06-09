numeros = []
somadores = []

while True:
  numero = int(input())

  if numero == 0:
    break
  numeros.append(numero)
  contador = 0
  soma = []
  while contador < 5:
    if numero % 2 == 0:
      soma.append(numero)
      numero += 2
      contador += 1
    else:
      numero += 1

  somadores.append(sum(soma))


for valor in somadores:
  print(valor)