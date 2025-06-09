qtdN_0_25=0
qtdN_26_50=0
qtdN_51_75=0
qtdN_76_100=0
while (True):
  num=int(input("Digite um número: "))
  if (num>=0 and num<=25):
   qtdN_0_25=+num
  elif(num>=26 and num<=50):
    qtdN_26_50=+num
  elif(num>=51 and num<=75):
    qtdN_51_75=+num
  elif(num>=76 and num<=100):
    qtdN_76_100=+num
    break
while num>=0:
  print(f"Foram digitados {qtdN_0_25} números entre 0 e 25")
  print(f"Foram digitados {qtdN_26_50} números entre 26 e 50")
  print(f"Foram digitados {qtdN_51_75} números entre 51 e 75")
  print(f"Foram digitados {qtdN_76_100} números entre 76 e 100")
  break