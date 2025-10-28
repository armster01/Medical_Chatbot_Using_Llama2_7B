# Medical Chatbot Using Llama 2 (7B)

## 🧠 Overview

This project is an AI-powered Medical Chatbot built using Llama 2 (7B), designed to provide intelligent responses to medical-related queries. It demonstrates how to integrate Large Language Models (LLMs), LangChain, Vector Databases (Pinecone), and Flask to build an end-to-end conversational medical assistant. The chatbot processes medical documents (e.g., PDFs) to create a knowledge base, allowing users to ask questions and receive contextually relevant answers based on the provided information.

## ✨ Features

- **Document Processing**: Loads and processes PDF documents from a specified directory.
- **Vector Embeddings**: Uses Sentence Transformers to generate embeddings and stores them in Pinecone for efficient retrieval.
- **Conversational AI**: Powered by Llama 2 7B model for generating human-like responses.
- **Web Interface**: Simple Flask-based chat interface for user interaction.
- **Retrieval-Augmented Generation (RAG)**: Combines retrieval from vector database with generative AI for accurate answers.
- **Source Citations**: Returns source documents for transparency.

## 🛠️ Tech Stack

- **Programming Language**: Python 3.10+
- **Framework**: Flask
- **LLM**: Meta Llama 2 7B (GGML quantized)
- **Vector Database**: Pinecone
- **Embeddings**: Sentence Transformers (all-MiniLM-L6-v2)
- **Libraries**: LangChain, CTransformers, PyPDF, PyMuPDF
- **Frontend**: HTML, CSS, JavaScript (Bootstrap)

## 📋 Prerequisites

1. Python 3.10 or higher
2. Access to Llama 2 7B model weights (download the GGML quantized version: `llama-2-7b-chat.ggmlv3.q4_0.bin`)
3. Pinecone account and API key
4. GPU recommended for faster inference (optional but beneficial)

## ⚠️ Ethical & Safety Notes

1. **Not Medical Advice**: This chatbot is for research and educational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment.
2. **Disclaimers**: Always include visible disclaimers in the UI: "Consult a licensed medical professional for any health concerns."
3. **Data Sources**: Use trusted, curated medical sources (peer-reviewed documents, clinical guidelines) for the retrieval corpus.
4. **Transparency**: Expose citations and sources to users for accountability.
5. **Rate Limiting & Monitoring**: Implement rate limits, logging, and human-in-the-loop escalation for high-risk answers.
6. **Privacy**: Ensure user data privacy and comply with relevant regulations (e.g., HIPAA if applicable).

## 🚀 Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/medical-chatbot-llama2.git
   cd medical-chatbot-llama2
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download Llama 2 Model**:
   - Download the GGML quantized model: `llama-2-7b-chat.ggmlv3.q4_0.bin`
   - Place it in the `model/` directory.

5. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory.
   - Add your Pinecone API key:
     ```
     PINECONE_API_KEY=your_pinecone_api_key_here
     ```

6. **Prepare Data**:
   - Place your medical PDF documents in the `data/` directory.

## 📖 Usage

1. **Store Document Embeddings**:
   ```bash
   python store_index.py
   ```
   This will process the PDFs, create embeddings, and store them in Pinecone.

2. **Run the Flask App**:
   ```bash
   python app.py
   ```
   The app will run on `http://localhost:8080`.

3. **Access the Chat Interface**:
   - Open your browser and go to `http://localhost:8080`.
   - Start chatting with the medical chatbot!

## 🏗️ Project Structure

```
medical_chatbot_using_llama/
├── app.py                      # Main Flask application
├── store_index.py              # Script to process and store embeddings
├── experiment.ipynb            # Jupyter notebook for experimentation
├── requirements.txt            # Python dependencies
├── setup.py                    # Package setup
├── tech_stack.txt              # Tech stack summary
├── .gitignore                  # Git ignore file
├── README.md                   # This file
├── data/                       # Directory for PDF documents
│   └── The_GALE_ENCYCLOPEDIA_of_MEDICINE_SECOND.pdf
├── model/                      # Directory for Llama 2 model
│   └── llama-2-7b-chat.ggmlv3.q4_0.bin
├── src/                        # Source code
│   ├── __init__.py
│   ├── helper.py               # Utility functions for PDF processing and embeddings
│   └── prompt.py               # Prompt template for the LLM
├── static/                     # Static files (CSS, JS)
│   └── style.css
└── templates/                  # HTML templates
    └── chat.html
```

## 🔧 Configuration

- **Model Configuration**: Adjust parameters in `app.py` (e.g., `max_new_tokens`, `temperature`).
- **Chunk Size**: Modify `chunk_size` and `chunk_overlap` in `src/helper.py` for document splitting.
- **Retriever Settings**: Change `k` value in `app.py` for number of retrieved documents.

## 🚀 Deployment

### Local Deployment
Follow the usage instructions above.

### Docker Deployment (Optional)
1. Build the Docker image:
   ```bash
   docker build -t medical-chatbot .
   ```
2. Run the container:
   ```bash
   docker run -p 8080:8080 medical-chatbot
   ```

### Cloud Deployment
- Deploy to platforms like Heroku, AWS, or Google Cloud.
- Ensure model files are accessible (consider using cloud storage for large models).
- Set up environment variables securely.

## 🤝 Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -am 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## 🙏 Acknowledgments

- Meta for Llama 2 model
- LangChain for the framework
- Pinecone for vector database
- Hugging Face for embeddings

## 📞 Contact

Adittya Saha - armstersaha8@gmail.com
  Repo Owner - armster01

<img width="1876" height="813" alt="Screenshot 2025-10-28 142729" src="https://github.com/user-attachments/assets/3c84f37f-8ba4-466a-a513-5ae756f7a6c1" />

<img width="1887" height="811" alt="Screenshot 2025-10-28 145858" src="https://github.com/user-attachments/assets/96c3e282-10ee-42a8-a5ba-a582ce13a7c9" />

<img width="1624" height="193" alt="Screenshot 2025-10-28 160642" src="https://github.com/user-attachments/assets/d12d4549-4be9-4d67-b8d8-de50c313bd31" />

<img width="1489" height="282" alt="Screenshot 2025-10-28 164045" src="https://github.com/user-attachments/assets/590dd64b-148e-4a99-ae62-6d8563c04169" />



