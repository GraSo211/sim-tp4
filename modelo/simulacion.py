from modelo.servidor.mecanico import Mecanico
from modelo.servidor.asistente import Asistente
from modelo.cliente.cliente import Cliente
from modelo.vector_estado import Vector_Estado
from modelo.cliente.estado_cliente import Estado_Cliente
from modelo.evento import Evento

CANT_MAXIMA_ITERACIONES = 100000
BICIS_REPARADAS = 3


class Simulacion:
    def __init__(self, TIEMPO_SIMULACION, HORA_OBSERVAR, CANT_ITERACIONES):
        self.TIEMPO_SIMULACION = TIEMPO_SIMULACION
        self.HORA_OBSERVAR = HORA_OBSERVAR
        self.CANT_ITERACIONES = CANT_ITERACIONES
        self.reloj_inicial = 0
        self.cont_iteraciones = 0
        self.mecanico = Mecanico(BICIS_REPARADAS)
        self.asistente = Asistente()
        self.clientes: list[Cliente] = []
        self.vector_estado_anterior: Vector_Estado = None
        self.array_vector_estado_mostrar: list[Vector_Estado] = []



    def determinar_evento_asociado(proximo_evento, cliente, tiempo_fin_reparacion, tiempo_fin_limpieza):
        if proximo_evento == cliente.hora_llegada:
            return Evento.LLEGADA_CLIENTE
        elif proximo_evento == cliente.hora_fin_atencion:
            return Evento.FIN_ATENCION_ASISTENTE
        elif proximo_evento == tiempo_fin_reparacion:
            return Evento.FIN_REPARACION
        elif proximo_evento == tiempo_fin_limpieza:
            return Evento.FIN_LIMPIEZA

    def simular_taller_bicicletas(self):
        # INICIA LA SIMULACION
        clientes_id = 1
        cliente1 = Cliente(clientes_id, Estado_Cliente.CREADO)
        self.clientes.append(cliente1)
        clientes_id += 1

        # ESTADO ACTUAL PRIMERO SERA EL INICIAL
        evento = Evento.INIT
        reloj = self.reloj_inicial

        [cliente_hora_llegada, tiempo_entre_llegada_cliente] = cliente1.llegada_cliente(reloj)
        cliente1.hora_llegada = cliente_hora_llegada


        tiempo_atencion_asistente = self.asistente.generar_tiempo_atencion(
            cliente1.motivo_llegada
        )
        cliente1.set_fin_atencion(reloj,tiempo_atencion_asistente)
        hora_fin_atencion = cliente1.hora_fin_atencion

        estado_cliente = cliente1.estado

        tiempo_reparacion = 0
        tiempo_fin_reparacion = reloj + tiempo_reparacion

        tiempo_fin_limpieza = 0

        vector_estado_actual = Vector_Estado(
            evento,
            reloj,
            tiempo_entre_llegada_cliente,
            cliente1.hora_llegada,
            cliente1.motivo_llegada,
            tiempo_atencion_asistente,
            hora_fin_atencion,
            estado_cliente,
            self.asistente.estado,
            self.asistente.cola,
            self.mecanico.cola_bicis_reparadas,
            tiempo_reparacion,
            tiempo_fin_reparacion,
            self.mecanico.estado,
            self.mecanico.cola_reparacion,
            tiempo_fin_limpieza,
        )

        CONT_ITERACIONES = 0
        while (
            CONT_ITERACIONES <= CANT_MAXIMA_ITERACIONES
            or reloj <= self.TIEMPO_SIMULACION
        ):
            # HACEMOS ALGO
            proximo_evento = min(
                [
                    cliente1.hora_llegada,
                    cliente1.hora_fin_atencion,
                    tiempo_fin_reparacion,
                    tiempo_fin_limpieza,
                ]
            )
            reloj = proximo_evento
            evento = self.determinar_evento_asociado(self.clientes[-1],tiempo_fin_reparacion,tiempo_fin_limpieza)

            if reloj >= self.HORA_OBSERVAR and self.CANT_MAXIMA_ITERACIONES > 0:
                self.array_vector_estado_mostrar.append(vector_estado_actual)
                self.CANT_MAXIMA_ITERACIONES -= 1

            # AL FINAL SUMAMOS 1 AL CONTADOR
            CONT_ITERACIONES += 1

        return self.array_vector_estado_mostrar
