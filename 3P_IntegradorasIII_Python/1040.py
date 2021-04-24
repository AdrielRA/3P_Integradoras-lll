notas = list(map(float, list(input().split())))
media = (notas[0] * 2 + notas[1] * 3 + notas[2] * 4 + notas[3] * 1) / 10
print("Media: {:.1f}".format(media))
if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_exame = float(input())
    print("Nota do exame: {:.1f}".format(nota_exame))
    media = (media + nota_exame) / 2
    if media >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {:.1f}".format(media))
