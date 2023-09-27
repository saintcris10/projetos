def somar(*args):
    return sum(args)

def multiplicar(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

def subtrair(*args):
    # Verificar se há pelo menos dois argumentos
    if len(args) < 2:
        return "Pelo menos dois números são necessários para a subtração."

    # Realizar a subtração inicial com o primeiro argumento
    resultado = args[0]

    # Realizar a subtração sequencial com os argumentos restantes
    for i in range(1, len(args)):
        resultado -= args[i]

    return resultado

def dividir(*args):
    # Verificar se há pelo menos dois argumentos
    if len(args) < 2:
        return "Pelo menos dois números são necessários para a divisão."

    # Realizar a divisão inicial com o primeiro argumento
    resultado = args[0]

    # Realizar a divisão sequencial com os argumentos restantes
    for i in range(1, len(args)):
        if args[i] == 0:
            return "Erro: Divisão por zero não é permitida."
        resultado //= args[i]

    return resultado

def par_impar(total):
    if total % 2 == 0:
        return ' o numero é par'
    return 'o numero é impar'

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar
duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)
