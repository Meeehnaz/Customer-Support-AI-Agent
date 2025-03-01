# Customer Support AI Agent

This project implements a **Customer Support AI Agent** using a Retrieval-Augmented Generation (RAG) pipeline. The agent answers common e-commerce questions by retrieving relevant information from a knowledge base and generating responses using the **Mistral** model via **Ollama**.

---

## Approach

The project follows a **Retrieval-Augmented Generation (RAG)** approach, which combines retrieval-based and generative AI techniques. Here’s how it works:

1. **Knowledge Base**:
   - A structured JSON file (`knowledge_base.json`) contains product and policy information.
   - The data is loaded, split into chunks, and embedded using **HuggingFace Sentence Transformers**.

2. **Vector Storage**:
   - The embeddings are stored in a **FAISS** vector store for efficient similarity search.

3. **Retrieval**:
   - When a user asks a question, the system retrieves the most relevant chunks from the knowledge base using FAISS.

4. **Generation**:
   - The retrieved context is passed to the **Mistral** model (via Ollama) to generate a response.
   - The response is streamed in real-time for a smooth user experience.

5. **User Interaction**:
   - A simple command-line interface allows users to interact with the chatbot.

---

## Features

- **RAG Implementation**: Combines retrieval and generation for accurate responses.
- **FAISS Vector Store**: Efficient similarity search for retrieving relevant information.
- **Streaming Responses**: Real-time streaming of AI responses for better interaction.
- **Customizable Knowledge Base**: Easily extendable by modifying `knowledge_base.json`.

---

## Prerequisites

Before running the project, ensure you have the following installed:

1. **Python 3.8+**
2. **Ollama** (for running the Mistral model locally)
3. **Required Python Libraries** (listed in `requirements.txt`)

---

## Installation

### Step 1: Install Python Dependencies
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

### Step 2: Install Ollama Locally
Ollama is used to run the Mistral model locally. Follow these steps to install it:

1. **Download Ollama**:
   - Visit the [Ollama website](https://ollama.ai/) and download the appropriate version for your operating system (Windows, macOS, or Linux).
   - Follow the installation instructions provided on the website.

2. **Pull the Mistral Model**:
   - Once Ollama is installed, open your terminal and run the following command to download the Mistral model:
     ```bash
     ollama pull mistral
     ```

3. **Verify Installation**:
   - Run the following command to ensure Ollama is working:
     ```bash
     ollama run mistral "Hello, world!"
     ```
   - You should see a response from the Mistral model.

---

## Setup

### Step 1: Prepare the Knowledge Base
1. Add your knowledge base data to a JSON file named `knowledge_base.json` in the following format:
   ```json
   [
     {
       "type": "product",
       "name": "UltraPhone X",
       "details": {
         "price": "$799",
         "features": [
           "6.5\" OLED display",
           "128GB storage",
           "12MP camera",
           "Face Recognition"
         ],
         "colors": ["Black", "Silver", "Blue"],
         "availability": "In stock",
         "warranty": "1-year limited warranty"
       }
     },
     {
       "type": "policy",
       "name": "Shipping Policy",
       "details": {
         "standard_shipping": "3-5 business days - $4.99",
         "express_shipping": "1-2 business days - $12.99",
         "free_shipping": "Orders over $50 qualify for free standard shipping",
         "international_shipping": "Available to select countries for additional fees",
         "po_box_restriction": "Currently not shipping to P.O. boxes"
       }
     }
   ]
   ```

2. Run the `embeddings.py` script to generate the FAISS index:
   ```bash
   python embeddings.py
   ```
   This will create a `faiss_index` folder containing the vector store.

---

### Step 2: Run the Chatbot
1. Start the chatbot by running:
   ```bash
   python agent.py
   ```
2. Interact with the chatbot in the command-line interface. Type `bye` to quit.

---

## Example Conversations

Check the output folder for example conversations showing the agent in action!

---

## Customization

- **Extend the Knowledge Base**: Add more entries to `knowledge_base.json` and regenerate the FAISS index.
- **Change the Model**: Replace `mistral:latest` in `agent.py` with another model.
- **Modify the System Prompt**: Update the `system_prompt` variable in `agent.py` to change the AI's behavior.

---

## Troubleshooting

1. **Ollama Not Responding**:
   - Ensure Ollama is running by checking its status:
     ```bash
     ollama serve
     ```
   - If the Mistral model is not downloaded, run:
     ```bash
     ollama pull mistral
     ```

2. **FAISS Index Not Found**:
   - Ensure you have run `embeddings.py` to generate the FAISS index.

3. **Python Dependency Issues**:
   - Ensure all dependencies are installed by running:
     ```bash
     pip install -r requirements.txt
     ```

