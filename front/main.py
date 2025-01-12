import streamlit as st
from dotenv import load_dotenv
from process_data import (
    ask_question,
    select_model,
)

load_dotenv()

st.set_page_config(
    page_title='Assitente Financeiro',
    page_icon='📄',
)
st.header('🤖 Assitente Financeiro')

with st.sidebar:
    st.header('Upload de arquivo')

    selected_model = st.sidebar.selectbox(
        label='Selecione o modelo LLM', options=select_model()
    )

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

question = st.chat_input('como posso ajuda?')
# st.chat_message('user').write(question)
# st.chat_message('ai').write('ia')

for message in st.session_state.messages:
    st.chat_message(message.get('role')).write(message.get('content'))

st.chat_message('user').write(question)
st.session_state.messages.append({'role': 'user', 'content': question})

# print(selected_model)
with st.spinner('Buscando resposta...'):
    response = ask_question(model=selected_model, query=question, st=st)

    st.chat_message('ai').write(response)
    st.session_state.messages.append({'role': 'ai', 'content': response})
