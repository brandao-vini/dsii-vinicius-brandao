# --- EXERCÍCIO 5: IGUAIS OU DIFERENTES ---

# Pede ao usuário o primeiro número inteiro.
num1 = int(input("Digite o primeiro número inteiro: "))

# Pede ao usuário o segundo número inteiro.
num2 = int(input("Digite o segundo número inteiro: "))

# Compara se os dois números são exatamente iguais.
# Em Python, '==' é usado para comparar se duas coisas são iguais.
if num1 == num2:
    # Se forem iguais, imprime esta mensagem.
    print("Os números digitados são IGUAIS.")
# Senão (se não forem iguais)...
else:
    # ...imprime esta outra mensagem.
    print("Os números digitados são DIFERENTES.")