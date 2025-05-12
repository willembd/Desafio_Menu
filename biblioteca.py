tarefas = []

def exibir_tarefas():
    i=1
    quanti_tarefas = len(tarefas)

    print("======  Lista de Trefas ======")
    if quanti_tarefas == 0:
        print("A lista esta Vazia")
    else:
        for i in range(len(tarefas)):
            print(f"{i+1}. {tarefas[i]}")
    print("=============================")

def inserir_tarefa():
    tarefas.append(input("Digite uma tarefa:"))

def deletar_tarefa():
    quanti_tarefas = len(tarefas)
    exibir_tarefas()

    if quanti_tarefas == 0:
        print("Nenhuma Tarefa para ser Deletada")
    else:
        opdelete = int(input("Número da tarefa para deletar : "))

        if opdelete > quanti_tarefas:
            print("Valor Invalido!!")
        else:
            del tarefas[opdelete-1]

