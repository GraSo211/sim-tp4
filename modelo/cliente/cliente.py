import random
from modelo.cliente.estado_cliente import Estado_Cliente
from modelo.cliente.motivo_cliente import Motivo_Cliente
class Cliente:
    def __init__(self, id:int, estado:Estado_Cliente,   ):
        self.id:int = id
        self.estado:Estado_Cliente = estado
        self.rnd_m:float = 0
        self.motivo_llegada: Motivo_Cliente = None
        self.rnd_tell:float = 0
        self.tiempo_entre_llegada:float = 0.0
        self.tiempo_llegada:float = 0.0

    # EL UNICO EVENTO DEL CLIENTE ES SU LLEGADA AL LOCAL
    # SU LLEGADA PUEDE SER POR 3 MOTIVOS:
    # - COMPRAR ACCESORIOS
    # - ENTREGAR BICICLETA PARA REPARACION
    # - RETIRAR BICICLETA REPARADA



    def _generar_motivo_llegada(self):
        rnd = round(random.random(),4)
        self.rnd_m = rnd
        if(rnd<0.45):
            self.motivo_llegada = Motivo_Cliente.CA.value

        elif(rnd < 0.7):
            self.motivo_llegada = Motivo_Cliente.EBR.value
        else:
            self.motivo_llegada = Motivo_Cliente.RBR.value


    def evento_llegada_cliente(self, reloj: float):
        # EL CLIENTE LLEGA AL LOCAL ENTRE 13 Y 17 MINUTOS DESPUES DEL ULTIMO CLIENTE
        self.rnd_tell = round(random.random(),4)
        rnd_uniforme  = round((13+(17-13)*self.rnd_tell),4)
        self.tiempo_entre_llegada = rnd_uniforme
        self.tiempo_llegada = round(reloj + self.tiempo_entre_llegada,4)
        self._generar_motivo_llegada()




    def __str__(self):
        return (f"Cliente(id={self.id}, estado={self.estado if self.estado else 'None'}, "
            f"motivo_llegada={self.motivo_llegada})")


    def __repr__(self):
        return self.__str__()