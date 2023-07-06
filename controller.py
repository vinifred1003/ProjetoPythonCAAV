from model import Model

class Controller:
    
  def __init__(self, modelo=None, placa=None, marca=None, ano=None, nome = None, CNH = None,CPF = None,data_nasc = None,logradouro = None,numero = None ):
    #var dos carros
    self.modelo = modelo
    self.placa = placa
    self.marca = marca
    self.ano = ano
    #variaveis dos clientes
    self.nome = nome
    self.CNH = CNH
    self.CPF = CPF
    self.data_nasc = data_nasc
    self.logradouro = logradouro
    self.numero = numero
    
    
    self.model = Model(self)


  def set(self, view, model):
    self.view = view
    self.model = model

  def salvar_dados(self):
    self.model.create(self.modelo, self.placa, self.marca, self.ano, self.nome,self.CNH,self.CPF,self.data_nasc,self.logradouro,self.numero)

  def ler_dados(self):
    self.model.read()
    return (self.model.resultado)
 
  def excluir_dados(self, placa):
    self.model.delete(placa)

  def salvar_cliente(self):
    self.model.create_cliente(self.nome,self.CNH,self.CPF,self.data_nasc,self.logradouro,self.numero)
