lados = list(map(float, list(input().split())))
if ((lados[1] - lados[2]) < lados[0] < (lados[1] + lados[2])) and (
        (lados[0] - lados[2]) < lados[1] < (lados[0] + lados[2])) and (
        (lados[0] - lados[1]) < lados[2] < (lados[0] + lados[1])):
    print("Perimetro = {:.1f}".format(lados[0] + lados[1] + lados[2]))
else:
    print("Area = {:.1f}".format(((lados[0] + lados[1]) * lados[2]) / 2))
