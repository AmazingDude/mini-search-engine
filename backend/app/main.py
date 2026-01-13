"""
FastAPI Entry Point
--------------------
This is where you create your FastAPI app and define API endpoints.

Endpoints to implement:
- GET  /           → Health check
- POST /index      → Build/rebuild the search index
- GET  /search     → Search for documents
"""

from fastapi import FastAPI

# TODO: Import your modules
# from app.indexer.indexer import ...
# from app.search.search import ...

app = FastAPI(title="Mini Search Engine", version="1.0.0")


@app.get("/")
def health_check():
    """Health check endpoint"""
    # TODO: Return a simple status message
    pass


@app.post("/index")
def build_index():
    """
    Build the search index from documents.

    TODO:
    1. Load documents from data/documents.json
    2. Call your indexer to build the inverted index
    3. Return success message with stats
    """
    pass


@app.get("/search")
def search(q: str):
    """
    Search for documents matching the query.

    Args:
        q: The search query string

    TODO:
    1. Preprocess the query (tokenize, clean)
    2. Look up terms in the inverted index
    3. Score and rank results
    4. Return ranked list of documents
    """
    pass
