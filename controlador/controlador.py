class Controlador:
    def __init__(self,vista):
        self.vista = vista;
        self.vista.callback_iniciar_simulacion(self.iniciar_simulacion)

    def iniciar_simulacion(self):
        self.validar_tiempo()



        

    def validar_tiempo(self):

        try:
            tiempo_duracion =  int(self.vista.tiempo_duracion.get() )
            if(tiempo_duracion > 100000 ):
                self.vista.tiempo_error["text"] = "El tiempo debe ser menor o igual a 100.000 minutos."
                return
        
        except:
            self.vista.tiempo_error["text"] = "El tiempo debe ser un numero menor o igual a 100.000 minutos."


    def validar_hora(self):
        hora_observar = int(self.vista)

    def validar_iteraciones():
        pass