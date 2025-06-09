ofertas = int(input())
G = 0
V = 0

for n in range(ofertas):
    entrada = input().upper()
    tipo, valor = entrada.split()
    if (tipo == "G"):
        G = G+int(valor)
    else:
        V = V+int(valor)

if (V<G):
    print("NAO VAI TER CORTE, VAI TER LUTA!")
else:
    print("A greve vai parar.")