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
        self.reloj_inicial = 0
        self.cont_iteraciones = 0
        self.mecanico = Mecanico(BICIS_REPARADAS)
        self.asistente = Asistente()
        self.clientes: list[Cliente] = []
        self.vector_estado_anterior: Vector_Estado = None
        self.array_vector_estado_mostrar: list[Vector_Estado] = []

    def determinar_evento_asociado(
        proximo_evento, cliente, tiempo_fin_reparacion, tiempo_fin_limpieza
    ):
        if proximo_evento == cliente.hora_llegada:
            return Evento.LLEGADA_CLIENTE
        elif proximo_evento == cliente.hora_fin_atencion:
            return Evento.FIN_ATENCION_ASISTENTE
        elif proximo_evento == tiempo_fin_reparacion:
            return Evento.FIN_REPARACION
        elif proximo_evento == tiempo_fin_limpieza:
            return Evento.FIN_LIMPIEZA

    def simular_taller_bicicletas(self):
        reloj = self.reloj_inicial
        evento = Evento.INIT
        cola_eventos = []

        # Planificamos primer cliente
        cliente_id = 1
        cliente = Cliente(cliente_id, Estado_Cliente.CREADO)
        tiempo_entre_llegada_cliente, cliente_hora_llegada = cliente.llegada_cliente(
            reloj
        )
        cliente.hora_llegada = cliente_hora_llegada
        motivo_cliente = cliente.motivo_llegada
        self.clientes.append(cliente)
        cola_eventos.append((cliente.hora_llegada, Evento.LC, cliente))

        # Variables para estadísticas
        tiempo_ocupado_asistente = 0
        tiempo_ocupado_mecanico = 0
        clientes_retiro_bici_no_lista = 0
        total_clientes_retiro = 0

        CONT_ITERACIONES = 0
        while (
            CONT_ITERACIONES <= CANT_MAXIMA_ITERACIONES
            or reloj <= self.TIEMPO_SIMULACION
        ):
            # Obtener próximo evento
            cola_eventos.sort()
            reloj, evento, cliente = cola_eventos.pop(0)

            if evento == Evento.LC:
                if motivo_cliente == Motivo_Cliente.RBR:
                    # total_clientes_retiro += 1
                    if self.mecanico.cola_bicis_reparadas == 0:
                        ##clientes_retiro_bici_no_lista += 1
                        pass
                    else:
                        self.mecanico.cola_bicis_reparadas -= 1

                if self.asistente.estado == Estado_Asistente.LIBRE:
                    self.asistente.estado = Estado_Asistente.OCUPADO
                    tiempo_atencion = self.asistente.generar_tiempo_atencion(
                        cliente.motivo_llegada
                    )
                    tiempo_ocupado_asistente += tiempo_atencion
                    cliente.hora_fin_atencion = reloj + tiempo_atencion
                    cola_eventos.append((cliente.hora_fin_atencion, Evento.FA, cliente))
                else:
                    self.asistente.cola += 1

                # Planificar próximo cliente
                cliente_id += 1
                nuevo_cliente = Cliente(cliente_id, Estado_Cliente.CREADO)
                tiempo_entre_llegada_cliente, cliente_hora_llegada = (
                    nuevo_cliente.llegada_cliente(reloj)
                )
                nuevo_cliente.hora_llegada = cliente_hora_llegada
                motivo_cliente = nuevo_cliente.motivo_llegada
                self.clientes.append(nuevo_cliente)
                cola_eventos.append(
                    (nuevo_cliente.hora_llegada, Evento.LC, nuevo_cliente)
                )

            elif evento == Evento.FA:
                if cliente.motivo_llegada == Motivo_Cliente.EBR:
                    self.mecanico.cola_reparacion += 1
                    if self.mecanico.estado == Estado_Mecanico.LIBRE:
                        self.mecanico.estado = Estado_Mecanico.OCUPADO
                        tiempo_reparacion = self.mecanico.tiempo_reparar_bicicleta()
                        tiempo_ocupado_mecanico += tiempo_reparacion
                        cola_eventos.append(
                            (reloj + tiempo_reparacion, Evento.FR, cliente)
                        )

                if self.asistente.cola > 0:
                    self.asistente.cola -= 1
                    # Aquí puedes obtener al siguiente cliente esperando
                    # y planificar su atención
                else:
                    self.asistente.estado = Estado_Asistente.LIBRE

            elif evento == Evento.FR:
                cola_eventos.append(
                    (reloj + self.mecanico.tiempo_limpieza, Evento.FL, cliente)
                )  # 5 min limpieza

            elif evento == Evento.FL:
                self.mecanico.cola_bicis_reparadas += 1
                if self.mecanico.cola_reparacion > 0:
                    self.mecanico.cola_reparacion -= 1
                    tiempo_reparacion = self.mecanico.tiempo_reparar_bicicleta()
                    tiempo_ocupado_mecanico += tiempo_reparacion
                    cola_eventos.append((reloj + tiempo_reparacion, Evento.FR, cliente))
                else:
                    self.mecanico.estado = Estado_Mecanico.LIBRE

            if reloj >= self.HORA_OBSERVAR:
                # Crear vector de estado
                # Crear vector de estado
                vector_estado = Vector_Estado(
                    evento=evento,
                    reloj=reloj,
                    tiempo_entre_llegadas=(
                        tiempo_entre_llegada_cliente
                        if "tiempo_entre_llegada_cliente" in locals()
                        else 0
                    ),
                    hora_llegada=cliente.hora_llegada if cliente else 0,
                    motivo=cliente.motivo_llegada if cliente else None,
                    tiempo_atencion=(
                        cliente.hora_fin_atencion - reloj
                        if hasattr(cliente, "hora_fin_atencion")
                        else 0
                    ),
                    tiempo_fin_atencion=(
                        cliente.hora_fin_atencion
                        if hasattr(cliente, "hora_fin_atencion")
                        else 0
                    ),
                    estado_cliente=cliente.estado if cliente else Estado_Cliente.CREADO,
                    estado_asistente=self.asistente.estado,
                    cola_asistente=self.asistente.cola,
                    cola_bicis_listas_para_retiro=self.mecanico.cola_bicis_reparadas,
                    tiempo_reparacion=0,  # reemplazar si guardás el valor
                    tiempo_fin_reparacion=0,  # reemplazar si lo calculás
                    estado_mecanico=self.mecanico.estado,
                    cola_mecanico=self.mecanico.cola_reparacion,
                    tiempo_fin_limpieza=0,  # podés guardarlo en una variable al planificarlo
                )

                self.array_vector_estado_mostrar.append(vector_estado)

            CONT_ITERACIONES += 1
        return self.array_vector_estado_mostrar