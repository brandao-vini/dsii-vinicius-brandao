# --- Programa 1: Lendo dois caracteres ---

print("--- Digite dois caracteres ---")

# Pede para o usuário digitar o primeiro caractere e guarda na variável 'char1'
# O [0] garante que vamos pegar apenas a primeira letra do que for digitado
char1 = input("Digite o primeiro caractere: ")[0]

# Pede para o usuário digitar o segundo caractere e guarda na variável 'char2'
char2 = input("Digite o segundo caractere: ")[0]

# Imprime na tela a frase formatada com os caracteres digitados
print(f"\nO usuário digitou ({char1}) e ({char2})!")