import math

leitura = input()
x1 = float(leitura.split()[0])
y1 = float(leitura.split()[1])
leitura = input()
x2 = float(leitura.split()[0])
y2 = float(leitura.split()[1])
print("{:.4f}".format(math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2))))
