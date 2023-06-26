
from tkinter import *
from tkinter import ttk
from viewCadastroCarro import ViewCadastroCarro
def donothing():
    pass
root = Tk()
class View():
    def __init__(self):
      self.root = root
      self.janela()
      self.menu()
      self.Filtros()
      self.Registros()
      root.mainloop()
    
    def janela(self):
      self.root.title("Projetinho")
      self.root.attributes('-fullscreen', True)
      self.root.configure(background="gray")
      self.root.resizable(True, True)
     
    
    def Filtros(self):
      self.FrameFiltros = Frame(self.root, bd=4, bg='gray', highlightthickness=3, highlightbackground='#3F48CC')
      self.FrameFiltros.place(relx=0.2, rely=0, relwidth=0.8, relheight=0.2)

      self.lbId = Label(self.FrameFiltros, text="Código", fg="white",bg="gray")
      self.lbId.place(relx=0.02,rely=0.28)

      self.EntryId = Entry(self.FrameFiltros, bd=2, bg="white")
      self.EntryId.place(relx=0.02,rely=0.45)
   
      self.lbNome = Label(self.FrameFiltros, text="Nome", fg="white",bg="gray")
      self.lbNome.place(relx=0.2,rely=0.28)

      self.EntryNome = Entry(self.FrameFiltros, bd=2, bg="white")
      self.EntryNome.place(relx=0.2,rely=0.45)

      self.lbPlaca = Label(self.FrameFiltros, text="Placa", fg="white",bg="gray")
      self.lbPlaca.place(relx=0.4,rely=0.28)

      self.EntryPlaca = Entry(self.FrameFiltros, bd=2, bg="white")
      self.EntryPlaca.place(relx=0.4,rely=0.45)
      
      self.lbCNH = Label(self.FrameFiltros, text="CNH", fg="white",bg="gray")
      self.lbCNH.place(relx=0.6,rely=0.28)

      self.EntryCNH = Entry(self.FrameFiltros, bd=2, bg="white")
      self.EntryCNH.place(relx=0.6,rely=0.45)

    def Quit(self):
      self.root.destroy()  
    def menu(self):
   
      self.FrameBotoes = Frame(self.root, bd=4, bg='#3F48CC',height=1000,width=300)
      self.FrameBotoes.grid(column=0, row=0)

      self.botaoRA=Button(self.FrameBotoes, text="Relatório dos Alugueis",fg="white", bg="#7092BE" ,height=5,width=40)
      self.botaoRA.grid(column=0, row=0)

      self.botaoEA=Button(self.FrameBotoes, text="Exibição dos Alugueis", fg="white", bg="#7092BE", highlightthickness=3 ,highlightbackground='#3F48CC' ,height=5,width=40)
      self.botaoEA.grid(column=0, row=1)
      
      self.botaoCCar=Button(self.FrameBotoes, text="Cadastro dos Carros" ,fg="white", bg="#7092BE", height=5,width=40, command=self.abrir_janela_cadastro_carro)
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

      self.botaoS=Button(self.FrameBotoes, text="Sair", fg="white", bg="#7092BE", height=4,width=40,command=self.Quit)
      self.botaoS.grid(column=0, row=8)

    def Registros(self):
      self.FrameRegistros = Frame(self.root, bd=4, bg='white')
      self.FrameRegistros.place(relx=0.2, rely=0.2, relwidth=0.8, relheight=0.8)

    def abrir_janela_cadastro_carro(self):
      cadastro_carro = ViewCadastroCarro()
      cadastro_carro.openNewWindow()
    
      
      self.listR = ttk.Treeview(self.FrameRegistros, height=4, column=("col1, col2, col3, col4"))
      self.listR.heading("#0", text="")
      self.listR.heading("#1", text="Código")
      self.listR.heading("#2", text="Nome")
      self.listR.heading("#3", text="Placa")
      self.listR.heading("#4", text="CNH")

      self.listR.column("#0", width=1)
      self.listR.column("#1", width=50)
      self.listR.column("#2", width=200)
      self.listR.column("#3", width=125)
      self.listR.column("#4", width=125)

      self.listR.place(relx=0, rely=0, relwidth=1, relheight=1)
      
      self.scrollListR = Scrollbar(self.FrameRegistros, orient_='vertical')
      self.listR.configure(yscroll=self.scrollListR.set)
      self.scrollListR.place(relx=0.98, rely=0.05, relwidth=0.015, relheight=0.9)

Janela = View()
