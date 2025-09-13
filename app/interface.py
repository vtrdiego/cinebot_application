import streamlit as st
import time
from main import run_chatbot_pipeline
import base64

# Caminho de imagens
image_path = "data/images/cinebot.png"
image_ico = "data/images/ico.png"

# Função de streaming da resposta da LLM
def gerar_resposta_streaming(pergunta):

    resposta_llm = run_chatbot_pipeline(pergunta)
    resposta = resposta_llm + " Caso queira a indicação sobre um filme, fique à vontade para perguntar.."

    for palavra in resposta.split():
        yield palavra + " "
        time.sleep(0.08)

# Configurações da página
st.set_page_config(
    page_title="Cinebot - Recomendação de filmes",  
    page_icon=image_ico,                                   
    layout="wide"                                      
)

# Injeção de CSS personalizado
st.markdown(
    """
    <style>
    /* Alinha mensagens do usuário à direita */
    .stChatMessage:has([data-testid="stChatMessageAvatarUser"]) {
        flex-direction: row-reverse;
        text-align: right;
    }

    /* Estiliza e centraliza a logo */
    .logo-container {
        display: flex;
        justify-content: center;
        margin-top: -55px;
        margin-bottom: 40px;
    }
    .logo-container img {
        width: 650px;
    }

    /* Reduz e centraliza a barra de input */
    div[data-testid="stChatInput"] {
        max-width: 50%;
        margin: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Logomarca centralizada
with open(image_path, "rb") as img_file:

    encoded = base64.b64encode(img_file.read()).decode()

st.markdown(
    f"""
    <div class="logo-container">
        <img src="data:image/png;base64,{encoded}" alt="Logo CineBot">
    </div>
    """,
    unsafe_allow_html=True
)

# Inicializa o histórico se ainda não existir
if "historico" not in st.session_state:
    st.session_state.historico = []

# Exibe o histórico do chat
for mensagem in st.session_state.historico:
    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["conteudo"])

# Campo de entrada do usuário
pergunta = st.chat_input(placeholder="Descreva o filme que procura..", max_chars=200)

# Se houver nova pergunta
if pergunta:
    
    # Salva a pergunta no histórico
    st.session_state.historico.append({"role": "user", "conteudo": pergunta})

    # Exibe a pergunta do usuário
    with st.chat_message("user"): 
        st.markdown(pergunta)

    # Espaço para a resposta do assistente
    with st.chat_message("assistant"):
        mensagem_resposta = st.empty()
        mensagem_resposta.markdown("Gerando resposta, aguarde...")  # mensagem temporária

        resposta = ""
        for trecho in gerar_resposta_streaming(pergunta):
            resposta += trecho
            mensagem_resposta.markdown(resposta + "▌")  # cursor de digitação

        # Substitui pelo texto final
        mensagem_resposta.markdown(resposta)

        # Salva a resposta no histórico
        st.session_state.historico.append({"role": "assistant", "conteudo": resposta})