import streamlit as st
from rag.chunking import ChunkingStrategy


st.title("RAG Chatbot (Pinecone + LangChain + OpenAI)")
question = st.text_input("Ask a question about the Documents:")

# PDF ingnestion.


# Usage of ChunkingStrategy
if question:
    chunker = ChunkingStrategy()
    chunks = chunker.chunk(question)
    st.write("Chunks:", chunks)


