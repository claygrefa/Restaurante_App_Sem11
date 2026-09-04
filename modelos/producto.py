# modelos/producto.py
# Clase Producto: representa cada producto del restaurante.
# Guarda su codigo, nombre, precio y stock disponible.


class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int = 0):
        # Validaciones basicas para no permitir datos vacios o negativos.
        # Se usa ValueError como pide la guia para las validaciones de dominio.
        if not codigo or not str(codigo).strip():
            raise ValueError("El codigo del producto no puede estar vacio.")
        if not nombre or not str(nombre).strip():
            raise ValueError("El nombre del producto no puede estar vacio.")
        if precio is None or float(precio) < 0:
            raise ValueError("El precio no puede ser negativo.")
        if stock is None or int(stock) < 0:
            raise ValueError("El stock no puede ser negativo.")

        # Atributos con nombres descriptivos.
        self.codigo: str = str(codigo).strip()
        self.nombre: str = str(nombre).strip()
        self.precio: float = float(precio)
        self.stock: int = int(stock)

    def vender(self, cantidad: int) -> None:
        # Metodo que disminuye el stock cuando se realiza una venta valida.
        # La validacion completa se hace en el servicio Restaurante,
        # pero aqui reforzamos que nunca quede en negativo.
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser mayor que cero.")
        if cantidad > self.stock:
            raise ValueError("No hay stock suficiente para esta venta.")
        self.stock -= cantidad

    def agregar_stock(self, cantidad: int) -> None:
        # Metodo auxiliar para aumentar el stock (por ejemplo cuando se
        # registra o se reabastece un producto).
        if cantidad <= 0:
            raise ValueError("La cantidad a agregar debe ser mayor que cero.")
        self.stock += cantidad

    def convertir_a_diccionario(self) -> dict:
        # Convierte el objeto Producto a un diccionario compatible con JSON.
        # Se usa para poder guardarlo con json.dump().
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
        }

    @classmethod
    def desde_diccionario(cls, datos: dict) -> "Producto":
        # Reconstruye un objeto Producto a partir de un diccionario
        # obtenido con json.load(). Se controla KeyError como pide la guia.
        try:
            return cls(
                codigo=datos["codigo"],
                nombre=datos["nombre"],
                precio=datos["precio"],
                # .get() con valor 0 permite compatibilidad con productos
                # de semanas anteriores que aun no tenian stock.
                stock=datos.get("stock", 0),
            )
        except KeyError as e:
            raise KeyError(f"Falta la clave {e} al reconstruir un Producto.")

    def __str__(self) -> str:
        # Representacion legible del producto para mostrar en consola.
        return (
            f"[{self.codigo}] {self.nombre} - "
            f"Precio: ${self.precio:.2f} - Stock: {self.stock}"
        )
