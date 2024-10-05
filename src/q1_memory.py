from typing import List, Tuple
from datetime import datetime
from collections import Counter
import json

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:

    date_counter = Counter()
    user_per_date = {}
    
    # Leer archivo en modo streaming
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            date = datetime.strptime(tweet['created_at'], "%Y-%m-%d").date()
            user = tweet['user']['screen_name']
            
            date_counter[date] += 1
            
            if date not in user_per_date:
                user_per_date[date] = Counter()
            user_per_date[date][user] += 1
    
    # Obtener las top 10 fechas con más tweets
    top_dates = date_counter.most_common(10)
    
    # Encontrar el usuario más activo en esas fechas
    result = [(date, user_per_date[date].most_common(1)[0][0]) for date, _ in top_dates]