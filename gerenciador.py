def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "concluida": False}
    tarefas.append(tarefa)
    print(f'Tarefa {nome_tarefa} adicionada com sucesso!')
    return tarefas

def verificar_tarefas(tarefas):
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
    else:
        print("Lista de Tarefas:")
        for idc, tarefa in enumerate(tarefas, start=1):
            status = "✔" if tarefa["concluida"] else "PENDENTE"
            print(f"{idc}. {tarefa['tarefa']} - {status}")

tarefas = []
while True:
    print("\nMenu do gerenciador de Lista de Tarefas:")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Atualizar tarefa")
    print("4. Marcar tarefa como concluída")
    print("5. Excluir tarefa")
    print("6. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == "2":
        verificar_tarefas(tarefas)
    elif escolha == "6":
        print("Saindo do gerenciador de tarefas. Até mais!")
        break
   
print("Programa encerrado.")