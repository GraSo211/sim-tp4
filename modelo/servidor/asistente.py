import random
from modelo.servidor.estado_asistente import Estado
from modelo.cliente.motivo_cliente import Motivo_Cliente

class Asistente:
    def __init__(self):
        self.estado:Estado = Estado.LIBRE.value
        self.cola:int = 0


    def generar_tiempo_atencion(self,motivo_cliente: Motivo_Cliente):
        # EL TIEMPO DE ATENCION DE LOS CLIENTES ES:
        # 3 MINUTOS SI ES PARA ENTREGAR O RETIRAR BICICLETAS
        # EN CASO DE COMPRAR ACCESORIOS LA ATENCION SERA UNA DISTRIBUCION UNIFORME
        # ENTRE 6 Y 10 MINUTOS
        if(motivo_cliente == Motivo_Cliente.CA.value ):
            tiempo = random.uniform(6,10);

        elif(motivo_cliente == Motivo_Cliente.EBR.value or motivo_cliente == Motivo_Cliente.RBR.value ):
            tiempo = 3;

        return round(tiempo,4)
    

    def calcular_fin_atencion(self, tiempo_inicio: float, duracion: float) -> float:
        return round(tiempo_inicio + duracion,4)
    

    def empezar_a_trabajar(self):
        self.estado = Estado.OCUPADO.value
        if self.cola > 0:
            self.cola -= 1