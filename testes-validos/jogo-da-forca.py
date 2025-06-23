# Antes de tudo, é necessário um arquivo com o nome 'palavras_forca.txt' com as palavras a serem usadas e caso precise, aletere o caminho até o arquivo

import getpass
import random
import re
import time
import sys

print("Qual modo de jogo deseja jogar?")
print("1 - Usuário x Usuário")
print("2 - Usuário x Máquina")
print("3 - Fechar")

while True:
    try:
        i = int(input(" "))
    except ValueError:
        print("Informe um valor valido!")
        continue

    if i == 3:
        break

    elif i == 1:
        str_select = getpass.getpass("Jogador 1, escolha a palavra (A palavra ficará exibida por 3 segundos após o envio e em seguida ocultará): ")
        print("A palavra escolhida foi: ", end='')
        sys.stdout.flush()
        print(str_select, end='', flush=True)
        time.sleep(3)
        sys.stdout.write('\r' + 'A palavra escolhida foi: ' + '*' * len(str_select) + '\r')
        sys.stdout.flush()


    elif i == 2:
        with open('palavras_forca.txt', 'r') as palavras:
            str = palavras.readlines()
            str = [str2.strip() for str2 in str]
            str_select = random.choice(str)

    else:
        print("Informe um valor valido!")

    str_select = str_select.lower().replace(" ", "-")
    str_ocult = ['_'] * len(str_select)
    errors = []
    chances = 5
    while chances > 0:
        print('\n' + '-' * 30)
        print(f"Você possui {chances} chances")
        print("\n"," ".join(str_ocult))
        print(f"\nErros: {" ".join(errors)}")
        print("\n1 - Chutar letra (Caso de erro, consome uma chance)")
        print("2 - Chutar palavra (Caso de erro, consome duas chances)")
        print("3 - Encerrar jogo")

        try:
            esc = int(input(" "))
        except ValueError:
            print("Informe um valor valido!")
            continue

        if esc == 3:
            break

        elif esc == 1:
            letra = input("Letra: ")
            if re.search(letra, str_select):
                for match in re.finditer(letra, str_select):
                    pos = match.start()
                    str_ocult[pos] = letra
                    if "_" not in str_ocult:
                        print(f"Você acertou! A palavra era {str_select}")
                        break
            else:
                print("Você errou :( continue tentando!")
                errors.append(letra)
                chances = chances - 1

        elif esc == 2:
            chute = input("Palavra: ")
            if chute == str_select:
                print(f"Você acertou! A palavra era {str_select}")
                break
            else:
                print("Você errou :( continue tentando!")
                errors.append(chute)
                chances = chances - 2

        else:
            print("Informe um valor valido!")

    if "_" in str_ocult and chances <= 0:
        print(f"Suas chances acabaram! A palavra era {str_select}")
        break
