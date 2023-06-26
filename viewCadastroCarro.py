from tkinter import *
from Controller import CarroController

def donothing():
    pass

root = Tk()

class ViewCadastroCarro():
    def __init__(self):
         
        self.root = root
        self.janela()
        self.Insercoes()
        self.botao()
        root.mainloop()

    def janela(self):
        self.root.title("Cadastro de Carro")
        self.root.geometry("400x300")
        self.root.configure(background="#7092BE")
        self.root.resizable(True, True)

    def Insercoes(self):
        self.lbModelo = Label(self.root, text="Modelo", fg="white", bg="gray")
        self.lbModelo.place(relx=0.1, rely=0.15)

        self.EntryModelo = Entry(self.root, bd=2, bg="white")
        self.EntryModelo.place(relx=0.1, rely=0.25)

        self.lbPlaca = Label(self.root, text="Placa", fg="white", bg="gray")
        self.lbPlaca.place(relx=0.1, rely=0.35)

        self.EntryPlaca = Entry(self.root, bd=2, bg="white")
        self.EntryPlaca.place(relx=0.1, rely=0.45)

        self.lbMarca = Label(self.root, text="Marca", fg="white", bg="gray")
        self.lbMarca.place(relx=0.6, rely=0.15)

        self.EntryMarca = Entry(self.root, bd=2, bg="white")
        self.EntryMarca.place(relx=0.6, rely=0.25)

        self.lbAno = Label(self.root, text="Ano", fg="white", bg="gray")
        self.lbAno.place(relx=0.6, rely=0.35)

        self.EntryAno = Entry(self.root, bd=2, bg="white")
        self.EntryAno.place(relx=0.6, rely=0.45)

    def botao(self):
        self.BotaoSalvar = Button(self.root, bd=2, text="Salvar")
        self.BotaoSalvar.place(relx=0.40, rely=0.65, relwidth=0.2, relheight=0.1)

    def openNewWindow (self):
      newWindow = Toplevel(ViewCadastroCarro)
      mainloop()