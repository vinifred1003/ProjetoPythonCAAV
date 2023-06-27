from model import Model

class Controller:
    
  def __init__(self, modelo=None, placa=None, marca=None, ano=None):

    self.modelo = modelo
    self.placa = placa
    self.marca = marca
    self.ano = ano
    self.model = Model(self)

  def set(self, view, model):
    self.view = view
    self.model = model

  def salvar_dados(self):
    self.model.create(self.modelo, self.placa, self.marca, self.ano)

  def ler_dados(self):
    self.model.read()
    return self.model.resultado
 
