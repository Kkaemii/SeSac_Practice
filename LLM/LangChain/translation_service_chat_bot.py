import streamlit as st
from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

langs = ["Korean", "Japanese", "Chinese", "English"]  # 변역할 언어
left_co, cent_co, last_co = st.columns(3)

# 웹 페이지에서 왼쪽에 언어를 선택할 수 있는 라디오 버튼 생성
with st.sidebar:
    language = st.radio("번역을 원하는 언어를 선택하세요 : ", langs)

st.markdown("### 언어 번역 서비스 입니다. 😎")
prompt = st.text_input("번역을 원하는 텍스트를 입력하세요")  # 텍스트 입력

trans_template = PromptTemplate(
    input_variables=["trans"],
    template="your task is to translate this text to " + language + "TEXT : {trans}",
)  # 해당 서비스가 번역에 대한 것임을 지시

# 메모리는 텍스트 저장
memory = ConversationBufferMemory(input_key="trans", memory_key="chat_history")

llm = ChatOpenAI(temperature=0, model="gpt-4o")
trans_chain = LLMChain(
    llm=llm, prompt=trans_template, verbose=True, output_key="translate", memory=memory
)

# 프롬프트(trans_template)가 있으면 이를 처리하고 화면에 응답을 작성
if st.button("번역"):
    if prompt:
        response = trans_chain({"trans": prompt})
        st.info(response["translate"])
