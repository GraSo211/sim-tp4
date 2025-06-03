import random
from modelo.cliente.estado_cliente import Estado_Cliente
from modelo.cliente.motivo_cliente import Motivo_Cliente
class Cliente:
    def __init__(self, id:int, estado:Estado_Cliente,   ):
        self.id:int = id
        self.estado:Estado_Cliente = estado
        self.motivo_llegada: Motivo_Cliente = None
        self.hora_llegada:float = 0
        self.hora_fin_atencion:float = None


    def _llegada_cliente(self):
        tiempo_entre_llegada = random.uniform(13,17)
        self._generar_motivo_llegada()
        
        return tiempo_entre_llegada
    

    def _generar_motivo_llegada(self):
        rnd = random.random()
        if(rnd<0.45):
            self.motivo_llegada = Motivo_Cliente.CA

        elif(rnd < 0.7):
            self.motivo_llegada = Motivo_Cliente.EBR
        else:
            self.motivo_llegada = Motivo_Cliente.RBR

    



