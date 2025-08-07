# agents/citation_propagator.py
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables (ignore if .env file doesn't exist)
try:
    load_dotenv(override=True)
except Exception:
    pass  # Ignore errors loading .env file

# Get API key from environment variable
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")
if not PERPLEXITY_API_KEY:
    raise ValueError("PERPLEXITY_API_KEY environment variable is not set. Please set it in your .env file.")

def propagate_citations(contradicted_papers):
    """For each contradicted paper, find recent papers or articles citing it using Perplexity web search."""
    client = OpenAI(api_key=PERPLEXITY_API_KEY, base_url="https://api.perplexity.ai")
    citation_cascades = {}

    for paper in contradicted_papers:
        # Craft a prompt to find papers/articles citing this specific work
        SYSTEM_PROMPT = (
            "You are an expert scientific researcher. Identify any academic papers, articles, web discussions, or blogs that reference or mention the following published work—even informally. For each, provide the title, source, and a brief excerpt or mention pulled from the search result. Format each as: Title: [title] | Source: [link or context] | Excerpt: [relevant text]"
        )

        response = client.chat.completions.create(
            model="sonar-reasoning",  # Or "sonar-small-chat"; experiment for accuracy
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Find papers citing: {paper['title']}"},
            ],
            temperature=0.2,
        )

        # Parse the results—these are actual web-search-derived citations
        citing_papers = []
        for line in response.choices[0].message.content.strip().split("\n"):
            if "Title:" in line:
                parts = line.split("| Excerpt:")
                title = parts[0].replace("Title:", "").strip()
                excerpt = parts[1].strip() if len(parts) > 1 else ""
                citing_papers.append(f"{title}: {excerpt}")

        citation_cascades[paper["title"]] = citing_papers

    return citation_cascades

