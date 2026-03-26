# função para adicionar tarefa, recebe a lista de tarefas e o nome da tarefa a ser adicionada
def adicionar_tarefa(tarefas, nome_tarefa):
    # criado variável tarefa para armazenar o nome da tarefa e seu status de conclusão
    tarefa = {"tarefa": nome_tarefa, "concluida": False}
    tarefas.append(tarefa)
    print(f'Tarefa {nome_tarefa} adicionada com sucesso!')
    return tarefas

# função para listar as tarefas, recebe a lista de tarefas e exibe cada tarefa com seu status de conclusão
def verificar_tarefas(tarefas):
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
    else:
        print("Lista de Tarefas:")
        for idc, tarefa in enumerate(tarefas, start=1):
            status = "✔" if tarefa["concluida"] else "•"
            # criado variável nome_tarefa para armazenar o nome da tarefa e exibir na listagem
            nome_tarefa = tarefa["tarefa"]
            print(f"{idc}. [{status}] - {nome_tarefa}")

def atualizar_tarefa(tarefas, idc, novo_nome):
    if 0 < idc <= len(tarefas):
        # atualiza o nome da tarefa com base no ID fornecido, subtraindo 1 para acessar o índice correto na lista
        tarefas[idc - 1]["tarefa"] = novo_nome
        print(f"Tarefa {idc} atualizada para: {novo_nome}")
    else:
        print("ID da tarefa inválido.")

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
    elif escolha == "3":
        verificar_tarefas(tarefas)
        print("Opção de atualizar tarefa selecionada.")
        idc = int(input("Digite o ID da tarefa a ser atualizada: "))
        novo_nome = input("Digite o novo nome da tarefa: ")
        atualizar_tarefa(tarefas, idc, novo_nome)
    elif escolha == "4":
        print("Opção de marcar tarefa como concluída selecionada.")
    elif escolha == "5":
        print("Opção de excluir tarefa selecionada.")

    elif escolha == "6":
        print("Saindo do gerenciador de tarefas. Até mais!")
        break
   
print("Programa encerrado.")