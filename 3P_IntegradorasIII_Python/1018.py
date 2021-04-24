N = int(input())
N_ = N
cont_100 = 0
cont_50 = 0
cont_20 = 0
cont_10 = 0
cont_5 = 0
cont_2 = 0
cont_1 = 0
while N >= 100:
    cont_100 += 1
    N -= 100
while N >= 50:
    cont_50 += 1
    N -= 50
while N >= 20:
    cont_20 += 1
    N -= 20
while N >= 10:
    cont_10 += 1
    N -= 10
while N >= 5:
    cont_5 += 1
    N -= 5
while N >= 2:
    cont_2 += 1
    N -= 2
while N >= 1:
    cont_1 += 1
    N -= 1
print(N_)
print("{} nota(s) de R$ 100,00".format(cont_100))
print("{} nota(s) de R$ 50,00".format(cont_50))
print("{} nota(s) de R$ 20,00".format(cont_20))
print("{} nota(s) de R$ 10,00".format(cont_10))
print("{} nota(s) de R$ 5,00".format(cont_5))
print("{} nota(s) de R$ 2,00".format(cont_2))
print("{} nota(s) de R$ 1,00".format(cont_1))
