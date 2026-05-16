import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from base_datos.repositorio_persona import (RepositorioPersona)

from servicios.benchmark_servicio import (ServicioBenchmark)

from servicios.complejidad_servicio import (ServicioComplejidad)

from servicios.exportacion_excel_servicio import (ServicioExportarExcel)


class VentanaPrincipal:

    def __init__(self):

        self.ventana = tk.Tk()

        self.ventana.title("Sistema de Ordenamiento")

        self.ventana.geometry("650x500")

        self.ventana.resizable(False, False)

        # Datos cargados
        self.personas = []

        self.personas_ordenadas = []

        # Servicios
        self.repositorio = (RepositorioPersona())

        self.servicio_benchmark = (ServicioBenchmark())

        self.servicio_complejidad = (ServicioComplejidad())

        self.servicio_excel = (ServicioExportarExcel())

        self.crear_componentes()

    def crear_componentes(self):

        titulo = tk.Label(
            self.ventana,
            text=(
                "SISTEMA DE "
                "ORDENAMIENTO "
                "DE PERSONAS"
            ),
            font=("Arial", 18, "bold")
        )

        titulo.pack(pady=15)

        # Botón cargar datos
        boton_cargar = tk.Button(
            self.ventana,
            text="Cargar Datos",
            width=20,
            command=self.cargar_datos
        )

        boton_cargar.pack()

        # Estado
        self.label_estado = tk.Label(
            self.ventana,
            text=(
                "Datos cargados: "
                "0 registros"
            ),
            font=("Arial", 11)
        )

        self.label_estado.pack(pady=10)

        # Criterio
        label_criterio = tk.Label(self.ventana, text="Ordenar por:")

        label_criterio.pack()

        self.combo_criterio = (
            ttk.Combobox(
                self.ventana,
                state="readonly",
                values=[
                    "nombre",
                    "edad",
                    "puntaje_evaluacion"
                ]
            )
        )

        self.combo_criterio.current(0)

        self.combo_criterio.pack(pady=5)

        # Título algoritmos
        label_algoritmos = tk.Label(
            self.ventana,
            text="ALGORITMOS",
            font=(
                "Arial",
                14,
                "bold"
            )
        )

        label_algoritmos.pack(pady=10)

        # Botones algoritmos
        boton_bubble = tk.Button(
            self.ventana,
            text="Bubble Sort",
            width=20,
            command=lambda:
            self.ejecutar_algoritmo(
                "bubble"
            )
        )

        boton_bubble.pack(pady=5)

        boton_insertion = tk.Button(
            self.ventana,
            text="Insertion Sort",
            width=20,
            command=lambda:
            self.ejecutar_algoritmo(
                "insertion"
            )
        )

        boton_insertion.pack(pady=5)

        boton_selection = tk.Button(
            self.ventana,
            text="Selection Sort",
            width=20,
            command=lambda:
            self.ejecutar_algoritmo(
                "selection"
            )
        )

        boton_selection.pack(pady=5)

        # Tiempo
        self.label_tiempo = (
            tk.Label(
                self.ventana,
                text=(
                    "Tiempo de "
                    "ejecución: "
                    "0 segundos"
                ),
                font=("Arial", 11)
            )
        )

        self.label_tiempo.pack(pady=15)

        # Complejidad
        self.label_big_o = (tk.Label(self.ventana, text="Big O: -"))

        self.label_big_o.pack()

        self.label_big_theta = (tk.Label(self.ventana, text="Big Θ: -"))

        self.label_big_theta.pack()

        self.label_big_omega = (tk.Label(self.ventana, text="Big Ω: -"))

        self.label_big_omega.pack()

        # Exportar
        boton_exportar = (
            tk.Button(
                self.ventana,
                text="Exportar Excel",
                width=20,
                command=self.exportar_excel
            )
        )

        boton_exportar.pack(pady=15)

        # Salir
        boton_salir = tk.Button(
            self.ventana,
            text="Salir",
            width=20,
            command=self.ventana.quit
        )

        boton_salir.pack()

    def cargar_datos(self):

        self.personas = (self.repositorio.obtener_todas_las_personas())

        total = len(self.personas)

        self.label_estado.config(
            text=(
                f"Datos cargados: "
                f"{total} registros"
            )
        )

        messagebox.showinfo(
            "Éxito",
            (
                "Datos cargados "
                "correctamente."
            )
        )

    def ejecutar_algoritmo(self, algoritmo):

        if not self.personas:

            messagebox.showwarning(
                "Advertencia",
                (
                    "Debe cargar "
                    "los datos primero."
                )
            )

            return

        criterio = (self.combo_criterio.get())

        (self.personas_ordenadas, tiempo) = (
            self.servicio_benchmark.ejecutar_ordenamiento(
                self.personas, algoritmo, criterio))

        complejidad = (self.servicio_complejidad.obtener_complejidad(algoritmo))

        self.label_tiempo.config(
            text=(
                f"Tiempo de "
                f"ejecución: "
                f"{tiempo:.5f} "
                f"segundos"
            )
        )

        self.label_big_o.config(
            text=(
                f"Big O: "
                f"{complejidad['big_o']}"
            )
        )

        self.label_big_theta.config(
            text=(
                f"Big Θ: "
                f"{complejidad['big_theta']}"
            )
        )

        self.label_big_omega.config(
            text=(
                f"Big Ω: "
                f"{complejidad['big_omega']}"
            )
        )

        messagebox.showinfo("Éxito", "Ordenamiento completado.")

    def exportar_excel(self):

        if not self.personas_ordenadas:

            messagebox.showwarning(
                "Advertencia",
                (
                    "Primero debe "
                    "ordenar los datos."
                )
            )

            return

        ruta = (self.servicio_excel.exportar(self.personas_ordenadas))

        messagebox.showinfo(
            "Éxito",
            (
                f"Archivo exportado:\n"
                f"{ruta}"
            )
        )

    def ejecutar(self):

        self.ventana.mainloop()