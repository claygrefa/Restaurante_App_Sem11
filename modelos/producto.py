# Clase Producto

class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int):
        if not codigo or not nombre:
            raise ValueError("Código y nombre no pueden estar vacíos.")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a cero.")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad: int):
        """Disminuye el stock solo si la cantidad es válida."""
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero.")
        if cantidad > self.stock:
            raise ValueError("Stock insuficiente.")
        self.stock -= cantidad

    def convertir_a_diccionario(self):
        """Convierte el objeto en un diccionario compatible con JSON."""
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }

    @staticmethod
    def desde_diccionario(data: dict):
        """Reconstruye un Producto desde un diccionario JSON."""
        return Producto(
            data["codigo"],
            data["nombre"],
            data["precio"],
            data["stock"]
        )
