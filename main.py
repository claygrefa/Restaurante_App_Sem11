# main.py
# Punto de entrada del programa restaurante_app (Semana 11).
# Coordina la interaccion por consola con el usuario y llama a los
# metodos del servicio Restaurante SIN modificar directamente las
# colecciones internas (como pide la guia).
#
# Toda la logica de negocio esta en servicios/restaurante.py.
# Toda la persistencia JSON esta en servicios/archivo_servicio.py.

from servicios import ArchivoServicio, Restaurante


def mostrar_menu() -> None:
    # Menu principal del sistema.
    print("\n=========== RESTAURANTE APP - SEMANA 11 ===========")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Registrar usuario")
    print("4. Listar usuarios")
    print("5. Vender producto")
    print("6. Consultar ventas por usuario")
    print("7. Listar todas las ventas")
    print("0. Salir")
    print("===================================================")


def opcion_registrar_producto(restaurante: Restaurante) -> None:
    # Solicita los datos del producto y llama al servicio para registrarlo.
    # Se usa input() como pide la guia (no datos quemados).
    print("\n--- Registrar producto ---")
    try:
        codigo = input("Codigo del producto: ").strip()
        nombre = input("Nombre del producto: ").strip()
        precio = float(input("Precio del producto: ").strip())
        stock = int(input("Stock inicial: ").strip())

        if restaurante.registrar_producto(codigo, nombre, precio, stock):
            print("Producto registrado correctamente.")
        else:
            print("Ya existe un producto con ese codigo.")
    except ValueError as e:
        # Se controlan ValueError propios de las validaciones o del casting.
        print(f"Datos invalidos: {e}")


def opcion_listar_productos(restaurante: Restaurante) -> None:
    print("\n--- Lista de productos ---")
    productos = restaurante.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return
    for producto in productos:
        print(producto)


def opcion_registrar_usuario(restaurante: Restaurante) -> None:
    print("\n--- Registrar usuario ---")
    try:
        identificacion = input("Identificacion del usuario: ").strip()
        nombre = input("Nombre del usuario: ").strip()
        correo = input("Correo del usuario: ").strip()

        if restaurante.registrar_usuario(identificacion, nombre, correo):
            print("Usuario registrado correctamente.")
        else:
            print("Ya existe un usuario con esa identificacion.")
    except ValueError as e:
        print(f"Datos invalidos: {e}")


def opcion_listar_usuarios(restaurante: Restaurante) -> None:
    print("\n--- Lista de usuarios ---")
    usuarios = restaurante.listar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    for usuario in usuarios:
        print(usuario)


def opcion_vender_producto(restaurante: Restaurante) -> None:
    # Operacion PRINCIPAL de la Semana 11.
    # Sigue el flujo esperado indicado por el profesor:
    #  Usuario selecciona la opcion vender
    #    -> main.py solicita identificacion, producto y cantidad
    #    -> Restaurante busca usuario y producto
    #    -> Se valida cantidad y stock
    #    -> Se crea Venta y se agrega a la coleccion
    #    -> Producto disminuye su stock
    #    -> Se guardan ventas.json y productos.json
    #    -> El sistema muestra el resultado
    print("\n--- Vender producto ---")
    try:
        identificacion_usuario = input("Identificacion del usuario: ").strip()
        codigo_producto = input("Codigo del producto: ").strip()
        cantidad = int(input("Cantidad a vender: ").strip())

        ok = restaurante.vender_producto(
            codigo_producto=codigo_producto,
            identificacion_usuario=identificacion_usuario,
            cantidad=cantidad,
        )

        if ok:
            producto = restaurante.buscar_producto(codigo_producto)
            print("Venta registrada correctamente.")
            print(f"Stock actualizado de '{producto.nombre}': {producto.stock}")
        else:
            # Se explica al usuario por que no se realizo la venta.
            print(
                "No fue posible realizar la venta. Verifique que el usuario "
                "y el producto existan, que la cantidad sea mayor a 0 y "
                "que exista stock suficiente."
            )
    except ValueError as e:
        print(f"Datos invalidos: {e}")


def opcion_consultar_ventas_por_usuario(restaurante: Restaurante) -> None:
    # Consulta las ventas asociadas unicamente a un usuario dado.
    print("\n--- Consultar ventas por usuario ---")
    identificacion_usuario = input("Identificacion del usuario: ").strip()

    usuario = restaurante.buscar_usuario(identificacion_usuario)
    if usuario is None:
        print("El usuario indicado no existe.")
        return

    ventas = restaurante.consultar_ventas_por_usuario(identificacion_usuario)
    if not ventas:
        print(f"El usuario {usuario.nombre} no tiene ventas registradas.")
        return

    print(f"Ventas del usuario {usuario.nombre}:")
    for venta in ventas:
        # Buscamos el producto para mostrar tambien el nombre y no solo el codigo.
        producto = restaurante.buscar_producto(venta.producto_codigo)
        nombre_producto = producto.nombre if producto is not None else "?"
        print(
            f"  - Codigo: {venta.producto_codigo} | "
            f"Producto: {nombre_producto} | "
            f"Cantidad: {venta.cantidad}"
        )


def opcion_listar_ventas(restaurante: Restaurante) -> None:
    print("\n--- Todas las ventas registradas ---")
    ventas = restaurante.listar_ventas()
    if not ventas:
        print("No hay ventas registradas.")
        return
    for venta in ventas:
        print(venta)


def main() -> None:
    # Se crea el servicio de archivos y se le entrega al servicio Restaurante.
    # Al construir el Restaurante, este recupera productos, usuarios y ventas
    # desde los archivos JSON (o inicia con listas vacias si aun no existen).
    archivo_servicio = ArchivoServicio(
        ruta_productos="datos/productos.json",
        ruta_usuarios="datos/usuarios.json",
        ruta_ventas="datos/ventas.json",
    )
    restaurante = Restaurante(archivo_servicio)

    # Bucle principal del menu por consola.
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            opcion_registrar_producto(restaurante)
        elif opcion == "2":
            opcion_listar_productos(restaurante)
        elif opcion == "3":
            opcion_registrar_usuario(restaurante)
        elif opcion == "4":
            opcion_listar_usuarios(restaurante)
        elif opcion == "5":
            opcion_vender_producto(restaurante)
        elif opcion == "6":
            opcion_consultar_ventas_por_usuario(restaurante)
        elif opcion == "7":
            opcion_listar_ventas(restaurante)
        elif opcion == "0":
            print("Saliendo del programa. Hasta pronto.")
            break
        else:
            print("Opcion no valida. Intente nuevamente.")


# Punto de entrada estandar del script.
if __name__ == "__main__":
    main()
