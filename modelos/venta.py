# Clase Venta 
# Representa la relación Usuario + Producto

class Venta:
    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero.")

        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo
        self.cantidad = cantidad

    def convertir_a_diccionario(self):
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad
        }

    @staticmethod
    def desde_diccionario(data: dict):
        return Venta(
            data["usuario_id"],
            data["producto_codigo"],
            data["cantidad"]
        )
