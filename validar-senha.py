import re

valido = []
def caracteres_especiais(string):
    return re.findall(r'[^a-zA-Z0-9s]', string)

senha = input("Senha: ")

maiusculas = [letramaior for letramaior in senha if letramaior.isupper()]
minusculas = [letramenor for letramenor in senha if letramenor.islower()]
numeros = re.findall(r'[0-9]', senha)
especiais = caracteres_especiais(senha)

if len(senha)>=8:
    print("MINIMO DE 8 CARACTERES ✅")
    valido.append("valido")
else:
    print("MINIMO DE 8 CARACTERES ❌")

if len(maiusculas)>=1:
    print("MAIUSCULA ✅")
    valido.append("valido")
else:
    print("MAIUSCULA ❌")

if len(minusculas)>=1:
    print("MINUSCULA ✅")
    valido.append("valido")
else:
    print("MINUSCULA ❌")

if len(numeros)>=1:
    print("NUMERO ✅")
    valido.append("valido")
else:
    print("NUMERO ❌")

if len(especiais)>=1:
    print("CARACTER ESPECIAL ✅")
    valido.append("valido")
else:
    print("CARACTER ESPECIAL ❌")

if len(valido)==5:
    print(f"nA senha {senha} é valida!")
else:
    print(f"nA senha {senha} é invalida!")
