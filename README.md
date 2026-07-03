# 🏠 Housing Oracle

An **agentic RAG application** for UK housing information — combining housing law, open-source government data, polls, and statistics into a single, queryable intelligence layer.

---

## Project Structure

```
housing-oracle/
├── data/                       # ← All source data lives here
│   ├── text/                   #   Legislation, policy papers, guidance notes
│   ├── csv/                    #   ONS statistics, polls, price indices
│   └── raw/                    #   Unprocessed source files before cleaning
│
├── src/                        # ← Application source code
│   ├── ingestion/              #   Data loading & chunking pipeline
│   │   ├── text_loader.py      #     Load text documents
│   │   ├── csv_loader.py       #     Load structured CSV data
│   │   └── chunker.py          #     Split docs into retrieval-friendly chunks
│   │
│   ├── vectorstore/            #   Embedding & vector database layer
│   │   ├── embeddings.py       #     Embedding model wrapper
│   │   └── store.py            #     Vector DB interface (ChromaDB / FAISS / etc.)
│   │
│   ├── retrieval/              #   Search & ranking
│   │   ├── retriever.py        #     Hybrid search (vector + keyword)
│   │   └── reranker.py         #     Result re-ranking
│   │
│   ├── agents/                 #   Agentic RAG layer
│   │   ├── orchestrator.py     #     Top-level agent routing & synthesis
│   │   ├── tools.py            #     Callable agent tools
│   │   └── prompts.py          #     System & task prompts
│   │
│   └── config.py               #   Central configuration & path constants
│
├── scripts/                    # ← CLI entry-points
│   ├── ingest.py               #   Run the ingestion pipeline
│   └── query.py                #   Ask the agent a question
│
├── tests/                      # ← Test suite
│   ├── test_ingestion.py
│   ├── test_retrieval.py
│   └── test_agents.py
│
├── notebooks/                  # ← Exploratory Jupyter notebooks
├── .env.example                # ← Required environment variables
├── requirements.txt            # ← Python dependencies
└── .gitignore
```

## Quick Start

```bash
# 1. Clone & enter the repo
git clone <repo-url> && cd housing-oracle

# 2. Create a virtual environment
python -m venv .venv && source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env   # then fill in your API keys

# 5. Add your data
#    Drop text files into  data/text/
#    Drop CSV files into   data/csv/

# 6. Run ingestion
python scripts/ingest.py

# 7. Query the oracle
python scripts/query.py "What are a tenant's rights under Section 21?"
```