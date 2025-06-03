from vista.vista import Vista
from controlador.controlador import Controlador

class Main:
    def __init__(self):
        self.vista = Vista()
        
        self.controlador = Controlador(self.vista)
        


        




    def run(self):
        self.vista.mainloop();
if __name__ == "__main__":
    main = Main()
    main.run()