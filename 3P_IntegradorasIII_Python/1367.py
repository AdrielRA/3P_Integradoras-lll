N = int(input())
while N > 0:
    P = 0
    S = 0
    tempos = [0] * 26
    for i in range(0, N):
        leitura = list(input().split())
        if leitura[2] == "correct":
            P += int(leitura[1])
            P += tempos[ord(leitura[0]) - 64]
            S += 1
        else:
            tempos[ord(leitura[0]) - 64] += 20
    print("{} {}".format(S, P))
    N = int(input())
