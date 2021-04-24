N = int(input())
Dia = N // 86400
Hor = (N - (Dia*86400)) // 3600
Min = (N - ((Dia*86400) + (Hor*3600))) // 60
Seg = N - ((Dia*86400) + (Hor*3600) + (Min*60))
print("{}:{}:{}".format(Hor + Dia * 24, Min, Seg))
