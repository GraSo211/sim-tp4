import tkinter as tk

BG_COLOR = "#f5f5f5"
FONT_TITLE = ("Montserrat", 32, "bold")
FONT_LABEL = ("Montserrat", 18, "bold")
FONT_ENTRY = ("Montserrat", 16)
FONT_NOTE = ("Montserrat", 12, "bold")
FG_LABEL = "#333"
FG_NOTE = "gray"
FG_ERROR = "red"
BTN_COLOR = "#4CAF50"
BTN_TEXT_COLOR = "white"


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SIMULACIÓN TP4 - GRUPO 6")
        self.geometry("1280x720")
        self.configure(bg=BG_COLOR)
        self._crear_widgets()

    def _titulo_ventana(self):
        frame_titulo = tk.Frame(self, bg=BG_COLOR)
        frame_titulo.pack(fill="x", pady=20)

        titulo = tk.Label(
            frame_titulo,
            text="SIMULACIÓN TP4 - GRUPO 6",
            font=FONT_TITLE,
            bg=BG_COLOR,
            fg=FG_LABEL,
        )
        titulo.pack()

    def _tiempo_simulacion(self):
        tk.Label(
            self.frame_sim,
            text="Ingrese el tiempo (X) que durará la simulación:",
            font=FONT_LABEL,
            bg=BG_COLOR,
            fg=FG_LABEL,
        ).grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.tiempo_entry = tk.Entry(
            self.frame_sim,
            font=FONT_ENTRY,
            width=30,
        )
        self.tiempo_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(
            self.frame_sim,
            text=(
                "El tiempo debe estar en minutos.\n"
                "La simulación durará hasta cumplir con el tiempo indicado\n"
                "o hasta las 100.000 iteraciones, lo que ocurra primero."
            ),
            font=FONT_NOTE,
            bg=BG_COLOR,
            fg=FG_NOTE,
            justify="left",
        ).grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="w")

    def _iteraciones_hora(self):
        tk.Label(
            self.frame_sim,
            text="Ingrese el tiempo (J) a partir del cual quiere observar la simulación:",
            font=FONT_LABEL,
            bg=BG_COLOR,
            fg=FG_LABEL,
        ).grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.hora_observar = tk.Entry(
            self.frame_sim,
            font=FONT_ENTRY,
            width=30,
        )
        self.hora_observar.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(
            self.frame_sim,
            text="Ingrese la cantidad de iteraciones (I) que quiere observar:",
            font=FONT_LABEL,
            bg=BG_COLOR,
            fg=FG_LABEL,
        ).grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.cant_iteraciones = tk.Entry(
            self.frame_sim,
            font=FONT_ENTRY,
            width=30,
        )
        self.cant_iteraciones.grid(row=3, column=1, padx=10, pady=10)

    def _iniciar_simulacion(self):
        frame_btn = tk.Frame(self, bg=BG_COLOR)
        frame_btn.pack(pady=20)

        btn_iniciar_sim = tk.Button(
            frame_btn,
            text="Iniciar simulación",
            font=FONT_LABEL,
            bg=BTN_COLOR,
            fg=BTN_TEXT_COLOR,
            command=self._accion_iniciar_simulacion,
            padx=20,
            pady=10
        )
        btn_iniciar_sim.pack()

    def _accion_iniciar_simulacion(self):
        print("INICIAR SIMULACIÓN")
        

    def _crear_widgets(self):
        self._titulo_ventana()

        self.frame_sim = tk.Frame(self, bg=BG_COLOR)
        self.frame_sim.pack(pady=10)

        self._tiempo_simulacion()
        self._iteraciones_hora()

        # todo: Mensaje de error RECORDAR ACTUALIZAR EL GRID POR CADA ELEMENTO NUEVO AGREGADO
        self.tiempo_error = tk.Label(
            self.frame_sim,
            bg=BG_COLOR,
            text="",
            font=FONT_NOTE,
            fg=FG_ERROR,
        )
        self.tiempo_error.grid(row=4, column=0, columnspan=2, pady=5)

        self._iniciar_simulacion()


if __name__ == "__main__":
    app = App()
    app.mainloop()
