media = float(input("Digite a média do aluno: "))
if media >= 5:
    print(f'A média informada é :{media} Aluno foi aprovado!')
elif media >= 4 and media <= 4.9:
    print('A média informada é :', media, 'Aluno está de recuperação!')
else:
    print('A média informada é :', media, 'Aluno foi reprovado!')
    