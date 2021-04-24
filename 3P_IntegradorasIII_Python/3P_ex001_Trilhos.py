class Pilha(object):
    def __init__(self):
        self.dados = []

    def Push(self, elemento):
        self.dados.append(elemento)

    def Pop(self):
        return self.dados.pop(-1) if not self.Empty() else 0

    def Top(self):
        return self.dados[-1] if not self.Empty() else 0

    def Empty(self):
        return len(self.dados) == 0


qnt_vagoes = int(input())

while qnt_vagoes > 0:

    leitura = list(map(int, list(input().split())))
    trem = []
    for i in range(0, qnt_vagoes):
        trem.append(leitura[i])
        if trem[0] == 0:
            break

    while trem[0] > 0:

        P = Pilha()
        atual = 0
        for i in range(1, qnt_vagoes + 1):
            P.Push(i)
            while (not P.Empty()) and (trem[atual] == P.Top()):
                atual += 1
                P.Pop()

        result = "Yes" if P.Empty() else "No"
        print(result)

        leitura = list(map(int, list(input().split())))
        trem.clear()
        for i in range(0, qnt_vagoes):
            trem.append(leitura[i])
            if i == 0 and trem[i] == 0:
                break
    print('')
    qnt_vagoes = int(input())
