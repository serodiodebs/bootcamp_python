### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

# quantidade = int(input("Digite a quantidade: "))
# preco = float(input("Digite o preço: "))

# if quantidade > 0 and preco > 0:
#     print("Dados Válidos")
# else:
#     print("Dados inválidos")


### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

# temperatura = int(input("Digite a temperatura: "))

# if temperatura < 18:
#     print("Temperatura Baixa")
# elif temperatura >= 18 and temperatura <= 26:
#      print("Temperatura Normal")
# else:
#       print("Temperatura Alta")

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

# if log['level'] == 'ERROR':
#     print(log['message'])


### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# idade = int(input("Digite sua idade: "))
# email = input("Digite seu e-mail: ")

# if not 18 <=  idade <= 65:
#     print("Idade fora do esperado.")
# elif "@" not in email or "." not in email:
#     print("e-mail inválido")
# else:
#     print("Dados válidos") 


### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

# transacao = {'valor': 9000, 'hora': 22}
# if transacao['valor'] > 10000 or transacao['hora'] < 9 or transacao['hora'] > 18:
#     print("Transação Suspeita")
# else:
#     print("Transação ok")

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
# texto = "Era uma casa muito engraçada não tinha teto não tinha nada"
# palavras = texto.split()
# contagem = {}

# for palavra in palavras:
#     if palavra in contagem:
#         contagem[palavra] += 1
#     else:
#         contagem[palavra] = 1

# print(contagem)

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
# numeros = [10, 20, 30, 40, 50]
# minimo = min(numeros)
# maximo = max(numeros)
# normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

# print(normalizados)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando
# usuarios = [
#     {"nome": "Alice", "email": "alice@example.com"},
#     {"nome": "Bob", "email": ""},
#     {"nome": "Carol", "email": "carol@example.com"},
#     {"nome": "Marlon", "email": ""},
# ]

# usuarios_invalidos = [usuario for usuario in usuarios if not usuario["email"]]
# print(usuarios_invalidos)

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.
# numeros = [1,2,3,4,5,1000,549,320, 797]

# extraidos = [numero for numero in numeros if numero % 2 == 0]
# print(extraidos)

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
# vendas = [
#     {"categoria": "eletrônicos", "valor": 1200},
#     {"categoria": "livros", "valor": 200},
#     {"categoria": "eletrônicos", "valor": 800}
# ]

# totais = {}

# for item in vendas:
#     categoria = item["categoria"]
#     valor = item["valor"]

#     if categoria in totais:
#         totais[categoria] += valor
#     else:
#         totais[categoria] = valor

# print(totais)

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
# entrada = ""
# while entrada != "sair":
#     entrada = input("Digite o que quiser. Mas, para sair digite a palavra 'sair'. ")


### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
# intervalo = int(input("Digite um número entre 16 e 21: "))

# while intervalo < 16 or intervalo > 21:
#     print("Número não está dentro do intervalo. Favor digitar o número correto.")
#     intervalo = int(input("Digite um número entre 16 e 21: "))
# print(intervalo)

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.
# pag_inicial = 1
# pag_final = 3

# while pag_inicial <= pag_final:
#     print(f"Processamento da página {pag_inicial} de {pag_final}")
#     pag_inicial += 1
# print("Todas as páginas foram processadas")

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
# tentativa_ini = 1
# tentativa_fim = 3

# while tentativa_ini <= tentativa_fim:
#     print(f"Tentativa {tentativa_ini} de {tentativa_fim}")
#     #entra o código pra conectar aqui. 
#     if not True: #aqui seria caso true. Mas pro exercício tem que ser false mesmo
#         print("Conectado com sucesso!")
#         break
#     tentativa_ini += 1
# else:
#     print("Máxima de tentativas atingidas.")

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

lista = [1, 2, 3, 'gato', 'parar', 14.97]
i = 0

while i < len(lista):
    if lista[i] == 'parar':
        print("Condição de parada identificada.")
        break
    print(f"item: {lista[i]}")
    i += 1
print("todos itens processados")
