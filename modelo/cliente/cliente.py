import random
from modelo.cliente.estado_cliente import Estado_Cliente
from modelo.cliente.motivo_cliente import Motivo_Cliente
class Cliente:
    def __init__(self, id:int, estado:Estado_Cliente,   ):
        self.id:int = id
        self.estado:Estado_Cliente = estado
        self.motivo_llegada: Motivo_Cliente = None
        self.tiempo_entre_llegada:float = 0.0
        self.tiempo_llegada:float = 0.0

    # EL UNICO EVENTO DEL CLIENTE ES SU LLEGADA AL LOCAL
    # SU LLEGADA PUEDE SER POR 3 MOTIVOS:
    # - COMPRAR ACCESORIOS
    # - ENTREGAR BICICLETA PARA REPARACION
    # - RETIRAR BICICLETA REPARADA



    def _generar_motivo_llegada(self):
        rnd = random.random()
        if(rnd<0.45):
            self.motivo_llegada = Motivo_Cliente.CA

        elif(rnd < 0.7):
            self.motivo_llegada = Motivo_Cliente.EBR
        else:
            self.motivo_llegada = Motivo_Cliente.RBR


    def evento_llegada_cliente(self, reloj: float):
        # EL CLIENTE LLEGA AL LOCAL ENTRE 13 Y 17 MINUTOS DESPUES DEL ULTIMO CLIENTE
        self.tiempo_entre_llegada = random.uniform(13, 17)
        self.tiempo_llegada = reloj + self.tiempo_entre_llegada
        self._generar_motivo_llegada()







