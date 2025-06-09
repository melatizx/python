idade = int(input("Qual é a sua idade? \n"))
if (idade < 0):
  print("Idade inválida")
elif (idade < 18):
  print("Você é menor de idade")
else:
  print("Você é maior de idade")