from typing import List, Tuple
import re
from collections import Counter
from utils import load_data


def q2_time(file_path: str) -> List[Tuple[str, int]]:

    # Cargar los datos completos
    data = load_data(file_path)

    # Inicializamos un contador para los emojis
    emoji_counter = Counter()

    # Expresión regular para encontrar emojis
    emoji_pattern = re.compile(r'[^\w\s,]')

    # Recorremos cada tweet
    for tweet in data:
        emojis = emoji_pattern.findall(tweet['text'])
        emoji_counter.update(emojis)

    # Obtener los 10 emojis más comunes
    return emoji_counter.most_common(10)