from controller import Controller
from viewCarros import ViewCarros
from model import Model
import tkinter as tk

root1 = tk.Tk()

controller = Controller()
model = Model(controller)

view = ViewCarros(root1)

controller.set(view, model)

view.run()

root1.mainloop()
