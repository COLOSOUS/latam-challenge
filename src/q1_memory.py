from typing import List, Tuple
from datetime import datetime
from collections import Counter
import json

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Función que obtiene las 10 fechas con más tweets y el usuario que más tweets publicó en cada una de esas fechas,
    para el caso se optimiza la función para la memoria al procesar el archivo línea por línea sin cargar todo.

    Parámetros:
    file_path (str): Ruta al archivo JSON que contiene los tweets.

    Retorna:
    List[Tuple[datetime.date, str]]: Lista de tuplas con la fecha y el usuario que más tweets publicó en cada una de las 10 fechas con más tweets.
    Formato del retorno: [(fecha, usuario), (fecha, usuario), ...]

    Las suposiciones son las siguientes:
    - El archivo JSON se puede procesar de manera incremental (streaming).
    - El formato del archivo sigue siendo consistente y no tiene datos corruptos.
    - La estructura es idéntica a la de la versión optimizada para tiempo.
    """
    date_counter = Counter()
    user_per_date = {}
    
    # Leer archivo en modo streaming
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            date = datetime.strptime(tweet['date'].split("T")[0], "%Y-%m-%d").date()
            user = tweet['user']['username']
            
            date_counter[date] += 1
            
            if date not in user_per_date:
                user_per_date[date] = Counter()
            user_per_date[date][user] += 1
    
    # Obtener las top 10 fechas con más tweets
    top_dates = date_counter.most_common(10)
    
    # Encontrar el usuario más activo en esas fechas
    result = [(date, user_per_date[date].most_common(1)[0][0]) for date, _ in top_dates]
    return result
