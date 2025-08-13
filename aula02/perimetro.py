# --- Programa 3: Perímetro e Área de um Retângulo ---

print("\n--- Calcule a Área e o Perímetro de um Retângulo ---")

# Pede a base e converte para número (float aceita casas decimais)
base = float(input("Digite o valor da base: "))

# Pede a altura e converte para número
altura = float(input("Digite o valor da altura: "))

# Calcula o perímetro: (base + altura) * 2
perimetro = 2 * (base + altura)

# Calcula a área: base * altura
area = base * altura

# Imprime os resultados calculados
print(f"\nO perímetro do retângulo é: {perimetro}")
print(f"A área do retângulo é: {area}")