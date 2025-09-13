import re
from translation import translation_user_input

#Função para normalizar a pergunta
def input_normalization(query: str) -> str:

    query = translation_user_input(query)
    query = query.lower()
    query = re.sub(r"[^a-zA-Z0-9áéíóúâêîôûãõàèìòùç ,\?]", "", query)
    query = query.strip()
    
    return query