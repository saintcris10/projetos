# calcular uma area:

def calcular_area_quadrada(comrpimento, altura):
    area = comrpimento * altura
    return area

# Solicitar a base e a altura ao usuário
comprimento = float(input("Digite o comprimento da area: "))
altura = float(input("Digite a altura da area: "))

# Calcular a área usando a função
area_resultante = calcular_area_quadrada(comprimento, altura)

# Exibir o resultado
print(f"A área total com comprimento {comprimento} e altura {altura} é igual a {area_resultante}.")

