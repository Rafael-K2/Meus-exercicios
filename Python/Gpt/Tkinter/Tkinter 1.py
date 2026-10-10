import tkinter as tk
from tkinter import messagebox

def lg():
    janela_1.withdraw()
    login = usuario.get()

    if login == 'Rafael':
        janela_2 = tk.Toplevel()
        janela_2.title('Login bem sucedido')
        janela_2.geometry('400x200')
    else:
        messagebox.showwarning('Error', 'Login Falhou')

janela_1 = tk.Tk()
janela_1.title('Lista')
janela_1.geometry('400x200')

usuario = tk.Entry(janela_1)
usuario.pack(pady=10)

bt = tk.Button(janela_1,text='Login',command=lg)
bt.pack(pady=10)

janela_1.mainloop()