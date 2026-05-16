**Autor:** Cristian Camilo Cortes Ortiz

**Código:** 202478542

**Universidad del Valle**  

**Programa:** Tecnología en Desarrollo de Software

**Asignatura:** Análisis y Diseño de Algoritmos

**Profesor:** Daniel Quintero Capera  

**Fecha:** 16 Mayo 2026

# Sistema de Ordenamiento de Personas

Aplicación desarrollada en **Python + Tkinter + SQLite** para el taller de 
**Análisis y Diseño de Algoritmos**, enfocada en la implementación y análisis 
asintótico de algoritmos clásicos de ordenamiento.

El sistema permite cargar un conjunto de personas desde una base de datos SQLite,
ordenar los registros usando algoritmos clásicos y analizar su rendimiento 
empírico y teórico.

## Características

* Carga de datos desde SQLite
* Implementación manual de algoritmos de ordenamiento
* Medición de tiempo de ejecución
* Análisis de complejidad algorítmica
* Exportación de resultados a Excel
* Interfaz gráfica con Tkinter
* Arquitectura modular basada en separación de responsabilidades

## Algoritmos Implementados

### Bubble Sort (Burbuja)

* Peor caso: `O(n²)`
* Caso promedio: `Θ(n²)`
* Mejor caso: `Ω(n)`

### Insertion Sort (Inserción)

* Peor caso: `O(n²)`
* Caso promedio: `Θ(n²)`
* Mejor caso: `Ω(n)`

### Selection Sort (Selección)

* Peor caso: `O(n²)`
* Caso promedio: `Θ(n²)`
* Mejor caso: `Ω(n²)`

## Tecnologías Utilizadas

* Python 3.13+
* Tkinter
* SQLite3
* OpenPyXL

---

# Instalación del Proyecto

## 1. Clonar el repositorio

```bash
git clone https://github.com/Cristianco9/univalle-ada-2026-i.git
```

Entrar al proyecto:

```bash
cd proyecto_ordenamiento
```

---

## 2. Crear entorno virtual

### Windows (CMD)

```cmd
python -m venv venv
```

Activar:

```cmd
venv\Scripts\activate
```

### Windows (PowerShell)

```powershell
python -m venv venv
```

Activar:

```powershell
venv\Scripts\Activate.ps1
```

### Linux

Crear:

```bash
python3 -m venv venv
```

Activar:

```bash
source venv/bin/activate
```

### macOS

Crear:

```bash
python3 -m venv venv
```

Activar:

```bash
source venv/bin/activate
```

---

## 3. Instalar dependencias

Con el entorno virtual activado:

```bash
pip install -r requirements.txt
```

Si no existe el archivo `requirements.txt`, instalar manualmente:

```bash
pip install openpyxl
```

---

## 4. Configurar Base de Datos SQLite

Crear la base de datos SQLite:

```bash
sqlite3 personas.db
```

Dentro de SQLite ejecutar:

```sql
.read script.sql
```

Verificar las tablas:

```sql
.tables
```

Verificar cantidad de registros:

```sql
SELECT COUNT(*) FROM personas;
```

Salir:

```sql
.quit
```

---

## 5. Ejecutar el Proyecto

Desde la raíz del proyecto:

### Windows

```cmd
python main.py
```

### Linux

```bash
python3 main.py
```

### macOS

```bash
python3 main.py
```

---

## Exportación de Resultados

Los resultados ordenados se exportan automáticamente en:

```text
output/personas_ordenadas.xlsx
```

---

## Flujo de Uso del Sistema

1. Ejecutar la aplicación
2. Presionar **Cargar Datos**
3. Seleccionar el criterio de ordenamiento:

   * nombre
   * edad
   * puntaje_evaluacion

4. Elegir algoritmo:

   * Bubble Sort
   * Insertion Sort
   * Selection Sort

5. Ver tiempo de ejecución
6. Analizar complejidad teórica
7. Exportar resultados a Excel

---

## Requerimientos del Taller Cubiertos

* Menú interactivo
* Ordenamiento manual sin `.sort()`
* Uso de Bubble Sort
* Uso de Insertion Sort
* Uso de Selection Sort
* Medición del tiempo de ejecución
* Complejidad asintótica (`Big O`, `Big Θ`, `Big Ω`)
* Carga de datos desde base de datos
* Exportación de resultados a Excel
* Arquitectura modular