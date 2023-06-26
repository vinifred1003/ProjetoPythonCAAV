
from Controller import CarroController
from viewAlugueis import View
from model import Model
from viewCadastroCarro import ViewCadastroCarro

Controller = CarroController()
model = Model()

view = View(Controller)

Controller.set(view, model)

view.run()
