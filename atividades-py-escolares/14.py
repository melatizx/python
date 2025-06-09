print("Informe seu sexo: ")
print("M - masculino")
print("F - feminino")
sexo = input("")
if(sexo == "M" or sexo == "m"):
  print("Masculino")
elif(sexo == "F" or sexo == "f"):
  print("Feminino")
else: 
  print("Sexo inválido")