numeros = list(map(int, list(input().split())))
print("Sao Multiplos" if numeros[1] % numeros[0] == 0 or numeros[0] % numeros[1] == 0 else "Nao sao Multiplos")
