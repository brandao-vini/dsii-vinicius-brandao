''' Algoritmo de apresentação de dados do usuário '''
''' Aula 02 - Entrada de Dados '''
# Entrada de dados do usuário
# Usando input para capturar dados do usuário       
nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
idade = int(input('Digite sua idade: ')) #transformando o str em inteiro
print(type(idade))
print(type(nome))
print(nome, sobrenome, idade)
