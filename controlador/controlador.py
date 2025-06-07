from modelo.simulacion import Simulacion


class Controlador:
    def __init__(self, vista):
        self.vista = vista

        self.vista.callback_iniciar_simulacion(self.iniciar_simulacion)

    def validar_parametro(self, valor_raw, tipo=int, por_defecto=None, nombre_campo=""):
        valor_raw = valor_raw.strip() if valor_raw else ""
        if valor_raw == "":
            return por_defecto, True
        try:
            valor = tipo(valor_raw)
            return valor, True
        except ValueError:
            error_msg = f"El valor para {nombre_campo} debe ser un número válido."
            return error_msg, False

    def iniciar_simulacion(self):
        # Validar tiempo de simulación
        tiempo_duracion, ok = self.validar_parametro(
            self.vista.tiempo_duracion.get(), int, 1000, "Tiempo de simulación"
        )
        if not ok or tiempo_duracion <= 0:
            self.vista.tiempo_error["text"] = "El tiempo debe ser un número positivo."
            return

        # Validar hora a observar (debe ser >=0 y < tiempo_duracion)
        hora_observar_raw = self.vista.hora_observar.get()
        hora_observar, ok = self.validar_parametro(
            hora_observar_raw, int, 0, "Hora a observar"
        )
        if not ok or hora_observar < 0 or hora_observar >= tiempo_duracion:
            self.vista.tiempo_error["text"] = (
                "La hora a observar debe ser >= 0 y menor que el tiempo de simulación."
            )
            return

        # Validar cantidad de iteraciones
        cant_iteraciones, ok = self.validar_parametro(
            self.vista.cant_iteraciones.get(), int, 100000, "Cantidad de iteraciones"
        )
        if not ok or cant_iteraciones < 0:
            self.vista.tiempo_error["text"] = (
                "La cantidad de iteraciones debe ser un número positivo."
            )
            return

        # Validar parametros opcionales (con sus valores por defecto)
        evento_llc_val_a, ok = self.validar_parametro(
            self.vista.evento_llc_val_a.get(), int, 13, "evento_llc_val_a"
        )
        if not ok:
            self.vista.tiempo_error["text"] = evento_llc_val_a
            return

        evento_llc_val_b, ok = self.validar_parametro(
            self.vista.evento_llc_val_b.get(), int, 17, "evento_llc_val_b"
        )
        if not ok:
            self.vista.tiempo_error["text"] = evento_llc_val_b
            return

        motivo_ca_prob, ok = self.validar_parametro(
            self.vista.motivo_ca_prob.get(), int, 45, "motivo_ca_prob"
        )
        if not ok:
            self.vista.tiempo_error["text"] = motivo_ca_prob
            return

        motivo_ebr_prob, ok = self.validar_parametro(
            self.vista.motivo_ebr_prob.get(), int, 25, "motivo_ebr_prob"
        )
        if not ok:
            self.vista.tiempo_error["text"] = motivo_ebr_prob
            return

        motivo_rbr_prob, ok = self.validar_parametro(
            self.vista.motivo_rbr_prob.get(), int, 30, "motivo_rbr_prob"
        )
        if not ok:
            self.vista.tiempo_error["text"] = motivo_rbr_prob
            return

        evento_motivo_ca_val_a, ok = self.validar_parametro(
            self.vista.evento_motivo_ca_val_a.get(), int, 6, "evento_motivo_ca_val_a"
        )
        if not ok:
            self.vista.tiempo_error["text"] = evento_motivo_ca_val_a
            return

        evento_motivo_ca_val_b, ok = self.validar_parametro(
            self.vista.evento_motivo_ca_val_b.get(), int, 10, "evento_motivo_ca_val_b"
        )
        if not ok:
            self.vista.tiempo_error["text"] = evento_motivo_ca_val_b
            return

        evento_rep_val_a, ok = self.validar_parametro(
            self.vista.evento_rep_val_a.get(), int, 18, "evento_rep_val_a"
        )
        if not ok:
            self.vista.tiempo_error["text"] = evento_rep_val_a
            return

        evento_rep_val_b, ok = self.validar_parametro(
            self.vista.evento_rep_val_b.get(), int, 22, "evento_rep_val_b"
        )
        if not ok:
            self.vista.tiempo_error["text"] = evento_rep_val_b
            return

        evento_limpieza_val, ok = self.validar_parametro(
            self.vista.evento_limpieza_val.get(), int, 5, "evento_limpieza_val"
        )
        if not ok:
            self.vista.tiempo_error["text"] = evento_limpieza_val
            return

        # Ya todo validado y limpio, crear simulación

        print(
            f"""
            TIEMPO_SIMULACION = {tiempo_duracion}
            HORA_OBSERVAR = {hora_observar}
            CANT_ITERACIONES = {cant_iteraciones}
            evento_llc_val_a = {evento_llc_val_a}
            evento_llc_val_b = {evento_llc_val_b}
            motivo_ca_prob = {motivo_ca_prob}
            motivo_ebr_prob = {motivo_ebr_prob}
            motivo_rbr_prob = {motivo_rbr_prob}
            evento_motivo_ca_val_a = {evento_motivo_ca_val_a}
            evento_motivo_ca_val_b = {evento_motivo_ca_val_b}
            evento_rep_val_a = {evento_rep_val_a}
            evento_rep_val_b = {evento_rep_val_b}
            evento_limpieza_val = {evento_limpieza_val}
            """
        )

        self.modelo = Simulacion(
            TIEMPO_SIMULACION=tiempo_duracion,
            HORA_OBSERVAR=hora_observar,
            CANT_ITERACIONES=cant_iteraciones,
            evento_llc_val_a=evento_llc_val_a,
            evento_llc_val_b=evento_llc_val_b,
            motivo_ca_prob=motivo_ca_prob,
            motivo_ebr_prob=motivo_ebr_prob,
            motivo_rbr_prob=motivo_rbr_prob,
            evento_motivo_ca_val_a=evento_motivo_ca_val_a,
            evento_motivo_ca_val_b=evento_motivo_ca_val_b,
            evento_rep_val_a=evento_rep_val_a,
            evento_rep_val_b=evento_rep_val_b,
            evento_limpieza_val=evento_limpieza_val,
        )

        (
            array_vector_estado,
            prob_cliente_retirar_bicicleta_no_disp,
            porc_ocup_mec,
            porc_ocup_asist,
        ) = self.modelo.simular_taller_bicicletas()
        self.vista.mostrar_vector_estado(
            array_vector_estado,
            prob_cliente_retirar_bicicleta_no_disp,
            porc_ocup_mec,
            porc_ocup_asist,
        )

    def validar_tiempo(self):
        valor_raw = self.vista.tiempo_duracion.get().strip()
        if valor_raw == "":
            return 1000, True  # valor por defecto

        try:
            tiempo_duracion = int(valor_raw)
            if tiempo_duracion <= 0:
                return "El tiempo debe ser un número positivo.", False
            return tiempo_duracion, True
        except ValueError:
            return "El tiempo debe ser un número positivo.", False

    def validar_hora(self, tiempo_x):
        valor_raw = self.vista.hora_observar.get().strip()
        if valor_raw == "":
            return 0, True  # valor por defecto

        try:
            hora_observar = int(valor_raw)
            if hora_observar < 0 or hora_observar >= tiempo_x:
                return (
                    "La hora a partir de la cual quiere observar debe ser un número positivo y menor al tiempo X.",
                    False,
                )
            return hora_observar, True
        except ValueError:
            return (
                "La hora a partir de la cual quiere observar debe ser un número positivo y menor al tiempo X.",
                False,
            )

    def validar_iteraciones(self):
        valor_raw = self.vista.cant_iteraciones.get().strip()
        if valor_raw == "":
            return 100, True  # valor por defecto

        try:
            cant_iteraciones = int(valor_raw)
            if cant_iteraciones < 0:
                return "La cantidad de iteraciones debe ser un número positivo.", False
            return cant_iteraciones, True
        except ValueError:
            return "La cantidad de iteraciones debe ser un número positivo.", False
