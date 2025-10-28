from flask import Flask, render_template, request, jsonify
from src.helper import download_embeddings
from src.prompt import PROMPT
from langchain_pinecone import PineconeVectorStore
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

embedding = download_embeddings()

index_name = "medical-bot-llama2-7b"

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embedding
)

llm = CTransformers(model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
                    model_type="llama",
                    config={'max_new_tokens': 512,
                            'temperature': 0.8})

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True,
    chain_type_kwargs={"prompt": PROMPT}
)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    result = qa({"query": input})
    response = result["result"]
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)