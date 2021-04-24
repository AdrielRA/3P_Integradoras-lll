while True:
    try:
        texto = input()
        result = []
        lado = 0
        pos_cont = 0
        for i in range(0, len(texto)):
            if texto[i] == ']':
                lado = -1
                pos_cont = 0
            elif texto[i] == '[':
                lado = 0
                pos_cont = 0
            elif texto[i] != '[' and texto[i] != ']':
                result.insert(pos_cont, texto[i]) if lado == 0 else result.append(texto[i])
                pos_cont += 1
        print(''.join(result))
    except EOFError:
        break
