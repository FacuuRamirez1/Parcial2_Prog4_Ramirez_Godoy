# Parcial2_Prog4_Ramirez_Godoy

📄 Informe Técnico del Proyecto: Gestión Jerárquica de Datos
Introducción y Objetivo General
El presente proyecto, desarrollado para el Segundo Parcial de Programación I , tuvo como objetivo principal diseñar e implementar una aplicación en Python 3.x que gestione la persistencia y consulta de datos utilizando una estructura de directorios jerárquica. 

⚽El proyecto se basó en el dominio del Fútbol Argentino para modelar y demostrar la aplicación de conocimientos avanzados en el diseño de estructuras de datos, manipulación de archivos CSV, la librería estándar os para la gestión de directorios, y la recursividad como mecanismo obligatorio para la lectura del sistema de archivos.




Diseño y Estructura de Persistencia

Se estableció una estructura de datos jerárquica que se mapea directamente al sistema de archivos , definiendo tres niveles de jerarquía/filtrado:


Nivel 1 (Región) 


Nivel 2 (Sub-Región / Ciudad) 


Nivel 3 (Liga): Representado por el archivo CSV final (la "hoja" de la jerarquía).

Cada ítem individual (equipo) se representa en Python como un diccionario y es almacenado como un registro en el archivo CSV correspondiente.


🗺️ Diseño de la Jerarquía de Carpetas
La aplicación está diseñada para crear y navegar la estructura de carpetas de forma dinámica. El diseño lógico de la jerarquía es el siguiente:


Futbol_argentino/ 
├── [Región - Nivel 1]/ 
│   ├── [Ciudad - Nivel 2]/ 
│   │   ├── liga_profesional.csv 
│   │   └── federal_a.csv
│   └── [Otra Ciudad - Nivel 2]/ 
│       └── primera_nacional.csv
└── [Otra Región - Nivel 1]/
    └── [Ciudad C - Nivel 2]/
        └── liga_profesional.csv
Implementación Técnica y Cumplimiento de Requisitos
La implementación se centró en los requisitos obligatorios definidos en la Fase 2:

1. Lectura Recursiva del Sistema de Archivos
Se implementó una función utilizando la técnica de recursividad para recorrer la estructura de carpetas completa.


Paso Recursivo: Cuando se identifica un directorio, la función se llama a sí misma para cada subdirectorio/archivo.


Caso Base: Si el elemento es un archivo CSV, se lee su contenido para consolidar todos los ítems.

El objetivo se cumplió al recolectar todos los ítems almacenados en los diferentes archivos CSV de la jerarquía en una única lista de diccionarios en memoria para su posterior procesamiento (consultas, estadísticas, ordenamientos).

2. Gestión Jerárquica de Archivos (os y csv)
La librería os se utiliza para la creación y manejo seguro de rutas.




Alta (Create): La función de Alta verifica y crea la estructura de carpetas necesaria de forma dinámica (os.makedirs) siguiendo la jerarquía ingresada. Los datos se persisten usando el modo 'a'.




Modificación (Update) y Eliminación (Delete): Estas operaciones modifican el ítem en la memoria y luego sobrescriben únicamente el archivo CSV específico de la liga (usando el modo 'w') para reflejar la persistencia del cambio.





Se incorporó el manejo de excepciones (try/except) para controlar errores durante la lectura o escritura de archivos (ej. FileNotFoundError) y para validar estrictamente la entrada de datos (ej. tipo de dato, no vacíos).