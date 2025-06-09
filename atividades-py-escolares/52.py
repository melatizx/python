from function import EhPrimo

if __name__ == '__main__':
  num = int(input("Digite um numero: "))
  EhPrimo(num)
  p = num
  primos = []
  for p in range(2, num):
    if(EhPrimo(p) == True):
      primos.append(p)
    else:
      pass
  print(primos)