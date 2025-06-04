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

    def simular_taller_bicicletas(self):
        # INICIA LA SIMULACION
        clientes_id = 1
        cliente1 = Cliente(clientes_id, Estado_Cliente.CREADO)
        self.clientes.append(cliente1)
        clientes_id += 1

        # ESTADO ACTUAL PRIMERO SERA EL INICIAL
        evento = Evento.INIT
        reloj = self.reloj_inicial

        tiempo_entre_llegada_cliente = cliente1._llegada_cliente()
        cliente1.hora_llegada = tiempo_entre_llegada_cliente

        tiempo_atencion_asistente = self.asistente._generar_tiempo_atencion(cliente1.motivo_llegada)
        hora_fin_atencion = tiempo_atencion_asistente + reloj

        estado_cliente = cliente1.estado

        tiempo_reparacion = 0;
        tiempo_fin_reparacion = reloj+tiempo_reparacion;

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
            tiempo_fin_limpieza
        )

        self.array_vector_estado_mostrar.append(vector_estado_actual)

        return self.array_vector_estado_mostrar
