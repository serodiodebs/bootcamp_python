# nome = input("Qual seu nome? ")
# salario = float(input("Informe seu salário: "))
# perc_bonus = float(input("Qual o seu percentual de bônus? "))

# resultado = 1000 + (salario * perc_bonus)

# print(f"Olá {nome}! o total que você receberá após o bônus é de: {resultado}")

# Incremento no desafio da aula01

# Para resolver os bugs identificados — tratamento de entradas inválidas que não podem ser convertidas
# para um número de ponto flutuante e prevenção de valores negativos para salário e bônus,
# você pode modificar o código diretamente. Isso envolve adicionar verificações adicionais
# após a tentativa de conversão para garantir que os valores sejam positivos.

CONSTANTE_VALOR_APLICADO = 1000

try:
    nome = input("Qual seu nome? ")

    if nome.isdigit():
        raise ValueError("Nome de usuário errado.")
        exit()

    elif len(nome) == 0:
        raise ValueError("Você não digitou nada. Insira seu nome corretamente.")
        exit()

    elif nome.isspace():
        raise ValueError("Você digitou só espaço. Insira seu nome corretamente.")
        exit()

except ValueError as e:
    print(e)
    exit()

try:
    salario = float(input("Informe seu salário: "))

    if salario < 0:
        print("Digite um valor maior do que Zero para o salário.")

except ValueError:
    print("Salário inválido. Insira um valor positivo para o mesmo.")
    exit()

try:
    perc_bonus = float(input("Qual o seu percentual de bônus? "))

    if perc_bonus < 0:
        print("Digite um valor maior do que Zero para o Bônus.")

except ValueError:
    print("Bônus inválido. Insira um valor positivo para o mesmo.")
    exit()

resultado = CONSTANTE_VALOR_APLICADO + (salario * perc_bonus)
print(f"Olá {nome}! O total que você receberá após o bônus é de: {resultado}.")
