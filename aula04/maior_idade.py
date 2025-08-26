# --- EXERCÍCIO 4: MAIOR DE IDADE ---

# Define o ano atual.
# Você pode mudar este valor para o ano em que estiver executando o código.
ano_atual = 2025

# Pergunta o ano de nascimento e guarda o número.
ano_nascimento = int(input("Em que ano você nasceu? "))

# Calcula a idade da pessoa.
idade = ano_atual - ano_nascimento

# Imprime a idade calculada para a pessoa conferir.
print(f"Quem nasceu em {ano_nascimento} tem (ou fará) {idade} anos em {ano_atual}.")

# Verifica se a idade é maior ou igual a 18.
if idade >= 18:
    # Se for, a pessoa é maior de idade.
    print("Você é MAIOR de idade.")
# Senão...
else:
    # ...a pessoa é menor de idade.
    print("Você é MENOR de idade.")