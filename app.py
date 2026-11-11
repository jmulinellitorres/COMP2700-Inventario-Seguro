"""BASE EDUCATIVA INSEGURA. Corregir los TODO antes de la entrega."""
import json
import os
import logging
import datetime
from seguridad import verificar_clave
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
DATOS = RAIZ / "inventario.json"
USUARIOS = RAIZ / "usuarios.json"
LOG = RAIZ / "auditoria.jsonl"


def cargar_inventario():
    try:
        return json.loads(DATOS.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print("Error: El archivo de inventario contiene JSON inválido.")
        return None
    except FileNotFoundError:
        print("Error: El archivo de inventario no existe.")
        return None
    except OSError:
        print("Error: No se pudo leer el archivo de inventario.")
        return None


def guardar_inventario(productos):
    DATOS.write_text(json.dumps(productos, indent=2), encoding="utf-8")


def registrar_evento(usuario, accion, resultado, **detalles):
    eventos_de_usuario = { "usuario": usuario,
                            "accion": accion,
                            "resultado": resultado,
                            "detalles": detalles,
                            "fecha/hora": datetime.datetime.now().astimezone().isoformat()
                          }
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(eventos_de_usuario)+"\n")


def autenticar(nombre, clave):
    usuarios = json.loads(USUARIOS.read_text(encoding="utf-8"))
    for usuario in usuarios:
        if usuario["usuario"] == nombre:
            if verificar_clave(usuario["hash"], clave):
                registrar_evento(nombre, "login", "exitoso")
                return {"usuario": nombre, "rol": usuario["rol"]}
    registrar_evento(nombre, "login", "fallido")
    print("Credenciales incorrectas.")
    return None


def consultar_inventario(sesion):
    if sesion is None:
        print("Session no valida")
        return 
    
    productos = cargar_inventario()
    if productos is None:
        return

    for producto in productos:
         print(producto["id"], producto["nombre"], producto["cantidad"])


def modificar_cantidad(sesion, identificador, entrada):
    if sesion is None or sesion["rol"] != "admin":
        if sesion is not None:
            nombre_usuario = sesion["usuario"]
        else:
            nombre_usuario = "sin_sesion"
        registrar_evento(
            nombre_usuario,
            "modificar",
            "rechazado",
            producto=identificador
        )
        print("No tiene permiso para modificar")
        return False
    try:
        cantidad = int(entrada)
    except ValueError:
        print("Error: Debe introducir un número entero.")
        return False
    if cantidad < 0 or cantidad > 1000:
        print("Error: La cantidad debe estar entre 0 y 1000.")
        return False
    productos = cargar_inventario()
    if productos is None:
        return False
    for producto in productos:
        if producto["id"] == identificador:
            anterior = producto["cantidad"]
            producto["cantidad"] = cantidad
            guardar_inventario(productos)
            registrar_evento(
                sesion["usuario"],
                "modificar",
                "exitoso",
                producto=identificador,
                anterior=anterior,
                nueva=cantidad
            )
            print("Cantidad actualizada.")
            return True
    print("Error: El identificador del producto no existe.")
    return False
    
    
def main():
    print("Inventario académico — BASE CON DEBILIDADES")
    print("Estudiante:", input("Escriba su nombre: "))
    sesion = None
    while True:
        if sesion is None:
            nombre = input("Usuario (o salir): ")
            if nombre == "salir":
                break
            sesion = autenticar(nombre, input("Contraseña de prueba: "))
            continue
        print("1. Consultar | 2. Modificar | 3. Cerrar sesión | 0. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            consultar_inventario(sesion)
        elif opcion == "2":
            identificador = input("ID del producto: ")
            entrada = input("Nueva cantidad: ")
            modificar_cantidad(sesion, identificador, entrada)
        elif opcion == "3":
            sesion = None
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
