import os
from PyPDF2 import PdfReader
import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import ChatOpenAI
from langchain.callbacks import get_openai_callback
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


def process_text(text):
    # character Text Splitter를 사용하여 텍스트를 청크로 분할
    text_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len
    )
    chunks = text_splitter.split_text(text)

    # 임베딩 처리 (벡터 변환), 임베딩은 OpenAI모델 사용
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002", api_key=api_key)
    documents = FAISS.from_texts(chunks, embeddings)
    return documents


def main():  # streamlit을 이용한 웹사이트 생성
    st.title("PDF 요약하기")
    st.divider()
    pdf = st.file_uploader("PDF파일을 업로드해주세요", type="pdf")

    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""  # 텍스트 변수에 PDF내용을 저장
        for page in pdf_reader.pages:
            text += page.extract_text()

        documents = process_text(text)
        query = (
            "PDF파일의 내용을 약 5문장으로 간단히 요약해주세요"  # LLM에 PDF요약 요청
        )

        if query:
            docs = documents.similarity_search(query)
            llm = ChatOpenAI(model="gpt-4", api_key=api_key, temperature=0.31)
            chain = load_qa_chain(llm, chain_type="stuff")

            with get_openai_callback() as cost:
                response = chain.run(input_documents=docs, question=query)
                print(cost)

            st.subheader("==요약 결과==")
            st.write(response)


if __name__ == "__main__":
    main()
