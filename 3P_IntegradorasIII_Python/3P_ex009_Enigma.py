mensagem = input()
crib = input()

tam_msg = len(mensagem)
tam_crib = len(crib)
cont = 0
for i in range(0, tam_msg - tam_crib + 1):
    contar = True
    for j in range(0, tam_crib):
        if crib[j] == mensagem[i + j]:
            contar = False
            break
    if contar:
        cont += 1
print(cont)
