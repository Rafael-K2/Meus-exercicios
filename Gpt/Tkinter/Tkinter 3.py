import tkinter as tk
from tkinter import messagebox
def limpar():
    n.delete(0,tk.END)
    i.delete(0,tk.END)
    c.delete(0,tk.END)
def cadastro():

    with open('Cadastrados.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'Nome:{n.get()}\n')
        arquivo.write(f'Idade:{i.get()}\n')
        arquivo.write(f'Cidade:{c.get()}\n')
        arquivo.write('-' * 20 + '\n')

j1 = tk.Tk()
j1.title('Cadastro')
j1.geometry('400x200')

nome = tk.Label(j1, text='Nome:').pack()
n = tk.Entry(j1)
n.pack()

idade = tk.Label(j1,text='idade').pack()
i = tk.Entry(j1)
i.pack()

cidade = tk.Label(j1, text='cidade').pack()
c = tk.Entry(j1)
c.pack()

cadastrar = tk.Button(j1,text='cadastrar',command=cadastro).pack()
limpa = tk.Button(j1,text='limpar',command=limpar).pack()

j1.mainloop()