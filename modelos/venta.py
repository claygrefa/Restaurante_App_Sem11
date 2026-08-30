class Venta:
    """
    Entidad que representa la relación e historial de compra entre un Usuario y un Producto.
    """
    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int):
        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo
        self.cantidad = cantidad

    def a_diccionario(self) -> dict:
        """Serializa la venta a un formato de diccionario apto para JSON."""
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad
        }

    @classmethod
    def de_diccionario(cls, datos: dict) -> 'Venta':
        """Instancia un objeto Venta utilizando los datos almacenados en JSON."""
        return cls(
            usuario_id=datos["usuario_id"],
            producto_codigo=datos["producto_codigo"],
            cantidad=int(datos["cantidad"])
        )