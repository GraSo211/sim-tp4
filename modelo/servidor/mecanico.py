from modelo.servidor.estado_mecanico import Estado
import random;
class Mecanico:
    def __init__(self, cola_bicis_reparadas:int):
        self.estado:Estado = Estado.LIBRE
        self.tiempo_limpieza:float = 5;
        self.cola_reparacion = 0;
        self.cola_bicis_reparadas = cola_bicis_reparadas;

    def tiempo_reparar_bicicleta(self):
        return random.uniform(18, 22)

    def calcular_fin_limpieza(self, tiempo_actual: float):
        return tiempo_actual + self.tiempo_limpieza

    def atender_bicicleta(self, tiempo_actual: float):
        self.estado = Estado.OCUPADO
        return tiempo_actual + self.tiempo_reparar_bicicleta()