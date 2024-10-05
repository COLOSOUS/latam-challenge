import json

def load_data(file_path: str):
    """
    Carga y procesa datos desde un archivo JSON.
    
    Args:
    - file_path (str): Ruta al archivo JSON.

    Returns:
    - list: Lista de diccionarios de tweets procesados.
    
    Nota:
    - Este archivo debe ser usado por todas las funciones de procesamiento que necesiten cargar datos JSON.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data