"""
complexity_plotter.py
---------------------

Módulo responsable de generar representaciones gráficas de complejidad
algorítmica a partir de la clasificación realizada por la Red Neuronal
Multicapa (MLP).

La finalidad de este componente es proporcionar una visualización intuitiva
del crecimiento temporal estimado de un algoritmo, permitiendo al usuario
comprender fácilmente el comportamiento de la complejidad predicha.

Las gráficas generadas son exportadas en formato PNG y pueden ser enviadas
directamente a través de:

- Bots de Telegram.
- APIs REST.
- Aplicaciones Web.
- Sistemas de Reportes.
- Herramientas académicas.

Complejidades soportadas:
-------------------------

O(1)       → Constante
O(log n)   → Logarítmica
O(n)       → Lineal
O(n log n) → Linealítmica
O(n²)      → Cuadrática
O(n³)      → Cúbica
O(2^n)     → Exponencial

Autores:
    - Cristian Cortes
    - Katherine Arboleda

Proyecto:
    Clasificador Inteligente de Complejidad Algorítmica
    mediante Redes Neuronales Multicapa (MLP)

Universidad del Valle
Análisis y Diseño de Algoritmos
"""

# ============================================================================
# IMPORTACIONES
# ============================================================================

# Permite almacenar la imagen en memoria sin crear archivos físicos.
import io

# Biblioteca para operaciones matemáticas y generación de curvas.
import numpy as np

# Backend sin interfaz gráfica.
# Obligatorio para servidores Linux, Docker y FastAPI.
import matplotlib

matplotlib.use("Agg")

# Biblioteca principal para generar gráficas.
import matplotlib.pyplot as plt

# Permite crear elementos personalizados para la leyenda.
import matplotlib.patches as mpatches


# ============================================================================
# CONFIGURACIÓN DE COMPLEJIDADES
# ============================================================================
#
# Cada entrada define:
#
# - Función matemática
# - Etiqueta descriptiva
# - Color principal
# - Color de relleno
#
# Estas configuraciones permiten generar automáticamente
# las curvas de complejidad.
#

COMPLEXITY_CONFIG = {

    "O(1)": {

        # Complejidad constante
        "fn": lambda n: np.ones_like(n),

        "label":
        "O(1) — Constante",

        "color":
        "#2ecc71",

        "fill":
        "#2ecc7122",
    },

    "O(log n)": {

        # Complejidad logarítmica
        "fn": lambda n: np.log2(
            np.maximum(n, 1)
        ),

        "label":
        "O(log n) — Logarítmica",

        "color":
        "#27ae60",

        "fill":
        "#27ae6022",
    },

    "O(n)": {

        # Complejidad lineal
        "fn": lambda n: n,

        "label":
        "O(n) — Lineal",

        "color":
        "#f39c12",

        "fill":
        "#f39c1222",
    },

    "O(n log n)": {

        # Complejidad linealítmica
        "fn": lambda n: (
            n * np.log2(
                np.maximum(n, 1)
            )
        ),

        "label":
        "O(n log n) — Linealítmica",

        "color":
        "#e67e22",

        "fill":
        "#e67e2222",
    },

    "O(n²)": {

        # Complejidad cuadrática
        "fn": lambda n: n ** 2,

        "label":
        "O(n²) — Cuadrática",

        "color":
        "#e74c3c",

        "fill":
        "#e74c3c22",
    },

    "O(n³)": {

        # Complejidad cúbica
        "fn": lambda n: n ** 3,

        "label":
        "O(n³) — Cúbica",

        "color":
        "#c0392b",

        "fill":
        "#c0392b22",
    },

    "O(2^n)": {

        # Complejidad exponencial
        "fn": lambda n: 2 ** n,

        "label":
        "O(2^n) — Exponencial",

        "color":
        "#8e44ad",

        "fill":
        "#8e44ad22",
    },
}


