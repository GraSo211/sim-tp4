from enum import Enum

class Evento(Enum):
    INIT = "INICIALIZACION"
    LC= "LLEGADA_CLIENTE"
    FA = "FIN_ATENCION_CLIENTE"
    FR = "FIN_REPARACION"
    FL = "FIN_LIMPIEZA"