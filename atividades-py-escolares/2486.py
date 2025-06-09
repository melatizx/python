mgalimentos = {
    "sucodelaranja" : 120,
    "morangofresco" : 85,
    "mamao" : 85,
    "goiabavermelha" : 70,
    "manga" : 56,
    "laranja" : 50,
    "brocolis" : 34,
}

calorias = 0
alimentos = []
indice = 0
numalimentos = int(input("numalimentos "))
if numalimentos > 0:
    for i in range(0, numalimentos):
        entrada = input().split()
        qntd = entrada[0]
        opc= "".join(entrada[1:])
        calorias += mgalimentos[opc]* int(qntd)
    
print(calorias)