import ollama
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Initialize embedding model 
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load FAISS index 
vectorstore = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

# System prompt
system_prompt = """
You are a professional customer support AI. Your job is to provide **accurate and helpful** responses using the provided knowledge base.
**DO NOT make up information**. If the answer is unclear, say: "I'm sorry, I don't have that information."
If the user greets you, respond politely with a friendly greeting. If the question is irrelevant or off-topic, kindly inform the user that you can only assist with general queries related to the products.
Ensure all responses are clear, friendly, and professional.
"""


# Chat Function
def chat():
    print("Customer Support AI is running. Type 'bye' to quit.")
    while True:
        query = input("\nYou: ")
        if query.lower() == "bye":
            print("Agent: Goodbye!")
            break
        
        # Retrieve relevant info 
        docs = vectorstore.similarity_search(query, k=2)
        context = "\n\n".join([doc.page_content for doc in docs])

        # Formulate the final prompt
        user_prompt = f"""
        {system_prompt}
        
        **Context from knowledge base:** 
        {context}
        
        **User Question:** {query}
        
        **Response:**
        """

        # Get response from Mistral (via Ollama)
        try:
    
            response = ollama.chat(
            model="mistral:latest",
            messages=[{"role": "user", "content": user_prompt}],
            stream=True
            )
            print("Agent: ", end="", flush=True)  
            for chunk in response:
                print(chunk["message"]["content"], end="", flush=True) 
            print()  
        except Exception as e:
            print(f"Error: {e}. Please check the Ollama setup.")

# Start chatbot
if __name__ == "__main__":
    chat()