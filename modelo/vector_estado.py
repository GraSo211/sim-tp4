from modelo.evento import Evento
from modelo.servidor.estado_asistente import Estado as Estado_Servidor
from modelo.cliente.motivo_cliente import Motivo_Cliente
from modelo.cliente.estado_cliente import Estado_Cliente
from modelo.cliente.cliente import Cliente
from typing import List

class Vector_Estado:
    def __init__(
        self,
        evento: Evento,
        reloj: float,
        rnd_tell:float,
        tiempo_entre_llegadas: float,
        hora_llegada: float,
        rnd_m:float,
        motivo: Motivo_Cliente,
        rnd_ta:float,
        tiempo_atencion: float,
        tiempo_fin_atencion: float,
        estado_cliente: Estado_Cliente,
        estado_asistente: Estado_Servidor,
        cola_asistente: int,
        cola_bicis_listas_para_retiro: int,
        rnd_tr:float,
        tiempo_reparacion: float,
        tiempo_fin_reparacion: float,
        estado_mecanico: Estado_Servidor,
        cola_mecanico: int,
        tiempo_fin_limpieza: float,
        cont_retirar_bici: int,
        cont_retirar_bici_no_reparada: int,
        acum_tiempo_ocupacion_asistente: float,
        acum_tiempo_ocupacion_mecanico: float,
        cliente : Cliente,
        cola_eventos,
        clientes_en_cola: List[Cliente]
    ):
        self.evento: Evento = evento
        self.reloj: float = reloj
        self.rnd_tell:float = rnd_tell
        self.tiempo_entre_llegadas: float = tiempo_entre_llegadas
        self.hora_llegada: float = hora_llegada
        self.rnd_m: float = rnd_m
        self.motivo: Motivo_Cliente = motivo
        self.rnd_ta: float = rnd_ta
        self.tiempo_atencion: float = tiempo_atencion
        self.tiempo_fin_atencion: float = tiempo_fin_atencion
        self.estado_cliente: Estado_Cliente = estado_cliente
        self.estado_asistente: Estado_Servidor = estado_asistente
        self.cola_asistente: int = cola_asistente
        self.cola_bicis_listas_para_retiro: int = cola_bicis_listas_para_retiro
        self.rnd_tr:float = rnd_tr
        self.tiempo_reparacion: float = tiempo_reparacion
        self.tiempo_fin_reparacion: float = tiempo_fin_reparacion
        self.estado_mecanico: Estado_Servidor = estado_mecanico
        self.cola_mecanico: int = cola_mecanico
        self.tiempo_fin_limpieza: float = tiempo_fin_limpieza
        self.cont_retirar_bici = cont_retirar_bici
        self.cont_retirar_bici_no_reparada = cont_retirar_bici_no_reparada
        self.acum_tiempo_ocupacion_asistente = acum_tiempo_ocupacion_asistente
        self.acum_tiempo_ocupacion_mecanico = acum_tiempo_ocupacion_mecanico
        self.cliente: Cliente = cliente
        self.cola_eventos = cola_eventos
        self.clientes_en_cola: List[Cliente] = clientes_en_cola
    
    def __str__(self):
    

        return (
            f"Evento: {self.evento}\n"
            f"Reloj: {self.reloj}\n"
            f"Tiempo entre llegadas: {self.tiempo_entre_llegadas}\n"
            f"Hora llegada: {self.hora_llegada}\n"
            f"Motivo: {self.motivo}\n"
            f"Tiempo atención: {self.tiempo_atencion}\n"
            f"Tiempo fin atención: {self.tiempo_fin_atencion}\n"
            f"Estado asistente: {self.estado_asistente}\n"
            f"Cola bicis listas para retiro: {self.cola_bicis_listas_para_retiro}\n"
            f"Tiempo reparación: {self.tiempo_reparacion}\n"
            f"Tiempo fin reparación: {self.tiempo_fin_reparacion}\n"
            f"Estado mecánico: {self.estado_mecanico}\n"
            f"Cola mecánico: {self.cola_mecanico}\n"
            f"Tiempo fin limpieza: {self.tiempo_fin_limpieza}\n"
            f"Cola asistente: {self.cola_asistente}\n"
            f"Estado cliente: {self.estado_cliente}\n"
            f"Contador retirar bicicleta: {self.cont_retirar_bici}\n"
            f"Contador retirar bicicleta NO reparada: {self.cont_retirar_bici_no_reparada}\n"
            f"Acumulado ocupación asistente: {self.acum_tiempo_ocupacion_asistente}\n"
            f"Acumulado ocupación mecánico: {self.acum_tiempo_ocupacion_mecanico}\n"
            f"Cliente:\n{self.cliente}"
            f"COLA_EVENTOS: {self.cola_eventos}"
        )
