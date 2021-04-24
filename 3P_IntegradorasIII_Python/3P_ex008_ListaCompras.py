N = int(input())

for i in range(0, N):
    produtos = input()
    produtos = list(produtos.split())
    result = []
    for item in produtos:
        if item not in result:
            result.append(item)
    produtos = ' '.join(sorted(result))
    print(produtos)
