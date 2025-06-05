import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont


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


class Vista(tk.Tk):
    def __init__(
        self,
    ):
        super().__init__()
        self.title("SIMULACIÓN TP4 - GRUPO 6")
        self.geometry("1280x720")
        self.configure(bg=BG_COLOR)
        self._crear_widgets()

    def callback_iniciar_simulacion(self, callback):
        self._callback_iniciar_simulacion = callback

    def _accion_iniciar_simulacion(self):
        if self._callback_iniciar_simulacion:
            self._callback_iniciar_simulacion()

        # Ocultar los inputs y el botón
        self.frame_sim.pack_forget()
        self.frame_btn.pack_forget()

        # Mostrar tabla en su lugar
        self.frame_vector_estado.pack(fill="both", expand=True, pady=10, padx=10)

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

        self.tiempo_duracion = tk.Entry(
            self.frame_sim,
            font=FONT_ENTRY,
            width=30,
        )
        self.tiempo_duracion.grid(row=0, column=1, padx=10, pady=5)

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
        self.frame_btn = tk.Frame(self, bg=BG_COLOR)
        self.frame_btn.pack(pady=20)

        btn_iniciar_sim = tk.Button(
            self.frame_btn,
            text="Iniciar simulación",
            font=FONT_LABEL,
            bg=BTN_COLOR,
            fg=BTN_TEXT_COLOR,
            command=self._accion_iniciar_simulacion,
            padx=20,
            pady=10,
        )
        btn_iniciar_sim.pack()

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

        # Frame para mostrar vector_estado debajo de inputs
        self.frame_vector_estado = tk.Frame(self, bg=BG_COLOR)

        # Creamos el Treeview vacío inicialmente
        self.tree_vector_estado = ttk.Treeview(self.frame_vector_estado)
        self.tree_vector_estado.pack(fill="both", expand=True)


    def mostrar_vector_estado(self, lista_vectores_estado):
        # Limpiar frame por si ya hay un Treeview anterior
        for widget in self.frame_vector_estado.winfo_children():
            widget.destroy()

        # Scrollbars
        scroll_y = tk.Scrollbar(self.frame_vector_estado, orient="vertical")
        scroll_y.pack(side="right", fill="y")

        scroll_x = tk.Scrollbar(self.frame_vector_estado, orient="horizontal")
        scroll_x.pack(side="bottom", fill="x")

        # Treeview
        self.tree_vector_estado = ttk.Treeview(
            self.frame_vector_estado,
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set
        )
        self.tree_vector_estado.pack(fill="both", expand=True)

        # Vincular scrollbars al Treeview
        scroll_y.config(command=self.tree_vector_estado.yview)
        scroll_x.config(command=self.tree_vector_estado.xview)

        if not lista_vectores_estado:
            self.tree_vector_estado["columns"] = []
            return


        atributos = [
            "evento",
            "reloj",
            "tiempo_entre_llegadas",
            "hora_llegada",
            "motivo",
            "tiempo_atencion",
            "tiempo_fin_atencion",
            "estado_asistente",
            "cola_asistente",
            "cola_bicis_listas_para_retiro",
            "tiempo_reparacion",
            "tiempo_fin_reparacion",
            "estado_mecanico",
            "cola_mecanico",
            "tiempo_fin_limpieza",
            "cont_retirar_bici",
            "cont_retirar_bici_no_reparada",
            "acum_tiempo_ocupacion_asistente",
            "acum_tiempo_ocupacion_mecanico"
        ]


        self.tree_vector_estado["columns"] = atributos
        self.tree_vector_estado["show"] = "headings"

        for attr in atributos:
            self.tree_vector_estado.heading(attr, text=attr)
            self.tree_vector_estado.column(attr, anchor="center", width=150)  # ancho fijo

        for vector in lista_vectores_estado:
            valores = [getattr(vector, attr) for attr in atributos]
            self.tree_vector_estado.insert("", tk.END, values=valores)
