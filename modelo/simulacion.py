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
        self.mecanico = Mecanico()
        self.cola_bicis_reparadas = BICIS_REPARADAS
        self.asistente = Asistente()
        self.vector_estado_anterior: Vector_Estado = None
        self.array_vector_estado_mostrar: list[Vector_Estado] = []
        # PARA ESTADISTICAS SE NOS PIDE:
        # PROBABILIDAD DE QUE EL CLIENTE LLEGUE A RETIRAR UNA BICI Y NO ESTE REPARADA
        # PORCENTAJE DE OCUPACION DEL ASISTENTE Y MECANICO
        self.cont_retirar_bici = 0
        self.cont_retirar_bici_no_reparada = 0
        self.acum_tiempo_ocupacion_asistente = 0.0
        self.acum_tiempo_ocupacion_mecanico = 0.0


    def determinar_evento_asociado(
        self,
        proximo_evento,
        cliente: Cliente,
        tiempo_fin_reparacion,
        tiempo_fin_limpieza,
        tiempo_fin_atencion,
    ):
        if proximo_evento == cliente.tiempo_llegada:
            return Evento.LC.value
        elif proximo_evento == tiempo_fin_atencion:
            return Evento.FA.value
        elif proximo_evento == tiempo_fin_reparacion:
            return Evento.FR.value
        elif proximo_evento == tiempo_fin_limpieza:
            return Evento.FL.value

    def simular_taller_bicicletas(self):
        reloj = self.reloj_inicial
        evento = Evento.INIT.value
        cola_eventos = []
        id_cliente = 1

        # COMENZAMOS DEFINIENDO EL ESTADO INICIAL DE LA SIMULACION
        # EN EL ESTADO INICIAL LAS COLAS ESTAN EN CERO CON EXCEPCION DE LA COLA DE BICIS LISTAS PARA RETIRO
        # EL RELOJ ESTA EN CERO

        # CREAMOS LA PRIMER LLEGADA DE UN CLIENTE
        cliente = Cliente(id_cliente, Estado_Cliente.SA.value)
        id_cliente += 1
        cliente.evento_llegada_cliente(reloj)
        cola_eventos.append((cliente.tiempo_llegada, Evento.LC.value, cliente ))

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
            estado_asistente=self.asistente.estado,
            cola_asistente=len(self.asistente.cola_atencion),
            cola_bicis_listas_para_retiro=self.cola_bicis_reparadas,
            tiempo_reparacion=0.0,
            tiempo_fin_reparacion=0.0,
            estado_mecanico=self.mecanico.estado,
            cola_mecanico=self.mecanico.cola_reparacion,
            tiempo_fin_limpieza=0.0,
            cont_retirar_bici= self.cont_retirar_bici,
            cont_retirar_bici_no_reparada= self.cont_retirar_bici_no_reparada,
            acum_tiempo_ocupacion_asistente = 0.0,
            acum_tiempo_ocupacion_mecanico = 0.0
        )

        self.vector_estado_anterior = vector_estado
        if self.HORA_OBSERVAR == 0:
            self.array_vector_estado_mostrar.append(vector_estado)

        cant_iteraciones = 0



        # CON EL ESTADO INICIAL SETEADO PODEMOS INICIAR LA SIMULACION
        # MIENTRAS EL TIEMPO DE LA SIMULACION SEA MENOR AL DEFINIDO POR EL USUARIO O LA CANTIDAD DE ITERACIONES SEA MENOR O IGUAL A LA CANTIDAD MAXIMA DE ITERACIONES
        while (
            reloj < self.TIEMPO_SIMULACION
            and cant_iteraciones < CANT_MAXIMA_ITERACIONES
        ):
            
            # COMENZAREMOS BUSCANDO CUAL ES EL PROXIMO EVENTO, PARA ELLO BUSCAMOS EL QUE TENGA EL MENOR TIEMPO EN LA COLA DE EVENTO
            evento_actual = min(cola_eventos)
            cola_eventos.remove(evento_actual)
            reloj = evento_actual[0]

            # CON EL PROXIMO EVENTO DETERMINADO, DEFINIMOS COMO ACTUAR FRENTE A ÉL
            # TENEMOS 4 OPCIONES:
            # SI EL EVENTO ES UNA LLEGADA DE CLIENTE SUCEDE LOS SIGUIENTE
            # EN CUANTO LLEGA UN CLIENTE, INICIAMOS LA LLEGADA DEL PROXIMO,
            # SI EL CLIENTE VIENE A COMPRAR ACCESORIOS SE GENERA SU FIN DE ATENCION
            # SI VIENE A RETIRAR BICICLETA SE GENERA SU FIN DE ATENCION (Y AHI DESCONTAMOS LA BICI)
            # SI VIENE A ENTREGAR BICICLETA, SE GENERA SU FIN DE ATENCION Y SE GENERA EL EVENTO REPARACION
            if evento_actual[1] == Evento.LC.value:
                
                self.asistente.evento_atencion(evento_actual[2],reloj)


                # SI SU MOTIVO DE LLEGADA ES ENTREGAR UNA BICI ENTONCES EL MECANICO SE PONE A REPARAR
                
                if evento_actual[2].motivo_llegada == Motivo_Cliente.EBR.value:
                    self.mecanico.evento_reparacion(reloj)
                    if self.mecanico.cola_reparacion == 0 :
                        cola_eventos.append((self.mecanico.tiempo_fin_reparacion, Evento.FR.value,self.mecanico))

                
                # GENERAMOS EL FIN DE ATENCION SEA CUAL SEA SU MOTIVO DE LLEGADA
                cola_eventos.append((self.asistente.tiempo_fin_atencion, Evento.FA.value, evento_actual[2]))
                
            
                
                # GENERACION DEL PROXIMO CLIENTE
                cliente = Cliente(id_cliente, Estado_Cliente.CREADO.value)
                id_cliente += 1
                cliente.evento_llegada_cliente(reloj)
                cola_eventos.append((cliente.tiempo_llegada, Evento.LC.value, cliente))

            # SI EL EVENTO ES UN FIN DE ATENCION SE ACTUALIZA AL ASISTENTE
            elif evento_actual[1] == Evento.FA.value:
                if(evento_actual[2].motivo_llegada == Motivo_Cliente.RBR.value):
                    self.cont_retirar_bici += 1
                    if self.cola_bicis_reparadas > 0:
                        self.cola_bicis_reparadas -= 1
                    else:
                        self.cont_retirar_bici_no_reparada += 1
                    
                        
                self.asistente.evento_fin_atencion(reloj)

                if self.asistente.estado == Estado_Asistente.OCUPADO.value:
                    cola_eventos.append((self.asistente.tiempo_fin_atencion, Evento.FA.value, self.asistente))



            # SI EL EVENTO ES UN FIN DE REPARACION SE ACTUALIZA AL MECANICO
            elif evento_actual[1] == Evento.FR.value:
                self.mecanico.evento_fin_reparacion(reloj)
                self.cola_bicis_reparadas +=1
                cola_eventos.append((self.mecanico.tiempo_fin_limpieza, Evento.FL.value, self.mecanico))


            # SI EL EVENTO ES UN FIN DE LIMPIEZA SE ACTUALIZA AL MECANICO Y SI EL MECANICO TIENE PENDIENTES REPARACIONES, SE INICIAN
            elif evento_actual[1] == Evento.FL.value:
                self.mecanico.evento_finalizar_limpieza(reloj)
                if(self.mecanico.estado == Estado_Mecanico.OCUPADO.value):
                    cola_eventos.append((self.mecanico.tiempo_fin_reparacion, Evento.FR.value, self.mecanico))

            



            # CON LAS 4 OPCIONES RESUELTAS, GENERAMOS EL NUEVO VECTOR DE ESTADO
            vector_estado = Vector_Estado(
                evento=evento_actual[1],
                reloj=reloj,
                tiempo_entre_llegadas=cliente.tiempo_entre_llegada,
                hora_llegada=cliente.tiempo_llegada,
                motivo=cliente.motivo_llegada,
                tiempo_atencion= self.asistente.tiempo_atencion ,
                tiempo_fin_atencion= self.asistente.tiempo_fin_atencion,
                estado_cliente= cliente.estado,
                estado_asistente= self.asistente.estado,
                cola_asistente= len(self.asistente.cola_atencion),
                cola_bicis_listas_para_retiro=self.cola_bicis_reparadas,
                tiempo_reparacion= self.mecanico.tiempo_reparacion ,
                tiempo_fin_reparacion= self.mecanico.tiempo_fin_reparacion,
                estado_mecanico=self.mecanico.estado,
                cola_mecanico=self.mecanico.cola_reparacion,
                tiempo_fin_limpieza= self.mecanico.tiempo_fin_limpieza,
                cont_retirar_bici= self.cont_retirar_bici,
                cont_retirar_bici_no_reparada= self.cont_retirar_bici_no_reparada,
                acum_tiempo_ocupacion_asistente = round(self.acum_tiempo_ocupacion_asistente,4),
                acum_tiempo_ocupacion_mecanico = round(self.acum_tiempo_ocupacion_mecanico,4)
            )
            
            # PARA ESTADISTICAS DE OCUPACION ANTES DE ITERAR ACUMULAMOS SI Y SOLO SI ESTAN OCUPADOS}
            tiempo_actual = vector_estado.reloj
            tiempo_anterior = self.vector_estado_anterior.reloj
            if self.mecanico.estado == Estado_Mecanico.OCUPADO.value:
                self.acum_tiempo_ocupacion_mecanico += round(tiempo_actual - tiempo_anterior,4)

            if self.asistente.estado == Estado_Asistente.OCUPADO.value:
                self.acum_tiempo_ocupacion_asistente += self.asistente.tiempo_atencion




            # SI EL RELOJ ESTA DENTRO DEL RANGO INDICADO POR EL USUARIO Y NO NOS EXCEDIMOS DE LA CANTIDAD DE ITERACIONES QUE DEFINIO AGREGAMOS EL NUEVO VECTOR ESTADO A LA LISTA PARA MOSTRAR
            # ! POR EL MOMENTO PARA DEBUG SE AGREGAN TODAS
            #if reloj >= self.HORA_OBSERVAR and self.CANT_ITERACIONES > 0:
            #    self.array_vector_estado_mostrar.append(vector_estado)
            #    self.CANT_ITERACIONES -= 1

            # ! BORRAR DESPUES:
            self.array_vector_estado_mostrar.append(vector_estado)

            # FINALMENTE SUMAMOS UNA ITERACION Y ACTUALIZAMOS EL VECTOR ESTADO
            cant_iteraciones += 1
            self.vector_estado_anterior = vector_estado

        # TAMBIEN NOS PIDEN LA ULTIMA FILA DE LA SIMULACION ASI QUE AL SALIR DEL CICLO AGREGAMOS EL ULTIMO VECTOR GENERADO
        self.array_vector_estado_mostrar.append(self.vector_estado_anterior)
        return self.array_vector_estado_mostrar