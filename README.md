# Base educativa — COMP 2700

**Estudiante:** Jose A. Mulinelli Torres
**Curso:** COMP 2700 — Cybersecurity

## Descripción del proyecto

Este proyecto consiste en analizar y corregir las debilidades de seguridad de una aplicación académica de inventario desarrollada en Python.

Las correcciones realizadas incluyen autenticación mediante contraseñas protegidas con Argon2id, autorización basada en roles, validación de entradas, persistencia de los datos, registro de auditoría y manejo de errores.

El programa funciona mediante una interfaz de terminal (CLI) y utiliza archivos JSON para almacenar la información.

Esta aplicación tiene fines exclusivamente educativos y utiliza datos ficticios. No está diseñada para un entorno de producción.

## Requisitos y dependencias

- Python 3.10 o posterior.
- Biblioteca `argon2-cffi`.
- Git, si se desea clonar el repositorio.

Las dependencias necesarias se encuentran especificadas en el archivo `requirements.txt`.

## Instrucciones de ejecución

### 1. Descargar o clonar el repositorio

Para clonar el repositorio, ejecute:

```bash
git clone https://github.com/jmulinellitorres/COMP2700-Inventario-Seguro.git
```

Acceda a la carpeta del proyecto:

```bash
cd COMP2700-Inventario-Seguro
```

También puede descargar el proyecto como archivo ZIP desde GitHub y extraerlo en una carpeta.

### 2. Crear el entorno virtual

```bash
python -m venv .venv
```

### 3. Activar el entorno virtual

**Windows CMD:**

```cmd
.venv\Scripts\activate.bat
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### 4. Instalar las dependencias

```bash
python -m pip install -r requirements.txt
```

### 5. Ejecutar el programa

```bash
python app.py
```

En algunos sistemas operativos puede ser necesario utilizar `python3` en lugar de `python`.

## Cuentas académicas de prueba

Las siguientes cuentas son ficticias y se proporcionan exclusivamente para comprobar el funcionamiento de la aplicación:

| Usuario | Contraseña de prueba | Permisos              |
| ------- | -------------------- | --------------------- |
| admin   | AdminDemo2700!       | Consultar y modificar |
| user    | UserDemo2700!        | Consultar             |

Las contraseñas se almacenan mediante hashes Argon2id con salt en `usuarios.json`, en lugar de almacenarse en texto plano.

## Uso del programa

Al ejecutar `app.py`, el programa solicita el nombre del estudiante y las credenciales de una cuenta de prueba.

Después de iniciar sesión, presenta las siguientes opciones:

- **1. Consultar:** muestra los productos del inventario.
- **2. Modificar:** permite al administrador modificar las cantidades de productos existentes.
- **3. Cerrar sesión:** termina la sesión actual.
- **0. Salir:** cierra el programa.

Para modificar un producto, debe introducirse su identificador completo, por ejemplo, `P001`.

Las cantidades permitidas son números enteros entre 0 y 1000, inclusive.

Las modificaciones autorizadas se almacenan en `inventario.json`, mientras que los eventos de autenticación y modificación se registran en `auditoria.jsonl`.

## Pruebas realizadas

Se realizaron pruebas para comprobar el funcionamiento de las correcciones de seguridad.

| Prueba                      | Resultado obtenido                                                                                                   |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Autenticación               | Se aceptaron credenciales correctas y se rechazaron credenciales incorrectas.                                        |
| Autorización                | Se verificó que `admin` puede modificar cantidades, mientras que `user` y las sesiones ausentes no tienen permiso.   |
| Validación de entradas      | Se rechazaron `-1`, `1001`, `abc`, `2.5` y la entrada vacía. Se aceptaron los límites válidos `0` y `1000`.          |
| Consulta del inventario     | Se comprobó que tanto `admin` como `user` pueden consultar los productos.                                            |
| Modificación de productos   | El administrador modificó P001 de 10 a 20. Se rechazó el identificador inexistente P999.                             |
| Persistencia                | Se comprobó que P001 conservó la cantidad 20 después de cerrar y volver a ejecutar el programa.                      |
| Auditoría                   | Se verificaron registros de inicios de sesión exitosos y fallidos, modificaciones autorizadas e intentos rechazados. |
| Archivo ausente             | El programa mostró un mensaje de error controlado sin crear automáticamente el archivo.                              |
| JSON inválido               | El programa mostró un mensaje de error controlado sin sobrescribir el contenido inválido.                            |
| Recuperación del inventario | Después de restaurar el archivo válido, se pudo consultar nuevamente el inventario.                                  |

Al finalizar las pruebas, el producto P001 quedó con una cantidad de 20 unidades.

## Uso de inteligencia artificial

Durante el desarrollo de este proyecto se utilizó ChatGPT (OpenAI) como herramienta de apoyo para comprender el funcionamiento del código y explicar conceptos relacionados con Python y la ciberseguridad.

También se utilizó para recibir orientación paso a paso durante la implementación de las correcciones de seguridad, revisar fragmentos de código, generar un script de pruebas para la pregunta 4 y ayudar a preparar la documentación del archivo README.md.

Las sugerencias proporcionadas por la inteligencia artificial se verificaron mediante referencias consultadas en Internet, pruebas de ejecución y la comparación de los resultados obtenidos con los requisitos establecidos en cada pregunta del proyecto.

La inteligencia artificial se utilizó como herramienta de aprendizaje y apoyo. La implementación y las pruebas de ejecución del programa se realizaron personalmente.

## Fuentes consultadas

1. LabEx. (s. f.). _How to handle missing JSON file._
   https://labex.io/tutorials/python-how-to-handle-missing-json-file-495790

2. Stack Overflow. (2019). _Save data in a JSON file without overwriting existing file in Python._
   https://stackoverflow.com/questions/54283830/save-data-in-a-json-flie-without-overwriting-existing-file-in-python

3. Stack Overflow en español. (2021). _¿Cómo guardo un diccionario en un archivo JSON?_
   https://es.stackoverflow.com/questions/487964

4. Turkel, W. J., y Crymble, A. (2017). _Trabajar con archivos de texto en Python._ Programming Historian.
   https://programminghistorian.org/es/lecciones/trabajar-con-archivos-de-texto

5. Stack Overflow. (2010). _ISO time (ISO 8601) in Python._
   https://stackoverflow.com/questions/2150739/iso-time-iso-8601-in-python

6. W3Schools. (s. f.). _Python Dates._
   https://www.w3schools.com/python/python_datetime.asp

7. CodeRivers. (s. f.). _Python Fields: A Comprehensive Guide._
   https://coderivers.org/blog/python-fields/

8. Stack Overflow. (2011). _Delete an element from a dictionary._
   https://stackoverflow.com/questions/5844672/delete-an-element-from-a-dictionary

## Límites del prototipo

Los permisos de los usuarios se aplican dentro del programa. Sin embargo, una persona con acceso de escritura a los archivos locales podría modificarlos directamente.

El proyecto no incluye cifrado de datos, protección del sistema operativo, recuperación de contraseñas, autenticación multifactor (MFA) ni protección del registro de auditoría contra modificaciones externas.

Estas limitaciones corresponden al alcance de la aplicación académica, por lo que el prototipo no debe considerarse un sistema que ofrece seguridad completa.

No deben publicarse entornos virtuales, carpetas de caché, credenciales reales ni información personal de terceros.
