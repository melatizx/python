controle = [6,2,5,5,4,5,6,3,7,6]
leds = 0
i=0
leds_controle=[]
while True:
  N = int(input("Nº de testes: "))
  if N >= 1 and N <= 10000:
    break

while i < N:
    vari = input("Numero: ")
    for valor in vari:
      leds+=controle[int(valor)]
    leds_controle.append(leds)
    leds=0
    i+=1

for led in leds_controle:
   print(f"{led} leds")