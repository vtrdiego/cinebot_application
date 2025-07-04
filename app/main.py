from search_data import search_answer
from translation import translation_response_model
from response_llm import response_model
from normalization import input_normalization
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_chatbot_pipeline(user_input: str) -> str:

    #Normalização da pergunta traduzida
    query = input_normalization(user_input)

    logging.info(f"\n\nPergunta do usuário: {query}")

    #Buscar o filme no banco vetorial
    data = search_answer(query)

    logging.info(f"\nDados do Retrieve: {data}")

    #Gerar a resposta do modelo
    response = response_model(query,data)

    logging.info(f"\nResposta da LLM: {response}\n\n")

    #Tradução da resposta da llm
    translation_response = translation_response_model(response)

    return translation_response 