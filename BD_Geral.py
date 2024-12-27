import sqlite3

# Inicializa o banco de dados
def inicializar_banco():
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            data_vencimento TEXT,
            prioridade INTEGER,
            concluida INTEGER DEFAULT 0
        )
    """)
    conexao.commit()
    conexao.close()

# Função para adicionar uma tarefa
def adicionar_tarefa(titulo, descricao, data_vencimento, prioridade):
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO tarefas (titulo, descricao, data_vencimento, prioridade)
        VALUES (?, ?, ?, ?)
    """, (titulo, descricao, data_vencimento, prioridade))
    conexao.commit()
    conexao.close()

# Função para listar todas as tarefas
def listar_tarefas():
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    conexao.close()
    return tarefas

# Função para marcar uma tarefa como concluída
def concluir_tarefa(id_tarefa):
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()
    cursor.execute("UPDATE tarefas SET concluida = 1 WHERE id = ?", (id_tarefa,))
    conexao.commit()
    conexao.close()

# Função para excluir uma tarefa
def excluir_tarefa(id_tarefa):
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))
    conexao.commit()
    conexao.close()

# Inicializa o banco de dados ao iniciar o programa
inicializar_banco()