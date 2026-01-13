"""
Document Models
---------------
Define data structures for documents and API responses.

Using Pydantic for data validation (optional but recommended).
You can also use simple dicts if you prefer.
"""

from typing import List, Optional

# Option 1: Using Pydantic (recommended for FastAPI)
# from pydantic import BaseModel
#
# class Document(BaseModel):
#     id: str
#     url: str
#     title: str
#     description: str
#
# class SearchResult(BaseModel):
#     doc_id: str
#     url: str
#     title: str
#     description: str
#     score: float


# Option 2: Using TypedDict (simpler)
# from typing import TypedDict
#
# class Document(TypedDict):
#     id: str
#     url: str
#     title: str
#     description: str


# TODO: Define your document structure
# Choose Option 1 or 2 above, or create your own

pass
