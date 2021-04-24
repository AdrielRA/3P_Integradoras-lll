import math
valores = list(map(float, list(input().split())))
delta = math.pow(valores[1], 2) - 4 * valores[0] * valores[2]
if delta > 0 and 0 < valores[0]:
    print("R1 = {:.5f}".format((-valores[1] + math.sqrt(delta)) / (2 * valores[0])))
    print("R2 = {:.5f}".format((-valores[1] - math.sqrt(delta)) / (2 * valores[0])))
else:
    print("Impossivel calcular")
