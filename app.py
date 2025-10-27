import streamlit as st
from openai import OpenAI

modelo = OpenAI(api_key="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") # é o modelo de IA

st.write("### Chatbot com IA") #titulo

# session state é memoria do navegador
# vai ser um dicionario Python
# dicionario = {"quem": "userLevi", "texto":"qualé galera"...}
# "role" - é quem enviou a mensagem
# "content" - é o texto da mensagem (conteúdo) 
if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

# Adicionando uma mensagem na lista: 
# st.session_state["lista_mensagens"].append(mensagem)
#exibir o historico
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content) 

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui:")

if mensagem_usuario: # vai verificar se a variavel existe
    
    st.chat_message("user").write(mensagem_usuario) # user = usuario, assistant = robo
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)


    #respota da IA
    resposta_modelo = modelo.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o"
    )
    resposta_ia = resposta_modelo.choices[0].message.content
    #resposta_ia = "Você quis dizer: " + mensagem_usuario
    
    #exibir a resposta da ia na tela
    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role":"assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)

