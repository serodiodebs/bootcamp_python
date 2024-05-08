#Refatorar o códio do desafio da aula 03 para ter type hint nas variáveis utilizadas.

CONSTANTE_VALOR_APLICADO = 1000

nome_validado: bool = False
salario_validado: bool = False
bonus_validado: bool = False

while nome_validado is not True:
    try:
        nome: str = input("Qual seu nome? ")

        if nome.isdigit():
            raise ValueError("Nome de usuário errado.")

        elif len(nome) == 0:
            raise ValueError("Você não digitou nada. Insira seu nome corretamente.")

        elif nome.isspace():
            raise ValueError("Você digitou só espaço. Insira seu nome corretamente.")

        else:
            nome_validado = True
    except ValueError as e:
        print(e)

while salario_validado is not True:
    try:
        salario: float = float(input("Informe seu salário: "))

        if salario < 0:
            print("Digite um valor maior do que Zero para o salário.")

        else:
            salario_validado = True
    except ValueError:
        print("Salário inválido. Insira um valor positivo para o mesmo.")

while bonus_validado is not True:
    try:
        perc_bonus: float = float(input("Qual o seu percentual de bônus? "))

        if perc_bonus < 0:
            print("Digite um valor maior do que Zero para o Bônus.")

        else:
            bonus_validado = True
    except ValueError:
        print("Bônus inválido. Insira um valor positivo para o mesmo.")

resultado = CONSTANTE_VALOR_APLICADO + salario * perc_bonus
print(f"Olá {nome}! O total que você receberá após o bônus é de: {resultado}.")