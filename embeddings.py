import json
import faiss
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load and structure the knowledge base
with open("knowledge_base.json", "r") as f:
    knowledge_data = json.load(f)

documents = []
for item in knowledge_data:
    content = f"{item['name']}: {json.dumps(item['details'], indent=2)}"
    documents.append(Document(page_content=content, metadata={"type": item["type"], "name": item["name"]}))

# Split text for better retrieval
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = text_splitter.split_documents(documents)

# Use SentenceTransformers for embeddings
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Store embeddings in FAISS
vectorstore = FAISS.from_documents(split_docs, embedding_model)
vectorstore.save_local("faiss_index")

print("Embeddings saved successfully!")
