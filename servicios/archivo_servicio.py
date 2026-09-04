import json

class ArchivoServicio:

    def cargar(self, ruta: str):
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Error: archivo JSON inválido.")
            return []
        except PermissionError:
            print("Error: no hay permisos para leer el archivo.")
            return []

    def guardar(self, ruta: str, datos: list):
        try:
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
        except PermissionError:
            print("Error: no hay permisos para escribir en el archivo.")
