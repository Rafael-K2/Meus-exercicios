import tkinter as tk
from tkinter import messagebox

def adicionar():
    with open('Lista.txt','a',encoding='utf-8') as arquivo:
        arquivo.write(lista.get() + '\n')
        arquivo.write('-'*20 + '\n')
        lista.delete(0, tk.END)


def janela2():

    def carregar_lista():
        listas.delete(0, tk.END)

        with open('Lista.txt','r',encoding='utf-8') as arquivo:
            for l in arquivo:
                txt = l.strip()
                listas.insert(tk.END,txt)
    def remover():
        selecionado = listas.curselection()
        if selecionado:
            with open('Lista.txt','r',encoding='utf-8') as arquivo:
                linhas = arquivo.readlines()
            linhas.pop(selecionado[0])
            with open('Lista.txt','w',encoding='utf-8') as arquivo:
                arquivo.writelines(linhas)
            listas.delete(selecionado[0])


    j2 = tk.Toplevel()
    j2.title('Lista')
    j2.geometry('400x200')

    listas = tk.Listbox(j2)
    listas.pack()
    bt3 = tk.Button(j2,text='Carregar',command=carregar_lista)
    bt3.pack()

    bt_remover = tk.Button(j2,text='Remover selecionado', command=remover)
    bt_remover.pack()


j1 = tk.Tk()
j1.title('Login')
j1.geometry('300x150')

addlist = tk.Label(j1, text='Adicionar tarefa a lista:')
addlist.pack()

lista = tk.Entry(j1)
lista.pack()

adlist = tk.Button(j1,text='Adicionar', command=adicionar)
adlist.pack()

vlista = tk.Button(j1, text='Ver lista', command=janela2,)
vlista.pack()

j1.mainloop()