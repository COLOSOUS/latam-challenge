from typing import List, Tuple
import re
from collections import Counter
from utils import load_data
import emoji
import pandas as pd

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Función que obtiene los 10 emojis más usados en los tweets, optimizada para tiempo de ejecución.
    
    Parámetros:
    file_path (str): Ruta al archivo JSON que contiene los tweets.
    
    Retorna:
    List[Tuple[str, int]]: Lista de tuplas con el emoji y su conteo.
    Formato del retorno: [(emoji, conteo), (emoji, conteo), ...]
    
    Las suposiciones son las siguientes:
    - Cada tweet tiene un campo 'text' que contiene el texto donde pueden aparecer los emojis.
    - Se utiliza una expresión regular para detectar emojis.
    - El archivo puede cargarse completamente en memoria.
    """
    # Cargar los datos usando pandas (rápido en carga pero consume memoria)
    data = pd.read_json(file_path, lines=True)
    
    # Filtrar los tweets que contienen emojis
    all_emojis = []
    
    # Usar pandas para iterar rápidamente por cada tweet
    for tweet in data['content']:
        all_emojis += [char for char in tweet if char in emoji.EMOJI_DATA]

    # Contar la frecuencia de los emojis
    emoji_count = Counter(all_emojis)
    
    # Obtener los 10 emojis más frecuentes
    top_10_emojis = emoji_count.most_common(10)
    
    return top_10_emojis