import tkinter as tk
from tkinter import messagebox

COR_MENU = "#014D0D"
COR_CONTEUDO = "#145F20"
COR_BOTOES = "#00C120"

def troca_de_janelas(frame):
    for f in frames:
        f.pack_forget()

    frame.pack(fill='both', expand=True)

def cadastrar_o_aluno():
    nome = nome_do_aluno.get().capitalize()
    idade = idade_do_aluno.get().capitalize()
    with open('Alunos.txt','a',encoding='utf-8') as arquivo:
        arquivo.write('Nome:'+ nome + '\n')
        arquivo.write('Idade:' + idade + '\n')
        arquivo.write('-' *200 + '\n')

def atualizar_lista_de_alunos():
    lista_dos_alunos.delete(0, tk.END)
    with open('Alunos.txt','r',encoding='utf8') as arquivo:
        for l in arquivo:
            texto = l.strip()
            lista_dos_alunos.insert(tk.END, texto)

def deletar_aluno_selecionado():
    selecionado = lista_dos_alunos.curselection()
    if selecionado:
        with open('Lista.txt','r',encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
        linhas.pop(selecionado[0])
        with open('Lista.txt','w',encoding='utf-8') as arquivo:
            arquivo.writelines(linhas)
        lista_dos_alunos.delete(selecionado[0])

#region Janela principal
janela = tk.Tk()
janela.title('Infostudant')
janela.state('zoomed')
#endregion
#region Frames principais
opcoes = tk.Frame(
    janela,
    height=300,
    width=300,
    bg=COR_MENU
)
opcoes.pack(side='left', fill='y')

conteudo = tk.Frame(
    janela,
    height=100,
    width=100,
    bg=COR_CONTEUDO
)
conteudo.pack(side='left', fill='both', expand=True)
pg_inicial = tk.Frame(
    conteudo,
    height=100,
    width=100,
    bg=COR_CONTEUDO
)
pg_inicial.pack(side='left', fill='both', expand=True)
#endregion

#region Frames secundarios
cadastrar_aluno = tk.Frame(
    conteudo,
    height=100,
    width=100,
    bg=COR_CONTEUDO
)

ver_alunos_cadastrados = tk.Frame(
    conteudo,
    height=100,
    width=100,
    bg=COR_CONTEUDO
)

frames = [
    pg_inicial,
    cadastrar_aluno,
    ver_alunos_cadastrados
]
#endregion
tk.Label(
    pg_inicial,
    text='Página inicial',
    font=('Arial', 35),
    bg=COR_CONTEUDO
).grid(
    row=0,
    column=1,
)

tk.Label(
    pg_inicial,
    text='''Este é um app de teste
    então provavelmente ta muito mal feito''',
    font=('Arial',50),
    bg=COR_CONTEUDO
).grid(
    row=2,
    column=1
)

tk.Label(
    opcoes,
    bg=COR_MENU,
    width=20,
    text='Menu lateral',
    font=('Arial', 20),
    pady=20
).pack()
#region Página para ver os alunos cadastrados
tk.Button(
    opcoes,
    bg=COR_BOTOES,
    width=25,
    height=2,
    text='Ver alunos cadastrados',
    font=('Arial', 14),
    command=lambda: troca_de_janelas(ver_alunos_cadastrados),
).pack()
tk.Label(
    ver_alunos_cadastrados,
    text=('Alunos cadastrados'),
    font=('Arial',50),
    bg=COR_CONTEUDO
).pack()
lista_dos_alunos = tk.Listbox(
    ver_alunos_cadastrados,
    width=50,
    height=25,
    justify='center',
    font=('Arial', 15)
)
lista_dos_alunos.pack(pady=40)
tk.Button(
    ver_alunos_cadastrados,
    text='Atualizar lista dos alunos',
    bg=COR_BOTOES,
    font=('Arial',20),
    command=atualizar_lista_de_alunos
).pack()
tk.Button(
    ver_alunos_cadastrados,
    text='Deletar seleção',
    bg=COR_BOTOES,
    font=('Arial',20),
    command=deletar_aluno_selecionado
).pack()
#endregion
#region Página para cadastrar os alunos
tk.Button(
    opcoes,
    bg=COR_BOTOES,
    width=25,
    height=2,
    text='Cadastrar aluno',
    font=('Arial', 14),
    command=lambda: troca_de_janelas(cadastrar_aluno),
).pack()

formulario = tk.Frame(
    cadastrar_aluno,
    height=1100,
    width=700,
    bg=COR_BOTOES
)
formulario.place(y=0, x=400)
tk.Label(
    formulario,
    text='Informações do aluno',
    font=('Arial',30),
    bg=COR_BOTOES
).grid(
    row=0,
    column=1
)

tk.Label(
    formulario,
    text='Nome do aluno',
    font=('Arial',25),
    bg=COR_BOTOES
).grid(
    row=1,
    column=0
)

nome_do_aluno = tk.Entry(
    formulario,
    
)
nome_do_aluno.grid(
    row=1,
    column=1,
    
)
tk.Label(
    formulario,
    text='Idade do aluno',
    font=('Arial',25),
    bg=COR_BOTOES
).grid(
    row=2,
    column=0
)

idade_do_aluno = tk.Entry(
    formulario,
)
idade_do_aluno.grid(
    row=2,
    column=1,
)

tk.Button(
    formulario,
    bg=COR_BOTOES,
    width=15,
    height=2,
    text='Cadastrar aluno',
    font=('Arial', 14),
    command=cadastrar_o_aluno
).grid(
    row=3,
    column=1,
)
#endregion
janela.mainloop()