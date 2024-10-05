from typing import List, Tuple
import emoji
from collections import defaultdict
import re
from collections import Counter
import json

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Función que obtiene los 10 usuarios (@) más mencionados en los tweets, optimizada para uso de memoria.
    Se procesa el archivo línea por línea.
    
    Parámetros:
    file_path (str): Ruta al archivo JSON que contiene los tweets.
    
    Retorna:
    List[Tuple[str, int]]: Lista de tuplas con el usuario y su conteo de menciones.
    Formato del retorno: [(usuario, menciones), (usuario, menciones), ...]
    
    Las suposiciones son las siguientes:
    - Se procesan los tweets de forma incremental.
    - Cada línea es un JSON válido.
    - Las menciones se extraen usando la misma expresión regular.
    """
    mention_counter = Counter()
    mention_pattern = re.compile(r'@\w+')

    # Procesar línea por línea para minimizar el uso de memoria
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            mentions = mention_pattern.findall(tweet['content'])
            mention_counter.update(mentions)

    # Obtener los 10 usuarios más mencionados
    return mention_counter.most_common(10)