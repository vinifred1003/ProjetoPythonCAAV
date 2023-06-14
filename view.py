
from tkinter import *


def donothing():
    pass

class View():
    def __init__(self):
      self.root = Tk()

      self.janela()
      self.menu()
      self.texto()
    
      self.root.mainloop()
    
    def janela(self):
      self.root.title("Projetinho")
      self.root.attributes('-fullscreen', True)
      self.root.configure(background="gray")
      self.root.resizable(True, True)

    def texto(self):  
      self.Frame_1 = Frame(self.root,bd=4, bg='gray', highlightthickness=3 ,highlightbackground='#3F48CC')
      self.Frame_1.place(relx=0.2, rely=0, relwidth=0.8, relheight=0.2)
      
      self.Frame_2 = Frame(self.root,bd=4, bg='white')
      self.Frame_2.place(relx=0.2, rely=0.2, relwidth=0.8, relheight=0.8)
      
## auygsuygdyug

    def menu(self):
      botao=Button(self.root, text="Relatório dos Alugueis",fg="white", bg="#7092BE" ,height=6,width=40)
      botao.grid(column=0, row=0)

      botao=Button(self.root, text="Exibição dos Alugueis", fg="white", bg="#7092BE", highlightthickness=3 ,highlightbackground='#3F48CC' ,height=6,width=40)
      botao.grid(column=0, row=1)
      
      botao=Button(self.root, text="Cadastro dos Carros" ,fg="white", bg="#7092BE", height=6,width=40)
      botao.grid(column=0, row=2)

      botao=Button(self.root, text="Cadastro dos Clientes", fg="white", bg="#7092BE", height=6,width=40)
      botao.grid(column=0, row=3)

      botao=Button(self.root, text="Exibição dos Alugueis", fg="white", bg="#7092BE", height=6,width=40)
      botao.grid(column=0, row=4)
      
      botao=Button(self.root, text="Marketing", fg="white", bg="#7092BE", height=6,width=40)
      botao.grid(column=0, row=5)
      
      botao=Button(self.root, text="Configurações", fg="white", bg="#7092BE", height=6,width=40)
      botao.grid(column=0, row=6)

      botao=Button(self.root, text="Ajuda", fg="white", bg="#7092BE", height=6,width=40)
      botao.grid(column=0, row=7)

      botao=Button(self.root, text="Sair", fg="white", bg="#7092BE", height=6,width=40)
      botao.grid(column=0, row=8)

Janela = View()
