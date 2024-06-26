# 1.Calcular Média de Valores em uma Lista
# def calcular_media_de_valores(valores:list) -> float:
#     return sum(valores) / len(valores)

# lista_valores = [1.5, 50.8, 190, 500, 1498, 2024, 165.98]
# valores = calcular_media_de_valores(lista_valores)
# print(valores)

# 2.Filtrar Dados Acima de um Limite
# def filtrar_dados_acima_do_limite(lista_numeros:list, limite:float) -> list:
#     lista_filtrada = [numeros for numeros in lista_numeros if numeros > limite ]

#     return lista_filtrada

# # criando os parâmetros para a função
# numeros = [1, 2, 10, 33.08, 59, 78, 84.56, 120, 2989.98, 5000]
# filtro = 60

# print(filtrar_dados_acima_do_limite(numeros, filtro))

# 3.Contar Valores Únicos em uma Lista
def contar_valores_unicos(lista_numeros:list) -> int:
    return len(set(lista_numeros))

# criando os parâmetros para a função 
valores = [10, 20, 20, 40, 87.9, 87.8, 87.8, 100, 675, 675]
print(contar_valores_unicos(valores))


# 4.Converter Celsius para Fahrenheit em uma List
# 5.Calcular Desvio Padrão de uma Lista
# 6.Encontrar Valores Ausentes em uma Sequência
