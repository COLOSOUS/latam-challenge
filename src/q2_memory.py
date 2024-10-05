from typing import List, Tuple
import re
from collections import Counter




def q2_memory(file_path: str) -> List[Tuple[str, int]]:

    # Se inicializa contador
    emoji_counter = Counter()
    emoji_pattern = re.compile(r'[^\w\s,]')

    # Procesar línea por línea para minimizar el uso de memoria
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            emojis = emoji_pattern.findall(tweet['text'])
            emoji_counter.update(emojis)

    # Obtener los 10 emojis más comunes
    return emoji_counter.most_common(10)