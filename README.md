# MultiPDF Chat App

# Introduction
<p>The MultiPDF Chat App is a Python application that allows you to chat with multiple PDF documents. You can ask questions about the PDFs using natural language, and the application will provide relevant responses based on the content of the documents. This app utilizes a language model to generate accurate answers to your queries. Please note that the app will only respond to questions related to the loaded PDFs.</p>

# How  It Works
<p>The application follows these steps to provide responses to your questions:</p>
1. **PDF Loading:** The app reads multiple PDF documents and extracts their text content.<br>
2. **Text Chunking:** The extracted text is divided into smaller chunks that can be processed effectively.<br>
3. **Language Model:** The application utilizes a language model to generate vector representations (embeddings) of the text chunks.<br>
4. **Similarity Matching:** When you ask a question, the app compares it with the text chunks and identifies the most semantically similar ones.<br>
5. **Response Generation:** The selected chunks are passed to the language model, which generates a response based on the relevant content of the PDFs.<br>

# Dependencies and Installation
 <p>To install the MultiPDF Chat App, please follow these steps:</p>
   1. **Clone the repository to your local machine.**

2. **Install the required dependencies by running the following command:**

    ```
    pip install -r requirements.txt
    ```

3. **Obtain an API key from OpenAI and add it to the `.env` file in the project directory.**

    ```shell
    OPENAI_API_KEY=your_secret_api_key
    ```

## Usage

To use the MultiPDF Chat App, follow these steps:

1. **Ensure that you have installed the required dependencies and added the OpenAI API key to the `.env` file.**

2. **Run the `main.py` file using the Streamlit CLI. Execute the following command:**

    ```
    streamlit run app.py
    ```

3. **The application will launch in your default web browser, displaying the user interface.**

4. **Load multiple PDF documents into the app by following the provided instructions.**

5. **Ask questions in natural language about the loaded PDFs using the chat interface.**

