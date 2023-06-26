
class CarroController:
    
  def __init__(self):
    pass

  def set(self, view, model):
    self.view = view
    self.model = model

  def addCarro(self):
    modelo = self.view.EntryModelo.get()
    marca = self.view.EntryMarca.get()
    placa = self.view.EntryPlaca.get()
    ano = self.view.EntryAno.get()
    

