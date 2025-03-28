import streamlit as st
from dotenv import load_dotenv
import os

# 랭체인 모듈 임포트
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_tools_agent, load_tools
from langchain.memory import ConversationBufferMemory
from langchain_community.callbacks import StreamlitCallbackHandler
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_openai import ChatOpenAI

load_dotenv(override=True)


def create_agent_chain(history):
    """
    LangChain 에이전트(Agent)를 생성하는 함수
    - OpenAI 기반 챗 모델 사용
    - 도구(duckduckgo 검색, 위키피디아 검색) 로드
    - 메모리(대화 기록 저장) 활용
    """

    chat = ChatOpenAI(
        model_name=os.environ["OPEN_API_MODEL"],
        temperature=os.environ["OPEN_API_TEMPERATURE"],
    )

    # 사용할 도구 (duckduckgo, 및 wikipedia)
    tools = load_tools(["ddg-search", "wikipedia"])

    # 프롬프트 템플릿 가져오기
    prompt = hub.pull("hwchase17/openai-tools-agent")

    # 대화 기록 저장하는 메모리 설정
    memory = ConversationBufferMemory(
        chat_memory=history, memory_key="chat_history", return_messages=True
    )

    # OpenAI챗 모델과 도구, 프롬프트를 이용해 에이전트 생성
    agent = create_openai_tools_agent(chat, tools, prompt)

    # 에이전트를 실행하는 객체 생성 (대화 기록 포함)
    return AgentExecutor(agent=agent, tools=tools, memory=memory)


# Streamlit 애플리케이션 제목 설정
st.title("langchain-streamlit-app")

# 대화 기록 저장 객체 생성
history = StreamlitChatMessageHistory()

# 이전 대화 내용을 화면에 표시
for message in history.messages:
    st.chat_message(message.type).write(message.content)

# 사용자 입력을 받을 입력창 생성
prompt = st.chat_input("What's up?")

if prompt:
    # 사용자 입력을 화면에 표시
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI응답 처리
    with st.chat_message("assistant"):
        callback = StreamlitCallbackHandler(st.container())
        agent_chain = create_agent_chain(history)
        response = agent_chain.invoke({"input": prompt}, {"callbacks": [callback]})

        st.markdown(response["output"])
##=================================================

# import streamlit as st
# from dotenv import load_dotenv

# from langchain_openai import ChatOpenAI
# from langchain import hub
# from langchain.agents import AgentExecutor, create_openai_tools_agent, load_tools
# from langchain.memory import ConversationBufferMemory
# from langchain_community.callbacks import StreamlitCallbackHandler
# from langchain_community.chat_message_histories import StreamlitChatMessageHistory

# load_dotenv()

# model = st.selectbox("Select LLM Model", ("GPT-4", "GPT-3.5-Turbo"))
# model = model.lower()
# col1, col2 = st.columns(2)
# with col1:
#     temperature = st.slider("Slide Temperature Bar", 0.0, 1.0, 0.1, 0.1)
# with col2:
#     tool = st.selectbox("Select Search Engine", ("ddg-search", "wikipedia"))
# tools = load_tools([tool])
# history = StreamlitChatMessageHistory()
# memory = ConversationBufferMemory(
#     chat_memory=history, memory_key="chat_history", return_messages=True
# )
# chat = ChatOpenAI(model=model, temperature=temperature)


# def create_agent_chain(history):
#     prompt = hub.pull("hwchase17/openai-tools-agent")
#     agent = create_openai_tools_agent(chat, tools, prompt)
#     return AgentExecutor(agent=agent, tools=tools, memory=memory)


# for message in history.messages:
#     st.chat_message(message.type).write(message.content)

# prompt = st.chat_input("What is up?")

# if prompt:
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     with st.chat_message("assistant"):
#         callback = StreamlitCallbackHandler(st.container())
#         agent_chain = create_agent_chain(history)
#         response = agent_chain.invoke(
#             {"input": prompt},
#             {"callbacks": [callback]},
#         )

#         st.markdown(response["output"])

###+====================================================================
# 필요한 패키지 설치
# 아래 명령어를 터미널에서 실행하여 필요한 패키지를 설치합니다.
# pip install streamlit python-dotenv langchain langchain-community langchain-openai duckduckgo-search wikipedia
