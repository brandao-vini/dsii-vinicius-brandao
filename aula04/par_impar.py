# --- EXERCÍCIO 3: PAR OU ÍMPAR ---

# Pede ao usuário para digitar um número inteiro.
numero = int(input("Digite um número inteiro qualquer: "))

# Verifica o resto da divisão do número por 2.
# O símbolo '%' calcula o resto de uma divisão.
# Se o resto da divisão por 2 for igual a 0...
if (numero % 2) == 0:
    # ...o número é par.
    print(f"O número {numero} é PAR.")
# Senão (ou seja, se o resto não for 0)...
else:
    # ...o número é ímpar.
    print(f"O número {numero} é ÍMPAR.")