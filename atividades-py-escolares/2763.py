coisax = []
delimitador = ""
n=0
CPF = input()

for digito in CPF:
    if digito in ".-":
        pass
    else:
        coisax.append(digito)
    if len(coisax)==3:
        printando = delimitador.join(coisax)
        print(printando)
        coisax=[]
        n+=1
    elif len(coisax)==2 and n==3:
        printando = delimitador.join(coisax)
        print(printando)