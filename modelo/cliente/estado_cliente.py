from enum import Enum

class Estado_Cliente(Enum):
    CREADO = "CREADO"
    SA = "SIENDO ATENDIDO"
    EA = "ESPERANDO ATENCION"