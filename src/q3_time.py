from typing import List, Tuple
import re
from collections import Counter
import pandas as pd
def q3_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Función que obtiene los 10 usuarios (@) más mencionados en los tweets, optimizada para tiempo de ejecución.
    
    Parámetros:
    file_path (str): Ruta al archivo JSON que contiene los tweets.
    
    Retorna:
    List[Tuple[str, int]]: Lista de tuplas con el usuario y su conteo de menciones.
    Formato del retorno: [(usuario, menciones), (usuario, menciones), ...]
    
    Las suposiciones son las siguientes:
    - Cada tweet tiene un campo 'content' que contiene las menciones con '@'.
    - Se utiliza una expresión regular para detectar menciones (@usuario).
    - El archivo puede cargarse completamente en memoria.
    """
    
    # Cargar el archivo JSON utilizando pandas
    df = pd.read_json(file_path, lines=True)

    # Inicializamos un contador para los usuarios mencionados
    mention_counter = Counter()

    # Expresión regular para encontrar menciones
    mention_pattern = re.compile(r'@\w+')

    # Filtramos las filas que tienen texto válido y aplicamos la búsqueda de menciones
    for text in df['content'].dropna():  # Asegurarse de no tener valores nulos
        mentions = mention_pattern.findall(text)
        mention_counter.update(mentions)

    # Obtener los 10 usuarios más mencionados
    return mention_counter.most_common(10)