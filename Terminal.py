from BD_Geral import adicionar_tarefa
from BD_Geral import listar_tarefas
from BD_Geral import concluir_tarefa
from BD_Geral import excluir_tarefa

def menu():
    print("\n=== Gerenciador de Tarefas ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Excluir tarefa")
    print("5. Sair")

def executar():
    while True:
        menu()
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            titulo = input("Título da tarefa: ")
            descricao = input("Descrição da tarefa: ")
            data_vencimento = input("Data de vencimento (YYYY-MM-DD): ")
            prioridade = int(input("Prioridade (1-Alta, 2-Média, 3-Baixa): "))
            adicionar_tarefa(titulo, descricao, data_vencimento, prioridade)
            print("Tarefa adicionada com sucesso!")
        
        elif escolha == "2":
            tarefas = listar_tarefas()
            for tarefa in tarefas:
                status = "Concluída" if tarefa[5] else "Pendente"
                print(f"[{tarefa[0]}] {tarefa[1]} - {tarefa[2]} (Vence: {tarefa[3]}, Prioridade: {tarefa[4]}) - {status}")
        
        elif escolha == "3":
            id_tarefa = int(input("ID da tarefa a concluir: "))
            concluir_tarefa(id_tarefa)
            print("Tarefa concluída!")
        
        elif escolha == "4":
            id_tarefa = int(input("ID da tarefa a excluir: "))
            excluir_tarefa(id_tarefa)
            print("Tarefa excluída!")
        
        elif escolha == "5":
            print("Saindo do Gerenciador de Tarefas.")
            break
        
        else:
            print("Opção inválida. Tente novamente!")

# Executar o programa
executar()