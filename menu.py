from biblioteca import inserir_tarefa, exibir_tarefas, deletar_tarefa

op = 0

while op != 4:
    print("==========  MENU  ==========")
    print("1. Lista de Terefas")
    print("2. Inserir Tarefas")
    print("3. Deletar Tarefa")
    print("4. Sair")

    op = int(input("Digite o número da Opção: "))

    match op:
        case 1:
            exibir_tarefas()
        case 2:
            inserir_tarefa()
        case 3:
            deletar_tarefa()
        case 4:
            break
