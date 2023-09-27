

def adicao(x,y):
    return x + y

def subtracao(x,y):
    return x - y

def multiplicaçao(x,y):
    return x * y

def divisao(x,y):
    if y == 0:
        return "Erro: divisão não permitida por zero!"
    return x / y

# função principal

def calculadora():
    while True:
        print("\nBem vindo a calculadora:")
        print("\nSelecione uma operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Digite o número da operação desejada (1/2/3/4/5): ")

        if escolha == "5":
            print("Encerrando a calculadora.")
            
            break

        if escolha not in ("1", "2", "3", "4"):
            print("Opção inválida. Tente novamente.")
            
            continue

        n_1 = float(input("dijite o primeiro numero:"))
        n_2 = float(input("dijite o segundo numero:"))

        if escolha == "1":
            print("resultado:", adicao(n_1 , n_2))
        elif escolha == "2":
            print("resultado:", subtracao(n_1 , n_2))
        elif escolha == "3":
            print("resultado:", multiplicaçao(n_1 , n_2))
        elif escolha == "4":
            resultado = divisao(n_1 , n_2)
            if isinstance(resultado,str):
                print(resultado)
            else:
                print("resultado:", resultado)

if __name__ == "__main":
    calculadora()