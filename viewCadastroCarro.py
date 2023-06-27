from tkinter import *
from controller import Controller

def donothing():
    pass

class ViewCadastroCarro(Toplevel):
    def __init__(self, janela_classe_visivel):
        super().__init__(janela_classe_visivel)
        self.janela_classe_visivel = janela_classe_visivel
        self.run()
        self.Insercoes()
        self.botao()


    def run(self):
        self.title("Cadastro de Carro")
        self.geometry("600x300")
        self.configure(background="#7092BE")
        self.resizable(True, True)
   
    def Insercoes(self):
        self.lbModelo = Label(self, text="Modelo", fg="white", bg="gray")
        self.lbModelo.place(relx=0.1, rely=0.15)

        self.EntryModelo = Entry(self, bd=2, bg="white")
        self.EntryModelo.place(relx=0.1, rely=0.25)

        self.lbPlaca = Label(self, text="Placa", fg="white", bg="gray")
        self.lbPlaca.place(relx=0.1, rely=0.35)

        self.EntryPlaca = Entry(self, bd=2, bg="white")
        self.EntryPlaca.place(relx=0.1, rely=0.45)

        self.lbMarca = Label(self, text="Marca", fg="white", bg="gray")
        self.lbMarca.place(relx=0.6, rely=0.15)

        self.EntryMarca = Entry(self, bd=2, bg="white")
        self.EntryMarca.place(relx=0.6, rely=0.25)

        self.lbAno = Label(self, text="Ano", fg="white", bg="gray")
        self.lbAno.place(relx=0.6, rely=0.35)

        self.EntryAno = Entry(self, bd=2, bg="white")
        self.EntryAno.place(relx=0.6, rely=0.45)
    
    def Quit(self):
        self.destroy()
    
    def botao(self):
        self.BotaoSalvar = Button(self, bd=2, text="Salvar", command=self.salvar_dados)
        self.BotaoSalvar.place(relx=0.40, rely=0.65, relwidth=0.2, relheight=0.1)
    
    def salvar_dados(self):
        modelo = self.EntryModelo.get()
        placa = self.EntryPlaca.get()
        marca = self.EntryMarca.get()
        ano = self.EntryAno.get()

        dados_carro = Controller(modelo, placa, marca, ano)
        dados_carro.salvar_dados()

