palavra = list(input().split())
qnt = 0
jipe = 0
while palavra[0] not in "ABEND":
    T = int(palavra[1])
    if palavra[0] in "SALIDA":
        qnt += T
        jipe += 1
    else:
        qnt -= T
        jipe -= 1
    palavra = list(input().split())
print(qnt)
print(jipe)
