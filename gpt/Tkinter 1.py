import tkinter as tk

janela_1 = tk.Tk()
janela_1.title('Lista')
janela_1.geometry('300x200')

bt = tk.Button(janela_1,text='Adicionar')
bt.pack(pady=10)

janela_1.mainloop()