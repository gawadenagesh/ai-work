# multi-doc-rag-app

Minimal Retrieval-Augmented Generation (RAG) demo using local PDFs.

Overview
- Loads PDFs from the `data/` directory, splits into chunks, creates embeddings,
  stores them in a Chroma vector DB, and answers user questions with `ChatOllama`.

Quickstart
1. Create a Python environment (recommended `python3.11`):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. (Optional) Install and run Ollama if you intend to use `ChatOllama`.

3. Place your PDF files in the `data/` folder.

4. Run the app:

```bash
python app.py
```

Notes
- The vector DB is persisted to `./chroma_db` after the first run.
- If you change the PDF set and want to rebuild the DB, remove `./chroma_db` and rerun.
- If an answer cannot be found in the documents, the assistant responds "I don't know.".

License
- This demo is provided as-is for learning and experimentation.
