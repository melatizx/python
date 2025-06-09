while True:
  try:
    vol = float(input(""))
    dia = float(input(""))

    raio = dia/2
    altura = vol / (3.14 * raio**2)
    area = 3.14*raio**2
    altura2 = "{:.2f}".format(altura)
    area2 = "{:.2f}".format(area)
    print(f"ALTURA = {altura2}")
    print(f"AREA = {area2}")

  except EOFError:
    break