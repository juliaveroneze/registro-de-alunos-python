import sqlite3
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from PIL import Image, ImageTk

# --- Conexão com o banco ---
def conectar():
    conn = sqlite3.connect("alunos.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER,
            curso TEXT
        )
    ''')
    conn.commit()
    conn.close()

# --- Funções CRUD ---
def adicionar_aluno():
    nome = nome_entry.get()
    idade = idade_entry.get()
    curso = curso_entry.get()

    if not nome or not idade or not curso:
        messagebox.showwarning("Campos vazios", "Preencha todos os campos.")
        return

    try:
        idade = int(idade)
    except ValueError:
        messagebox.showerror("Erro", "Idade deve ser um número.")
        return

    conn = sqlite3.connect("alunos.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO alunos (nome, idade, curso) VALUES (?, ?, ?)", (nome, idade, curso))
    conn.commit()
    conn.close()

    listar_alunos()
    limpar_campos()
    messagebox.showinfo("Sucesso", "Aluno adicionado com sucesso!")

def listar_alunos():
    for row in tabela.get_children():
        tabela.delete(row)

    conn = sqlite3.connect("alunos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos")
    for aluno in cursor.fetchall():
        tabela.insert("", "end", values=aluno)
    conn.close()

def atualizar_aluno():
    selecionado = tabela.selection()
    if not selecionado:
        messagebox.showwarning("Selecionar", "Selecione um aluno para atualizar.")
        return

    item = tabela.item(selecionado)
    aluno_id = item["values"][0]

    nome = nome_entry.get()
    idade = idade_entry.get()
    curso = curso_entry.get()

    try:
        idade = int(idade)
    except ValueError:
        messagebox.showerror("Erro", "Idade deve ser um número.")
        return

    conn = sqlite3.connect("alunos.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE alunos SET nome=?, idade=?, curso=? WHERE id=?", (nome, idade, curso, aluno_id))
    conn.commit()
    conn.close()

    listar_alunos()
    limpar_campos()
    messagebox.showinfo("Atualizado", "Aluno atualizado com sucesso!")

def deletar_aluno():
    selecionado = tabela.selection()
    if not selecionado:
        messagebox.showwarning("Selecionar", "Selecione um aluno para deletar.")
        return

    item = tabela.item(selecionado)
    aluno_id = item["values"][0]

    confirmar = messagebox.askyesno("Confirmar", "Deseja realmente excluir o aluno?")
    if confirmar:
        conn = sqlite3.connect("alunos.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM alunos WHERE id=?", (aluno_id,))
        conn.commit()
        conn.close()

        listar_alunos()
        limpar_campos()
        messagebox.showinfo("Excluído", "Aluno removido com sucesso!")

def selecionar_item(event):
    selecionado = tabela.selection()
    if not selecionado:
        return
    item = tabela.item(selecionado)
    valores = item["values"]
    nome_entry.delete(0, ttk.END)
    nome_entry.insert(0, valores[1])
    idade_entry.delete(0, ttk.END)
    idade_entry.insert(0, valores[2])
    curso_entry.delete(0, ttk.END)
    curso_entry.insert(0, valores[3])

def limpar_campos():
    nome_entry.delete(0, ttk.END)
    idade_entry.delete(0, ttk.END)
    curso_entry.delete(0, ttk.END)

# --- Interface ---
conectar()
app = ttk.Window(themename="cosmo")
app.title("Sistema de Registro de Alunos")
app.geometry("720x480")
imagem = Image.open("registro-alunos-python/user.png")
imagem = imagem.resize((150, 150))  # ajuste conforme desejar
foto = ImageTk.PhotoImage(imagem)

# Adicionar ao topo da janela
label_imagem = ttk.Label(app, image=foto)
label_imagem.image = foto  # evitar coleta de lixo
label_imagem.pack(pady=5)
frame_form = ttk.Frame(app, padding=10)
frame_form.pack(pady=10)

ttk.Label(frame_form, text="Nome:").grid(row=0, column=0, sticky=W, padx=5, pady=5)
nome_entry = ttk.Entry(frame_form, width=30)
nome_entry.grid(row=0, column=1)

ttk.Label(frame_form, text="Idade:").grid(row=1, column=0, sticky=W, padx=5, pady=5)
idade_entry = ttk.Entry(frame_form, width=30)
idade_entry.grid(row=1, column=1)

ttk.Label(frame_form, text="Curso:").grid(row=2, column=0, sticky=W, padx=5, pady=5)
curso_entry = ttk.Entry(frame_form, width=30)
curso_entry.grid(row=2, column=1)

frame_botoes = ttk.Frame(app)
frame_botoes.pack(pady=10)

ttk.Button(frame_botoes, text="Adicionar", command=adicionar_aluno, bootstyle=SUCCESS).pack(side=LEFT, padx=5)
ttk.Button(frame_botoes, text="Atualizar", command=atualizar_aluno, bootstyle=WARNING).pack(side=LEFT, padx=5)
ttk.Button(frame_botoes, text="Excluir", command=deletar_aluno, bootstyle=DANGER).pack(side=LEFT, padx=5)
ttk.Button(frame_botoes, text="Limpar", command=limpar_campos, bootstyle=SECONDARY).pack(side=LEFT, padx=5)

tabela = ttk.Treeview(app, columns=("ID", "Nome", "Idade", "Curso"), show="headings", height=10, bootstyle="info")
tabela.heading("ID", text="ID")
tabela.heading("Nome", text="Nome")
tabela.heading("Idade", text="Idade")
tabela.heading("Curso", text="Curso")
tabela.column("ID", width=50)
tabela.pack(pady=10)
tabela.bind("<<TreeviewSelect>>", selecionar_item)

listar_alunos()
app.mainloop()
