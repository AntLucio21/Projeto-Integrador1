import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

from BD_Geral import adicionar_tarefa
from BD_Geral import listar_tarefas
from BD_Geral import concluir_tarefa
from BD_Geral import excluir_tarefa

# Função para atualizar a lista de tarefas na interface
def atualizar_lista():
    for item in tabela.get_children():
        tabela.delete(item)

    tarefas = listar_tarefas()
    for tarefa in tarefas:
        status = "Concluída" if tarefa[5] else "Pendente"
        tabela.insert("", "end", values=(tarefa[0], tarefa[1], tarefa[3], tarefa[4], status))

# Função para adicionar uma nova tarefa
def adicionar():
    titulo = entrada_titulo.get()
    descricao = entrada_descricao.get("1.0", tk.END).strip()
    data_vencimento = entrada_data.get()
    prioridade = prioridade_var.get()

    if not titulo or not data_vencimento or not prioridade:
        messagebox.showwarning("Erro", "Preencha todos os campos obrigatórios!")
        return

    try:
        datetime.strptime(data_vencimento, "%Y-%m-%d")
    except ValueError:
        messagebox.showwarning("Erro", "Data de vencimento inválida! Use o formato YYYY-MM-DD.")
        return

    adicionar_tarefa(titulo, descricao, data_vencimento, prioridade)
    messagebox.showinfo("Sucesso", "Tarefa adicionada!")
    atualizar_lista()

# Função para concluir uma tarefa
def concluir():
    item_selecionado = tabela.selection()
    if not item_selecionado:
        messagebox.showwarning("Erro", "Selecione uma tarefa para marcar como concluída!")
        return

    tarefa_id = tabela.item(item_selecionado)["values"][0]
    concluir_tarefa(tarefa_id)
    messagebox.showinfo("Sucesso", "Tarefa concluída!")
    atualizar_lista()

# Função para excluir uma tarefa
def excluir():
    item_selecionado = tabela.selection()
    if not item_selecionado:
        messagebox.showwarning("Erro", "Selecione uma tarefa para excluir!")
        return

    tarefa_id = tabela.item(item_selecionado)["values"][0]
    excluir_tarefa(tarefa_id)
    messagebox.showinfo("Sucesso", "Tarefa excluída!")
    atualizar_lista()

# Criando a interface gráfica
janela = tk.Tk()
janela.title("Gerenciador de Tarefas")

# Seção de formulário
tk.Label(janela, text="Título:").grid(row=0, column=0, sticky="w")
entrada_titulo = tk.Entry(janela, width=30)
entrada_titulo.grid(row=0, column=1, pady=5)

tk.Label(janela, text="Descrição:").grid(row=1, column=0, sticky="nw")
entrada_descricao = tk.Text(janela, width=30, height=5)
entrada_descricao.grid(row=1, column=1, pady=5)

tk.Label(janela, text="Data de Vencimento (YYYY-MM-DD):").grid(row=2, column=0, sticky="w")
entrada_data = tk.Entry(janela, width=30)
entrada_data.grid(row=2, column=1, pady=5)

tk.Label(janela, text="Prioridade:").grid(row=3, column=0, sticky="w")
prioridade_var = tk.StringVar(value="1")
tk.OptionMenu(janela, prioridade_var, "1 (Alta)", "2 (Média)", "3 (Baixa)").grid(row=3, column=1, pady=5)

tk.Button(janela, text="Adicionar Tarefa", command=adicionar, bg="green", fg="white").grid(row=4, column=1, pady=10)

# Tabela para exibir as tarefas
colunas = ("ID", "Título", "Vencimento", "Prioridade", "Status")
tabela = ttk.Treeview(janela, columns=colunas, show="headings", height=10)
for coluna in colunas:
    tabela.heading(coluna, text=coluna)
    tabela.column(coluna, width=150)

tabela.grid(row=5, column=0, columnspan=2, pady=10)

# Botões de ação
tk.Button(janela, text="Concluir Tarefa", command=concluir, bg="blue", fg="white").grid(row=6, column=0, pady=10)
tk.Button(janela, text="Excluir Tarefa", command=excluir, bg="red", fg="white").grid(row=6, column=1, pady=10)

# Atualizar lista ao iniciar
atualizar_lista()

# Iniciar o loop da interface
janela.mainloop()
