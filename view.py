
from tkinter import *


def donothing():
    pass
root = Tk()
class View():
    def __init__(self):
      
      self.root = root
      self.janela()
      self.menu()
      self.Frames()
      self.Filtros()
      root.mainloop()
    
    def janela(self):
      self.root.title("Projetinho")
      self.root.attributes('-fullscreen', True)
      self.root.configure(background="gray")
      self.root.resizable(True, True)

    def Frames(self):  
      self.FrameFiltros = Frame(self.root, bd=4, bg='gray', highlightthickness=3, highlightbackground='#3F48CC')
      self.FrameFiltros.place(relx=0.2, rely=0, relwidth=0.8, relheight=0.2)
      
      self.FrameRegistros = Frame(self.root, bd=4, bg='white')
      self.FrameRegistros.place(relx=0.2, rely=0.2, relwidth=0.8, relheight=0.8)
      
    
    def Filtros(self):
      self.FrameFiltros = Frame(self.root, bd=4, bg='gray', highlightthickness=3, highlightbackground='#3F48CC')
      self.FrameFiltros.place(relx=0.2, rely=0, relwidth=0.8, relheight=0.2)

      self.lbId = Label(self.FrameFiltros, text="Código")
      self.lbId.place(relx=0.1,rely=0.1)

    def menu(self):
   
      self.FrameBotoes = Frame(self.root, bd=4, bg='#3F48CC',height=1000,width=300)
      self.FrameBotoes.grid(column=0, row=0)

      self.botaoRA=Button(self.FrameBotoes, text="Relatório dos Alugueis",fg="white", bg="#7092BE" ,height=5,width=40)
      self.botaoRA.grid(column=0, row=0)

      self.botaoEA=Button(self.FrameBotoes, text="Exibição dos Alugueis", fg="white", bg="#7092BE", highlightthickness=3 ,highlightbackground='#3F48CC' ,height=5,width=40)
      self.botaoEA.grid(column=0, row=1)
      
      self.botaoCCar=Button(self.FrameBotoes, text="Cadastro dos Carros" ,fg="white", bg="#7092BE", height=5,width=40)
      self.botaoCCar.grid(column=0, row=2)

      self.botaoCC=Button(self.FrameBotoes, text="Cadastro dos Clientes", fg="white", bg="#7092BE", height=5,width=40)
      self.botaoCC.grid(column=0, row=3)

      self.botaoEC=Button(self.FrameBotoes, text="Exibição dos Carros", fg="white", bg="#7092BE", height=5,width=40)
      self.botaoEC.grid(column=0, row=4)
      
      self.botaoM=Button(self.FrameBotoes, text="Marketing", fg="white", bg="#7092BE", height=5,width=40)
      self.botaoM.grid(column=0, row=5)
      
      self.botaoC=Button(self.FrameBotoes, text="Configurações", fg="white", bg="#7092BE", height=5,width=40)
      self.botaoC.grid(column=0, row=6)

      self.botaoA=Button(self.FrameBotoes, text="Ajuda", fg="white", bg="#7092BE", height=5,width=40)
      self.botaoA.grid(column=0, row=7)

      self.botaoS=Button(self.FrameBotoes, text="Sair", fg="white", bg="#7092BE", height=4,width=40)
      self.botaoS.grid(column=0, row=8)

Janela = View()
