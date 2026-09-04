from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio

class Restaurante:

    def __init__(self):
        self.archivo = ArchivoServicio()

        self._productos = [Producto.desde_diccionario(p)
                           for p in self.archivo.cargar("datos/productos.json")]

        self._usuarios = [Usuario.desde_diccionario(u)
                          for u in self.archivo.cargar("datos/usuarios.json")]

        self._ventas = [Venta.desde_diccionario(v)
                        for v in self.archivo.cargar("datos/ventas.json")]

    def buscar_producto(self, codigo: str):
        for p in self._productos:
            if p.codigo == codigo:
                return p
        return None

    def buscar_usuario(self, identificacion: str):
        for u in self._usuarios:
            if u.identificacion == identificacion:
                return u
        return None

    def registrar_producto(self, producto: Producto):
        self._productos.append(producto)
        self.guardar_productos()

    def registrar_usuario(self, usuario: Usuario):
        self._usuarios.append(usuario)
        self.guardar_usuarios()

    def vender_producto(self, codigo_producto: str, identificacion_usuario: str, cantidad: int):
        usuario = self.buscar_usuario(identificacion_usuario)
        producto = self.buscar_producto(codigo_producto)

        if usuario is None or producto is None:
            print("Error: usuario o producto no existen.")
            return False

        if cantidad <= 0:
            print("Error: cantidad inválida.")
            return False

        if producto.stock < cantidad:
            print("Error: stock insuficiente.")
            return False

        venta = Venta(usuario.identificacion, producto.codigo, cantidad)
        self._ventas.append(venta)

        producto.vender(cantidad)

        self.guardar_productos()
        self.guardar_ventas()

        print("Venta registrada correctamente.")
        return True

    def ventas_por_usuario(self, identificacion: str):
        return [v for v in self._ventas if v.usuario_id == identificacion]

    def guardar_productos(self):
        datos = [p.convertir_a_diccionario() for p in self._productos]
        self.archivo.guardar("datos/productos.json", datos)

    def guardar_usuarios(self):
        datos = [u.convertir_a_diccionario() for u in self._usuarios]
        self.archivo.guardar("datos/usuarios.json", datos)

    def guardar_ventas(self):
        datos = [v.convertir_a_diccionario() for v in self._ventas]
        self.archivo.guardar("datos/ventas.json", datos)
