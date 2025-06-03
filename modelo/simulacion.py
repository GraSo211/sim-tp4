from servidor.mecanico import Mecanico
from servidor.asistente import Asistente
from cliente.cliente import Cliente
from vector_estado import Vector_Estado

CANT_MAXIMA_ITERACIONES = 100000
BICIS_REPARADAS = 3
class Simulacion:
    def __init__(self, TIEMPO_SIMULACION ,HORA_OBSERVAR, CANT_ITERACIONES  ):
        self.TIEMPO_SIMULACION = TIEMPO_SIMULACION;
        self.HORA_OBSERVAR = HORA_OBSERVAR;
        self.CANT_ITERACIONES = CANT_ITERACIONES;
        self.reloj_inicial = 0
        self.cont_iteraciones = 0
        self.mecanico = Mecanico(),
        self.asistente = Asistente()
        self.clientes: list[Cliente] = []
        self.vector_estado_anterior: Vector_Estado = None

    def simular_taller_bicicletas(self):
        vector_estado_actual = Vector_Estado()

