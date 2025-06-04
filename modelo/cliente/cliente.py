import random
from modelo.cliente.estado_cliente import Estado_Cliente
from modelo.cliente.motivo_cliente import Motivo_Cliente
class Cliente:
    def __init__(self, id:int, estado:Estado_Cliente,   ):
        self.id:int = id
        self.estado:Estado_Cliente = estado
        self.motivo_llegada: Motivo_Cliente = None
        self.hora_llegada:float = None
        self.hora_fin_atencion:float = None


    def llegada_cliente(self, tiempo_actual):
        tiempo_entre_llegada = random.uniform(13, 17)
        self.hora_llegada = tiempo_actual + tiempo_entre_llegada
        self._generar_motivo_llegada()
        return tiempo_entre_llegada, self.hora_llegada
    


    def set_fin_atencion(self, tiempo_inicio, duracion):
        self.hora_fin_atencion = tiempo_inicio + duracion

    

    def _generar_motivo_llegada(self):
        rnd = random.random()
        if(rnd<0.45):
            self.motivo_llegada = Motivo_Cliente.CA

        elif(rnd < 0.7):
            self.motivo_llegada = Motivo_Cliente.EBR
        else:
            self.motivo_llegada = Motivo_Cliente.RBR

    



