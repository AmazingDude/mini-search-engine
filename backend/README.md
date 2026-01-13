# 🔍 Mini Search Engine - Backend

Your task: Implement a search engine from scratch!

## 📁 Structure

```
backend/
├── app/
│   ├── main.py           # FastAPI endpoints (start here!)
│   ├── indexer/
│   │   └── indexer.py    # Build inverted index
│   ├── search/
│   │   └── search.py     # Query + ranking logic
│   ├── models/
│   │   └── document.py   # Data structures (optional)
│   └── utils/
│       └── text.py       # Text preprocessing
├── data/
│   └── (put documents.json here)
└── requirements.txt
```

## 🚀 Getting Started

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the server
uvicorn app.main:app --reload

# 3. Open http://localhost:8000/docs to see API
```

## 📋 Implementation Order

1. **Start with `utils/text.py`** - Implement text preprocessing
2. **Then `indexer/indexer.py`** - Build the inverted index
3. **Then `search/search.py`** - Implement search & ranking
4. **Finally `main.py`** - Wire it all together in API endpoints

## 🎯 Tips

-   Each file has TODO comments explaining what to implement
-   Test each module before moving to the next
-   Use `print()` statements to debug
-   The existing `web_crawl_results.json` has 247k documents you can use

## 📚 Key Concepts

**Inverted Index:**

```
{ "python": {"doc1": 2, "doc3": 1}, "web": {"doc2": 3} }
```

Maps terms → documents containing them (with frequency)

**TF Scoring:**

```
score = term_frequency / document_length
```

Higher frequency = more relevant

Good luck! 🚀
