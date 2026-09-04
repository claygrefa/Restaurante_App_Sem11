from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante

restaurante = Restaurante()

def menu():
    print("\n--- SISTEMA RESTAURANTE APP ---")
    print("1. Registrar usuario")
    print("2. Registrar producto")
    print("3. Vender producto")
    print("4. Consultar ventas por usuario")
    print("5. Salir")

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        identificacion = input("Identificación: ")
        nombre = input("Nombre: ")
        usuario = Usuario(identificacion, nombre)
        restaurante.registrar_usuario(usuario)

    elif opcion == "2":
        codigo = input("Código del producto: ")
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock inicial: "))
        producto = Producto(codigo, nombre, precio, stock)
        restaurante.registrar_producto(producto)

    elif opcion == "3":
        usuario_id = input("Identificación del usuario: ")
        codigo = input("Código del producto: ")
        cantidad = int(input("Cantidad: "))
        restaurante.vender_producto(codigo, usuario_id, cantidad)

    elif opcion == "4":
        usuario_id = input("Identificación del usuario: ")
        ventas = restaurante.ventas_por_usuario(usuario_id)
        print("\nVentas del usuario:")
        for v in ventas:
            print(f"Producto: {v.producto_codigo} | Cantidad: {v.cantidad}")

    elif opcion == "5":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")
