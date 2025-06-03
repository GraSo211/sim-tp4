class Controlador:
    def __init__(self, vista):
        self.vista = vista
        self.vista.callback_iniciar_simulacion(self.iniciar_simulacion)

    def iniciar_simulacion(self):
        [res, status] = self.validar_tiempo()
        if not status:
            error = res
        else:
            tiempo_duracion = res

        if not status:
            self.vista.tiempo_error["text"] = error
            return

        [res, status] = self.validar_hora(tiempo_duracion)
        if not status:
            error = res
        else:
            hora_observar = res

        if not status:
            self.vista.tiempo_error["text"] = error
            return

        [res, status] = self.validar_iteraciones()
        if not status:
            error = res
        else:
            cant_iteraciones = res

        if not status:
            self.vista.tiempo_error["text"] = error
            return

    def validar_tiempo(self):
        status = False
        res = None
        try:
            tiempo_duracion = int(self.vista.tiempo_duracion.get())
            if tiempo_duracion <= 0:
                res = "El tiempo debe ser un número positivo."
                return res, status
            else:
                res = tiempo_duracion
                status = True
                return res, status

        except:
            res = "El tiempo debe ser un número positivo."
            return res, status

    def validar_hora(self, tiempo_x):
        status = False
        res = None
        try:
            hora_observar = int(self.vista.hora_observar.get())
            if hora_observar < 0 or hora_observar > tiempo_x:
                res = "La hora a partir de la cual quiere observar debe ser un número positivo y menor al tiempo X."
                return res, status
            else:
                res = hora_observar
                status = True
                return res, status

        except:
            res = "La hora a partir de la cual quiere observar debe ser un número positivo y menor al tiempo X."
            return res, status

    def validar_iteraciones(self):
        status = False
        res = None
        try:
            cant_iteraciones = int(self.vista.cant_iteraciones.get())
            if cant_iteraciones < 0:
                res = "La cantidad de iteraciones debe ser un número positivo."
                return res, status
            else:
                res = cant_iteraciones
                status = True
                return res, status

        except:
            res = "La cantidad de iteraciones debe ser un número positivo."
            return res, status
