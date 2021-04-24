N = int(input())
for i in range(0, N):
    string = input()
    result = list(string)
    for j in range(0, len(result)):
        if 'A' <= result[j] <= 'Z' or 'a' <= result[j] <= 'z':
            result[j] = chr(ord(result[j]) + 3)
    aux = list(result)
    for j in range(0, len(result)):
        aux[j] = result[(len(result) - j) - 1]
    result = aux
    for j in range(int(len(result) / 2), len(result)):
        result[j] = chr(ord(result[j]) - 1)
    result = ''.join(result)
    print(result)
