pontos = list(map(float, list(input().split())))
result = ""
if pontos[0] == 0 and pontos[1] == 0:
    result = "Origem"
elif pontos[0] == 0:
    result = "Eixo Y"
elif pontos[1] == 0:
    result = "Eixo X"
elif pontos[0] > 0:
    if pontos[1] > 0:
        result = "Q1"
    else:
        result = "Q4"
else:
    if pontos[1] > 0:
        result = "Q2"
    else:
        result = "Q3"
print(result)
