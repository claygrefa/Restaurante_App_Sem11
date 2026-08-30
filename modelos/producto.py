class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, valor: int):
        if valor < 0:
            raise ValueError("El stock no puede ser negativo.")
        self._stock = valor

    def vender(self, cantidad: int):
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser mayor a cero.")
        if cantidad > self._stock:
            raise ValueError("Stock insuficiente.")
        self._stock -= cantidad

    def a_diccionario(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }

    @classmethod
    def de_diccionario(cls, datos: dict) -> 'Producto':
        return cls(
            codigo=datos["codigo"],
            nombre=datos["nombre"],
            precio=float(datos["precio"]),
            stock=int(datos["stock"])
        )