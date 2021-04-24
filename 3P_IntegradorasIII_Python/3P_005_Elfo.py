class Rena:
    def __init__(self):
        self.S = ""
        self.P = 0
        self.I = 0
        self.A = 0.0


T = int(input())
for i in range(0, T):
    leitura = input()
    N = int(leitura.split()[0])
    M = int(leitura.split()[1])
    renas = []
    for j in range(0, N):
        leitura = input()
        rena = Rena()
        rena.S = leitura.split()[0]
        rena.P = int(leitura.split()[1])
        rena.I = int(leitura.split()[2])
        rena.A = float(leitura.split()[3])
        renas.append(rena)
    renas.sort(key=lambda x: (-x.P, x.I, x.A, x.S))
    print("CENARIO {" + str(i + 1) + "}")
    for j in range(0, M):
        print(str(j + 1) + " - " + renas[j].S)


"""class Rena:
    def __init__(self):
        self.S = ""
        self.P = 0
        self.I = 0
        self.A = 0.0


def ordenar(lista, rena_aux, pos):
    while pos > 0 and rena_aux.P > lista[pos - 1].P:
        lista[pos] = lista[pos - 1]
        pos -= 1
    while pos > 0 and rena_aux.P == lista[pos - 1].P:
        if rena_aux.I < lista[pos - 1].I:
            lista[pos] = lista[pos - 1]
            pos -= 1
        else:
            break
    while pos > 0 and rena_aux.I == lista[pos - 1].I:
        if rena_aux.A < lista[pos - 1].A:
            lista[pos] = lista[pos - 1]
            pos -= 1
        else:
            break
    while pos > 0 and rena_aux.A == lista[pos - 1].A:
        if rena_aux.S < lista[pos - 1].S:
            lista[pos] = lista[pos - 1]
            pos -= 1
        else:
            break
    lista[pos] = rena_aux


T = int(input())
for i in range(0, T):
    leitura = input()
    N = int(leitura.split()[0])
    M = int(leitura.split()[1])
    renas = []
    for j in range(0, N):
        leitura = input()
        rena = Rena()
        rena.S = leitura.split()[0]
        rena.P = int(leitura.split()[1])
        rena.I = int(leitura.split()[2])
        rena.A = float(leitura.split()[3])
        renas.append(rena)
        ordenar(renas, rena, j)
    print("CENARIO {" + str(i + 1) + "}")
    for j in range(0, M):
        print(str(j + 1) + " - " + renas[j].S)
"""
