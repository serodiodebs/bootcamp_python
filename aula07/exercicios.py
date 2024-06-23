# 1.Calcular Média de Valores em uma Lista
def calcular_media_de_valores(valores:list) -> float:
    return sum(valores) / len(valores)

lista_valores = [1.5, 50.8, 190, 500, 1498, 2024, 165.98]
valores = calcular_media_de_valores(lista_valores)
print(valores)