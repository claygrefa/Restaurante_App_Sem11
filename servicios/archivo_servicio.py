import json
import os

class ArchivoServicio:
    """
    Servicio encargado de centralizar la lectura y escritura segura en archivos JSON,
    manejando las excepciones requeridas por la guía.
    """
    @staticmethod
    def asegurar_directorio():
        """Crea la carpeta 'datos' si no existe en el proyecto."""
        if not os.path.exists("datos"):
            os.makedirs("datos")

    @staticmethod
    def cargar_json(nombre_archivo: str) -> list:
        """Lee un archivo JSON y devuelve su contenido en forma de lista. Maneja excepciones de archivos."""
        ArchivoServicio.asegurar_directorio()
        ruta = os.path.join("datos", nombre_archivo)
        
        if not os.path.exists(ruta):
            return []  # Si no existe, retorna lista vacía para que la app inicie
        
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except (FileNotFoundError, json.JSONDecodeError, PermissionError) as e:
            print(f"Aviso al cargar {nombre_archivo}: {e}. Se inicializa con lista vacía.")
            return []

    @staticmethod
    def guardar_json(nombre_archivo: str, datos: list):
        """Guarda una lista de diccionarios en un archivo JSON específico de forma segura."""
        ArchivoServicio.asegurar_directorio()
        ruta = os.path.join("datos", nombre_archivo)
        
        try:
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
        except (PermissionError, IOError) as e:
            print(f"Error al guardar {nombre_archivo}: {e}")