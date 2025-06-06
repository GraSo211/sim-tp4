from modelo.servidor.estado_mecanico import Estado
import random


class Mecanico:
    def __init__(self, evento_rep_val_a, evento_rep_val_b, evento_limpieza_val):
        self.estado: Estado = Estado.LIBRE.value
        self.tiempo_limpieza: float = evento_limpieza_val
        self.cola_reparacion = 0
        self.rnd_tr = 0.0
        self.tiempo_reparacion = 0.0
        self.tiempo_fin_limpieza: float = 0.0
        self.tiempo_fin_reparacion: float = 0.0
        self.evento_rep_val_a = evento_rep_val_a
        self.evento_rep_val_b = evento_rep_val_b

    # EL MECANICO TIENE 3 OPCIONES:
    # ESTAR LIBRE
    # ESTAR OCUPADO REPARANDO UNA BICICLETA
    # ESTAR LIMPIANDO SU ZONA DE TRABAJO

    # ORIGINALMENTE ESTA LIBRE, CUANDO LLEGA UNA BICICLETA A REPARAR
    # SE OCUPA REPARANDO, Y CUANDO TERMINA LIMPIA SU ZONA DE TRABAJO SIN IMPORTAR SI HAY BICIS EN LA COLA DE REPARACION
    # AL FINALIZAR LA LIMPIEZA VUELVE A ESTAR LIBRE U OCUPADO REPARANDO OTRA BICICLETA

    def evento_reparacion(self, reloj: float):
        # EL REPARAR BICICLETAS LE LLEVA ENTRE 18 Y 22 MINUTOS UNIFORMES
        if self.estado == Estado.LIBRE.value:
            self.estado = Estado.OCUPADO.value
            self.rnd_tr = round(random.random(),4)
            rand_uniforme = round((self.evento_rep_val_a+(self.evento_rep_val_b-self.evento_rep_val_a)*self.rnd_tr), 4)
            self.tiempo_reparacion = rand_uniforme
            self.tiempo_fin_reparacion = round(reloj + self.tiempo_reparacion, 4)
        # SI ESTA REPARANDO Y LLEGA UNA NUEVA BICICLETA, SE AUMENTA LA COLA DE REPARACION
        else:
            self.cola_reparacion += 1

    def evento_fin_reparacion(self, reloj: float):
        # AL FINALIZAR LA  REPARACION, EL MECANICO LIMPIA SU ZONA DE TRABAJO
        self.estado = Estado.LIMPIANDO.value
        self.tiempo_fin_limpieza = round(self.tiempo_limpieza + reloj, 4)

    def evento_finalizar_limpieza(self, reloj: float):
        # AL FINALIZAR LA LIMPIEZA, SI HAY BICIS EN LA COLA DE REPARACION, SE OCUPA REPARANDO OTRA
        if self.cola_reparacion > 0:
            self.estado = Estado.OCUPADO.value
            self.cola_reparacion -= 1
            self.rnd_tr = round(random.random(),4)
            rand_uniforme = round((self.evento_rep_val_a+(self.evento_rep_val_b-self.evento_rep_val_a)*self.rnd_tr), 4)
            self.tiempo_reparacion = rand_uniforme
            self.tiempo_fin_reparacion = round(reloj + self.tiempo_reparacion, 4)

        # SI NO HAY BICIS EN LA COLA DE REPARACION, VUELVE A ESTAR LIBRE
        else:
            self.estado = Estado.LIBRE.value
