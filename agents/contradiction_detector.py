# agents/contradiction_detector.py
import os
from openai import OpenAI

# Get your key from environment, or set directly.
PERPLEXITY_API_KEY = "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"  # or "YOUR_KEY_HERE"

def detect_contradictions(claim: str) -> list:
    """
    Search the web for research papers or content that appears to
    contradict the given claim, using Perplexity API for real-time
    web search. Returns a list of paper titles and relevant excerpts.
    """
    client = OpenAI(api_key=PERPLEXITY_API_KEY, base_url="https://api.perplexity.ai")

    # Craft a prompt to find scientific papers that contradict your claim.
    # Perplexity will do live web search and extract sources.
    SYSTEM_PROMPT = (
        "You are an expert scientific researcher. Identify recent academic papers or "
        "articles that directly address or contradict the following research claim. "
        "For each, provide the title and a brief excerpt supporting the contradiction. "
        "Only include papers found via real-time web search. Format each as: "
        "Title: [title] | Excerpt: [relevant text]"
    )

    response = client.chat.completions.create(
        model="sonar-reasoning",  # Uses Perplexity's real-time web search model
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": claim},
        ],
        temperature=0.2,
    )

    # Parse the results—these are actual web-search-derived contradictions.
    results = []
    for line in response.choices[0].message.content.strip().split("\n"):
        if "Title:" in line:
            parts = line.split("| Excerpt:")
            title = parts[0].replace("Title:", "").strip()
            excerpt = parts[1].strip() if len(parts) > 1 else ""
            results.append({"title": title, "excerpt": excerpt})

    return results
