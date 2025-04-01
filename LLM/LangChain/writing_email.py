import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="이메일 작성 서비스입니다📨", page_icon=":robot:")
st.header("이메일 작성기 📨")


def getEmail():
    input_text = st.text_area(
        label="메일 입력",
        label_visibility="collapsed",
        placeholder="메일 내용을 입력해주새요",
        key="input_text",
    )
    return input_text


input_text = getEmail()


# 이메일 변환 작업을 위한 템플릿 정의
query_template = """
메일을 작성해주세요.
작성된 내용을 정중한 표현으로 고쳐주세요
아래는 이메일입니다.
이메일 : {email}
"""

from langchain.prompts import PromptTemplate

# PromptTemplate 인스턴스 생성
prompt = PromptTemplate(input_variables=["email"], template=query_template)

from langchain_community.chat_models import ChatOpenAI


# 언어 모델 호출
def loadLanguageModel():
    llm = ChatOpenAI(temperature=0, model="gpt-4o")
    return llm


# 예시 이메일 표시
st.button("예제를 보여주세요", type="secondary", help="봇이 작성한 메일을 확인해보세요")
st.markdown("###봇이 작성한 메일은 ###")

if input_text:
    llm = loadLanguageModel()
    # 프롬프트 템플릿 및 언어모델을 사용하여 이메일 형식 지정
    prompt_with_email = prompt.format(email=input_text)
    formatted_email = llm.invoke(prompt_with_email).content
    # 서식이 지정된 이메일 표시
    st.write(formatted_email)
