# --- EXERCÍCIO 2: MAIOR E MENOR NÚMERO ---

# Pede ao usuário o primeiro número e guarda.
# 'int' é usado aqui porque geralmente comparamos números inteiros.
numero1 = int(input("Digite o primeiro número: "))

# Pede ao usuário o segundo número e guarda.
numero2 = int(input("Digite o segundo número: "))

# Compara os dois números.
# Se o primeiro número for maior que o segundo...
if numero1 > numero2:
    # ...então avisamos qual é o maior e qual é o menor.
    print(f"O número {numero1} é o MAIOR.")
    print(f"O número {numero2} é o MENOR.")
# 'elif' é uma forma de dizer "senão, se...".
# Se o segundo número for maior que o primeiro...
elif numero2 > numero1:
    # ...avisamos que o segundo é o maior.
    print(f"O número {numero2} é o MAIOR.")
    print(f"O número {numero1} é o MENOR.")
# 'else' é para o caso de nenhuma das condições acima ser verdade.
# A única possibilidade que sobra é os dois serem iguais.
else:
    print("Os dois números são iguais.")