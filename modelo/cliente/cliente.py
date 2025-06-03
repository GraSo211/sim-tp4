import random
from modelo.cliente.estado_cliente import Estado_Cliente
from modelo.cliente.motivo_cliente import Motivo_Cliente
class Cliente:
    def __init__(self, id:int, estado:Estado_Cliente,  hora_llegada:float, ):
        self.id:int = id
        self.estado:Estado_Cliente = estado
        self.motivo_llegada: Motivo_Cliente = None
        self.tiempo_entre_llegada:float = None
        self.hora_llegada:float = hora_llegada
        self.hora_fin_atencion:float = None


    def _llegada_cliente(self):
        self.tiempo_entre_llegada = random.uniform(13,17)
        self._generar_motivo_llegada()
        
        return self.tiempo_entre_llegada + self.hora_llegada
    

    def _generar_motivo_llegada(self):
        rnd = random()
        if(rnd<0.45):
            self.motivo_llegada = Motivo_Cliente.COMPRAR_ACCESORIOS

        elif(rnd < 0.7):
            self.motivo_llegada = Motivo_Cliente.ENTREGAR_BICICLETA_REPARACION
        else:
            self.motivo_llegada = Motivo_Cliente.RETIRAR_BICICLETA_REPARADA

    



