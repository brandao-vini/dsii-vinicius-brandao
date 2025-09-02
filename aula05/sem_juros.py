# Exercício 2: Cálculo de prestações sem juros

# Solicita o valor total da compra e o número de prestações
valor_compra = float(input("Digite o valor total da compra: R$ "))
numero_prestacoes = int(input("Digite o número de prestações: "))

# Calcula o valor de cada prestação
if numero_prestacoes > 0:
    valor_prestacao = valor_compra / numero_prestacoes
    print(f"\nO valor de cada uma das {numero_prestacoes} prestações será de R$ {valor_prestacao:.2f}.")
else:
    print("\nO número de prestações deve ser maior que zero.")