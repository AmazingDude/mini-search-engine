# 🔍 Mini Search Engine

> A from-scratch implementation of a search engine to learn data structures, algorithms, and information retrieval concepts.

**Tech Stack:** React + Python (FastAPI) + Custom Inverted Index

![Status](https://img.shields.io/badge/status-active-success.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![React](https://img.shields.io/badge/react-18+-61dafb.svg)

---

## 🚀 New Here? Start Here!

**👉 [START-HERE.md](START-HERE.md) - Begin your journey with a 5-minute quick start!**

---

## 📖 Quick Start

```bash
# 1. Install Python dependencies
cd server
pip install -r requirements.txt

# 2. Start backend
uvicorn app:app --reload

# 3. Load data (in new terminal)
python load_data.py

# 4. Install frontend dependencies (in new terminal)
cd client/mini-search-engine
npm install

# 5. Start frontend
npm run dev

# 6. Open browser at http://localhost:5173
```

**⚠️ First time?** Read [START-HERE.md](START-HERE.md) or [SETUP.md](SETUP.md) for detailed instructions.

---

## 📚 Documentation

| Document                               | Description                                    |
| -------------------------------------- | ---------------------------------------------- |
| **[START-HERE.md](START-HERE.md)**     | 🎯 **New users start here!** 5-min quick start |
| **[INDEX.md](INDEX.md)**               | 📖 Complete documentation navigation guide     |
| **[QUICKREF.md](QUICKREF.md)**         | ⚡ One-page quick reference cheat sheet        |
| **[CHECKLIST.md](CHECKLIST.md)**       | ✅ Track your setup & learning progress        |
| **[SETUP.md](SETUP.md)**               | 🚀 Step-by-step setup instructions             |
| **[GUIDE.md](GUIDE.md)**               | 📘 Complete project documentation              |
| **[STRUCTURE.md](STRUCTURE.md)**       | 🏗️ Project structure & architecture            |
| **[ALGORITHMS.md](ALGORITHMS.md)**     | 🧠 How the search algorithms work              |
| **[WORKFLOW.md](WORKFLOW.md)**         | 🔄 Complete user & data flow diagrams          |
| **[VISUAL-GUIDE.md](VISUAL-GUIDE.md)** | 🎨 UI design and visual examples               |
| **[SUMMARY.md](SUMMARY.md)**           | ✅ Project deliverables & highlights           |

**New here?** Read [START-HERE.md](START-HERE.md) then [INDEX.md](INDEX.md) for guided reading paths.

---

## ✨ Features

✅ **Custom Inverted Index** - No external search libraries
✅ **Text Preprocessing** - Tokenization, normalization, stopword removal
✅ **TF Scoring** - Term frequency ranking
✅ **TF-IDF Ready** - Advanced scoring available
✅ **RESTful API** - FastAPI with OpenAPI docs
✅ **Modern UI** - React + Vite frontend
✅ **Large Dataset** - 247k+ web pages indexed

---

## 🎯 What You'll Learn

-   **Data Structures** - Hash maps, inverted index
-   **Algorithms** - Text processing, ranking, sorting
-   **Information Retrieval** - TF, TF-IDF, document scoring
-   **Backend Development** - FastAPI, REST APIs
-   **Frontend Development** - React, async data fetching
-   **System Design** - Modular architecture

---

## 🏗️ Architecture

```
┌─────────────────┐
│  React Frontend │ ← User Interface
└────────┬────────┘
         │ HTTP
         ↓
┌─────────────────┐
│ FastAPI Backend │ ← API Layer
│                 │
│  Preprocessor   │ ← Text cleaning
│  Indexer        │ ← Inverted index
│  Searcher       │ ← Ranking logic
└─────────────────┘
         ↓
┌─────────────────┐
│   247k Docs     │ ← Dataset
└─────────────────┘
```

---

## 🎮 Try It Out

**Example Queries:**

-   `python programming`
-   `web development`
-   `machine learning`
-   `react javascript`

---

## 🧪 Testing

```bash
# Test modules
cd server
python test_modules.py

# Test API
python test_api.py

# Check dependencies
python ../start.py
```

---

## ⚙️ Configuration

Edit `server/config.py`:

```python
USE_TFIDF = True           # Switch to TF-IDF scoring
REMOVE_STOPWORDS = False   # Keep stopwords
DEFAULT_RESULT_LIMIT = 20  # More results per page
```

---

## 📊 API Endpoints

| Endpoint            | Method | Description         |
| ------------------- | ------ | ------------------- |
| `/`                 | GET    | Health check        |
| `/index`            | POST   | Build/rebuild index |
| `/search?q={query}` | GET    | Search documents    |
| `/stats`            | GET    | Index statistics    |

**API Docs:** http://localhost:8000/docs (when running)

---

## 🔮 Future Enhancements

-   [ ] Phrase search ("exact match")
-   [ ] Boolean operators (AND, OR, NOT)
-   [ ] Stemming (running → run)
-   [ ] Fuzzy matching / typo tolerance
-   [ ] Query suggestions
-   [ ] Persistent storage
-   [ ] Caching layer
-   [ ] Pagination

---

## 🤝 Contributing

This is a learning/portfolio project. Feel free to:

-   Fork and experiment
-   Suggest improvements
-   Add features
-   Report issues

---

## 📝 License

MIT - Feel free to use for learning and portfolios

---

## 🙏 Acknowledgments

Built as a hands-on learning project to understand search engine fundamentals without using Elasticsearch, Solr, or other search libraries.

---

## 📞 Questions?

-   Check [SETUP.md](SETUP.md) for installation help
-   Read [ALGORITHMS.md](ALGORITHMS.md) to understand how it works
-   See [GUIDE.md](GUIDE.md) for complete documentation

---

**Happy Searching!** 🚀
