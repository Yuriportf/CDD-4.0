tarefas = []

while True:
    print("\nMENU")
    print("1 - Listar Tarefas")
    print("2 - Inserir uma Tarefa")
    print("3 - Deletar Tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção digitando o número correspondente: ")

    if opcao == '1':
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada no momento.")
        else:
            print("Tarefas cadastradas:")
            indice = 1
            for tarefa in tarefas:
                print(f"{indice}. {tarefa}")
                indice += 1

    elif opcao == '2':
        nova_tarefa = input("Digite a descrição da nova tarefa: ")
        tarefas.append(nova_tarefa)
        print("Tarefa adicionada com sucesso!")

    elif opcao == '3':
        if len(tarefas) == 0:
            print("Nenhuma tarefa para deletar.")
        else:
            print("Tarefas cadastradas:")
            numero_tarefa = 1
            for tarefa in tarefas:
                print(f"{numero_tarefa}. {tarefa}")
                numero_tarefa += 1

            entrada_usuario = input("Digite o número da tarefa que deseja deletar: ")

            if entrada_usuario.isdigit():
                numero_digitado = int(entrada_usuario)

                if numero_digitado >= 1 and numero_digitado <= len(tarefas):
                    tarefa_removida = tarefas[numero_digitado - 1]
                    tarefas.pop(numero_digitado - 1)
                    print(f"A tarefa '{tarefa_removida}' foi removida com sucesso.")
                else:
                    print("Número inválido. Nenhuma tarefa corresponde a esse número.")
            else:
                print("Entrada inválida. Por favor, digite apenas números inteiros.")

    elif opcao == '4':
        print("Encerrando o programa. Até logo!")
        break

    else:
        print("Opção inválida. Por favor, digite um número de 1 a 4.")
