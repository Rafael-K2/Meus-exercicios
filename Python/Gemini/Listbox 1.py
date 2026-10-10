import tkinter as tk
from tkinter import messagebox
def adicionar():
    with open('Listinha.txt','a',encoding='utf-8') as arquivo:
        arquivo.write(add_lista.get() + '\n')


def atualizar ():
    
    with open('Listinha.txt', 'r', encoding='utf-8') as arquivo:
        for l  in arquivo:
            listinha.insert(tk.END,l.strip())





def limpar():
    add_lista.delete(0,tk.END)





j1 = tk.Tk()
j1.title('Olá')
j1.geometry('200x400')

listinha = tk.Listbox(j1)
listinha.pack()

adl = tk.Label(j1,text='Adicionar a lista')
adl.pack()

add_lista = tk.Entry(j1)
add_lista.pack()

bt_atualizar = tk.Button(j1,text='Atualizar lista',command=atualizar)
bt_atualizar.pack()

bt_adicionar = tk.Button(j1,text='Adicionar a lista', command=adicionar)
bt_adicionar.pack()

bt_apagar = tk.Button(j1,text='Apagar item selecionado')
bt_apagar.pack()






j1.mainloop()