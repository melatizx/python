pal = input("Digite uma palavra: ")

palr = pal.lower().strip().replace(' ', '')
if palr == palr[::-1]:
  print("É um palindromo")
else:
  print("Não é um palindromo")