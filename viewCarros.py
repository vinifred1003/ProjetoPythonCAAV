
from tkinter import *
from tkinter import ttk
from viewCadastroCarro import ViewCadastroCarro
from controller import Controller
from viewCadastroCliente import ViewCadastroCliente
class ViewCarros():
    def __init__(self, root1):
      self.root1 = root1
      self.run()
      self.menu()
      self.Filtros()
      self.Registros()
      self.controller = Controller(None, None, None, None)
      self.framesCarros()
      dados = self.controller.ler_dados()
      for item in dados:
        self.listR.insert("", "end", values=item)
      

    def run(self):
      self.root1.title("Carros Cadastrados")
      self.root1.attributes('-fullscreen', True)
      self.root1.configure(background="gray")
      self.root1.resizable(True, True)
    

    def framesCarros(self):
      self.FramePrincipal = Frame(self.root1, bd=4, bg='white')
      self.FramePrincipal.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
      
      self.Filtros()
      self.Registros()

    def Filtros(self):
      self.FrameFiltros = Frame(self.root1, bd=4, bg='gray', highlightthickness=3, highlightbackground='#3F48CC')
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
      self.root1.destroy()  
    
    def esconder(self):
      self.withdraw() 
    
    def chamarCadastroCliente(self):  
      self.root2 = Toplevel()
      self.root2.withdraw() 
      ViewCadastroCliente(self.root2)

    def chamarCadastroCarro(self):  
      self.root3 = Toplevel()
      self.root3.withdraw()
      ViewCadastroCarro(self.root3)
        
    def menu(self):
      self.FrameBotoes = Frame(self.root1, bd=4, bg='#3F48CC',height=1000,width=300)
      self.FrameBotoes.grid(column=0, row=0)

      self.botaoRA=Button(self.FrameBotoes, text="Relatório dos Alugueis",fg="white", bg="#7092BE" ,height=5,width=40)
      self.botaoRA.grid(column=0, row=0)

      self.botaoEA=Button(self.FrameBotoes, text="Exibição dos Alugueis", fg="white", bg="#7092BE", highlightthickness=3 ,highlightbackground='#3F48CC' ,height=5,width=40)

      self.botaoCCar=Button(self.FrameBotoes, text="Cadastro dos Carros" ,fg="white", bg="#7092BE", height=5,width=40,command=self.chamarCadastroCarro)
      self.botaoCCar.grid(column=0, row=2)

      self.botaoCC= Button(self.FrameBotoes, text="Cadastro dos Clientes", fg="white", bg="#7092BE", height=5,width=40,command=self.chamarCadastroCliente)
      self.botaoCC.grid(column=0, row=3)

      self.botaoEC=Button(self.FrameBotoes, text="Exibição dos Carros", fg="white", bg="#7092BE", height=5,width=40)
      self.botaoEC.grid(column=0, row=4)
            
      self.botaoC=Button(self.FrameBotoes, text="Exibição dos Clientes", fg="white", bg="#7092BE", height=5,width=40)
      self.botaoC.grid(column=0, row=5)

      self.botaoM=Button(self.FrameBotoes, text="Marketing", fg="white", bg="#7092BE", height=5,width=40)
      self.botaoM.grid(column=0, row=6)

      self.botaoA=Button(self.FrameBotoes, text="Ajuda", fg="white", bg="#7092BE", height=5,width=40)
      self.botaoA.grid(column=0, row=7)

      self.botaoS=Button(self.FrameBotoes, text="Sair", fg="white", bg="#7092BE", height=4,width=40,command=self.Quit)
      self.botaoS.grid(column=0, row=8)

    
    def Registros(self):
      self.FrameRegistros = Frame(self.root1, bd=4, bg='white')
      self.FrameRegistros.place(relx=0.2, rely=0.2, relwidth=0.8, relheight=0.8)
    
      
      self.listR = ttk.Treeview(self.FrameRegistros, height=4, column=("col1, col2, col3, col4, col5"))
      self.listR.heading("#0", text="")
      self.listR.heading("#1", text="Código")
      self.listR.heading("#2", text="Modelo")
      self.listR.heading("#3", text="Placa")
      self.listR.heading("#4", text="Marca")
      self.listR.heading("#5", text="Ano")

      self.listR.column("#0", width=1)
      self.listR.column("#1", width=50)
      self.listR.column("#2", width=200)
      self.listR.column("#3", width=125)
      self.listR.column("#4", width=125)
      self.listR.column("#5", width=100)
      
      self.listR.place(relx=0, rely=0, relwidth=1, relheight=1)
      
      self.scrollListR = Scrollbar(self.FrameRegistros, orient_='vertical')
      self.listR.configure(yscroll=self.scrollListR.set)
      self.scrollListR.place(relx=0.98, rely=0.05, relwidth=0.015, relheight=0.9)

