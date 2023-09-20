# MultiPDF Chat App

# Introduction
<p>The MultiPDF Chat App is a Python application that allows you to chat with multiple PDF documents. You can ask questions about the PDFs using natural language, and the application will provide relevant responses based on the content of the documents. This app utilizes a language model to generate accurate answers to your queries. Please note that the app will only respond to questions related to the loaded PDFs.</p>

# How  It Works
<p>The application follows these steps to provide responses to your questions:</p>

    <ol>
        <li><strong>PDF Loading:</strong> The app reads multiple PDF documents and extracts their text content.</li>
        <li><strong>Text Chunking:</strong> The extracted text is divided into smaller chunks that can be processed effectively.</li>
        <li><strong>Language Model:</strong> The application utilizes a language model to generate vector representations (embeddings) of the text chunks.</li>
        <li><strong>Similarity Matching:</strong> When you ask a question, the app compares it with the text chunks and identifies the most semantically similar ones.</li>
        <li><strong>Response Generation:</strong> The selected chunks are passed to the language model, which generates a response based on the relevant content of the PDFs.</li>
    </ol>
# Dependencies and Installation
 <p>To install the MultiPDF Chat App, please follow these steps:</p>

    <ol>
        <li>Clone the repository to your local machine.</li>
        <li>Install the required dependencies by running the following command:</li>
    </ol>

    <pre><code>pip install -r requirements.txt</code></pre>

    <ol start="3">
        <li>Obtain an API key from OpenAI and add it to the <code>.env</code> file in the project directory.</li>
    </ol>

    <pre><code>OPENAI_API_KEY=your_secret_api_key</code></pre>

    <h3>Usage</h3>

    <p>To use the MultiPDF Chat App, follow these steps:</p>

    <ol>
        <li>Ensure that you have installed the required dependencies and added the OpenAI API key to the <code>.env</code> file.</li>
        <li>Run the <code>main.py</code> file using the Streamlit CLI. Execute the following command:</li>
    </ol>

    <pre><code>streamlit run app.py</code></pre>

    <ol start="3">
        <li>The application will launch in your default web browser, displaying the user interface.</li>
        <li>Load multiple PDF documents into the app by following the provided instructions.</li>
        <li>Ask questions in natural language about the loaded PDFs using the chat interface.</li>
    </ol>
