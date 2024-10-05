from typing import List, Tuple
from collections import Counter
from datetime import datetime
from utils import load_data
import pandas as pd
def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Función que obtiene las 10 fechas con más tweets y el usuario que más tweets publicó en esas fechas.

    Parámetros:
    file_path (str): Ruta al archivo JSON que contiene los tweets.

    Retorna:
    List[Tuple[datetime.date, str]]: Lista de tuplas con la fecha y el usuario que más tweets publicó en cada una de las 10 fechas con más tweets.
    Formato del retorno: [(fecha, usuario), (fecha, usuario), ...]

    Las suposiciones son las siguientes:
    - El archivo JSON contiene una lista de tweets donde cada tweet tiene una clave 'created_at' en formato "YYYY-MM-DD" y un 'user' con clave 'screen_name'.
    - El archivo puede ser grande, pero la memoria disponible permite cargarlo completamente en esta versión optimizada para tiempo.
    - La estructura del archivo es válida y no hay datos corruptos.
   
    # Cargar datos del archivo completo
    data = load_data(file_path)
    
    # Contar fechas de tweets
    date_counter = Counter()
    user_per_date = {}
    
    for tweet in data:
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
    """
    # Cargar datos con pandas
    data = pd.read_json(file_path, lines=True)

    # Extraer solo la fecha de 'created_at' y agregarla como una nueva columna
    data['date'] = pd.to_datetime(data['date']).dt.date

    # Contar el número de tweets por fecha
    date_counts = data['date'].value_counts()

    # Obtener las 10 fechas con más tweets
    top_dates = date_counts.nlargest(10)

    # Contar el usuario con más tweets por cada fecha
    user_per_date = data.groupby(['date', data['user'].apply(lambda x: x['username'])]).size().groupby(level=0).idxmax().apply(lambda x: x[1])
    # Formar el resultado final
    result = {date: {'count': count, 'top_user': user_per_date[date]} for date, count in top_dates.items()}

    return result