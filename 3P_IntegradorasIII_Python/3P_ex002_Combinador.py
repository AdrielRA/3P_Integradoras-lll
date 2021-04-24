qnt_testes = int(input())

for i in range(0, qnt_testes):
    str = input()
    str1 = str.split()[0]
    str2 = str.split()[1]
    maior = list(str1)
    menor = list(str2)

    if len(str1) < len(str2):
        maior = list(str2)
        menor = list(str1)

    tam_maior = len(maior)
    tam_menor = len(menor)

    result = list()

    for j in range(0, tam_menor):
        result += str1[j] + str2[j]
    for j in range(tam_menor, tam_maior):
        result += maior[j]
    result = ''.join(result)

    print(result)
