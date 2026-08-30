from servicios.restaurante import Restaurante

def mostrar_menu():
    """Muestra las opciones disponibles en la consola para el usuario."""
    print("\n--- SISTEMA RESTAURANTE_APP (SEMANA 11) ---")
    print("1. Registrar usuario")
    print("2. Registrar producto")
    print("3. Realizar venta")
    print("4. Consultar ventas de un usuario")
    print("5. Listar productos y stock")
    print("6. Listar usuarios")
    print("7. Salir")

def main():
    """Punto de entrada principal que coordina la interfaz por consola y la interacción con el servicio."""
    restaurante = Restaurante()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            cedula = input("Ingrese identificación del usuario: ").strip()
            nombre = input("Ingrese nombre del usuario: ").strip()
            correo = input("Ingrese correo del usuario: ").strip()
            if restaurante.registrar_usuario(cedula, nombre, correo):
                print("¡Usuario registrado y guardado con éxito!")
            else:
                print("Error: Ya existe un usuario con esa identificación.")

        elif opcion == "2":
            codigo = input("Ingrese código del producto: ").strip()
            nombre = input("Ingrese nombre del producto: ").strip()
            try:
                precio = float(input("Ingrese precio: "))
                stock = int(input("Ingrese stock inicial: "))
                if restaurante.registrar_producto(codigo, nombre, precio, stock):
                    print("¡Producto registrado y guardado con éxito!")
                else:
                    print("Error: Ya existe un producto con ese código.")
            except ValueError as e:
                print(f"Error en los datos ingresados: {e}")

        elif opcion == "3":
            cedula = input("Ingrese identificación del usuario: ").strip()
            codigo = input("Ingrese código del producto: ").strip()
            try:
                cantidad = int(input("Ingrese cantidad a vender: "))
                if restaurante.vender_producto(codigo, cedula, cantidad):
                    print("¡Venta realizada y registrada correctamente!")
                else:
                    print("Error: Venta rechazada (verifique que el usuario y producto existan, o que haya stock suficiente).")
            except ValueError as e:
                print(f"Error de valor: {e}")

        elif opcion == "4":
            cedula = input("Ingrese identificación del usuario a consultar: ").strip()
            ventas = restaurante.consultar_ventas_usuario(cedula)
            if not ventas:
                print("No se encontraron ventas para este usuario.")
            else:
                print(f"\n--- Ventas del usuario {cedula} ---")
                for v in ventas:
                    prod = restaurante.buscar_producto(v.producto_codigo)
                    nombre_prod = prod.nombre if prod else "Desconocido"
                    print(f"- Producto: {nombre_prod} (Código: {v.producto_codigo}) | Cantidad: {v.cantidad}")

        elif opcion == "5":
            print("\n--- LISTA DE PRODUCTOS ---")
            for p in restaurante.productos:
                print(f"Código: {p.codigo} | Nombre: {p.nombre} | Precio: ${p.precio:.2f} | Stock: {p.stock}")

        elif opcion == "6":
            print("\n--- LISTA DE USUARIOS ---")
            for u in restaurante.usuarios:
                print(f"ID: {u.identificacion} | Nombre: {u.nombre} | Correo: {u.correo}")

        elif opcion == "7":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()