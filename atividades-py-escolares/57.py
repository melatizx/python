qtd = 0
print("Responda com 's' ou 'n': ")
print("'s' = sim")
print("'n' = não")

ass1 = input("Telefonou para a vítima? ")
if ass1 == 's':
  qtd = qtd+1
ass2 = input("Esteve no local do crime? ")
if ass2 == 's':
  qtd = qtd+1
ass3 = input("Mora perto da vítima? ")
if ass3 == 's':
  qtd = qtd+1
ass4 = input("Devia para a vítima? ")
if ass4 == 's':
  qtd = qtd+1
ass5 = input("Já trabalhou com a vítima? ")
if ass5 == 's':
  qtd = qtd+1

if qtd == 5:
  print("Assassino")
elif qtd == 3 or qtd == 4:
  print("Cumplice")
elif qtd == 2:
  print("Suspeito")
else:
  print("Inocente")