import asyncio
import aiohttp
from aiohttp import ClientTimeout
from bs4 import BeautifulSoup
import json
import os
from urllib.parse import urljoin, urldefrag, urlparse

# 🌱 Seed URLs
seed_urls = [
    "https://www.wikipedia.org/",
    "https://www.nytimes.com/",
    "https://www.bbc.com/",
    "https://www.cnn.com/",
    "https://www.theguardian.com/",
    "https://www.reuters.com/",
    "https://www.stackoverflow.com/",
    "https://www.github.com/",
    "https://www.medium.com/",
    "https://www.quora.com/",
    "https://www.nationalgeographic.com/",
    "https://www.coursera.org/",
    "https://www.edx.org/",
    "https://www.khanacademy.org/",
    "https://www.imdb.com/",
    "https://www.reddit.com/",
    "https://www.wikipedia.org/wiki/Special:Random",
    "https://www.wikimedia.org/",
    "https://www.mozilla.org/",
    "https://www.python.org/"
]

# 💾 Output folder setup
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "web_crawl_results.json")

# 🔧 Config
MAX_PAGES = 50000
MAX_CONCURRENT = 25000
TIMEOUT = 15

visited = set()
results = []

# 📥 Fetch and extract metadata
async def fetch_page(session, url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0 Safari/537.36"
        )
    }
    try:
        async with session.get(url, headers=headers, timeout=ClientTimeout(total=TIMEOUT)) as resp:
            if resp.status >= 500:
                return None

            html = await resp.text(errors="ignore")
            soup = BeautifulSoup(html, "html.parser")

            title = soup.title.string.strip() if soup.title else ""
            desc_tag = soup.find("meta", attrs={"name": "description"})
            description = desc_tag["content"].strip() if desc_tag and "content" in desc_tag.attrs else ""

            new_links = []
            for a in soup.find_all("a", href=True):
                href = a["href"].strip()
                href = urldefrag(href).url
                absolute_url = urljoin(url, href)
                parsed = urlparse(absolute_url)
                if parsed.scheme in ("http", "https"):
                    new_links.append(absolute_url)

            return {
                "url": url,
                "title": title,
                "description": description,
                "links": list(set(new_links))
            }

    except Exception:
        return None

# 🔁 Main crawl logic
async def crawl(seed_urls):
    print(f"🚀 Starting crawl from seeds...")
    queue = list(seed_urls)
    connector = aiohttp.TCPConnector(limit_per_host=MAX_CONCURRENT)

    async with aiohttp.ClientSession(connector=connector) as session:
        while queue and len(visited) < MAX_PAGES:
            url = queue.pop(0)
            if url in visited:
                continue
            visited.add(url)

            result = await fetch_page(session, url)
            if result:
                results.append({
                    "url": result["url"],
                    "title": result["title"],
                    "description": result["description"]
                })

                # Add new links to the queue
                for link in result["links"]:
                    if len(visited) + len(queue) >= MAX_PAGES:
                        break
                    if link not in visited:
                        queue.append(link)

                # Print update every 100 results
                if len(results) % 100 == 0:
                    print(f"💾 {len(results)} pages collected so far...")

                    # Auto-save every 100 results
                    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
                        json.dump(results, f, indent=2, ensure_ascii=False)

        # Final save
        with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)

        print(f"\n✅ Crawl complete! {len(results)} pages saved to {OUTPUT_PATH}")


# ▶️ Run the crawler
if __name__ == "__main__":
    asyncio.run(crawl(seed_urls))
