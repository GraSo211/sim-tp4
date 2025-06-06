import random
from modelo.servidor.estado_asistente import Estado
from modelo.cliente.motivo_cliente import Motivo_Cliente
from modelo.cliente.cliente import Cliente
from typing import List
from modelo.cliente.estado_cliente import Estado_Cliente
class Asistente:
    def __init__(self, evento_motivo_ca_val_a, evento_motivo_ca_val_b ):
        self.estado:Estado = Estado.LIBRE.value
        self.cola_atencion: List[Cliente] = []
        self.rnd_ta: float = 0.0
        self.tiempo_atencion:float = 0.0
        self.tiempo_fin_atencion:float = 0.0
        self.evento_motivo_ca_val_a = evento_motivo_ca_val_a
        self.evento_motivo_ca_val_b = evento_motivo_ca_val_b


    # EL ASISTENTE TIENE 2 OPCIONES:
    # ESTAR LIBRE
    # ESTAR OCUPADO ATENDIENDO A UN CLIENTE

    def evento_atencion(self, cliente: Cliente, reloj: float):
        # AL LLEGAR UN CLIENTE, SI EL ASISTENTE ESTA LIBRE, SE OCUPA ATENDIENDO
        
        if self.estado == Estado.LIBRE.value:
            self.estado = Estado.OCUPADO.value
            # EL TIEMPO DE ATENCION DE LOS CLIENTES ES:
            # 3 MINUTOS SI ES PARA ENTREGAR O RETIRAR BICICLETAS
            # EN CASO DE COMPRAR ACCESORIOS LA ATENCION SERA UNA DISTRIBUCION UNIFORME
            # ENTRE 6 Y 10 MINUTOS
            cliente.estado = Estado_Cliente.SA.value
            if(cliente.motivo_llegada == Motivo_Cliente.CA.value ):
                self.rnd_ta = round(random.random(),4)
                rnd_uniforme = round((self.evento_motivo_ca_val_a+(self.evento_motivo_ca_val_b-self.evento_motivo_ca_val_a)*self.rnd_ta),4);
                self.tiempo_atencion = rnd_uniforme;
                self.tiempo_fin_atencion = round(reloj + self.tiempo_atencion,4);

            elif(cliente.motivo_llegada == Motivo_Cliente.EBR.value or cliente.motivo_llegada == Motivo_Cliente.RBR.value ):
                self.rnd_ta = 0
                self.tiempo_atencion = round(3,4);
                self.tiempo_fin_atencion = round(reloj + self.tiempo_atencion,4);

        # SI ESTA OCUPADO, AUMENTA LA COLA DE ESPERA
        else:
            cliente.estado = Estado_Cliente.EA.value
            self.cola_atencion.append(cliente)


    

    def evento_fin_atencion(self, reloj:float ) -> float:
        # AL FINALIZAR LA ATENCION, SI HAY CLIENTES EN LA COLA, SE ATIENDE AL SIGUIENTE
        if(len(self.cola_atencion) > 0):
            self.estado = Estado.OCUPADO.value
            cliente = self.cola_atencion.pop(0)
            cliente.estado = Estado_Cliente.SA.value
            if(cliente.motivo_llegada == Motivo_Cliente.CA.value ):
                self.rnd_ta = round(random.random(),4)
                rnd_uniforme = round((self.evento_motivo_ca_val_a+(self.evento_motivo_ca_val_b-self.evento_motivo_ca_val_a)*self.rnd_ta),4);
                self.tiempo_atencion = rnd_uniforme;
            elif(cliente.motivo_llegada == Motivo_Cliente.EBR.value or cliente.motivo_llegada == Motivo_Cliente.RBR.value ):
                self.rnd_ta = 0
                self.tiempo_atencion = round(3,4)
            
            self.tiempo_fin_atencion = round(reloj + self.tiempo_atencion,4);
            return cliente

        # SI NO HAY CLIENTES EN LA COLA, VUELVE A ESTAR LIBRE
        else:
            self.estado = Estado.LIBRE.value
            return None

