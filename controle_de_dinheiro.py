
# Função para carregar o saldo atual de um arquivo (se existir)
def carregar_saldo():
    try:
        with open("saldo.txt", "r") as arquivo:
            saldo = float(arquivo.read())
        return saldo
    except FileNotFoundError:
        return 0.0

# Função para salvar o saldo em um arquivo
def salvar_saldo(saldo):
    with open("saldo.txt", "w") as arquivo:
        arquivo.write(str(saldo))

# Função para registrar entrada
def registrar_entrada(saldo):
    entrada = float(input("Digite o valor da entrada: "))
    saldo += entrada
    print(f"Entrada de R${entrada} registrada. Saldo atual: R${saldo:.2f}")
    registrar_transacao(f"Entrada de R${entrada}")
    return saldo

# Função para registrar saída
def registrar_saida(saldo):
    saida = float(input("Digite o valor da saída: "))
    if saldo >= saida:
        saldo -= saida
        print(f"Saída de R${saida} registrada. Saldo atual: R${saldo:.2f}")
        registrar_transacao(f"Saída de R${saida}")
        return saldo
    else:
        print("Saldo insuficiente. A saída não pode ser registrada.")
        return saldo

# Função para registrar transações em um arquivo de registro
def registrar_transacao(transacao):
    with open("registro.txt", "a") as arquivo_registro:
        arquivo_registro.write(transacao + "\n")

# Função principal
def main():
    saldo = carregar_saldo()

    while True:
        print("\nSelecione uma opção:")
        print("1. Registrar Entrada")
        print("2. Registrar Saída")
        print("3. Saldo Atual")
        print("4. Sair")

        opcao = input("Escolha uma opção (1/2/3/4): ")

        if opcao == "1":
            saldo = registrar_entrada(saldo)
        elif opcao == "2":
            saldo = registrar_saida(saldo)
        elif opcao == "3":
            print(f"Saldo atual: R${saldo:.2f}")
        elif opcao == "4":
            salvar_saldo(saldo)
            print("Saldo salvo. Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
