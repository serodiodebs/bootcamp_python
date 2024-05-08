# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# print(num1 + num2)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# numero1 = int(input("Digite o primeiro número: "))
# resto = numero1 % 5
# print(f"O resto de {numero1} dividido por 5 é: {resto}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# n1 = int(input("Digite o 1º número: "))
# n2 = int(input("Digite o 2º número: "))
# print(n1 * n2)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# n1 = int(input("Digite o 1º número: "))
# n2 = int(input("Digite o 2º número: "))
# print(n1 // n2)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# n1 = int(input("Digite um número: "))
# print(n1 **2)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# NUM1 = 1.7
# NUM2 = 3.6
# print(f"A soma de {NUM1} com {NUM2} é igual à {NUM1 + NUM2}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# num1 = float(input("Digite um numero no formato 0.0: "))
# num2 = float(input("Digite outro numero no formato 0.0: "))
# print((num1 + num2) /2)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# base = float(input("Digite um número: "))
# expoente = int(input("O número será elevado à: "))
# print(base ** expoente)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# celsius = float(input("Digite a temperatura em graus Celsius: "))
# print(f"{celsius} graus Celsius em Fahrenheit é: {(celsius * 1.8) + 32}")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# raio = float(input("Digite o Raio: "))
# print(3.14*(raio**2))

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# palavra = input("Digite uma palavra: ")
# print(f"A palavra que digitou foi: {palavra.upper()}")

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# nome = input("Digite seu nome completo: ")
# print(f"Seu nome é: {nome.upper()}")

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# frase = input("Digite uma frase com espaços no início e final: ")
# frase_ok = frase.strip()
# print(f"A frase é:{frase_ok}")

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# data = input("Digite uma data no formato 'dd/mm/aaa': ")
# data_splitada = data.split("/")
# print(f"Dia: {data_splitada[0]}")
# print(f"Mês: {data_splitada[1]}")
# print(f"Ano: {data_splitada[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# palavra1 = input("Digite uma palavra: ")
# palavra2 = input("Digite mais uma palavra: ")

# print(f"Você digitou as palavras: {palavra1+palavra2}")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
#ex1 = bool(input("True ou False? "))
# ex2 = bool(input("True ou False? "))

# print(f"O AND lógico é {ex1 and ex2}")

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# ex1 = bool(input("True ou False? "))
# ex2 = bool(input("True ou False? "))

# print(f"O OR lógico é {ex1 or ex2}")

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inve90rta esse valor.
# ex1 = bool(input("Digite True ou False? "))
# vl1_invertido = not ex1

# print("O NOT lógico é:", vl1_invertido)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# num1 = int(input("Insira um número: "))
# num2 = int(input("Insira outro número: "))

# resultado = (num1 == num2)
# print("São iguais? ", resultado)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# resultado = (num1 != num2)
# print("São Diferentes? ", resultado)

# #### try-except e if

# 21: Conversor de Temperatura
# try:
#     celsius = float(input("Digite uma temperatura em celsius: "))
#     fahrenheit = (celsius * 9/5) + 32

#     print(f"{celsius} em Fahrenheit é: {fahrenheit}")
# except ValueError:
#     print("Insira um valor numérico para poder realizar o cálculo")

# 22: Verificador de Palíndromo
# palavra = input("Insira uma palavra ou frase: ")

# if isinstance(palavra, str):
#     inverso = palavra.replace(" ", "").lower()
#     if inverso == inverso[::-1]:
#         print("É palíndromo")
#     else:
#         print("Não é palíndromo")
# else:
#     print("Entrada errada, insira uma palavra ou frase")

# 23: Calculadora Simples
# try:
#     numero1 = float(input("Digite o primeiro número: "))
#     numero2 = float(input("Digite o segundo número: "))
#     operacao = input("Qual operação deseja realizar? (Opções: + - * /): ")

#     if operacao == '+':
#         resultado = numero1 + numero2
#     elif operacao == '-':
#         resultado = numero1 - numero2
#     elif operacao == '*':
#         resultado = numero1 * numero2
#     elif operacao == '/':
#         resultado = numero1 / numero2
#     print(resultado)
# except ValueError:
#     print("Você não inseriu um número, favor inserir apenas números para os cálculos.")
# except NameError:
#     print("Impossível realizar a operação desejada. Insira um operador correto.")

# 24: Classificador de Números
# try:
#     numero1 = float(input("Digite um número: "))

#     if numero1 > 0:
#         if numero1 % 2 == 0:
#             resultado = 'Positivo Par'
#         else:
#             resultado = 'Positivo Ímpar'
#     elif numero1 < 0:
#         if numero1 % 2 == 0:
#             resultado = 'Negativo Par'
#         else:
#             resultado = 'Negativo Ímpar'
#     else:
#         resultado = 'Zero'
#     print(resultado)
# except ValueError:
#     print("Verificação impossível. Insira um número.")

# 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula.
# O programa deve converter a string de entrada em uma lista de números inteiros.
# Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro.
# Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro.
# Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

numeros = input("Insira uma lista de números separados por vírgula: ")
numeros_sep = numeros.split(",")
numeros_lista = []

try:
    for numero in numeros_sep:
        numeros_lista.append(int(numero.strip()))
    print("Lista de números: ", numeros_lista)
except ValueError:
    print("Erro. Todos os valores inseridos tem que ser números inteiros.")
