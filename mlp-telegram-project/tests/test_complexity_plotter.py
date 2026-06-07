"""
Pruebas unitarias para complexity_plotter.py

Se valida:

- Generación de imágenes PNG
- Tipo de retorno
- Complejidades soportadas
- Complejidades inválidas
- Configuración de complejidades
- Orden de complejidades

Autores:
    Cristian Cortes
    Katherine Arboleda

Curso:
    Análisis y Diseño de Algoritmos
    Universidad del Valle
"""

from complexity.complexity_plotter import (
    generate_complexity_plot,
    COMPLEXITY_CONFIG,
    COMPLEXITY_ORDER,
    Y_LIMITS
)


# ==========================================================
# TIPO DE RETORNO
# ==========================================================

def test_returns_bytes():
    """
    Debe retornar una imagen en formato bytes.
    """

    image = generate_complexity_plot(
        "O(n)"
    )

    assert isinstance(
        image,
        bytes
    )


# ==========================================================
# PNG VÁLIDO
# ==========================================================

def test_returns_png_image():
    """
    La imagen debe iniciar con la firma PNG.
    """

    image = generate_complexity_plot(
        "O(n)"
    )

    png_signature = b"\x89PNG"

    assert image.startswith(
        png_signature
    )


# ==========================================================
# IMAGEN NO VACÍA
# ==========================================================

def test_image_not_empty():
    """
    La imagen generada debe contener datos.
    """

    image = generate_complexity_plot(
        "O(n)"
    )

    assert len(image) > 0


# ==========================================================
# COMPLEJIDAD CONSTANTE
# ==========================================================

def test_generate_constant_plot():
    """
    Debe generar correctamente
    una gráfica O(1).
    """

    image = generate_complexity_plot(
        "O(1)"
    )

    assert len(image) > 0


# ==========================================================
# COMPLEJIDAD LOGARÍTMICA
# ==========================================================

def test_generate_logarithmic_plot():
    """
    Debe generar correctamente
    una gráfica O(log n).
    """

    image = generate_complexity_plot(
        "O(log n)"
    )

    assert len(image) > 0


# ==========================================================
# COMPLEJIDAD LINEAL
# ==========================================================

def test_generate_linear_plot():
    """
    Debe generar correctamente
    una gráfica O(n).
    """

    image = generate_complexity_plot(
        "O(n)"
    )

    assert len(image) > 0


# ==========================================================
# COMPLEJIDAD N LOG N
# ==========================================================

def test_generate_nlogn_plot():
    """
    Debe generar correctamente
    una gráfica O(n log n).
    """

    image = generate_complexity_plot(
        "O(n log n)"
    )

    assert len(image) > 0


# ==========================================================
# COMPLEJIDAD CUADRÁTICA
# ==========================================================

def test_generate_quadratic_plot():
    """
    Debe generar correctamente
    una gráfica O(n²).
    """

    image = generate_complexity_plot(
        "O(n²)"
    )

    assert len(image) > 0


# ==========================================================
# COMPLEJIDAD CÚBICA
# ==========================================================

def test_generate_cubic_plot():
    """
    Debe generar correctamente
    una gráfica O(n³).
    """

    image = generate_complexity_plot(
        "O(n³)"
    )

    assert len(image) > 0


# ==========================================================
# COMPLEJIDAD EXPONENCIAL
# ==========================================================

def test_generate_exponential_plot():
    """
    Debe generar correctamente
    una gráfica O(2^n).
    """

    image = generate_complexity_plot(
        "O(2^n)"
    )

    assert len(image) > 0


# ==========================================================
# COMPLEJIDAD INVÁLIDA
# ==========================================================

def test_invalid_complexity_fallback():
    """
    Una complejidad inválida no debe generar error.
    """

    image = generate_complexity_plot(
        "INVALID"
    )

    assert len(image) > 0


# ==========================================================
# CONFIGURACIÓN CONSISTENTE
# ==========================================================

def test_complexity_order_matches_config():
    """
    Todas las complejidades del orden
    deben existir en la configuración.
    """

    for complexity in COMPLEXITY_ORDER:

        assert complexity in COMPLEXITY_CONFIG


# ==========================================================
# LÍMITES Y DEFINIDOS
# ==========================================================

def test_all_complexities_have_y_limits():
    """
    Todas las complejidades deben
    tener límites de eje Y definidos.
    """

    for complexity in COMPLEXITY_CONFIG:

        assert complexity in Y_LIMITS


# ==========================================================
# CONFIGURACIÓN DE CURVAS
# ==========================================================

def test_complexity_config_structure():
    """
    Cada complejidad debe definir
    función y etiqueta.
    """

    for complexity, config in COMPLEXITY_CONFIG.items():

        assert "fn" in config
        assert "label" in config


# ==========================================================
# GENERACIÓN MASIVA
# ==========================================================

def test_generate_all_complexities():
    """
    Debe generar imágenes para todas
    las complejidades registradas.
    """

    for complexity in COMPLEXITY_CONFIG:

        image = generate_complexity_plot(
            complexity
        )

        assert len(image) > 0