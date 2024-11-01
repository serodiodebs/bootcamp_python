nome = input("Digite seu nome: ")
salario = float(input("Informe seu salário sem centavos, apenas o número redondo: "))
bonus = float(input("Qual o seu percentual de bônus? Digite: "))
total = 1000 + salario * bonus

print(f"Olá {nome}, o seu salário é {salario} e o % de bônus informado foi de {bonus}, sendo assim o total recebido será: {total}")