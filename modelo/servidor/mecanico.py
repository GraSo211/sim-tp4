from estado import Estado
import random;
class Mecanico:
    def __init__(self):
        self.estado:Estado = Estado.Libre
        self.tiempo_limpieza = 5;



    def _tiempo_reparar_bicicleta():
        return random.uniform(18,22)



    def _tiempo_fin_limpieza(self,tiempo):
        return tiempo + self.tiempo_limpieza
        