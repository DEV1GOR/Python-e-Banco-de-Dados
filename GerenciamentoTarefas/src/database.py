import sqlite3 # Trazendo o SQLite pra brincadeira — simples, leve e sem drama

# Função básica pra abrir uma conexão com o banco
def conectar_banco():
    conexao = sqlite3.connect('tarefas.db')  # Cria (ou abre) o banco de dados
    cursor = conexao.cursor()
    return conexao, cursor

def criar_tabela():
    conexao, cursor = conectar_banco()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            concluida INTEGER DEFAULT 0
        )
    """)
    conexao.commit()
    conexao.close()

# Funções CRUD: Cadastrar, Ler, Atualizar e Deletar 
def adicionar_tarefa(descricao):
    conexao, cursor = conectar_banco()
    cursor.execute("INSERT INTO tarefas (descricao) VALUES (?)", (descricao,))
    conexao.commit()
    conexao.close()
    print(f"Tarefa '{descricao}' adicionada com sucesso!")

def listar_tarefas():
    conexao, cursor = conectar_banco()
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    conexao.close()
    return tarefas

def atualizar_tarefa(id_tarefa, concluida):
    conexao, cursor = conectar_banco()
    cursor.execute("UPDATE tarefas SET concluida = ? WHERE id = ?", (concluida, id_tarefa))
    conexao.commit()
    conexao.close()
    print(f"Tarefa {id_tarefa} atualizada!")

def deletar_tarefa(id_tarefa):
    conexao, cursor = conectar_banco()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))
    conexao.commit()
    conexao.close()
    print(f"Tarefa {id_tarefa} deletada!")