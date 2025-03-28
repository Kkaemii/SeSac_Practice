import streamlit as st
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


st.set_page_config(page_title="🐦🖇️")
text = "🐦🖇️뭐든지 질문하세요~"
st.header(text, divider="rainbow")


def generate_response(input_text):
    llm = ChatOpenAI(temperature=0, model="gpt-4o")
    st.info(llm.invoke(input_text).content)


with st.form("Question"):
    text = st.text_area("질문 입력 :")
    st.form_submit_button("보내기")
    generate_response(text)


# if "messages" not in st.session_state:
#     st.session_state.messages = []

# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# if prompt := st.chat_input("What'up ?!"):
#     with st.chat_message("user"):
#         st.markdown(prompt)
#     st.session_state.messages.append({"role": "user", "content": prompt})
