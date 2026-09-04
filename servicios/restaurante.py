# servicios/restaurante.py
# Servicio Restaurante: administra las colecciones (productos, usuarios y ventas)
# y ejecuta las reglas de negocio del sistema.
#
# Aqui vive TODA la logica de negocio:
#  - registrar productos y usuarios,
#  - buscar productos y usuarios,
#  - realizar ventas (vender_producto),
#  - consultar ventas por usuario,
#  - mantener los archivos JSON sincronizados usando ArchivoServicio.
#
# main.py NO debe modificar las colecciones directamente: siempre
# lo hace a traves de estos metodos.

from typing import List, Optional

from modelos import Producto, Usuario, Venta
from servicios.archivo_servicio import ArchivoServicio


class Restaurante:
    def __init__(self, archivo_servicio: ArchivoServicio):
        # Guardamos el servicio de archivos como dependencia.
        self._archivo = archivo_servicio

        # Colecciones internas de objetos (NO diccionarios, como pide la guia).
        # Se recuperan al iniciar la aplicacion desde los archivos JSON.
        self._productos: List[Producto] = self._archivo.cargar_productos()
        self._usuarios: List[Usuario] = self._archivo.cargar_usuarios()
        self._ventas: List[Venta] = self._archivo.cargar_ventas()

    # -----------------------------------------------------------------
    # PRODUCTOS
    # -----------------------------------------------------------------
    def registrar_producto(
        self, codigo: str, nombre: str, precio: float, stock: int
    ) -> bool:
        # Registra un producto nuevo. Si ya existe el codigo, no lo agrega.
        if self.buscar_producto(codigo) is not None:
            return False
        producto = Producto(codigo, nombre, precio, stock)
        self._productos.append(producto)
        # Persistimos productos.json despues de modificar la coleccion.
        self._archivo.guardar_productos(self._productos)
        return True

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        # Recorre la coleccion de productos y devuelve el que coincida con
        # el codigo, o None si no existe. Uso claro de coleccion.
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto
        return None

    def listar_productos(self) -> List[Producto]:
        # Devuelve una copia de la coleccion de productos.
        return list(self._productos)

    # -----------------------------------------------------------------
    # USUARIOS
    # -----------------------------------------------------------------
    def registrar_usuario(
        self, identificacion: str, nombre: str, correo: str
    ) -> bool:
        # Registra un usuario nuevo. Si ya existe la identificacion, no lo agrega.
        if self.buscar_usuario(identificacion) is not None:
            return False
        usuario = Usuario(identificacion, nombre, correo)
        self._usuarios.append(usuario)
        # Persistimos usuarios.json despues de modificar la coleccion.
        self._archivo.guardar_usuarios(self._usuarios)
        return True

    def buscar_usuario(self, identificacion: str) -> Optional[Usuario]:
        # Recorre la coleccion de usuarios y devuelve el que coincida.
        for usuario in self._usuarios:
            if usuario.identificacion == identificacion:
                return usuario
        return None

    def listar_usuarios(self) -> List[Usuario]:
        return list(self._usuarios)

    # -----------------------------------------------------------------
    # VENTAS  (operacion principal de la Semana 11)
    # -----------------------------------------------------------------
    def vender_producto(
        self, codigo_producto: str, identificacion_usuario: str, cantidad: int
    ) -> bool:
        # Operacion principal de la Semana 11.
        # Antes de registrar la venta se debe comprobar:
        #  - Que el usuario exista.
        #  - Que el producto exista.
        #  - Que la cantidad sea mayor que cero.
        #  - Que exista stock suficiente.
        usuario = self.buscar_usuario(identificacion_usuario)
        producto = self.buscar_producto(codigo_producto)

        # Si el usuario o el producto no existen, no se puede vender.
        if usuario is None or producto is None:
            return False

        # Si la cantidad no es valida o no hay stock suficiente, no se puede vender.
        if cantidad <= 0 or producto.stock < cantidad:
            return False

        # Se crea el objeto Venta que representa la relacion Usuario -> Producto.
        venta = Venta(usuario.identificacion, producto.codigo, cantidad)

        # Se agrega la venta a la coleccion de ventas.
        self._ventas.append(venta)

        # Se disminuye el stock del producto llamando a su propio metodo.
        producto.vender(cantidad)

        # Una sola operacion modifica DOS colecciones (ventas y productos),
        # por lo tanto persistimos ambos archivos JSON.
        self._archivo.guardar_ventas(self._ventas)
        self._archivo.guardar_productos(self._productos)
        return True

    def consultar_ventas_por_usuario(
        self, identificacion_usuario: str
    ) -> List[Venta]:
        # Consulta que devuelve unicamente las ventas asociadas a un usuario.
        # Demuestra el uso de colecciones para RECORRER, COMPARAR y FILTRAR.
        ventas_usuario: List[Venta] = []
        for venta in self._ventas:
            if venta.usuario_id == identificacion_usuario:
                ventas_usuario.append(venta)
        return ventas_usuario

    def listar_ventas(self) -> List[Venta]:
        # Devuelve una copia de la coleccion de ventas.
        return list(self._ventas)
