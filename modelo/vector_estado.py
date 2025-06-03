from modelo.evento import Evento
from modelo.servidor.estado import Estado as Estado_Servidor
from modelo.cliente.motivo_cliente import Motivo_Cliente
from modelo.cliente.estado_cliente import Estado_Cliente


class Vector_Estado:
    def __init__(
        self,
        evento: Evento,
        reloj: float,
        tiempo_entre_llegadas: float,
        hora_llegada: float,
        motivo: Motivo_Cliente,
        tiempo_atencion: float,
        tiempo_fin_atencion: float,
        estado_cliente: Estado_Cliente,
        estado_asistente: Estado_Servidor,
        cola_asistente: int,
        cola_bicis_listas_para_retiro:int,
        tiempo_reparacion:float,
        tiempo_fin_reparacion: float,
        estado_mecanico: Estado_Servidor,
        cola_mecanico:int,
        tiempo_fin_limpieza:float

    ):
        self.evento: Evento = evento
        self.reloj: float = reloj
        self.tiempo_entre_llegadas:float = tiempo_entre_llegadas
        self.hora_llegada:float = hora_llegada
        self.motivo: Motivo_Cliente = motivo
        self.tiempo_atencion: float = tiempo_atencion
        self.tiempo_fin_atencion:float = tiempo_fin_atencion
        self.estado_cliente: Estado_Cliente = estado_cliente
        self.estado_asistente: Estado_Servidor = estado_asistente
        self.cola_asistente: int = cola_asistente
        self.cola_bicis_listas_para_retiro: int = cola_bicis_listas_para_retiro
        self.tiempo_reparacion: float = tiempo_reparacion
        self.tiempo_fin_reparacion: float = tiempo_fin_reparacion
        self.estado_mecanico: Estado_Servidor = estado_mecanico
        self.cola_mecanico: int = cola_mecanico
        self.tiempo_fin_limpieza: float =  tiempo_fin_limpieza
        # todo agregar al vector estado los acumuladores
