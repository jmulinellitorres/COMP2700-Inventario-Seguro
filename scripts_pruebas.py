import app
#Script para pregunta 4
print("Inventario académico — BASE CON DEBILIDADES")
print("Estudiante: Jose A. Mulinelli Torres")

print("\nPRUEBA 1: Usuario sin permisos")
sesion = app.autenticar("user", "UserDemo2700!")
app.modificar_cantidad(sesion, "P001", "99")

print("\nPRUEBA 2: Modificación sin sesión")
app.modificar_cantidad(None, "P001", "99")

print("\nPRUEBA 3: Consulta sin sesión")
app.consultar_inventario(None)

print("\nVERIFICACIÓN DEL INVENTARIO")
productos = app.cargar_inventario()

for producto in productos:
    if producto["id"] == "P001":
        print("Producto:", producto["id"])
        print("Cantidad final:", producto["cantidad"])

print("\nPRUEBAS FINALIZADAS")