# ============================================================================
# ORDEN DE COMPLEJIDADES
# ============================================================================
#
# Define el orden de visualización de las curvas
# en el panel comparativo.
#

COMPLEXITY_ORDER = [

    "O(1)",
    "O(log n)",
    "O(n)",
    "O(n log n)",
    "O(n²)",
    "O(n³)",
    "O(2^n)"
]


# ============================================================================
# LÍMITES DEL EJE Y
# ============================================================================
#
# Cada complejidad crece a velocidades distintas.
#
# Estos límites evitan que la gráfica se deforme
# y mantienen una visualización legible.
#

Y_LIMITS = {

    "O(1)": (0, 5),

    "O(log n)": (0, 12),

    "O(n)": (0, 110),

    "O(n log n)": (0, 800),

    "O(n²)": (0, 12000),

    "O(n³)": (0, 1_200_000),

    "O(2^n)": (0, 1200),
}


# ============================================================================
# GENERADOR DE GRÁFICAS
# ============================================================================

def generate_complexity_plot(
    complexity: str
) -> bytes:
    """
    Genera una imagen PNG en memoria que representa la complejidad
    algorítmica detectada por el clasificador MLP.

    Parámetros
    ----------
    complexity : str

        Complejidad detectada.

        Ejemplos:

            O(1)
            O(log n)
            O(n)
            O(n log n)
            O(n²)
            O(n³)
            O(2^n)

    Retorna
    --------
    bytes

        Imagen PNG lista para enviar por:

        - Telegram Bot API
        - FastAPI
        - HTTP Responses
        - Web Applications

    Complejidad Temporal
    --------------------

    O(n)

    Complejidad Espacial
    --------------------

    O(n)
    """

    # ---------------------------------------------------------------------
    # Validación de complejidad
    # ---------------------------------------------------------------------

    if complexity not in COMPLEXITY_CONFIG:

        complexity = "O(n)"

    config = COMPLEXITY_CONFIG[
        complexity
    ]

    y_limits = Y_LIMITS.get(
        complexity,
        (0, 1000)
    )

    # ---------------------------------------------------------------------
    # Generación del dominio n
    # ---------------------------------------------------------------------

    if complexity == "O(2^n)":

        n = np.linspace(
            1,
            10,
            300
        )

    elif complexity == "O(n³)":

        n = np.linspace(
            1,
            100,
            300
        )

    else:

        n = np.linspace(
            1,
            100,
            300
        )

    # ---------------------------------------------------------------------
    # Creación de la figura
    # ---------------------------------------------------------------------

    fig, (
        ax_main,
        ax_compare
    ) = plt.subplots(

        1,
        2,

        figsize=(12, 5),

        facecolor="#1a1a2e"
    )

    # ---------------------------------------------------------------------
    # Configuración visual global
    # ---------------------------------------------------------------------

    for ax in (
        ax_main,
        ax_compare
    ):

        ax.set_facecolor(
            "#16213e"
        )

        ax.tick_params(
            colors="#aaaaaa",
            labelsize=9
        )

        ax.spines[:].set_color(
            "#333366"
        )

        ax.xaxis.label.set_color(
            "#aaaaaa"
        )

        ax.yaxis.label.set_color(
            "#aaaaaa"
        )

    # =====================================================================
    # PANEL PRINCIPAL
    # =====================================================================

    y = config["fn"](n)

    y_clipped = np.clip(
        y,
        0,
        y_limits[1] * 1.05
    )

    ax_main.plot(

        n,
        y_clipped,

        color=config["color"],

        linewidth=3,

        zorder=5
    )

    ax_main.fill_between(

        n,
        y_clipped,

        alpha=0.15,

        color=config["color"]
    )

    ax_main.set_title(

        f"Complejidad: {complexity}",

        color="white",

        fontsize=14,

        fontweight="bold",

        pad=12
    )

    ax_main.set_xlabel(
        "Tamaño de entrada (n)"
    )

    ax_main.set_ylabel(
        "Operaciones"
    )

    ax_main.set_xlim(
        1,
        n[-1]
    )

    ax_main.set_ylim(
        y_limits
    )

    # ---------------------------------------------------------------------
    # Anotación descriptiva
    # ---------------------------------------------------------------------

    mid = len(n) // 2

    ax_main.annotate(

        config["label"],

        xy=(
            n[mid],
            y_clipped[mid]
        ),

        xytext=(
            n[mid] * 0.4,
            y_limits[1] * 0.8
        ),

        color=config["color"],

        fontsize=9,

        fontweight="bold",

        arrowprops=dict(
            arrowstyle="->",
            color=config["color"],
            lw=1.5
        )
    )

    ax_main.grid(

        True,

        color="#333366",

        linestyle="--",

        alpha=0.4
    )

    # =====================================================================
    # PANEL COMPARATIVO
    # =====================================================================

    n_compare = np.linspace(
        1,
        20,
        200
    )

    legend_patches = []

    for key in COMPLEXITY_ORDER:

        cfg = COMPLEXITY_CONFIG[
            key
        ]

        y_cmp = cfg["fn"](
            n_compare
        )

        is_selected = (
            key == complexity
        )

        lw = (
            3.5
            if is_selected
            else 1.2
        )

        alpha = (
            1.0
            if is_selected
            else 0.4
        )

        zorder = (
            10
            if is_selected
            else 2
        )

        y_cmp_clipped = np.clip(
            y_cmp,
            0,
            500
        )

        ax_compare.plot(

            n_compare,
            y_cmp_clipped,

            color=cfg["color"],

            linewidth=lw,

            alpha=alpha,

            zorder=zorder,

            linestyle="-"
            if is_selected
            else "--"
        )

        patch = mpatches.Patch(

            color=cfg["color"],

            label=cfg["label"],

            alpha=(
                1.0
                if is_selected
                else 0.5
            )
        )

        legend_patches.append(
            patch
        )

    ax_compare.set_title(

        "Comparativa de complejidades",

        color="white",

        fontsize=12,

        fontweight="bold",

        pad=12
    )

    ax_compare.set_xlabel(
        "Tamaño de entrada (n)"
    )

    ax_compare.set_ylabel(
        "Operaciones (escala relativa)"
    )

    ax_compare.set_xlim(
        1,
        20
    )

    ax_compare.set_ylim(
        0,
        500
    )

    ax_compare.grid(

        True,

        color="#333366",

        linestyle="--",

        alpha=0.4
    )

    ax_compare.legend(

        handles=legend_patches,

        loc="upper left",

        fontsize=7.5,

        facecolor="#0f3460",

        edgecolor="#333366",

        labelcolor="white",

        framealpha=0.9
    )

    # =====================================================================
    # TÍTULO GENERAL
    # =====================================================================

    fig.suptitle(

        "Análisis de Complejidad Algorítmica — MLP Classifier",

        color="white",

        fontsize=11,

        y=1.01,

        alpha=0.7
    )

    plt.tight_layout()

    # =====================================================================
    # EXPORTAR IMAGEN A MEMORIA
    # =====================================================================

    buf = io.BytesIO()

    plt.savefig(

        buf,

        format="png",

        dpi=150,

        bbox_inches="tight",

        facecolor=fig.get_facecolor()
    )

    plt.close(fig)

    buf.seek(0)

    return buf.read()


# ============================================================================
# PRUEBA LOCAL
# ============================================================================

if __name__ == "__main__":

    for complexity in COMPLEXITY_CONFIG:

        data = generate_complexity_plot(
            complexity
        )

        filename = (
            complexity
            .replace("(", "")
            .replace(")", "")
            .replace(" ", "_")
            + ".png"
        )

        with open(
            f"/tmp/{filename}",
            "wb"
        ) as f:

            f.write(data)

        print(
            f"Generado: {filename} "
            f"({len(data)} bytes)"
        )