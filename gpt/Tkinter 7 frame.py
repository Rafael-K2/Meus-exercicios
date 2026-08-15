import tkinter as tk

j1 = tk.Tk()
j1.geometry('300x600')
j1.title('IO')

telinha_1 =  tk.Frame(j1,
                      bg='lightgrey',
                      width=100,
                      height=200
                      )
telinha_1.place(x=0,y=0)

menu = tk.Label(telinha_1,
                text='Menu',
                width=10,
                height=10,
                bg='lightgray'
                )
menu.place(x=0,y=-65)

telinha_2 = tk.Frame(j1,
                     bg='lightblue',
                     width=200,
                     height=200
                     )
telinha_2.place(x=100,y=0)

conteudo = tk.Label(telinha_2,
                text='Conteudo',
                width=10,
                height=10,
                bg='lightblue'
                )
conteudo.place(x=0,y=-65)

j1.mainloop()