# Clase Usuario 

class Usuario:
    def __init__(self, identificacion: str, nombre: str):
        if not identificacion or not nombre:
            raise ValueError("Identificación y nombre no pueden estar vacíos.")

        self.identificacion = identificacion
        self.nombre = nombre

    def convertir_a_diccionario(self):
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre
        }

    @staticmethod
    def desde_diccionario(data: dict):
        return Usuario(
            data["identificacion"],
            data["nombre"]
        )
