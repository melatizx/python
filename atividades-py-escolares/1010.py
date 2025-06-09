entrada= input()
c1, n1, v1 = entrada.split()
entrada= input()
c2, n2, v2 = entrada.split()

c1 = int(c1)
n1 = int(n1)
v1 = float(v1)
c2 = int(c2)
n2 = int(n2)
v2 = float(v2)

valorpecas1 = n1*v1
valorpecas2 = n2*v2

pagar = valorpecas1+valorpecas2

print(f'VALOR A PAGAR: R$ {pagar:.2f}')