"""
telegram_bot.py
---------------

Bot de Telegram encargado de proporcionar una interfaz conversacional
para interactuar con el sistema de clasificación de complejidad algorítmica.

Este módulo permite que estudiantes, docentes o usuarios finales envíen
fragmentos de código Python directamente desde Telegram y obtengan una
predicción de su complejidad temporal realizada por la red neuronal MLP.

Arquitectura:
-------------
Usuario
    │
    ▼
Telegram Bot
    │
    ▼
REST API (FastAPI)
    │
    ▼
MLP Classifier
    │
    ▼
Predicción de Complejidad

Funcionalidades principales:
----------------------------
- Entrenamiento remoto del modelo.
- Consulta del estado del sistema.
- Análisis automático de algoritmos.
- Visualización de métricas de entrenamiento.
- Recuperación de Hard Examples.
- Ejecución de benchmarks.
- Consulta de complejidades teóricas.
- Detección automática de código pegado en mensajes.

Tecnologías utilizadas:
-----------------------
- python-telegram-bot
- Requests
- FastAPI
- REST Architecture
- Async Programming

Autores:
    - Cristian Cortes
    - Katherine Arboleda

Proyecto:
    Clasificador de Complejidad Algorítmica mediante Redes Neuronales Multicapa (MLP)
"""

import os
import requests

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# -------------------------------------------------------------------------
# Configuración de variables de entorno
# -------------------------------------------------------------------------

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
API_URL = os.getenv("API_URL")


class BotConfiguration:
    """
    Contenedor conceptual para la configuración del bot.

    Attributes
    ----------
    TOKEN : str
        Token de autenticación del bot de Telegram.

    API_URL : str
        URL base de la API REST utilizada por el sistema.
    """
    pass


# ─────────────────────────────────────────────────────────────────────────────
# /start
# ─────────────────────────────────────────────────────────────────────────────

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Comando de bienvenida.

    Es ejecutado cuando el usuario utiliza el comando /start.

    Proporciona una breve descripción del sistema y orienta al usuario
    hacia el comando de ayuda.

    Parameters
    ----------
    update : Update
        Información del mensaje recibido.

    context : ContextTypes.DEFAULT_TYPE
        Contexto de ejecución proporcionado por Telegram.

    Returns
    -------
    None
    """

    await update.message.reply_text(
        "MLP Algorithm Complexity Classifier\n"
        "Escribe /help para ver los comandos disponibles."
    )


# ─────────────────────────────────────────────────────────────────────────────
# /help
# ─────────────────────────────────────────────────────────────────────────────

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Muestra todos los comandos disponibles del sistema.

    Este comando actúa como guía rápida para el usuario,
    describiendo las funcionalidades soportadas por el bot.

    Returns
    -------
    None
    """

    await update.message.reply_text(
        "Comandos disponibles:\n\n"
        "/train_complexity  - Entrena el MLP clasificador\n"
        "/analize <codigo>  - Clasifica la complejidad de un algoritmo\n"
        "/status            - Estado del modelo\n"
        "/complexity_metrics- Accuracy y loss por epoca\n"
        "/hardexamples      - Ejemplos mas dificiles del entrenamiento\n"
        "/benchmark         - Benchmark heap vs sort\n"
        "/complexity        - Complejidades teoricas de los modulos\n"
        "/help              - Muestra este mensaje\n\n"
        "Tambien puedes pegar codigo directamente como mensaje de texto."
    )


# ─────────────────────────────────────────────────────────────────────────────
# /status
# ─────────────────────────────────────────────────────────────────────────────

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Consulta el estado actual del sistema.

    Realiza una petición HTTP al endpoint /status de la API REST
    y presenta información relacionada con:

    - Estado de disponibilidad.
    - Estado del modelo neuronal.
    - Accuracy actual del entrenamiento.

    Returns
    -------
    None
    """

    response = requests.get(f"{API_URL}/status")
    data = response.json()

    await update.message.reply_text(
        f"Estado del sistema\n\n"
        f"Modelo: {data['mlp_model']}\n"
        f"Accuracy: {data['accuracy']}"
    )


# ─────────────────────────────────────────────────────────────────────────────
# /train_complexity
# ─────────────────────────────────────────────────────────────────────────────

async def train_complexity(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Inicia el proceso de entrenamiento del modelo MLP.

    El bot envía una solicitud al endpoint correspondiente de la API,
    espera la finalización del proceso y posteriormente muestra un
    resumen estadístico del entrenamiento realizado.

    Información mostrada:
    ---------------------
    - Accuracy de prueba.
    - Mejor accuracy de entrenamiento.
    - Cantidad de muestras.
    - Número de épocas ejecutadas.

    Returns
    -------
    None
    """

    await update.message.reply_text(
        "Entrenando MLP clasificador de complejidad...\n"
        "Esto puede tardar unos segundos."
    )

    try:
        response = requests.post(
            f"{API_URL}/train_complexity",
            timeout=120
        )

        data = response.json()

        if "error" in data:
            await update.message.reply_text(f"Error: {data['error']}")
            return

        await update.message.reply_text(
            f"Entrenamiento completo\n\n"
            f"Test accuracy:  {data.get('test_accuracy')}%\n"
            f"Best train acc: {data.get('best_train_acc')}%\n"
            f"Train samples:  {data.get('train_samples')}\n"
            f"Test samples:   {data.get('test_samples')}\n"
            f"Epocas:         {data.get('epochs')}"
        )

    except requests.exceptions.Timeout:
        await update.message.reply_text(
            "El entrenamiento esta tomando mas tiempo del esperado. "
            "Intenta /status para verificar si ya termino."
        )

    except Exception as e:
        await update.message.reply_text(
            f"Error: {str(e)}"
        )


