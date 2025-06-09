alt = float(input("Informe sua altura em m: "))
print("M - Masculino")
print("F - Feminino")
sexo = input("Informe seu sexo: ")
if(sexo=='F' or sexo=='f'):
  peso = (62.1*alt)-44.7
  print("Peso ideal: ", peso)
elif(sexo=='M' or sexo=='m'):
  peso = (72.7*alt)-58
  print("Peso ideal: ", peso)
else:
  print("Sexo invalido")