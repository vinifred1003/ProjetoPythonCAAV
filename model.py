import mysql.connector
from Controller import CarroController

class Model:
    def __init__(self, controller):
        self.controller = controller
        self.conexao = None
        self.cursor = None
        self.create
    def conexaoBD(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="aluguel_de_carro"
        )

    def cursorBD(self):

        self.cursor = self.conexao.cursor()
        
    def create(self):    
        #Create
        comando = f'INSERT INTO carros (modelo, marca, placa, ano) VALUES ("{modelo}","{marca}","{placa}","{ano}");'
        self.cursor.execute(comando)
        self.conexao.commit()
        #Read
    def read(self):
      comando='SELECT * FROM carros;'
      self.cursor.execute(comando)
      self.resultado = self.cursor.fetchall
    
    def delete(self):    
        #delete
        comando = f'DELETE FROM carros WHERE modelo ="{modelo}";'
        self.cursor.execute(comando)
        self.conexao.commit()
