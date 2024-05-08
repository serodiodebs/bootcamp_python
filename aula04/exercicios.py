# Exercícios de Listas e Dicionários
# 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
# v1
# lista : list = [*range(1,11)]

# for num in lista:
#     print(num**2)

# # v2
# lista : list = []
# lista.extend(range(1,11))

# for num in lista:
#     print(f"{num} elevado ao quadrado é: {num**2}")

# # v3
# lista : list = [num for num in range(1,11)]
# i = 0

# while i < len(lista):
#     print(f"{lista[i]} elevado ao quadrado é: {lista[i]**2}")
#     i += 1

# 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
# nomes: list = ["Python", "Java", "C++", "JavaScript"]

#remove c++ e adiciona Ruby
# nomes.remove("C++")
# nomes.append("Ruby")
# print(nomes)

# 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
# livro: dict = {
#     "título": "A Revolução dos Bichos",
#     "autor": "George Orwell",
#     "ano": 1945
# }

# for chave,valor in livro.items():
#     print(f"o {chave} é {valor}")

# 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
# palavra: str = 'paralelepipedo'
# dicionario: dict = {}

# for letra in palavra:
#     if letra in dicionario:
#         dicionario[letra] += 1
#     else:
#         dicionario[letra] = 1
# print(dicionario)

# 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
# lista_frutas: list = ["maçã", "banana", "cereja"]
# valores: dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

# total = sum(valores[fruta] for fruta in lista_frutas)
# print(total)

# 6. Eliminação de Duplicatas
# Dada uma lista de emails, remover todos os duplicados.
# lista_email: list = ["email1@m.com", "email2@m.com","email3@m.com","email1@m.com","email4@m.com","email2@m.com","email6@m.com"]

# lista_nova: list = list(set(lista_email))
# print(f"Lista duplicada: {lista_email}")
# print(f"Lista sem duplicada: {lista_nova}")

# 7. Filtragem de Dados
# Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
# lista_idades: list = [10,20,15,13,19,55,87,90,48,37,63,23,90, 11, 5, 6]

# lista_filtrada: list = [idade for idade in lista_idades if idade >= 19]
# print(lista_filtrada)

# 8. Ordenação Personalizada
# Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
# lista_dicionario = [
#     {"nome": "Amanda"},
#     {"nome": "Sertorio"},
#     {"nome": "Denis"},
#     {"nome": "Edison"},
#     {"nome": "Patricia"}
# ]

# lista_dicionario.sort(key=lambda pessoa: pessoa["nome"])
# print(lista_dicionario)

# 9. Agregação de Dados
# Dado um conjunto de números, calcular a média.
# numeros = [90, 10, 40, 87, 66, 100, 548, 20, 18, 33, 37]

# media_numeros = sum(numeros) / len(numeros)
# print(media_numeros)

# 10. Divisão de Dados em Grupos
# Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
valores = [7, 4, 10, 17, 15, 22, 25, 28, 33, 31, 35, 39, 40, 46, 35, 50, 57, 52, 69, 63, 78, 73]
pares = [num for num in valores if num % 2 == 0 ]
impares = [num for num in valores if num % 2 != 0 ]

print(f"Os pares são: {pares}")
print(f"Os impares são: {impares}") 

# Exercícios com Dicionários

# 11. Atualização de Dados
# Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

# 12. Fusão de Dicionários
# Dados dois dicionários, fundi-los em um único dicionário.

# 13. Filtragem de Dados em Dicionário
# Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

# 14. Extração de Chaves e Valores
# Dado um dicionário, criar listas separadas para suas chaves e valores.

# 15. Contagem de Frequência de Itens
# Dada uma string, contar a frequência de cada caractere usando um dicionário.

# Exercícios de Funções

# 1. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.

# 2. Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.

# 3. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.

# 4. Implemente uma função que receba dois argumentos: uma lista de números e um número. 
# A função deve retornar todas as combinações de pares na lista que somem ao número dado.

# 5. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas