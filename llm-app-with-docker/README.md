# Document Q&A with RAG 🤖📃

A powerful Retrieval-Augmented Generation (RAG) application that allows you to chat with your documents. Built with LlamaIndex, Groq, and Gradio. This application is containerized with Docker for easy deployment.

## ✨ Features

- **Multi-Format Support**: Upload and chat with PDF, DOCX, TXT, CSV, XLSX, PPTX, HTML, and more.
- **Fast Inference**: Powered by Llama 3 (via Groq) for near-instant responses.
- **High-Quality Embeddings**: Uses Mixedbread AI for accurate semantic search.
- **Advanced Parsing**: Utilizes LlamaParse for superior document understanding.
- **Interactive UI**: Clean and responsive chat interface using Gradio.
- **Dockerized**: specific container support for consistent runtime environment.

## 🛠️ Prerequisites

You need the following API keys to run the application:

- **Llama Cloud API Key**: For parsing documents ([Get Key](https://cloud.llamaindex.ai/))
- **Groq API Key**: For LLM inference ([Get Key](https://console.groq.com/))
- **Mixedbread AI API Key**: For embeddings ([Get Key](https://mixedbread.ai/))

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
cd llm-app-with-docker
```

### 2. Configure Environment Variables

Create a `.env` file in the root directory:

```bash
LLAMA_CLOUD_API_KEY="your_llama_cloud_key"
GROQ_API_KEY="your_groq_key"
MXBAI_API_KEY="your_mxbai_key"
```

---

## 🐳 Running with Docker (Recommended)

### Build the Image

```bash
docker build -t docqa .
```

### Run the Container

Run the container passing your environment variables:

```bash
docker run --env-file .env -p 7860:7860 --name docqa-container docqa
```

Alternatively, pass keys individually:

```bash
docker run -e GROQ_API_KEY=your_key -e MXBAI_API_KEY=your_key -p 7860:7860 docqa
```

Access the app at `http://localhost:7860`.

---

## 🐍 Running Locally

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the App

```bash
python app.py
```

## 📂 Project Structure

- `app.py`: Main application logic (Gradio UI + RAG pipeline).
- `Dockerfile`: Docker configuration.
- `requirements.txt`: Python dependencies.
- `.env`: API keys configuration.
