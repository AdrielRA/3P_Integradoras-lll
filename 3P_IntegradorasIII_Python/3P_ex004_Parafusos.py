while True:
    try:
        N = int(input())
        P = []
        for i in range(0, N):
            leitura = list(map(int, list(input().split())))
            for j in range(leitura[0], leitura[1] + 1):
                P.append(j)
        P = sorted(P)
        num = int(input())
        result = ""
        if P.count(num) > 0:
            inicio = P.index(num)
            fim = inicio + P.count(num) - 1
            result = str(num) + " found from " + str(inicio) + " to " + str(fim)
        else:
            result = str(num) + " not found"
        print(result)
    except:
        break
