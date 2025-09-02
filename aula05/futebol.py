# Exercício 1: Resultado da partida de futebol

# Solicita o número de gols de cada time
gols_time1 = int(input("Digite o número de gols do primeiro time: "))
gols_time2 = int(input("Digite o número de gols do segundo time: "))

# Verifica o resultado da partida
if gols_time1 > gols_time2:
    print(f"\nO resultado foi {gols_time1} a {gols_time2}.")
    print("Vitória do primeiro time!")
elif gols_time2 < gols_time1:
    print(f"\nO resultado foi {gols_time1} a {gols_time2}.")
    print("Vitória do segundo time!")
else:
    print(f"\nO resultado foi {gols_time1} a {gols_time2}.")
    print("O jogo terminou em empate.")