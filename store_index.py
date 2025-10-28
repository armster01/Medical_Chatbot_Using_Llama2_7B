from src.helper import load_pdf_files, filter_to_minimal_docs, text_split, download_embeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

if not PINECONE_API_KEY:
    raise ValueError("PINECONE_API_KEY not found in environment variables")

# Set Pinecone API key
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

# Index configuration
index_name = "medical-bot-llama2-7b"
dimension = 384
metric = "cosine"
spec = ServerlessSpec(cloud="aws", region="us-east-1")

# Create index if it doesn't exist
if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=dimension,
        metric=metric,
        spec=spec
    )

# Load and process documents
extracted_data = load_pdf_files("data")
minimal_docs = filter_to_minimal_docs(extracted_data)
text_chunk = text_split(minimal_docs)

# Download embeddings
embedding = download_embeddings()

# Create and populate the vector store
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunk,
    embedding=embedding,
    index_name=index_name
)

print(f"Index '{index_name}' has been created and populated with {len(text_chunk)} document chunks.")