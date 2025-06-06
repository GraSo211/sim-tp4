import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont


BG_COLOR = "#f5f5f5"
FONT_TITLE = ("Montserrat", 32, "bold")
FONT_LABEL = ("Montserrat", 18, "bold")
FONT_MINI = ("Montserrat", 12, "bold")
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

        self.frame_vector_estado = tk.Frame(self, bg=BG_COLOR)

        # Creamos el Treeview vacío inicialmente
        self.tree_vector_estado = ttk.Treeview(self.frame_vector_estado)
        self.tree_vector_estado.pack(fill="both", expand=True)

    def mostrar_vector_estado(
        self,
        lista_vectores_estado,
        prob_cliente_retirar_bicicleta_no_disp,
        porc_ocup_mec,
        porc_ocup_asist,
    ):
        # Limpiar frame por si ya hay un Treeview anterior
        for widget in self.frame_vector_estado.winfo_children():
            widget.destroy()

        # === Crear frames para organizar verticalmente ===
        frame_superior = tk.Frame(self.frame_vector_estado)
        frame_superior.pack(fill=tk.BOTH, expand=True)

        frame_inferior = tk.Frame(self.frame_vector_estado)
        frame_inferior.pack(fill=tk.X)

        # Atributos del vector de estado
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
            "acum_tiempo_ocupacion_mecanico",
        ]

        columnas = atributos + ["id_cliente", "estado_cliente"]

        # Frame contenedor de tabla y scrollbars
        frame_tabla = tk.Frame(frame_superior)
        frame_tabla.pack(fill=tk.BOTH, expand=True)

        # Scrollbars
        scroll_y = tk.Scrollbar(frame_tabla, orient=tk.VERTICAL)
        scroll_x = tk.Scrollbar(frame_tabla, orient=tk.HORIZONTAL)

        # Treeview
        self.tree_vector_estado = ttk.Treeview(
            frame_tabla,
            columns=columnas,
            show="headings",
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set,
        )

        # Configurar scrollbars
        scroll_y.config(command=self.tree_vector_estado.yview)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        scroll_x.config(command=self.tree_vector_estado.xview)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

        # Configurar columnas
        for col in columnas:
            self.tree_vector_estado.heading(col, text=col)
            self.tree_vector_estado.column(col, anchor="center", width=150)

        self.tree_vector_estado.pack(fill=tk.BOTH, expand=True)

        # Insertar datos
        for vector in lista_vectores_estado:
            valores = [getattr(vector, attr) for attr in atributos]
            if vector.cliente:
                valores.append(vector.cliente.id)
                valores.append(vector.cliente.estado)
            else:
                valores.extend(["", ""])
            self.tree_vector_estado.insert("", tk.END, values=valores)

        # === Mostrar resultados debajo ===
        label_resultados = tk.Label(
            frame_inferior,
            text=(
                f"Probabilidad de falta de bicicletas reparadas al intentar retirarlas: {prob_cliente_retirar_bicicleta_no_disp:.2%}\n"
                f"  (cont_retirar_bici_no_reparada / cont_retirar_bici)\n\n"
                f"Ocupación del mecánico: {porc_ocup_mec:.2%}\n"
                f"  ((acum_tiempo_ocupacion_mecanico / reloj)*100)\n\n"
                f"Ocupación del asistente: {porc_ocup_asist:.2%}\n"
                f"  ((acum_tiempo_ocupacion_asistente / reloj)*100)"
            ),
            font=FONT_MINI,
            justify="center",
            anchor="center",
            padx=20,
            pady=10,
        )
        label_resultados.pack(pady=(10, 0), fill=tk.X, expand=True)

        # === Botón de reinicio debajo ===
        btn_reiniciar = tk.Button(
            frame_inferior,
            text="Reiniciar simulación",
            font=FONT_LABEL,
            bg="#f44336",
            fg=BTN_TEXT_COLOR,
            command=self._reiniciar_simulacion,
            padx=20,
            pady=10,
        )
        btn_reiniciar.pack(pady=20)

    def _reiniciar_simulacion(self):
        # MOSTRAMOS DE VUELTA LOS INPUTS Y EL BOTON INICIAR
        self.frame_sim.pack(pady=10)
        self.frame_btn.pack(pady=20)

        # OCULTAMOS LA TABLA
        self.frame_vector_estado.pack_forget()

        # PONEMOS EN 0 LOS CAMPOS
        self.tiempo_duracion.delete(0, tk.END)
        self.hora_observar.delete(0, tk.END)
        self.cant_iteraciones.delete(0, tk.END)
        self.tiempo_error.config(text="")
