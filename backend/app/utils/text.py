"""
Text Processing Utilities
-------------------------
Functions for cleaning and tokenizing text.

Text preprocessing pipeline:
1. Lowercase: "Hello World" → "hello world"
2. Remove punctuation: "hello, world!" → "hello world"
3. Tokenize: "hello world" → ["hello", "world"]
4. Remove stopwords: ["the", "a", "is"] → [] (optional)
"""

from typing import List

# Common English stopwords (words to ignore)
STOPWORDS = {
    'a', 'an', 'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
    'of', 'with', 'by', 'from', 'is', 'are', 'was', 'were', 'be', 'been',
    'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
    'could', 'should', 'may', 'might', 'must', 'shall', 'can', 'need',
    'it', 'its', 'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she',
    'we', 'they', 'what', 'which', 'who', 'when', 'where', 'why', 'how'
}


def preprocess(text: str) -> List[str]:
    """
    Full preprocessing pipeline.

    Args:
        text: Raw text string

    Returns:
        List of cleaned tokens

    TODO:
    1. Call lowercase()
    2. Call remove_punctuation()
    3. Call tokenize()
    4. Call remove_stopwords() (optional)
    5. Return the cleaned tokens
    """
    pass


def lowercase(text: str) -> str:
    """
    Convert text to lowercase.

    Args:
        text: Input text

    Returns:
        Lowercased text

    TODO: Use Python's .lower() method
    """
    pass


def remove_punctuation(text: str) -> str:
    """
    Remove punctuation from text.

    Args:
        text: Input text

    Returns:
        Text without punctuation

    TODO:
    - Option 1: Use string.punctuation and str.translate()
    - Option 2: Use regex
    - Option 3: Loop through and filter characters

    Hint: import string; string.punctuation gives you all punctuation chars
    """
    pass


def tokenize(text: str) -> List[str]:
    """
    Split text into tokens (words).

    Args:
        text: Cleaned text

    Returns:
        List of tokens

    TODO: Use Python's .split() method
    """
    pass


def remove_stopwords(tokens: List[str]) -> List[str]:
    """
    Remove common stopwords from token list.

    Args:
        tokens: List of tokens

    Returns:
        Filtered list without stopwords

    TODO: Filter out tokens that are in STOPWORDS set
    """
    pass
