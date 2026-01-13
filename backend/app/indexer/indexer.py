"""
Indexer Module
--------------
Builds and manages the inverted index.

What is an inverted index?
- A data structure that maps terms to the documents containing them
- Example: {"python": ["doc1", "doc3"], "web": ["doc2", "doc3"]}
- Enables fast lookups: "Which documents contain this word?"

Your tasks:
1. Build an inverted index from a list of documents
2. Store term frequencies (how many times each term appears)
3. Provide methods to look up terms
"""

from typing import Dict, List, Any


# This will store your inverted index
# Structure: { "term": { "doc_id": frequency, ... }, ... }
inverted_index: Dict[str, Dict[str, int]] = {}

# This will store document metadata
# Structure: { "doc_id": { "url": ..., "title": ..., "description": ... }, ... }
documents: Dict[str, Dict[str, Any]] = {}


def build_index(docs: List[Dict[str, Any]]) -> None:
    """
    Build the inverted index from a list of documents.

    Args:
        docs: List of documents, each with keys: id, url, title, description

    TODO:
    1. Clear any existing index
    2. Loop through each document
    3. Get the text content (title + description)
    4. Tokenize and clean the text (use utils/text.py)
    5. Count term frequencies
    6. Add to inverted_index: term -> {doc_id: frequency}
    7. Store document metadata in documents dict
    """
    pass


def get_term_docs(term: str) -> Dict[str, int]:
    """
    Get all documents containing a term.

    Args:
        term: The search term

    Returns:
        Dict mapping doc_id to term frequency
        Example: {"doc1": 3, "doc5": 1}

    TODO: Look up the term in inverted_index
    """
    pass


def get_document(doc_id: str) -> Dict[str, Any]:
    """
    Get document metadata by ID.

    Args:
        doc_id: The document identifier

    Returns:
        Document metadata (url, title, description)

    TODO: Look up the doc_id in documents dict
    """
    pass


def get_stats() -> Dict[str, int]:
    """
    Get index statistics.

    Returns:
        Dict with: total_documents, unique_terms

    TODO: Return counts from your data structures
    """
    pass
