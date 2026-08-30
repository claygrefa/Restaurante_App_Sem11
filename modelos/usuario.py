class Usuario:
    """
    Representa a una persona registrada que puede realizar compras en el sistema.
    """
    def __init__(self, identificacion: str, nombre: str, correo: str):
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    def a_diccionario(self) -> dict:
        """Convierte los datos del usuario en un diccionario para la persistencia JSON."""
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo
        }

    @classmethod
    def de_diccionario(cls, datos: dict) -> 'Usuario':
        """Crea una instancia de Usuario reconstruyéndola desde un diccionario JSON."""
        return cls(
            identificacion=datos["identificacion"],
            nombre=datos["nombre"],
            correo=datos["correo"]
        )