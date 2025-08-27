import tempfile
import streamlit as st
from langchain.chains.conversation.base import ConversationChain
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from streamlit_chat import message
from MyLCH import getOpenAI, getGenAI

st.markdown("Page 8")
st.sidebar.markdown("Clicked Page 8")
memory = ConversationBufferMemory(
    return_messages=True
)
chain = ConversationChain( memory=memory, llm=getOpenAI(), verbose=False)

def conversational_chat(query):  # 문맥 유지를 위해 과거 대화 저장 이력에 대한 처리
    result = chain.predict(input=query)
    st.session_state['chathistory'].append((query, result))
    return result

if 'history' not in st.session_state:
    st.session_state['chathistory'] = []

if 'generated' not in st.session_state:
    st.session_state['chatgenerated'] = ["안녕하세요!  전 당신에 사랑스러운 귀염둥이 입니다. " ]

if 'past' not in st.session_state:
    st.session_state['chatpast'] = ["안녕하세요!"]

# 챗봇 이력에 대한 컨테이너
response_container = st.container()
# 사용자가 입력한 문장에 대한 컨테이너
container = st.container()

with container:  # 대화 내용 저장(기억)
    with st.form(key='Conv_Question', clear_on_submit=True):
        user_input = st.text_input("Query:", placeholder="무엇이든 물어보세요? (:", key='input')
        submit_button = st.form_submit_button(label='Send')

    if submit_button and user_input:
        output = conversational_chat(user_input)

        st.session_state['chatpast'].append(user_input)
        st.session_state['chatgenerated'].append(output)

if st.session_state['chatgenerated']:
    with response_container:
        for i in range(len(st.session_state['chatgenerated'])):
            message(st.session_state["chatpast"][i], is_user=True, key=str(i) + '_user', avatar_style = "fun-emoji", seed = "Nala")
            message(st.session_state["chatgenerated"][i], key=str(i), avatar_style = "bottts", seed = "Fluffy")

