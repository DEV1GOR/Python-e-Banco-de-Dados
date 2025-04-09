# Importa funções do módulo database responsável por interagir com o banco de dados
from database import criar_tabela, adicionar_tarefa, listar_tarefas, atualizar_tarefa, deletar_tarefa

# Função para exibir o menu principal do sistema
# O lugar onde sonhos começam... e tarefas se acumulam
def menu():
    print("\n=== Gerenciamento de Tarefas ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Deletar tarefa")
    print("5. Sair")

def main():
    criar_tabela()   # Garante que a tabela de tarefas será criada ao iniciar o programa (caso não exista)

     # Loop infinito que mantém o menu ativo até o usuário decidir sair
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            descricao = input("Digite a descrição da tarefa: ")
            adicionar_tarefa(descricao)
        
        elif opcao == "2":
            tarefas = listar_tarefas()
            if tarefas:
                print("\nTarefas:")
                for tarefa in tarefas:
                    status = "Concluída" if tarefa[2] == 1 else "Pendente"
                    print(f"ID: {tarefa[0]} | Descrição: {tarefa[1]} | Status: {status}")
            else:
                print("Nenhuma tarefa cadastrada.")
        
        elif opcao == "3":
            id_tarefa = int(input("Digite o ID da tarefa a marcar como concluída: "))
            atualizar_tarefa(id_tarefa, 1)
        
        elif opcao == "4":
            id_tarefa = int(input("Digite o ID da tarefa a deletar: "))
            deletar_tarefa(id_tarefa)
        
        elif opcao == "5":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida!")

# O ritual sagrado de execução direta
if __name__ == "__main__":
    main()