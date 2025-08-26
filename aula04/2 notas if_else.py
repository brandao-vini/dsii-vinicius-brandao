# --- EXERCÍCIO 1: MÉDIA DO ALUNO com IF ELSE ---

# Pede para o usuário digitar a primeira nota e guarda o valor.
# A palavra 'float' serve para garantir que o número possa ter casas decimais (ex: 7.5)
nota1 = float(input("Digite a primeira nota: "))

# Pede para o usuário digitar a segunda nota e guarda o valor.
nota2 = float(input("Digite a segunda nota: "))

# Calcula a média: soma as duas notas e divide por 2.
media = (nota1 + nota2) / 2

# Imprime a média na tela para a pessoa ver.
# O 'f' antes das aspas permite colocar a variável 'media' direto no texto.
print(f"A média do aluno é: {media}")

# Agora, vamos verificar se o aluno foi aprovado.
# 'if' significa "se". Se a média for maior ou igual a 6, faça o seguinte:
if media >= 6:
    # Imprime "Aprovado" na tela.
    print("Resultado: Aprovado")
# 'else' significa "senão". Se a condição do 'if' não for verdadeira, faça isto:
else:
    # Imprime "Reprovado" na tela.
    print("Resultado: Reprovado")