from enum import Enum
import random
class Estado(Enum):
    LIBRE = "LIBRE"
    OCUPADO = "OCUPADO"

class Motivo_Cliente(Enum):
    COMPRAR_ACCESORIOS ="COMPRAR_ACCESORIOS"
    ENTREGAR_BICICLETA_REPARACION = "ENTREGAR_BICICLETA_REPARACION"
    RETIRAR_BICICLETA_REPARADA = "RETIRAR_BICICLETA_REPARADA"


class Asistente:
    def __init__(self, estado: Estado):
        self.estado = estado

    def _generar_tiempo_atencion(motivo_cliente: Motivo_Cliente):
        # EL TIEMPO DE ATENCION DE LOS CLIENTES TIENE UNA DISTRIBUCION UNIFORME
        # ENTRE 13 Y 17 MINUTOS SI ES PARA ENTREGAR O RETIRAR BICICLETAS
        # EN CASO DE COPMRAR ACCESORIOS LA ATENCION SERA UNA DISTRIBUCION UNIFORME
        # ENTRE 6 Y 10 MINUTOS
        if(motivo_cliente == Motivo_Cliente.COMPRAR_ACCESORIOS ):
            rnd = random.uniform(6,10);

        elif(motivo_cliente == Motivo_Cliente.ENTREGAR_BICICLETA_REPARACION or motivo_cliente == Motivo_Cliente.RETIRAR_BICICLETA_REPARADA ):
            rnd  = random.uniform(13, 17)