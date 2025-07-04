import deepl

auth_key = "6d9fc52e-1e2c-45e7-a7e2-9ecdca2e4bc0:fx" 
translator = deepl.Translator(auth_key)

#Tradução para pergunta do usuário
def translation_user_input(input: str) -> str:
    result = translator.translate_text(input, target_lang="EN-US")
    return result.text

#Tradução para resposta da LLM
def translation_response_model(response: str) -> str:
    result = translator.translate_text(response, target_lang="PT-BR")
    return result.text