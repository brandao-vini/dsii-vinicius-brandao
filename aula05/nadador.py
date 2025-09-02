# Exercício 3: Categorias de natação por idade

# Solicita a idade do nadador
idade = int(input("Digite a idade do nadador: "))

# Classifica o nadador na categoria correspondente
if 5 <= idade <= 7:
    print("Categoria: Infantil A")
elif 8 <= idade <= 11:
    print("Categoria: Infantil B")
elif 12 <= idade <= 13:
    print("Categoria: Juvenil A")
elif 14 <= idade <= 17:
    print("Categoria: Juvenil B")
elif idade >= 18:
    print("Categoria: Adultos")
else:
    print("O nadador ainda não tem a idade mínima para participar!")