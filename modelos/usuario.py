# modelos/usuario.py
# Clase Usuario: representa a la persona registrada que puede
# realizar una compra dentro del restaurante.
# Se conserva la validacion de semanas anteriores y se agrega
# la persistencia JSON pedida en la Semana 11.


class Usuario:
    def __init__(self, identificacion: str, nombre: str, correo: str):
        # Validaciones basicas para no permitir campos vacios.
        if not identificacion or not str(identificacion).strip():
            raise ValueError("La identificacion del usuario no puede estar vacia.")
        if not nombre or not str(nombre).strip():
            raise ValueError("El nombre del usuario no puede estar vacio.")
        if not correo or "@" not in str(correo):
            raise ValueError("El correo del usuario no es valido.")

        # Atributos descriptivos.
        self.identificacion: str = str(identificacion).strip()
        self.nombre: str = str(nombre).strip()
        self.correo: str = str(correo).strip()

    def convertir_a_diccionario(self) -> dict:
        # Convierte el objeto Usuario a un diccionario compatible con JSON.
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
        }

    @classmethod
    def desde_diccionario(cls, datos: dict) -> "Usuario":
        # Reconstruye un objeto Usuario desde un diccionario cargado de JSON.
        try:
            return cls(
                identificacion=datos["identificacion"],
                nombre=datos["nombre"],
                correo=datos["correo"],
            )
        except KeyError as e:
            raise KeyError(f"Falta la clave {e} al reconstruir un Usuario.")

    def __str__(self) -> str:
        return f"{self.identificacion} - {self.nombre} ({self.correo})"
