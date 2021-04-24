N = int(input())
for i in range (0, N):
    T = int(input())
    alturas = list(map(int, list(input().split())))
    pulos = list(input())
    cont_tiro = 0
    for j in range(0, T):
        if (alturas[j] < 3 and pulos[j] == 'S') or (alturas[j] > 2 and pulos[j] == 'J'):
            cont_tiro += 1
    print(cont_tiro)
