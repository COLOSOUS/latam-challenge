from typing import List, Tuple
from collections import Counter
from datetime import datetime
from utils import load_data

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:

    # Cargar datos del archivo completo
    data = load_data(file_path)
    
    # Contar fechas de tweets
    date_counter = Counter()
    user_per_date = {}
    
    for tweet in data:
        date = datetime.strptime(tweet['created_at'], "%Y-%m-%d").date()
        user = tweet['user']['screen_name']
        
        date_counter[date] += 1
        
        if date not in user_per_date:
            user_per_date[date] = Counter()
        user_per_date[date][user] += 1
    
    # Obtener las top 10 fechas con más tweets
    top_dates = date_counter.most_common(10)