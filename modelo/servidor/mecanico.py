from modelo.servidor.estado_mecanico import Estado
import random;
class Mecanico:
    def __init__(self, cola_bicis_reparadas:int):
        self.estado:Estado = Estado.LIBRE
        self.tiempo_limpieza:float = 5;
        self.cola_reparacion = 0;
        self.cola_bicis_reparadas = cola_bicis_reparadas;



    def _tiempo_reparar_bicicleta():
        return random.uniform(18,22)



    def _tiempo_fin_limpieza(self,tiempo):
        return tiempo + self.tiempo_limpieza
        
