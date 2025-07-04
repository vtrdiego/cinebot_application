###### Chatbot de Recomendação de Filmes com IA ######

Este projeto tem como objetivo oferecer uma solução inovadora para recomendação de filmes utilizando um chatbot conversacional baseado em Inteligência Artificial.

A aplicação foi desenvolvida com técnicas de Processamento de Linguagem Natural (NLP) e o modelo RAG (Recuperação Aumentada por Geração). Ao invés de recomendar filmes com base em histórico ou popularidade, o sistema entende descrições livres inseridas pelo usuário e retorna sugestões personalizadas com base no significado do texto.

Para isso, o chatbot transforma a entrada do usuário em embeddings vetoriais, realiza uma busca semântica em um banco de dados com representações vetoriais de filmes, e utiliza um modelo de linguagem (LLM) para gerar uma resposta contextualizada e natural.

O sistema foi construído com tecnologias open source e visa melhorar a experiência do usuário frente ao paradoxo da escolha, oferecendo recomendações mais precisas, naturais e alinhadas ao interesse real descrito em linguagem comum.

###### Funcionalidades ######

- Recomendações personalizadas de filmes via texto descritivo
- Processamento semântico com embeddings (BAAI/bge-base-en-v1.5)
- Banco de dados vetorial com PostgreSQL + PGVector
- Geração de respostas com modelo LLM (Phi-3-mini via `llama-cpp-python`)
- Interface web interativa via Streamlit

###### Tecnologias Utilizadas ######

- Python
- Streamlit
- PostgreSQL + PGVector
- Sentence-Transformers
- llama-cpp-python
- Docker (opcional para ambiente local)

###### BIBLIOTECAS NECESSÁRIAS ######

Caso não tenha as bibliotecas necessárias instaladas, execute o seguinte comando para instalar (recomendado criar um venv):

pip install -r requirements.txt

###### DATASETS ######

A aplicação já vem com um dataset pronto para utilização. 
Caso queira realizar alterações, modificar no arquivo *dataset_processing.py* e executar para criar o novo dataset. Caso contrário, apenas siga os passos abaixo.

###### EXECUTAR A APLICAÇÃO ######

A seguir está o passo a passo de como inicar as configurações necessárias para executar a aplicação:

1) Baixe o modelo atualizado para a seguinte pasta: cinebot_application/data/llm

LINK PARA DOWNLOAD DO MODELO:
https://huggingface.co/bartowski/Phi-3.5-mini-instruct-GGUF/blob/main/Phi-3.5-mini-instruct-Q5_K_M.gguf

2) Ativar o Docker Desktop;

3) Executar o comando abaixo para criar o conteiner Docker com PostgreSQL + PGVector + tabela:
docker-compose up -d

4) Executar o arquivo "insert.py" para inserir os dados no Banco de Dados;

5) Executar a interface do chatbot:
streamlit run app/interface.py

###### Observação ######
Sempre que for utilizar a aplicação, é necessário ativar o conteiner diretamente no Docker.