valores = list(map(int, list(input().split())))
result = "Valores nao aceitos"
if valores[1] > valores[2] and valores[3] > valores[0]:
    if valores[2] + valores[3] > valores[0] + valores[1]:
        if 0 < valores[2] and 0 < valores[3]:
            if valores[0] % 2 == 0:
                result = "Valores aceitos"
print(result)
