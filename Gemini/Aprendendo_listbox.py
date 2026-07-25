import tkinter as tk
def delet():
    lista.delete(lista.curselection())



def add():
    conteudo = addlist.get()
    lista.insert(tk.END,conteudo)
    with open('l.txt','a',encoding='utf-8') as arquivo:
        arquivo.write(f'{conteudo}\n')
        arquivo.write('-' *20+ '\n')

j1 = tk.Tk()
j1.title('Listbox')
j1.geometry('600x300')

lista = tk.Listbox(j1)
lista.pack()

addlist = tk.Entry(j1,)
addlist.pack()


bt = tk.Button(j1,text='Adicionar', command=add).pack()
btd = tk.Button(j1, text='Retira da lista', command=delet).pack()

j1.mainloop()