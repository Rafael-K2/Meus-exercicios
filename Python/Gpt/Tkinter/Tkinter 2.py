import tkinter as tk
from tkinter import messagebox

tentativa_login = 3

def janela_2():
    global tentativa_login
    login = usuario.get()
    password = senha.get()

    if login == 'Rafael' and password == '1808':
        j1.withdraw()
        j2 = tk.Toplevel()
        j2.title('Painel')
        j2.geometry('400x200')

        msg = tk.Label(j2,text=f'Bem vindo de volta {login}!')
        msg.pack()
    else:
        tentativa_login -= 1
        messagebox.showerror('Error',f'login invalido, você tem mais {tentativa_login} tentativas')
    if tentativa_login == 0:
        messagebox.showerror('Ops','Você excedeu o limite de 3 tentativas')
        entrar.config(state='disabled')

def limpar():
    usuario.delete(0,tk.END)
    senha.delete(0,tk.END)

j1 = tk.Tk()
j1.title('Login')
j1.geometry('400x200')

lg = tk.Label(j1, text='Usuario').pack()
usuario = tk.Entry(j1)
usuario.pack()

ps = tk.Label(j1, text='Senha').pack()
senha = tk.Entry(j1, show='*')
senha.pack()

entrar = tk.Button(j1, text='Fazer login', command=janela_2)
entrar.pack()

apagar = tk.Button(j1,text='Limpar',command=limpar)
apagar.pack()

j1.mainloop()