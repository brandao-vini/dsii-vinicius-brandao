# --- Programa 4: Cálculo de Prestação em Atraso ---

print("\n--- Calculadora de Prestação em Atraso ---")

# Pede os dados e converte para número (float)
valor_original = float(input("Digite o valor original da prestação: "))
taxa = float(input("Digite a taxa de juros (% ao mês, por exemplo): "))
tempo = float(input("Digite o tempo de atraso (em meses, por exemplo): "))

# Aplica a fórmula para calcular o novo valor com juros
# prestação = valor + (valor * (taxa/100) * tempo)
valor_final = valor_original + (valor_original * (taxa / 100) * tempo)

# Imprime o resultado formatado como moeda (duas casas decimais)
# O :.2f dentro do print formata o número para ter sempre 2 casas depois da vírgula
print(f"\nO valor atualizado da prestação é: R$ {valor_final:.2f}")