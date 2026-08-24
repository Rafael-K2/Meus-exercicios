import tkinter as tk
from tkinter import messagebox
def limpar():
    n.delete(0,tk.END)
    i.delete(0,tk.END)
    c.delete(0,tk.END)
def cadastro():
    messagebox.showinfo('Finalizado','Cadastro feito com sucesso!')
    with open('Cadastrados.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'Nome:{n.get()}\n')
        arquivo.write(f'Idade:{i.get()}\n')
        arquivo.write(f'Cidade:{c.get()}\n')
        arquivo.write('-' * 20 + '\n')
def ver_cadastro():
    j1.withdraw()
    j2 = tk.Toplevel()
    j2.title('Cadastros')
    j2.geometry('400x200')
    with open('Cadastrados.txt','r',encoding='utf-8') as arquivo:
        cadastrados = tk.Label(j2,text=arquivo.read()).pack()
'''Usar Text ao envez de Label da próxima vez
texto = tk.Text(j2)
texto.pack(fill='both', expand=True)

texto.insert('1.0', arquivo.read())
texto.config(state='disabled')'''



j1 = tk.Tk()
j1.title('Cadastro')
j1.geometry('400x200')

nome = tk.Label(j1,
                 text='Nome:')
nome.pack()
n = tk.Entry(j1)
n.pack()

idade = tk.Label(j1,
                text='idade')
idade.pack()
i = tk.Entry(j1)
i.pack()

cidade = tk.Label(j1,
                 text='cidade')
cidade.pack()
c = tk.Entry(j1)
c.pack()

cadastrar = tk.Button(j1,
                      text='cadastrar',
                      command=cadastro)
cadastrar.pack()
limpa = tk.Button(j1,
                  text='limpar',
                  command=limpar)
limpa.pack()

ver_cad = tk.Button(j1,
                    text='Ver cadastrados',
                    command=ver_cadastro)
ver_cad.pack()

j1.mainloop()