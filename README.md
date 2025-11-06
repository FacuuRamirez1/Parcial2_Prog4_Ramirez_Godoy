## Informe Técnico del Proyecto: Gestión Jerárquica de Datos

### Introducción y Objetivo General

&nbsp;&nbsp;&nbsp;El presente proyecto, desarrollado para el Segundo Parcial de Programación I , tuvo como objetivo principal diseñar e implementar una aplicación en Python 3.x que gestione la persistencia y consulta de datos utilizando una estructura de directorios jerárquica.

&nbsp;&nbsp;&nbsp;Se basó en el dominio del Fútbol Argentino para modelar y demostrar la aplicación de conocimientos avanzados en el diseño de estructuras de datos, manipulación de archivos CSV, la librería estándar os para la gestión de directorios, y la recursividad como mecanismo obligatorio para la lectura del sistema de archivos.

### Diseño y Estructura de Persistencia

&nbsp;&nbsp;&nbsp;Se estableció una estructura de datos jerárquica que se mapea directamente al sistema de archivos , definiendo tres niveles de jerarquía/filtrado:

- Nivel 1: Futbol_argentino (tema principal).

- Nivel 2: liga_profesional, primera_nacional y federal_A (Categorías o ligas).

- Nivel 3: equipos_LP, equipos_PN y equipos_FA (archivo CSV final, con los equipos de cada Categoría).

&nbsp;&nbsp;&nbsp;Cada ítem individual (equipo) se representa en Python como un diccionario y es almacenado como un registro en el archivo CSV correspondiente.

### Diseño de la Jerarquía de Carpetas

La aplicación está diseñada para crear y navegar la estructura de carpetas de forma dinámica. El diseño lógico de la jerarquía es el siguiente:

Futbol_argentino/  
├── Federal_A/  
│ └── equipos_FA.csv  
│── Liga_profesional/  
│ └── equipos_LP.csv  
└── Primera_nacional/  
 └── equipos_PN.csv

&nbsp;&nbsp;&nbsp;Implementación Técnica y Cumplimiento de Requisitos
La implementación se centró en los requisitos obligatorios definidos en la Fase 2:

#### 1. Lectura Recursiva del Sistema de Archivos:

&nbsp;&nbsp;&nbsp;Se implementó una función utilizando la técnica de recursividad para recorrer la estructura de carpetas completa.

&nbsp;&nbsp;&nbsp;Paso Recursivo: Cuando se identifica un directorio, la función se llama a sí misma para cada subdirectorio/archivo.

&nbsp;&nbsp;&nbsp;Caso Base: Si el elemento es un archivo CSV, se lee su contenido para consolidar todos los ítems.

&nbsp;&nbsp;&nbsp;El objetivo se cumplió al recolectar todos los ítems almacenados en los diferentes archivos CSV de la jerarquía en una única lista de diccionarios en memoria para su posterior procesamiento (consultas, estadísticas, ordenamientos).

#### 2. Gestión Jerárquica de Archivos (os y csv):

&nbsp;&nbsp;&nbsp;La librería os se utiliza para la creación y manejo seguro de rutas.

&nbsp;&nbsp;&nbsp;Alta (Create): La función de Alta verifica y crea la estructura de carpetas necesaria de forma dinámica (os.makedirs) siguiendo la jerarquía ingresada. Los datos se persisten usando el modo 'a'.

&nbsp;&nbsp;&nbsp;Modificación (Update) y Eliminación (Delete): Estas operaciones modifican el ítem en la memoria y luego sobrescriben únicamente el archivo CSV específico de la liga (usando el modo 'w') para reflejar la persistencia del cambio.

&nbsp;&nbsp;&nbsp;Se incorporó el manejo de excepciones (try/except) para controlar errores durante la lectura o escritura de archivos (ej. FileNotFoundError) y para validar estrictamente la entrada de datos (ej. tipo de dato, no vacíos).

### Video explicativo

- Link del video explicativo:
