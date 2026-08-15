import tkinter as tk

j1 = tk.Tk()
j1.geometry('450x600')
j1.title('OI')

telinha_1 = tk.Frame(j1,
                    bg='lightblue',
                    width=130,
                    height=150
                    )

telinha_1.place(x=0,y=0)

txt_1 = tk.Label(telinha_1,
                text='Menu',
                bg='lightblue'
                )

txt_1.place(x=0,y=0)

telinha_2 = tk.Frame(j1,
                     bg='lightgreen',
                     width=130,
                     height=150
                     )

telinha_2.place(x=150,y=0)

txt_2= tk.Label(telinha_2,
                text='Conteudo',
                bg='lightgreen'
                )

txt_2.place(x=0,y=0)


j1.mainloop()
