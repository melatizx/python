while True:
    xy = list(input().split(" "))
    x = int(xy[0])
    y = int(xy[1])
    if x > y:
        print("Decrescente")
    elif x < y:
        print("Crescente")
    else:
        break