#lista
operacoes = [
    "[1] Somar", "[2] Subtrair", "[3] Multiplicar",
    "[4] Dividir", "[5] Exponenciação", "[6] Raiz Quadrada"
]

# Créditos 
print("\ndesenvolvido por Vinícius Brandão - 3DS - Noturno - Prof. Itai!")

print("---------------------------")


print("-- Menu --")
for item in operacoes:
    print(item)
print("---------------------------")


escolha = input("Escolha uma operação, dentre a quantidade listada acima: ")


if escolha == '6':
    
    num = float(input("Digite o número: "))
    if num < 0:
        print("Erro: Não existe raiz real de número negativo.")
    else:
    
        resultado = num ** 0.5
        print(f"A raiz quadrada de {num} é: {resultado}")

elif escolha in ['1', '2', '3', '4', '5']:
    
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print(f"Resultado: {num1 + num2}")
    elif escolha == '2':
        print(f"Resultado: {num1 - num2}")
    elif escolha == '3':
        print(f"Resultado: {num1 * num2}")
    elif escolha == '4':
        if num2 == 0:
            print("Erro: Divisão por zero não é permitida.")
        else:
            print(f"Resultado: {num1 / num2}")
    elif escolha == '5':
        
        print(f"Resultado: {num1 ** num2}")
else:
    
    print("Opção inválida. Por favor, reinicie o programa.")

