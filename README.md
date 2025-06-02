# 🛠️ Mini Compilador DSL

Un lenguaje de dominio específico (DSL) creado con **ANTLR** y **Python** para analizar y consultar datos de reservas hoteleras almacenados en archivos CSV. Este mini compilador permite la ejecución de comandos intuitivos para obtener información relevante y estadísticas del sistema de inventario hotelero.

---

## 🎯 Características Principales

* ✅ **Lenguaje DSL personalizado** para la consulta de reservas.
* 🔎 **Filtrado avanzado** mediante operadores lógicos (`AND`, `OR`, `BETWEEN`).
* 📈 **Agregaciones en tiempo real** como `COUNT`, `SUM`, `AVERAGE`.
* 📂 **Carga dinámica de archivos CSV** para análisis inmediato.
* 🧪 **40+ scripts predefinidos** para pruebas y demostraciones.
* 🚨 **Manejo robusto de errores sintácticos y semánticos**.
* 🌳 **Visualización de árboles de parseo (Parse Trees)** para depuración.
* 🧼 Sintaxis clara y estilo declarativo, tipo SQL simplificado.

---

## 📋 Menú de Consultas DSL

Consultas disponibles:

1. Total reservas confirmadas
2. Precio promedio suites
3. Reservas con tarjeta
4. Suma precios dobles
5. Reservas largas
6. Reservas entre fechas
   ...
7. Habitaciones confirmadas

Manejo de errores (41-50):

* Columna inexistente
* Tipo incorrecto
* Sintaxis inválida
* Agregación no numérica
* BETWEEN no numérico
* Archivo no encontrado
* Operador inválido
* Expresión incompleta
* Tipos mixtos

---

## 🔧 Requisitos del Sistema

* Python 3.8 o superior
* ANTLR 4.9+

Instalación de dependencias:

```bash
pip install pandas antlr4-python3-runtime python-dateutil
```

---

## 🧱 Instalación y Uso

1. Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/mini-compilador-dsl.git
cd mini-compilador-dsl/GestionInventarioHotel
```

2. Generar los archivos a partir del archivo `.g4`:

```bash
antlr4 -Dlanguage=Python3 CSVFilter.g4
```

3. Ejecutar el compilador DSL:

```bash
python main.py
```

---

## 📁 Estructura del Proyecto

```
GestionInventarioHotel/
├── CSVFilter.g4              # Gramática ANTLR del DSL
├── CSVFilterVisitor.py       # Visitor generado
├── main.py                   # Programa principal
├── consultas.csv             # Archivo de datos de entrada
├── ejemplos/                 # Scripts DSL de ejemplo
└── utils/                    # Funciones auxiliares (validación, agregación, etc.)
```

---

## 🤝 Contribuciones

Si deseas mejorar este compilador, corregir errores o proponer nuevas funcionalidades para el DSL, ¡serán bienvenidas tus contribuciones mediante issues o pull requests!

---

## 📬 Contacto

* Email: [diegoguerrero@umariana.edu.co](mailto:diegoguerrerov@umariana.edu.co)
* LinkedIn: [Diego Guerrero](https://www.linkedin.com/in/diego-guerrero-dev)
* GitHub: [@Diego-9612](https://github.com/Diego-9612)

---

> Este proyecto es una demostración académica de cómo implementar lenguajes de dominio específico usando ANTLR y Python, aplicados al análisis de datos estructurados como CSV en el contexto de la hotelería.