# ─────────────────────────────────────────────────────────────────────────────
# /complexity_metrics
# ─────────────────────────────────────────────────────────────────────────────

async def complexity_metrics(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Recupera y resume las métricas de entrenamiento del modelo.

    Muestra información relevante como:

    - Primera época.
    - Mejor época alcanzada.
    - Última época ejecutada.
    - Últimas cinco épocas registradas.

    El resumen es optimizado para respetar los límites de longitud
    impuestos por Telegram.

    Returns
    -------
    None
    """

    response = requests.get(f"{API_URL}/complexity_metrics")
    data = response.json()

    if not data:
        await update.message.reply_text(
            "No hay metricas disponibles.\n"
            "Ejecuta /train_complexity primero."
        )
        return

    items = list(data.items())
    total = len(items)

    best = max(
        items,
        key=lambda x: x[1].get('accuracy', 0)
    )

    best_epoch = best[0]
    best_acc = best[1]['accuracy']
    best_loss = best[1]['loss']

    first_key, first_val = items[0]
    last_key, last_val = items[-1]

    text = (
        f"Metricas de entrenamiento\n\n"
        f"Total de epocas: {total}\n\n"
        f"Epoca inicial\n"
        f"  {first_key}: acc={first_val['accuracy']}%  loss={first_val['loss']}\n\n"
        f"Mejor epoca\n"
        f"  {best_epoch}: acc={best_acc}%  loss={best_loss}\n\n"
        f"Ultima epoca\n"
        f"  {last_key}: acc={last_val['accuracy']}%  loss={last_val['loss']}\n\n"
        f"Ultimas 5 epocas:\n"
    )

    for key, val in items[-5:]:
        text += (
            f"  {key}: "
            f"acc={val['accuracy']}% "
            f"loss={val['loss']}\n"
        )

    await update.message.reply_text(text)


# ─────────────────────────────────────────────────────────────────────────────
# /hardexamples
# ─────────────────────────────────────────────────────────────────────────────

async def hard_examples(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Obtiene los ejemplos más difíciles identificados durante
    el entrenamiento mediante Hard Example Mining.

    Estos ejemplos corresponden a las muestras que generaron
    los mayores valores de pérdida (loss).

    Returns
    -------
    None
    """

    response = requests.get(f"{API_URL}/hard-examples")
    data = response.json()

    text = "Ejemplos mas dificiles (hard mining)\n\n"

    for loss, idx in data["hard_examples"]:
        text += f"Sample {idx} -> loss {loss:.4f}\n"

    await update.message.reply_text(text)


# ─────────────────────────────────────────────────────────────────────────────
# /benchmark
# ─────────────────────────────────────────────────────────────────────────────

async def benchmark(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Ejecuta y muestra los resultados del benchmark comparativo
    entre los algoritmos Top-K basados en Heap y Ordenamiento.

    Returns
    -------
    None
    """

    response = requests.get(f"{API_URL}/benchmark")
    data = response.json()

    text = "Benchmark Heap vs Sort (Top-K)\n\n"

    for item in data["benchmark"]:
        text += (
            f"N={item['n']}\n"
            f"  Heap: {item['heap_time']:.6f}s\n"
            f"  Sort: {item['sort_time']:.6f}s\n\n"
        )

    await update.message.reply_text(text)


# ─────────────────────────────────────────────────────────────────────────────
# /complexity
# ─────────────────────────────────────────────────────────────────────────────

async def complexity(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Consulta las complejidades teóricas de los algoritmos
    y estructuras de datos implementadas en el proyecto.

    Returns
    -------
    None
    """

    response = requests.get(f"{API_URL}/complexity")
    data = response.json()

    text = "Complejidades teoricas\n\n"

    for key, value in data.items():
        text += f"{key} -> {value}\n"

    await update.message.reply_text(text)


# ─────────────────────────────────────────────────────────────────────────────
# /analize
# ─────────────────────────────────────────────────────────────────────────────

async def analize(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Procesa el comando /analize.

    Permite al usuario enviar un fragmento de código Python
    directamente como argumento del comando para ser clasificado
    por la red neuronal.

    Returns
    -------
    None
    """

    if not context.args:

        await update.message.reply_text(
            "Uso: /analize <codigo Python>\n\n"
            "Ejemplo:\n"
            "/analize for i in range(n):\\n"
            "  for j in range(n):\\n"
            "    pass\n\n"
            "Tambien puedes pegar el codigo directamente como mensaje."
        )

        return

    raw_text = update.message.text
    code = raw_text[len("/analize "):].strip()

    code = (
        code
        .replace("\\n", "\n")
        .replace("\\t", "\t")
    )

    await _call_analize_api(update, code)


# ─────────────────────────────────────────────────────────────────────────────
# Mensajes de texto
# ─────────────────────────────────────────────────────────────────────────────

async def analize_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Detecta automáticamente código Python enviado como mensaje
    de texto normal.

    Si el mensaje contiene patrones sintácticos típicos de Python,
    el bot asume que se trata de un algoritmo y solicita su análisis.

    Returns
    -------
    None
    """

    text = update.message.text.strip()

    code_keywords = (
        "def ",
        "for ",
        "while ",
        "return ",
        "if ",
        "class "
    )

    if any(kw in text for kw in code_keywords):

        await update.message.reply_text(
            "Analizando complejidad..."
        )

        await _call_analize_api(update, text)


# ─────────────────────────────────────────────────────────────────────────────
# Helper principal
# ─────────────────────────────────────────────────────────────────────────────

async def _call_analize_api(update: Update, code: str):
    """
    Función auxiliar encargada de comunicarse con la API REST
    para realizar la clasificación de complejidad algorítmica.

    Parameters
    ----------
    update : Update
        Información del mensaje recibido.

    code : str
        Fragmento de código Python a analizar.

    Returns
    -------
    None
    """

    try:
        response = requests.post(
            f"{API_URL}/analize",
            json={"code": code},
            timeout=10
        )

        data = response.json()

        if "error" in data:
            await update.message.reply_text(
                f"Error: {data['error']}"
            )
            return

        complexity = data.get("complexity", "?")
        confidence = data.get("confidence", 0)
        top3 = data.get("top3", [])

        emoji_map = {
            "O(1)": "🟢",
            "O(log n)": "🟡",
            "O(n)": "🟡",
            "O(n log n)": "🟠",
            "O(n²)": "🔴",
            "O(n³)": "🔴",
            "O(2^n)": "💀",
            "O(n!)": "💀",
        }

        reason_map = {
            "O(1)": "Operaciones constantes.",
            "O(log n)": "Reducción logarítmica.",
            "O(n)": "Recorrido lineal.",
            "O(n log n)": "Divide y vencerás.",
            "O(n²)": "Bucles anidados.",
            "O(n³)": "Triple iteración.",
            "O(2^n)": "Explosión exponencial.",
            "O(n!)": "Permutaciones factoriales.",
        }

        emoji = emoji_map.get(complexity, "🔵")
        reason = reason_map.get(complexity, "Patrón no identificado.")

        conf_pct = round(confidence * 100, 1)

        text = (
            f"Analisis de Complejidad\n\n"
            f"{emoji} Complejidad: {complexity}\n"
            f"Razon: {reason}\n"
            f"Confianza: {conf_pct}%"
        )

        await update.message.reply_text(text)

    except Exception as e:
        await update.message.reply_text(
            f"Error al analizar: {str(e)}"
        )


# ─────────────────────────────────────────────────────────────────────────────
# main
# ─────────────────────────────────────────────────────────────────────────────

def main():
    """
    Punto de entrada principal de la aplicación.

    Configura:

    - Token de autenticación.
    - Registro de comandos.
    - Manejadores de mensajes.
    - Inicio del proceso de polling.

    Returns
    -------
    None
    """

    app = ApplicationBuilder().token(TOKEN).build()

    commands = [
        ("start", start),
        ("help", help_command),
        ("status", status),
        ("train_complexity", train_complexity),
        ("analize", analize),
        ("complexity_metrics", complexity_metrics),
        ("hardexamples", hard_examples),
        ("benchmark", benchmark),
        ("complexity", complexity),
    ]

    for name, fn in commands:
        app.add_handler(
            CommandHandler(name, fn)
        )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            analize_message
        )
    )

    print("Bot running...")

    app.run_polling()


if __name__ == "__main__":
    main()