intens = [4, 4.5, 5, 2, 1.5]
entrada = input()
item = int(entrada.split()[0])
qntd = int(entrada.split()[1])
print("Total: R$ {:.2f}".format(intens[item - 1] * qntd))
