"""
Search Module
-------------
Handles query processing and document ranking.

How search works:
1. User enters query: "python programming"
2. Preprocess query: ["python", "programming"]
3. Find candidate docs: docs containing any query term
4. Score each doc: how relevant is it to the query?
5. Rank by score: highest score first
6. Return top results

Scoring algorithms to implement:
- TF (Term Frequency): score = term_count / doc_length
- TF-IDF (advanced): score = TF * log(total_docs / docs_with_term)
"""

from typing import List, Dict, Any


def search(query: str, top_k: int = 10) -> List[Dict[str, Any]]:
    """
    Search for documents matching the query.

    Args:
        query: The search query string
        top_k: Number of results to return

    Returns:
        List of results, each with: doc_id, url, title, description, score

    TODO:
    1. Preprocess the query (use utils/text.py)
    2. Get candidate documents (docs containing query terms)
    3. Score each candidate document
    4. Sort by score (highest first)
    5. Return top_k results with metadata
    """
    pass


def get_candidates(query_terms: List[str]) -> set:
    """
    Find all documents containing at least one query term.

    Args:
        query_terms: List of preprocessed query terms

    Returns:
        Set of document IDs

    TODO:
    1. For each query term, get documents containing it
    2. Combine all doc IDs into a set (union)
    """
    pass


def score_document(doc_id: str, query_terms: List[str]) -> float:
    """
    Calculate relevance score for a document.

    Args:
        doc_id: The document to score
        query_terms: List of preprocessed query terms

    Returns:
        Relevance score (higher = more relevant)

    TODO (TF scoring):
    1. For each query term:
       - Get term frequency in this document
       - Divide by document length (normalize)
       - Add to total score
    2. Return total score

    Formula: score = sum(term_freq / doc_length) for each term
    """
    pass
