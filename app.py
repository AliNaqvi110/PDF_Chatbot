# import libraries
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings, HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from htmlTemplates import css, bot_template, user_template
from langchain.llms import HuggingFaceHub


# get text data from pdfs
def get_pdf_text(docs):
    text=""
    for pdf in docs:                                # for number of  document
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:               # for each document
            text += page.extract_text()             # extracting text
    return text


# get multiple chunks from the text
def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


# get vector
def get_vectorstore(text_chunks):
    # generate embddings
    embeddings =  OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore


# get conversations
def get_conversations(vectorstore):
    # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain


# handle user question
def  handleQuestion(user_question):
    if st.session_state.conversations is not None:  # Check if conversations is not None
        response = st.session_state.conversations({'question': user_question})
        st.session_state.chat_history = response['chat_history']

        for i, message in enumerate(st.session_state.chat_history):
            if i % 2 == 0:
                st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
            else:
                st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)




def main():
    # function to load API keys
    load_dotenv()

    # set layout
    st.set_page_config(page_title="Pdf Chatbot", page_icon=":books")

    # Add css
    st.write(css, unsafe_allow_html=True)

    # initialize session state
    if "conversations" not in st.session_state:
        st.session_state.conversations=None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history=None

    # add header
    st.header("Pdf Chatbot :books")
    user_question = st.text_input("Ask a question about your document")

    if user_question:
        handleQuestion(user_question)

    # Add user and Bot template
    # st.write(user_template.replace("{{MSG}}", "Hi Chatbot"), unsafe_allow_html=True)
    # st.write(bot_template.replace("{{MSG}}", "Hello Buddy"), unsafe_allow_html=True)


    # side bar
    with st.sidebar:
        st.subheader("Your Document")                                                   # Sub Header
        pdf_docs = st.file_uploader("Upload your PDFs", accept_multiple_files=True)     # file Uploader 
        if st.button("Process"):                                                        # button
            
            # Add Spinner
            with st.spinner("Processing"):
                # get pdf text
                raw_text = get_pdf_text(pdf_docs)

                # get text chunks
                text_chunks = get_text_chunks(raw_text)


                # create vector store
                vectorstore = get_vectorstore(text_chunks)

                # create conversations
                st.session_state.conversations = get_conversations(vectorstore)



if __name__ == '__main__':
    main()