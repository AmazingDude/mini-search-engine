import { useState } from "react";
import "./App.css";

const API_URL = "http://localhost:8000";

function App() {
    const [query, setQuery] = useState("");
    const [results, setResults] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [stats, setStats] = useState(null);

    const handleSearch = async (e) => {
        e.preventDefault();

        if (!query.trim()) {
            return;
        }

        setLoading(true);
        setError(null);

        try {
            const response = await fetch(
                `${API_URL}/search?q=${encodeURIComponent(query)}&limit=10`
            );

            if (!response.ok) {
                throw new Error("Search failed");
            }

            const data = await response.json();
            setResults(data.results);
            setStats({
                totalResults: data.total_results,
                processingTime: data.processing_time_ms,
            });
        } catch (err) {
            setError(
                "Failed to fetch results. Make sure the backend server is running."
            );
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="app">
            <header className="header">
                <h1>🔍 Mini Search Engine</h1>
                <p className="subtitle">
                    Built with React + FastAPI + Custom Inverted Index
                </p>
            </header>

            <main className="main">
                <form onSubmit={handleSearch} className="search-form">
                    <input
                        type="text"
                        value={query}
                        onChange={(e) => setQuery(e.target.value)}
                        placeholder="Enter your search query..."
                        className="search-input"
                        disabled={loading}
                    />
                    <button
                        type="submit"
                        className="search-button"
                        disabled={loading}
                    >
                        {loading ? "Searching..." : "Search"}
                    </button>
                </form>

                {error && <div className="error">⚠️ {error}</div>}

                {stats && (
                    <div className="stats">
                        Found {stats.totalResults} results in{" "}
                        {stats.processingTime}ms
                    </div>
                )}

                <div className="results">
                    {results.length > 0
                        ? results.map((result) => (
                              <div key={result.doc_id} className="result-card">
                                  <a
                                      href={result.url}
                                      target="_blank"
                                      rel="noopener noreferrer"
                                      className="result-title"
                                  >
                                      {result.title || result.url}
                                  </a>
                                  <p className="result-url">{result.url}</p>
                                  <p className="result-description">
                                      {result.description || result.snippet}
                                  </p>
                                  <span className="result-score">
                                      Score: {result.score.toFixed(4)}
                                  </span>
                              </div>
                          ))
                        : query &&
                          !loading && (
                              <p className="no-results">No results found</p>
                          )}
                </div>
            </main>
        </div>
    );
}

export default App;
