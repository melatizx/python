def EhPrimo(num):
  eh_primo = False

  if (not (num % 2 == 0) or num == 2):
    eh_primo = True
    for i in range(3, num):
      if (num % i == 0):
        eh_primo = False
        break
  return eh_primo


if __name__ == '__main__':
  num = int(input("Digite um numero: "))
  primo = EhPrimo(num)
  if (primo):
    print(f"O número {num} é primo")
  else:
    print(f"O número {num} NÃO é primo")