import math
import statistics

# <defs>
def formatar(resul):
    return int(resul) if resul == int(resul) else resul

def media(num):
    return sum(num) / len(num)

def calcular_mmc(a, b):
    return abs(a * b) // math.gcd(a, b)

def e_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
# </defs>

# <defs avcds>
def media_ponderada(val, pes):
    return sum(v * p for v, p in zip(val, pes)) / sum(pes)
            
def juros_compostos(capital, taxa, tempo):
    return capital * (1 + taxa / 100) ** tempo
            
def pa(primeiro, razao, termos):
        return [primeiro + razao * i for i in range(termos)]

def pg(primeiro, razao, termos):
    return [primeiro * (razao ** i) for i in range(termos)]
#</defs avcds>


while True:
    
    print("Seleciona a opereação: ")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Porcentagem")
    print("6 - Elevar")
    print("7 - Raiz Quadrada")
    print("8 - Raiz Cubica")
    print("9 - Area")
    print("10 - Media")
    print("11 - Fatorial")
    print("12 - Módulo")
    print("13 - Logaritmo")
    print("14 - Conversão de unidades")
    print("15 - MMC/MDC")
    print("16 - Identificador de Numero Primo")
    print("17 - Trigonometria")
    print("18 - Sequência de Fibonacci")
    print("19 - Avançado")
    print("20 - Sair")
    ope = int(input(" "))
      
    if ope == 20: 
        break

    elif ope in {1, 2, 3, 4}:
        n1 = float(input("n1: "))
        n2 = float(input("n2: "))
        if ope == 1:
            resul = n1 + n2
            print(f"Resultado: {formatar(resul)}")

        elif ope == 2:
            resul = n1 - n2
            print(f"Resultado: {formatar(resul)}")

        elif ope == 3:
            resul = n1 * n2
            print(f"Resultado: {formatar(resul)}")

        elif ope == 4:
            resul = n1 / n2
            print(f"Resultado: {formatar(resul)}")

    elif ope == 5:
        n1 = float(input("num: "))
        n2 = float(input("%: "))
        resul = (n1 * n2) / 100
        print(f"Resultado: {formatar(resul): .2f}%")

    elif ope == 6:
        base = float(input("base: "))
        expo = int(input("expoente: "))
        resul = pow(base, expo)
        print(f"Resultado: {formatar(resul)}")

    elif ope in {7, 8}:
        n1 = float(input("num: "))
        if ope == 7:
            resul = math.sqrt(n1)
            print(f"Resultado: {formatar(resul)}")

        elif ope == 8:
            resul = math.pow(n1, 1/3)
            print(f"Resultado: {formatar(resul)}")

    elif ope == 9:
        print("Qual area deseja calcular?")
        print("1 - Quadrado")
        print("2 - Retângulo")
        print("3 - Triângulo")
        print("4 - Circulo")
        print("5 - Trapézio")
        print("6 - Sair")
        calcarea = int(input(" "))

        if calcarea == 6:
            continue
        elif calcarea == 1:
            lado = float(input("lado: "))
            resul = lado * lado 
            print(f"Resultado: {formatar(resul)}")
        elif calcarea in {2, 3}:
            base = float(input("base: "))
            altura = float(input("altura: "))
            if calcarea == 2:
                resul = base * altura
                print(f"Resultado: {formatar(resul)}")
            elif calcarea == 3:
                resul = (base * altura) / 2
                print(f"Resultado: {formatar(resul)}")
        elif calcarea == 4:
            raio = float(input("raio: "))
            resul = math.pi * (raio * raio)
            print(f"Resultado: {formatar(resul)}")
        elif calcarea == 5:
            base1 = float(input("base maior: "))
            base2 = float(input("base menor: "))
            altura = float(input("altura: "))
            resul = ((base1 + base2) * altura) / 2
            print(f"Resultado: {formatar(resul)}")
        else:
            print("ERROR, INSIRA UM VALOR VALIDO!")
            continue

    elif ope == 10:
        num = list(map(float, input("digite números separados por espaço: ").split()))
        print(f"Resultado: {formatar(media(num)): .2f}")

    elif ope == 11:
        num = int(input("num: "))
        resul = math.factorial(num)
        print(f"Resultado: {formatar(resul)}")

    elif ope == 12:
        num = float(input("num: "))
        resul = abs(num)
        print(f"Resultado: {formatar(resul)}")

    elif ope == 13:
        print("Selecione o tipo de log: ")
        print("1 - Natural (base e)")
        print("2 - Base Personalizada")
        print("3 - Base 10")
        print("4 - Sair")
        log = int(input(" "))

        if log == 4:
            continue
        elif log == 1:
            num = float(input("num: "))
            resul = math.log(num)
            print(f"Resultado: {formatar(resul)}")
        elif log == 2:
            num = float(input("num: "))
            base = float(input("base: "))
            resul = math.log(num, base)
            print(f"Resultado: {formatar(resul)}")
        elif log == 3:
            num = float(input("num: "))
            resul = math.log10(num)
        else:
            print("ERROR, INSIRA UM VALOR VALIDO!")
            continue

    elif ope == 14:
        print("Qual tipo de conversão gostaria de realizar?")
        print("1 - Distancia")
        print("2 - Tempo")
        print("3 - Temperatura")
        print("4 - Sair")
        decisao = int(input(" "))

        if decisao == 4:
            continue

        elif decisao == 1:
            print("Defina oque quer converter")
            print("1 - CM => M")
            print("2 - M => KM")
            print("3 - KM => M")
            print("4 - M => CM")
            print("5 - Sair")
            dist = int(input(" "))

            if dist == 5:
                continue
            elif dist == 1:
                cm = float(input("cm: "))
                m = cm / 100
                print(f"Resultado: {formatar(m)}m")
            elif dist in {2, 4}:
                m = float(input("m: "))
                if dist == 2:
                    km = m / 1000
                    print(f"Resultado: {formatar(km)}km")
                elif dist == 4:
                    cm = m * 100
                    print(f"Resultado: {formatar(cm)}cm")
            elif dist == 3:
                km = float(input("km: "))
                m = km * 1000
                print(f"Resultado: {formatar(m)}m")
            else:
                print("ERROR, INSIRA UM VALOR VALIDO!")
                continue

        elif decisao == 2:
            print("Defina oque quer converter")
            print("1 - Seg => Min")
            print("2 - Min => Hora")
            print("3 - Hora => Min")
            print("4 - Min => Seg")
            print("5 - Sair")
            tempo = int(input(" "))

            if tempo == 5:
                continue
            elif tempo == 1:
                seg = float(input("seg: "))
                min = seg / 60
                print(f"Resultado: {formatar(min)} min(s)")
            elif tempo in {2, 4}:
                min = float(input("min: "))
                if tempo == 2:
                    hora = min / 60
                    print(f"Resultado: {formatar(hora)} hora(s)")
                elif tempo == 4:
                    seg = min * 60
                    print(f"Resultado: {formatar(seg)} seg(s)")
            elif tempo == 3:
                hora = float(input("km: "))
                min = hora * 60
                print(f"Resultado: {formatar(min)} min(s)")
            else:
                print("ERROR, INSIRA UM VALOR VALIDO!")
                continue

        elif decisao == 3:
            print("Defina oque quer converter")
            print("1 - Celsius => Kelvin")
            print("2 - Celsius => Fahrenheit")
            print("3 - Kelvin => Celsius")
            print("4 - Kelvin => Fahrenheit")
            print("5 - Fahrenheit => Celsius")
            print("6 - Fahrenheit => Kelvin")
            print("7 - Sair")
            graus = int(input(" "))

            if graus == 7:
                continue
            elif graus in {1, 2}:
                c = float(input("celsius: "))
                if graus == 1:
                    k = c + 273.15
                    print(f"Resultado: {formatar(k)} K")
                elif graus == 2:
                    f = (c * 9/5) + 32
                    print(f"Resultado: {formatar(k): .2f} °F")
            elif graus in {3, 4}:
                k = float(input("kelvin: "))
                if graus == 3:
                    c = k - 273.15
                    print(f"Resultado: {formatar(k): .2f} °C")
                elif graus == 4:
                    f = (k - 273.15) * 9/5 + 32
                    print(f"Resultado: {formatar(k): .2f} °F")
            elif graus in {5, 6}:
                f = float(input("fahrenheit: "))
                if graus == 5:
                    c = (f - 32) * 5/9
                    print(f"Resultado: {formatar(k): .2f} °C")
                elif graus == 6:
                   k = (f - 32) * 5/9 + 273.15
                   print(f"Resultado: {formatar(k)} K")
            else:
                print("ERROR, INSIRA UM VALOR VALIDO!")
                continue

        elif ope == 15:
            n1 = int(input("num1: "))
            n2 = int(input("num2: "))
            mdc = math.gcd(n1, n2)
            mmc = calcular_mmc(n1, n2)
            print(f"MDC: {formatar(mdc)}")
            print(f"MMC: {formatar(mmc)}")

        elif ope == 16:
            num = int(input("num: "))
            print(f"{'Sim, é primo' if e_primo(num) else 'Não é primo'}")

        elif ope == 17:
            angulo = int(input("angulo: "))
            radiano = math.radians(angulo)
            print(f"Seno: {math.sin(radiano)}")
            print(f"Cosseno: {math.cos(radiano)}")
            print(f"Tangente: {math.tan(radiano)}")

        elif ope == 18:
            num = int(input("posição: "))
            print(f"Numero correspondente: {fibonacci(num)}")

        elif ope == 19:
            print("1 - Media Ponderada")
            print("2 - Permutação/Combinação")
            print("3 - Conversão de Moedas")
            print("4 - Conversão Base Numerica")
            print("5 - Juros Compostos")
            print("6 - Desvio Padrão")
            print("7 - Progressões")
            print("8 - Conversão de Massa")
            print("9 - Hipotenusa")
            print("10 - Velocidade Media")
            print("11 - Sair")
            avcd = int(input(" "))

            if avcd == 11:
                continue

            elif avcd == 1:
                val = list(map(float, input("valores separados por espaço: ").split()))
                pes = list(map(float, input("pesos separados por espaço: ").split()))
                print(print(f"Resultado: {media_ponderada(val, pes): .2f}"))

            elif avcd == 2:
                print("Selecione qual: ")
                print("1 - Permutação")
                print("2 - Combinação")
                print("3 - Sair")
                pc = int(input(" "))

                if pc == 3:
                    continue

                elif pc == 1:
                    e = int(input("elementos: "))
                    p = int(input("posições: "))
                    resul = math.perm(e, p)
                    print(f"Resultado: {resul}")

                elif pc == 2:
                    e = int(input("elementos: "))
                    esc = int(input("escolhas: "))
                    resul = math.comb(e, esc)
                    print(f"Resultado: {resul}")

                else:
                    print("ERROR, INSIRA UM VALOR VALIDO!")
                    continue
            
            elif avcd == 3:
                print("Volte mais tarde, estamos trabalhando na conversão de moedas! :)")
                continue

            elif avcd == 4:
                num = int(input("num: "))
                print(f"Binário: {bin(num)[2:]}")
                print(f"Octal: {oct(num)[2:]}")
                print(f"Hexadecimal: {hex(num)[2:]}")

            elif avcd == 5:
                capital = float(input("capital inicial: "))
                taxa = float(input("taxa de juros (% ao mês): "))
                tempo = int(input("meses: "))
                print(f"Final: {juros_compostos(capital, taxa, tempo): .2f}")
            
            elif avcd == 6:
                numeros = list(map(float, input("números separados por espaço: ").split()))
                print(f"Desvio Padrão: {statistics.stdev(numeros): .2f}")

            elif avcd == 7:
                print("Selecione a progressão: ")
                print("1 - Aritmética")
                print("2 - Geométrica")
                print("3 - Sair")
                progre = int(input(" "))

                if progre == 3:
                    continue

                elif progre == 1:
                    primeiro = float(input("primeiro termo: "))
                    razao = float(input("razão: "))
                    termos = int(input("qtd de termos: "))
                    print(f"PA: {pa(primeiro, razao, termos)}")

                elif progre == 2:
                    primeiro = float(input("primeiro termo: "))
                    razao = float(input("razão: "))
                    termos = int(input("qtd de termos: "))
                    print(f"PG: {pg(primeiro, razao, termos)}")
                
                else:
                    print("ERROR, INSIRA UM VALOR VALIDO!")
                    continue
            
            elif avcd == 8:
                print("Selecione qual conversão fazer: ")
                print("1 - MG => G")
                print("2 - G => KG")
                print("3 - KG => G")
                print("4 - G => MG")
                print("5 - Sair")
                esc_massa = int(input(" "))

                if esc_massa == 5:
                    continue

                elif esc_massa == 1:
                    val = float(input("massa: "))
                    print(f"{formatar(val*0.001)}G")
                
                elif esc_massa == 2:
                    val = float(input("massa: "))
                    print(f"{formatar(val*0.001)}KG")

                elif esc_massa == 3:
                    val = float(input("massa: "))
                    print(f"{formatar(val*1000)}G")
                
                elif esc_massa == 4:
                    val = float(input("massa: "))
                    print(f"{formatar(val*1000)}MG")
                
                else:
                    print("ERROR, INSIRA UM VALOR VALIDO!")
                    continue 

        else:
                print("ERROR, INSIRA UM VALOR VALIDO!")
                continue
    
    print("Deseja realizar outra operação?")
    outra = input("'sim' ou 'não': ")

    if outra.lower() == 'não' or outra.lower() == 'nao':
        break
    else:
        pass
