from llama_cpp import Llama
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def response_model(question: str, data_movie: str) -> str:

    start_time = time.time()

    model_path = "data/llm/Phi-3.5-mini-instruct-Q5_K_M.gguf"

    # Carrega o modelo
    llm = Llama(
        model_path=model_path, 
        n_threads=8, 
        n_ctx=1024, 
        n_gpu_layers=0
    )

    prompt = f"""
    TASK:
    You are a chatbot that makes a detailed movie recommendation using ONLY the following information:
    {data_movie}

    RULES:
    1.Don't ask questions.
    2.Never recommend a movie that isn't in data_movie.
    3.If the user's question isn't about movies, following the examples below, respond with "Sorry, I don't have that information."

    EXAMPLES OF MOVIE QUESTIONS:
    -Recommend me an action movie set in the Wild West.
    -Tell me a superhero comedy movie.
    -I want an action-adventure movie.
    -Recommend me a sci-fi movie that has dreams and espionage as its theme. 
    """
    
    prompt_model = f"<|system|> {prompt}<|end|><|user|> {question}<|end|><|assistant|>"

    # Configuração do modelo 
    response = llm(
        prompt_model, 
        max_tokens=400, 
        temperature=0.3, 
        top_p=0.9
    )

    end_time = time.time()
    logging.info(f"TEMPO DE EXECUÇÃO LLM: {end_time - start_time:.2f} segundos")

    return(response['choices'][0]['text'].strip())