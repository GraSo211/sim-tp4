import random
from modelo.servidor.estado import Estado
from modelo.cliente.motivo_cliente import Motivo_Cliente

class Asistente:
    def __init__(self):
        self.estado:Estado = Estado.LIBRE
        self.cola:int = 0

    def _generar_tiempo_atencion(motivo_cliente: Motivo_Cliente):
        # EL TIEMPO DE ATENCION DE LOS CLIENTES ES:
        # 3 MINUTOS SI ES PARA ENTREGAR O RETIRAR BICICLETAS
        # EN CASO DE COMPRAR ACCESORIOS LA ATENCION SERA UNA DISTRIBUCION UNIFORME
        # ENTRE 6 Y 10 MINUTOS
        if(motivo_cliente == Motivo_Cliente.COMPRAR_ACCESORIOS ):
            tiempo = random.uniform(6,10);

        elif(motivo_cliente == Motivo_Cliente.ENTREGAR_BICICLETA_REPARACION or motivo_cliente == Motivo_Cliente.RETIRAR_BICICLETA_REPARADA ):
            tiempo = 3;

        return tiempo
    

    