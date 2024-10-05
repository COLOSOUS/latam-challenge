from typing import List, Tuple
from collections import defaultdict
import emoji
import json


def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Función que obtiene los 10 emojis más usados en los tweets, optimizada para uso de memoria.
    Se procesa el archivo línea por línea.
    
    Parámetros:
    file_path (str): Ruta al archivo JSON que contiene los tweets.
    
    Retorna:
    List[Tuple[str, int]]: Lista de tuplas con el emoji y su conteo.
    Formato del retorno: [(emoji, conteo), (emoji, conteo), ...]
    
    Las suposiciones son las siguientes:
    - Se procesan los tweets de forma incremental.
    - Cada línea es un JSON válido.
    - Los emojis se extraen usando la misma expresión regular.
    """
     # Diccionario para contar los emojis
    emoji_counter = defaultdict(int)
    
    # Abrir el archivo en modo de lectura
    with open(file_path, 'r', encoding='utf-8') as file:
        # Leer cada línea como un objeto JSON
        for line in file:
            try:
                tweet = json.loads(line.strip())
                tweet_text = tweet.get("content", "")  # Obtener el texto del tweet
                
                # Contar los emojis en el texto
                for char in tweet_text:
                    if char in emoji.EMOJI_DATA:
                        emoji_counter[char] += 1
            except json.JSONDecodeError:
                # Ignorar cualquier línea que no se pueda decodificar como JSON
                continue
    
    # Obtener los 10 emojis más frecuentes
    top_10_emojis = sorted(emoji_counter.items(), key=lambda x: x[1], reverse=True)[:10]
    
    return top_10_emojis