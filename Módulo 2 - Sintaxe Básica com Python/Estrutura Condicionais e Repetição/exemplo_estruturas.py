# Passo 1: Criar uma lista de convidados
convidados = []

# Passo 2: Pedir ao usuário quantos convidados deseja adicionar
quantidade = int(input("Quantos convidados deseja adicionar? "))

# Usando FOR para adicionar convidados à lista
for i in range(quantidade):
    nome = input(f"Digite o nome do {i + 1}º convidado: ")
    convidados.append(nome)

# Passo 3: Criar um menu usando um loop WHILE
while True:
    print("\n=== MENU ===")
    print("1 - Mostrar lista de convidados")
    print("2 - Remover um convidado")
    print("3 - Procurar um convidado")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:  # Mostrar a lista de convidados
        print("\nLista de Convidados:")
        for convidado in convidados:  # Percorrendo a lista com FOR
            print(f"- {convidado}")

    elif opcao == 2:  # Remover um convidado
        nome_remover = input("Digite o nome do convidado para remover: ")
        if nome_remover in convidados:
            convidados.remove(nome_remover)
            print(f"{nome_remover} foi removido da lista.")
        else:
            print("Convidado não encontrado! Tente novamente.")
            continue  # Volta para o menu sem executar mais nada

    elif opcao == 3:  # Procurar um convidado
        nome_procurar = input("Digite o nome do convidado para buscar: ")
        if nome_procurar in convidados:
            print(f"{nome_procurar} está na lista de convidados!")
        else:
            print(f"{nome_procurar} NÃO está na lista!")

    elif opcao == 4:  # Sair do programa
        print("Saindo... Obrigado por usar o sistema!")
        break  # Interrompe o loop

    else:
        print("Opção inválida! Escolha um número entre 1 e 4.")
