# Mini Compilador DSL para Gestión de Inventario Hotelero Antlr y Python
Un lenguaje de dominio específico (DSL) para consultar y analizar datos de reservas hoteleras desde archivos CSV.

## Características Principales

- 🚀 **Consultas tipo comando** con sintaxis intuitiva
- 🔍 **Filtrado avanzado** con operadores lógicos (`AND`, `OR`, `BETWEEN`)
- 📊 **Agregaciones** en tiempo real (`COUNT`, `SUM`, `AVERAGE`)
- 📁 **Carga dinámica** de archivos CSV
- 🛠 **40+ scripts de ejemplo** predefinidos
- 🚨 **Manejo de errores** detallado
- 🌳 **Visualización de Parse Trees**

## Menu de Consultas 

Consultas válidas (1-40):
 1. Total reservas confirmadas
 2. Precio promedio suites
 3. Reservas con tarjeta
 4. Suma precios dobles
 6. Reservas entre fechas
 5. Reservas largas
 7. Habitaciones más caras
 8. Reservas canceladas transferencia
 9. Promedio noches individuales
10. Reservas pendientes
11. Reservas habitación específica
12. Pagos en efectivo
13. Precio promedio dobles
14. Reservas muy largas
15. Reservas enero 2025
16. Suites confirmadas
17. Total canceladas
18. Pagos electrónicos
19. Precio promedio estancias cortas
20. Reservas tercer trimestre 2024
21. Reservas cortas confirmadas
22. Habitaciones ocupadas
23. Reservas en fechas específicas
24. Precio promedio individuales
25. Reservas suites largas
26. Clientes con reservas
27. Reservas de 4 a 5 noches
28. Pagos no electrónicos
29. Estancia promedio general
30. Reservas Navidad 2024
31. Precios fuera de rango
32. Reservas recientes
33. Conteo de habitaciones dobles
34. Reservas económicas
35. Clientes con reservas activas
36. Temporada alta
37. Reservas con tarjeta
38. Reservas de 1 noche
39. Precios moderados
40. Habitaciones confirmadas


41. Error: Columna inexistente
42. Error: Tipo incorrecto
43. Error: Sintaxis inválida
44. Error: Función no soportada
45. Error: Agregación no numérica
46. Error: BETWEEN no numérico
47. Error: Archivo no encontrado
48. Error: Operador inválido
49. Error: Expresión incompleta
50. Error: Tipos mixtos

 0. Salir

## Requisitos

- Python 3.8+
- ANTLR 4.9
- Dependencias:
  ```bash

  pip install pandas antlr4-python3-runtime python-dateutil

## Instalación

Clona el repositorio:
```bash

  git clone https://github.com/tu-usuario/mini-compilador-dsl.git
  cd mini-compilador-dsl/GestionInventarioHotel
  ```
## Genera los archivos ANTLR:

```

antlr4 -Dlanguage=Python3 CSVFilter.g4

```

