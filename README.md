# SISTEMA OPTOGESTIÓN
## Sistema de gestión de pacientes para jornadas de atención optométrica

## Descripción del proyecto

OPTOGESTIÓN es un programa desarrollado en Python para un centro universitario de atención optométrica. Su propósito es facilitar el registro, almacenamiento, consulta y procesamiento de la información de los pacientes atendidos durante las jornadas visuales.

El sistema funciona mediante un menú interactivo en consola que permite gestionar los registros de los pacientes y consultar información estadística de manera sencilla y organizada.

Los datos se almacenan en un archivo JSON, permitiendo conservar la información incluso después de cerrar el programa.

## Objetivo general

Desarrollar un sistema en Python que permita administrar la información de los pacientes atendidos en jornadas optométricas, utilizando estructuras de datos, funciones, condicionales, ciclos y almacenamiento permanente mediante archivos JSON.

## Funcionalidades principales

1. Registrar paciente:
   Permite ingresar los siguientes datos:
   - Identificador único (ID).
   - Nombre completo.
   - Edad.
   - Sexo.
   - Uso de corrección visual.

2. Consultar paciente:
   Permite buscar un paciente mediante su identificador y visualizar toda su información registrada.

3. Mostrar pacientes registrados:
   Presenta los nombres de todos los pacientes almacenados en el sistema.

4. Buscar pacientes con corrección visual:
   Permite identificar y mostrar los pacientes que utilizan corrección visual.

5. Generar estadísticas:
   Calcula y presenta:
   - Número total de pacientes registrados.
   - Edad promedio de los pacientes.
   - Cantidad de pacientes que utilizan corrección visual.

6. Salir:
   Permite finalizar la ejecución del programa.

## Tecnologías y herramientas utilizadas

- Python: lenguaje de programación utilizado para desarrollar el sistema.
- Listas: permiten almacenar los registros de los pacientes.
- Diccionarios: organizan la información individual de cada paciente.
- Funciones: permiten organizar las diferentes operaciones.
- Condicionales: permiten controlar las opciones del menú y validar información.
- Ciclos: facilitan la ejecución repetitiva del menú y el recorrido de los registros.
- JSON: permite almacenar y conservar permanentemente la información de los pacientes.

## Estructura del proyecto

Proyecto-Optogestion/
|
|-- main.py
|   Código fuente del programa.
|
|-- pacientes.json
|   Archivo que almacena los registros de los pacientes.
|
|-- README.md
    Documentación del proyecto.

## Almacenamiento de información

Los registros de los pacientes se almacenan en el archivo pacientes.json.

La información se organiza mediante una lista de diccionarios. Cada diccionario contiene los datos correspondientes a un paciente.

Ejemplo de un registro:

[
    {
        "id": "P001",
        "nombre": "Laura Gómez",
        "edad": 24,
        "sexo": "F",
        "usa_correccion": true
    }
]

El archivo permite conservar los registros para futuras consultas y evitar que la información se pierda al cerrar el programa.

## Instrucciones de ejecución

1. Instalar Python:
   Verificar que Python esté instalado en el equipo.

2. Descargar el repositorio:
   Clonar el repositorio desde GitHub o descargarlo en formato ZIP.

3. Abrir el proyecto:
   Abrir la carpeta utilizando Visual Studio Code o una terminal.

4. Ejecutar el programa:
   Desde la terminal, ejecutar el siguiente comando:

   python main.py

5. Utilizar el menú principal:
   Una vez iniciado el programa, aparecerá el menú de OPTOGESTIÓN, desde donde se podrá seleccionar la funcionalidad deseada.

El menú permanecerá disponible hasta que el usuario seleccione la opción de salida.

## Validaciones del sistema

- La edad de los pacientes debe estar entre 1 y 120 años.
- Las respuestas relacionadas con el uso de corrección visual deben admitir únicamente las opciones Sí o No.
- La consulta de pacientes debe verificar que el identificador exista.
- El sistema debe informar cuando no se encuentren pacientes que cumplan una búsqueda.
- Las estadísticas deben evitar divisiones entre cero cuando no existan registros.

## Contexto académico

Proyecto: Proyecto Final de Programación I.
Sistema: OPTOGESTIÓN.
Área de aplicación: Atención optométrica.
Lenguaje de programación: Python.
Institución: Universidad CES.

## Integrantes

- Leidy Yolima Aristizabal Giraldo
- Janny Faisury Cano Mona
- Karen Sofia Estepa Albarracin
- Laura Sofia Serna Gallego

OPTOGESTIÓN - Organización y gestión de información para jornadas de atención optométrica.
