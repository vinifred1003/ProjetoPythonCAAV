
from tkinter import *
from tkinter import ttk
from viewCadastroCarro import ViewCadastroCarro
from controller import Controller
from viewCadastroCliente import ViewCadastroCliente
class ViewClientes():
    def __init__(self, root1):
      self.root1 = root1
      self.Filtros_Clientes()
      self.Registros_Clientes()
      self.controller = Controller(None, None, None, None)
      self.framesClientes()
      self.atualizar()
    
    def framesClientes(self):
      self.FramePrincipal = Frame(self.root1, bd=4, bg='white')
      self.FramePrincipal.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
      
      self.Filtros_Clientes()
      self.Registros_Clientes()

    def limpa_campos (self):
      self.EntryId.delete(0 , END)
      self.EntryNome.delete(0 , END)
      self.EntryCNH.delete(0 , END)
      self.EntryCPF.delete(0 , END)   

    def Filtros_Clientes(self):
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

      self.lbCNH = Label(self.FrameFiltros, text="CNH", fg="white",bg="gray")
      self.lbCNH.place(relx=0.4,rely=0.28)

      self.EntryCNH = Entry(self.FrameFiltros, bd=2, bg="white")
      self.EntryCNH.place(relx=0.4,rely=0.45)
      
      self.lbCPF = Label(self.FrameFiltros, text="CPF", fg="white",bg="gray")
      self.lbCPF.place(relx=0.6,rely=0.28)

      self.EntryCPF = Entry(self.FrameFiltros, bd=2, bg="white")
      self.EntryCPF.place(relx=0.6,rely=0.45)
      
      self.BotaoDel =Button(self.FrameFiltros, text="Apagar", command=self.excluir_por_CPF )
      self.BotaoDel.place(relx=0.9, rely=0.45) 
      
      self.BotaoBuscar =Button(self.FrameFiltros, text="Atualizar Tabela", command= self.excluir_por_CPF)
      self.BotaoBuscar.place(relx=0.8, rely=0.45) 

    def Quit(self):
      self.root1.destroy()  

    def esconder(self):
      self.withdraw() 
    
    def atualizar(self):
      self.listC.delete_cliente(*self.listC.get_children())
      dados = self.controller.ler_dados()
      for item in dados:
        self.listC.insert("", "end", values=item)

    def excluir_por_CPF(self):
        CPF = self.EntryPlaca.get()
        self.controller.excluir_dados(CPF)
        self.limpa_campos()
        self.atualizar()

    def DuploClique(self, event):
      self.limpa_campos()
      self.listC.selection()
     
      for n in self.listC.selection():
        col1, col2, col3, col4, col5 = self.listC.item(n,'values')
        self.EntryId.insert(END, col1)
        self.EntryModelo.insert(END, col2)
        self.EntryMarca.insert(END, col3)
        self.EntryPlaca.insert(END, col4)

    def Registros_Clientes(self):
      self.FrameRegistros = Frame(self.root1, bd=4, bg='white')
      self.FrameRegistros.place(relx=0.2, rely=0.2, relwidth=0.8, relheight=0.8)
    
      
      self.listC = ttk.Treeview(self.FrameRegistros, height=4, column=("col1, col2, col3, col4, col5"))
      self.listC.heading("#0", text="")
      self.listC.heading("#1", text="Código")
      self.listC.heading("#2", text="Nome")
      self.listC.heading("#3", text="CNH")
      self.listC.heading("#4", text="CPF")
      self.listC.heading("#5", text="Data de Nascimento")

      self.listC.column("#0", width=1)
      self.listC.column("#1", width=50)
      self.listC.column("#2", width=200)
      self.listC.column("#3", width=125)
      self.listC.column("#4", width=125)
      self.listC.column("#5", width=125)
      
      self.listC.place(relx=0, rely=0, relwidth=1, relheight=1)
      
      self.scrollListC = Scrollbar(self.FrameRegistros, orient_='vertical')
      self.listC.configure(yscroll=self.scrollListC.set)
      self.scrollListC.place(relx=0.98, rely=0.05, relwidth=0.015, relheight=0.9)
      self.listC.bind("<Double-1>", self.DuploClique)
      