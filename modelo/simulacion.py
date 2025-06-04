from modelo.servidor.mecanico import Mecanico
from modelo.servidor.asistente import Asistente
from modelo.cliente.cliente import Cliente
from modelo.vector_estado import Vector_Estado
from modelo.cliente.estado_cliente import Estado_Cliente
from modelo.evento import Evento
from modelo.cliente.motivo_cliente import Motivo_Cliente
from modelo.servidor.estado_asistente import Estado as Estado_Asistente
from modelo.servidor.estado_mecanico import Estado as Estado_Mecanico

CANT_MAXIMA_ITERACIONES = 100000
BICIS_REPARADAS = 3


class Simulacion:
    def __init__(self, TIEMPO_SIMULACION, HORA_OBSERVAR, CANT_ITERACIONES):
        self.TIEMPO_SIMULACION = TIEMPO_SIMULACION
        self.HORA_OBSERVAR = HORA_OBSERVAR
        self.CANT_ITERACIONES = CANT_ITERACIONES
        self.reloj_inicial = 0.0
        self.mecanico = Mecanico(BICIS_REPARADAS)
        self.asistente = Asistente()
        self.vector_estado_anterior: Vector_Estado = None
        self.array_vector_estado_mostrar: list[Vector_Estado] = []

    def determinar_evento_asociado(
        proximo_evento, cliente, tiempo_fin_reparacion, tiempo_fin_limpieza
    ):
        if proximo_evento == cliente.hora_llegada:
            return Evento.LC.value
        elif proximo_evento == cliente.hora_fin_atencion:
            return Evento.FA.value
        elif proximo_evento == tiempo_fin_reparacion:
            return Evento.FR.value
        elif proximo_evento == tiempo_fin_limpieza:
            return Evento.FL.value

    def simular_taller_bicicletas(self):
        reloj = self.reloj_inicial
        evento = Evento.INIT
        cola_eventos = []
        id_cliente = 1

        # COMENZAMOS DEFINIENDO EL ESTADO INICIAL DE LA SIMULACION
        # EN EL ESTADO INICIAL LAS COLAS ESTAN EN CERO CON EXCEPCION DE LA COLA DE BICIS LISTAS PARA RETIRO
        # EL RELOJ ESTA EN CERO

        
        # CREAMOS LA PRIMER LLEGADA DE UN CLIENTE
        cliente = Cliente(id_cliente, Estado_Cliente.SA.value)
        cliente.evento_llegada_cliente(reloj)
        cola_eventos.append(cliente.tiempo_llegada)
        
        # TANTO EL MECACNICO COMO EL ASISTENTE ESTAN LIBRES

        # CON ESTOS DATOS INICIALES, CREAMOS EL PRIMER VECTOR DE ESTADO
        vector_estado = Vector_Estado(
            evento=evento,
            reloj=reloj,
            tiempo_entre_llegadas=cliente.tiempo_entre_llegada,
            hora_llegada=cliente.tiempo_llegada,
            motivo=cliente.motivo_llegada,
            tiempo_atencion=0.0,
            tiempo_fin_atencion=0.0,
            estado_cliente=cliente.estado,
            estado_asistente= self.asistente.estado,
            cola_asistente=len(self.asistente.cola_atencion),
            cola_bicis_listas_para_retiro=self.mecanico.cola_bicis_reparadas ,
            tiempo_reparacion=0.0,
            tiempo_fin_reparacion=0.0,
            estado_mecanico=self.mecanico.estado,
            cola_mecanico=len(self.mecanico.cola_mecanico),
            tiempo_fin_limpieza=0.0
        )

        self.vector_estado_anterior = vector_estado
        if self.HORA_OBSERVAR == 0:
            self.array_vector_estado_mostrar.append(vector_estado)
        
        # CON EL ESTADO INICIAL SETEADO PODEMOS INICIAR LA SIMULACION


        id_cliente += 1