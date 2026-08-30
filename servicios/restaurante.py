from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio

class Restaurante:
    """
    Servicio principal que administra las colecciones de objetos, las reglas de negocio
    y la coordinación con la capa de persistencia.
    """
    def __init__(self):
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []
        self._ventas: list[Venta] = []
        self.cargar_datos()  # Carga inicial al instanciar el servicio

    def cargar_datos(self):
        """Recupera los datos de los tres archivos JSON al iniciar la aplicación."""
        prods_json = ArchivoServicio.cargar_json("productos.json")
        self._productos = [Producto.de_diccionario(p) for p in prods_json]

        usrs_json = ArchivoServicio.cargar_json("usuarios.json")
        self._usuarios = [Usuario.de_diccionario(u) for u in usrs_json]

        ventas_json = ArchivoServicio.cargar_json("ventas.json")
        self._ventas = [Venta.de_diccionario(v) for v in ventas_json]

    def guardar_productos(self):
        """Actualiza el archivo productos.json con el estado actual."""
        datos = [p.a_diccionario() for p in self._productos]
        ArchivoServicio.guardar_json("productos.json", datos)

    def guardar_usuarios(self):
        """Actualiza el archivo usuarios.json con el estado actual."""
        datos = [u.a_diccionario() for u in self._usuarios]
        ArchivoServicio.guardar_json("usuarios.json", datos)

    def guardar_ventas(self):
        """Actualiza el archivo ventas.json con el registro de operaciones."""
        datos = [v.a_diccionario() for v in self._ventas]
        ArchivoServicio.guardar_json("ventas.json", datos)

    def registrar_usuario(self, identificacion: str, nombre: str, correo: str) -> bool:
        """Registra un nuevo usuario si no existe duplicado y guarda los cambios."""
        if any(u.identificacion == identificacion for u in self._usuarios):
            return False
        usuario = Usuario(identificacion, nombre, correo)
        self._usuarios.append(usuario)
        self.guardar_usuarios()
        return True

    def registrar_producto(self, codigo: str, nombre: str, precio: float, stock: int) -> bool:
        """Registra un nuevo producto si el código es único y guarda los cambios."""
        if any(p.codigo == codigo for p in self._productos):
            return False
        producto = Producto(codigo, nombre, precio, stock)
        self._productos.append(producto)
        self.guardar_productos()
        return True

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        """Busca y retorna un objeto Usuario según su identificación."""
        for usuario in self._usuarios:
            if usuario.identificacion == identificacion:
                return usuario
        return None

    def buscar_producto(self, codigo: str) -> Producto | None:
        """Busca y retorna un objeto Producto según su código."""
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto
        return None

    def vender_producto(self, codigo_producto: str, identificacion_usuario: str, cantidad: int) -> bool:
        """
        Ejecuta la regla de negocio de venta: valida existencia, stock disponible,
        registra la venta en la colección, reduce el stock y persiste ambos archivos afectados.
        """
        usuario = self.buscar_usuario(identificacion_usuario)
        producto = self.buscar_producto(codigo_producto)

        # Validaciones requeridas
        if usuario is None or producto is None:
            return False

        if cantidad <= 0 or producto.stock < cantidad:
            return False

        # Creación y registro de la venta
        venta = Venta(usuario.identificacion, producto.codigo, cantidad)
        self._ventas.append(venta)
        producto.vender(cantidad)  # Disminuye el stock de forma segura

        # Persistir colecciones modificadas (ventas y productos)
        self.guardar_ventas()
        self.guardar_productos()
        return True

    def consultar_ventas_usuario(self, identificacion_usuario: str) -> list[Venta]:
        """Fringa y devuelve las ventas asociadas a una identificación de usuario específica."""
        ventas_usuario: list[Venta] = []
        for venta in self._ventas:
            if venta.usuario_id == identificacion_usuario:
                ventas_usuario.append(venta)
        return ventas_usuario

    @property
    def productos(self):
        """Retorna la lista de productos del sistema."""
        return self._productos

    @property
    def usuarios(self):
        """Retorna la lista de usuarios registrados."""
        return self._usuarios