import mysql.connector

class Model:
    def __init__(self, controller):
        self.controller = controller
        self.conexao = None
        self.cursor = None
        self.resultado=None
        self.conexaoBD()
        self.cursorBD()
    def conexaoBD(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="aluguel_de_carro"
        )
        
    def cursorBD(self):
        self.cursor = self.conexao.cursor()
        
    def create(self, modelo, placa, marca, ano):
        comando = f'INSERT INTO carros (modelo, marca, placa, ano) VALUES ("{modelo}","{marca}","{placa}","{ano}");'
        self.cursor.execute(comando)
        self.conexao.commit()
        pass
    
    def read(self):
        comando = 'SELECT * FROM carros;'
        self.cursor.execute(comando)
        self.resultado = self.cursor.fetchall()
        pass
   
    def delete(self, modelo):    
        comando = f'DELETE FROM carros WHERE modelo ="{modelo}";'
        self.cursor.execute(comando)
        self.conexao.commit()
